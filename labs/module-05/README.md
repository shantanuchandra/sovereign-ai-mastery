# Module 05 lab — prepare legal questions from processing evidence

**Fictional educational simulation.** All workloads, reviewers and evidence URLs in `cases.json` are invented. The program validates a local register; it neither inspects infrastructure nor determines applicable law. Its strongest output is `REVIEW_REQUIRED`.

**Outcome:** Build an applicability matrix for review and discover a prohibited support, backup, preprocessing or licence route before comparing price. Read [Module 05](../../chapters/05-laws-regulation-jurisdiction.md) and its [ten-hour study plan](../../learning/schedule.html#module-05).

## Environment and budget

Python 3.10+ standard library on local CPU, including an Apple Silicon M4 Pro with 16 GB memory. No Docker, GPU, model download, cloud account, API key or paid service. Use public source text and synthetic records only. Reserve 90–120 minutes for the executable exercise and additional study time for the review matrix.

## Run the exercise

From the repository root:

```sh
python3 labs/module-05/evaluate.py labs/module-05/cases.json
python3 -m unittest discover -s labs/module-05 -p 'test_*.py' -v
```

The first command prints 14 results as JSON; the second runs adversarial tests. No network request is made. Exit code 2 indicates invalid input, not a finding that a law has been violated. A scenario marked BLOCKED is valid lab input and does not make the program crash.

## Procedure

1. Save a working copy of `cases.json` outside `sources/`. Predict the disposition for each ID before reading the output. Every supplied review and test record is a synthetic assertion.
2. Identify all nine lifecycle paths: source, preprocess, inference, retrieval, output, telemetry, backup, support, activation/update. Explain what derived data each path might contain. An omitted path must remain unresolved.
3. Inspect `PLANT-OFFSITE-INFERENCE` and `SPEECH-PREPROCESS-EXPORT`. Both use a domestic destination outside the named physical site. Explain why final local inference cannot repair an earlier off-site step.
4. For the air-gap case, change the activation flow from `network: true` to `false`. Then delete its observed test evidence. Record both outcomes. Local placement plus a boolean does not establish actual disconnection.
5. Set a transfer review to `reviewed` while retaining a prohibited route. Check that a review label does not waive the signed scenario boundary. Restore the file afterward.
6. Remove the backup row; replace a country with `UNKNOWN`; remove a review reference; report an adverse observation. Re-run separately and retain outputs with file versions.
7. Open the chapter's primary sources and prepare separate UAE federal, DIFC, ADGM and Saudi reviewer questions. The evaluator does not select a regime, evaluate legal mechanisms or infer localization from country selection.
8. Export a synthetic Studio journal for a premises-only or air-gapped workload. Compare its proposed lifecycle paths with this lab register. List any gaps; do not present either tool as observed production evidence.

## Acceptance and evidence packet

Require a prediction/output comparison, three mutations, the original and modified file hashes, a nine-path inventory, an applicability matrix, outstanding reviewer questions, named fictional owners and a bounded release decision. Keep observations and conclusions separate.

`BLOCKED` means a reported veto exists; `UNVERIFIED` means evidence/review is missing; `REVIEW_REQUIRED` means complete assertions still need substantive review. No supplied case grants legal, vendor or physical assurance.

For the PM artifact include instrument/version/pinpoint, activity, entities and roles, recipient/site, purpose, policy authority, legal question, test evidence, owner, status and change trigger. Treat a source quote, an executed contract and a runtime observation as different evidence types.

## Root-cause drill

A synthetic timeout attempts an off-site support upload; the gateway blocks it. Preserve configuration, attempted destination, gateway event, application error and bundle schema. Do not claim a confirmed data breach from an attempted route alone. Investigate SDK support defaults and the procurement checklist that omitted support handling. Require local or disabled diagnostics, independently reviewed configurations, adverse-path tests, update/restore coverage and a dated decision. If offline licences, capacity or quality cannot meet the requirement, state NOT FEASIBLE UNDER CURRENT CONSTRAINTS.

## Cost and cleanup

Runtime is local and small. Delete temporary JSON/output copies when finished; retain only reviewed synthetic artifacts in a public learning journal. No external resources exist to tear down. Never put real customer identifiers or legal advice into the public repository.
