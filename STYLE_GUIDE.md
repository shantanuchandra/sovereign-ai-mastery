# Editorial, Typography & Reference Style Guide

> **Status:** Editorial standard v4.0 (2026-11-17).  
> **Applies to:** Course chapters, technical labs, case studies, PM templates, assessments, and the capstone.  
> **Primary publishing target:** A responsive, accessible, searchable course **website**, built from version-controlled Markdown. GitHub Markdown is the authoring format, not the finished reading experience.

## NON-NEGOTIABLE EDITORIAL RULES

**Specific style prohibition for social publications:** Do not use the em dash character (—), dash-led faux drama, generic AI platitudes, or a question whose answer is a slogan. Use periods, commas, colons, or a rewritten sentence. A build-time scan should fail social artifacts containing the em dash.


1. **No AI slop.** Do not use broad hype, vague claims, generic three-part slogans, motivational padding, repeated transitions, or unsupported superlatives. Delete any sentence that changes no reader decision, mental model, or procedure. No fabricated examples presented as real deployments. Ban phrases such as "in today's rapidly evolving landscape", "game-changer", "leverage the power", "unlock the potential", "robust and seamless", and "it is important to note".
2. **Quote the evidence, not just the bibliography.** For each material legal/regulatory or market assertion, show a **short, exact, attributed quotation** in the text or an evidence table, with a pinpoint source section/article, URL, retrieval date, and a clear interpretation. A bibliography alone does not qualify. Quote only what was checked in the actual source. Keep quotes brief; do not reproduce paywalled standards or substantial passages of protected works.
3. **Interpretations are not quotations.** Separate **verbatim source**, **editorial inference**, **scenario assumption**, **verification evidence**, and **open question**. A vendor's claim is not independent proof.
4. **Taxonomy/ontology first.** Every module must state which entities, classes, properties, and relationships it introduces or changes, and link to `taxonomy/ONTOLOGY.md`. Distinguish a *classification/taxonomy* (hierarchical grouping) from an *ontology* (entities, relations, constraints), and mark course-authored constructs as nonstandard.
5. **Website-first delivery.** Markdown is authored in Git; the finished learning product is the responsive site in `dist/`, with in-page contents, accessible diagrams, source footnotes, module progress metadata, learning artifacts, and related modules.
6. **One HTML-authored LinkedIn document per module.** Every module ships a designed HTML/CSS question carousel, exported as a portrait PDF whose **slide headlines are questions**; it is a public thought-leadership derivative, not a reproduction of the whole chapter. Include a question-based LinkedIn post draft and conservative, sourced claims. Never publish private lab configs, internal data, or answer keys.
7. **No false independent reviews.** AI-generated editorial reviews must be labeled as such. Different-model review requires a genuinely separate model's output, saved with model/version, date and prompt; if unavailable, mark **NOT COMPLETED**, provide the prompt, and perform a separately documented self-critique.

## 1. Editorial mission and readership

**Reader:** An intermediate AI Product Manager growing toward technical leadership in enterprise sovereign AI, especially UAE/GCC markets.

**Editorial promise:** Write an **executive playbook**: concise, strategic, evidence-led, and decision-first, with enough technical detail to implement and verify designs. Every chapter must support architectural judgment, hands-on work, and a reusable PM decision artifact.

### Default voice

- Executive and precise: begin with the decision, explain the mechanism, then show evidence, implementation, and trade-offs.
- Prefer **plain English** and define jargon at first use; retain exact technical terms once defined.
- Use a **BLUF** (bottom line up front): thesis, who should care, decision, and important caveat in the first screen.
- Write for an experienced PM: skip obvious PM basics, define non-obvious engineering terms, and remove filler or hype.
- Explain both **what works** and **when it is not the right choice**.
- State jurisdiction, assumptions, uncertainty, and publication/version dates whenever needed.
- Never present illustrative architectures, case simulations, or unverified vendor claims as certified production deployments.

### Technical level and progression

1. **Intuition:** Analogy or business problem in short prose.
2. **Precise model:** Definitions, boundaries, taxonomy, and formal constraints.
3. **Architecture:** Components, data/control flows, interfaces, isolation and failure modes.
4. **Hands-on:** Reproducible, tested steps and verification evidence.
5. **PM judgment:** Trade-off matrix, business rationale, stakeholder questions, and decision output.

