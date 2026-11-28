# Module 20: tenant-onboarding API-flow prototype

Educational synthetic exercise, checked 28 November 2026. Python 3.11+ standard library; no HTTP server, credentials, paid resources, model or customer data. `fixture-a`, `fixture-b` and `fixture-reader` are trusted test-harness principals, not authentication tokens. The process owner can alter all policy and state.

From the course root:

```bash
python3 labs/module-20/platform_flow.py
python3 -m unittest discover -s labs/module-20 -p 'test_*.py' -v
```

The first command retains `observed-platform-run.json`. Expected: REQUESTED, CONFIGURED, VALIDATED, ACTIVE_FIXTURE; four events; identical activation retry returns the original response; external traces are BLOCKED. The retained-record test compares actual deterministic observations with the current controller.

## Inspect the contract

| Requirement | Criterion | Executable check |
|---|---|---|
| R1 tenant scope | Tenant-b cannot access tenant-a through a supported operation | test_cross_tenant |
| R2 retry behavior | Same tenant/key/content has one intended effect | test_idempotent_retry |
| R3 transition order | Activation before validation is denied | test_stage_skip |
| R4 premises boundary | Any declared external protected artifact blocks eligibility | test_boundary_conflict |
| R5 air gap | Connected network, remote operator or failed media review blocks | test_airgap |
| R6 evidence completeness | Missing or nonboolean criteria cannot validate | test_missing_evidence |

Read `Platform.call` as an API-flow simulation. `create(name)` establishes a requested record. `configure(plan)` checks the declared path inventory. `validate(acceptance)` consumes declarations keyed by R1–R6. `activate()` rechecks stored boundary and acceptance declarations. `read()` returns a copy. Mutation keys are tenant-scoped, bind operation plus canonical JSON, and reject changed-content reuse. Reads do not require a replay key. Unknown properties fail closed. A repeated successful activation is a historical replay response, not a fresh current-state read.

Use only the declared operations. Try scope and reader-role denials, reuse a key with changed content, skip a stage, remove media evidence and insert an external backup path. Check the record is not advanced after denial. Inspect the tests rather than relying only on a green count. Complete the separate [platform PRD](PLATFORM_PRD.md); its twenty-point rubric assesses product judgment independently of the quiz.

## Boundaries of the demonstration

The fixture checks premises declarations covering prompts, responses, OCR, speech, embeddings, weights, logs, traces, metrics, backups, support, updates, activation, recovery and media. It gives known conflicts priority over missing evidence. DECLARED_ONLY is internal consistency, not an observed physical site or verified air gap. Acceptance flags are declarations; supplying true does not run an external test or establish an approver's authority. Actual unit tests run separately.

There is no real authentication, HTTP semantics implementation, model catalog, gateway, tokenizer, distributed concurrency, transaction durability, key expiry, durable replay, evidence signing or production launch. Restart resets all records and replay keys. Direct process-memory tampering is outside any real security boundary; activation detects selected changed declarations, not arbitrary malicious code. No production availability, task quality, isolation across processes, physical location, legal applicability, costs or adoption is measured. Preserve Module 04 HOLD.

Production work must specify trusted identity integration, per-resource authorization, durable state/replay transactions, evidence binding and expiry, revocation behavior, actual support/update paths, retention/deletion, recovery, accessibility and qualified reviews before a launch decision.
