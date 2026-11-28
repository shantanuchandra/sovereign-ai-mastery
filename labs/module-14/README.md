# Module 14 lab: an exact-action gate for synthetic tools

**Educational draft.** Build and attack an in-memory ticket gate. This runs real Python authorization/approval logic, with fixed synthetic proposals and narrow mock tools. It does not call an LLM, OAuth server, MCP implementation, network API or enterprise application. Fixture handles named `session-A` and `credential-A` stand in for trusted identity infrastructure; they are public teaching labels, not usable credentials. No private data or paid service is involved.

## Environment and procedure

Python 3.11+ standard library, Apple Silicon or Linux CPU; no packages, GPU, Docker, model download or internet required. Plan 60–90 minutes. The course baseline M4 Pro/16 GB has ample room for this tiny fixture; the actual test environment is recorded in the author audit. No cloud resource needs cleanup.

From the repository root:

```bash
python3 labs/module-14/gated_agent.py
python3 -m unittest discover -s labs/module-14 -p 'test_*.py' -v
```

The demonstration performs four actual control attempts: close without approval is denied; exact approved close completes; replay is denied; cross-tenant resource access is denied. Exactly one synthetic tool call occurs. `observed-control-run.json` retains an observed output; signing keys and grant IDs are random per process, so compare meaning rather than bytes. The file contains no reusable token, approval signature, prompt or ticket body.

## What the program controls

`Action` binds request ID, tenant, initiating user, agent, tool, resource/version, exact parameters and policy revision. Trusted fixture registries resolve sessions to users, user delegation to agents, and opaque credential handles to tenant/agent/audience/scope/expiry. Only `ticket.read` and `ticket.close` exist. Read accepts no parameters; close accepts exactly `{"status":"closed"}`. Extra URLs and shell proposals are rejected.

`approve` is a trusted reviewer-service stand-in. It validates the proposal and ordinary permissions before issuing a grant. Reviewer must be a different eligible actor in the same tenant. The grant records a fingerprint of the canonical action, approver, expiry and random ID, authenticated with HMAC using an ephemeral process key. It is retained in a server-owned registry. The actual human consent interface, authentication and key management are outside this exercise.

`invoke` copies the action, checks permissions and current boundary/policy/resource version, verifies the registered grant/signature, checks reviewer revocation/expiry/action binding, and rejects spent grants. A lock serializes validation and execution inside this process. The program records AUTHORIZED intent before the tool call and COMPLETED after the synthetic return. Missing audit availability blocks execution. Grant/request consumption prevents concurrent replay in this single process.

Audit contains digests, tenant, status and fixed reason codes, never raw parameters, credentials, prompt, ticket body or signature. Digests of predictable inputs are guessable; redaction is not anonymization. The memory list is mutable and lacks retention, external integrity and access controls.

## Boundaries and evidence states

The teaching policy is physical BANK-A site, on-site operators and offline operation. `boundary_state` checks declared placement of prompts, outputs, weights, embeddings, OCR, speech, diagnostics, logs, telemetry, backups, support, activation, updates and recovery, plus controlled offline media review. Any known external path or online/remote mode is BLOCKED even with other evidence missing. Missing fields stay UNVERIFIED. All favorable fields yield DECLARED_ONLY, never certification, acceptance or proof of an actual air gap.

These declarations are deliberately separate from the executable control tests. This program opens no network connection and invokes no subprocess; it does not inspect the OS, other processes, physical connectivity, actual local services, support procedures or transferred artifacts. A connected laptop running it is not an air-gapped facility. A quality score cannot change a boundary decision.

## Mutation exercises

| Mutation | Expected control result | Evidence to inspect |
|---|---|---|
| Change resource/request ID after approval | Denial before tool | Action binding and zero added calls |
| Tamper signature or extend expiry | Denial | Registry plus HMAC checks |
| Execute exactly at expiry | Denial | `now >= expires` |
| Revoke reviewer/delegation/credential scope | Denial | Current trusted registries |
| Increment resource or policy version | Denial | Freshness check |
| Cross-tenant session/credential/resource/reviewer | Denial | Independent tenant checks |
| Run concurrent duplicate writes | One completes, one denied | One actual call |
| Disable audit before invocation | Denial, resource unchanged | No unaudited call |
| Move any protected artifact off site | BLOCKED | Conflict dominates missing evidence |
| Add an external fallback with better score | BLOCKED | Eligibility before preferences |

The 44 unit tests cover these adverse cases and a favorable read/write. Never disable a control merely to make a test green. Keep synthetic fixtures distinct from actual customer permissions.

## Limits and recovery

The process loses all state on restart and generates a new key; old grants become invalid. It does not demonstrate durable idempotency, distributed locks, database isolation, atomic downstream writes, disaster recovery or production exactly-once semantics. No network/OS isolation measurement, packet capture or real credential exchange is claimed.

A real connector may complete a write and lose its response. Record UNKNOWN_OUTCOME, query the authoritative resource using the original request identity, and reconcile before retrying. Production needs durable intent/result records and appropriate downstream idempotency/concurrency controls. The lab's synchronous memory operation has no such external timeout; the chapter discusses that separate design requirement without fabricating a test.

Retain wanted synthetic output; cleanup consists only of deleting your own saved output if no longer needed. Do not remove shared environments or models. Complete the [control-spec](CONTROL_SPEC.md), then return to [Module 14](../../chapters/14-agents-apis-enterprise-integrations.md).
