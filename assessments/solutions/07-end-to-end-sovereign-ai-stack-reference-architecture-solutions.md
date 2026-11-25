# Module 07 facilitator solutions and marking rubric

Author-generated educational draft, 25 November 2026. Keep outside the public reader build. Independent assessment NOT COMPLETED. The source repository may remain public; exclusion from reader navigation is not confidentiality.

## Q1. Dependencies (5 points)

Identify external embedding computation and derived data flow (2), backup destination and recovery dependency (1), site-rule conflicts despite a local main model (1), and remediation owners/tests before reconsideration (1). Do not award a “local model means local system” answer.

## Q2. Trust and location (5 points)

Physical site records where components/artifacts exist; trust zone groups authority or isolation assumptions; authorization states which actor can perform an operation (3). NIST SP 800-207's abstract rejects implicit trust based solely on physical/network location (1). Test identities and permissions as well as location; the source does not decide fictional PLANT-A's legal duties (1).

## Q3. Incomplete graph (5 points)

Missing activation/retirement paths mean UNVERIFIED, not an observed boundary breach by themselves (2). Inventory entitlement/identity dependencies, offline start/renewal behavior, deletion scope and retained replicas (2). Obtain build-linked observations, owners and review rather than only adding boxes (1). A later known conflict takes precedence over this gap state.

## Q4. Counterfactual (5 points)

Changing premises to country scope is an explicit requirement change (2). Identify decision authority, remaining country/legal/operational constraints and fresh route tests (2). Rank preferences only after hard gates; a score cannot authorize a policy change or cure a physical conflict (1).

## Q5. Named product, hypothetical customer (5 points)

AWS Outposts racks' service-link guide describes a necessary regional connection, including management/update traffic (2). This contradicts treating the described connected product architecture as proof of a physical air gap (1). Request a precisely identified alternative's architecture, activation/update/support/recovery dependencies and observed disconnected operation; reject marketing substitution for evidence (2). Do not invent a real outage, assume customer-data leakage from the mere existence of a link, or generalize this result to every AWS offering.

Source: AWS, *Connectivity through service link*, Outposts racks user guide, introduction and management-traffic list, https://docs.aws.amazon.com/outposts/latest/userguide/service-links.html. Inspected 2026-11-25. No real deployment tested.

## Q6. Root-cause analysis (15 points)

1. **State/observation (3):** Start UNVERIFIED for undocumented support/recovery. Observed off-site diagnostics and online activation under a physical-air-gap rule mean BLOCKED even while gaps remain. The score has no veto authority.
2. **Direct causes (2):** Diagnostic routing copied protected material outside the site; activation used a prohibited network transport. Treat these as distinct observations. The drawing's omissions did not physically create or fix the routes.
3. **Systemic gap (2):** Happy-path-only architecture review, incomplete lifecycle ownership and acceptance criteria allowed hidden management dependencies. These are supported process hypotheses to investigate, not fabricated findings about a real team.
4. **Containment/owners (2):** Accountable release authority holds deployment. Platform/network owners contain the offending routes; incident leadership preserves redacted evidence and keeps approved manual lookup available. Do not send the evidence off site for convenience.
5. **Repair/retest (3):** Remove the actual prohibited route, establish a supported offline activation alternative or reject the product under the unchanged rule, and complete support/recovery mapping. Schedule a build-linked retest, for example 2026-11-27, covering cold start, renewal, failure/restore, update media and all protected paths. A future test plan is not passing evidence.
6. **Bounded closure (3):** A repeated conflict stays BLOCKED. Resolved observed conflicts with incomplete evidence become UNVERIFIED. Complete favorable synthetic declarations become only REVIEW_REQUIRED. Human review still must authenticate infrastructure, evidence and operating procedures, assess residual uncertainty and define expiry/change triggers. No automatic production approval or legal compliance claim.

**Total 40 points.** Illustrative course knowledge threshold 24/40, with mandatory remediation for invented evidence or any hard-boundary override. This is not an external qualification.

## Lab and PM marking

Run all 14 tests and compare the original graph with a mutation. Require a correct status transition, editable Mermaid and an explanation of at least one tool limitation. The complete fixture's favorable declarations do not verify a facility or operator. The program's strict inventory policy scopes all declared components, even those marked nonprotected; an edge's protection Boolean does not declassify a derivative.

The ADR's separate 20-point rubric awards boundary/use 4, planes/privilege 4, lifecycle/evidence 6, alternatives/economics 3, and accountable bounded closure 3. Require 12/20 plus remediation of hard-gate overrides. Automatic work-order execution reopens intended use, action permissions, human stop/fallback and consequence analysis; the advisory-only assessment cannot simply be reused.
