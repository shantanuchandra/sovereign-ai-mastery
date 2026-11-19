# Module 02 — Classifying what must remain under control

> **Executive thesis:** Classify sovereignty requirements by whose objectives they serve, then identify the workload, control owners, and evidence. National, sectoral, enterprise and workload scopes can coexist, but a high-level policy or domestic hosting claim does not prove that one AI workload meets its actual physical, operational or legal boundaries.

| Course context | Detail |
|---|---|
| Part / week | I — Foundations / Week 2 |
| Audience | Enterprise AI PM making architecture and procurement decisions |
| Prerequisite | [Module 01: Who controls the intelligence?](01-sovereign-ai-fundamentals.md) |
| Current publication | **In-progress chapter, Section 2.1**. Sections 2.2–2.7 and both module-critical reviews are pending |
| Output | Scope-to-claim matrix with a bounded recommendation |
| Environment | Browser and Markdown, no GPU or cloud spend; fictional and synthetic data only |
| Sources reviewed | 19 November 2026 |
| Status | Educational decision framework, not legal advice or sovereignty certification |

## 1. Executive brief: identify whose requirement applies

A fictional UAE industrial group proposes one enterprise AI platform for an employee-policy assistant, a factory maintenance assistant and a disconnected industrial-control reference assistant. One common governance register can help all three. A single managed inference endpoint cannot automatically satisfy their different data and network boundaries.

**Product decision:** Classify the authority and scope of every proposed sovereignty requirement before accepting a platform topology. Keep an evidence record for each workload. A national investment objective, a sector policy and an enterprise processing permission do not automatically waive a tighter factory-level prohibition. If mandatory requirements conflict or local compute is inadequate, record **BLOCKED** or **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**, not a weaker substitute architecture.

### 2.1 Sovereignty by scope: national, sectoral, enterprise, workload

**Four scopes answer “whose sovereignty objective?” They are not four increasing levels of certification.** A company can be part of a national AI ecosystem while needing different evidence for every enterprise workload.

#### Compare the four scopes without confusing strategy and proof

| Scope | Decision boundary | Illustrative objective | Responsible evidence owner | What this does not establish |
|---|---|---|---|---|
| **National** | State-wide strategy or public policy programme; enforceable obligations depend on the actual instrument | Build domestic compute capacity and supplier diversity | Public programme owner or authority for national outcomes; enterprise still validates its workload | That a domestic model endpoint meets every enterprise data or access rule |
| **Sectoral** | Industry ecosystem or a specifically applicable regulator/sector authority | Shared service controls for a hypothetical financial-services AI platform | Sector policy or regulator evidence, followed by counsel's entity/activity applicability review | That all firms in the sector have identical AI location rules |
| **Enterprise** | A company's procurement, identity, risk, infrastructure and contracting estate | Require enterprise-held keys and reviewed model-exit procedures | CIO, CISO, data owners and platform team | That a permissive enterprise default overrides a stricter team requirement |
| **Workload** | A named use case with defined data, users, operators and lifecycle stages | Restrict a factory assistant and all its data derivatives to one physical site | Workload sponsor plus platform and security test owners | That tested inference location also proves logging, support, backup or failover boundaries |

The scopes **overlap**. National or sector context can inform an enterprise requirement, and enterprise controls may be inherited by workloads. But inheritance needs explicit authority, applicability and a collision rule. A sector category alone is not evidence that a particular law applies.

**Source ledger:** OECD AI Principle 2.2 recommends “an inclusive, dynamic, sustainable, and interoperable digital ecosystem” as a government ecosystem objective.[^oecd-scope-21] NIST AI RMF 1.0, Map 1.1, emphasizes documenting the “prospective settings in which the AI system will be deployed.”[^nist-scope-21] Neither source defines or certifies this course's four sovereignty scopes. The classification is a **course-authored** decision tool.

#### Build a requirement chain that preserves authority

Use the [course ontology](../taxonomy/ONTOLOGY.md) rather than a national-to-workload “sovereign” checkbox:

**Policy source or authority → applicable requirement → named workload → dependency/control → repeatable test → dated evidence → recorded decision.**

A strategy can influence the market without automatically creating a mandatory workload rule. A contract may govern operations without establishing legal applicability. Only a qualified specialist should decide the relevant legal obligations.

A scope record needs: **claim ID, issuer and evidence of authority, affected organization, workload and lifecycle, permitted and prohibited flows, owner, criterion, dependencies, test, evidence state and exception/appeal process**. Missing issuance or applicability stays **UNKNOWN**, not silently inherited.

Rules for PMs:

1. **No policy laundering.** A national capability announcement or domestic region label is never runtime test evidence.
2. **No downgrade of workload hard boundaries.** A company-wide country-only default does not permit a restricted factory assistant to send inference, embeddings, diagnostics or backups off its named **physical premises**.
3. **Air-gap is separate.** “Single premises only” may allow local networking. A physically air-gapped requirement allows **no inbound or outbound network**, not even an approved remote-support or update channel.
4. **No scores before eligibility.** Reject architectures failing binding site, operator, network or minimum model-quality constraints before ranking cost or convenience. When requirements cannot be reconciled, escalate to owners instead of inventing an exception.

#### Worked architecture: one group, three legitimate outcomes

*The organization, workloads, policies, failures and acceptance results below are fictional; no real UAE sector rule or vendor capability is asserted.*

