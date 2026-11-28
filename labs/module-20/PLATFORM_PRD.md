# Platform PRD: a controlled first workload

Version 0.1 teaching template. 28 November 2026. BANK-A, dates, targets, budgets and staffing below are illustrative; replace them with reviewed evidence before a real commitment. Draft product artifact, not launch approval. Module 04 remains HOLD.

## Decision and strategy hypothesis

For eligible internal read-only document assistants, test whether one documented, supported onboarding journey reduces repeated coordination while preserving BANK-A's physical-premises boundary. Start with one approved model and three synthetic pilot teams. Expand only after the journey and operating burden are understood. The hypothesis is challenged if teams need repeated specialist rescue or cannot explain failures; model catalog breadth is not the primary success measure.

Requester: application developer. Outcome owner: business workload owner. Accountable platform product lead: named learner placeholder to replace. Engineering owns supported interfaces and state; security owns scope/abuse review; operations owns recovery/support; data owners and qualified privacy/legal reviewers assess actual permitted handling. Name an individual for each role in the completed draft, without inventing approval evidence.

## Scope and evidence contract

Initial scope: request, configure, validate and activate one synthetic tenant journey. Later scope: actual identity integration, one supported local inference gateway, workload evaluation, recoverable state and controlled pilot. Excluded initially: autonomous high-impact actions, unrestricted model uploads and public customer access. Revisit each exclusion with a concrete demand and control review.

BANK-A's protected artifacts, support and recovery remain on the physical site. Air gap additionally requires disconnected operation plus reviewed offline updates/media. External paths are BLOCKED. Missing evidence is UNVERIFIED. Complete declarations are DECLARED_ONLY. No score converts one state into another. The actual lab reaches ACTIVE_FIXTURE, which cannot authorize a real service.

## Requirements and acceptance traceability

| ID / owner | Requirement and criterion | Evidence now | Production acceptance gap |
|---|---|---|---|
| R1 / Security | Reject cross-tenant read/mutation before record lookup | test_cross_tenant; fixture scope mapping | Trusted identity; real gateway/storage authorization |
| R2 / Engineering | Identical tenant/key/operation/content replay adds no event; changed reuse denied | test_idempotent_retry and test_idempotency_conflict | Durable atomic replay, concurrency, expiry and restart tests |
| R3 / Engineering | Reject skipped stage without advancing record | test_stage_skip | Durable transitions and administrative change controls |
| R4 / Operations | External declared artifact blocks premises eligibility | test_boundary_conflict | Actual paths, facilities, support, backup and restore evidence |
| R5 / Security/Operations | Connected network/remote operator conflicts with air gap | test_airgap | Observed connectivity; reviewed offline transfer/update procedure |
| R6 / Product/Control owners | Complete strictly boolean fixture criteria needed before validation | test_missing_evidence; test_strict_acceptance | Evidence binding, review authority, expiry and independent results |

Add each real requirement's outcome, version, risk, criterion, implementation reference, test observation, decision and owner. Do not use acceptance true values as test reports. Add model rights, quality slices, support, retention/deletion, accessibility and recovery criteria before moving from synthetic exercise to pilot proposal.

## API journey and launch contract

Document input/output/error examples and state order. Make denied scope, invalid property, missing evidence, invalid transition and replay conflict distinguishable to a permitted developer without disclosing another tenant's content. Document key lifetime and historical replay semantics; a timeout must not invite an uncontrolled repeated effect. Decide suspension, revocation, retirement and recovery journeys with the same care as onboarding.

Launch proposal requires accepted real identity and per-resource access tests; complete workload evaluation; observed allowed paths; tested restore; support/on-call ownership; security and data-owner review; accessible documentation and a rollback/suspension drill. A confirmed forbidden path stops expansion immediately. Actual pilot and production approval remain pending. Preserve failed evidence and owners rather than changing the definition of ready to fit a date.

## Launch KPIs and decision rules

All following numbers are teaching targets, not measured performance or contractual service levels. Pilot window: 1 March–31 March 2027, conditional on gates. Cohort: every approved eligible request started in that window. Keep attempted-but-ineligible, unapproved, paused and abandoned requests visible in separate counts.

