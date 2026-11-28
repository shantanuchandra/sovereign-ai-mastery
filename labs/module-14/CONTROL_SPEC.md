# Agent control-spec, abuse-case register and go/no-go rubric

**Course-authored PM artifact; educational draft, not an official standard.** Example values below describe fictional BANK-A and synthetic maintenance tickets. Replace them with reviewed evidence before any real deployment. Independent security, legal, accessibility and production approval remain NOT COMPLETED.

## Decision record

| Field | Fictional worked example / evidence required |
|---|---|
| Owner, version, date | Product owner; bank-a-v1; 2026-11-28 |
| Permitted outcome | Read own-tenant maintenance state; propose a closure; execute reviewed exact closure |
| Excluded actions | Delete, arbitrary query/shell/URL, payment, credential retrieval, cross-tenant write |
| Operating boundary | Physical BANK-A only; offline; on-site operator; no remote fallback/support |
| Protected artifacts | Prompts/outputs/weights/embeddings/OCR/speech/diagnostics/logs/telemetry/backups/support/activation/updates/recovery |
| Evidence status | Synthetic control tests observed; actual identity, facility and enterprise evidence UNVERIFIED |
| Current disposition | Educational exercise may proceed; enterprise go-live NOT APPROVED |

## Principals, tools and permissions

Identify initiating user, delegated agent, tenant, gateway client and downstream service independently. Derive tenant/user from trusted authentication rather than proposal text. Credential owner: security; audience: ticket-service; scope: read/close separately; expiry/revocation checked at every invocation. Lab labels are fixture handles only.

| Operation | Schema / boundary | Permission and approval |
|---|---|---|
| ticket.read | Own-tenant resource and current version; empty params | Active user delegation, matching agent and read credential; no separate reviewer |
| ticket.close | Own-tenant resource/version; exactly status=closed | Same ordinary checks plus close scope, exact-action single-use grant |
| Unknown operation | Not registered | Denied, no generic fallback |

Reviewer eligibility: separate approver in same tenant, currently authorized. Consent screen must show actor, resource/version, exact changes, consequences and expiry. Require fresh consent after changes. Approval signs/binds tenant, user, agent, tool, resource/version, parameters, request ID and policy revision; grant has ID, approver and expiry. No model claim, conversation Boolean or detached signature substitutes for identity and permission checks.

## Execution and recovery contract

1. Validate typed proposal and trusted identities; reject hard boundary conflicts/missing authority.
2. Check tenant/resource, credential audience/scope/lifetime and delegation.
3. Obtain a reviewer grant for writes; revalidate policy/resource/reviewer at invocation.
4. Atomically reserve the operation/idempotency identity and consume grant in durable production infrastructure.
5. Record authorized intent without raw secrets; invoke the narrow adapter.
6. Record observed result. If response is lost, keep UNKNOWN_OUTCOME and reconcile with the authoritative resource before retrying.
7. Retain tenant-scoped evidence under approved access/retention rules; rotate credentials and invalidate pending grants after relevant changes.

Lab implementation uses one memory lock and an ephemeral key; steps 4–7 require additional production implementation and failure injection. Owner: enterprise application engineering with security and operations. No claim of exactly-once distributed execution.

## Abuse-case register

| Abuse or failure | Control / adverse test | Owner / current status |
|---|---|---|
| Retrieved instruction requests shell/URL | Fixed catalog and strict schemas; reject unknown tools/extra URL | App engineering; lab observed |
| Agent changes resource after review | Canonical binding plus resource version | Security; lab observed |
| Tenant A proposes tenant B resource | Downstream tenant/resource authorization | App owner; lab observed |
| Generic administrator token hides user | Scoped audience/delegation; wrong-audience/scope tests | IAM owner; fixture only, real IAM pending |
| Replayed approval or concurrent request | Single-use grant/request; one-process race test | Platform; durable multi-process test pending |
| Reviewer revoked after issuance | Current eligibility recheck | Security; lab observed |
| Operator edits policy before invocation | Policy revision binding | Product/security; lab observed |
| Audit unavailable before execution | Fail closed with unchanged resource | Operations; lab observed |
| Remote diagnostics exports protected text | Full lifecycle placement gate | Operations/privacy; declaration only |
| Downstream write succeeds, response lost | Unknown outcome, durable reconciliation/idempotency | Enterprise owner; production test pending |
| New tool version adds delete capability | Deployment review and denial regression | Platform owner; production governance pending |

## Test and evidence plan

Retain exact code/tool/schema/policy versions, environment/date, test inventory, actual outcomes, denial counts, action/result fingerprints, owners and retest dates. Use synthetic inputs for exported evidence. Never publish a credential, signature, customer text or raw exception body. Verify all protected paths during startup, normal use, update, degraded operation and restore; declarations are not observed controls.

Dated next review: **2026-11-29**, conditional on access to independent reviewers and a safe test environment. If unavailable, retain NOT COMPLETED and name the gap; do not claim it occurred. Production test plan must cover distributed retries/crashes, identity forgery/revocation, key rotation, tenant offboarding, audit access/tamper, actual OS egress and facility/media recovery. The date is a target, not a completed review.

## Go/no-go rubric

Five criteria, 0–4 each, total 20: scoped identity/delegation; exact tool/resource authorization; approval lifecycle; durable audit/reconciliation; complete boundary/operating evidence. Score 0 absent, 1 declared, 2 designed, 3 observed in bounded tests, 4 independently verified in the target environment. Suggested teaching threshold 15/20 to request review, never automatic approval.

**Hard exclusions:** any prohibited data/operator/network path, unauthorized cross-tenant action, absent applicable rights/qualified sign-off, invalid reviewer/credential or unresolved high-impact unknown outcome. No score overrides these. Missing facility/IAM/durable-store evidence stays UNVERIFIED; an observed violation is BLOCKED. A safe teaching run can finish while the enterprise remains no-go.

## Capstone handoff

Attach the control-spec, abuse register, actual test record, unresolved gaps and named owners to the architecture decision. Feed data and control boundaries, tool definitions, principals, approvals and unknown-outcome cases into Module 15 threat modeling. Do not transform a completed synthetic lab into production acceptance.