**Depth guidance:** No need to re-explain basic PM concepts. Explain computer science and systems concepts when they are prerequisites to making sovereignty decisions.

## 2. Headings, structure, and readable prose

- **H1 (`#`)**: Exactly one per chapter: `Module NN — Descriptive Title`.
- **H2 (`##`)**: Fixed core sections in `CHAPTER_TEMPLATE.md`; begin with numbered labels for scanability.
- **H3 (`###`)**: Subtopics, patterns, mechanisms, examples, and lab steps.
- **H4 (`####`)**: Rare; if deeper nesting is required, restructure.
- Keep headings descriptive: "How provider access changes operational sovereignty" rather than "More considerations".
- Prefer sentence case; preserve acronyms (GPU, RAG, IAM, MLOps), proper nouns, and code identifiers.
- Aim for paragraphs of 2–5 sentences; lists for procedures and comparisons, not as a substitute for explanation.
- Tables should convey decisions or contrasts and remain accessible on narrow screens (roughly <= 5 columns when feasible).
- Put an **outcome** and **why it matters** near the beginning, a summary and self-check near the end.
- Include inline links and an end-of-chapter reference list.
- Every code block specifies a language: `bash`, `python`, `yaml`, `json`, `sql`, `mermaid`, etc.
- Use examples from UAE/GCC where appropriate, but explain applicability and compare with another market when informative.

### Adaptive length — no quotas

The learner selected **adaptive depth**. No fixed word count or mandatory min/max applies. A simple classification concept may fit in 1,000–2,000 words; advanced architecture and threat models may need substantially more. These are illustrations, not quotas.

Write only what the concept, lab, and PM decision require. Use a progressive detail path: **executive brief -> decision table -> technical deep dive -> lab -> PM application -> assessment**. Long technical procedures may live in linked lab files, but every chapter still contains a runnable lab entry and measurable acceptance criteria. Avoid lengthy repetition between modules; link to the canonical earlier explanation.

## 3. Typography and visual system

**GitHub limitation:** Standard GitHub Markdown does **not** let a repository force a custom reader font. Heading hierarchy, whitespace, tables, code blocks, and diagrams are reliable there; font recommendations apply to exported docs, the course website, slides, or PDFs.

### Chosen design system (final)

- **Reader headings and long-form body:** Georgia / Iowan Old Style / Baskerville (fallback: Times New Roman, serif). **Navigation, controls, tables and captions:** Inter / system UI (fallback: Segoe UI, Arial, sans-serif).
- **Code and terminal:** JetBrains Mono (fallback: SFMono-Regular, Consolas, Liberation Mono, monospace).
- **Arabic text when included:** Noto Sans Arabic, with a system sans-serif fallback; check script shaping and direction.
- **Colors for optional publishing theme:** midnight/navy `#14283F`, teal `#0E766E`, white `#FFFFFF`, cool gray `#475569`, pale slate `#F2F5F8`. Test contrast; do not convey status through color alone.
- **GitHub Markdown:** GitHub controls the viewer font; typography guidance applies to the website, slides, or exported PDF. Do not embed or redistribute commercial font files.

### Typography tokens for future exports / site

- H1: 30–36 px, weight 700, line-height ~1.2.
- H2: 24–28 px, weight 650–700, line-height ~1.25.
- H3: 19–22 px, weight 600, line-height ~1.3.
- Body: 16–18 px, line-height 1.55–1.7; line length ~65–80 characters.
- Code: 13–15 px with a readable monospace face.
- Captions: 13–14 px; maintain accessible contrast.
- Never use color alone to encode risk levels or correctness.

### Diagrams and visuals

- Use **Mermaid by default** for version-controlled flowcharts, sequence diagrams, control boundaries, and architecture overviews rendered by GitHub.
- Use tables for a small number of alternatives; decision trees for classification logic; C4-style diagrams for architectures.
- Every diagram must have a caption, a textual walkthrough, and labels that do not rely on color alone.
- **Website rendering is mandatory.** GitHub's Markdown Mermaid viewer does not automatically power the custom HTML reader. Build a legible static SVG from the committed Mermaid source, retain the original source in expandable HTML, and fail quality checks if the page shows only raw graph instructions. The static diagram must display without network/CDN access or JavaScript. For unsupported diagram types use a build-time renderer rather than silently leaving a code fence.
- For complex cross-plane architecture or executive exhibits, create **custom-designed vector diagrams** with an editable source (SVG plus editable authoring source where applicable) under `diagrams/`; include alt text, version, and source attribution. Mermaid drafts are encouraged as a first step.
- Be conservative with screenshots: add timestamp, product version, attribution, and alt text.

