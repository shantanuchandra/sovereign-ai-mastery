<!--
Module: 05
Part: II (Regional Policy, Regulation & Governance)
Week: 05
Status: DRAFT ONLY. Not published or approved.
Last updated: 2026-11-23
Source review date: 2026-11-23 (named official overview/guidance pages only; not a legal consolidation)
Reviewers: GPT-6 author self-check only; independent legal/accessibility/calibration review NOT COMPLETED
-->
# Module 05 — Laws, Regulation & Jurisdiction

> **Executive thesis:** Locating a model in a UAE data centre does not answer which privacy, sector, access or cross-border obligations govern an enterprise AI workflow. First identify the parties, data subjects, activity, locations, legal instruments and exceptions; then ask qualified counsel to settle applicability and translate that decision into contracts, technical controls and observable tests.

**Draft gate:** Module 04 is still HOLD. This Module 05 Markdown is an **unpublished working draft**, prepared on a separate branch. No legal, regulatory or production compliance sign-off is asserted. It incorporates and expands the existing public [Module 05 website teaching exemplar](../modules/05-laws-regulation-jurisdiction.html); the exemplar is not itself proof that this new source chapter has passed website conversion or review.

| Field | Value |
|---|---|
| Part / week | Part II, Week 5 |
| Audience | Intermediate AI PM, advanced enterprise controls |
| Study plan | 2 hours reading, 3 hours lab, 2 hours PM memo, 1 hour review |
| Prerequisites | [Module 02 taxonomy](02-classifications-components-maturity-models.md), [Module 03 requirements](03-enterprise-sovereignty-requirements-strategy.md), [Module 04 ecosystem](04-uae-gcc-global-sovereign-ai-ecosystems.md) |
| PM deliverable | Legal applicability and control-to-evidence matrix, for counsel review |
| Environment | Python 3.10+ standard library, synthetic records, no cloud/GPU |
| Governing constraint | No assumption that any geography or product label proves legal authority |

## 1. Executive brief: the decision that matters

**Fictional case: GulfCare Group.** A UAE-headquartered enterprise has one UAE mainland subsidiary, a DIFC subsidiary, an ADGM subsidiary and a Saudi affiliate. It proposes a multilingual employee-document assistant. A supplier hosts inference in a UAE region, but its technical support team outside the UAE can inspect crash logs and reset service credentials. The vendor presents a storage-region screenshot and a generic security certification.

**Decision:** **HOLD production approval** for regulated or restricted information. A screenshot may establish a selected storage setting, not the applicable rule, support access path, downstream telemetry route, legal basis, processor contract or onward disclosure. Authorize only a **synthetic-data discovery pilot** with explicit prohibitions on real personal data and an approved cleanup plan. Even that pilot must pass the relevant enterprise test-environment policy.

**What would change the decision:** An activity-by-entity inventory, current counsel-approved applicability memo, legal data-flow analysis, complete processor/subprocessor/support map, explicit control owners, tested deny-by-default destinations, contractual transfer safeguards where applicable, and acceptance evidence for each workload. Country-level sovereignty narratives from Module 04 cannot waive a named-site, physically disconnected or statutory requirement.

**No-AI alternative:** An access-controlled, manually curated search index or rule-based intranet knowledge base. Use it when precise extraction is adequate, or when no compliant and technically feasible AI design can satisfy a hard constraint.

## 2. Learning objectives

After this module the learner should be able to:

1. Keep legal jurisdiction, data residency, technical control and operational sovereignty as separate decision dimensions.
2. Triage UAE federal, DIFC, ADGM and Saudi regimes as **candidate** instruments, without declaring their applicability from cloud-region metadata.
3. Distinguish a statute, implementing regulation, official guidance, regulator assessment tool, contract, enterprise policy and supplier claim.
4. Draw cross-border paths through human support, prompts, retrieval, model logs, embeddings, backup/restore and licensing, not only primary storage.
5. Convert counsel-reviewed requirements into testable deny/allow conditions, audit records and vendor exit tests.
6. Defend a go/no-go recommendation in a six-question assessment with an explicit fail-closed incident RCA.

## 3. Taxonomy, ontology & the mental model

The course-authored ontology, [taxonomy/ONTOLOGY.md](../taxonomy/ONTOLOGY.md), distinguishes:

