# Module 02 | Facilitator solutions and marking rubric

> **Facilitator-only teaching material.** The repository is public, but the website publisher intentionally excludes `assessments/solutions/` from its output. Do not link this file from the learner website. All enterprise workloads and tests below are fictional and use synthetic data. These exercises do not determine legal compliance or certify sovereign AI.

**Assessment:** [Module 02 learner Questions 1–6](../../chapters/02-classifications-components-maturity-models.md)  
**Applied lab:** [Module 02 release-first scoring lab](../../labs/module-02/README.md)  
**Framework:** [Course-authored sovereignty taxonomy and ontology](../../taxonomy/ONTOLOGY.md)  
**Total:** 40 points = Q1–4 (4 each), Q5 (6), Q6 (18). Recommended learning thresholds, not professional certification: 34–40 sound judgment, 27–33 revise evidence gaps, below 27 redo boundary and RCA exercises. **Any answer proposing remote inference for a hard premises-only or air-gap workload must be corrected, irrespective of numerical score.**

## Q1. Scope and authority (4 points)

The **named workload-specific single-physical-premises restriction** governs the factory use case unless an authorized, applicable policy change explicitly supersedes it. A broader enterprise permission for public/synthetic material is not a waiver for restricted engineering drawings.

Award: **1** for distinguishing workload and enterprise scopes; **1** for signed issuer/applicability/exception authority; **1** for identifying two lifecycle paths (e.g., embeddings, diagnostics, logs, backup, vendor support, evaluation, failover); **1** for an actionable synthetic egress and location test with data/platform owner. Do not accept “in the UAE” as equivalent to “inside FACTORY-A.”

**Release inference:** A managed endpoint outside FACTORY-A is ineligible for restricted source data, whether the endpoint is in-country or abroad. Do not infer any actual UAE legal obligation solely from this classroom case.

## Q2. Four dimensions (4 points)

**Territorial:** the server is on the physical site, but diagnostic data and external support routes remain unverified or adverse if tested. **Operational:** unbounded vendor administrator rights defeat the assumed enterprise control policy; privileges and break-glass sessions must be scoped and logged. **Technological:** model/runtime rights, update dependencies, local capacity, recovery and portability need separate tests. **Legal/contractual:** identify executed vendor terms, data-media handling and jurisdictional questions for specialist review; location alone is not legal compliance.

Award **1 per dimension** for a distinguishable, concrete assessment; at least one point requires explaining a revocation test: remove supplier access, expire credentials, attempt a synthetic forbidden admin session, inspect local logs and confirm denial. A strong answer names IAM/CISO and procurement owners. A claim of automatic PASS based on site ownership is wrong.

## Q3. Deployment and autonomy (4 points)

For the synthetic employee assistant, approved off-site managed inference **could be considered** subject to exact processing location, support, logging, licensing and contracts; it is not presumed accepted. OT-Q6 requires a **physically disconnected system**: neither a private link, domestic hosted endpoint, allowlisted internet route nor temporary remote support tunnel satisfies **no inbound or outbound network**.

Award: **1** for portfolio differentiation; **1** for explicit denial of all network paths under an air gap; **1** for an offline update procedure (signed, versioned artifact; checksum/signature check; malware scan where feasible; removable-media custody; local install and rollback); **1** for recording physical access, offline restore and operator evidence rather than declaring automatic compliance. No unrestricted cloud fallback is permitted.

## Q4. Maturity versus evidence (4 points)

The **synthetic adverse off-site diagnostic route** causes **BLOCKED** for the factory hard boundary. The previously claimed M3 territorial evidence must be invalidated for the changed agent/gateway version. A high technological score and a numerical average cannot compensate for the failure. Legal/contractual remains **UNKNOWN**, pending specialist review.