## 4. Terminology and precision rules

- Spell **sovereign**, not "soverign".
- State the **subject** of sovereignty (which company, nation, sector, or workload) and **what is controlled**.
- Do not equate "located in UAE", "encrypted", "private", "compliant", or "open-source" with full sovereignty.
- Distinguish **data residency**, **data governance**, **data access**, **model control**, **infrastructure control**, **operator control**, and **legal jurisdiction**.
- An example autonomy/maturity score must be labeled **course-authored**, not an official standard or certification.
- In regulatory discussions, distinguish binding legal text, regulator guidance, standards, contractual controls, and the author's interpretation.
- Define and test claims such as "no data egress", "customer-owned key", "private inference", and "vendor independent" rather than repeating marketing labels.

## 5. Citation and external source policy

### Reference priority

1. **Primary law and regulators:** official legislation, government portals, competent regulators, official policy documents.
2. **Standards and technical authorities:** ISO, NIST, OWASP, IETF, CNCF, etc. (check access/license conditions).
3. **Original documentation:** software project docs, official product docs, release notes, security specifications, model cards/licenses.
4. **Research:** peer-reviewed papers, arXiv preprints labeled as such, reproducible technical evaluations.
5. **Industry analysis:** independent research and trade coverage; useful context, not substitutes for primary legal facts.
6. **Vendor marketing:** label as provider claim; corroborate when making important comparisons.

### Required academic-style footnotes (final)

- Use GitHub-flavored Markdown footnotes such as `[^nist-ai-rmf]` **close to the material claim**. A reference list alone is not sufficient. Reserve inline ordinary links for navigation and optional further reading.
- **Citation entry format:** `Author/Institution, *Title*, edition/version (publication/update date if known), URL. Verified: YYYY-MM-DD.` Include an article, clause, page, commit, or section when applicable.
- Example:

```markdown
NIST publishes an AI risk management framework.[^nist-ai-rmf]

[^nist-ai-rmf]: National Institute of Standards and Technology,
    *AI Risk Management Framework (AI RMF 1.0)* (2023),
    https://www.nist.gov/itl/ai-risk-management-framework.
    Verified: 2026-11-17.
```

- Every legal obligation, benchmark, model spec, product feature, cost figure, date, and case-study outcome must have a traceable source close to the claim.
- Include **publisher, title, edition/version, publication date when known, URL, and last verified date** in references.
- Prefer exact regulation/article/section or standard clause where possible. Do **not** reproduce paywalled ISO text.
- Quote sparingly and respect copyright; paraphrase faithfully and link back to the source.
- Mark time-sensitive facts with `Last verified: YYYY-MM-DD`; review them before publishing and on a scheduled cadence.
- Distinguish documented fact, deduction, and hypothetical scenario: e.g., `[Source-backed]`, `[Analysis]`, `[Illustrative]` when ambiguity could mislead.
- Avoid broken, shortened, AI-invented, and tracking-heavy links.

### Starter authoritative reference directory (links checked against official search results, 2026-11-17)