| Entity or relation | Precise PM interpretation | Example evidence |
|---|---|---|
| **Legal entity** | Contracting company and establishment/branch context, not a server | Trade/entity record reviewed by counsel |
| **Processing activity** | Who uses what information for which purpose, on whose instruction | Versioned activity inventory |
| **Legal candidate** | Instrument potentially governing a party/activity | Official current text and article; applicability status |
| **Controller / processor** | Role to be assessed under the specific instrument | Purpose/means and contract analysis |
| **Destination** | Physical/logical processing, storage, or viewing path | Traces, privileged-access logs and data-flow map |
| **Sovereignty constraint** | Distinct customer, sector, geographic or physical rule | Approved requirement ID with authority |
| **Control** | Mechanism implementing a requirement | Deny-by-default egress, token scope, key custody |
| **Evidence** | Observable bounded test or signed contractual record | Negative-path test ID and owner acceptance |

**Relationships (educational, not an official legal ontology):** entity *performs* activity; activity *uses* data and *engages* processors; instrument *may govern* entity/activity; reviewed obligation *requires* a control; control *is tested by* evidence. A server's region is an attribute of one destination, not a shortcut from entity to lawful processing.

~~~mermaid
flowchart LR
    E["Legal entity and role"] --> A["Processing activity"]
    A --> D["Data and derived outputs"]
    A --> V["Vendor and privileged paths"]
    E --> L["Candidate legal instruments"]
    A --> L
    L --> C["Counsel-reviewed applicability"]
    C --> R["Approved requirements"]
    R --> T["Technical and contractual controls"]
    T --> X["Tests and dated evidence"]
    V --> X
    D --> X
    X --> G{"Release gate"}
    G -->|all hard gates evidenced| P["Review for release"]
    G -->|gap or forbidden path| H["HOLD / BLOCKED"]
~~~

**Diagram reading order:** begin with the entity and processing activity. Only after identifying candidate instruments and getting counsel's scope ruling should the product team write binding acceptance tests. Vendor routes and data derivatives must also feed the release decision. This is a decision-flow illustration, **not** a compliance engine.

## 4. How it works: legal and technical deep dive

### 5.1 UAE federal personal data protection framework

**Decision:** Do not equate a mainland company, an Emirates ID in a record, and a UAE data centre with an automatic legal conclusion. The UAE government identifies Federal Decree Law No. 45 of 2021 as a personal-data framework.[^uae-overview][^uae-federal] The UAE AI Office also describes an extraterritorial aspect to its geographical scope.[^uae-ai-office]

**Regime triage:** For each activity ask counsel (a) who is the controller/processor, (b) whether the data and party fall within the law's scope and exclusions, (c) which implementing measures and other sector laws apply, (d) whether an access, transfer, profiling or retention condition is triggered, and (e) which version/language controls. The official text and actual applicability—not the marketing label—govern that review. Health, banking/credit, public authority and certain free-zone activity require explicit specialist scoping rather than assuming that one general law supersedes everything.

**PM requirements:** Maintain entity and subject-geography tags, a reviewed legal-basis record, purpose/retention boundaries, subject-rights workflow where applicable, and privileged access inventory. A law mentioning permitted transfer mechanisms does **not** create an unconditional licence to disclose overseas; counsel must assess the specific parties, safeguards, data and implementing framework.

**Exact official anchor:** The UAE government overview names “Federal Decree Law No. 45 of 2021”.[^uae-overview] This is evidence that an instrument exists, **not** that GulfCare's support workflow is lawful.

### 5.2 DIFC and ADGM data protection regimes

**Decision:** DIFC and ADGM have distinct data-protection frameworks and competent authorities. A DIFC subsidiary's application cannot inherit a mainland legal answer merely because its backend is in Abu Dhabi; the same is true in reverse.

| Regime | Official source checked | PM's immediate task | Unsafe inference |
|---|---|---|---|
| DIFC | DIFC Law No. 5 of 2020 legal database, as amended; Commissioner of Data Protection tools[^difc-law][^difc-tools] | Map the entity/activity against DIFC applicability and Articles 26–27 transfer assessment with legal counsel | Every DIFC-owned application automatically complies when stored inside UAE |
| ADGM | ADGM Data Protection Regulations 2021 guidance, especially Part 6 and Article 42(2) transfer safeguards[^adgm-guidance] | Identify exporter, importer, country, transfer scenario, processor terms and chosen safeguards | An SCC template, on its own, proves actual technical protection or that every transfer is permitted |
| UAE federal | Law No. 45 of 2021 and official federal overview[^uae-federal][^uae-overview] | Determine scope, exceptions and overlapping sector duties | Federal labels automatically resolve free-zone or sector applicability |

