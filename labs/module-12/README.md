# Module 12 lab: authorize evidence before generation

**Educational draft, 28 November 2026. Independent assurance pending.** Only fictional policy text and synthetic identities are used. Two exercises have separate evidence: standard-library vector retrieval with an extractive baseline, and a real local small-model generation. The baseline is not an LLM. The actual generation is not a quality benchmark or production authorization.

## Outcome and prerequisites

Make the unauthorized document ineligible before vector vocabulary, document-frequency calculation, ranking or model context. Preserve tenant/group permissions through chunks; reject deleted, quarantined, changed-version and revoked material. The exercise uses Python 3.13 on macOS arm64; standard-library tests need no installation, account, API or paid resource. The optional generation reuses Module 11's separately prepared pinned model bundle and environment. Preparation and dependency installation are online; do not describe that step as an air gap.

## 1. Inspect and run retrieval

From the repository root:

```bash
python3 -m unittest discover -s labs/module-12 -p 'test_*.py'
python3 labs/module-12/rag.py --output /tmp/module12-my-retrieval.json
```

Choose a fresh output path. Existing observations are never silently overwritten. `documents.json` has six documents: A/B travel, A HR payroll, retired text, quarantined instruction and Arabic leave policy. `cases.json` has six retrieval/abstention expectations. IDs in `PRINCIPALS` represent a trusted identity provider in this fixture. There is no HTTP authentication service or production token validation here; a real caller must never choose its own group/tenant from a query field.

The implementation creates 24-word chunks with four-word overlap. It filters each current source by tenant, permitted group, active/trusted state and matching version before producing sparse TF-IDF vectors. Term frequency weights words; inverse document frequency reduces the weight of common words within the authorized candidate set. Cosine similarity compares normalized vectors. This is a real sparse vector search, not a neural embedding model or approximate-nearest-neighbour index. A 0.08 threshold and top two are teaching constants, not tuned enterprise settings.

Expected retained observation: six of six expected-document-or-abstention cases, with **one Arabic retrieval case**. The observation is `observed-retrieval.json`; it is re-executed and compared exactly by a test. It says nothing about Arabic generation, semantic paraphrases, large datasets or production leakage rates. Two cases exercise expected abstention. No cache or reranker is implemented.

## 2. Test revocation at context construction

```bash
cd labs/module-12
python3 -c "from rag import Rag,load; r=Rag(load()); c=r.retrieve('a-staff','Travel'); r.revoke('a-travel'); r.context('a-staff',c)"
```

Expected: `PermissionError`, with no released context. Run from the root again for subsequent commands. The fixture retains old chunks in memory to show why source deletion/revocation must affect retrieval and final context checks. `context` requires the canonical span, current version and current policy epoch. This is a single-process demonstration, not a distributed atomic transaction; production requires a policy snapshot/lease and a defined policy-change boundary through answer delivery.

## 3. Run actual local generation

Use the Module 11 online preparation instructions first if its bundle is unavailable. Do not download or install anything inside a declared disconnected zone. With the existing teaching environment and model directory, replace paths for your machine:

```bash
python labs/module-12/run_local_model.py /path/to/verified-model /tmp/module12-my-model-run.json
```

The runner verifies the nine local artifacts through Module 11's verifier, checks the pinned model/revision, uses CPU float32 and two threads, refuses custom remote model code, requests local-only loading, sets offline/telemetry library options and denies Python connect/name-resolution functions. Its single authorized travel chunk is supplied to real SmolLM2-135M-Instruct generation. Those process guards are **not** OS isolation, packet-capture evidence or proof about physical premises/native libraries.

Actual retained macOS output, `observed-model-run.json`:

```text
The answer is: 7 days before departure
```

The synthetic source says seven days. The declared exact-answer criterion permits only `seven`, `7`, `seven days` or `7 days`; therefore this actual output **fails the format criterion**, although it contains the correct fact. Raw output is retained and release stays WITHHELD/REVIEW_REQUIRED. Do not reclassify a format failure as a factual error or silently change the metric after seeing the answer. One English generation cannot establish Arabic/model/domain quality or a performance percentile.

## 4. Inspect evidence and adverse tests

Forty-four standard-library tests cover six cases, cross-tenant/group denial, caller/query confusion, authorization before tokenization, quarantine, retained old chunks, immediate revocation, context tampering, version drift, unknown identity/terms, Arabic retrieval, schema/size bounds, content-free audit fields and observed-record consistency. Model-record mutation tests reject invented scores, changed prompt/context/model/fixture, false release, missing hash inventory, nonfinite timing and output-token violations.

`check_record` recomputes record consistency, not execution authenticity or artifact provenance. Re-run the generator to produce new evidence rather than editing retained raw output. No model weights, real credentials or private documents are committed.

## 5. Extend and explain limits

Add an approved corpus source with a different document version; prove stale chunks fail until re-indexed. Add a cache only with principal/tenant/group, query normalization, source version and policy-epoch scope, plus a revocation test. Compare keyword/semantic/hybrid and reranking under the same eligible set; do not retrieve globally and hide forbidden results at display time.

This lab does not implement OCR/parser sandboxing, malware screening, a production identity provider, distributed revocation, neural embedding/reranking, learned grounding or deletion from persisted backups. A `trusted` flag is a fixture declaration, not an injection detector. A malicious instruction in an approved document can still reach the model. The prompt wrapper alone is not an injection defense; least privilege and independent response/action controls remain necessary. Source citations identify supplied chunks; they do not prove every generated claim follows from them.

## PM artifact and acceptance

Complete [REQUIREMENTS.md](REQUIREMENTS.md) with owners and failure evidence. Fixture success permits a teaching demonstration only. Production needs independently tested authentication, authorization at storage/query/context/output, lifecycle propagation, permitted residency paths, qualified task/language assessment, incident handling and accountable approval.
