# Module 04 lab: dated ecosystem evidence is not deployment acceptance

**Learning decision:** Given a publicly documented AI strategy, research platform or provider model announcement, decide what that source actually establishes, and what evidence a UAE/GCC enterprise must still obtain before deploying. **A source citation is not a legal opinion, a contract, an independent benchmark or an air-gap/site-control test.**

**Duration:** 100–120 minutes including PM artifact review. **Equipment:** Python 3.11 or later, standard library only. No GPU, provider account, internet call, credentials or paid service is required. The lab evaluator runs entirely locally and makes **zero network requests**. All workload IDs, architecture candidates, ownership, evidence statuses and test observations are fictional. Public URLs are dated research references, not live links fetched by the script.

## Run the evidence-map exercise

From the repository root:

~~~sh
python3 labs/module-04/evaluate.py labs/module-04/cases.json
python3 -m unittest discover -s labs/module-04 -p 'test_*.py' -v
~~~

If your Python launcher is named `python`, use that in place of `python3`. Do **not** use real customer documents, privileged network traces, credentials or employee audio in your tests.

Files:
- [cases.json](cases.json): five dated public-source claim records plus four **fictional** architectures and evidence assertions
- [evaluate.py](evaluate.py): deterministic hard gates and missing-evidence decisions
- [test_evaluate.py](test_evaluate.py): seventeen negative and provenance test cases

The scripted decisions for unchanged inputs should be:

| Fictional ID | Claim and boundary | Script result | Why that status is correct |
|---|---|---|---|
| `GCC-DESK-04` | Approved managed processing locations; supplier role and law unknown | `UNVERIFIED` | A national strategy announcement cannot verify a service or signed contract |
| `GCC-PLANT-04` | Exact named FACTORY-A premises, including speech, embeddings, diagnostics, support and backup derivatives | `BLOCKED` | Synthetic restricted ASR export attempt violates the named physical-site constraint |
| `GCC-OT-04` | No inbound or outbound networking of any kind | `NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS` | A required offline model licence is unavailable in the fictional scenario |
| `GCC-QA-04` | Synthetic Arabic dialect evaluation at an approved named lab | `UNVERIFIED` | An unreviewed synthetic test is not task-level evaluation acceptance |

**No deployment is certified.** Even if you change each fictional evidence label to `reviewed` with an associated `test_id`, the evaluator's highest no-conflict state is `REVIEW_REQUIRED`. “Source inspected” in the public claim ledger never becomes “data-center or model verified.” Each actual customer site needs physical/network evidence, actual model licences, applicable-law counsel review, native-speaking language evaluation and authorized sign-off.

## Exercise 1: reproduce a dated public-actor evidence map (20 min)

Read the **issuer-controlled** source URL for each of the five claim rows. Verify that it is an announced strategy, a research platform, a vendor/model offering or a regulatory timeline. In the claim register, record:

| Source ID | Issuer | Public instrument type | What it supports | What it cannot prove | Checked date / reviewer |
|---|---|---|---|---|---|
| UAE-STRATEGY-2019 | UAE AI Office | National strategy signal | Opportunity/ambition to explore AI | Specific supplier's customer compliance | [add timestamp] |
| UAE-TII-EMIRATI-2026 | TII | Model announcement | Arabic language/speech/OCR model-family existence | Dialect accuracy for your users or physical air gap | [add timestamp] |
| KSA-ALLAM-2024 | IBM/SDAIA | Hosted model offering | ALLaM announcement | Customer endpoint residency and offline rights | [add timestamp] |
| QATAR-FANAR-2026 | QCRI/QCAI | Research platform | Fanar project existence | Model licence, deployment controls | [add timestamp] |
| EU-AI-ACT-2026 | Council of EU | Regulatory timeline | Dated, role-dependent compliance review | Application to a specific fictional company without legal analysis | [add timestamp] |

**Source discipline:** An official issuer announcement is primary evidence of what the issuer announced, **not independent evidence of advertised benchmark superiority**. For sources without a reliable publication date, preserve `unknown`. Do not invent a date just to make a sorted landscape chart appear complete. The source rows represent the **dates of the material examined**, not its actual future availability or every provider's current catalog.

## Exercise 2: separate model origin, control and hosting (20 min)

For each fictional workload, identify the physical/contractual authority, model origin, serving location, data/derivative paths, support/operator location, network rule, licences and which gaps must go to legal versus engineering versus a native Arabic quality reviewer.

