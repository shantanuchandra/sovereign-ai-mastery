# Sovereign AI Mastery Program — Table of Contents

> **Curriculum version:** 3.0 (approved editorial baseline)  
> **Updated:** 2026-11-17  
> **Audience:** AI Product Managers with intermediate AI product experience  
> **Specialization:** Enterprise sovereign AI platform design, implementation, and leadership  
> **Geographic focus:** UAE and GCC, with global comparisons  
> **Duration:** 24 weeks / ~240 hours (~10 hours per week)  
> **Depth:** Advanced technical labs with an executive decision-first teaching style  
> **Lab baseline:** Apple Silicon M4 Pro, 16 GB unified memory; Python + Docker; cloud/GPU extensions optional

**Plan your study:** [Ten one-hour sessions per module — 240 hours total](learning/schedule.html). Checkboxes record self-reported learning, not publication approval.

## Program outcomes

At completion, a learner should be able to:

1. Explain sovereign AI and distinguish it from data residency, private AI, secure AI, sovereign cloud, and general compliance.
2. Determine when sovereignty applies at **national, sector, enterprise, or individual-workload level**.
3. Classify sovereign AI across scope, control dimensions, deployment, autonomy, and components; assess trade-offs rather than treating sovereignty as binary.
4. Design and demonstrate a credible enterprise sovereign AI reference implementation.
5. Assess UAE/GCC regulatory questions and international comparisons without confusing technical controls with legal compliance.
6. Evaluate model, infrastructure, vendor, security, operational, and economic decisions with evidence.
7. Lead product discovery, roadmap design, implementation, commercialization, and executive review for a sovereign AI platform.

## Website, ontology, quotation & social publishing contract

The final product is a **responsive course website** generated from Markdown. Every chapter has a source-quoted evidence ledger, a conspicuous **taxonomies and ontology** segment linking to `taxonomy/ONTOLOGY.md`, a lab, PM artifact, five-question quiz, a separate solution key, and a **HTML-authored, question-led LinkedIn carousel (with optional exported PDF)** with an accompanying `POST.md`. Content must meet the **no AI slop** standard in `STYLE_GUIDE.md`. Legal assertions require primary-source pinpoint quotes and validation; course-authored classification models must never be presented as official legal standards. At least one critical review is required, with different-model review status recorded honestly.

## Learning format & evidence of mastery

- **Each module:** executive decision brief; core concepts; technical deep dive; Mermaid/custom architecture diagrams; UAE/GCC case; **practical lab; distinct PM deliverable; quiz and scenario; separate solutions file**; academic footnotes and verified primary references.
- **Assessment:** knowledge & scenarios (15%); technical labs (30%); PM/commercial deliverables (20%); security and sovereignty design reviews (15%); final capstone and defense (20%). Each chapter has a spoiler-free quiz, technical verification criteria, and separate answer/rubric file.
- **Continuous capstone:** enterprise sovereign AI platform with private model serving, secured RAG, agent/tool controls, tenant isolation, auditability, monitoring, and an executive business case. Use synthetic data throughout; distinguish lab demonstrations from production assurance.
- **Disclaimer:** curriculum assessment is educational, not a certification, legal opinion, or proof of production compliance.

---

## Part I — Sovereign AI Foundations (Weeks 1–3)

### Module 01 — Sovereign AI Fundamentals (Week 1)

1.1 What is sovereign AI?  
1.2 From digital sovereignty to data, cloud, and AI sovereignty  
1.3 Sovereign vs. private vs. secure vs. compliant AI  
1.4 National sovereignty versus **enterprise-level sovereign AI**  
1.5 Can a company build or operate sovereign AI without owning everything?  
1.6 Sovereignty, control, independence, self-sufficiency, and jurisdiction  
1.7 Benefits, myths, limitations, and risk-based trade-offs

