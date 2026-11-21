# Module 03 source-accuracy ledger: claim-level documentary audit

**Audit date:** 2026-11-21 (Asia/Kolkata). **Auditor:** GPT-6 bounded self-audit, not an independent human or different-model review. **Scope:** `chapters/03-enterprise-sovereignty-requirements-strategy.md`, Module 03 facilitator solutions and question-led social material. **Sources reopened directly:** NIST AI RMF 1.0 Core and Executive Summary, NIST SP 800-207 official publication abstract, and the Ollama maintainers' README. **Disposition:** source quotations and bounded external product claims inventoried and reconciled for this chapter revision; no product, legal, physical-isolation or independent certification.

## Method and revision

1. Locate every explicitly attributed external reference in the seven Module 03 teaching headers and assessment. Separate quotations from the many fictional scenario statements and course-authored requirements/control heuristics.
2. Reopen the primary issuer-hosted page; compare each short quoted string, section label and publication version with surrounding meaning.
3. Record both what the text supports and what it **cannot** establish. Do not treat the GitHub repository's authoring timestamp as the vendor's publication date.
4. Correct misquotation and overbroad vendor-description wording in the learner chapter; add a source-text regression assertion. The regression is a **local-file consistency check**, not an online primary-source verification test.

**Corrective chapter commit:** [701984d](https://github.com/shantanuchandra/sovereign-ai-mastery/commit/701984d28bcf4433f6540eff20189c20cd7d15aa) fixes NIST's hyphenation and clarifies that the Ollama README illustrates a localhost API and lists cloud deployment integrations; neither fact demonstrates an air-gapped installation. **Source regression commit:** [38f9a5d](https://github.com/shantanuchandra/sovereign-ai-mastery/commit/38f9a5d7645aa344c3fc9ed2c783f1976eb86616).

## External source and claim inventory

| ID and chapter scope | Original issuer / exact pinpoint | 2026-11-21 comparison and disposition | Limit of the supported conclusion |
|---|---|---|---|
| S03-01; §3.1 | [NIST AI RMF 1.0, Core §5.2, MAP 1.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), published 2023 | **MATCH:** the chapter's deployment-settings quotation occurs in MAP 1.1 | NIST asks for documented deployment context; it does **not** establish a UAE data-residency law or sovereign cloud requirement |
| S03-02; §3.1 | Same Core, MAP 1.4 | **MATCH IN SCOPE:** MAP 1.4 addresses defining or re-evaluating business use/value | The six business-problem types and two-pass architecture screen are course-authored |
| S03-03; §3.1 | Same Core, §5.4 MANAGE 1.1 and MANAGE 2.1 | **MATCH:** MANAGE 1.1 contains the chapter's go/no-go words, and MANAGE 2.1 explicitly considers viable non-AI approaches | The wording supports risk-treatment decisions, not a mandated architecture or capital investment |
| S03-04; §3.3 | [NIST AI RMF 1.0, Executive Summary](https://airc.nist.gov/airmf-resources/airmf/0-ai-rmf-1-0/), published 2023 | **CORRECTED:** original chapter omitted the hyphen in `non-sector-specific`; the corrected short quotation now matches the official version | Framework scope is voluntary; it does not assert fulfillment of UAE law or contractual conditions |
| S03-05; §3.3, §3.4 | [NIST AI RMF Core §5.1, GOVERN 1 and GOVERN 1.5](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | **MATCH IN SCOPE:** governance processes, clearly allocated roles, periodic risk review are in the issuer's categories | The RACI, enterprise-veto order, evidence states and no-egress checks are course-authored teaching decisions |
| S03-06; §3.3, §3.4, §3.5, §3.7 | [NIST SP 800-207, official Abstract](https://csrc.nist.gov/pubs/sp/800/207/final), published August 2020 | **MATCH:** chapter's short “no implicit trust” wording and location-based trust interpretation agree with the abstract | Zero-trust authentication/authorization principles are not territory or physical site certification |
| S03-07; §3.5 and §3.7 | NIST AI RMF Core §5 opening | **MATCH:** the quoted checklist limitation occurs in §5 | An enterprise's controls still need testable acceptance; this does not create an official NIST sovereign-AI control checklist |
| S03-08; §3.5 and §3.7 | NIST AI RMF Core, GOVERN 1.5 | **MATCH:** cited short periodic-review excerpt and responsibility concept occur in GOVERN 1.5 | Evidence-expiry graphs and scorecards remain instructional constructions |
| S03-09; Q5 and facilitator Q5 | [Ollama maintainers, `README.md`, REST API section](https://github.com/ollama/ollama/blob/main/README.md), accessed 2026-11-21 | **MATCH:** the README contains the chapter's local REST API quote and shows `http://localhost:11434/api/chat` | Localhost API documentation does **not** establish an offline installation, licence rights of a selected model, absence of outbound cloud paths, operational air-gap status, or an approved customer deployment |
| S03-10; Q5 | Same Ollama README, Infrastructure & Deployment / Cloud integrations | **QUALIFIED:** the README lists cloud deployment integrations; the previous chapter language “advertises local or cloud use” was too broad for that cited passage | The presence of an integration list does not establish default routing or actual customer egress |

**Publisher and version caveats:** The NIST pages identify the quoted content as **AI RMF 1.0 (2023)** and warn that a revision is in progress; this audit does not relabel 1.0 as a newer edition. NIST SP 800-207 states **August 2020**. The Ollama README uses a moving `main` branch; its content was inspected on 2026-11-21, but its publication/update date and a fixed source commit were not established by this audit. Recheck the vendor passage if it changes.

## Coverage of the seven teaching headers and social material

- **§3.1:** MAP 1.1/1.4 and MANAGE 1.1/2.1 checked; strategy and fictional financial assumptions are course-authored.
- **§3.2:** Data sensitivity, criticality and impact axes, physical-premises examples, egress hierarchy and simulated failures are teaching assumptions. No external statutory mandate is asserted in this section.
- **§3.3:** AI RMF Executive Summary, GOVERN and NIST SP 800-207 checked. The exact Executive Summary quote was corrected.
- **§3.4:** NIST GOVERN/MAP and SP 800-207 are explicitly described as context for a course-authored RACI and approval workflow; no vendor/product performance claim.
- **§3.5:** AI RMF Core opening, GOVERN 1.5 and SP 800-207 checked. The ten-field test specification is not presented as NIST's own standard.
- **§3.6:** Cost scores, alternatives, architecture and RCA remain fictional assumptions with no newly attributed outside numerical result.
- **§3.7:** Repeats the checked NIST AI RMF and zero-trust concepts; no additional primary issuer identified.
- **Q1–Q6 and the facilitator key:** Q5 is the only named real product source: the bounded Ollama README. Q6 is a synthetic failure, not a reported incident. The facilitator's Q5 reasoning explicitly rejects vendor-documentation-as-air-gap-proof.
- **LinkedIn HTML, slides and post:** Their premises-only, disconnected, risk-gate and board-decision examples are educational claims based on the chapter's fictional design. No added real customer incident, vendor SLA, statutory quotation or numerical outcome identified in the inspected text.

## Publication distinction and residual blockers

**Educational source-audit outcome:** No remaining *identified* external quotation mismatch after the two chapter corrections. This is a source-level self-audit of the listed materials; a separately commissioned reviewer should challenge completeness and interpretation before independent sign-off. The regression test should pass in a new completed CI workflow before treating this revision as technically published.

**Do not close on the strength of source evidence:** T03-02 requires real physical air-gap and recovery evidence **if a real deployment is ever being approved**; the fictional training exercise cannot obtain it. The educational chapter must continue to label isolation as unverified, rather than demand fabricated site inspection. E03-02 manual keyboard, screen-reader, zoom/reflow and PDF reading-order checks remain open. E03-03 independent grading calibration remains open. Both distinct critical reviews are GPT-6 self-critiques, **not independent reviews**. Module 03 remains HOLD under the course's existing two-review release contract.

**Reusable lesson:** Check exact punctuation in official quotations; distinguish a publisher's documented endpoint or integration catalog from proved operating behavior; scope source acceptance, CI acceptance, accessibility acceptance and real-world security acceptance separately.