Award: **1** for BLOCKED; **1** for invalidating stale M3; **1** for concrete retest (normal/crash/support/restore, timestamps, packet/proxy/DNS traces, denied paths, exact configuration and signed reviewer); **1** for separate statuses and no weighted compensation. A configuration edit by itself is not reviewed test evidence.

## Q5. Real product example: Microsoft Foundry Models (6 points)

**What the official source says:** Microsoft's *Deployment types for Microsoft Foundry Models* describes where data are processed for its **Serverless API deployment types**. The documentation (accessed **20 November 2026**) states: “Global types: May be processed in any Azure region.” It also describes Data Zone types as confined to a Microsoft-specified data zone, while Standard (single region) processes inference in the deployment region. The documentation distinguishes *data at rest* from inference-processing placement.[^ms-ft-sol]

**Application to a *fictional* UAE customer:** If the approved workload boundary genuinely allows a named Azure deployment region and all support/backup/telemetry conditions are independently verified, a suitably available and configured **single-region** deployment could be considered. A **global** type is not evidence that inference remains in the customer's approved country. A data-zone designation is not itself a single-premises assurance. None of these **remote** inference types can satisfy the fictional factory's **one physical premises** boundary or the physically air-gapped tool's prohibition on network access.

**Six evidence items to request:** (a) exact model SKU, region and deployment type; (b) signed contract and service terms including support/subprocessor obligations; (c) official versioned processing and logging documentation for the selected SKU; (d) exported runtime/configuration evidence; (e) synthetic network and failover/diagnostic traces testing actual endpoints; (f) retention, deletion, identity, key-custody and exit evidence. The current public product page describes intended offerings; it does **not** prove a specific customer's runtime, license entitlement, legal compliance or certification.

**Marking:** **1** for correct global vs data zone vs regional distinction; **1** for global limitation; **1** for why documented single-region is *conditionally* suitable for some boundaries; **1** for rejecting remote inference for named factory premises and air gap; **1** for at least four specific evidence items; **1** for distinguishing official documentation, signed contract and independently observed runtime. If a learner assumes all Foundry models support every deployment type/region, ask for exact SKU verification.

**Probable RCA for a weak procurement memo:** The team substituted a product *deployment category* for evidence of its *selected service and actual traffic*. Fix by binding requirements to SKU, location, contract, operator, logs and dated runtime tests. The brand's published documentation is real; the purchaser and deployment are fictional.

## Q6. Full decision scenario and RCA (18 points)

**Executive release decision:** **BLOCKED** for PLANT-Q6 at the tested configuration. A synthetic controlled timeout demonstrated that a gateway fallback could cross the expressly forbidden physical-premises boundary. It does not establish that production/customer data were exported. OT-Q6 remains subject to an even stronger **no-network** rule.

| Required RCA item | Worked solution and evidence | Points |
|---|---|---:|
| Expected and observed | **Expected:** data, embeddings, prompts, outputs, telemetry, diagnostics and backups remain within FACTORY-A. **Observed:** a configured fallback routed a synthetic restricted marker to an off-site provider API during timeout. Separate observed test from any unconfirmed historical breach | 3 |
| State at T0 vs T2 | **T0:** earlier narrowly scoped M3 label is not present-tense proof after changes. **T2:** test trace is ADVERSE for the site-boundary criterion; current launch is BLOCKED, and updated review is required | 2 |
| Direct cause and root/process cause | **Direct cause:** remote endpoint in gateway fallback. **Contributing cause:** release workflow omitted degraded-mode routing, dependency change approval and evidence invalidation after update | 3 |
| Immediate containment and owners | Platform lead disables remote fallback/denies destination. Security preserves proxy/DNS/packet logs, checks historical event scope. Plant data owner maintains requirement and approval authority. Procurement/legal reviews support/vendor/contract rights. PM holds release and tracks RCA | 3 |
| Corrective architecture | Approved local fallback with capacity, model rights, IAM controls or controlled fail-closed error; **never** off-site inference for PLANT-Q6. **No** online diagnostics, tunnels or licence servers for OT-Q6; offline artifact intake and local recovery only | 2 |
| Reproducible retest and closure | Versioned synthetic markers; normal requests, overload, timeout, crash, update, support and restore; inspect all outgoing network paths and gateway/admin logs, licences, quality and local throughput; independent reviewer and dated signed dispositions, plus evidence-renewal trigger | 3 |
| Final bounded decision | **BLOCKED** until all hard gates retest successfully and missing operational, technological and legal questions receive proper review. A favorable TCO/maturity score is irrelevant to a confirmed hard violation | 2 |