**Lab:** Audit three hypothetical AI workloads against territorial, operational, technological, and legal control criteria.  
**PM deliverable:** One-page enterprise sovereignty decision memo.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/01-...-solutions.md` (use the chapter slug).

### Module 02 — Classifications, Components & Maturity Models (Week 2)

2.1 Sovereignty by scope: national, sectoral, enterprise, workload  
2.2 Control dimensions: territorial, operational, technological, legal  
2.3 Deployment classes: public, managed sovereign, private, hybrid, air-gapped, edge  
2.4 **Sovereign AI stack components:** physical facilities, chips, compute, network, storage, data, models, platforms, applications, IAM, security, operations  
2.5 Model ownership vs. model hosting vs. platform control  
2.6 Dependency and autonomy spectrum; why one-size-fits-all labels fail  
2.7 Sovereignty maturity, evidence, gaps, and scorecards

**Lab:** Score sample architectures against the course-authored sovereignty taxonomy and evidence checklist.  
**PM deliverable:** Classification and maturity matrix with recommended control gaps.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/02-...-solutions.md` (use the chapter slug).

### Module 03 — Enterprise Sovereignty Requirements & Strategy (Week 3)

3.1 What enterprise problems justify sovereignty investments?  
3.2 Classify workloads by data sensitivity, criticality, and impact  
3.3 Security and compliance requirements vs. additional sovereignty objectives  
3.4 Stakeholders: CIO, CTO, CISO, privacy, legal, business, procurement  
3.5 Translate business risks into verifiable technical and operational controls  
3.6 Decision frameworks, investment priorities, and alternatives  
3.7 Requirements traceability, success metrics, and governance

**Lab:** Convert a fictional UAE enterprise requirement set into testable controls.  
**PM deliverable:** Readiness assessment, stakeholder map, and prioritized roadmap.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/03-...-solutions.md` (use the chapter slug).

## Part II — Regional Policy, Regulation & Governance (Weeks 4–6)

### Module 04 — UAE, GCC & Global Sovereign AI Ecosystems (Week 4)

4.1 UAE National AI Strategy 2031 and national priorities  
4.2 UAE ecosystem: government, academic, model, infrastructure, and enterprise actors  
4.3 Saudi Arabia: national AI strategy, infrastructure, and operating environment  
4.4 Other GCC opportunities and regional comparisons  
4.5 India, EU, US, and China: comparative approaches  
4.6 Compute access, chips, supply chains, energy, and geopolitics  
4.7 Arabic models, local language needs, and cultural adaptation

**Lab:** Reproduce a dated evidence map of UAE/GCC AI ecosystem actors and claims.  
**PM deliverable:** Comparative ecosystem landscape and executive implications.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/04-...-solutions.md` (use the chapter slug).

### Module 05 — Laws, Regulation & Jurisdiction (Week 5)

**Educational draft; legal review pending:** A source-authored chapter under `chapters/05-laws-regulation-jurisdiction.md`, plus testable evidence-mapping lab, ontology cross-links, source-quoted evidence ledger, and question-led LinkedIn carousel.

5.1 UAE federal personal data protection framework  
5.2 DIFC and ADGM data protection regimes  
5.3 Sector, government, and critical infrastructure considerations  
5.4 Saudi PDPL and relevant data transfer considerations  
5.5 GDPR, EU AI Act, and other global comparisons  
5.6 Residency, international transfers, contracts, subprocessors, and lawful access  
5.7 How legal jurisdiction differs from operational or technical control  
5.8 Converting legal questions to reviewable requirements and evidence

**Lab:** Map illustrative UAE/KSA processing workflows to applicable legal questions and evidence gaps.  
**PM deliverable:** Regulatory applicability matrix for legal review, not legal advice.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/05-...-solutions.md` (use the chapter slug).

### Module 06 — Governance, Responsible AI & Risk (Week 6)

**Educational draft; independent assessment and manual accessibility review pending:** Source-authored chapter, synthetic governance lab, charter/RACI deliverable, six-question assessment and question-led carousel.

6.1 Governance structures, ownership, and decision rights  
6.2 NIST AI RMF and generative AI risk considerations  
6.3 ISO/IEC 42001 and related governance/security standards  
6.4 Fairness, transparency, accountability, explainability, and oversight  
6.5 Model risk management and intended-use boundaries  
6.6 Risk registers, controls, testing, and audit evidence  
6.7 Design an enterprise AI management operating model

**Lab:** Exercise a risk register with a simulated model failure and control gap.  
**PM deliverable:** AI governance charter, RACI, and audit readiness plan.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/06-...-solutions.md` (use the chapter slug).

