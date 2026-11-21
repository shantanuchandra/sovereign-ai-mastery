# Module 04 editorial, accessibility and assessment critical review

**Date:** 2026-11-22. **Reviewer:** GPT-6, second distinct bounded self-critique (editorial/accessibility/assessment). **Independent human/different-model review:** NOT COMPLETED. **Disposition:** HOLD.

## Inspected material

`TOC.md`, `STYLE_GUIDE.md`, `CHAPTER_TEMPLATE.md`, Module 04 chapter, lab README, separate Q1–Q6 facilitator solutions, eight-slide HTML carousel, LinkedIn post, publishing test and latest available CI failure. This review assesses teaching usability and answer separation, not infrastructure assurance.

| ID | Severity | Finding | Required evidence |
|---|---|---|---|
| E04-01 | MAJOR | Module 04 has seven numbered teaching sections, a synthetic evidence-map lab and a separate 40-point six-question key. This supports progression, but a chapter status table still describes the cumulative assessment/social deliverables as pending, which is now stale. | Update learner-facing status to distinguish authored, tested and verified deployment states; do not claim completed review gates. |
| E04-02 | BLOCKER until verified | Carousel has eight question-form `h2` headings, section labels, responsive/print CSS, and visible keyboard focus style. Source inspection cannot establish 195/320px reflow, zoom, contrast, keyboard order, screen-reader announcements or print/PDF reading order. | Run automated responsive/PDF checks in CI, then manual browser/assistive-tech inspection where possible. PDF is not tagged; keep accessible HTML alternative and do not claim certification. |
| E04-03 | MAJOR | Facilitator Q1–Q6 worked answers and rubrics are separate from learner content. No independent inter-rater assessment calibration was observed. | Score two contrasting synthetic learner submissions, document ambiguous scoring criteria and request a second independent rater before claiming calibration. |
| E04-04 | MAJOR | Social post correctly identifies fictional incident and rejects cloud licence/remote support exceptions. A chapter-next link to the carousel/post was missing and caused CI failure. | Source fix exists in commit 29c52a9; verify rendered navigation and accessibility in new CI. |
| E04-05 | MINOR | A few long chapter segments revisit the same premises-only factory example. Repetition is useful only when it changes the learner's artifact or decision. | Conduct targeted redundancy edit without deleting unique RCA, comparison, source or challenge details. |

## Assessment boundary and review decision

A high rubric score must never waive a named-premises or physical air-gap veto. The source-authored LinkedIn carousel is a public teaching derivative, not a facilitator answer key. No claim of tagged PDF, independent learner calibration, accessibility certification, independent human review or production legal assurance is made.

**Checks performed:** Source-level editorial review and inspection of CI failure traceback; no manual keyboard, screen-reader, print inspection, learner study or independent scoring occurred.

**Disposition:** HOLD until stale learner-facing progress metadata is corrected, actual post-fix CI passes, accessibility evidence is scoped honestly, and assessment calibration is recorded. This is distinct in purpose from the technical/security/source self-critique.
