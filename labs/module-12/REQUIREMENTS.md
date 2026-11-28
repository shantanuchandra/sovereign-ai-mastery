# RAG requirements and security acceptance record

**Template with fictional worked requirements; 28 November 2026. No deployment approval.** Subject: BANK-A employee policy assistant, physical BANK-A site only. Only approved staff documents; HR text restricted to HR. These are scenario requirements, not a claim about UAE law. Module 04's legal-review HOLD remains separate.

## Decision and architecture alternatives

| Alternative | Admissibility under unchanged boundary | Evidence needed |
|---|---|---|
| On-site retrieval and local model, controlled offline updates | Candidate, not approved | Full-path/facility and access tests |
| On-site generation with external embedding/reranking | BLOCKED | Requires explicit policy change before reconsideration |
| In-country managed RAG/cloud backup | BLOCKED by physical-site rule | A country label does not satisfy the premise |

## Workload and permission contract

Name document owners, approved repositories, tenant identifiers, group mapping authority, parser/version, permitted file types, maximum source/chunk/context sizes, index version, model bundle, retrieval settings and language/domain criteria. Record the trusted authentication issuer and effective service/database roles. Caller-supplied claims and prompt text cannot choose access rights. Define administrator/support exemptions explicitly; do not infer them from a product badge.

| Requirement | Test and expected adverse behavior | Accountable owner |
|---|---|---|
| AUTH-01 | Wrong/missing identity fails closed before any document lookup | Identity lead |
| RET-01 | A query sharing B's exact title never scores B chunks for A | Retrieval lead |
| RET-02 | Staff cannot retrieve HR; HR permission can be revoked | Security lead |
| LIFE-01 | Source deletion, group change or version replacement invalidates chunks and cached context | Data owner |
| CTX-01 | Revocation between retrieval and generation blocks/retries under new policy | Retrieval/security leads |
| GND-01 | Known missing evidence abstains; citations resolve to permitted versioned spans | Product/evaluation lead |
| LANG-01 | Report English/Arabic task and abstention denominators separately | Arabic/domain reviewer |
| LOG-01 | Logs exclude raw prompt/document/output by default; any sampled content has explicit scope/retention/access | Operations lead |
| SITE-01 | No external OCR, embedding, reranking, telemetry, backups, support, activation, update or recovery under unchanged rule | Platform lead |
| INJ-01 | Malicious source cannot grant access, execute tools or bypass independent action approval | Security lead |
| EXIT-01 | Rebuild index/runtime from permitted artifacts on approved hardware, preserve permission semantics and rerun tests | Platform/data leads |

Thresholds for latency, freshness, availability, grounding and refusal must be agreed before evaluation. Proposed teaching thresholds are six retrieval cases expected and zero fixture disclosure; they do not estimate production leakage probability. Add task-representative held-out data, paraphrases, Arabic varieties, malicious sources, delayed ACL events and multitenant concurrency. Record unavailable evidence as UNVERIFIED; one known boundary/access conflict is BLOCKED regardless of score.

## Full data and operating boundary

Inventory source files, parsers/OCR, normalized text, chunks, sparse/neural embeddings, index replicas, reranker requests, prompts, model outputs, diagnostics, crash dumps, telemetry, cache entries, backups, media transfer, update staging, licence activation, support sessions and failover copies. For each, name exact physical destination, operator, access path, retention/deletion, key owner, startup/restart behavior and evidence. Offline preparation occurs in separately authorized staging; use reviewed manifests/media and verify inside the disconnected zone. Do not label the connected teaching laptop physically air-gapped.

## Release record

Current teaching evidence: synthetic retrieval fixture and actual one-English-prompt local generation. Generation factual content is correct but exact-format check fails. No independent production/security/legal/accessibility review is complete. Disposition: **REVIEW_REQUIRED, no production release**. Owners must attach dated evidence and approval; do not tick this template as an automated certification.

## Rubric, 20 points

Award 0–4 each for explicit boundary/alternatives, identity/ACL lifecycle, measurable retrieval/grounding/language criteria, full operations/data-flow controls, and evidence/owner/incident/exit plan. Suggested 12/20 means revise with reviewer; it never overrides a failed hard constraint or grants production permission.
