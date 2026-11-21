# Module 04 technical, security and source-accuracy critical review

**Date:** 2026-11-22. **Reviewer:** GPT-6, bounded self-critique. **Independent human/different-model review:** NOT COMPLETED. **Disposition:** HOLD pending CI and source assurance.

## Scope and evidence

Read `TOC.md`, `STYLE_GUIDE.md`, `CHAPTER_TEMPLATE.md`, the Module 04 chapter, local lab README, separate facilitator solutions, social HTML and post, publishing contract test, Pages workflow, previous improvement records, and failed workflow [44957233405](https://github.com/shantanuchandra/sovereign-ai-mastery/actions/runs/44957233405). The failed job's traceback identifies `qa/test_module04_social_contract.py::test_site_wiring`: the builder lacked a literal `module-04/CAROUSEL.html` chapter link. The corrective [commit 29c52a9](https://github.com/shantanuchandra/sovereign-ai-mastery/commit/29c52a99388754f94a11117a73e760049e001848) adds explicit links to the Module 04 carousel and post; CI result for that commit was not available at review time.

## Findings

| ID | Severity | Observation | Closure evidence |
|---|---|---|---|
| T04-01 | BLOCKER until validated | Module 04 social contract failed on prior head. Chapter navigation omitted the actual carousel and post links, despite copying social assets to dist. | Corrected in source; require successful new Pages run and rendered link test at exact head SHA. |
| T04-02 | MAJOR | The local lab uses synthetic evidence labels and deterministic hard gates. Its passing tests can demonstrate evaluator behavior, not supplier contracts, physical isolation or lawful processing. | Preserve `REVIEW_REQUIRED` ceiling, premises-only and air-gap hard vetoes; obtain qualified site/operator evidence for any real deployment. Not a curriculum code defect, but real-world assurance NOT COMPLETED. |
| T04-03 | BLOCKER for source sign-off | Chapter spans multiple GCC jurisdictions and named issuers. This review did not independently reopen and compare every material quotation, issuer publication date, legal scope or source pinpoint. | Perform a complete source-ledger audit; correct mismatches and retain issuer retrieval dates distinct from publication dates. |
| T04-04 | MAJOR | Generated eight-page PDF exporter and tests exist in source, but the previous workflow stopped before PDF export. | Observe actual export step, page/size/text assertions and deployed artifact in successful CI. |
| T04-05 | MAJOR | Strategy and vendor announcements do not establish workload-specific sovereignty. | Preserve distinctions among policy, product claim, procurement contract, technical observation and legal advice; require explicit owners and evidence. |

## Technical decision

The fictional factory's off-premises speech/embedding/backup path remains prohibited even when the target is within the same country. A physically air-gapped terminal cannot use remote support, telemetry, online licensing or emergency cloud fallback. A blocked gateway request is evidence of gateway denial, **not** proof that the application routing policy is correct. A supplier promise is not an independent test. These are course-authored teaching constraints, not purported universal GCC law.

**Tests actually inspected:** Prior CI job step conclusions show the Module 04 GCC evidence lab passed, and the Module 04 social publication contract failed; all downstream PDF/site/deployment steps were skipped. No local Python execution, physical network inspection, packet capture or independent legal review was performed in this self-critique.

**Disposition:** HOLD. T04-01 and T04-04 await successful post-fix CI. T04-03 awaits full issuer audit. Do not advance Module 05 on this review alone.
