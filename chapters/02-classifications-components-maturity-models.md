# Module 02 — Classifying what must remain under control

> **Executive thesis:** Classify sovereignty requirements by whose objectives they serve, then identify the workload, control owners, and evidence. National, sectoral, enterprise and workload scopes can coexist, but a high-level policy or domestic hosting claim does not prove that one AI workload meets its actual physical, operational or legal boundaries.

| Course context | Detail |
|---|---|
| Part / week | I — Foundations / Week 2 |
| Audience | Enterprise AI PM making architecture and procurement decisions |
| Prerequisite | [Module 01: Who controls the intelligence?](01-sovereign-ai-fundamentals.md) |
| Current publication | **Teaching headers 2.1–2.7 drafted; module not released**. Dedicated lab, assessment/solutions, publishing artifacts and both critical reviews remain pending |
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

**2.1 completed.** The four scopes above establish whose objectives apply. Section 2.2 below tests which control dimensions can actually enforce them.

[^oecd-scope-21]: OECD.AI, *Fostering an inclusive AI-enabling ecosystem* (AI Principle 2.2), [official principle and rationale](https://oecd.ai/en/dashboards/ai-principles/P11). Exact quotation verified **19 November 2026**. A national policy principle, not an enterprise sovereignty certification.
[^nist-scope-21]: NIST, *AI Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (2023), [AI RMF Core, Map 1.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Exact quotation verified **19 November 2026**. Risk-context guidance, not the source of the course-authored scope taxonomy.


### 2.2 Control dimensions: territorial, operational, technological, legal

**Product decision:** Treat territorial, operational, technological and legal/contractual controls as **four independently testable dimensions**. An enterprise can score well on one and fail a non-negotiable requirement in another. Never average a hard failure into a reassuring “sovereignty percentage.” First reject configurations that cannot satisfy mandatory boundaries; only then compare eligible alternatives for cost, quality and delivery speed.

The dimensions below are part of the [course-authored ontology](../taxonomy/ONTOLOGY.md), not an official regulatory framework or a provider certification. Their purpose is to help an AI PM turn an ambiguous request such as “we need sovereign AI” into a procurement decision with a named owner, observable test and evidence state.

#### Four dimensions, four different failure paths

| Dimension | What the enterprise is trying to govern | An observable acceptance test | A misleading shortcut |
|---|---|---|---|
| **Territorial** | Where restricted inputs, outputs, embeddings, model adaptations, evaluation traces, telemetry, logs, backups and replicas are processed, accessed or retained | Use synthetic markers to trace inference, retrieval, evaluation, monitoring, support, failover, restore and deletion to **approved destinations**; review packet and service records | “Our primary database is in-country, so the entire AI lifecycle is resident” |
| **Operational** | Who can deploy, configure, read, suspend, override, support, recover or export the workload and its data | Review privileged accounts and break-glass authority; revoke vendor access; simulate supervised maintenance and recovery; inspect audit trails | “The enterprise owns the server, so the supplier cannot administer it” |
| **Technological** | Ability to operate, inspect and replace critical models, serving systems, keys, integrations and supplier dependencies when necessary | Review model and artifact rights; prove offline cold-start where required; replace a model/runtime; test compatibility, quality, exit and rollback | “The weights are available, so an executable provider-exit plan exists” |
| **Legal / contractual** | Which actual processing activities, entities, contract terms, disclosure obligations and regulator questions require a specialist decision | Map processors, service terms, subprocessors, access and transfers; obtain counsel's applicability review and accountable sign-off | “A region selector or a generic compliance badge proves the workload meets every legal requirement” |

**Interpretation:** The territorial dimension is not merely *storage* geography. The operational dimension is not merely employee access to the UI. Technological autonomy does not require fabricating chips, but a claimed replacement option must be demonstrated. Legal scope cannot be inferred from the location dropdown; applicable obligations depend on facts reviewed by qualified owners.

NIST's **AI RMF 1.0 Core** describes the four functions “govern, map, measure, and manage,” which support a risk-review process across the AI lifecycle. Its actions **“do not constitute a checklist”**, and its functions are *not* the four sovereignty dimensions above.[^nist-core-dim22] NIST **SP 800-207** states that zero trust grants no implicit trust “based solely on their physical or network location.” That principle explains why an on-site system must still be tested for privileged access, without turning NIST security guidance into a sovereignty certification.[^nist-zt-dim22]

#### Model the boundaries explicitly

For each workload, draw four overlays over the same architecture. The **territorial overlay** traces data and derivatives across inference, retrieval, evaluation, logs and failure recovery. The **operational overlay** traces people, service identities, support tools and authority to override controls. The **technological overlay** traces deployment artifacts, model rights, licence checks, dependencies and migration paths. The **legal overlay** records entities, activities, contracts and questions referred for review.

**Concrete topology (fictional factory assistant):**

```text
[On-site user] -> [Enterprise identity gateway] -> [Local RAG / model runtime]
                             |                           |
                      [Local audit log]          [On-site vector index]
                             |                           |
                     [Local backups]         [Offline approved updates]
                             |
                  [Supervised maintenance]
```

*Reading the diagram:* Every arrow is a hypothesis to verify. The diagram does not prove that telemetry, operating-system diagnostics, licence checks, network tunnels or backup destinations are local. List those as independent dependencies and confirm them by testing and review.

**Invariant:** A requirement of **one physical premises** means *all restricted material and derivatives stay on that premises*. An approved country or region is a different, weaker geographic boundary for this purpose. An **air-gapped** requirement is stronger still: **no inbound or outbound network paths**, including allowlisted vendor support, update channels or remote analytics. An on-site server with unrestricted internet is not automatically an air gap or a proved premises-contained design.

#### Worked UAE enterprise use case: four dimensions produce different decisions

**Scenario (fictional):** A UAE industrial group has a public-policy drafting assistant, an engineering maintenance copilot, and a disconnected operations reference system. The group wants shared governance, but their mandatory boundaries differ. No real regulator or customer event is represented here.

| Fictional workload | Territory | Operations | Technology | Legal and contract questions |
|---|---|---|---|---|
| **PUB-22**, synthetic or public policy text | Named processing locations permitted subject to review | Provider administration may be considered with controls | A managed model can be acceptable if exit risk is explicitly evaluated | Verify data rights, contractual terms and actual applicability; **no compliance claim** |
| **PLANT-22**, restricted plant drawings and manuals | **One named physical premises; no restricted derivatives may leave** | Enterprise operators or approved **on-site** contractor under enterprise control | On-site capacity, runnable model, controlled updates and tested restore required | Review supplier support/media terms and any applicable laws separately |
| **OT-22**, disconnected synthetic operational procedures | One named air-gapped facility | No remote support; approved local operators | Offline model serving, media custody, integrity checks and local rollback | Review offline service and software licence terms, without implying legal clearance |

**Candidate A: managed in-country model endpoint.** It may be an efficient option for PUB-22 if named processing locations, operations, logs, retention and contractual boundaries pass review. It **fails PLANT-22** if inference leaves the factory, regardless of national location. It **fails OT-22** because any network connection to that endpoint contradicts air-gap isolation.

**Candidate B: enterprise-owned regional data center.** Ownership may strengthen some operational controls, but a data center away from PLANT-22's specific physical premises still violates its territorial rule. For OT-22 it also fails unless the required disconnected boundary is met by a specifically approved local architecture.

**Candidate C: on-site model and retrieval with local telemetry.** This is *conditionally eligible* for PLANT-22 if the hardware meets measured quality/capacity needs, enterprise access controls work, supplier support paths remain permitted, and every derivative and recovery path stays onsite. It does not become “fully sovereign” merely by being installed.

**Candidate D: fully disconnected local enclave.** This is *conditionally eligible* for OT-22 if a secure offline artifact intake process, on-site administrator access, backups and physical-media testing work. If no suitable local compute or permitted model licence is available, record **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**, rather than quietly introducing a cloud API.

#### Failure drill and RCA: local inference, remote evaluation

**Fictional acceptance test:** PLANT-22 uses on-premises inference and storage. An evaluation feature, enabled after an update, asynchronously exports sampled prompt-output pairs to a remote analytics account. A synthetic restricted-label marker appears in a firewall trace destined outside the factory. Local serving is functioning, but the **territorial hard requirement fails**. Operational and technological review remain separate; do not mark them failed or passed without their own tests.

| RCA stage | Observation, owner and correction |
|---|---|
| **Impact / status** | Synthetic trace shows prohibited egress in the tested configuration; **BLOCKED** for restricted deployment, not a statement that production data actually leaked |
| **Direct cause** | Evaluation connector defaulted to a remote sink after the software update |
| **Contributing process gap** | Release checklist inventoried primary inference and databases, but not evaluation, diagnostics or third-party observability |
| **Immediate containment** | Platform owner disables the connector and outbound route; security owner preserves test artifacts and investigates historical destinations |
| **Corrective design** | Use a validated local evaluation pipeline or remove the connector; require dependency inventory, explicit deny-by-default egress, update controls and change-triggered retests |
| **Verification and closure** | Replay synthetic prompts under normal, failure, restore and support conditions. Capture network and privileged-access evidence; review versioned configuration and dated results. Close only with owner sign-off and a documented disposition |

**Root cause:** The organization treated a territorial *architecture diagram* as evidence that all lifecycle operations met the boundary. The failed test exposes a gap between intended topology and observed runtime behavior. No amount of strong model portability or favorable legal advice fixes that physical-site egress failure.

#### PM artifact: four-dimension evidence register

Record a **separate status and owner for each dimension**. Here is a draft acceptance set for fictional PLANT-22:

| Claim ID / owner | Falsifiable criterion | Evidence state and release consequence |
|---|---|---|
| **TERR-22 / platform + data owner** | No restricted content or derivative leaves named plant premises across all lifecycle and recovery paths | **FAILED**: synthetic evaluation egress; **release blocked** until corrected and retested |
| **OPER-22 / CISO** | Only approved enterprise/on-site operators can administer model, data, keys, recovery and support; revoked identities cannot reconnect | **UNVERIFIED**: run access/revocation and supplier drill |
| **TECH-22 / architecture owner** | A suitably licensed local model can run within capacity limits, cold-start offline if needed and be replaced without lost access controls | **UNVERIFIED**: demonstrate substitution, licences, benchmark and rollback |
| **LEGAL-22 / counsel + procurement** | Applicable obligations, processor roles, contracts, access, transfer and deletion terms have specialist review and documented disposition | **REVIEW REQUIRED**: architecture and location do not establish legal compliance |

**Release logic:** Fail a hard territorial or air-gap constraint and the result is **BLOCKED**, even if an optional weighted score looks attractive. When evidence is incomplete, use **UNVERIFIED** rather than **PASS**. An unfavorable controlled test requires correction and retesting. If the site cannot supply suitable compute, record **NOT FEASIBLE UNDER CURRENT CONSTRAINTS** instead of substituting remote inference. Do not copy “NIST-aligned,” “in-country” or “private cloud” into a verified sovereignty status.

**Learner challenge (30 minutes):** Use the [Architecture & Learning Studio](../learning/index.html) with synthetic inputs. Start from **Strict on-premises IP research assistant**. Keep **Single premises only; no data or derivatives may leave** and **On-prem production GPU servers inside the premises** selected, but change operator authority from **Enterprise employees administer all layers** to **Approved contractor, physically on-site under enterprise control**. Which dimension changed, and what new supervised-support test is needed? Next change compute to **Approved managed AI platform** and predict the mandatory blocker. Finally select **Air-gapped factory operations**, change connectivity from **Air-gapped: no inbound or outbound network** to **General internet access including external service endpoints**, and explain why the engine should reject the candidate before any vendor ranking.

**Submission:** Provide a four-row register with claim, test, evidence owner, release status and one corrective action; add a one-paragraph architecture decision explaining why none of the four dimensions may substitute for another. The Studio is a deterministic educational simulator. It does **not** inspect real environments, validate supplier assertions or determine regulatory compliance.

**2.2 completed.** The four dimensions above identify the controls to test. Section 2.3 below evaluates deployment classes against those controls.

[^nist-core-dim22]: NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, **NIST AI 100-1** (2023), [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Official HTML checked **19 November 2026**; the quoted function names and checklist limitation appear near the opening of Section 5. This source does not establish the course-authored four-dimension taxonomy.
[^nist-zt-dim22]: NIST, *Zero Trust Architecture*, **SP 800-207**, abstract (August 2020), [official final publication](https://csrc.nist.gov/pubs/sp/800/207/final). Official abstract checked **19 November 2026**; the quotation concerns physical/network trust, not AI sovereignty.


### 2.3 Deployment classes: public, managed sovereign, private, hybrid, air-gapped, edge

**Executive decision:** Choose a deployment class **after** establishing the workload's non-negotiable processing, operator, connectivity, model-quality and recovery requirements. “Sovereign cloud,” “private,” and “edge” are not interchangeable guarantees. A design is eligible only when its actual data and control paths satisfy the declared boundary. Rank cost, latency and convenience *only among eligible candidates*.

This section adds the course-authored **DeploymentClass** classification to the [ontology](../taxonomy/ONTOLOGY.md): a Workload **uses** a DeploymentClass, which **comprises** Components and Dependencies, **enforces** Controls, and **requires** Tests and Evidence. A deployment class is an architectural pattern, not a compliance certificate. A single system may combine several classes, but every cross-class transfer needs its own authorization and verification.

#### Compare the six classes by who operates what

| Class | Typical control arrangement | Possible advantage | Main exposure or operational cost | Hard-boundary verdict |
|---|---|---|---|---|
| **Public cloud AI** | Provider-operated shared infrastructure and managed services, with tenant-specific logical controls | Elastic capacity and fast experiments | Provider and subprocessor access, service-region exceptions, telemetry, backups, availability and exit | **REJECT** when restricted prompts must remain at a named physical premises |
| **Managed “sovereign” offering** | Provider or partner operates an advertised restricted-location/control configuration | Potentially useful for country- or region-bounded workloads | “Sovereign” is a supplier description; verify actual operator identities, subprocessors, model endpoint, logs, support, keys, failover and contracts | **CONDITIONAL** for permitted geography, **REJECT** for site-only if inference or derivatives leave the site |
| **Private enterprise deployment** | Dedicated enterprise-controlled resources on-site or at a named hosted facility | More direct control over access, configuration and data paths | Enterprise bears more capacity, patching, incident response and recovery work; hosted private may still be off-premises | **CONDITIONAL** only when the exact physical facility and all derivative paths satisfy the requirement |
| **Hybrid** | Explicit links between local and external compute or services | Can separate low-sensitivity processing from restricted workloads | Boundary crossing, routing errors, fallback, synchronization and inconsistent observability | **REJECT** for restricted data when any external path is required; can be valid with strict segregation of permitted workloads |
| **Air-gapped** | Physically disconnected enclave with local inference, storage, operations and recovery | Meets a mandatory no-network topology if independently tested | Offline patch/media handling, model supply, hardware, capacity and support burden | **CONDITIONAL** only with **no inbound or outbound network path**, including remote support, licensing and failover |
| **Edge** | Processing close to a device or industrial site; can be locally or remotely administered | Low-latency or intermittent-network operation | Device security, fleet management, remote telemetry, constrained compute and update paths | **NOT automatically site-only or air-gapped**: inspect each device and every management connection |

**Two axes, not one ladder:** *where the model runs* and *who can operate it* are independent. A private GPU cluster in another city is off-premises for a factory-only workload. An edge appliance that phones home is not air-gapped. A managed service running in-country is not evidence that support access or backups meet a particular customer's requirement.

#### Architecture boundary map and tests

For each option, trace **user → identity → retrieval → embedding → inference → output → evaluation → logs → backups → restore**, then add administrator sessions, licence activation, updates, diagnostics, key management and incident response. A diagram showing only inference is incomplete. Capture normal, degraded, disaster-recovery and vendor-support paths. Mark every edge as **allowed, prohibited or unverified**.

**Public or managed pattern (illustrative):** Enterprise user → tenant gateway → provider endpoint → provider logging/operations. Verify the named region, endpoint, network route, subprocessor roles, failover and administrative access from actual configuration and contracts. A marketing region label is not packet-level evidence.

**On-site private pattern (illustrative):** Plant user → local identity service → local vector store → local model → local logs and backups. Validate that update agents, crash reporting, evaluation and remote support cannot export restricted material. A local model does not automatically have a valid offline licence or adequate quality.

**Air-gapped pattern (illustrative):** Local user → disconnected identity and model services → local outputs and audit storage. Updates enter only through approved **offline media** with documented custody, malware checks, artifact signature/hash verification, staging, rollback and operator approval. There must be **no inbound or outbound network connection**. A firewall rule or disabled Wi-Fi icon alone does not establish physical disconnection.

NIST SP 800-207 explains that zero trust assumes no implicit trust “based solely on their physical or network location.”[^nist-deploy-23] This supports explicit identity and access testing in private and on-site designs, but **does not certify** any deployment class as sovereign. NIST AI RMF 1.0 **Map 4.1** calls for documented approaches to component-level technology and legal risks, including third-party software and data; **Govern 6.2** addresses contingency processes for third-party failures.[^nist-rmf-deploy-23] These are voluntary risk-management references, not a substitute for local legal advice or vendor-specific proof.

#### Fictional UAE industrial-group decision: three workloads, four viable questions

The following organization, requirements and outcomes are **synthetic teaching examples**, not assertions about real UAE law, vendors or infrastructure.

| Workload and binding requirement | Candidate | Eligibility | Evidence still needed |
|---|---|---|---|
| **POL-23:** synthetic employee handbook; approved named processing sites | Managed regional service | **CONDITIONAL** | Endpoint configuration, access, retention, support, backup, failover, legal and procurement review |
| **ENG-23:** proprietary engineering manuals, embeddings and outputs stay within **one named factory premises** | Hosted private cluster in another UAE city | **REJECT** | Off-premises location alone conflicts with the signed requirement |
| **ENG-23:** same requirement | Factory-local private RAG and model serving | **CONDITIONAL** | Quality/latency, capacity, key custody, logs, no-egress, local backup and offline restart |
| **OPS-23:** disconnected operations reference; **no inbound or outbound network** | Edge appliance with remote fleet telemetry | **REJECT** | Remote telemetry violates the air gap regardless of device location |
| **OPS-23:** same requirement | Disconnected local enclave with controlled offline media | **CONDITIONAL** | Physical disconnection, media chain of custody, offline model licensing, rollback, operator drill |

**Hybrid nuance:** The group can use managed AI for POL-23 and an isolated local system for ENG-23. This is a *portfolio-level hybrid* architecture, not permission to forward ENG-23 prompts, embeddings, diagnostics or backups to the managed endpoint. A cross-boundary model fallback must default to **disabled**. For OPS-23, even an approved remote-support tunnel contradicts the mandatory air-gap requirement.

**Trade-off calculation:** Compare eligible designs using measured quality on a synthetic task set, p95 latency under realistic concurrency, recovery time, annualized infrastructure and support cost, change-management workload, licence rights and a supplier-exit drill. Do not invent universal prices or GPU throughput. Record the test environment, version, workload size, confidence interval where applicable and owner. If a local model fails minimum quality or capacity and the requirement cannot be changed by its legitimate owner, mark **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**; do not silently substitute a remote API.

#### Failure simulation and root-cause analysis: “local” edge with remote telemetry

**Fictional observation:** ENG-23 pilots a factory-floor edge device. Inference and vector search are local, but the device-management agent exports sampled error traces containing a synthetic restricted marker to an external fleet dashboard. The network test detects a forbidden destination. **The territorial requirement fails**, even though local inference latency is acceptable. This is a simulated acceptance failure, not a claim of an actual incident.

| RCA stage | Finding and accountable action |
|---|---|
| **Impact / decision** | **BLOCKED** for restricted data; retain synthetic trace, route and build version as evidence |
| **Direct cause** | Fleet agent's default diagnostic collection includes a prompt-output excerpt |
| **Contributing gap** | Architecture review classified the appliance as “edge/on-prem” without tracing the management plane and error-handling path |
| **Containment** | Platform owner disables outbound diagnostics and closes the network route; security lead checks for other outbound dependencies |
| **Corrective architecture** | Replace remote fleet management with approved local monitoring or disable the feature entirely; establish deny-by-default egress and configuration tests |
| **Retest / closure** | Replay synthetic errors, normal requests, restart, update, failover and recovery; inspect packet traces and local logs, verify no forbidden destinations and obtain data-owner sign-off |

**Root cause:** The team treated *compute placement* as proof of *end-to-end processing containment*. The correction is not merely to rename the device “private”; it is to verify the entire data and management path and make the failed condition a release-blocking regression test.

#### PM artifact: deployment eligibility and evidence matrix

A procurement or architecture review should produce this minimum record for **ENG-23**:

| Field | Example decision |
|---|---|
| Requirement ID / owner | SITE-ENG-23; engineering data owner |
| Non-negotiable boundary | One physical factory premises, including derivatives, support and recovery |
| Class considered | Edge/local private appliance |
| Known failure | Remote fleet telemetry exported synthetic restricted marker |
| Gate and evidence | **FAILED** territorial egress; packet capture, software version and test ID retained |
| Operational / technological unknowns | Admin revocation, offline entitlement, model quality, GPU headroom and restore still **UNVERIFIED** |
| Corrective owner / due criterion | Platform lead to remove remote telemetry and demonstrate local monitoring; security lead to rerun no-egress drill |
| Release decision | **BLOCKED** until all hard constraints pass; do not compensate with a favorable weighted score |
| Reopen triggers | Vendor update, new support path, failover change, model/runtime change or new derivative type |

**Learner challenge (30 minutes):** Open the [Architecture & Learning Studio](../learning/index.html). Select **Strict on-premises IP research assistant** with **Single premises only; no data or derivatives may leave**. Compare **Approved managed AI platform** with **On-prem production GPU servers inside the premises**; explain the hard eligibility difference before discussing cost. Then choose **Air-gapped factory operations** and attempt **General internet access including external service endpoints**. Record the rejected connectivity requirement. Finally sketch a hybrid portfolio with a synthetic public-document assistant and a restricted factory assistant: identify the network, support and evaluation interfaces that **must not** cross between them.

**Submission:** A six-row deployment-class matrix with one concrete allowed/prohibited flow per class, a four-row eligibility decision for the fictional workloads, and one RCA/retest entry. State which conclusions are tested, which are vendor assertions, and which require specialist legal review. The Studio is a teaching simulator, not proof of a production configuration.

**Exit check:** Can an in-country managed service satisfy a physical single-premises constraint? **Not when restricted processing leaves that premises.** Is an edge appliance inherently air-gapped? **No.** Can a hybrid portfolio contain both restricted and managed workloads? **Yes, only with verified segregation and no prohibited cross-boundary flow.**

**Sections 2.1–2.3 complete.** Section 2.4 below extends the deployment comparison into a component-by-component control and evidence map.

[^nist-deploy-23]: NIST, *Zero Trust Architecture*, SP 800-207, final August 2020, [official abstract](https://csrc.nist.gov/pubs/sp/800/207/final), accessed **20 November 2026**. The short quotation concerns trust and identity, not sovereignty certification.
[^nist-rmf-deploy-23]: NIST, *Artificial Intelligence Risk Management Framework 1.0*, NIST AI 100-1 (2023), [AI RMF Core, Map 4.1 and Govern 6.2](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), accessed **20 November 2026**. The source is voluntary risk guidance; the six-class taxonomy is course-authored.


### 2.4 Sovereign AI stack components: from facilities to operations

**Product decision:** Treat the sovereign AI stack as **twelve dependency layers and four cross-cutting control dimensions**, not as a shopping list of locally hosted technology. A facility can be in the permitted geography while an update service, model endpoint, privileged account, evaluation sink or backup crosses the forbidden boundary. Before approving an architecture, name each layer's owner, operator, allowed flows, replaceability and test evidence.

A practical stack spans **physical facilities, chips, compute, network, storage, data, models, platforms, applications, identity and access management (IAM), security, and operations**. IAM, security and operations are not just the final three boxes on an architecture diagram: they cut across every other layer. A PM should not infer that a company must manufacture chips or own buildings to meet a scoped objective. It must show that external dependencies cannot bypass the *specific requirements* for the workload.

#### Twelve layers, twelve evidence questions

| Layer | Component or decision under examination | Control owner and evidence to request | Example of a failed claim |
|---|---|---|---|
| **1. Facilities and utilities** | Site, power, cooling, racks, physical access and resilient capacity | Facilities lead: site inventory, access badge test, power-failure drill and repair contracts | Server is in an approved country but outside the *required factory premises* |
| **2. Chips and firmware** | CPU/GPU or accelerator, boot chain, device firmware and replacement supply | Platform hardware lead: asset origin, firmware/update path, inventory, capacity and failure test | Local inference fails because no replacement accelerator can be obtained in the agreed recovery window |
| **3. Compute and runtime** | Host OS, hypervisor, containers, scheduler, model execution engine | Platform SRE: administrator map, approved capacity tests, runtime image digest and offline restart | A licence-entitlement call blocks local inference when supplier links are disabled |
| **4. Network** | Segmentation, routing, DNS, proxy, private links, update and remote-support channels | Network/security leads: deny-by-default rules, observed destinations and change-triggered egress regression | "Isolated" subnet has an unnoticed outbound support tunnel |
| **5. Storage and recovery** | Object/file/block stores, snapshots, replication, key custody and restore | Storage lead: snapshot destinations, recovery test, retention and deletion evidence | Recovery replicas are copied to an unapproved remote region |
| **6. Data and derivatives** | Source files, prompts, answers, embeddings, feedback, training or evaluation samples | Data owner: classification, lineage, destination inventory, purpose and deletion test | Evaluation extracts include restricted prompt content despite local inference |
| **7. Models and artefacts** | Weights, tokenizers, licences, provenance, adaptations and evaluation sets | Model lead: model card/license review, checksum, permitted use and replacement benchmark | A model is downloadable but its licence or runtime cannot support the required offline use |
| **8. AI platform** | Gateway, RAG pipeline, vector database, orchestration, inference/evaluation APIs | Platform architect: service map, tenant isolation, API access test, logs and versioned policies | A model gateway silently falls back to an external provider |
| **9. Applications and tools** | Business UI, connectors, agent actions, document ingestion and user authorization | Product owner: end-to-end workflow test, plugin permissions and failure behavior | The app sends a maintenance attachment to an external helpdesk |
| **10. IAM and secrets** | Users, service accounts, privileged support, keys, tokens and emergency access | IAM/CISO: role matrix, MFA where applicable, revoke/reissue and break-glass drill | Supplier access persists after contract termination |
| **11. Security and assurance** | Threat modeling, patch and vulnerability management, logging, incident response and testing | CISO: threat model, signed test record, exceptions, incident and recovery exercise | A green encryption checkbox is accepted instead of an egress test |
| **12. Operations and supplier exit** | Monitoring, change control, backups, support, patch intake, spares, rollback and decommissioning | Operations/procurement: RACI, runbooks, portability rehearsal, support trace and deletion attestation | A vendor update changes the data destination without reapproval |

This is a **course-authored decomposition**. It provides a curriculum map, not an official reference stack or certification. The underlying [ontology](../taxonomy/ONTOLOGY.md) can represent **Workload → dependsOn → Component → operatedBy → Actor**, while **Requirement → addressedBy → Control → testedBy → Test → produces → Evidence** connects architecture to a release decision. A shared component may serve multiple workloads, but a test of one workload does not automatically prove the controls for another.

**Official source boundary:** NIST AI RMF 1.0 *Map 4.1* explicitly includes AI-system component risk arising from “third-party data or software.”[^nist-map-stack24] NIST SP 800-161 Rev. 1, updated 1 November 2024, addresses “identifying, assessing, and mitigating cybersecurity risks throughout the supply chain.”[^nist-scrm-stack24] NIST SP 800-207 states that zero trust does not confer implicit trust “based solely on their physical or network location.”[^nist-zt-stack24] These sources justify component, supplier and identity-risk evaluation; **none** establishes the course's twelve-layer stack or verifies a sovereign-AI deployment.

#### Two maps: data plane versus control plane

The **data plane** carries prompts, retrieved chunks, embeddings, model outputs, evaluation samples and application attachments. The **control plane** installs software, changes network policy, administers keys, supports users, monitors health, backs up data and controls failover. A control-plane action may cause data movement, so inspecting only prompt traffic is insufficient.

\`\`\`text
DATA PLANE (restricted site)
User -> Application -> Retrieval index -> Local model -> Response
                     \-> Local evaluation and audit sink

CONTROL PLANE (restricted site)
Enterprise IAM -> Admin console -> Runtime / update controls
Local monitoring -> Local backup -> Local restore

External supplier / cloud / support destination
    X No restricted data or derivatives may cross this boundary
    X No unapproved admin or diagnostic channel
\`\`\`

*Diagram reading:* The crossed paths are requirements, **not proof** that software obeys them. A site-level review traces firmware and model update intake, diagnostics, exception handling and disaster recovery. An air-gapped variant forbids **all inbound and outbound network connectivity**; offline signed media and locally audited maintenance replace online update channels. Physical media and people still need controls.

#### Fictional UAE enterprise: shared governance, separate stack footprints

**Case (fictional UAE industrial group):** Three product teams want a common enterprise AI platform. Their use cases are (A) public/synthetic policy drafting, (B) proprietary factory engineering search and (C) an air-gapped operations reference. The group wants to reuse evaluation code and IAM policies, but **cannot reuse the same remote runtime or monitoring endpoint** for all three.

| Workload | Critical physical and network boundary | Eligible architecture hypothesis | Compulsory residual checks |
|---|---|---|---|
| **PUBLIC-24:** policy drafting using synthetic material | Named permitted processing locations, no restricted customer content | Managed inference platform **conditionally eligible** | Endpoint/deployment class, logs, subprocessor/support access, contracts, costs and evaluated output quality |
| **PLANT-24:** restricted engineering RAG | **One named physical factory premises; no data or derivative exits** | Local compute and local model, index, logs, keys and backup **conditionally eligible** | Capacity, denied egress, runtime entitlement, on-site supplier service, restore and model licence |
| **OT-24:** disconnected reference assistant | **Air-gapped: no inbound or outbound network** | Fully local, disconnected serving with controlled offline artefacts **conditionally eligible** | Approved removable-media intake, integrity verification, rollback, physical security and safe operation |

**Design option 1, one managed platform:** operationally simpler for PUBLIC-24, **REJECT** for PLANT-24 and OT-24 if traffic leaves their prohibited boundaries. **Option 2, one regional enterprise data center:** may serve less restrictive workloads, but remains off-site for the plant. Owning a distant facility does not satisfy PLANT-24. **Option 3, segmented portfolio:** share non-sensitive policy templates and code through approved, reviewed releases; operate separate local model/data stacks for the restricted workloads. This costs more in hardware, operations and duplicated verification, but is the only eligible *class of design* among these options under the fictional hard boundaries. Eligibility is not proof of a passing implementation.

**Capacity and cost:** Measure tokens/sec or task latency, concurrency, model quality, accelerator headroom, power, equipment replacement, skilled support, update operations and restore objectives using synthetic tests. Do not invent benchmark numbers, cost savings or a “sovereignty premium.” If PLANT-24 cannot meet acceptable model quality on local equipment or OT-24 cannot obtain legally usable offline artefacts, record **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**. Neither can silently fall back to the managed API.

#### Failure exercise and RCA: an apparently local stack with an external control plane

**Test observation, fictional:** PLANT-24 performs inference, storage and retrieval on-premises. During a simulated runtime crash, an observability agent packages exception traces with synthetic restricted-label prompt fragments, then attempts HTTPS upload to the supplier's managed diagnostics account. A deny-egress rule blocks the connection. The immediate test does not prove that production data escaped, but it shows a **forbidden management/data flow** and the design cannot pass the physical-site requirement yet.

| RCA step | Finding, owner and required response |
|---|---|
| **Symptom and status** | Synthetic diagnostics tried to cross the single-premises boundary; **BLOCKED** for restricted launch |
| **Direct cause** | Preconfigured observability agent used a remote diagnostic collector |
| **Contributing process gap** | Stack review mapped database, inference and GPU ownership but excluded control-plane exception reporting and vendor service tools |
| **Containment** | Platform team retains the outbound deny, disables the agent's remote upload, preserves synthetic trace evidence and checks historical route logs |
| **Correction** | Switch to a fully local diagnostic sink or remove the agent, approve offline/supervised support, update the component and derivative inventory |
| **Independent retest** | Replay normal, crash, update, backup, failover and restore scenarios; examine packet/DNS/firewall traces, privileged sessions, local artifacts and actual destination configuration |
| **Closure** | Dated versioned results reviewed by security and plant data owners; no restricted-data release before the hard boundary passes |

**Root cause:** The team evaluated **where the AI workload executes** but not **where its control plane operates**. An isolated data plane can still be coupled to an externally managed diagnostic system. A blocked connection protects this particular test, but an attempted prohibited route is a design defect that needs remediation and retesting.

#### PM artifact: stack ownership, failure and evidence ledger

For each of the twelve layers, the PM should record **component ID, vendor, legal owner, actual operator, physical location, data/control-plane connections, lifecycle stages, licence/exit rights, mandatory requirement, evidence owner, test ID, evidence date and disposition**.

A concise example for PLANT-24:

| Entry | Decision record |
|---|---|
| **Claim** | SITE-PLANT-24: restricted content/derivatives remain inside named plant premises under normal and degraded operation |
| **Layer and dependency** | 12 / observability agent; supplier-operated diagnostic endpoint is a cross-boundary dependency |
| **Authority** | Plant data owner sets prohibition; platform owns configuration; security validates paths; procurement owns vendor service terms |
| **Acceptance test** | Inject synthetic prompt marker, trigger model fault, record all outbound attempts; also verify backup, support and recovery flows |
| **Observed evidence** | **FAILED / BLOCKED**: attempted HTTPS diagnostics to off-site collector, test version and trace retained |
| **Solution and closure** | Local-only sink, revised supplier support runbook, regression test and independent sign-off |
| **Alternative if infeasible** | Reject the proposed supplier component or record unfulfilled requirement; never reclassify the site boundary as “country only” |

**Prioritization rule:** Screen hard placement, network, operational authority, model licence and minimum quality constraints **before** weighting throughput or price. For eligible options, compare total cost and residual dependencies with documented assumptions. Red, amber or green scores cannot compensate for a failed no-egress or air-gap gate.

**Learner challenge (35 minutes):** Start in the [Architecture & Learning Studio](../learning/index.html) with **Strict on-premises IP research assistant**. Keep **Single premises only; no data or derivatives may leave**. Change only compute from **On-prem production GPU servers inside the premises** to **Approved managed AI platform** and predict the hard feasibility result. Return to local compute, then switch operator to **Approved contractor, physically on-site under enterprise control**. Name the additional administrator, support-media and contract evidence required.

Next choose **Air-gapped factory operations** and attempt **General internet access including external service endpoints**. State why neither an allowlist nor a country-resident endpoint would fix the mismatch. Create a **twelve-row stack ledger** for a fictional PLANT-24 pilot. Mark three entries **UNVERIFIED**, one **FAILED**, and propose a falsifiable test for each. Explain why the Studio can suggest a pattern but cannot inspect firmware, verify licences, read actual network logs or certify compliance.

**Exit check:** Does local GPU ownership establish control over all twelve layers? **No.** Is managed compute necessarily wrong for every workload? **No**, only when its actual boundaries conflict with scoped requirements. Does a suitable local model make an air-gapped workload ready? **Not until** offline integrity, capacity, operations, physical security and recovery controls are tested.

**Sections 2.1–2.4 are complete.** The next section separates model rights from hosting and platform authority.

[^nist-map-stack24]: NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (2023), [AI RMF Core, Map 4.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Short direct phrase checked against official NIST AI RMF results **20 November 2026**. This is AI risk mapping, not a sovereign-AI stack specification.
[^nist-scrm-stack24]: NIST, *Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations*, SP 800-161 Rev. 1 (May 2022, updated **1 November 2024**), [official abstract](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final). Direct phrase checked on the official HTML page **20 November 2026**. General C-SCRM guidance, not a sovereignty certification.
[^nist-zt-stack24]: NIST, *Zero Trust Architecture*, SP 800-207 (August 2020), [official abstract](https://csrc.nist.gov/pubs/sp/800/207/final). Direct phrase checked on official HTML **20 November 2026**. The principle concerns authorization and trust rather than sovereign-AI ownership.


### 2.5 Model ownership vs. model hosting vs. platform control

**Executive decision:** An enterprise can own a model and still have no control over where it runs, who can change its inference routing, or where prompts and logs travel. Conversely, an enterprise can license third-party weights and operate them entirely under an approved physical boundary. Evaluate three independently testable claims: **model rights**, **model hosting** and **platform control**. A procurement declaration such as “we own the AI” is not an acceptance criterion.

This distinction matters most when a supplier sells a downloadable model together with a managed gateway. Rights to copy weights do not automatically include rights to modify, redistribute or run the model offline; a locally served model is not automatically free of cloud dependencies; and platform operators may have privileged access without owning the model.

#### The three rights-and-control questions

| Dimension | Actual decision | Evidence and accountable owner | A claim this does **not** establish |
|---|---|---|---|
| **Model ownership and usage rights** | Who owns or licenses the weights, architecture, tokenizer, adaptations and checkpoints? What use, redistribution, export and modification are permitted? | Model lead and procurement: exact version, licence text, artifact hashes, approved usage, permitted offline copies and exit terms | Where inference takes place; access to original training data; whether the platform controls logs or routes |
| **Model hosting and execution** | Where do inference, embeddings, evaluation, adaptation and recovery actually execute, including degraded mode? | Platform/SRE: host inventory, deployment type, endpoint/region configuration, actual flow traces and failover tests | Who may change gateway rules, recover keys, view prompts or invoke external support |
| **Platform control** | Who can deploy or remove models, administer IAM, manage keys, change routing, enable tools, retain traces and grant vendor support? | CISO/platform lead: administrator matrix, versioned policies, privileged-session records, revocation tests and incident drill | Model IP ownership, approved processing geography or specialist legal compliance |

**Separate asset custody:** The application's source documents, prompt history, embeddings, fine-tuning data, evaluation corpora and generated responses are not automatically owned or licensed under the same terms as the model weights. Maintain a distinct inventory for each data class and derivative. If a customer owns its training documents but the vendor controls the monitoring agent, ownership of the data does not prevent an unauthorized export.

The [course ontology](../taxonomy/ONTOLOGY.md) expresses the relationships without pretending they are a formal legal standard: **Enterprise licenses ModelArtifact; Supplier publishes Artifact; Operator hosts Runtime; Platform routes Requests; Requirement constrains Route; Test verifies Claim**. Keep model rights, technical operations and legal/contractual obligations as separate nodes and evidence fields.

**Source check:** The Open Source Initiative's *Open Source AI Definition 1.0* (approved October 2024) distinguishes **Data Information, Code and Parameters**. Its text requires “Open Source models” and “Open Source weights” to include the data information and code used to derive the parameters.[^osi-open-25] Hence a download link for model weights does **not**, by itself, demonstrate that the full system meets OSI's Open Source AI Definition. NIST AI RMF 1.0, *Map 4.1*, addresses technology and legal risks “including the use of third-party data or software”.[^nist-map-25] These are sources on openness and risk management, **not** a definition of sovereign AI, an IP entitlement for any particular model, or a compliance certificate.

#### Draw the decision boundary before comparing vendors

Use the following path as an architecture inspection checklist. A different supplier may own or administer each element:

**Model artifact and licence → inference host and runtime → model gateway → retrieval/application → outputs.**

**Platform-control path → IAM and keys → gateway policy → observability, updates and recovery.**

The second path can silently override the first. If the local inference server fails, the gateway might automatically select a remote model API. If the local logging service fails, an agent may send diagnostic bundles to a provider endpoint. If the locally installed model requires online entitlement renewal, it may be unable to restart in a disconnected environment. Review **normal operation, failures, support, updates, backup/restore and exit** instead of relying on a static deployment diagram.

| Candidate design | Model rights | Who hosts and controls the platform? | Suitable use and hard limitation |
|---|---|---|---|
| **Licensed model on an enterprise-operated on-site GPU** | Rights to run and maintain local artifacts must be reviewed | Enterprise operates gateway, keys, logs, storage and model; vendor access must be constrained | **CONDITIONAL** for a single-premises workload if no-egress, capacity, licence, operator and recovery tests pass |
| **Enterprise-owned model hosted by a managed regional service** | Enterprise may own specified adaptations or weights | Provider hosts part of inference and may hold administration or support authority | Could serve a workload that allows approved off-site locations; **REJECT** when restricted processing must stay inside one plant |
| **Downloaded open-weight model behind a vendor-managed gateway** | Model weights are available but usage rights still require inspection | Supplier can set fallback endpoints, diagnostics or privileged support | **BLOCKED** for a site-only workload if the vendor can reroute restricted requests without an enterprise-enforced deny |
| **Proprietary hosted model API** | Customer licenses use of an endpoint rather than possessing weights | Provider operates inference and much of the serving platform | Potentially efficient for public or synthetic-data pilots; not eligible for air-gapped or strict single-site workloads requiring remote inference |

**PM trade-off:** Provider hosting can reduce local infrastructure and staffing demands, but makes runtime behavior, service continuity and exit dependent on a supplier. Local hosting shifts GPU capacity, power, patching, safety, monitoring and incident response to the enterprise. Compare eligible designs using measured quality, latency, concurrency, licensing and recovery evidence. Do not invent a universal ownership premium or claim one model is accurate enough without a benchmark.

#### Fictional UAE industrial use case: one model contract, three different outcomes

A UAE engineering company proposes a common model contract for **CORP-25**, a synthetic public-policy writing assistant; **PLANT-25**, a retrieval assistant for restricted machine drawings at one physical factory; and **OT-25**, a disconnected reference tool in a controlled operations facility. These workloads, permissions and failures are invented for teaching; no real supplier behavior, UAE rule or customer incident is asserted.

**CORP-25:** Inference may use named approved locations. A managed model API is a **CONDITIONAL** candidate after source and output rights, actual data processing, diagnostics, vendor access, continuity, contracts and exit are examined. Owning the model weights is not mandatory for every possible bounded control objective.

**PLANT-25:** No restricted documents, prompts, embeddings, adapted weights, generated answers, diagnostic traces, evaluation samples, or backups may leave the **named factory premises**. A licensed model can be hosted on on-site GPUs behind an enterprise-managed gateway and local vector index. A supplier may retain the model IP while the enterprise retains permitted operating authority. This architecture is only **CONDITIONAL** pending data-flow, access, licence, offline restart, quality and backup tests. An in-country managed endpoint outside the plant is **REJECT** even if the enterprise owns the model.

**OT-25:** A stricter **air-gap** condition requires **no inbound or outbound network connectivity**. Online activation, remote support, cloud inference, live telemetry and automatic model updates are prohibited. Offline model installation needs a valid licence, artifact checksums/signatures, malware assessment, controlled removable-media custody, local monitoring, rollback and on-site operations. A premises-only network is **not** an air gap.

**Shared-governance design:** The enterprise may use one policy for model inventories, licenses and evaluations across the portfolio while keeping the actual inference networks and key stores separated. Copy approved code and model versions into disconnected environments through their offline intake process. Never allow PLANT-25 or OT-25 to inherit CORP-25's external fallback simply because one procurement contract covers all three.

If the only capable model requires cloud inference, or no permitted offline licence or local compute exists, record **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**. A PM cannot resolve the failure by silently weakening the site or network requirement.

#### Failure drill: the local model falls back to a remote host

**Fictional test setup:** PLANT-25 serves licensed model weights from a GPU in its factory. The platform gateway has a performance fallback configured by a supplier. A simulated local timeout occurs during the synthetic acceptance suite. The gateway sends the pending prompt to the provider's hosted model API. A restricted-label synthetic marker is visible in an off-site proxy request. The enterprise-owned GPU and model artifacts remain local, but its **platform routing violates territorial control**.

| RCA item | Finding and response |
|---|---|
| **Observed symptom and impact** | Off-premises model request during controlled failure test; **FAILED / BLOCKED** for restricted-data launch. No actual customer-data disclosure is asserted |
| **Direct cause** | Gateway retry/fallback rule included a remote inference endpoint |
| **Contributing process gap** | Procurement and architecture checks examined model licence and normal serving location, not degraded-mode routing or operator privileges |
| **Containment and accountable owner** | Platform engineer disables the external fallback and denies the outbound route; CISO team retains synthetic trace and checks historical access |
| **Corrective action** | Use a truly on-site fallback with matching controls, or return an explicit controlled failure under overload. Document capacity limits and gateway change approval |
| **Retest** | Inject synthetic timeouts, overload, reboot, gateway failure, update and restore events. Inspect DNS, proxy/firewall traces, logs and privileges to confirm no prohibited route |
| **Closure** | Dated evidence, versioned gateway policy, licence/access review and sign-off by data owner, platform lead and security. A configuration edit without a retest is not PASS |

**Root cause and prevention:** The product review confused **possession of model artifacts** with **effective authority over inference routes**. An operational feature introduced for availability changed the legal/territorial risk profile without a new architecture decision. Make fallback and support paths explicit release gates and reopen the claim when gateways, service configurations or model deployments change.

#### PM artifact: model–host–platform control card

Prepare one row for every asset/right and a different row for every executable control. For fictional PLANT-25:

| Record and accountable owner | Requirement / evidence state |
|---|---|
| **MODEL-25, model lead + procurement** | Licenced third-party weights/tokenizer and approved usage/offline copies; exact model version and licence review **PENDING** |
| **HOST-25, platform SRE** | On-site GPU, inference process, local vector storage and approved keys; capacity and no-egress evidence **UNVERIFIED** across full lifecycle |
| **GATE-25, platform/SecOps** | Remote fallback forbidden; gateway change rights, admin revocation and denied egress must pass |
| **DATA-25, factory data owner** | All restricted inputs, embeddings, derived material, prompts, outputs, logs and recovery copies remain on the physical premises |
| **EXIT-25, architecture owner** | Rebuild local inference from approved artifacts, change model without losing retrieval access checks, benchmark quality and rehearse rollback |
| **Release decision, PM** | **BLOCKED** because the synthetic degraded-mode request crossed the boundary. A passed model-licence check cannot override a hard territorial failure |

**Decision procedure:** First identify hard physical, network, model-rights and minimum-quality requirements. Reject ineligible hosting/control proposals. For those remaining, test model quality, administrator rights, offline resilience, capacity, backup and exit with synthetic inputs; then compare operating costs and support burden. Do not collapse rights, location, independence and compliance into one score.

#### Learner challenge (30 minutes)

Open the [Architecture & Learning Studio](../learning/index.html) and select **Strict on-premises IP research assistant** with **Single premises only; no data or derivatives may leave**. Change only compute from **On-prem production GPU servers inside the premises** to **Approved managed AI platform**. Explain why model ownership cannot rescue an off-site inference plan. Restore local compute and change operator from **Enterprise employees administer all layers** to **Provider administration permitted by contract**. Identify the new privileged-access and support-path evidence required.

Next select **Air-gapped factory operations** and set **General internet access including external service endpoints**. Predict the hard rejection. For the valid offline baseline, set portability to **Model artifacts, serving and data must be enterprise-portable**, then design a *no-network* model substitution drill covering license, hashes, tokenizer compatibility, retrieval authorization, quality evaluation, local restore and rollback. Distinguish the result the Studio can simulate from the tests only a real deployment can perform.

**Submission:** Four rows for model rights, runtime host, platform controls and data derivatives, each with the owner, boundary, test, evidence and disposition. Add a one-paragraph go/no-go memo and an RCA/retest for the remote fallback. Use only fictional or synthetic data. Facilitator answer details belong in the separate solutions artifact, not the public learner chapter.

**Exit check:** A downloadable model is not automatically OSI Open Source AI, owned training data or a verified portable platform. Enterprise-owned weights do not prove hosting locality. A licensed third-party model can be conditionally eligible for local hosting if every hard boundary and rights requirement is tested. A physical air gap never permits remote model fallback.

**Sections 2.1–2.5 complete.** The next section maps dependencies to testable autonomy claims.

[^osi-open-25]: Open Source Initiative, *The Open Source AI Definition 1.0* (adopted October 2024), sections “Preferred form to make modifications” and “Open Source models and Open Source weights”, [official OSI definition](https://opensource.org/ai/open-source-ai-definition), text checked **20 November 2026**. This source does not declare a particular model sovereign or commercially usable.
[^nist-map-25]: NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1 (2023), Map 4.1 and Govern 6.1, [official NIST Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), checked **20 November 2026**. Source addresses third-party technology/legal risk, not sovereignty certification.
[^nist-scrm-25]: NIST, *Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations*, SP 800-161 Rev. 1, updated **1 November 2024**, [official NIST abstract](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final), checked **20 November 2026**. Use to justify supplier and dependency review; no jurisdiction-specific legal conclusion.


### 2.6 Dependency and autonomy spectrum; why one-size-fits-all labels fail

**Decision first:** Sovereignty is not a binary vendor label. Ask what happens to a *named workload* when its supplier, network, licensing service, key authority or recovery site becomes unavailable. An enterprise may own a model and still be unable to restart it without a vendor licence server. Conversely, a third-party licensed model can be locally operable when its rights, runtime and dependencies are demonstrably compatible with the approved boundary. **Never average away a hard territorial or air-gap failure.**

The following **course-authored autonomy spectrum** is a teaching taxonomy, not an official standard or certification. Use the [ontology](../taxonomy/ONTOLOGY.md) relationships **Workload dependsOn Component**, **Component operatedBy Actor**, **Dependency has FailureMode**, **Test produces Evidence**, and **Evidence supports Claim**. The actual system can score differently across identity, inference, data, recovery and supplier exit.

#### Five autonomy postures

| Posture | What remains possible during supplier disruption? | Minimum proof and limitation |
|---|---|---|
| **A0 Provider-bound** | Inference stops when the external endpoint fails | Provider outage test; no claim of local autonomy |
| **A1 Interface-portable** | Gateway can target a replacement API | Rehearsed migration of prompts, embeddings, policies and access; interface portability does not guarantee model quality |
| **A2 Locally runnable** | Local model may continue inference without external API | Measured offline run and restart; licence, monitoring and identity may still be remote |
| **A3 Locally operable** | Inference, retrieval, identity, audit and restore run under local authority for a tested interval | Isolation, expiry, cold-start, backup and operator tests; replacement hardware may still depend on a supplier |
| **A4 Reconstitutable** | Enterprise can rebuild and substitute critical runtime components from approved artifacts | Export and recovery rehearsal, licences, artifact checks, quality benchmark and supplier revocation |

**Do not treat A0–A4 as a universal maturity score.** A4 exit readiness can coexist with an unlawful processing location, and an air-gapped A3 system may be dependent on a scarce accelerator. Assess **territorial, operational, technological and legal** controls separately, each with **PASS / FAILED / UNVERIFIED** and a test ID. A failed mandatory control yields **REJECTED**, regardless of the autonomy posture.

#### Dependency mapping across four paths

| Path | Dependency edges to inventory | Fault to inject |
|---|---|---|
| Request | User → IAM → retrieval/index → embeddings → inference → output | Expired identity token; embedding endpoint unavailable; gateway remote fallback |
| Control | Admin → secrets → gateway configuration → logs → diagnostics | Supplier support account retained; telemetry collector off site |
| Recovery | Snapshots → key custody → restore image → runtime licence → local restart | Licence refresh fails after power cycle; backup destination unreachable |
| Exit | Artifact export → substitute model → rebuild retrieval → evaluate → revoke supplier | Incompatible embedding space; missing redistribution rights; undocumented API |

**Evidence requirement:** For each edge capture owner, operator, physical location, data class, derivative flows, network destination, licence term, failure response, test, date and change trigger. Supplier count is not dependency count: one vendor may control several failure-critical services. Test normal, degraded, maintenance and recovery paths.

#### Fictional UAE industrial portfolio: different outcomes are correct

A **fictional** UAE engineering group proposes one AI contract for three synthetic-data teaching workloads. These are invented policies, not statements of UAE law or real deployments.

| Workload | Named hard constraint | Architecture comparison and decision |
|---|---|---|
| **PUBLIC-26**, synthetic public-content assistant | Approved named hosting locations | Managed inference may be **CONDITIONAL**, after endpoint, retention, access, export and outage checks. A0 can be sufficient |
| **PLANT-26**, restricted factory drawings | **All restricted data and derivatives must stay inside one named physical factory premises**, including prompts, embeddings, logs, evaluation, backup and support | On-site model, local IAM, retrieval, keys and diagnostics is **CONDITIONAL A3** pending tests. A regional managed endpoint outside the factory is **REJECTED**, even if it is in the same country |
| **OT-26**, disconnected reference | **No inbound or outbound network connectivity**, including remote support, licence checks, telemetry, updates and failover | Disconnected runtime with offline approved media intake is **CONDITIONAL A3/A4**. Any online dependency is **REJECTED** |

A common managed platform is simpler for PUBLIC-26 but cannot be reused for the restricted workflows if traffic crosses prohibited boundaries. A data center owned by the enterprise elsewhere in the UAE still violates the single-factory-premises condition. A segmented portfolio permits reuse of approved non-sensitive policy and code via controlled releases, not live cross-boundary gateways. Evaluate local GPU capacity, power, staff, spares, latency, quality and recovery against managed-service operating costs **only after** screening hard constraints. No invented throughput or AED savings are assumed.

If the only capable model requires cloud inference, offline licence rights are absent, or the site cannot provide minimum compute and safety quality, record **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**. Do not relax a factory or air-gap requirement to make a preferred supplier eligible.

#### Failure mode and RCA: locally hosted, remotely licensed

**Fictional synthetic acceptance drill:** PLANT-26 serves a model on its factory GPU. The team disconnects external network access for a planned 72-hour test. Inference works until a simulated power cycle and entitlement expiry. The runtime attempts a supplier licence refresh, the firewall denies it, and the model cannot restart. No production data leak is asserted. The architecture has failed operational continuity even though its inference hardware remains local.

| RCA stage | Observation, owner and correction |
|---|---|
| Symptom | **FAILED / BLOCKED**: cold restart impossible without external entitlement; local continuity requirement unmet |
| Direct cause | Runtime requires an online licence service during restart |
| Contributing process gap | Procurement tested warm inference but omitted entitlement expiry, reboot, vendor outage and supplier exit |
| Containment | SRE keeps deny-egress policy, preserves synthetic logs and blocks unauthorized licence exceptions |
| Solution | Procurement secures lawful offline entitlement or replaces the runtime; platform team retains approved artifacts, keys and restore process locally |
| Retest | Repeat 72-hour isolation, expiry, cold restart, restore, update and gateway-failure tests with synthetic inputs; capture egress traces and quality/recovery measures |
| Closure | Dated evidence and data-owner, security and platform sign-off. Without a lawful offline solution, status remains **NOT FEASIBLE** |

**Root cause:** Local model execution was incorrectly treated as local *operability*. The hidden control-plane licensing dependency was never tested under failure. An air-gapped design must never be repaired by opening a network path, even to an in-country provider.

#### PM artifact: autonomy dependency and release register

| Field | Fictional PLANT-26 example |
|---|---|
| Claim and authority | AUT-PLANT-26; factory data owner owns the single-premises rule and local continuity requirement |
| Critical edge | MODEL-RUNTIME-26 → external supplier entitlement service; supplier operates endpoint |
| Evidence and test | Synthetic 72-hour isolation, expiry, cold-start and restore; versioned firewall, licence and service logs |
| Result | **FAILED** local restart; no-egress attempt blocked; other lifecycle egress paths **UNVERIFIED** |
| Correction owner | Procurement to validate licence, SRE to replace or reconfigure runtime, security to retest |
| Decision | **BLOCKED** until required hard constraints and local continuity pass; do not compensate with favorable portability or cost |
| Reopen triggers | Licence renewal, new model/runtime, firmware update, vendor support change, gateway fallback, key rotation |

#### Learner challenge (35 minutes)

In the [Architecture & Learning Studio](../learning/index.html), select **Strict on-premises IP research assistant** with **Single premises only; no data or derivatives may leave**. Compare **Approved managed AI platform** with **On-prem production GPU servers inside the premises**. Explain the hard eligibility difference before considering cost. For local compute, select **Model artifacts, serving and data must be enterprise-portable** and design a migration rehearsal with offline licence, tokenizer, embedding compatibility, retrieval access, quality thresholds and supplier credential revocation.

Then select **Air-gapped factory operations** and attempt **General internet access including external service endpoints**. Explain why private links, allowlists and domestic endpoints still fail the no-network rule. Submit five autonomy posture rows, eight critical dependency edges across the four paths, a fictional cold-restart RCA and a testable go/no-go decision. Label simulated versus real evidence; the Studio cannot certify actual networks, licences or compliance. Learner answers belong in the submission; facilitator solutions remain separate.

**Exit check:** Local weights do not guarantee offline continuity. API compatibility does not guarantee migration quality. A domestic data center outside a specified premises does not satisfy the premises-only rule. An air gap cannot depend on any external network service.

**Section 2.6 complete.** The autonomy spectrum above feeds the evidence-driven maturity and release gates in Section 2.7 below.

**Evidence boundary:** The A0–A4 spectrum is course-authored. NIST AI RMF 1.0 Map 4.1 addresses third-party data/software risks.[^nist-autonomy-26] NIST SP 800-161 Rev. 1 addresses cybersecurity supply-chain risks.[^nist-scrm-autonomy-26] NIST SP 800-207 cautions against implicit trust based solely on physical or network location.[^nist-zt-autonomy-26] These sources were reviewed for prior sections on **20 November 2026**; no fresh source fetch or sovereignty certification is claimed in this iteration.

[^nist-autonomy-26]: NIST, *AI Risk Management Framework 1.0*, NIST AI 100-1 (2023), [AI RMF Core, Map 4.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Previously reviewed 20 November 2026.
[^nist-scrm-autonomy-26]: NIST, *Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations*, SP 800-161 Rev. 1 (May 2022; updated 1 November 2024), [official publication](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final). Previously reviewed 20 November 2026.
[^nist-zt-autonomy-26]: NIST, *Zero Trust Architecture*, SP 800-207 (August 2020), [official publication](https://csrc.nist.gov/pubs/sp/800/207/final). Previously reviewed 20 November 2026.


### 2.7 Sovereignty maturity, evidence, gaps, and scorecards

**Decision first:** A sovereignty maturity score is a **diagnostic aid**, not permission to release a workload. The PM must first evaluate the binding requirements, especially physical processing boundaries, no-network conditions, operator rights and applicable obligations. A confirmed failure of any non-negotiable requirement results in **BLOCKED** or **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**. Only eligible candidates should be compared on capability, maturity, cost or portability.

A defensible scorecard has **two separate outputs**: (1) a **release disposition** based on hard gates and evidence, and (2) a **maturity profile** showing how consistently controls are defined, exercised, reviewed and maintained. Presenting only a total percentage conceals important gaps. These scales are **course-authored educational models**, not a NIST maturity level, national standard, legal determination or certification.

#### M0–M4: a capability progression, not a certificate

| Maturity stage | What the workload team can actually demonstrate | Minimum evidence expected | What remains unproven |
|---|---|---|---|
| **M0: Undefined** | Scope, control owners or boundaries are absent or contradictory | Workload inventory, outstanding discovery questions | Any sovereignty or compliance assurance |
| **M1: Declared** | Requirements and architecture assertions are recorded and approved in principle | Signed requirement register, deployment diagrams, named vendors and owners | That runtime behavior matches the diagram |
| **M2: Implemented** | Controls exist in a reproducible configuration | Configuration snapshots, policy/routing files, role assignments, contract/licence review | That normal, failure, support and recovery paths pass tests |
| **M3: Verified** | Acceptance tests for applicable hard constraints have passed in the precise tested configuration | Dated synthetic test traces, reviewer sign-off, version/scope IDs, model-quality and restore results | That controls remain effective after updates or changed operations |
| **M4: Sustained** | Repeated monitoring and change-triggered retests demonstrate continuing control | Change-control records, regression runs, access revocation exercises, incident/exit drills, evidence renewal cadence | Absolute risk elimination or universal legal compliance |

**Scoring rule:** Record a maturity stage **per required control dimension** (territorial, operational, technological, legal/contractual). Mark **UNKNOWN** when there is insufficient evidence; never treat UNKNOWN as M0 or as a passing M3. Compute a single *minimum stage* only over dimensions with valid evidence, alongside a conspicuous **coverage count**. It is invalid to report “M3 overall” when the legal/contractual column is UNKNOWN or the territorial column has a failed hard gate. For board reporting, prefer four labeled dimension stages plus an explicit disposition.

The [course ontology](../taxonomy/ONTOLOGY.md) represents the evidence chain: **Workload has Requirement; Requirement constrains Dependency; Control enforces Requirement; Test probes Control; Evidence records Test; Reviewer assesses Evidence; Decision appliesTo Workload**. This is a course-authored representation. Distinguish artifact existence (M1–M2), observed operation (M3) and repeated assurance (M4); the same supplier contract or diagram cannot advance the score through all stages.

#### Evidence states are not maturity stages

A **maturity stage** describes a process capability, while an **evidence state** describes what has actually been demonstrated for a *specific claim*. Use both fields. For every requirement, maintain:

| Evidence state | Interpretation for release | Example source artifact |
|---|---|---|
| **NOT PROVIDED** | Treat the claim as **UNVERIFIED**; request the missing record | No export of routing policy, contract or test trace |
| **ASSERTED / DESIGN ONLY** | Supplier promise or architecture draft; not runtime proof | Vendor response, target diagram or checklist |
| **CONFIGURED** | Team reviewed a current setting; behaviors outside that setting remain untested | Dated gateway policy, IAM permissions, egress rule |
| **TESTED / NOT REVIEWED** | A test produced logs but acceptance criteria or independence of review are pending | Packet trace and test run ID without signed disposition |
| **VERIFIED FOR SCOPE** | Named reviewer accepted reproducible results, relevant model/version, workload, time and conditions | Signed acceptance record with test vectors and observed destinations |
| **ADVERSE / EXPIRED** | A known failure or a stale/out-of-scope result means the claim cannot be treated as verified | Prohibited egress trace; evidence predates gateway update |

An **expired** evidence record is not the same as a test proving a defect. It means **re-verification is required**; a confirmed **ADVERSE** result means the applicable hard gate is **FAILED**. Keep these distinctions visible. A reviewer may never certify unseen tests merely because a vendor chose the label “independently validated.”

NIST AI RMF 1.0 Section 5 states that its Core actions “do not constitute a checklist”.[^nist-rmf-score27] In *Measure 1.1* it calls for documenting risks that cannot be measured, and *Measure 1.3* discusses assessment by internal experts not responsible for front-line development or independent assessors. These points support recording unknowns, review roles and limits of inference. They do **not** establish this M0–M4 scale. NIST SP 800-161 Rev. 1 discusses how supply-chain risk can be amplified by an organization's “decreased visibility” into technology acquisition and development.[^nist-scrm-score27] This supports explicit evidence gaps for provider operations, without converting a questionnaire into proof.

#### Worked enterprise example: three distinct maturity profiles

**Fictional UAE industrial group:** Its portfolio contains **CORP-27**, a synthetic policy assistant allowed to use verified named processing locations; **PLANT-27**, a maintenance RAG assistant with restricted artifacts confined to one physical factory premises; and **OT-27**, an operations reference required to be physically air-gapped. No real company, law, supplier configuration or breach is asserted.

| Workload / design | Territorial evidence | Operational evidence | Technological evidence | Legal/contractual review | Release disposition |
|---|---|---|---|---|---|
| **CORP-27: managed endpoint using only synthetic data** | M2; deployment settings inspected, telemetry/failover not reviewed | M1; vendor admin authority declared | M2; API and exit design documented | UNKNOWN; specialist review pending | **UNVERIFIED**, not a “sovereign M2 pass” |
| **PLANT-27: enterprise-operated model and index on the factory site** | **ADVERSE**; synthetic crash trace shows off-site diagnostic upload | M2; approved role matrix but no revoke drill | M3; local cold start and quality suite accepted for specified version | M1; relevant support terms identified | **BLOCKED** regardless of the relatively strong model result |
| **OT-27: disconnected local model and local backup** | M3; physical/network isolation test accepted for tested configuration | M2; offline media access controls configured | M1; restore and rollback only planned | UNKNOWN; licence and supplier conditions not reviewed | **UNVERIFIED / NOT READY** until missing hard controls are tested |

**Interpret the table correctly:** CORP-27 may eventually be appropriate for its synthetic use case despite a lower maturity profile than PLANT-27 on model execution. PLANT-27 is ineligible because the site boundary failed. OT-27 has a plausible no-network design but lacks tested recovery and reviewed licence rights. A spreadsheet average of these results would be nonsensical. Maturity is evaluated **per workload and time**, not inherited from an enterprise platform purchase.

**Physical boundary is not negotiable through scoring.** For PLANT-27, nothing restricted may leave its *specific* factory premises: source documents, prompts, embeddings, outputs, adaptations, evaluation samples, telemetry, crash traces, support bundles or backups. An endpoint in the same country but outside the plant is still off-premises. For OT-27, **air-gapped means no inbound or outbound network connectivity**. A firewall with an approved outbound allowlist or a temporary remote maintenance tunnel is not a physical air gap.

**When local capacity fails:** A team must measure approved workloads, latency, concurrent usage, quality and restore demand on permissible hardware. If the design cannot meet the minimum product criteria with available local models and licences, record **NOT FEASIBLE UNDER CURRENT CONSTRAINTS**. Never quietly move restricted inference to managed compute and call the higher quality a compensating score.

#### Failure drill: a stale M3 badge hides a changed telemetry destination

**Fictional sequence:** In week 1, PLANT-27 passes a narrowly scoped network test and the team records a green *territorial M3* label. In week 3, an observability upgrade enables a remote crash collector. A synthetic prompt marker appears in a DNS/proxy trace during a simulated exception. The dashboard still shows the old M3 value because evidence was not linked to software version or revalidation triggers.

| RCA requirement | Finding and corrective action |
|---|---|
| **Symptom and impact** | A controlled crash produces attempted restricted-data egress; **territorial hard gate FAILED**, restricted-data release **BLOCKED** |
| **Direct cause** | Upgraded agent configuration changed the diagnostic collector from local to remote |
| **Contributing process gap** | Scorecard stored “M3 verified” without workload/version/date validity, destination inventory or a rule that invalidates evidence on change |
| **Containment** | Platform owner disables remote collector and holds the release; security preserves synthetic traffic evidence and assesses historical paths |
| **Corrective design** | Local-only diagnostics, explicit deny-by-default egress, change-control webhook/manual approval, a versioned evidence link and documented retest owners |
| **Retest** | Simulate normal inference, crashes, support, model updates, backup/restore and deletion. Inspect DNS/proxy/packet evidence, IAM privileges and actual sink configuration |
| **Closure** | Signed, dated results for the precise deployed version; clear ticket for the original adverse finding; independent reviewer disposition and updated maturity/claim status |

**Root cause:** The organization treated a past *verified state* as a permanent *attribute of the product*. M3 must be tied to a version, scope, test date and review condition. A fixed configuration is not a passing test. **M4** requires evidence renewal and monitoring, not merely more dashboard color.

#### PM artifact: a release-first maturity scorecard

Build one record per material claim and join it to the four-dimension dashboard. A sample for fictional PLANT-27:

| Decision field | Example |
|---|---|
| **Workload, owner and authority** | PLANT-27 / plant data owner; platform and security evidence owners |
| **Non-negotiable requirement** | SITE-27: no restricted input or derivative may exit one named factory premises in any lifecycle path |
| **Current hard-gate result** | **FAILED** on synthetic remote diagnostic trace; launch **BLOCKED** |
| **Dimension profile** | Territorial: prior M3 **invalidated** by adverse test; Operational: M2; Technological: M3 for tested version; Legal/contractual: M1, still requires specialist review |
| **Evidence record** | Workload ID, version/build hash, test ID, date/time, environment, allowed destinations, measured observations, reviewer and source link |
| **Gap ticket** | GAP-27 / platform lead / remove collector and retest; add cross-path egress regression and change-triggered evidence invalidation |
| **Expected closure** | Accepted no-egress tests including failure and recovery paths, reviewed source/contract restrictions, named decision-maker's signed disposition |
| **Reopen when** | Model, gateway, support contract, location, telemetry, backup, licence, network or site requirement changes |

For prioritization, first classify each gap as **hard-gate blocker, required assurance gap, or optional optimization**. Within each class, rank by impact, exposure, affected workloads, reversibility, delivery cost and testability. Record an accountable owner and date for remediation. A score of 86/100, a high NIST mapping score or a provider's marketing claim never waives a failed physical-site rule.

**Suggested board view:** Display for each workload **release disposition**, **four dimension stages or UNKNOWN**, **number of required claims with verified evidence**, **hard-gate failures**, **highest-priority open gap**, **last tested version**, and **next review trigger**. Avoid colors as the only status indicator; use literal statuses such as BLOCKED, UNVERIFIED, VERIFIED FOR SCOPE and NOT FEASIBLE. Score histories are useful for improvement, not an assertion that risk has disappeared.

#### Learner challenge (40 minutes)

In the [Architecture & Learning Studio](../learning/index.html), load **Strict on-premises IP research assistant** with **Single premises only; no data or derivatives may leave** and **On-prem production GPU servers inside the premises**. Change the evidence dropdown among **Architecture and contracts only**, **Runtime logs captured, no completed acceptance review**, and **A test reportedly violated a requirement**. For each state, describe what additional independent checks and release actions are needed. The Studio's evidence labels are teaching inputs, not genuine runtime test records.

Next load **Air-gapped factory operations**. Change connectivity from **Air-gapped: no inbound or outbound network** to **General internet access including external service endpoints**. State the hard failure before discussing maturity. Return to full disconnection and propose three offline acceptance tests: media integrity, clean model restart and local restore without an internet path. Finally compare a managed **Employee knowledge and policy assistant** using synthetic data and **Approved managed AI platform** compute; explain why this candidate can have a different maturity profile and still be considered for its own stated boundary.

**Submission:** A three-workload scorecard with four separate dimension ratings (or UNKNOWN), explicit evidence states, a hard-gate result, a remediation plan and a dated reviewer field. Include an RCA for the stale evidence badge and explain why the score is not certification. Keep answers out of this learner source and use synthetic data only; facilitator solutions belong in a separate assessment artifact.

**Exit check:** Can a maturity average release a workload with a confirmed premises violation? **No.** Does M3 prove indefinite assurance? **No**, evidence is valid only for the tested scope and version until a material change or review expiration. Does a physically disconnected system automatically meet operational and recovery objectives? **No.** Is UNKNOWN evidence a pass? **No.**

**Applied lab:** [Run the Module 02 release-first scoring lab](../labs/module-02/README.md). Its four cases, evaluator and unit tests are **synthetic teaching tools**; the lab intentionally blocks premises-only egress violations and air-gap network connections, and never certifies a real deployment. Use the results to prepare the four-dimension claim matrix and decision memo.

**Module 02 content checkpoint:** All seven TOC teaching headers and the dedicated synthetic scoring lab are now drafted. This is **not** module publication acceptance. The five-question assessment and decision scenario, separate facilitator solutions, HTML/social teaching assets, technical/security/source Review A, editorial/accessibility/assessment Review B, and remediation of any blocking findings remain required **before Module 03**.

[^nist-rmf-score27]: NIST, *Artificial Intelligence Risk Management Framework 1.0*, NIST AI 100-1 (2023), [AI RMF Core, Section 5, Measure 1.1–1.3 and Manage 1.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Exact short quotation and subcategory text checked **20 November 2026**. This source is voluntary AI risk-management guidance; the maturity stages, status codes and release gates above are course-authored.
[^nist-scrm-score27]: NIST, *Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations*, SP 800-161 Rev. 1 (May 2022, updated **1 November 2024**), [official publication and abstract](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final). Short quotation from the abstract checked **20 November 2026**. Supply-chain risk guidance, not a measure of sovereignty maturity.
