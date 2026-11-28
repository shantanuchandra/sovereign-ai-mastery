# Module 20 facilitator solutions

28 November 2026. Educational key, separate from reader-facing chapter. Total 40 points. Knowledge/scenario assessment; the PM artifact has its own distinct twenty-point rubric in `labs/module-20/PLATFORM_PRD.md`. No score authorizes launch. Independent assessment NOT COMPLETED; Module 04 HOLD.

## Q1. strategy, feature and outcome (5 points)

A platform strategy identifies a repeated customer job, eligible scope, differentiated approach and choices about effort. A catalog dropdown is a feature. Reduced coordination to a useful supported workload is an outcome, measurable through observed journeys. A falsifier might be that all three pilot teams repeatedly require specialist rescue despite documented onboarding; investigate the actual cause before adding features. Award two for the distinctions, two for an observable outcome/falsifier and one for recognizing the illustrative cohort's limited external validity.

## Q2. scoped acceptance (5 points)

Given the trusted fixture principal mapped to tenant-b and an existing tenant-a record, when the caller invokes read or activate against tenant-a, the controller denies scope before exposing or changing its record. Retain the unchanged record and negative result. This checks the supplied mapping inside one process. It does not establish who the human is, credential validation, trusted tenant assignment, session handling or enforcement across an actual gateway/store. Award two for precondition/action, two for observation/unchanged state and one for identity limits.

## Q3. replay contract (5 points)

The key is scoped to tenant and binds operation plus canonical payload. An identical successful retry returns the retained result without an additional event; changed reuse denies conflict. Different tenants can reuse a textual key independently. Restart erases records and the replay dictionary, so the fixture has no durable duplicate suppression. Historical replay is not fresh current-state attestation. A production design needs atomic durable operations, concurrent request handling, key lifecycle, revocation policy and ambiguous-outcome reconciliation. Award two for scope and identical result, one for changed-content behavior, one for restart and one for rejecting an exactly-once claim.

## Q4. launch measure (5 points)

Example: all approved eligible requests started in a specified pilot month form the cohort; numerator is those reaching a reviewed usable pilot within five working days. Report actual counts, timestamps, full-cohort completion and each paused/abandoned reason. Unapproved and ineligible attempts need separately visible counts rather than silently disappearing. Product owns review; operations and security enforce stop rules for confirmed boundary or authorization incidents. An illustrative 80% goal is not observed adoption, production reliability or a legal measure. Award two for a coherent formula/window, one for exclusions and abandonment visibility, one for owner/action and one for evidence limits.

## Q5. sourced real specification applied to a hypothetical team (5 points)

OpenAPI 3.1.1 describes an interface for HTTP APIs; it can declare operations, inputs, responses and security requirements. A document containing security schemes establishes the authored contract, not runtime object authorization or a tested deployment. The hypothetical team's inference is unsupported. OWASP API1:2023 recommends checks on relevant client-input record-accessing functions. Inspect runtime identity/tenant binding, permitted operations, object/resource checks and direct API calls, including cross-tenant reads and mutations; test data and administrative paths beyond the UI.

Change the decision only with reproducible runtime observations and reviewed enforcement, not a schema badge. Even passing those tests leaves coverage limits, actual deployment configuration, privileged access and physical boundary evidence open. No real OpenAPI customer incident is asserted. Award one for specification scope, one for declaration/enforcement distinction, two for concrete runtime/adverse evidence and one for bounded conclusion.

Sources checked 2026-11-28: OpenAPI Initiative, *OpenAPI Specification* 3.1.1, introduction and Security Scheme/Requirement Objects, https://spec.openapis.org/oas/v3.1.1.html; OWASP API Security Project, *API1:2023 Broken Object Level Authorization*, How To Prevent, https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/. These are primary specification/guidance sources, not independent product assurance.

## Q6. decision and root-cause analysis (15 points)

1. **Preserve the observation (2):** missing identity/media evidence begins UNVERIFIED. A denied tenant-b call establishes that specific fixture scope check passed. ACTIVE_FIXTURE means declarations drove a simulated stage transition; it does not establish a launch or execute an external evidence system. Retain inputs, test outputs and exact plan version.
2. **State transition (2):** external traces and a connected updater under an air gap are known conflicts, so the design is BLOCKED despite other missing evidence. A 92/100 preference score and true acceptance field cannot change this. Keep identity and physical/media evidence separately unresolved.
3. **Direct cause (2):** prohibited paths violate the stated premise. The apparent launch inference is caused by conflating fixture stages/declarations with real control acceptance. If the actual controller was given that conflicting plan, configure/activation should deny; investigate whether the inspection refers to another plan, unprotected mutation, stale evidence or a bypass rather than claiming the tests validated it.
4. **Systemic cause (2):** absent evidence binding, unclear approval authority and score-first prioritization permit a favorable demo to masquerade as approval. Renaming a stage fixes no control. Removing paused tenants changes the measured population and conceals product friction.
5. **Contain and assign (2):** engineering prevents progression and preserves artifacts; operations disables the prohibited exporter/updater in a real affected service under an approved incident procedure; security assesses scope and identity controls; product halts expansion and corrects the KPI contract. Data/qualified privacy/legal owners assess actual handling and obligations if applicable. A simulation itself exported no customer data.
6. **Remediate and retest (3):** on illustrative 4 December 2026, engineering and security rerun both positive and cross-tenant adverse cases against the exact candidate, test replay/concurrency/restarts in the proposed durable implementation, and demonstrate evidence cannot be relabeled or changed after review. Operations supplies observed allowed trace/update paths, offline-media procedure and facility/operator evidence; qualified reviewers accept relevant scope. Record actual date and results, not promised success. A changed implementation requires new evidence and review.
7. **Bounded closure and roadmap (2):** passing fixture controls can close only corresponding bounded behavior defects. Reclassify a removed conflict as UNVERIFIED until its real replacement evidence is accepted. Identity, facility, network, quality, recovery and review gaps remain open. Revise roadmap prerequisites and report full cohort plus paused/abandoned reasons. Launch remains pending until actual gates pass; retain residual risk and named decision authority.

## Scenario challenge and trade-offs

BANK-A requires on-site handling and explicit disconnected operation if air-gapped. No managed remote-support alternative is eligible under that unchanged premise. Recommend a controlled local journey only conditionally on evidence, or report no eligible option. Enterprise-B may assess an approved domestic managed pattern because its stated requirements differ; inspect actual contract, administrator, support, telemetry, updates and recovery paths before recommendation. Neither domestic location nor encryption independently closes all controls. A complete answer shows the changed premise, remaining common review needs and a decision that can be stopped.

## Lab verification and actual observation

Run from course root:

```bash
python3 labs/module-20/platform_flow.py
python3 -m unittest discover -s labs/module-20 -p 'test_*.py' -v
```

Actual retained demo: four ordered stages, four events, identical historical activation retry, external trace BLOCKED and six trace IDs mapped to tests. The 28 tests cover tenant/role denials, key behavior, stages, full artifact conflicts, missing evidence, strict booleans, malformed inventories, changed stored declarations and defensive copies. The retained record equality test checks reproducibility. These observations do not establish authentication, HTTP, durability, actual evidence authority, network isolation or launch readiness. Read the test assertions and current output; a count is not a coverage guarantee.