DIFC's official law portal shows a **2025 amendment** listing. Use the consolidated authoritative version and counsel review to avoid teaching a frozen 2020 text as the whole current regime.[^difc-law] Its official assessment tool offers “Data Export / International Transfers (Articles 26 & 27)” as a topic; the tool guides review but does not give legal permission on the enterprise's behalf.[^difc-tools]

ADGM's Office of Data Protection guidance explicitly discusses international transfers in **Part 6** and identifies standard contractual clauses as an appropriate safeguard under Article 42(2) in relevant circumstances.[^adgm-guidance] A safeguard is an element of a lawful transfer analysis; it does not prove that GulfCare's logs or support staff satisfy a contractual restriction. Obtain signed terms, subprocessor lists, authorization processes and technically observed route evidence.

### 5.3 Sector, government and critical infrastructure considerations

**Decision:** Legal and sector scopes are overlays, not optional examples. The UAE government identifies Federal Law No. 2 of 2019 as regulating ICT in health fields, including free zones; a separate Cabinet executive regulation exists.[^uae-health][^uae-health-exec] The UAE government also publishes a Critical Information Infrastructure Protection Policy description.[^uae-cii] Neither source alone determines that a fictional company is a regulated healthcare provider or designated critical operator.

A PM should ask: Does the planned model receive patient records, clinical notes, financial account data, government records, industrial telemetry or critical-operational details? Which regulator or customer-specific contract has authority? Does a sector rule supersede, coexist with or add to the general privacy analysis? Who authorizes remote diagnostics? What are the incident and retention consequences?

**Fictional physical-boundary counterexample:** PLANT-05 is an industrial subsidiary whose signed customer rule says that restricted data **and all derivatives** must remain in its named physical building. Even a UAE regional backup is **BLOCKED** by that enterprise rule. OT-05 is an explicitly physically air-gapped archive: no inbound or outbound connections, including support tunnels, online activation, telemetry, remote updates or disaster-recovery links. All paths must be examined; a firewall denial of a remote attempt is evidence of containment, **not** evidence of application conformance. These are **scenario constraints**, not universal national laws.

### 5.4 Saudi PDPL and data transfer considerations

**Decision:** Do not teach “Saudi PDPL means all AI must be in Saudi Arabia.” Ask which exact provision applies to the activity and whether the contemplated access qualifies as an international transfer or disclosure. SDAIA hosts the PDPL and an **explicitly distinct** Regulation on Personal Data Transfer Outside the Kingdom.[^ksa-pdpl][^ksa-transfer]

The PDPL's **Article 29** and the transfer regulation require a structured review of purposes, protection level, safeguards, exceptions and risk; the transfer regulation's **Article 4** sets out particular exemption cases, **Article 6** covers withdrawal/cessation situations, and **Article 7** addresses risk assessment.[^ksa-pdpl][^ksa-transfer] Whether a particular export is permitted depends on specific conditions, authoritative language and current amendments, as determined by counsel. A rule about safeguards does not mean a provider's generic terms are adequate.

**Architecture comparison:** For Saudi subsidiary files, compare (A) a local inference service with restricted administrative access, (B) a regional managed service with complete subprocessor and transfer controls, and (C) deterministic local search without generative inference. Do not rank them until counsel has recorded applicable requirements and security has tested each destination and privileged path. A named-premises constraint could reject both A and B if their logs or licences leave the approved building.

### 5.5 GDPR, EU AI Act and global comparisons

**Decision:** GDPR asks privacy/processing questions; the EU AI Act adds system-role, use-case, risk and deployment questions. They are not interchangeable. GDPR Articles 3, 28 and Chapter V (including Article 44) are starting points for territorial scope, processor governance and third-country transfer review, respectively.[^gdpr]

The EU AI Act's timeline is **version-sensitive**. The European Commission AI Act Service Desk's November 2026 enforcement FAQ states that Annex III high-risk system rules apply from **2 December 2027**, and high-risk rules for systems embedded in regulated products from **2 August 2028** under the then-current timetable.[^eu-ai-act] Do not transplant an earlier 2026 deadline from a stale slide deck or infer that every internal retrieval bot is Annex III high-risk. The exact role, use case and amended law must be reviewed.