## Part III — Sovereign Infrastructure & Architecture (Weeks 7–10)

### Module 07 — End-to-End Sovereign AI Stack & Reference Architecture (Week 7)

**Educational draft; independent assessment and manual accessibility review pending:** Seven-topic lesson, synthetic graph lab, ADR template, six-question assessment and question-led carousel.

7.1 Physical-to-application stack  
7.2 Data, compute, management, and control planes  
7.3 Lifecycle from ingestion and training to deployment and retirement  
7.4 Boundaries of control, trust zones, and privileged administration  
7.5 Enterprise reference architectures  
7.6 Architecture for variable sovereignty requirements  
7.7 Architecture decision records and trade-off analysis

**Lab:** Model an end-to-end architecture, trust boundaries, and control-plane paths in Mermaid.  
**PM deliverable:** Architecture decision record and executive design justification.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/07-...-solutions.md` (use the chapter slug).

### Module 08 — Data Sovereignty & Engineering (Week 8)

[Read the educational draft](chapters/08-data-sovereignty-engineering.md). Independent assessment and manual accessibility review pending.

8.1 Data classification, ownership, governance, and stewardship  
8.2 Data acquisition, pipelines, storage, transformations, and cataloging  
8.3 Structured, unstructured, and multimodal data  
8.4 Embeddings, vectors, derived data, and retrieval-specific concerns  
8.5 Lineage, provenance, retention, deletion, and backups  
8.6 Data egress, geographic controls, and cross-boundary flows  
8.7 Privacy-enhancing methods and synthetic data

**Lab:** Build and validate an auditable synthetic-data ingestion and local retrieval pipeline.  
**PM deliverable:** Data-flow and data-control specification with retention rules.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/08-...-solutions.md` (use the chapter slug).

### Module 09 — GPUs, Compute, Networking & Platform Engineering (Week 9)

[Read the educational draft](chapters/09-gpus-compute-networking-platform-engineering.md). Independent assessment and manual accessibility review pending.

9.1 GPUs, accelerator types, and memory constraints  
9.2 Compute profiles: training, fine-tuning, batch and online inference  
9.3 Clusters, storage, high-speed networks, and scheduling  
9.4 Docker, Kubernetes, and infrastructure fundamentals  
9.5 Resource quotas, isolation, and multitenancy  
9.6 Latency, throughput, availability, and capacity sizing  
9.7 Utilization, power, hardware supply, and compute economics

**Lab:** Deploy Docker services locally and perform a reproducible compute/capacity estimate.  
**PM deliverable:** Compute-sizing decision worksheet with assumptions.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/09-...-solutions.md` (use the chapter slug).

### Module 10 — Sovereign Cloud & Deployment Patterns (Week 10)

[Read the educational draft](chapters/10-sovereign-cloud-deployment-patterns.md). Independent assessment and manual accessibility review pending.

10.1 Public cloud, sovereign-managed cloud, private cloud, and on-premises  
10.2 Hybrid, edge, and distributed designs  
10.3 Connected, restricted-connectivity, and air-gapped systems  
10.4 Remote access, support, update, and control risks  
10.5 Availability zones, resilience, and disaster recovery  
10.6 Infrastructure as code, supply chain, and portability  
10.7 Placement decisions based on controls, performance, and cost

**Lab:** Compare local-private, managed sovereign, and hybrid deployment diagrams.  
**PM deliverable:** UAE bank deployment selection scorecard and ADR.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/10-...-solutions.md` (use the chapter slug).

## Part IV — Models, RAG, Agents & AI Engineering (Weeks 11–14)

### Module 11 — Sovereign Models & Model Strategy (Week 11)