| Topic | Official / primary resource | Use in course |
|---|---|---|
| UAE AI strategy | [UAE National Strategy for AI 2031](https://ai.gov.ae/strategy/) | Ecosystem, national strategic context |
| UAE personal data | [UAE government: data protection laws](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws) | Federal regulatory overview; confirm the actual law and scope |
| UAE federal law | [Federal Decree Law No. 45 of 2021](https://www.uaelegislation.gov.ae/en/legislations/1972/download) | Primary text for personal-data controls |
| DIFC | [DIFC Commissioner of Data Protection](https://www.difc.com/Business/registrars-and-commissioners/commissioner-of-data-protection) | DIFC-specific requirements |
| ADGM | [ADGM Office of Data Protection guidance](https://www.adgm.com/operating-in-adgm/office-of-data-protection/guidance) | ADGM-specific requirements |
| AI risk management | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | Governance and risk methods; check ongoing revisions |
| Generative AI risk | [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | GenAI risks and mitigations |
| AI management systems | [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) | AIMS requirements and governance concepts; licensed standard |
| EU AI law | [EU AI Act Explorer (official)](https://ai-act-service-desk.ec.europa.eu/en/ai-act-explorer) | Current articles and consolidated view |
| EU AI Act schedule | [EU AI Act implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline) | Time-sensitive obligations; verify before use |
| LLM security | [OWASP Top 10 for LLM Applications](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) | Threats, mitigation exercises |

**GCC expansion:** Saudi PDPL source: [SDAIA official English PDF](https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf). Before legal analysis, check amendments, implementing regulations, regulatory interpretation, applicability, and transfer rules. Add additional GCC authorities during chapter research rather than infer requirements from vendor marketing.

## 5A. Quotation and citation protocol — required in every chapter

**Workflow:** retrieve original primary source -> locate a specific sentence, article or clause -> copy a short excerpt exactly -> preserve original wording/case/punctuation -> record its scope -> attach a claim-level footnote -> explain the implication and limitations. **If the quoted wording cannot be independently found, remove the quote and mark the claim unverified.**

Create an **Evidence ledger** table in every module:

| Claim ID | Verbatim quote (≤ 25 words per original source in all displayed extracts) | Primary source + pinpoint | Your interpretation | Limits / uncertainty | Checked |
|---|---|---|---|---|---|
| CL-01 | “...” | Issuer, section, link | ... | ... | YYYY-MM-DD |

- Use quotation marks for verbatim text; do not use them for paraphrases.
- Attribute quotations in the running text with footnotes, not unlabelled callouts.
- Quote official law and policy only in the smallest excerpt necessary. **Link back to complete original** rather than copy its full wording.
- For multi-jurisdiction chapters, validate the version and amendments, distinguish legislative text from regulator commentary, and avoid overclaiming what legal obligations require.
- For technical claims, cite official documentation with a pinpoint anchor or version; use measured outputs for lab observations.
- For course-derived taxonomy or PM heuristics, say **Course-derived framework; not a regulation or standard** instead of sourcing it to an unrelated standard.
- Source entry must record: title, institution, publication/update date if known, date checked, canonical URL, article/section, evidence type, and material caveat. Never guess publication dates.

## 5B. Editorial quality gate — no fluff

Every paragraph must pass **SCOPE**:

- **S**pecific: one testable assertion or decision, not a slogan.
- **C**ontextual: whose jurisdiction, workload, timeframe, and assumptions?
- **O**bservable: what evidence or measurement would show it?
- **P**recise: avoid conflating legal duty, contractual requirement, security control, and sovereignty objective.
- **E**conomical: remove duplicated claims, boilerplate intros, generic conclusions, and redundant adjectives.

Bad: “In an ever-changing digital world, sovereign AI empowers organizations with cutting-edge, seamless control.”  
Better: “Keeping prompts in a UAE region does not establish operational control if a vendor can access plaintext logs from another jurisdiction.”

**Peer-review red flags:** fabricated citations; “as per regulations” without a section; anonymous real-world examples; unexplained scores; an architecture without administrative paths; “fully sovereign” without threat model; summaries that add no decision; untested code; invented interview quotes.

## 5C. Website design system and technical publishing contract

- **Site is canonical presentation:** desktop/tablet/mobile, responsive navigation, in-page table of contents, search-ready structure, high contrast, keyboard-accessible navigation, readable code blocks, captions, footnote backlinks, and visible review dates.
- **Text tokens:** body `Inter, ui-sans-serif, system-ui`; technical/code `JetBrains Mono, ui-monospace, SFMono-Regular, monospace`. These are CSS font stacks; **do not distribute proprietary font binaries**. Use system fallback when the named font is absent. Prefer 16–18px body, line-height ~1.6, 65–75ch prose measure.
- **Palette:** deep ink `#132438`, midnight `#0B1725`, cool white `#F6F8FA`, teal `#0D7B72`, muted sand `#E5B96F`, outlined borders `#DCE4E8`. Teal denotes action/relationships, sand denotes evidence or caution; never color alone for semantics.
- **Hierarchy:** one H1 per page, H2 for core chapter sections, H3 for named ideas, short paragraphs and tables with explicit headers. Prefer question-led headings when it improves reader reasoning; avoid clickbait.
- **Visuals:** Mermaid sources committed next to chapters; complex ontology/architecture visuals supplied as editable SVG plus textual equivalent. Include caption, alt text, legend, source, and export-safe dimensions. Keep diagrams accurate under dark/light themes.
- **Publication:** build with `python scripts/build_site.py`, preview `python -m http.server 8000 --directory dist`; no paid service required. Every module gets a canonical page at `/modules/NN-slug.html`; taxonomy has its own entry point. Markdown remains editable in repo.
- **Safety:** No tracking by default; no externally hosted scripts required for the base site. Do not index solutions or internal review files in the public learner site. Preview links and PDF links are relative. Display a notice when a legal section has not been source-reviewed within its freshness interval.

## 5D. LinkedIn packaging — required for every module

- Output locations: `social/module-NN/NN-questions.pdf`, `social/module-NN/POST.md`, and the editable content outline `social/module-NN/SLIDES.md`.
- **7–9 portrait pages** (recommended 4:5), one **question** as each slide headline. Every slide must be answerable in a sentence or with 2–3 concrete decision points, not a rhetorical slogan.
- Pattern: *provocative but accurate question → concise answer/evidence → decision test/question*.
- Suggested sequence: hook question, definition question, misconception question, taxonomy question, real scenario question, risk/verification question, practical decision question, close/source question.
- Cite sources unobtrusively on relevant slides; final slide has the primary URLs or short references. No fabricated engagement statistics or clickbait claims.
- `POST.md` is **entirely question-led**, with an opening question, short observation, 2–3 substantive follow-up questions, and a transparent link placeholder for the website module. The author reviews and posts manually.
- PDFs must be text-selectable, legible on mobile, visually inspected after rendering, and checked for clipping.

## 6. Case study and vendor evidence standard

Use this standardized mini-profile:

1. **What is being claimed?** e.g., in-country operations, key custody, model portability.
2. **Who claims it?** government, company, vendor, independent auditor.
3. **What evidence exists?** architecture, audit, contract, public declaration, test.
4. **What is missing?** admin access scope, backups, telemetry, legal jurisdiction, exit option.
5. **What should an enterprise buyer ask?** due diligence questions and acceptance tests.

Do not conflate national initiatives, commercial products, and legal mandates.

## 7. Technical labs and reproducibility

- **Default tested target:** Mac with **M4 Pro and 16 GB unified memory**; Python 3.x, `venv`, Docker Desktop (or supported alternative), Git, and small licensed local models.
- **Apple Silicon guidance:** use ARM64 images; note when `linux/amd64` emulation is necessary. GPU accelerated inference can run on the macOS host with a Metal-compatible backend (e.g. suitable `llama.cpp`/Ollama release); **do not claim NVIDIA CUDA or native Docker GPU passthrough is available on macOS**.
- Use CPU-friendly containers for APIs, PostgreSQL/pgvector, policy, and observability; prefer 1B–4B quantized models for initial experiments where compatible with actual RAM use. State when model/context size exceeds memory. Optional remote GPU/fine-tuning labs must be clearly optional with spend cap and cleanup.
- Prefer local-first and low-cost setup. A learning exercise is not 'fully sovereign' merely because it runs on a laptop; document provenance, binary/artifact downloads, telemetry, and operating-system control assumptions.
- Pin or specify tested versions; record platform, model license, image digests when material, and expected output.
- Never embed API secrets, passwords, private keys, or confidential enterprise data.
- Use synthetic or permissibly licensed public datasets; document data and model usage rights.
- Every lab must have setup, procedure, verification, failure recovery, clean-up, and acceptance criteria.
- Record data flow and network egress assumptions. If a lab uses internet downloads, say so explicitly; do not label it fully offline.
- Lab instructions are educational references. Production hardening requires separate risk and compliance review.

## 8. PM artifacts and assessment expectations

Each chapter must produce at least one reusable deliverable:

- Sovereignty assessment, decision record, architecture diagram, PRD section, vendor scorecard, financial model, threat model, or working demo.
- Criteria must be measurable: "log all administrative operations" is more testable than "ensure transparency".
- Include discussion questions for CTO/CISO/procurement/business stakeholder perspectives.
- Use scenario questions that require a defended judgment, not only memorized definitions.
- **Question 5 must use a real-world sourced example:** a named product with verified primary documentation or an actual, attributed incident. Do not invent the organizational circumstances of a real-world incident; a fictional customer scenario using a real product must be explicitly labeled.
- **Question 6 must support a complete RCA:** require observed behavior, expected behavior, state before evidence, state after evidence, direct cause, contributing cause, containment, owner, reproducible retest, and bounded decision. A one-sentence answer is unacceptable.
- **Dynamic learning is strongly encouraged:** run a constrained questionnaire, compute a provisional architecture and evidence plan, then invite the learner to change one variable and explain the consequence.
- **Separate solutions are mandatory**: create `assessments/solutions/NN-short-title-solutions.md` for every chapter. Include quiz answer rationales, scenario trade-offs, lab expected output and troubleshooting, and a PM artifact scoring rubric. No solutions inline with the learner chapter.

## 9. Repository structure and publishing conventions

Suggested directories:

```text
README.md                  # audience, prerequisites, syllabus map
TOC.md                     # source-of-truth course map
STYLE_GUIDE.md             # editorial and evidence rules
CHAPTER_TEMPLATE.md        # canonical authoring skeleton
chapters/                  # one Markdown file per module
labs/                      # working examples, setup scripts, notebooks
assessments/               # rubrics, exercises, answer keys (optional separate)
diagrams/                  # Editable Mermaid and custom SVG source
site/                      # Website CSS and client JS
scripts/build_site.py       # Markdown-to-HTML site builder
dist/                      # Generated website (do not hand-edit)
taxonomy/                  # Controlled vocabulary, ontology and relation map
social/module-NN/          # Question-led PDF, slide copy, post text
reviews/                   # Review prompts, results and evidence status
capstone/                  # PRD, blueprint, build, validation, defense
references/sources.md      # curated authoritative reading list (as expanded)
.github/                   # PR templates, Markdown lint, link-check (optional)
```

**Naming:** `NN-kebab-case-topic.md`; avoid dates in chapter filenames. Use relative links to other repository pages. Keep media as project-owned or properly licensed assets, never depend on hotlinked vendor graphics for the long term.

### GitHub workflow proposal

- Visibility: **private** (per learner preference).
- Branch: `main` for approved learning content; topic/lesson branches for authoring.
- Commits: concise, imperative messages (`docs: add sovereign AI classification module`).
- Reviews: technical check + source verification; legal review for specific legal claims.
- Final decisions: GitHub owner `shantanuchandra`, repo `sovereign-ai-mastery`, private visibility **required before remote publishing** (observed public on 2026-11-17); Inter/JetBrains Mono; academic footnotes; adaptive length; local-first Apple Silicon labs; separate solutions. Do not add a public reuse license unless explicitly approved.

## 10. Chapter acceptance checklist

- [ ] Accurate, readable, and consistent terminology.
- [ ] Concept -> mechanism -> architecture -> implementation -> PM decision progression.
- [ ] Practical enterprise scenario and UAE/GCC applicability.
- [ ] Primary-source evidence for legal, technical, and time-sensitive claims.
- [ ] Clear architecture diagrams and tested, safe commands.
- [ ] Trade-offs, failure modes, cost/operational constraints.
- [ ] Reusable PM artifact and measurable definition of done.
- [ ] Five-question quiz and one judgment scenario plus separate solutions and PM rubric.
- [ ] Assessment and source updates included.
- [ ] GitHub Markdown preview and accessibility check completed.

## 11. Publication acceptance additions (v3.0)

- [ ] Source quotations checked against original documents and linked with pinpoint footnotes.
- [ ] No AI slop: SCOPE edit completed; every statement is specific, contextual and decision-relevant.
- [ ] Taxonomy/ontology entities and relationships are defined or referenced and change-controlled.
- [ ] Website page builds, works without network access, and passes navigation/accessibility spot checks.
- [ ] Question-led HTML carousel and post created, with no solution leaks or exaggerated claims.
- [ ] Second-model critique status recorded **accurately**; internal self-review does not masquerade as cross-model review.


## 8. Website-first reader, highlighting & GitHub annotations (v4.0)

The learner's final format is a **book-reading website**, not a dashboard or generic docs portal. The index should resemble the opening pages of a well-edited book. Every chapter uses a three-column shell at desktop widths: **table of contents (left)**, **reading surface (center)**, **personal marginalia (right)**. On narrower screens, notes and navigation move into toggleable panels. Fonts must favor long-form readability: Georgia/Baskerville for prose and display headlines, system sans-serif for controls, and monospaced for code. Use warm paper backgrounds (`#fffcf5`), ink (`#1d302e`), and sparing clay (`#ad693f`) highlights. Never use remote font CDNs, tracking scripts, or third-party widgets by default.

**Required reader features:** complete seven-part TOC with 24 numbered modules; in-page section navigation; accessible quoted sources; selectable text, persistent highlights and notes; exact-quote and context-based reanchoring; no silent marking of changed, unmatched source passages; and privacy disclosure for annotation syncing. Source content remains Markdown, and the website is generated reproducibly with `python scripts/build_site.py`.

### Annotation storage and security

- The reader stores highlights and field notes in browser local storage first. Local storage is device/browser-specific and is not the cross-device source of truth.
- The GitHub sync control can read/write `annotations/notes.json` in the repository using GitHub Contents API. A **fine-grained personal access token with only Contents read/write for the selected repository** is supplied by the user in the browser for the current session; it is never committed, logged by app code, or stored in cookies/local storage. No shared secret may be baked into static HTML/JS.
- **All notes in a public GitHub repository are public.** If the user wants private notes, the implementation should support a separate private annotation repository. Never imply that a public course repo provides private annotations.
- GitHub writes are opt-in; the UI must not claim cross-device persistence before an authenticated upload succeeds. Report upload errors and retain local drafts. Store quote, stable page id, text offset, short context, timestamps, and user note, so annotations can be reanchored after minor editorial edits. Material changes may leave marks unmatched rather than misattach them.
- Never put credentials, sensitive workplace details, client data, legal strategy, or confidential conversations into public notes.

## 9. Question-led HTML carousel: design contract

- **Canonical social format:** `/social/module-NN/CAROUSEL.html`, containing 6–10 self-contained 4:5 portrait slides using HTML/CSS. In an exported PDF, each slide must occupy one page. The HTML remains editable and previewable in the browser.
- **PDF derivative:** export from Chromium print with backgrounds preserved and verify layout at portrait 4:5. The post remains fully usable if PDF export is unavailable.
- Slide 1 must open with a provocative **specific question**; each subsequent slide is also titled as a question. Mix layouts: statement, contrast, quote, framework, evidence, decision, challenge. Not every slide should be a wall of text or repeat a fixed template.
- Each slide carries a small module identifier, page number and restrained visual hierarchy. Use original geometric diagrams or diagrams from the chapter, not generic stock imagery or AI decoration.
- Include a final question that can stimulate thoughtful LinkedIn discussion, plus a route back to the complete chapter and key official sources. Never imply the slides constitute legal advice.
- If authoritative claims are repeated, give the exact citations in the chapter or a source page. Avoid unsourced sensationalism to boost engagement.

## 10. Publication gate for the book website

Before a module is marked ready, verify: left-rail course TOC; long-form chapter rendering; source quote ledger; ontology backlink; local lab; PM deliverable; separate solutions not publicly copied; selection/highlight/note behavior; mobile layout; HTML question deck; PDF export check; bibliography links; and no console errors. Run the local browser QA and static link checker. Mark unverified steps visibly; never substitute a claim of QA for an actual run.

## LinkedIn editorial design contract (v4.1)

- Source: `social/module-NN/CAROUSEL.html`, not a screenshot, canvas image, or PDF. 4:5 slide aspect ratio; use print CSS for a portrait document.
- Typography: two styles at most (an editorial serif for questions and a neutral sans for explanations). Maintain reading contrast of at least 4.5:1 for ordinary text and 3:1 for large headings. Never use cream-on-cream text or content clipped by the print page.
- Content: 7 to 9 slides; each slide headline must be a **real question**. One answer, mechanism, concrete example, counterexample, or decision per slide. Vary the structure across slides; don't make eight identical blocks.
- Evidence: reserve space for a compact source line when presenting a real product, regulation, benchmark or quotation. Attribute exact wording and distinguish direct source from editorial synthesis. Check every URL and publication date. Do not exceed reasonable quotation limits.
- Tone: ban em dashes (—), inflated claims, inspirational empty lines, decorative icons unrelated to the content, and stock imagery. Favor specific predicates and examples, not AI-sounding transitions.
- Delivery: inspect slides 1 through last at 1080×1350 preview size, inspect print/PDF with correct colors, text selectability and page breaks, and run a text scan for em dashes and unverified claims. The website chapter is the CTA destination.
