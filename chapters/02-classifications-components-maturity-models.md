# Module 02 — Classifying what must remain under control

> **Executive thesis:** Classify sovereignty requirements by whose objectives they serve, then identify the workload, control owners, and evidence. National, sectoral, enterprise and workload scopes can coexist, but a high-level policy or domestic hosting claim does not prove that one AI workload meets its actual physical, operational or legal boundaries.

| Course context | Detail |
|---|---|
| Part / week | I — Foundations / Week 2 |
| Audience | Enterprise AI PM making architecture and procurement decisions |
| Prerequisite | [Module 01: Who controls the intelligence?](01-sovereign-ai-fundamentals.md) |
| Current publication | **In-progress chapter, Sections 2.1–2.3**. Sections 2.4–2.7 and both module-critical reviews are pending |
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

**Next header:** 2.4, *Sovereign AI stack components*. Module 02 remains incomplete until Sections 2.4–2.7, lab, assessment, facilitator solutions, publishing artifacts and both critical reviews are completed.

[^nist-deploy-23]: NIST, *Zero Trust Architecture*, SP 800-207, final August 2020, [official abstract](https://csrc.nist.gov/pubs/sp/800/207/final), accessed **20 November 2026**. The short quotation concerns trust and identity, not sovereignty certification.
[^nist-rmf-deploy-23]: NIST, *Artificial Intelligence Risk Management Framework 1.0*, NIST AI 100-1 (2023), [AI RMF Core, Map 4.1 and Govern 6.2](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), accessed **20 November 2026**. The source is voluntary risk guidance; the six-class taxonomy is course-authored.