For US, India and China comparisons, distinguish separate national/sector instruments and enforcement institutions; Module 04 introduced their policy ecosystems. Module 05 does **not** claim that these countries have a single comparable sovereignty statute or a universal local-hosting duty. Log the actual activity, data-subject nexus, legal owner, instrument and jurisdiction before making any compliance claim.

### 5.6 Residency, transfers, contracts, subprocessors and lawful access

**Decision:** Inventory **all** data and control-plane paths before calling a service regional or sovereign. A live model request can be local while support, tokens, telemetry, embeddings, training/evaluation samples or backups traverse forbidden routes.

| Path | Question the contract must answer | Test evidence |
|---|---|---|
| Prompt + retrieval chunks | Which processor, region and retention terms govern source text? | Egress captures, scoped request logs, retention config |
| Embeddings + vector index | Are derived representations covered by the same handling rules? | Storage and deletion mapping, restore drill |
| Crash logs + diagnostics | Can offshore support view customer strings or identifiers? | Role matrix, sanitized logging test, support-session audit |
| Admin keys + break glass | Who can initiate a read/export, from where and with what approval? | PAM test, key custody, revoked-access drill |
| Model updates + licensing | Does a cold restart depend on a remote endpoint? | Disconnected cold-start and licence-expiry tests |
| Recovery/DR | Where do encrypted snapshots, metadata and restored plaintext go? | Backup topology, restore destination trace |
| Subprocessors | Are actual contractual parties and onward transfers disclosed? | Current subprocessor schedule and change notices |

**Access is a separate legal and technical question:** An employee of a provider viewing identifiable logs from abroad may warrant transfer and access analysis even if durable storage stays inside a selected region. A customer-managed encryption key is valuable but does not by itself prove that vendor operators never see plaintext at runtime.

**Contract requirements to negotiate:** processing scope, purposes, data categories, locations, support/telemetry paths, onward subprocessors, security rights, audit evidence, incident assistance, retention/deletion, access-request handling, jurisdictional conflicts, sovereign change control, vendor exit and escrow/portability where justified. Counsel must decide which clauses are mandatory or effective; this table is a due-diligence checklist, not a universal legal template.

### 5.7 How legal jurisdiction differs from operational or technical control

| Question | Legal jurisdiction | Operational control | Technical control |
|---|---|---|---|
| Who decides? | Applicable laws, courts, regulators, contract and competent counsel | Service operator and accountable managers | System architects, IAM/security and platform operators |
| Proof | Instrument/version, applicability ruling, signed terms | Access records, SOPs, approvals, incident drills | Network, identity, key, trace, cold-start and restore tests |
| Typical blind spot | Assuming data location decides every duty | Outsourced privileged support | Region setting ignores control plane and backup |
| Failed claim | “We host in UAE, so all transfers are legal” | “Only our staff have access,” despite outsourced admin | “Our firewall blocked one attempted leak, so routing is correct” |

**Constraint logic:** a legal conclusion cannot be inferred from a positive architecture test, and a valid contract cannot override a physically prohibited path under a signed customer requirement. The release board needs **both** legal review and observed system evidence for the relevant claim.

### 5.8 Converting legal questions into reviewable requirements and evidence

Use one **traceability record per claim** with fields: activity ID, contracting party and role, data subjects/category, destination graph ID, instrument title/version/article, quote/pinpoint, counsel owner and applicability state, requirement ID, control owner, test method/ID, observed result, residual risk, date, gate, exception authority.

**Sample translation (illustrative, not legal determination):**

- *Candidate instrument:* ADGM Data Protection Regulations 2021, Article 42(2) transfer safeguard discussion in official guidance.
- *Counsel question:* Does a named ADGM entity export logs to this support provider, and which safeguard is suitable?
- *Product rule pending counsel:* HOLD real-person diagnostic logs until a support-access and contractual mechanism is approved.
- *Technical test:* DENY-SUPPORT-01, attempt a support-role log view from an explicitly unapproved identity; expect denial and a time-stamped alert with no log-content exposure.
- *Evidence limit:* Test shows enforcement for the tested identity/version only, **not** that the chosen legal mechanism is sufficient.