| Measure / owner | Definition and illustrative target | Decision on miss |
|---|---|---|
| Permitted onboarding / Product | At least 80% of cohort reaches reviewed usable pilot within five working days; report numerator and denominator | Investigate waiting steps; pause expansion after cohort review |
| Support dependence / Developer experience | At most one specialist intervention per completed journey; count all interventions | Observe repeated confusion and repair workflow/docs |
| Task value / Business owner | At least 80% of twenty distinct approved synthetic tasks meet a prespecified rubric; report language/domain slices | Revisit workload/model; no quality claim from HTTP success |
| Authorization guardrail / Security | Zero confirmed cross-tenant disclosure in defined positive/adverse tests and pilot observations | Contain, suspend affected route, assess scope, retest before expansion |
| Boundary / Operations | No confirmed forbidden path; unknown path evidence remains open | BLOCKED for conflict; UNVERIFIED for absent evidence |
| Operational readiness / Operations | Successful approved restore and suspension drills against declared recovery targets | Delay pilot; retain failed observations |

Specify timestamps, missing data handling and independent task counts. The lab measures none of these KPIs. Do not exclude paused tenants to improve the completion percentage; publish both the full cohort view and explicit reason categories. Instrument with minimized operational metadata and reviewed access/retention.

## Twelve-month conditional roadmap

Illustrative planning window: December 2026–November 2027. These are forward plans, not achieved milestones. Named accountable individuals, estimates and real approvals must be supplied before commitment.

| Window | Outcome and accountable role | Prerequisite / decision gate |
|---|---|---|
| Dec 2026–Feb 2027 | Product + engineering: validate demand, PRD, identity/scope design, local-path inventory, durable prototype | Evidence review; stop if no eligible valuable workload |
| Mar–May 2027 | Operations + workload owner: controlled small pilot, docs, task-quality slices, suspension and restore drills | All pilot gates; March cohort only if ready; stop expansion on leakage/boundary conflict |
| Jun–Aug 2027 | Engineering: add tenant quotas, transparent metering, approved catalog versions and tested support paths | Pilot value and operating burden acceptable; no unresolved critical control gaps |
| Sep–Nov 2027 | Product + operations: expand eligible teams, test substitution/exit, review economics and renew priorities | Capacity, recovery, support and evidence maintained; compare guided alternative |

Order dependencies explicitly: identity before self-service, rights/evaluation before catalog growth, metering definitions before cost dashboards and restore before recovery promises. Reserve capacity for incidents, upgrades and findings. Each phase can end in revise, defer or stop; a date does not override its gate.

## Illustrative economics and assumptions

Planning arithmetic only: 3 staff-months per month × AED 30,000 per staff-month + AED 40,000 monthly infrastructure allocation = AED 130,000 monthly; ×12 = AED 1.56 million. Add an invented 25% contingency for AED 1.95 million total. These are not verified salaries, vendor tariffs or invoices. Replace with quotes and internal allocation policy; show low/high utilization and support-load sensitivity. Include idle capacity, storage, backups, power, patching, review time and exit cost. Compare with the smallest eligible guided service, using measured avoided work and task outcomes.

## Risks, unresolved evidence and review

Current gaps: real identity, durable/concurrent transitions and replay, genuine acceptance evidence, facility/network/operator review, task quality, support workload, load testing, recovery, documentation accessibility and qualified legal/rights assessment. Assign owner, evidence location, target date and stop rule to each. Retain dissent and changes in scope. Independent/different-model and manual accessibility reviews NOT COMPLETED.

## Distinct PM deliverable rubric: 20 points

Award 0–4 per row. Full credit requires the described evidence; half credit for a partly usable draft, zero for absent or contradictory material. This score assesses an educational artifact, not launch authorization.

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Strategy and stakeholders | 4 | Falsifiable customer outcome, repeated job, exclusions and actual role decisions |
| Requirements and boundary | 4 | Trace IDs, observable criteria, hard gate before score, full physical/air-gap inventory and unresolved evidence |
| API journey and operating ownership | 4 | Scope, retries, stage order, error/recovery behavior, actual-vs-fixture limits and named review responsibilities |
| Launch KPIs and acceptance | 4 | Populations, formulas, cohort/window, owner, stop rules, adverse evidence and quality distinct from availability |
| Roadmap and economics | 4 | Twelve conditional months, dependencies, dates/budget labeled illustrative, sensitivity and revisit/exit decision |

A design permitting a known forbidden path must be returned for revision even if other rows score well. The separate forty-point knowledge/scenario key does not add to this rubric.