| Workload | Scope and owner | Mandatory boundary | Candidate and decision |
|---|---|---|---|
| **CORP-01**, synthetic employee-policy assistant | Enterprise product owner and platform lead | Approved named processing locations; no confidential customer data in pilot | Managed model **CONDITIONAL** on service-specific runtime, support, logs, backup, access and contract evidence |
| **PLANT-02**, proprietary maintenance RAG | Workload data owner; enterprise default remains subordinate to the plant's more restrictive requirement | No plant documents, prompts, embeddings, answers, telemetry, diagnostics or backups leave one **physical factory premises** | On-site serving, local retrieval, local logs and restore **CONDITIONAL** on capacity, quality, egress, operator and recovery tests |
| **OT-03**, disconnected operations reference | Workload OT/security owner | Air-gapped: **no inbound or outbound network**; controlled offline media | Disconnected local model **CONDITIONAL** on offline intake, removable-media custody, recovery and safety review |

**Why not one endpoint?** The group can standardize identity labels, control tests, risk review templates and artifact validation while segregating processing paths. PLANT-02 cannot call CORP-01's managed API, even in the same country. OT-03 cannot inherit PLANT-02's network allowance merely because both are on-premises.

**Technical trade-off:** On-site compute increases responsibility for power, hardware, staff, quality, licensing and maintenance. Managed services can reduce some operational burdens for workloads that permit them. An air gap increases update and recovery complexity. Measure the trade-offs with synthetic evaluation cases; do not infer model throughput or legal compliance from the deployment category.

#### RCA: the country-default policy hid the factory restriction

**Fictional test observation:** A procurement questionnaire classified PLANT-02 as “country only” by inheriting an enterprise default. The proposed architecture used an in-country managed inference endpoint. During a synthetic acceptance test, restricted-label prompts crossed the factory gateway. Even if the remote endpoint satisfies a country-level requirement, it **fails** the explicit single-premises constraint.

| RCA stage | Observation and solution |
|---|---|
| **Impact/status** | **BLOCKED** for restricted data. The synthetic network trace proves a tested off-site route, not a real customer incident |
| **Direct cause** | Scope override for PLANT-02 was lost when procurement inputs were passed to the architecture selector |
| **Contributing process gap** | Scope, issuer and exception rights were not mandatory fields; no fail-closed test compared country policy with site restrictions |
| **Containment** | PM blocks launch; platform lead removes remote inference; security inspects support, logs and network destinations |
| **Corrective design** | Require an explicit scope/issuer chain and reject off-premises compute before vendor scoring; use local serving or record infeasibility |
| **Verification and closure** | Repeat synthetic inference, embedding, telemetry, backup and failover tests; review admin/support routes and capacity; record dated evidence and sign-off |

**Root cause:** The failure is not that national or enterprise scope is intrinsically weaker. It is that **the named workload's binding boundary was discarded during policy translation**. A category label cannot substitute for requirement traceability.

#### PM artifact: scope-to-claim decision record

A product review must produce one row per independent constraint, not a single “sovereign yes/no” field:

| Field | Example: PLANT-02 |
|---|---|
| Claim and scope | SITE-PLANT-02, workload-only physical-site boundary |
| Issuer and authority state | Plant data owner; signed internal policy **to be verified** |
| Broader context | Enterprise permits managed in-country service for **other** workloads |
| Lifecycle | Collection, retrieval, inference, evaluation, monitoring, backup, failure, deletion and support |
| Permitted geography/network | Single premises; local network only; no restricted external egress |
| Control/acceptance | Deny forbidden destinations; inspect packet/proxy traces, privileged access, recovery and deletion evidence |
| Current evidence | **UNVERIFIED** until a reviewed test |
| Decision | **REJECT** off-site endpoint; assess feasible on-site alternatives; assign evidence owners and exception authority |

**Five-step decision sequence:** collect claim issuers, establish scope and applicable obligations with specialists, reconcile hard constraints, compare **eligible** technical options, then record approved tests and review triggers. The final matrix should name the owner who can reject a design and what evidence could change that rejection.

#### Learner challenge (30 minutes)

Open the [Architecture & Learning Studio](../learning/index.html) using synthetic inputs. Start with **Employee knowledge and policy assistant** and **Selected country only**. Change just the location dropdown to **Single premises only; no data or derivatives may leave**, keeping **Approved managed AI platform** compute. Predict the explicit blocker. Then choose **On-prem production GPU servers inside the premises** and **Local network only; no external egress**. State which operator, backup and model-quality claims remain unverified. Finally select **Air-gapped factory operations** and compare it against a configuration with **General internet access including external service endpoints**.

Submit a **three-row scope matrix** identifying national/sector *context* where actually evidenced, the enterprise default, and a stricter workload control. For each, specify issuer, authority status, hard boundaries, candidate, acceptance test and owner. Explain why the Studio can model trade-offs but **cannot** decide whether a regulator's rule applies.

**Acceptance:** No premises-only or air-gapped requirement is silently weakened, no unsupported law or vendor guarantee is introduced, and every missing piece of evidence has a named next action.

**Next header:** 2.2, *Control dimensions: territorial, operational, technological, legal*. Module 02 remains a draft until its other headers, lab, solutions and two distinct reviews are completed.

[^oecd-scope-21]: OECD.AI, *Fostering an inclusive AI-enabling ecosystem* (AI Principle 2.2), [official principle and rationale](https://oecd.ai/en/dashboards/ai-principles/P11). Exact quotation verified **19 November 2026**. A national policy principle, not an enterprise sovereignty certification.
[^nist-scope-21]: NIST, *AI Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (2023), [AI RMF Core, Map 1.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Exact quotation verified **19 November 2026**. Risk-context guidance, not the source of the course-authored scope taxonomy.
