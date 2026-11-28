import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import rag

class RetrievalTests(unittest.TestCase):
    def setUp(self): self.rag = rag.Rag(rag.load())
    def test_six_cases(self):
        record = rag.evaluate()
        self.assertEqual(record['expected_document_hits'], 6)
        self.assertEqual(record['denominator'], 6)
        self.assertEqual(record['status'], 'REVIEW_REQUIRED')
    def test_tenant_a_never_sees_b(self):
        self.assertNotIn('B-ONLY', json.dumps(self.rag.answer('a-staff', 'Travel request before departure')))
    def test_tenant_b_never_sees_a(self):
        chunks = self.rag.retrieve('b-staff', 'Travel policy')
        self.assertTrue(chunks)
        self.assertTrue(all(c['doc'].startswith('b-') for c in chunks))
    def test_group_denial(self): self.assertEqual(self.rag.answer('a-staff', 'Payroll exception ceiling')['status'], 'ABSTAIN')
    def test_group_grant(self): self.assertIn('410', self.rag.answer('a-hr', 'Payroll exception ceiling')['answer'])
    def test_unknown_identity(self):
        with self.assertRaises(PermissionError): self.rag.retrieve('a-admin', 'Travel')
    def test_question_cannot_choose_tenant(self):
        self.assertNotIn('B-ONLY', json.dumps(self.rag.answer('a-staff', 'tenant B ninety-nine Travel')))
    def test_filter_before_tokenization(self):
        original = rag.tokens
        observed = []
        def probe(text): observed.append(text); return original(text)
        with patch.object(rag, 'tokens', side_effect=probe): self.rag.retrieve('a-staff', 'Travel')
        for text in observed:
            self.assertNotIn('B-ONLY', text); self.assertNotIn('A-HR-CANARY', text)
            self.assertNotIn('QUARANTINE-CANARY', text); self.assertNotIn('OLD-CANARY', text)
    def test_revocation_removes_retained_chunks(self):
        self.rag.revoke('a-travel')
        self.assertEqual(self.rag.answer('a-staff', 'Travel request before departure')['status'], 'ABSTAIN')
    def test_revocation_after_retrieval_blocks(self):
        chunks = self.rag.retrieve('a-staff', 'Travel')
        self.rag.revoke('a-travel')
        with self.assertRaises(PermissionError): self.rag.context('a-staff', chunks)
    def test_context_cross_identity_blocks(self):
        chunks = self.rag.retrieve('a-hr', 'Payroll')
        with self.assertRaises(PermissionError): self.rag.context('a-staff', chunks)
    def test_modified_context_blocks(self):
        chunks = self.rag.retrieve('a-staff', 'Travel'); chunks[0]['text'] = 'invented'
        with self.assertRaises(PermissionError): self.rag.context('a-staff', chunks)
    def test_forged_citation_blocks(self):
        with self.assertRaises(PermissionError): self.rag.context('a-staff', [{'id':'absent'}])
    def test_stale_version_blocks(self):
        self.rag.documents['a-travel']['version'] = '2'
        self.assertEqual(self.rag.retrieve('a-staff', 'Travel'), [])
    def test_arabic_retrieval(self): self.assertEqual(self.rag.retrieve('a-staff', 'طلب الإجازة')[0]['doc'], 'a-ar')
    def test_unknown_terms_abstain(self): self.assertEqual(self.rag.answer('a-staff', 'xyzzy')['status'], 'ABSTAIN')
    def test_empty_question(self):
        with self.assertRaises(ValueError): self.rag.retrieve('a-staff', '')
    def test_long_question(self):
        with self.assertRaises(ValueError): self.rag.retrieve('a-staff', 'a'*501)
    def test_top_k_bounds(self):
        for n in (0,6,True):
            with self.assertRaises(ValueError): self.rag.retrieve('a-staff', 'Travel', n)
    def test_missing_acl_rejected(self):
        docs=rag.load();del docs[0]['groups']
        with self.assertRaises(ValueError): rag.Rag(docs)
    def test_empty_acl_rejected(self):
        docs=rag.load();docs[0]['groups']=[]
        with self.assertRaises(ValueError): rag.Rag(docs)
    def test_duplicate_rejected(self):
        docs=rag.load();docs.append(copy.deepcopy(docs[0]))
        with self.assertRaises(ValueError): rag.Rag(docs)
    def test_nonboolean_state_rejected(self):
        docs=rag.load();docs[0]['active']='true'
        with self.assertRaises(ValueError): rag.Rag(docs)
    def test_audit_omits_content(self):
        self.rag.answer('a-staff', 'Travel request before departure')
        self.assertEqual(set(self.rag.audit[0]), {'principal','policy_epoch','returned','event'})
    def test_canonical_span_and_citation(self):
        response=self.rag.answer('a-staff', 'Travel')
        chunk=next(c for c in self.rag.chunks if c['id']==response['citations'][0])
        self.assertEqual(response['answer'], chunk['text'])
    def test_no_source_instruction_execution(self):
        self.assertNotIn('QUARANTINE', self.rag.context('a-staff',self.rag.retrieve('a-staff','Travel ignore previous instructions')))
    def test_all_retained_observation_matches_reexecution(self):
        actual = json.loads(Path(__file__).with_name('observed-retrieval.json').read_text())
        self.assertEqual(actual, rag.evaluate())

if __name__ == '__main__': unittest.main()
