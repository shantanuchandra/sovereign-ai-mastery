# Module 12 solutions: sovereign RAG systems

**Instructor/assessment material, 28 November 2026. Same-author educational draft; independent assessment pending.** This file is excluded from the public reader build. A public source repository does not provide answer-key confidentiality.

## Q1.

Retrieval returns relevant eligible evidence; the extractive baseline copies an authorized span; generation creates new tokens conditioned on evidence. `rag.py` runs real sparse TF-IDF vector retrieval and copying with no LLM. `run_local_model.py` loads pinned public weights and generates one real English response from permitted context. Neither implies production acceptance. Award 2 for distinguishing retrieval/extraction/generation, 2 for mapping both runs correctly, 1 for the bounded claim: **5 points**.

## Q2.

A forbidden document can displace an allowed one in global top-k. Post-filtering does not undo text sent to ranking/reranking, diagnostics or context, and can leave no allowed evidence even when it existed outside top-k. Derive identity from a trusted boundary and restrict candidates before vocabulary/statistics/scoring. Recheck permission/version when context is assembled. Award 2 for displacement, 2 for exposure paths, 1 for before-scoring restriction: **5 points**.

## Q3.

Bind chunks to source/tenant/group mapping, document version and policy snapshot/epoch. Update effective membership and invalidate or reject queued/cached contexts and responses when revoked. Cache keys need equivalent identity/tenant/access scope and build/policy dependencies; names alone do not demonstrate invalidation. Test revocation before search, between search/context/delivery, warm cache, queued retries and changed source versions. The single-process fixture rejects old-epoch context but does not establish distributed delivery semantics. Award 2 for lifecycle/scope, 2 for adverse tests, 1 for the distributed limitation: **5 points**.

## Q4.

The declared exact-format criterion fails; this does not prove the factual content wrong. Retrieval hit, citation validity, semantic support, answer format and production task behavior are separate metrics. The actual answer contains the correct seven-day value with extra prose, so retain the raw failure and do not change the agreed criterion after seeing it. One English generation does not establish Arabic quality, concurrent latency, leakage rate or a production approval. Award 2 for metric diagnosis, 2 for evidence distinction, 1 for limits: **5 points**.

## Q5.

Inspect whether row security is actually enabled, which policies apply, how permissive/restrictive policies compose and the exact effective connection role. PostgreSQL 18 section 5.9 documents superuser/`BYPASSRLS` bypass and normal owner bypass; owner enforcement has explicit configuration. Test the deployed retrieval route and admin/support/backup paths with tenant/group adversaries. A fixed Python identity registry does not prove PostgreSQL production behavior. This is a product-documentation case, not evidence that any named organization suffered disclosure. Award 2 for roles/exceptions, 2 for actual-path tests, 1 for scope/version: **5 points**.

## Q6.

The previously UNVERIFIED pilot now has an **observed access conflict and external telemetry conflict: BLOCKED for production release**. Five travel passes cannot override either. A redacted display cannot undo earlier forbidden context processing or external copying.

Contain by stopping the affected answer route, disabling external telemetry and all unauthorized fallbacks, restricting incident evidence to authorized responders and invalidating affected caches/queued contexts. Preserve enough scoped incident evidence for investigation; do not multiply raw sensitive logs. Follow the actual organization's incident/notification process with qualified review, rather than inventing legal duties from the fictional scenario.

Confirmed from the scenario: a cached response outlived group revocation and external telemetry copied a protected span. Hypotheses needing tests include missing group scope in cache keys, delayed ACL-event propagation, policy changes not checked at context/delivery, stale source permissions or an overprivileged service role. Do not claim all are proven causes.

Identity lead establishes authoritative group updates and timing. Retrieval/data owners implement permission-filtered search plus version/policy binding. Security lead defines invalidation, least privilege and incident controls. Platform lead removes prohibited diagnostic destinations and proves restart/update/support/recovery paths. Product/evaluation lead approves predeclared language/task/abstention criteria and records failed evidence. An independent accountable reviewer signs the release decision only after evidence review.

Plan a **30 November 2026 retest**, not a claimed completed event: test cold/warm caches, tenants sharing titles, staff/HR adversaries, missing identity, revocation between each request stage including delivery, queued retries, document deletion/version change and absent evidence. Observe actual effective roles and data destinations; prove no external reranker, telemetry, OCR, backup or recovery under the unchanged site rule. Retain failures, owners and exact builds. Improved travel scores leave the pilot BLOCKED while a known boundary conflict remains; fixing conflicts with missing assurance moves to UNVERIFIED/REVIEW_REQUIRED, never automatic approval.

Award 3 for correct before/after disposition, 3 for containment/full paths, 3 for separating confirmed causes/hypotheses, 3 for accountable remediation, 3 for dated adverse retest and residual gaps: **15 points**.

**Total 40 points.** Suggested 24/40 indicates a teaching discussion threshold, not production permission. An answer approving a known access/site violation must be revised even if its arithmetic score reaches the threshold.

## Lab expected evidence and PM rubric

`observed-retrieval.json`: six expected-document-or-abstention cases hit, one Arabic retrieval case, no model inference in that baseline. `observed-model-run.json`: real local SmolLM2 output “The answer is: 7 days before departure”, exact-format failure despite correct numeric fact, withheld release. Forty-four standard-library tests include adverse retrieval and record mutations. A validator establishes file consistency, not execution authenticity or facility isolation.

PM artifact has 20 points, 0–4 each for boundary/alternatives, identity/ACL lifecycle, measurable retrieval/grounding/language criteria, full operational paths, and owners/evidence/incident/exit. Suggested 12/20 never overrides known conflicts. Independent legal, security, domain/language, accessibility and production review remain pending.
