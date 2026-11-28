# Module 18 editorial, accessibility and assessment development review

28 November 2026. Separate same-author AI-assisted self-critique by Codex/GPT-6 module author; exact model revision not exposed. Independent and different-model review NOT COMPLETED. Module 04 remains HOLD. This records development checks, not deployed publication approval.

## Editorial and assessment inspection

The chapter has one title, 14 core sections and all seven TOC topics (18.1–18.7). Its approximately 4,000 words connect decisions to complete dependencies, current retirement, hard boundary gates and testable acceptance. BANK-A and the comparison enterprise are explicitly fictional. Geographic assumptions are contractual teaching constraints, not blanket UAE/GCC legal duties. Source facts, author analysis and actual local observations are separated.

Ontology references align with v1.8: RestoreExercise tests ExitPlan; ExitPlan reconstructs the model artifact and operating dependencies; AssuranceSnapshot evaluates a control and reopens review on relevant change. Mermaid, static SVG and the chapter text equivalent express the same decision flow. SVG includes title/description, visible labels and explicit BLOCK/UNVERIFIED language; no status depends on color alone. XML parsing passed. Final rendered SVG/chapter visual assessment remains with coordinator/manual review.

Q1–Q5 ask about objective scope, complete backup/current decisions, actual record outcomes, assurance limits and a real documented PostgreSQL restoration warning. Q6 requires status transitions, root causes, containment, roles and a concrete date. The separate key assigns 5 points each to Q1–Q5 and 15 to Q6, total 40. The distinct EXIT_PLAN.md has five 0–4 dimensions, total 20. No key is embedded in public lesson/social assets. Independent scoring calibration remains open.

## Actual rendering checks

The default Python lacked Playwright. The existing `/private/tmp/sovereign-module08-qa` environment supplied Playwright and pypdf. A restricted browser launch initially failed with a macOS process permission error; the approved local browser run then succeeded. No source content or browsing destination was external during the check: the test permits local file requests and blocks other requests.

```bash
PLAYWRIGHT_BROWSERS_PATH=/private/tmp/sovereign-ai-browsers /private/tmp/sovereign-module08-qa/bin/python social/module-18/test_rendered_carousel.py
```

Actual result: PASS for eight question headlines; document and slide overflow at 1280, 390 and 320 px; a deliberately injected horizontal-overflow mutation detected by the checker; a keyboard-reachable chapter link; print slide clipping checks; eight temporary 8×10-inch PDF pages with extractable text and all expected headings. The test uses temporary PDF output and did not build or modify shared dist. `export_pdf.py` is supplied for the coordinator's publication step.

A static scan found no em dash in HTML or social Markdown. The slides use semantic sections and `aria-labelledby`, local font fallbacks, no distributed font binaries and no external assets/CDN. The 4:5 authored desktop/print layout adapts to taller mobile cards to preserve text. POST.md and SLIDES.md retain fictional and bounded-evidence limitations. HTML is preferred and PDF explicitly untagged.

## Remaining work and independent prompt

Programmatic overflow, keyboard and extraction checks do not establish screen-reader usability, visual contrast, 200% zoom, PDF tags/reading order or manual diagram legibility. Those are NOT COMPLETED. Independent editorial/assessment review, actual domain/Arabic checks, coordinator site/link/route validation and final exported PDF review remain pending.

Prompt: read the chapter and key separately. Check the seven topics, source scope, actual lab outcomes, scoring arithmetic and distinction between declaration, observed local behavior and production assurance. Render the chapter/SVG and all eight slides; inspect typography, keyboard order, screen-reader semantics, contrast and 200% zoom. Confirm the public reader excludes solutions and no carousel line implies production RTO/RPO or physical isolation. Record reviewer/model/version/date/prompt and actual findings. If not performed, retain NOT COMPLETED rather than implying approval.
