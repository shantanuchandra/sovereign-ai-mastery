# LLMOps operating model and rollout checklist

Module 17 PM deliverable. Course-authored 20-point rubric, separate from the 40-point knowledge check. Educational draft, 28 November 2026. BANK-A is fictional; no production approval, legal applicability or physical deployment is asserted. Module 04 remains HOLD.

## Decision brief

Fill organization/workload, business outcome, intended users/tenants, physical/data/operator boundary, prohibited paths and decision date. State candidate, current version, target population, fallback behavior and accountable release owner. Separate assumptions, observed facts and missing evidence.

| Bundle component | Exact reference/digest | Evidence owner | Current evidence / expiry |
|---|---|---|---|
| Model/tokenizer/runtime/container | Fill immutable identifiers | Model/platform lead | Pending |
| Prompt/retrieval/corpus/index | Fill versions plus rights review | Retrieval/data lead | Pending |
| Identity/permission/tool policies | Fill revision plus live revocation checks | Security/application owner | Pending |
| Telemetry/storage/retention | Fill allowlist, destinations and operator paths | Operations/privacy | Pending |
| Registry/build/recovery dependencies | Fill provenance and compatibility | Platform/recovery owner | Pending |

Registration is not approval or activation. Map those powers to separate roles and trusted systems; record exceptions, evidence retention and revocation authority. An immutable digest proves identity only, not artifact safety or rights.

## Gate and measurement contract

| Gate | Acceptance evidence | Failure response | Owner / retest date |
|---|---|---|---|
| Hard premises/operator/connectivity | Actual complete-flow evidence, not labels | BLOCK known conflict | Security, fill date |
| Quality/Arabic/domain | Matched independent cases and slice denominators | Withhold missing/failed scope | Product/domain, fill date |
| Permissions/security | Threat-scoped adverse tests and current identity | Deny/revoke affected capability | Security/application, fill date |
| Recovery | Compatible restore, revocation and reconciliation drill | Bounded failure, no blind rollback | Operations, fill date |
| Observability | Producer field allowlist, destination/access/retention test | Stop prohibited exporter | Privacy/operations, fill date |

Define each service indicator: user-visible outcome, numerator, denominator, window, latency threshold, missing-data handling, delayed events, sample selection and tenant/language breakdown. List quota denials separately. Define target, error-budget formula and incident thresholds. Synthetic lab example: nine good of ten admitted, target95%, budget.5 bad events, one bad event consumes2×. This is not a production reliability estimate or SLA.

## Rollout and incident checklist

- Verify release reference equals the tested/approved bundle and current policy. Identify approver and permitted change window.
- Bound canary/shadow traffic and approve all additional data copies. Specify stop and recovery triggers.
- Inspect metrics, logs, traces, alert payloads, support, updates, activation, backups, failover and removable media; record administration paths.
- Confirm current eligibility of fallback, including revoked artifacts, database/index compatibility and permitted operating boundary.
- Name incident commander, technical owner and communication lead. Keep facts, hypotheses and unknown downstream outcomes distinct.
- Freeze discretionary changes on agreed budget exhaustion; contain security/boundary violations immediately according to the incident plan.
- Record actual rollback/restore result and tenant reconciliation. A serving-pointer switch cannot undo leaked data or completed tools.
- Set retest dates and owners. Reserve manual/independent accessibility, domain/Arabic, security and production evidence as open until actually completed.

## Resource and cost plan

Specify units collected, token-measurement method, tenant fairness/quotas, CPU/GPU utilization, memory, storage, telemetry ingestion, backups, failed/retried requests and staffing. Distinguish measured units, verified tariffs and allocation assumptions. The lab's tokens are invented and do not establish money, hardware capacity or energy usage. List retention/cost trade-offs and which minimum evidence remains necessary for incidents.

## Scoring and decision

Award 0–4 each for complete immutable bundle and role separation; scoped gates/evidence/status; correct tenant indicators and failure semantics; telemetry/boundary/incident/recovery design; resource model with accountable dated rollout/retest. Total20. Explain each awarded point. Missing qualified independent/production review remains an explicit approval gap regardless of score.

Choose BLOCKED for any known hard conflict, UNVERIFIED for missing required evidence and only a bounded conditional review recommendation when declared/tested requirements pass. The lab result is DECLARED_ONLY. No numerical score overrides the physical boundary or supplies external assurance. Carry the record into Module18 resilience/audit/vendor exit and the capstone.
