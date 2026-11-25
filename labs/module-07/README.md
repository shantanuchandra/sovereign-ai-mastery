# Module 07 architecture graph lab (educational draft)

This is a course-authored simulation using only synthetic declarations. Use it with the [Module 07 lesson](../../chapters/07-end-to-end-sovereign-ai-stack-reference-architecture.md). It is not a production architecture assessment.

## Run locally

Python 3.11+ standard library; CPU only, suitable for the Apple Silicon/16 GB course baseline. No model, container, cloud account, paid resource or network call is required during evaluation. Downloading the public repository is the preparation stage. Verified here with Python 3.14 on macOS. Allow 60–90 minutes.

```bash
python3 labs/module-07/validate.py labs/module-07/factory.json
python3 labs/module-07/validate.py labs/module-07/factory.json --mermaid
python3 -m unittest discover -s labs/module-07 -p 'test_*.py' -v
```

The fixture models a fictional UAE factory's advisory maintenance assistant. The enterprise requires every declared component to operate at PLANT-A; this strict inventory rule is a scenario assumption, not law. Its air-gap variant prohibits network transports even when both endpoint names refer to the same site. Offline media transfer is an architectural declaration requiring separate real inspection, not an observed safe transfer.

## Model and experiments

Nodes declare physical site, country, trust zone, plane, owner and protection label. Four planes distinguish stored/transformed information (data), execution (compute), administration (management), and policy/identity decisions (control). This classification is course-authored; a real component may implement functions in several planes. Split such functions into separately reviewable nodes.

Edges declare a lifecycle purpose, endpoints, transport, protection label, authorization, owner, test, evidence pointer, build and outcome. Fourteen required lifecycle purposes include ingestion, training, embeddings, speech/OCR, inference, outputs, diagnostics, telemetry, backup, support, activation, updates, failover and retirement. A familiar-looking main inference path does not establish that the other paths are safe.

1. Draw the fixture before running the exporter. Explain which edges cross trust zones and which owner authorizes each crossing.
2. Change the diagnostic edge to a network transport. The air-gap scenario must block even with a local-looking destination.
3. Move the identity or management component to another campus in the same country. Compare `premises` with `country`, retaining the other assumptions. A country policy is an explicit changed scenario, not a workaround for the original requirement.
4. Remove a lifecycle path, create a dangling endpoint, or reuse old-build evidence. Explain why these records become unverified rather than a successful design.
5. Add an off-site duplicate node. A duplicate identifier must not erase its known location conflict. Add an unknown network edge and confirm that classification gaps do not erase network conflicts.
6. Attempt to mark an edge unprotected when its source contains protected information. Explain why a Boolean change does not demonstrate lawful or authorized declassification.

## Interpretation and limitations

Complete favorable declarations return REVIEW_REQUIRED. Known location conflicts, air-gap network paths and declared failed tests return BLOCKED. Missing ownership, classification, routes, current-build evidence, explicit cross-zone authorization or valid references yield UNVERIFIED unless a known conflict also exists. Arbitrary risk-acceptance text cannot override blockers.

The program does not establish reachability, infer transitive data classification or prove that the inventory includes all actual traffic. It does not discover real infrastructure, authenticate evidence, verify model behavior, inspect packets, prove physical isolation, enforce access policies or determine law. It conservatively scopes every declared component under the chosen site/country rule. A real architecture with an external non-sensitive component requires a separately justified scope model; removing protection labels does not relax this lab's inventory policy.

The Mermaid exporter uses restricted identifiers and approved lifecycle labels, excluding user-supplied executable diagram directives. Its output is an editable teaching artifact. The website lesson provides a static plane view alongside the more detailed editable lab graph. Source and automated checks do not establish independent assessment or manual accessibility assurance.

## Deliverable

Submit the original graph, one counterfactual, exported Mermaid source and an architecture decision record using [ADR template](ADR.md). Trace every rejection to a component/path, unchanged requirement and named remediation owner. Keep synthetic records only. The build/test evidence establishes program behavior, not safety of the fictional factory.
