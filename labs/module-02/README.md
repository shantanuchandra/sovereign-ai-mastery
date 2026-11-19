# Module 02 lab: score claims, not marketing labels

**Decision:** A maturity score is not a release approval. First test architecture eligibility against non-negotiable site, connectivity, capacity and licence requirements. Then record *separately* the four sovereignty dimensions and the quality of evidence. An adverse hard-gate result blocks the workload even if three other dimensions look mature.

**Audience:** Enterprise AI PM, platform lead, security reviewer and procurement partner.  
**Duration:** 75–100 minutes.  
**Environment:** Python 3.11+ standard library on macOS, Linux or Windows; no GPU, Docker, cloud account or API key. The script requires no network access.  
**Inputs:** Entirely fictional case records in [cases.json](cases.json). The URLs, destination names and policy IDs in the lab are examples only.  
**Learning framework:** [Module 02, Section 2.7](../../chapters/02-classifications-components-maturity-models.md) and the [course ontology](../../taxonomy/ONTOLOGY.md). The M0–M4 stages are course-authored, not NIST maturity levels, legal advice or sovereign-AI accreditation.

## What you will produce

A four-workload **classification and maturity matrix** with (1) exact requirement and physical boundary, (2) eligible/ineligible architecture, (3) separate territorial, operational, technological and legal/contractual stages, (4) reviewable evidence coverage, (5) hard-gate failures and open gaps, and (6) an accountable go/no-go memo. A screenshot of a single aggregate score does **not** satisfy the lab.

## Setup, no downloads or credentials

Use a local copy of the repository. From its root:

\`\`\`sh
python3 --version
python3 labs/module-02/evaluate.py labs/module-02/cases.json
python3 -m unittest discover -s labs/module-02 -p 'test_*.py' -v
\`\`\`

If a Unix-style \`python3\` launcher is unavailable, use the installed \`python\` command for Python 3.11+. No installation commands are required. This lab has **no network egress by design**; it models sites and paths in JSON and does not create firewall rules, send packets, run inference or verify vendor products. An actual on-premises or air-gapped acceptance test requires approved infrastructure and independent observations.

Expected simulator dispositions for the unchanged fictional inputs:

| Workload ID | Illustrated circumstance | Expected disposition | Reason |
|---|---|---|---|
| CORP-02 | Synthetic corporate policy assistant at named approved site; controls only configured/declared | \`UNVERIFIED\` | No hard conflict reported, but no reviewed evidence across all required dimensions |
| PLANT-02 | Local GPU and index, with an observed synthetic restricted diagnostic path outside the named plant | \`BLOCKED\` | A confirmed case-simulation physical-premises failure is a hard gate |
| OT-02 | An air-gapped requirement with general outbound networking enabled | \`BLOCKED\` | An air gap forbids **any inbound or outbound network path**, even if the data are synthetic |
| LIC-02 | Strict premises-only runtime with offline licence use unavailable | \`NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS\` | An off-site model is not an authorized fallback for an infeasible local design |

The CLI returns JSON. \`scenario_reported_coverage\` counts *claims* marked reviewed in the **fictional input**, not authenticated evidence. Even four claimed reviewed dimensions produce \`REVIEW_REQUIRED\`, never \`CERTIFIED\` or \`COMPLIANT\`.

## Procedure: five controlled experiments

1. **Baseline classification (10 min).** Execute the commands above. Identify the scope of each requirement, the difference between an approved country and one physical premises, all required control dimensions, and the evidence status. Save the report locally. Do not treat the report as a production audit.
2. **Compare one variable (15 min).** Copy \`cases.json\` to an untracked scratch file. In **PLANT-02**, change \`compute_site\` to \`DOMESTIC-DC-B\` while keeping \`required_site\` as \`FACTORY-A\`. Re-run. Explain why domestic ownership or geographic proximity cannot satisfy the *single named premises* rule.
3. **Investigate the control plane (20 min).** Restore \`compute_site\` to \`FACTORY-A\`, then set \`restricted_offsite_flow\` to \`false\`. Record whether that modeled change removes a **synthetic** failure, and what real traces, privileged support tests, backup tests and independent review would still be needed. A JSON edit is **not** evidence of remediation.
4. **Challenge the air gap (15 min).** In **OT-02**, change \`network\` from \`internet\` to \`disconnected\` *and* \`external_network_path\` from \`true\` to \`false\`. Explain why changing only the visible network label is insufficient when a separate external management route remains. Outline offline artifact intake, signature/hash verification, removable-media custody, local recovery and rollback.
5. **Test evidence and recovery (20 min).** Set one \`dimension\`'s \`evidence\` from \`configured\` to \`reviewed\`. Observe how the reported coverage changes while approval is still withheld. In **LIC-02**, set \`offline_licence_available\` to \`true\` and run the model again. Identify the remaining evidence gaps and whether quality/capacity/restore tests have been performed. Record an explicit \`NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS\` disposition when the necessary model and licence cannot be operated locally.

## The release-first decision template

Fill one row per workload. You may use this Markdown table in a private or synthetic-only decision memo.

| ID and claim owner | Scope and immutable boundary | Candidate / four dimension stages | Adverse or missing evidence | Release disposition | Required next test and reviewer |
|---|---|---|---|---|---|
| CORP-02 | [owner, approved named locations] | [site, T/O/Tech/L] | [unreviewed logs and contracts] | [UNVERIFIED] | [verify exact service, admin paths, support, backup] |
| PLANT-02 | [factory data owner, FACTORY-A only] | [local compute, T/O/Tech/L] | [off-premises diagnostic path] | [BLOCKED] | [deny/retire remote path, synthetic normal/crash/restore traces] |
| OT-02 | [OT security owner, physical disconnection] | [local offline compute, T/O/Tech/L] | [external network path] | [BLOCKED] | [physical/network inspection and offline update/rollback] |
| LIC-02 | [plant data owner, FACTORY-A only] | [licensed local model, T/O/Tech/L] | [offline entitlement unavailable] | [NOT FEASIBLE] | [procurement rights and clean cold start] |

**Decision rubric:** A valid memo refuses to rank a hard-failing design by cost or an average maturity score. Missing evidence stays \`UNVERIFIED\`; a known adverse test is \`BLOCKED\`. Rights and jurisdictional applicability are reviewed by appropriate specialists, not inferred from Python or site selectors.

## Failure investigation and root-cause analysis

*Fictional symptom:* A procurement scorecard says “M3 territorial”, because the model is on a local GPU. During a simulated model crash, a telemetry agent attempts to send a synthetic restricted marker off the premises.

Document **expected vs observed**, symptom, impact, direct cause (external diagnostic collector), contributing process gap (exception path omitted from data-flow inventory), containment (route denial, artifact retention), named owner, corrective design (local sink or removal), **retest** (normal, crash, backup, restore, support, upgrade) and closure criteria (dated reviewed observations tied to exact build). A corrected JSON flag cannot close the real-world investigation.

**Clean-up:** Delete scratch input/output files. Do not upload real customer data, prompts, credentials, firewall traces, internal architecture maps or support logs to this public repository. No test account or billable service is created by this lab.

**Acceptance criteria:** (a) unchanged inputs produce the four expected dispositions, (b) automated unit tests run successfully, (c) a learner can show why domestic off-site inference fails a plant constraint, (d) the physical air-gap test rejects a hidden external route, (e) UNKNOWN/UNVERIFIED are never treated as PASS, and (f) the memo records owner, test, evidence and final decision independently for each dimension. Facilitator solutions, if prepared, live only in \`assessments/solutions/\`, not in this learner page.