**Direct-cause versus root-cause distinction:** Removing one fallback URL can stop one observed path without preventing later vendor configuration changes. The systemic fix is to **inventory all dependency and control-plane routes, deny unapproved destinations, test degraded modes and revoke stale evidence when policies or versions change**. For a genuine company event, retain an incident investigation; do not extrapolate from this synthetic case.

**Fail-closed test:** Any learner proposal that suggests sending restricted factory prompts to an off-site country-resident model is incorrect under the fictional requirement. If the local solution lacks a licensable model, acceptable quality, sufficient capacity or a tested recovery path, report **NOT FEASIBLE UNDER CURRENT CONSTRAINTS** and bring the decision to the authorized owner, rather than silently weakening it.

## Module 02 lab: expected outcomes and troubleshooting

Run the public synthetic lab exactly as written:

```sh
python3 labs/module-02/evaluate.py labs/module-02/cases.json
python3 -m unittest discover -s labs/module-02 -p 'test_*.py' -v
```

| Case | Expected simulator disposition | What the learner must not infer |
|---|---|---|
| CORP-02 | `UNVERIFIED` | That legal compliance or supplier operations were demonstrated |
| PLANT-02 | `BLOCKED` | That a local GPU outweighs an adverse diagnostics trace |
| OT-02 | `BLOCKED` | That an allowlist or a disconnected network *label* constitutes an actual air gap |
| LIC-02 | `NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS` | That the vendor permits offline licence or off-site substitution |

**Common failures:** A malformed JSON boolean such as `"false"` yields `INVALID`; correct to `false` without quotes. Missing one of four dimensions also yields `INVALID`. A classroom `reviewed` claim with a test ID changes *scenario-reported coverage* but never grants `COMPLIANT`; the maximum simulated state without hard failures is `REVIEW_REQUIRED`. An adversarial `adverse` evidence entry blocks a candidate. An M3/M4 label without reviewed source evidence creates an unverified gap. Python tests do not inspect real networks or external vendors.

## PM deliverable rubric (20 points, separate from quiz)

| PM evidence dimension | Points | Full-credit criteria |
|---|---:|---|
| Correct scope, authority and physical/network boundaries | 4 | Workload-specific owner, explicit site and connectivity conditions; no silent waivers |
| Eligibility-first architecture classification | 4 | Compares public/managed/private/hybrid/edge/air-gapped, rejects every hard mismatch before cost |
| Four-dimension maturity and evidence state | 4 | Territorial, operational, technological, legal/contractual statuses individually recorded, UNKNOWN not passed, version/date/reviewer |
| Dependency graph and remediation priorities | 4 | Model, host, control plane, support, evaluation, logs, licensing, backup and exit covered with actionable gap owner |
| Decision and reproducibility | 4 | Testable go/no-go, synthetic trace or honest UNVERIFIED, clear retest/rollback, specialist referrals where needed |

**Release rule for facilitator feedback:** A learner may demonstrate strong product judgment with a **BLOCKED** recommendation. Do not reward a misleading “APPROVED” outcome obtained by weakening the factory or air-gap boundary.

[^ms-ft-sol]: Microsoft, *Deployment types for Microsoft Foundry Models*, Microsoft Learn, deployment processing section, checked 20 November 2026, https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types. Microsoft product documentation, not independent customer-level processing evidence.