[Read the authored educational draft](chapters/11-sovereign-models-model-strategy.md). Independent/manual review remains pending.

11.1 Transformer/LLM essentials for product and architecture decisions  
11.2 Open-source, open-weight, and proprietary model distinctions  
11.3 Licenses, model artifacts, ownership, provenance, and IP  
11.4 Train, adapt, host, or consume external inference  
11.5 Model serving and private inference components  
11.6 Arabic/multilingual and domain-specific model needs  
11.7 Model selection: performance, cost, portability, autonomy

**Lab:** Run and evaluate a small, properly licensed local model on Apple Silicon.  
**PM deliverable:** Model choice matrix including licensing, portability, cost, and control.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/11-...-solutions.md` (use the chapter slug).

### Module 12 — Sovereign RAG Systems (Week 12)

12.1 Retrieval-augmented generation architecture  
12.2 Loading, parsing, chunking, embeddings, and indexing  
12.3 Search approaches, reranking, and retrieval quality  
12.4 Identity-aware retrieval and document permissions  
12.5 Tenant isolation, sensitive data, and data flow controls  
12.6 Grounding, evaluation datasets, and failure analysis  
12.7 Leakage prevention and responsible response behavior

**Lab:** Build local RAG with synthetic documents and tenant-aware retrieval checks.  
**PM deliverable:** RAG requirements and security acceptance-criteria document.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/12-...-solutions.md` (use the chapter slug).

### Module 13 — Fine-Tuning, Optimization & Evaluation (Week 13)

13.1 Fine-tuning compared with prompting and RAG  
13.2 PEFT/LoRA and training pipeline fundamentals  
13.3 Quantization, batching, memory, and inference optimization  
13.4 Dataset preparation, experiment tracking, and reproducibility  
13.5 Quality, safety, and task-level benchmarking  
13.6 Arabic and sector-sensitive evaluation  
13.7 Quality-versus-cost and deployment trade-offs

**Lab:** Measure quantization or inference tuning locally; optionally conduct cloud LoRA.  
**PM deliverable:** Optimization trade-off memo and evaluation plan.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/13-...-solutions.md` (use the chapter slug).

### Module 14 — Agents, APIs & Enterprise Integrations (Week 14)

14.1 Assistants, workflows, and agents  
14.2 Tool invocation and orchestration patterns  
14.3 Model gateways, routing, access policies, and audit logs  
14.4 Agent identity, credentials, permissions, and action boundaries  
14.5 Human approvals and high-impact actions  
14.6 Integration with enterprise applications and internal data  
14.7 Multi-tenant developer platforms and API experience

**Lab:** Build a gated agent with synthetic tools, permission checks, and audit events.  
**PM deliverable:** Agent control-spec, abuse-case register, and go/no-go rubric.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/14-...-solutions.md` (use the chapter slug).

## Part V — Security, Privacy & Operations (Weeks 15–18)

### Module 15 — AI Security & Threat Modeling (Week 15)

15.1 Threat models, trust boundaries, and attack surfaces  
15.2 Direct/indirect prompt injection and exfiltration  
15.3 Model supply chain, poisoned assets, and artifact integrity  
15.4 API, container, network, and platform vulnerabilities  
15.5 Zero-trust and least-privilege architecture  
15.6 Software/model bills of materials and provenance  
15.7 Security validation and red-team exercises

**Lab:** Threat-model the RAG service and run non-destructive security tests.  
**PM deliverable:** Threat model with prioritized mitigations and validation criteria.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/15-...-solutions.md` (use the chapter slug).

### Module 16 — Cryptography, Identity & Confidential Computing (Week 16)

16.1 Encryption at rest, in transit, and in use  
16.2 Customer/enterprise-managed keys and custody  
16.3 KMS, HSM, rotation, and separation of duties  
16.4 Confidential computing, attestation, and limitations  
16.5 IAM, RBAC/ABAC, service identities, and secrets  
16.6 Admin, support, and provider access control  
16.7 Measurable verification of sovereign controls

**Lab:** Implement local identity policies, key-separation simulation, and access evidence.  
**PM deliverable:** Key-custody and privileged-access control review.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/16-...-solutions.md` (use the chapter slug).

