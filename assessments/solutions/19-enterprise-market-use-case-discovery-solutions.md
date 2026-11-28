# Module 19 facilitator solutions

Keep outside the public reader build. Educational, course-derived key, 2026-11-28. Synthetic cases are not researched customers. Independent review NOT COMPLETED; Module 04 HOLD unchanged.

## Knowledge and decision assessment

Total 40 points

Q1–Q5 carry 5 points each, total 25. Q6 carries 15, total 40. The opportunity assessment has its own separate 20-point rubric in `labs/module-19/OPPORTUNITY_ASSESSMENT.md`.

## Q1. buying center, 5 points

An analyst using policy lookup is the end user; a process or department budget owner can be the economic buyer; security/privacy/legal/architecture approve applicable controls; the service operations team runs updates and recovery. Actual role assignments require evidence. Give one point for each role distinction (4), and one for recognizing a positive demo reaction as user-interest evidence rather than purchase authority or commitment (1). Do not assume a CISO holds the business budget.

## Q2. evidence states, 5 points

Missing baseline is UNKNOWN (1): the magnitude of improvement cannot be established (1). A known external telemetry destination violating the authored premises constraint is BLOCKED (1). Neither receives a numeric ranking (1); a known conflict dominates simultaneously missing evidence, with separate collection and redesign tasks retained (1). Assigning zero conceals missingness and creates a misleading comparable score.

## Q3. segments and necessity, 5 points

Identical score inputs yield 3.15 in both eligible fixtures (1). FIN belongs to physical-site and TEL to approved-managed (1). Required versus preferred sovereignty is distinct from desirability (1). FIN needs actual site/operator/support/update/recovery evidence; TEL needs approved configuration/contract/region evidence and existing managed alternatives (1). Their real willingness to pay, baseline value and procurement commitment remain open (1).

## Q4. neutral discovery, 5 points

Examples: “Walk me through the last time you searched for a procedure”; “How did you check it was the current approved version?” Award 1 each for neutral behavior-based questions (2). A test rejects the assistant if it cannot improve time to verified reference while meeting permission/version guardrails (1). Existing indexed search or procedure stewardship is a non-AI alternative (1). Investigate adoption, verification effort, integration and operating effort before claiming savings (1). Thresholds are agreed for the actual study, not invented market norms.

## Q5. real documented product, hypothetical buyer, 5 points

Microsoft's live *Data, Privacy, and Security for Microsoft Copilot*, verified 2026-11-28, states “aren't used to train foundation LLMs” and separately “The stored data includes the user's prompt and Copilot's response” (short extracts also shown in chapter ledger). https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy, organizational data and interaction storage sections. The documented web-search path generates a query sent to Bing. These are provider statements about actual documented behavior; the premises-only customer is invented, not an actual deployment or incident.

Award: distinguish non-training from no processing/storage (1); identify interaction storage and enabled web/agent data paths as separate review questions (1); decline to infer physical-site isolation, operator control or universal legal compliance (1); request exact edition/configuration, contract, all artifact destinations including logs/support/backups/recovery, observed egress and authorized operator evidence (1); preserve hypothetical scope and conditional eligibility pending control-owner review (1). Disabling web search alone cannot establish that every other protected artifact is on-site. A different documented architecture could change eligibility only if it meets the unchanged requirement with relevant evidence.

## Q6. evidence transition and root-cause analysis, 15 points

1. **Pre-test state (1):** eligible on complete synthetic declarations only; no actual facility assurance existed.
2. **Observation (2):** inspection reveals an external telemetry destination and missing baseline. Record the inspected configuration, boundary, timestamp and owner with minimized synthetic evidence. These are separate findings.
3. **State transition (2):** the telemetry declaration becomes contradicted; decision becomes BLOCKED. Baseline becomes UNKNOWN. Conflict dominates and desirability becomes null, including if value is raised to five.
4. **Direct cause (2):** an exporter routes a protected artifact outside the defined site. A score change does not alter this route. Do not claim a real leak occurred without observed payload/egress evidence.
5. **Systemic cause (2):** discovery accepted declarations without path inspection and lacked a baseline provenance gate; the handoff treated a numerical rank as design approval. Distinguish these contributing process gaps from the direct route.
6. **Containment and owner (2):** architecture/operations owner disables or isolates the prohibited route in the teaching design, preserves minimized evidence and blocks further advancement. Product/research owner repairs the baseline investigation; control approver reviews changed design.
7. **Corrective action and retest (2):** redesign collection, dashboards, support, backups and recovery on-site under the unchanged rule. On an explicitly proposed date, e.g. 2026-12-01, inspect configuration and observe all protected egress paths, with negative external-export tests. Collect a relevant baseline with provenance and population. This future retest date is a plan, not a completed result.
8. **Bounded closure (2):** close only after conflict evidence is resolved and baseline evidence complete under the reviewed scope; mark synthetic declaration eligibility separately from actual assurance. Residual risks include unknown support copies, real identity/retention, offline updates, demand and adoption. Otherwise retain BLOCKED or UNKNOWN. No legal or production approval follows automatically.

Give partial credit for correct state reasoning with incomplete roles or retest. A score overriding a prohibited route cannot earn the state-transition points. The proposed value increase treats desirability as permission and fails the exercise.

## Lab verification and interpretation

Actual local run: `python3 labs/module-19/discovery.py`; fixture results retained in `observed-discovery-run.json`. FIN/TEL: ELIGIBLE_FOR_DISCOVERY, 3.15; HEALTH: UNKNOWN, null; GOV/IND: BLOCKED, null. Stable eligible backlog FIN then TEL. Arithmetic: .35×4 + .25×3 + .20×3 + .20×2 = 3.15. Necessity stays separate.

`python3 -m unittest discover -s labs/module-19 -p 'test_*.py' -v` tests fixture states, invalid/missing evidence, every protected route plus extra diagnostics, malformed inventories combined with known operator/network conflicts, media/update rejection, numbers including NaN/infinity/booleans, immutability and retained-run equality. This verifies Python behavior only. Observed states are fixture declarations, not evidence of real interviews, actual region control, air gaps, financial return or market demand.

The separate PM rubric awards 4 points each for buyer/job rights, evidence integrity, eligibility/segmentation, economics/prioritization, and next experiment/handoff. Require revisions for fabricated research, market figures, unsupported compliance, or scoring away conflicts even if other dimensions score well.
