# Deployment selection scorecard and ADR

Educational template for a fictional UAE bank. Use synthetic information only. This is distinct from the lab JSON; it records an accountable business and architecture recommendation.

## 1. Decision context

- Workload, data/derivatives and business impact:
- Requirement owner and exact policy version:
- Permitted physical site or country; explain the distinction:
- Connectivity, approved operators and support restrictions:
- Failure scope, RTO and RPO with business rationale:
- Interim manual/degraded operation and authorizing owner:

## 2. Hard-gate inventory

For each alternative, attach all fifteen route declarations, including support, activation, failover and IaC state. Identify location, network path, operator, artifacts, evidence and owner. Record unknowns; keep known conflicts blocked regardless of score. Include normal, degraded, recovery and update operation.

| Alternative | Placement/operator/network conflicts | Recovery conflicts | Missing evidence |
|---|---|---|---|
| Local-private | | | |
| Managed domestic | | | |
| Hybrid | | | |

## 3. Compare admissible alternatives

Define preference weights before ranking. Record evidence-backed performance, operability, portability and cost criteria. If none are admissible or sufficiently specified, record no selection. Explain why invented lab scores/prices are not a real business case. Include cost sensitivity and consistent periods.

## 4. Recovery and exit evidence plan

Name the exact build and topology, failed dependency/domain, restored data consistency, retention/deletion enforcement, identity/registry/network prerequisites, approved recovery target, acceptance criteria, accountable owner and dated retest. Separate the supplied simulation from an actual drill. Include an authorized rebuild/exit target, rights and state-handling plan.

## 5. ADR

Decision and status; alternatives excluded and why; retained risks; assumptions that would reverse the choice; requirement-change authority; test/review owners and dates; evidence links; bounded conclusion. A course score cannot grant production or legal approval.

## PM rubric, 20 points

Policy and lifecycle/admin inventory: 6. Recovery/failure reasoning and separate objectives: 5. Conditional scorecard and economics: 3. Evidence/exit plan with owner and dated test: 4. Clear recommendation and review trigger: 2. Learning threshold 12/20, with every hard conflict corrected or explicitly kept blocked regardless of score. Worked interpretation is in the separate facilitator key.