**Fail-closed classification:** A legal candidate with applicability UNKNOWN remains **NEEDS_COUNSEL**. A physical-site hard gate without observed proof remains **HOLD**. An observed forbidden transfer/remote support dependency is **BLOCKED**, even when egress perimeter controls contained the attempt. No weighted maturity score can turn an unverified hard gate into approval.

## 5. UAE/GCC case study: GulfCare's support logs

**Entire case fictional; no actual patient, employee or supplier data.** The PM's first inventory finds four processing activities:

| ID | Processing activity and entities | Potential obligation / open question | Initial decision |
|---|---|---|---|
| GC-01 | UAE mainland employee handbook search, synthetic excerpts | Confirm data-subject scope and retention policy | PILOT_SYNTHETIC_ONLY |
| GC-02 | DIFC staff queries; support logs include email identifiers | DIFC entity role, Articles 26–27, support/export contracts | HOLD |
| GC-03 | ADGM subsidiary uploads vendor complaints | ADGM role, data sensitivity, Article 42 safeguards, controls | HOLD |
| GC-04 | Saudi affiliate's procurement records and uploaded attachments | Saudi PDPL scope and Article 29/transfer regulation; supplier access | HOLD |

**Incident drill (fictional):** An overseas support engineer opens a diagnostic bundle with a synthetic employee identifier after a simulated model timeout. A storage dashboard still shows UAE region. **Direct cause:** logger retained identifiers and an offshore viewer role inherited debug access. **Systemic cause:** procurement reviewed storage residency but omitted the support control plane and log derivatives from the transfer and supplier inventory.

**Containment:** Disable the support viewer, turn off sensitive diagnostics, retain **synthetic** event identifiers, inspect whether another path exists, and keep GC-02/GC-03 on HOLD. **Corrective plan:** engineering implements redaction and scoped support; security enforces deny-by-default policies and tests under failed model/cold-restore conditions; legal reviews roles, transfers and provider contracts; procurement approves subprocessor terms; PM records sign-offs and alternatives. **Retest:** try unapproved foreign support, break-glass, expired licence, crash-report upload and restored backup; expected outcome is no forbidden content path. A blocked firewall attempt is a **failed application-path test** despite successful perimeter containment.

**Harder variant:** Customer PLANT-05 says all derivatives must remain inside its named premises; OT-05 prohibits *all* network links. A “UAE-only” cloud support option does not meet either condition. If no offline-licensed, recoverable implementation exists, return **NOT FEASIBLE UNDER CURRENT CONSTRAINTS** and present a manual/non-AI route.

## 6. Hands-on lab: build a legal-control-evidence graph

**Objective:** Build an offline, synthetic traceability matrix; confirm the validator rejects missing source references, ownership and unsafe release claims while allowing unresolved legal questions to remain unresolved. The baseline is Python 3.10+, standard library, 16 GB Apple Silicon (or any current laptop), no cloud account, GPU, API, Docker, external data or paid service. **Cost:** no paid infrastructure; local time only.

From the repository root on this **draft branch**:

~~~bash
python3 labs/module-05/validate.py labs/module-05/control_map.json
python3 -m unittest discover -s labs/module-05 -p 'test_*.py' -v
~~~

This lab deliberately checks **schema and fail-closed policy mechanics**, not the truth of source URLs, regulatory scope, presence of a physical air gap, or actual vendor compliance.

1. Inspect the JSON input. For each fictional activity, identify the legal candidate, law-review state, approved source pinpoint, technical control, owner, test evidence, and release status.
2. Run the validator and record its JSON-like summary: counts for HOLD, BLOCKED, PILOT_SYNTHETIC_ONLY and any exception; no blanket COMPLIANT outcome should appear.
3. Clone the input. Mutate one legal candidate from NEEDS_COUNSEL to APPROVED without adding a counsel-review record; the program must exit nonzero.
4. Separately change the physically disconnected OT-05's network route to ALLOWED; the validator must reject it even if the candidate passes other scores.
5. Mutate the named-premises PLANT-05 backup destination offsite and assert a BLOCKED/HOLD safety outcome. Restore the untouched baseline.
6. Write a 1-page lab evidence sheet with command, Python version, commit SHA, observed result, case ID, timestamp, defect/correction and what the test **does not prove**.

**Acceptance criteria:** All records have source title/URL/article, named owner, legal disposition, control ID and test ID; unknown legal applicability cannot become approved; hard boundary failures cannot become approved; references remain to separate primary documents rather than a vendor brochure. Tests must include both positive and negative cases. A future CI pass does not replace independent legal or physical-site assurance.

