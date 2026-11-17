> **Website-first edition v3.0:** Final learner experience is a responsive static website; Markdown is the source. The sample [Module 05](chapters/05-laws-regulation-jurisdiction.md) demonstrates the required editorial contract: direct source quotations, ontology, practical lab, PM deliverable, assessment, separate solutions, and LinkedIn PDF.

# Sovereign AI Mastery

> A decision-first, hands-on, 24-week executive playbook for AI Product Managers designing **enterprise sovereign AI platforms** in the **UAE and GCC**, with global comparisons.

**Owner:** `shantanuchandra`  
**Repository target:** `shantanuchandra/sovereign-ai-mastery` (**public as approved by the owner**; annotations committed here will be public)  
**Editorial baseline:** v4.0 book-reader edition, 2026-11-17  
**Learning commitment:** ~240 hours / 24 weeks; adaptable to individual pace

## Start here

1. **[Table of contents](TOC.md)** — 7 parts, 24 modules, full lesson map, capstone plan, labs and PM deliverables.
2. **[Chapter template](CHAPTER_TEMPLATE.md)** — mandatory executive brief, deep dive, reproducible lab, PM decision playbook, five-question quiz and scenario, citations and follow-up.
3. **[Editorial and reference guide](STYLE_GUIDE.md)** — writing tone, visual system, source hierarchy, footnote style, lab standards and publication checklist.

## Who this is for

Intermediate AI PMs moving toward technical product leadership. The outcome is not merely knowledge of AI sovereignty terminology: the learner should be able to classify enterprise sovereignty requirements, assess vendor and architecture trade-offs, deploy a small local private AI reference system, evaluate governance controls, and defend an enterprise platform business case.

**Not a certification, legal opinion, or assurance of production compliance.** Course-authored sovereignty maturity models are educational decision tools, not official standards.

## Learning experience

Every module is authored in the **executive playbook** voice: **bottom line first**, rigorous but concise; length expands only when complexity warrants. Required elements:

- Conceptual explanation, trade-off table, Mermaid or custom diagram, and sourced UAE/GCC case with international perspective.
- **Practical lab** with observable acceptance criteria, cost and egress assumptions, failure recovery, and clean-up.
- **Distinct PM deliverable**, such as an architecture decision record, PRD, scorecard, procurement memo, or risk register.
- **Five-question quiz + decision scenario**. Solutions and PM scoring rubric live in a **separate** `assessments/solutions/` file.
- Academic-style Markdown footnotes attached to important claims, with official primary-source URLs and `Verified: YYYY-MM-DD`.

## Lab baseline

- **Computer:** Apple M4 Pro with 16 GB unified RAM.
- **Default:** Python, local virtual environment, Docker with ARM64-compatible images, Git, small locally hosted open-weight models where licensing permits.
- **GPU:** Prefer compatible macOS/Metal-backed inference executed on the host; do **not** assume CUDA or GPU passthrough in Docker on macOS.
- **Optional:** Cloud/GPU exercises for larger models, multi-node scaling, training, and production-like deployments, with published estimated costs and cleanup steps.
- **Security:** Synthetic/public data only. No real customer information, secrets, or embedded API keys.

## Capstone

Build and defend a reference **enterprise sovereign AI platform**: private model inference, secure RAG, constrained agents and tool access, tenant separation, auditable controls, performance/cost data, and an implementation roadmap. This is a learning implementation, not a statement of accredited sovereignty or regulatory compliance.

## Publishing conventions

Chapter paths: `chapters/part-XX-name/NN-short-title.md`  
Solution paths: `assessments/solutions/NN-short-title-solutions.md`  
Branch strategy: `main` as accepted content; topic branches for edits.  
Commit style: `docs: ...`, `lab: ...`, `fix: ...`.  
Visual identity for exports: **Inter** / **JetBrains Mono**, midnight navy / teal; standard GitHub Markdown controls actual GitHub display fonts.

**Repository visibility:** public, as approved by the owner. This does not make personal annotations private: syncing notes into `annotations/notes.json` will expose them publicly. A separate private notes repository is recommended for confidential thoughts. No open-source license is granted by this README. Third-party model, source, dataset, and image licenses must be respected.

## Authoring workflow

1. Pick the next module from [TOC.md](TOC.md).
2. Copy [CHAPTER_TEMPLATE.md](CHAPTER_TEMPLATE.md) to its chapter path and draft the learner-facing lesson.
3. Write a *separate* solutions file with verified lab results, answers, rationale, and PM rubric.
4. Review technical accuracy, primary-source links, timestamps, accessibility, costs, security assumptions, and GitHub Markdown rendering against [STYLE_GUIDE.md](STYLE_GUIDE.md).
5. Merge reviewed changes into `main`.

## Preview the website

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-site.txt
# Recommended for full-featured academic footnotes on macOS: brew install pandoc
python3 scripts/build_site.py
python3 -m http.server 8000 --directory dist
# Open http://localhost:8000
```

The builder uses Python and Pandoc (if available) for full Markdown+footnotes rendering; it includes a small fallback renderer for portable local previews. The build copies local CSS/SVG, not remotely hosted scripts. **The generated `dist/` website is the publication artifact**; author and review content under source Markdown files. The book design lives in `site/assets/site.css`; interactivity in `site/assets/annotations.js`. The notes toolbar requires an optional user-supplied, narrowly scoped GitHub token; it is never embedded in the site.

## Ontology and source integrity

- [`taxonomy/ONTOLOGY.md`](taxonomy/ONTOLOGY.md): explicit vocabulary and entity relationships. A course-authored model, not an official standard.
- [`STYLE_GUIDE.md`](STYLE_GUIDE.md): quote original sources with pinpoint citations; no AI slop; date and attribute claims.
- [`reviews/SECOND_MODEL_REVIEW_PROMPT.md`](reviews/SECOND_MODEL_REVIEW_PROMPT.md): independent-model challenge prompt; no independent review claimed until output is attached.
- [`social/module-05/05-questions.pdf`](social/module-05/05-questions.pdf): example question-led LinkedIn document PDF and post copy.

## Publication gate

Module publication requires the chapter, lab and acceptance tests, solution key (not shipped in the learner site), question-led PDF and post, source quote ledger, taxonomy/ontology links, website build, and a completed editorial QA record. Do not imply academic accreditation, legal approval, or certified sovereignty.


## Reader UI and annotations (new)

The homepage now resembles the opening page of a book, not a dashboard. Desktop layout: 24-module table of contents on the left, chapter on the central paper page, and a notes margin on the right. Select a text passage and choose **Highlight** or **Add note**. Marks are anchored to the exact quote, text offsets and neighboring context, and remain available in the same browser after refresh.

To persist across devices in GitHub, open **Sync with GitHub**, create a fine-grained personal access token scoped to this repo with **Contents: Read and write**, paste it into the session-only input, and authorize a sync. The site creates/updates `annotations/notes.json` via GitHub API. Token lives in memory for that browser tab only. **Because this repository is public, saved notes are public. Do not save secrets.** To keep notes private, create a separate private GitHub repository and select its `owner/repo` in the sync dialog; authorize a token scoped to that private repository.

The LinkedIn carousel is now authored in editable, standalone HTML at [`social/module-05/CAROUSEL.html`](social/module-05/CAROUSEL.html), with an **Export PDF** button and 8 distinct portrait layouts. The earlier PDF remains available as a historical sample; the HTML is now the canonical source.