# Module 02 A-01: primary-source verification ledger (in progress)

**Date opened:** 2026-11-20  
**Reviewer:** GPT-6 course-maintenance self-audit; not independent source certification.  
**Release disposition:** **OPEN / BLOCKING**. This ledger inventories claims for checking; it does **not** upgrade historical footnote assertions to independently verified facts.

## Audit protocol

For each claim, reopen the **primary** URL, locate the exact passage and section, compare quotation punctuation and context, record the retrieval date, and distinguish source wording from the course's inference. If the source is inaccessible, revised or ambiguous, remove the quotation or mark it unverified; do not retain an asserted verification date as evidence of this review. For vendor claims, also verify the exact SKU, region, control-plane and support/backup configuration. Have a separate reviewer record final approval and any unresolved limitations.

## Section 2.1: inventory and bounded interpretation

| ID | Current chapter quotation | Primary source and pinpoint as cited in chapter | Historical claim in chapter | Audit result this run | Required decision |
|---|---|---|---|---|---|
| A01-2.1-OECD | “an inclusive, dynamic, sustainable, and interoperable digital ecosystem” | [OECD AI Principles, Principle 2.2](https://oecd.ai/en/dashboards/ai-principles/P11) | Footnote previously claimed verification 2026-11-19; source's webpage does not alone establish the historical check | **VERIFIED 2026-11-20:** exact substring occurs in Principle 2.2's recommendation beginning “Governments should foster...”; source applies to *government-enabling AI ecosystems* | Quote and pinpoint are correct. **Do not** infer any enterprise-location requirement or official national/sector/enterprise/workload sovereignty classification |
| A01-2.1-NIST | “prospective settings in which the AI system will be deployed” | [NIST AI RMF 1.0, Section 5.2, MAP 1.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Footnote previously claimed verification 2026-11-19 | **VERIFIED 2026-11-20:** exact substring occurs in MAP 1.1, whose full context covers intended purposes, laws, norms, expectations and prospective deployment settings; source labels the extract NIST AI RMF **1.0 (2023)** | Correctly supports documenting the deployment context, **not** the course-authored four-scope typology |

**Interpretation guardrail:** National, sectoral, enterprise and workload scopes are explicitly **course-authored**. Neither of the two cited sources should be described as having defined or endorsed this classification. The fictional CORP-01, PLANT-02 and OT-03 scenarios are design exercises, not reports of UAE deployment or legal obligations.


## Section 2.2: independent source spot-check, 2026-11-20

The following quotations and versions were checked **directly against the issuer's current HTML pages** during this iteration. They support the chapter's risk-management and zero-trust interpretations, **not** its course-authored territorial/operational/technological/legal taxonomy.

| ID | Exact excerpt as used in chapter | Primary source / pinpoint | Finding on 2026-11-20 | Scope and decision |
|---|---|---|---|---|
| A01-2.2-RMF-FUNCTIONS | “govern, map, measure, and manage” | [NIST AI RMF 1.0, Section 5 AI RMF Core, opening](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | **VERIFIED** against Section 5's opening; four functions listed in this order; version explicitly **AI RMF 1.0 (2023)** | These functions are **AI risk management functions**, not the four sovereignty control dimensions invented by this course |
| A01-2.2-RMF-CHECKLIST | “do not constitute a checklist” | [NIST AI RMF 1.0, Section 5 AI RMF Core, opening](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | **VERIFIED** as an exact substring of “Actions do not constitute a checklist, nor are they necessarily an ordered set of steps.” | Supports the chapter's warning against treating an RMF-derived list as certification |
| A01-2.2-ZERO-TRUST | “based solely on their physical or network location” | [NIST SP 800-207, *Zero Trust Architecture*, official abstract](https://csrc.nist.gov/pubs/sp/800/207/final) | **VERIFIED** as an exact substring in the abstract; NIST publication date **August 2020** | Supports identity/authorization review even at a physical enterprise premises; it is **not** a sovereign-AI location standard |

**Method actually used:** Opened and read [OECD Principle 2.2](https://oecd.ai/en/dashboards/ai-principles/P11), [NIST AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), and [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) on **20 November 2026**. Matched the exact in-chapter excerpts to the source HTML and checked their surrounding subjects and visible version dates. The cited documents are guidance, not product-level validation or legal findings. No supplier SKU, contract, region-specific runtime route, visual accessibility or actual air-gap control was tested. A human or distinct-model audit has **not** occurred.

**Partial finding:** These quoted excerpts require **no immediate chapter correction** based on this narrow source comparison. **A-01 remains OPEN / BLOCKING**, because substantial quotations/claims in sections 2.3–2.7, the Microsoft Foundry product example, facilitator key and social materials still require the same claim-by-claim treatment. A successful spot-check must not be generalized to the rest of Module 02.

## Remaining A-01 work

This is a **verified review of the two quoted passages in Section 2.1 plus the two cited NIST passages in Section 2.2 below**, not a chapter-wide source audit. Before closing A-01, enumerate all remaining quoted claims in sections 2.2–2.7, facilitator solutions and social assets. For each, record exact quote, pinpoint, publication/update date **only if verified**, retrieval date, region/SKU applicability, and the disposition `VERIFIED`, `QUALIFIED`, `REMOVED` or `UNVERIFIED`. Any unverified material assertion must be qualified or removed before release. Legal applicability remains for qualified counsel; a primary-source quote alone cannot establish compliance.

## Separate assurance still required

A-03 must include observed interactive negative-case outputs; A-04/B-01 require actual mobile/PDF visual inspection; B-02/B-05 require blind assessment calibration. Neither review A nor review B is signed off. No human or separate-model review has occurred in this ledger.
