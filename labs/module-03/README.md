# Module 03 lab: turn an enterprise request into an acceptance decision

**Decision:** A fictional sovereignty request passes this exercise only when each non-negotiable requirement has a named issuer, control, test, dated evidence and bounded release status. An eligibility failure takes precedence over a favorable weighted investment score. Neither the Python script nor a stakeholder vote can certify real-world compliance.

**Time:** 90–110 minutes. **Environment:** Python 3.11+ standard library, no GPUs, cloud accounts or network access. **All workloads, data, authority names, requirements, evidence and test outcomes are fictional.** The lab simulates an evaluation; it cannot inspect a network, check legal applicability or authenticate a signature.

**Sources:** [Module 03 requirements and governance](../../chapters/03-enterprise-sovereignty-requirements-strategy.md), especially Sections 3.4–3.7; [course ontology](../../taxonomy/ONTOLOGY.md). The acceptance schema and decision statuses are course-authored.

## Run locally

From the repository root:

~~~sh
python3 labs/module-03/evaluate.py labs/module-03/cases.json
python3 -m unittest discover -s labs/module-03 -p 'test_*.py' -v
~~~

Use a Python 3.11+ interpreter named `python` if `python3` is unavailable. No pip packages or credentials are needed. The report is JSON with per-workload **hard failures, missing evidence, traceability and disposition**. Tests deliberately include failing fictional architectures; those cases are expected learning outcomes, not errors in the script.

## Dataset and expected decisions

| Workload | Named authority and control requirement | Expected simulator decision |
|---|---|---|
| **POLICY-03** | Business sponsor permits a managed model only at its approved named processing site; supplier/access/legal evidence incomplete | `UNVERIFIED` |
| **DESIGN-03** | Plant owner requires all restricted source data **and derivatives** to remain within physical FACTORY-A, including fallback and diagnostics | `BLOCKED`: synthetic remote diagnostics attempt |
| **OT-03** | Operations safety authority requires **no inbound or outbound network**, including activation and recovery | `BLOCKED`: hidden external network dependency |
| **LICENCE-03** | Plant owner requires a fully local model but offline licence rights are unavailable | `NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS` |

The simulated test values are **not authenticated**. Even if you mark every claim as reviewed, the maximum scripted result is `REVIEW_REQUIRED`, pending a real authorized reviewer. The simulator must never output `COMPLIANT` or `CERTIFIED`.

## Five experiments

1. **Trace the business objective (15 minutes).** Execute the baseline. For each case, record the business sponsor, requirement issuer, control implementer, evidence reviewer, allowed location/network paths and release decision. Compare against the four expected outcomes.
2. **Reject the wrong physical site (15 minutes).** In a scratch copy, change DESIGN-03 `compute_site` from `FACTORY-A` to `UAE-DC-2`. The location may be in the same country but does not satisfy the **named physical premises** rule. Explain why neither encryption nor a supplier's domestic-region label is a waiver.
3. **Distinguish control success from architecture failure (20 minutes).** Restore on-site compute, change DESIGN-03 `offsite_derivative_attempt` to `false` and set its evidence state to `configured`. This fictional edit removes an adverse scenario assertion, but the claim becomes **UNVERIFIED** until observed packet, DNS, support and backup traces are reviewed. Do not call a JSON edit remediation evidence.
4. **Challenge an air gap and offline licence (20 minutes).** In OT-03 set `network_mode` to `disconnected` but leave `external_management_path` true. It still blocks. Then set the external path false; it becomes **UNVERIFIED** because actual physical isolation and offline restore remain untested. For LICENCE-03 change `offline_licence_available` to true; record which other test and review gaps remain.
5. **Prepare the board pack (20–40 minutes).** Produce a three-page synthetic memo with a four-role stakeholder map, requirement-to-control-to-test-to-evidence chain, six useful metrics and a 30/60/90-day roadmap. Include the best **non-AI** alternative, remediation owner, exact build, next test and change trigger.

## Root-cause exercise

**Fictional observation:** DESIGN-03's local inference process fails under timeout. A gateway attempts to send a synthetic restricted marker to an external collector; a firewall denies delivery. The **egress deny worked**, while the **no-offsite-routing requirement failed**.

Write: expected versus observed; direct cause (remote gateway/collector rule); contributing process cause (degraded-mode dependencies absent from release review); containment (freeze configuration and preserve synthetic logs); correction (local-only fallback or controlled failure); retest (normal, timeout, crash, supplier support, backup, update and restore); closure (plant owner, security, platform and legal/procurement sign bounded results). Do **not** assert a production breach from this simulation.

## Marking guide, 20 points

| Criterion | Points |
|---|---:|
| Exact requirement issuer, workload and physical/network boundaries | 4 |
| Correct hard-failure disposition before any ROI or maturity ranking | 4 |
| Complete chain from risk to control, positive/negative test and evidence | 4 |
| Distinct stakeholder approvals and RCA owner/remediation | 4 |
| Business metrics, non-AI alternative, roadmap, uncertainty and change-triggered retest | 4 |

A strong answer can recommend **BLOCKED** or **NOT FEASIBLE**. The facilitator's full solution belongs in the separate Module 03 key, not this public lab. Never add real customer documents, credentials, firewall traces or private vendor terms to this public repository.
