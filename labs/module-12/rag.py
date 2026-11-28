"""Synthetic permission-aware vector retrieval. No network, neural embeddings or LLM here."""
import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import re
import unicodedata

@dataclass(frozen=True)
class Principal:
    tenant: str
    groups: frozenset

# Authenticated IDs are supplied by this fixed registry, never a question or caller tenant field.
PRINCIPALS = {
    'a-staff': Principal('A', frozenset({'staff'})),
    'a-hr': Principal('A', frozenset({'staff', 'hr'})),
    'b-staff': Principal('B', frozenset({'staff'})),
}

def tokens(text):
    return re.findall(r'\w+', unicodedata.normalize('NFKC', text).casefold())

def allowed(principal, doc):
    return (doc['tenant'] == principal.tenant and doc['active'] and doc['trusted']
            and bool(principal.groups.intersection(doc['groups'])))

def validate_documents(documents):
    if not isinstance(documents, list):
        raise ValueError('Document list required')
    seen = set()
    for doc in documents:
        if not isinstance(doc, dict) or set(doc) != {'id', 'tenant', 'groups', 'version', 'active', 'trusted', 'text'}:
            raise ValueError('Exact document schema required')
        if any(not isinstance(doc[k], str) or not doc[k].strip() for k in ('id', 'tenant', 'version', 'text')):
            raise ValueError('Nonempty string metadata required')
        if doc['id'] in seen or doc['tenant'] not in {'A', 'B'}:
            raise ValueError('Duplicate id or unknown tenant')
        if not isinstance(doc['groups'], list) or not doc['groups'] or any(g not in {'staff', 'hr'} for g in doc['groups']):
            raise ValueError('Explicit permitted groups required')
        if type(doc['active']) is not bool or type(doc['trusted']) is not bool:
            raise ValueError('Boolean lifecycle and source state required')
        seen.add(doc['id'])

class Rag:
    def __init__(self, documents):
        validate_documents(documents)
        self.documents = {d['id']: dict(d, groups=list(d['groups'])) for d in documents}
        self.epoch = 1
        self.audit = []
        self.chunks = []
        for doc in documents:
            words = doc['text'].split()
            for offset in range(0, len(words), 20):
                text = ' '.join(words[offset:offset + 24])
                self.chunks.append({'id': f"{doc['id']}:{offset}", 'doc': doc['id'],
                                    'version': doc['version'], 'text': text})
                if offset + 24 >= len(words):
                    break

    def revoke(self, doc_id):
        self.documents[doc_id]['active'] = False
        self.epoch += 1

    def retrieve(self, principal_id, question, top_k=2):
        if principal_id not in PRINCIPALS:
            raise PermissionError('Unknown authenticated identity')
        if not isinstance(question, str) or not question.strip() or len(question) > 500:
            raise ValueError('Question must have 1–500 characters')
        if type(top_k) is not int or not 1 <= top_k <= 5:
            raise ValueError('top_k must have 1–5 results')
        principal = PRINCIPALS[principal_id]
        # Filter before vocabulary, IDF, scoring, top-k and any generator context.
        candidates = [c for c in self.chunks if allowed(principal, self.documents[c['doc']])
                      and c['version'] == self.documents[c['doc']]['version']]
        counts = [Counter(tokens(c['text'])) for c in candidates]
        vocabulary = set().union(*(set(c) for c in counts)) if counts else set()
        idf = {term: math.log((1 + len(counts)) / (1 + sum(term in c for c in counts))) + 1
               for term in vocabulary}
        def vector(counter):
            values = {term: n * idf[term] for term, n in counter.items() if term in idf}
            norm = math.sqrt(sum(v * v for v in values.values()))
            return {term: v / norm for term, v in values.items()} if norm else {}
        query = vector(Counter(tokens(question)))
        scored = []
        for chunk, count in zip(candidates, counts):
            doc_vector = vector(count)
            score = sum(value * doc_vector.get(term, 0) for term, value in query.items())
            if score >= 0.08:
                scored.append(dict(chunk, score=round(score, 6), epoch=self.epoch))
        results = sorted(scored, key=lambda c: (-c['score'], c['id']))[:top_k]
        # No question, source text, unauthorized result counts or per-document scores in audit.
        self.audit.append({'principal': principal_id, 'policy_epoch': self.epoch,
                           'returned': len(results), 'event': 'retrieval'})
        return results

    def context(self, principal_id, chunks):
        if principal_id not in PRINCIPALS:
            raise PermissionError('Unknown authenticated identity')
        principal = PRINCIPALS[principal_id]
        approved = {c['id']: c for c in self.chunks}
        for chunk in chunks:
            canonical = approved.get(chunk.get('id'))
            if (canonical is None or any(chunk.get(k) != canonical[k] for k in ('doc', 'version', 'text'))
                or chunk.get('epoch') != self.epoch
                or not allowed(principal, self.documents[canonical['doc']])
                or canonical['version'] != self.documents[canonical['doc']]['version']):
                raise PermissionError('Context stale, modified or unauthorized; retrieve again')
        return '\n'.join(f"[{c['id']} v{c['version']}] {c['text']}" for c in chunks)

    def answer(self, principal_id, question):
        chunks = self.retrieve(principal_id, question)
        self.context(principal_id, chunks)
        if not chunks:
            return {'mode': 'extractive baseline; no LLM', 'status': 'ABSTAIN',
                    'answer': 'No authorized evidence found.', 'citations': []}
        # Copies an authorized span, never claims synthesized/model-generated quality.
        return {'mode': 'extractive baseline; no LLM', 'status': 'REVIEW_REQUIRED',
                'answer': chunks[0]['text'], 'citations': [chunks[0]['id']]}

def load():
    return json.loads(Path(__file__).with_name('documents.json').read_text())

def evaluate():
    cases = json.loads(Path(__file__).with_name('cases.json').read_text())
    rag = Rag(load())
    rows = []
    for case in cases:
        response = rag.answer(case['principal'], case['question'])
        if case['expected_document'] is None:
            hit = response['status'] == 'ABSTAIN'
        else:
            hit = any(c.startswith(case['expected_document'] + ':') for c in response['citations'])
        rows.append(dict(case, response=response, expected_document_hit=bool(hit)))
    return {'fixture_sha256': hashlib.sha256(Path(__file__).with_name('documents.json').read_bytes()).hexdigest(),
            'mode': 'permission-aware TF-IDF retrieval + extractive baseline; no LLM',
            'rows': rows, 'expected_document_hits': sum(r['expected_document_hit'] for r in rows),
            'denominator': len(rows), 'status': 'REVIEW_REQUIRED',
            'limits': 'Six synthetic cases; no semantic quality, latency, authentication service or production security claim'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    record = evaluate()
    if args.output:
        if args.output.exists():
            raise SystemExit('Evidence exists; choose a new path')
        args.output.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n')
    else:
        print(json.dumps(record, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