Prepare a **jurisdiction × actor × source × model × runtime × control** matrix. Keep public claims on one side and *observed customer control evidence* on the other. An Arabic model developed by an institution in one GCC country may be a legitimate sourcing candidate for a permitted external workload, but its origin never proves that a **named UAE factory premises** constraint or **air-gapped** requirement is satisfied.

## Exercise 3: break the premises-only design (20 min)

In a scratch copy of `cases.json`, change `GCC-PLANT-04` candidate `compute_site` to `DOMESTIC-DC`, change `restricted_offsite_derivative` to `false`, and change the first claim's `evidence` from `adverse` to `configured`. Observe that a **domestic data centre outside FACTORY-A** is still `BLOCKED`. Restore the site to `FACTORY-A`; the status becomes `UNVERIFIED`, not approved, because editing a JSON flag is not an independently observed remediation.

Test the full data inventory: source, retrieval chunks, prompts, embeddings, outputs, ASR transcripts, OCR text, translations, evaluation artifacts, adaptations, logs, diagnostics, operator access, support and **backups**. A real-world reviewer would need synthetic network negative tests, normal/crash/timeout/restore/update traces and site-specific evidence. The script has not run those infrastructure tests.

## Exercise 4: challenge a physical air gap and an offline licence (20 min)

For `GCC-OT-04`, set `offline_licence_available` to `true`, but change `network_mode` from `disconnected` to `private_links`. The result must be `BLOCKED`. Restore `network_mode` to `disconnected` and instead set `external_management_path` to `true`; the result must still be `BLOCKED`.

Restore `external_management_path` to `false`; you should now see `UNVERIFIED` because actual physical disconnection, offline acquisition of model artifacts, rights, capacity, quality, removable-media handling and restore were never demonstrated. A “temporary” supplier VPN is not an exception.

If no model/ASR/OCR capability can be lawfully licensed and operated entirely offline, record **NOT FEASIBLE UNDER CURRENT CONSTRAINTS** and propose an authorized manual/non-AI fallback rather than a connected substitute.

## Exercise 5: Arabic model testing and failure RCA (20–40 min)

Using **synthetic** Arabic phrases and invented asset IDs only, prepare a 12-row paired evaluation plan across MSA, Emirati dialect, another Gulf dialect, Arabic-English code-switching, RTL layout, ASR and OCR. Do **not** claim to have run any model benchmark unless you actually ran it. For each test state the expected intent, critical entity, output safety condition, human reviewer and success threshold.

**Fictional failure to investigate:** A text model stays on-site, but a voice adapter attempts to send synthetic restricted speech to an external ASR endpoint during a timeout. The perimeter firewall blocks delivery. Record **expected versus observed**, direct cause, contributing process cause, containment, corrected local-only architecture, evidence-specific retest, named closure owner and decision. Distinguish a successful egress firewall denial from a **failed application architecture invariant**.

## PM artifact: comparative ecosystem landscape and executive implications

Deliver a two-page decision memo with these sections: (1) dated source landscape for UAE/Saudi/Qatar/EU, with explicit publisher claims and limitations; (2) four fictional workloads and an eligibility-first **hard gate** decision; (3) supplier and model rights/portability, hosting and operator dependencies; (4) a ranked shortlist **only among eligible candidates**, with language quality, safety, cost and accessibility assumptions clearly marked UNKNOWN where not tested; (5) 30/60/90-day evidence collection roadmap, RACI and next review trigger; and (6) an RCA for the remote-ASR failure.

**Scoring (20 points, instructor-authored):** 4 for dated issuer claim provenance; 4 for independent hard-gate evaluation; 4 for Arabic task/dialect coverage; 4 for evidence ownership and negative test design; 4 for a bounded PM recommendation with a correct non-AI fallback. A student can earn full points by issuing a justified **BLOCKED** or **NOT FEASIBLE** decision. Answers must not live in the public learner chapter; any worked examples and rubric solutions belong in a separate facilitator artifact.

**Next release gate:** The Module 04 learner assessment requires five knowledge questions, one full decision/RCA scenario and separate solutions, then a designed question-led social HTML/PDF/post and two distinct critical self-reviews. Module 05 must not start before these educational module acceptance gates are complete. Independent real-world safety, accessibility and legal reviews remain outside the scope of this fictional exercise.
