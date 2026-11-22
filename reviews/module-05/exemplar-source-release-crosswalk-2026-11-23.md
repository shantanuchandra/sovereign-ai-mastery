# Module 05 website exemplar → source chapter reconciliation (draft-only)

**Prepared:** 23 November 2026. **Reviewer:** GPT-6 same-model source inspection. **Disposition:** RELEASE HOLD. This document is an author-side comparison, not independent legal, accessibility or assessment sign-off.

## Why this exists

The live site already has a hand-authored [Module 05 exemplar](../../modules/05-laws-regulation-jurisdiction.html), while the full TOC-aligned learner Markdown, lab validator, unit tests, answer key and PDF exporter were authored later on [draft/module-05-legal-controls-20261123](https://github.com/shantanuchandra/sovereign-ai-mastery/tree/draft/module-05-legal-controls-20261123). They are **different editions**. A successful draft-only CI run does not update the published HTML or make its references valid on \`main\`.

## Observed differences and release plan

| Area | Existing live exemplar (\`main\`) | Draft source branch | Release acceptance action |
|---|---|---|---|
| Lesson organisation | Four regional source subheads (§4.1 UAE, §4.2 DIFC, §4.3 ADGM, §4.4 Saudi, §4.5 EU, §4.6 evidence) plus a 14-section teaching essay | Eight **TOC 5.1–5.8** lessons: federal, DIFC/ADGM, sector/critical, Saudi, GDPR/EU, transfers/vendors, jurisdictions vs controls, requirements mapping | Render from approved Markdown and verify all eight headings and the sidebar navigation; don't silently carry over a partial 4.1–4.6 outline |
| Evidence dates | Site states last official-source check **17 Nov 2026** and its content includes dated regime summaries | Source footnotes label bounded overview/guidance checks **23 Nov 2026**, with explicit *not fully reviewed* clauses for consolidated law | Review actual authoritative versions on release date; retain per-source checked vs pending states; do not merely change dates |
| Lab promise | Live exemplar instructs readers to run \`labs/module-05/validate.py\` and \`control_map.json\` from root | Lab JSON, validator, 17 tests and README exist only on **unmerged draft branch** | Confirm the generated live build includes the validated lab assets at actual paths; until then the old live link/instruction is a known unavailable learner workflow |
| Answer key | Exemplar names separate \`assessments/solutions/05-laws-regulation-jurisdiction-solutions.md\` | 40-point facilitator key exists on draft branch | Ensure spoiler-free learner HTML, adequate facilitator-only answer visibility and approved publication rules; source key must not leak into quiz view |
| PM decision and RCA | GulfCare offshore support log scenario, legal-control-evidence matrix and a six-question quiz | Expanded source includes explicit named-premises and all-network air-gap veto, complete system graph, cold-start diagnostics RCA and acceptance owner | Review severity/status and glossary for consistency across published lesson and lab |
| Visual diagram | Existing hand-authored HTML uses designed reader styling | New Markdown embeds Mermaid; source guide requires a static SVG to render without CDN/JS | Export legible accessible SVG with text alternative and verify visible site diagram; Mermaid source alone is not proof of rendered diagram |
| Social learning | Existing Module 05 HTML question deck and POST.html predate draft | Updated same deck on draft branch, new POST.md and PDF exporter, portrait 8x10 test | Align headline, source claims, source dates and no em dashes; publish only after review and successful site build |
| Access | Public site HTML currently reachable by design | New Markdown release gate remains **HOLD** because Module 04 is not signed off | Treat old HTML as teaching exemplar, not as a published/approved Module 05 artifact |

## Concrete learner-facing risk discovered

The old public HTML explicitly offers a runnable Module 05 lab and separate solutions file. The **main branch at this audit** does **not** contain \`labs/module-05/validate.py\`, \`labs/module-05/control_map.json\` or \`assessments/solutions/05-laws-regulation-jurisdiction-solutions.md\`; those were created later on the draft branch. A learner opening the site's old exemplar cannot reproduce those exact repository commands from public \`main\`. Do not mark this as a working deployed lab because the **draft** CI succeeds.

**RCA:** The book-first/HTML exemplar was published ahead of the full Markdown and its lab/key dependency package. **Containment:** Keep the new package on the draft branch pending prior-module review, and avoid a fresh claim that the live Module 05 lab is available. **Corrective release action:** Build from the reviewed Markdown, package the actual lab assets (without exposing facilitator spoilers unintentionally), run path-resolution and browser tests against the **deployed** exact commit, and put a test in CI that verifies every surfaced lab command resolves to shipped files.

## Quality gates that remain genuinely open

1. **Module 04 prerequisite**: [Issue #7](https://github.com/shantanuchandra/sovereign-ai-mastery/issues/7) independent accessibility/PDF evaluation, calibration and source nonreliance reviewer acceptance.
2. **Legal accuracy**: qualified current consolidated UAE/DIFC/ADGM/Saudi/EU text and applicability review; official overview pages alone do not satisfy it.
3. **Module 05 independent assessment**: blind alternative rater for both fluent-but-unsafe and safe-but-incomplete Q6 submissions.
4. **Manual accessibility**: 320px/200% zoom, keyboard, screen reader, link names, contrast, PDF tagging and reading order. A Playwright reflow smoke test is useful but never substitutes for assistive technology.
5. **Release integration**: site builder, static Mermaid/SVG, navigation, 8x10 PDF and lab asset routes validated in a published exact-head Pages run.

**Next release-oriented work:** Strengthen draft rendered carousel layout tests and fix content clipping; then use a branch-scoped site rendering test and review the legal source versions. Do not merge before Module 04's release HOLD is resolved.