### Module 17 — MLOps, LLMOps & Observability (Week 17)

17.1 Model versioning and registry governance  
17.2 CI/CD, release gates, and controlled deployments  
17.3 Quality and drift monitoring  
17.4 Traces, logs, metrics, and privacy-conscious observability  
17.5 Tenant metering, quotas, and reliability SLOs  
17.6 Incident handling and service operations  
17.7 Resource and cost visibility

**Lab:** Implement versioned release flow, logging/metrics, and measurable SLOs.  
**PM deliverable:** LLMOps operating model and rollout checklist.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/17-...-solutions.md` (use the chapter slug).

### Module 18 — Resilience, Audit & Vendor Exit (Week 18)

18.1 Availability, resilience, and recovery objectives  
18.2 Backups, restoration, and business continuity  
18.3 Incident response and change control  
18.4 Compliance evidence and repeatable testing  
18.5 Model/data portability and migration planning  
18.6 Concentration, substitution, and exit risk  
18.7 Continuous assurance and sovereignty drift

**Lab:** Simulate restore, migration, or model substitution and record evidence.  
**PM deliverable:** Resilience and vendor-exit plan with recovery objectives.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/18-...-solutions.md` (use the chapter slug).

## Part VI — Product, Economics & Commercialization (Weeks 19–21)

### Module 19 — Enterprise Market & Use Case Discovery (Week 19)

19.1 Enterprise customer profiles and buying centers  
19.2 Finance, healthcare, telecom, government, and industry cases  
19.3 Value propositions for sensitive workloads  
19.4 Discovery interviews, jobs-to-be-done, and constraints  
19.5 Prioritization by value, feasibility, risk, and sovereignty necessity  
19.6 Market segmentation, competitive alternatives, and positioning  
19.7 Opportunity scoring and viability

**Lab:** Score fictional buyer interviews and segment opportunities with evidence.  
**PM deliverable:** Market opportunity assessment and prioritized use-case backlog.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/19-...-solutions.md` (use the chapter slug).

### Module 20 — Platform Product Strategy & PRDs (Week 20)

20.1 Platform vision, strategy, and stakeholder outcomes  
20.2 Personas: IT, AI engineer, security, developer, business owner  
20.3 Requirements, nonfunctional constraints, and traceability  
20.4 Model catalogs, gateways, governance features, and tenancy  
20.5 APIs, onboarding, documentation, and developer experience  
20.6 MVP, roadmap, prioritization, and sequencing  
20.7 Product metrics, acceptance criteria, and adoption

**Lab:** Prototype API flows and tenant onboarding against acceptance tests.  
**PM deliverable:** Platform PRD, launch KPIs, and 12-month roadmap.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/20-...-solutions.md` (use the chapter slug).

### Module 21 — Economics, Procurement & Go-to-Market (Week 21)

21.1 Total cost of ownership and CAPEX/OPEX  
21.2 GPU economics, inference unit costs, and utilization  
21.3 Private deployment versus external API break-even  
21.4 Build/buy/partner and supplier diligence  
21.5 RFPs, vendor scorecards, contracts, and SLAs  
21.6 Packaging, pricing, and customer economics  
21.7 GTM, partnership channels, and enterprise sales  
21.8 Business cases, scenario sensitivity, and executive decisions

**Lab:** Construct a sensitivity-based three-year TCO/pricing calculator.  
**PM deliverable:** Business case, procurement scorecard, and GTM narrative.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/21-...-solutions.md` (use the chapter slug).

## Part VII — Integrated Enterprise Platform Capstone (Weeks 22–24)

### Module 22 — Product & Architecture Blueprint (Week 22)

22.1 Select customer segment and workload  
22.2 Establish sovereignty objectives and capability tiers  
22.3 Finalize data, security, regulatory, and operational needs  
22.4 Design deployment architecture and trust boundaries  
22.5 Define controls, evidence, and API contracts  
22.6 Prepare backlog, milestones, and test strategy

**Lab:** Create integrated architecture diagrams and a control verification matrix.  
**PM deliverable:** Capstone PRD, system blueprint, and implementation backlog.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/22-...-solutions.md` (use the chapter slug).

