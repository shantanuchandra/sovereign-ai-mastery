# Module 10 facilitator solutions and scoring

Separate source-only key; excluded from the public reader build. Educational assessment, not approval of a provider, actual bank, physical site or production architecture.

Total 40 points: Q1–Q5 five each, Q6 fifteen. Learning threshold 24/40; an unresolved physical/operator/network conflict cannot be cleared by the score. PM deliverable separately totals 20 points, threshold 12/20 subject to the same gate.

## Q1. Different dimensions, 5 points

NIST SP 800-145 section 2 defines private cloud by exclusive organizational use while allowing different management and placement arrangements: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf, inspected 27 November 2026. Private does not establish on-site location. On-premises names placement, not every cloud characteristic. Domestic is country-level placement and does not prove BANK-A or enterprise-only administration. Award one point for each distinction and two for applying it to the explicit BANK-A requirement; do not award a legal-compliance conclusion.

## Q2. Full lifecycle and administrative plane, 5 points

Trace prompts/source data, derivatives/embeddings/OCR, outputs, diagnostics/telemetry, training, backup, support, activation/updates, failover, retirement and IaC state. Hybrid's local inference leaves known external support/recovery/state paths. Award two for specific hidden routes, one for derivatives retaining handling rules, one for operator/network review and one for excluding the incompatible proposal. “Encrypted” alone does not repair placement.

## Q3. Separate objectives, 5 points

Failure 10 minus checkpoint 8 gives simulated recovery-point age 2 minutes. Restore 14 minus failure 10 gives simulated interruption 4 minutes, within the invented objectives 2 and 10 respectively. Award two for arithmetic, one for independent gates and two for the simulation limit and real-test needs: exact build, dependency recovery, restored consistency/retention, workload acceptance and approved destinations. No data was actually restored.

## Q4. Infeasible objectives, 5 points

A target at the lost site cannot establish independent site-loss recovery. A target outside BANK-A violates the unchanged placement rule. Escalate the requirement pair to business/security/requirement owners; keep production blocked and seek an explicitly acceptable degraded/manual path or formally changed requirement. Award two for both conflicts, one for ownership, one for interim containment and one for preserving the original policy and retest scope. A country-only change would be a new policy decision.

## Q5. Real documented product, hypothetical application, 5 points

AWS Outposts racks service-link documentation states that a connection to the home Region is necessary and lists management/update traffic: https://docs.aws.amazon.com/outposts/latest/userguide/service-links.html, opening and traffic list, inspected 27 November 2026. That documented connection conflicts with the hypothetical physical-air-gap rule; private transport is still connectivity. This is not a claim about every AWS product, a real bank incident or the exact behavior of all workloads during temporary disconnection. Require the precise supported product/mode, administrative/update/activation paths and evidence against the unchanged rule, or an authorized requirement revision. Award two for source scope, one for transport distinction, one for bounded evidence and one for labeling the application hypothetical. Do not accept a marketing label as proof.

## Q6. Evidence state and RCA, 15 points

1. **Observation/status, 3:** the earlier declaration simulation was REVIEW_REQUIRED, while the untested actual deployment remained UNVERIFIED. A real drill's observed six-minute recovery-point age fails the two-minute criterion: record nonconformance/BLOCKED for release. Seven-minute restoration meeting RTO does not clear RPO. The proposed off-site destination is a second hard conflict, not remediation acceptance.
2. **Direct cause and systemic gap, 3:** investigate stale backup scheduling/configuration and the last application-consistent recoverable point. “Stale job” is the scenario hypothesis; collect timestamps, job outcomes and restored-record evidence rather than asserting every underlying cause is known. The systemic gap is treating a simulated timeline/backup plan as accepted recovery evidence without build/configuration control and separate criteria.
3. **Containment, 2:** retain the failed result, block real-data release and the off-site fallback, preserve forensic evidence without exporting protected data, and invoke only authorized degraded/manual operation.
4. **Owner and mitigation, 3:** platform/backup owner repairs schedule/configuration/alerts; data owner validates restored consistency and retirement rules; security/architecture owner verifies all normal/recovery/support/state destinations; business requirement owner approves objectives or formal policy changes. Ensure the exact candidate build is named.
5. **Retest and closure, 4:** plan a new drill on 30 November 2026, not a claim it has run. Measure separate RTO/RPO, restore correct data, verify retirement/identity/load dependencies and negative tests for prohibited destinations. Review evidence provenance, outcome, scope and dates. A passing bounded drill reaches REVIEW_REQUIRED until accountable acceptance; no blanket sovereignty/legal certification follows. Retain residual whole-site risk and re-open after relevant changes.

## Lab verification and adverse mutations

Default compare output ranks only local-private; the other two are BLOCKED even though their fictional scores are higher. Thirty tests exercise all fifteen purpose boundaries, network/operator changes, unknown/duplicate/missing routes, recovery scope/time/domain, route/event consistency, stale/assumed evidence, malformed inputs and duplicate candidate IDs. A source label such as deployment_test does not authenticate a drill. Country-only changes remove only site restrictions; air-gap/operator gates remain. Same-site recovery under site-loss blocks, and off-site recovery under premises-only blocks.

## PM deliverable rubric and scenario

Policy/inventory 6; recovery/objectives 5; scorecard/economics 3; evidence/exit ownership and dates 4; clear ADR/review trigger 2. Strong work explicitly excludes incompatible candidates, retains unknowns and separates fictional preferences from measured evidence. For the challenge, country-only authorization can remove off-site-within-country conflicts; network connectivity and provider-remote operators remain forbidden when air-gap/enterprise-only restrictions remain. New geography needs new data/control/recovery tests. No factual UAE bank regulatory finding is inferred.