**Extension:** Add an event-sourced exception log and a separate independent reviewer role. Do not create automated legal clearance or infer duties using unvalidated language-model output.

## 7. AI PM decision playbook

| Gate | Decision question | Owner / minimum evidence | Gate outcome |
|---|---|---|---|
| Entity and activity | Which legal entity, subjects, data and use? | PM + privacy, signed inventory | Unclear: HOLD |
| Legal scope | Which instrument and amendment applies? | Qualified counsel, dated opinion and pinpoint | UNKNOWN: NEEDS_COUNSEL |
| Architecture | Which control, data and privileged paths exist? | Platform/security, versioned diagram and trace | Unknown: HOLD |
| Contract | Are terms and subprocessors consistent with observed flows? | Legal/procurement, signed DPA/schedules | Gap: HOLD |
| Security | Are source, logs, embeddings, licence and backup flows verified? | Security/operator, negative-path tests | Forbidden attempt: BLOCKED |
| Business | Is a no-AI route safer or more economic? | PM/finance, TCO and service-level trade-off | Record alternative |
| Release | Are **all** hard gates met and evidence accepted? | Named sponsor, counsel, security and data owner | Never infer from maturity score |

**Prioritization:** First remove candidates failing a hard law/customer/physical constraint. Then compare remaining choices on task utility, privacy risk, measurable access controls, staff support, cost, latency and vendor exit. Explicitly maintain an **unresolved** state when a source is old, a legal owner is missing or a provider refuses to disclose support paths.

## 8. Economics and operating model

Use the same assumptions for all candidates:

~~~text
Annual total cost of ownership =
  hosting + inference + storage + identity/security operations
  + privacy/legal review + supplier assurance + engineering
  + recoverability drills + incident response + exit/migration reserve
~~~

This is an accounting framework, **not a vendor-price estimate**. Record measured throughput, quote dates, cloud regions, contract term, labour rate, number of legal regimes, support window and backup strategy before reporting an AED amount. A more costly local deployment can still be the only eligible choice for a named-site constraint; where no eligible AI candidate exists, the no-AI option is a valid product decision.

**Operating cadence:** Approve a versioned legal-control register before pilot; recheck laws, vendors and support access on material change; log monthly negative-path evidence as a **course-authored proposed cadence**; require explicit owner review at every release. Do not call periodic self-tests a legal audit.

## 9. Anti-patterns, common mistakes and failure modes

- **Region-as-law:** a storage-region dropdown is neither a controller-role analysis nor an international-access assessment.
- **Generic GDPR/PDPL equivalence:** different regimes have different scope, instruments, exceptions and enforcement mechanisms.
- **Stale legal timelines:** calendar slides and search summaries can lag amendments, especially the EU AI Act. Read the official current text.
- **Contracts without system tests:** a contractual UAE-only promise does not prove no offshore diagnostics or support.
- **Tests without legal ownership:** green egress tests cannot decide that a transfer mechanism is lawful.
- **No-AI alternative omitted:** a procurement process may be unable to buy a legitimate model architecture inside the hard boundary.
- **Firewall blocks treated as app success:** a denied outbound attempt proves containment; it also reveals a forbidden dependency that must be removed.

## 10. PM deliverable and capstone connection

Produce (1) a two-page **Regulatory Applicability and Controls Decision Memo** and (2) a versioned worksheet with one row per activity: entity and role, purpose, categories of personal/derived data, jurisdictional nexus, candidate instrument, section, source version, applicability rationale **from counsel**, vendor/subprocessors, access and storage destinations, signed enterprise physical rules, control owner, control ID, test evidence, legal/technical residual risk, exception approver and next review date.

**Definition of done for the draft exercise:** at least four fictional activities including UAE mainland/DIFC/ADGM/KSA; two alternative architectures plus no-AI; one unsupported supplier claim rejected; one failed negative path with a clear RCA; legal unknowns explicitly OPEN; traces and contracts separated; no statement of actual compliance. This becomes the capstone's policy-gateway and audit evidence backlog, not an auto-generated compliance certificate.

## 11. Knowledge check: six questions, no spoilers