### Module 23 — Build & Validate the Platform MVP (Week 23)

23.1 Private model service  
23.2 Secure RAG application  
23.3 Identity, tenancy, and access controls  
23.4 Gateway, audit events, and governance checks  
23.5 Functional, sovereignty, performance, and safety tests  
23.6 Operating manual, caveats, and demo

**Lab:** Integrate local model serving, RAG, identities, APIs, and evidence logs.  
**PM deliverable:** Demonstrable MVP, acceptance report, and residual-risk register.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/23-...-solutions.md` (use the chapter slug).

### Module 24 — Executive Defense & Mastery Review (Week 24)

24.1 Market opportunity and customer problem  
24.2 Product vision and roadmap  
24.3 Architecture, technology, and vendor trade-offs  
24.4 Demonstration and assurance claims  
24.5 Economics, pricing, and ROI  
24.6 Simulated CTO/CISO/legal/procurement Q&A  
24.7 12-month execution and maturity plan

**Lab:** Run a timed product/architecture executive defense with adversarial questions.  
**PM deliverable:** Executive deck, portfolio, investment proposal, and next-year plan.  
**Assessment:** Five knowledge questions + one decision scenario; solutions in `assessments/solutions/24-...-solutions.md` (use the chapter slug).

---

## Appendices

- **A — Glossary & Sovereignty Taxonomy:** terminology; scope, dimensions, degrees, and component mapping.
- **B — Architecture Library:** reference diagrams, trust boundaries, and example deployments.
- **C — AI PM Toolkit:** PRDs, user research, roadmap, KPIs, platform acceptance criteria.
- **D — Sovereignty Assessment:** control matrix, scoring rubric, vendor dependencies, evidence standards.
- **E — Security & Governance:** risk registers, threat models, control mapping, assurance templates.
- **F — Procurement & Economics:** GPU/TCO models, vendor scoring, RFP and contract checklists.
- **G — Cases:** UAE/GCC plus India/EU/US/China comparisons; positive and negative cases.
- **H — Learning Resources:** legal texts, standards, technical documentation, papers, tutorials.
- **I — Interviews & Leadership:** concept questions, architecture interviews, executive scenarios.
- **J — Trends & Curriculum Maintenance:** emerging technologies, regulatory updates, source review log.

## Course authoring contract

For each of the 24 modules, publish one learner chapter under `chapters/`, one practical lab (embedded or linked), one **separate** PM deliverable prompt and acceptance rubric, five knowledge questions plus a realistic decision scenario, and one spoiler-free solutions file under `assessments/solutions/`. Chapters must use `CHAPTER_TEMPLATE.md` and `STYLE_GUIDE.md`. Answers never appear inline with learner questions. Length is determined by topic complexity, not a fixed target. All cloud/GPU work must have an explicit local-first alternative or be clearly optional.

**Core lab machine:** Apple M4 Pro / 16 GB unified RAM. Run CPU and smaller Apple-Metal-capable models locally; do not assume CUDA or NVIDIA tooling works on macOS. Containerized APIs and supporting services run via Docker; GPU-accelerated model execution can run natively on the macOS host.

## Suggested publication structure

```text
README.md
TOC.md
STYLE_GUIDE.md
CHAPTER_TEMPLATE.md
references/
  sources.md
chapters/
  part-01-foundations/
    01-sovereign-ai-fundamentals.md
    02-classifications-components-maturity.md
    03-enterprise-requirements-strategy.md
  ...
labs/
diagrams/
assessments/
capstone/
.github/
```

**Status:** Editorial baseline finalized on 2026-11-17. Chapter authors must follow [CHAPTER_TEMPLATE.md](CHAPTER_TEMPLATE.md) and [STYLE_GUIDE.md](STYLE_GUIDE.md).
