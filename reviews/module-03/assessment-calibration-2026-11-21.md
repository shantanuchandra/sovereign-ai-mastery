# Module 03 assessment calibration: two synthetic Q5 responses

**Date:** 2026-11-21. **Reviewer:** GPT-6 self-calibration, not an independent second rater, learner study, human review or external validation. **Source of rubric:** `assessments/solutions/03-enterprise-sovereignty-requirements-strategy-solutions.md`, Q5, six one-point criteria. **Scope:** Q5 only, not the 40-point exam or 20-point board pack. All customer details and sample responses are invented for teaching.

## Sample A: plausible but unsafe (synthetic)

> “A public API is unacceptable because the factory is disconnected. B is also unacceptable since online activation is needed. Choose C because Ollama runs locally and is therefore fully air-gapped. We can disable the internet in the firewall and ask the supplier to open a temporary support tunnel for patches.”

| Q5 criterion | Score | Reason |
|---|---:|---|
| Reject A | 1/1 | Explicit rejection |
| Reject B | 1/1 | Explicit rejection |
| C is UNVERIFIED, not certified | 0/1 | Calls C fully air-gapped |
| Four falsifiable tests including licence/cloud routing | 0/1 | No four tests; firewall statement is not an observed test |
| Infeasibility plus non-AI fallback | 0/1 | Neither present |
| Vendor API evidence limits; reject support tunnels | 0/1 | Assumes local API proves isolation; proposes tunnel |
| **Total** | **2/6** | **Release-veto override:** do not accept the recommendation |

**Feedback:** A localhost API is not proof of disconnected installation, model-specific licence, out-of-band management isolation or offline restore. A support tunnel violates the fictional no-network rule even if time-limited.

## Sample B: conditional and evidence-led (synthetic)

> “Reject A: it requires external inference. Reject B as designed: its online activation violates the air-gap requirement. C is an evaluation candidate only; the Ollama README documents a local API, not certified physical isolation. Before release, a qualified operator must inventory and disconnect ports/radios/out-of-band management, prove model-specific offline licence rights, inspect DNS/proxy/firewall and disabled cloud/fallback paths, test offline install/reboot, and demonstrate signed-media intake and offline backup/restore against the approved RTO/RPO. Keep status UNVERIFIED until signed evidence exists. If the tests cannot pass, mark NOT FEASIBLE UNDER CURRENT CONSTRAINTS and use an approved manual search workflow. Never open a support tunnel.”

| Q5 criterion | Score | Reason |
|---|---:|---|
| Reject A | 1/1 | Explicit external-path rejection |
| Reject B | 1/1 | Explicit activation-path rejection |
| C is UNVERIFIED, not certified | 1/1 | Clearly conditional |
| Four falsifiable tests including licence/cloud routing | 1/1 | Physical, licensing, routing, installation, intake and restore checks |
| Infeasibility plus non-AI fallback | 1/1 | Both present |
| Vendor API evidence limits; reject support tunnels | 1/1 | Explicitly separates documented API from isolation and prohibits tunnel |
| **Total** | **6/6** | **Not a deployment approval:** high-quality answer describes evidence still to collect |

## Ambiguity and scoring guardrails

1. **Criterion 4:** Require at least four *distinct* checks, including an offline licence/provenance check and cloud/fallback route check. “Test security thoroughly” earns no point. An assertion that a firewall is configured is not an observed test.
2. **Criterion 3:** Merely preferring C earns no point. The answer must say it is unverified or conditional and name missing evidence.
3. **Criterion 6:** A response that invokes a supplier support tunnel cannot earn this point even if it correctly quotes the README.
4. **Critical safety override:** Numeric points do not authorize a GO. If a response approves prohibited network access, mark its release decision incorrect and require correction.
5. **Calibration limit:** These are two intentionally contrasting, author-created answers scored once by the same model. They demonstrate rubric discrimination, **not** inter-rater reliability. A separate blinded rater and representative borderline samples remain needed.

**Disposition:** E03-03 partially addressed by documented synthetic scoring; inter-rater calibration **OPEN**. E03-02 manual accessibility and technical T03 gates remain open. No live assessment or executable test was performed by creating this record.