1. **Q1 (4 points).** What five data points must the PM collect before declaring which regime governs GulfCare's UAE-based inference flow? Explain why the server region is insufficient.
2. **Q2 (4 points).** DIFC and ADGM subsidiaries share a supplier. Contrast their regulatory starting points and name two technical tests that neither jurisdiction's guidance can replace.
3. **Q3 (4 points).** Explain why Saudi PDPL Article 29 and the distinct transfer regulation require legal scoping. Give an example of an invalid “Saudi data must always stay in-country” inference.
4. **Q4 (4 points).** Construct a minimum legal-control-evidence row for a support log containing synthetic employee identifiers; identify counsel versus engineering responsibilities.
5. **Q5 real-source case (6 points).** The DIFC Commissioner offers an official “Data Export / International Transfers (Articles 26 & 27)” assessment tool.[^difc-tools] A vendor says completion of its questionnaire authorizes any cross-border support access. How would you respond, identify evidence to request and choose an interim product decision?
6. **Q6 incident and RCA (18 points).** PLANT-05's data and derivatives must stay at its named physical premises. OT-05 is physically air-gapped with **no inbound/outbound network links**. During a fictional cold restart, a speech adapter attempts remote activation and an offshore diagnostic fallback. The firewall denies the call. Write the direct and systemic causes, containment, six distinct corrective-owner responsibilities, expected negative tests, accepted evidence, and conditional release/no-AI disposition. Distinguish firewall success from application failure.

**Total: 40 points.** Worked answers, point allocation and safety-veto conditions remain in [the separate facilitator key](../assessments/solutions/05-laws-regulation-jurisdiction-solutions.md), not embedded in the public learner chapter.

## 12. Key takeaways

1. Legal applicability is a **counsel-reviewed relationship between an entity, activity and current instrument**, not a server-country attribute.
2. UAE federal, DIFC, ADGM, Saudi and EU frameworks require separate version and actor-role checks; sector rules may add requirements.
3. Contractual authority, system routes and physical enterprise constraints each need their own evidence.
4. A blocked egress attempt can show good perimeter containment **and** a failed application hard gate.
5. Prefer an explicitly held decision or non-AI fallback over an unsupported certification claim.

## 13. Evidence ledger: short official-source anchors

**Review method and limit:** The official issuer or regulator **overview/guidance pages** below were accessed via web retrieval **23 November 2026**. Where a primary statute is linked but its entire text was not article-by-article checked here, it is flagged **TEXT NOT FULLY REVIEWED**. Quotes are intentionally short. This is source-reading by a GPT-6 author, **not** a qualified legal opinion or different-model review.

| Claim ID | Exact short issuer anchor | Primary pinpoint / source | What the anchor does not establish |
|---|---|---|---|
| UAE-05-01 | “Federal Decree Law No. 45 of 2021” | UAE Government overview[^uae-overview] | Scope of a particular fictional activity |
| UAE-05-02 | “extraterritorial geographical effect” | UAE AI Office overview, Scope[^uae-ai-office] | Current official consolidated text or all exceptions |
| DIFC-05-01 | “Data Export / International Transfers (Articles 26 & 27)” | DIFC Commissioner official tools[^difc-tools] | Automated transfer authorization |
| ADGM-05-01 | “international transfers” | ADGM Office of Data Protection guidance, Part 6[^adgm-guidance] | Whether a specific importer and safeguard is acceptable |
| KSA-05-01 | “Article 29” | SDAIA PDPL and transfer regulation, Article 29 / Articles 4, 6–7[^ksa-pdpl][^ksa-transfer] | Universal Saudi localization or counsel approval |
| EU-05-01 | “2 December 2027” | EC AI Act Service Desk, Enforcement FAQ, Annex III[^eu-ai-act] | A specific AI system's risk classification |
| SEC-05-01 | “critical assets” | UAE Government CII protection policy overview[^uae-cii] | Designation of fictional PLANT-05 as critical infrastructure |

**Draft reviewer prompts:** Technical reviewer: trace every article/pinpoint and cross-border data path, reproduce schema and safety mutations, inspect current amendments, challenge physical-site exceptions. Editorial/accessibility reviewer: keyboard and 200% zoom reflow, screen-reader diagram narration, readability, assessment calibration with a different rater, no answer-key leakage. **Both reviews NOT COMPLETED**, because this is an unpublished draft.

[^uae-overview]: UAE Government, *Data protection laws*, official portal, https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws. Overview checked **2026-11-23**; not comprehensive article-by-article legal validation.
[^uae-federal]: UAE Legislation, *Federal Decree Law No. 45 of 2021 Concerning the Protection of Personal Data*, official text, https://www.uaelegislation.gov.ae/en/legislations/1972/download. Identified in government reference directory; **full consolidated text/version not independently reviewed in this draft**.
[^uae-ai-office]: UAE Office of Artificial Intelligence, *Personal Data Protection Law*, https://ai.gov.ae/personal-data-protection-law/. Scope and cross-border overview checked **2026-11-23**. Secondary official policy explanation, not a substitute for the operative statute.
[^difc-law]: Dubai International Financial Centre, *Data Protection Law DIFC Law No. 5 of 2020*, with 2025 amendment listing, https://www.difc.com/business/laws-and-regulations/legal-database/difc-laws/data-protection-law-difc-law-no-5-2020. Official law-index page checked **2026-11-23**; consolidated amended legal text requires counsel version check.
[^difc-tools]: DIFC Commissioner of Data Protection, *Data Protection Assessment Tools: Understanding DP Law 2020*, https://www.difc.com/business/registrars-and-commissioners/commissioner-of-data-protection/tools-and-templates. Official overview checked **2026-11-23**, including Articles 26–27 tool title and disclaimer.
[^adgm-guidance]: Abu Dhabi Global Market Office of Data Protection, *Guidance on the Data Protection Regulations 2021*, Part 6 and Article 42(2) SCC overview, https://www.adgm.com/operating-in-adgm/office-of-data-protection/guidance. Official guidance page checked **2026-11-23**; not definitive counsel analysis.
[^uae-health]: UAE Government, *ICT in the health sector*, Federal Law No. 2 of 2019 overview, https://u.ae/en/about-the-uae/digital-uae/whole-of-government-approach/digital-health/ict-in-the-health-sector. Checked **2026-11-23**, sector applicability not determined for fictional case.
[^uae-health-exec]: UAE Legislation, *Cabinet Resolution No. 32 of 2020*, https://uaelegislation.gov.ae/en/legislations/1444. Official instrument index checked **2026-11-23**; not a full amendment analysis.
[^uae-cii]: UAE Government, *Critical Information Infrastructure Protection Policy*, https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/policies/cyber-activities/Critical-Information-Infrastructure-Protection-Policy. Official policy overview checked **2026-11-23**, no site designation verified.
[^ksa-pdpl]: Saudi Data & AI Authority (SDAIA), *Personal Data Protection Law*, Article 29, https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPL/. Official article and scope landing text checked **2026-11-23**; Arabic authority/version and actual application require counsel.
[^ksa-transfer]: SDAIA, *Regulation on Personal Data Transfer Outside the Kingdom*, Articles 4, 6 and 7, https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/RegulationonPersonalDataTransferOutsidetheKingdom/. Issuer HTML reviewed **2026-11-23**; distinguished from general PDPL implementing regulation. Legal interpretation remains open.
[^gdpr]: European Union, *Regulation (EU) 2016/679 (GDPR)*, Articles 3, 28 and 44, https://eur-lex.europa.eu/legal-content/ENG/ALL/?uri=celex%3A32016R0679. Official EUR-Lex source identified **2026-11-23**; exact contemporary application, case law and transfer mechanisms not fully reviewed.
[^eu-ai-act]: European Commission, *AI Act Service Desk: When does enforcement start?*, https://ai-act-service-desk.ec.europa.eu/en/ai-act/faq/when-does-enforcement-start, checked **2026-11-23**. Official FAQ states Annex III and product-integrated high-risk schedules; verify current consolidated law for later amendments.

## 14. Website and social publishing plan

**Current state:** The [Module 05 HTML teaching exemplar](../modules/05-laws-regulation-jurisdiction.html) and early social HTML pages already exist on the published site, but this Markdown draft, lab and solution key **must remain on the draft branch** while Module 04 is held. Do not upgrade pre-existing exemplar links into a declaration that this branch was deployed. The module's final package will need a Markdown-to-HTML build, accessible diagram SVG, quiz spoiler separation, a true HTML-authored question-led carousel, portrait PDF and LinkedIn POST.md, plus rendered checks and two distinct recorded reviews.

**Next:** Finish Module 04 independent/accessibility gates, verify the current legal-source versions, calibrate the Q5/Q6 rubric with a demonstrably independent reviewer, reconcile the Module 05 website and source, and only then consider promotion of this branch. Module 06 examines governance and recurring risk management.
