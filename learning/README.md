# Architecture & Learning Studio (v1.0)

> A browser-only **adaptive learning exercise** for the Sovereign AI Mastery field guide. It is not an AI model, a compliance tool, legal advice, procurement clearance or a sovereignty certification.

## What it does

1. **Nine questions** define a bounded AI workload, its data class, processing geography, operational authority, portability, compute capacity, available evidence, jurisdiction and delivery stage.
2. A **deterministic decision engine** returns one of five provisional architecture patterns. Its reasoning trace connects every input to an implementation consequence.
3. A generated **layered architecture**, four-dimension control table, evidence status, test plan and hard gates explain how to assess the proposal.
4. **Change one constraint** compares the original and proposed architecture without overwriting inputs until the learner explicitly applies the change.
5. **Four adaptive case questions** change with the configuration. Each answer has a rationale. Wrong answers receive a probable reasoning error, corrective test and course reading.
6. **Export Markdown and JSON** records assumptions, the architecture, decisions, missed concepts, an optional reflection and unresolved evidence. The user may review and commit these files to the public GitHub repository.

## Rules and their limits

The engine is **rule-based**, not LLM-backed. It does not inspect actual deployments, execute cloud APIs, estimate production costs, evaluate model quality or verify laws. Inputs and quiz state stay in local browser storage; no questionnaire data is posted automatically. Export is initiated by the learner.

The course ontology in [`taxonomy/ontology.yaml`](../taxonomy/ontology.yaml) defines relevant classes and relationships. The Studio's dimensions and evidence states are a course-authored product design synthesis and **not an official framework**. The linked NIST AI RMF 1.0 is background on AI risk governance, not an endorsement of the Studio's sovereignty typology.

## Decision patterns

| Condition (priority order) | Provisional pattern | Required caution |
|---|---|---|
| Enterprise-only administration; no enterprise-operated production compute | Gated local prototype | Blocks production approval until the conflict is addressed |
| Enterprise-only administration; private compute available | Enterprise-operated private serving | Operational dependency and test evidence remain unverified |
| Country-only location, or approved managed operations, or sensitive data | Controlled managed serving | Exact processing, support, key custody and telemetry boundaries need verification |
| Otherwise, exit rehearsal mandatory or approved zone | Portable hybrid gateway | Portability needs a measured test, not just API compatibility |
| Otherwise | Limited managed API pilot | Vendor dependence and routing must be documented |

The pattern is a **starting hypothesis**, never a recommendation to purchase a named vendor product.

## Run locally

```sh
python3 -m http.server 8000
# Open http://localhost:8000/learning/
```

Requires no packages for the browser experience and no API key. The default desktop layout uses the field-guide palette with responsive mobile behavior.

## Test

```sh
node --test learning/tests/engine.test.mjs
node --check learning/studio-ui.mjs
node --check learning/studio-engine.mjs
python3 scripts/build_site.py
```

The tests cover normalizing inputs, incompatible requirements, false compliance claims, evidence states, adaptive misconceptions, architecture comparisons, and journal export. They do not replace a cross-browser visual test or an independent audit of legal applicability.

## Security and publication

- Do not input customer information, confidential architecture, personal identifiers, credentials or real access-control records.
- Local storage contains only chosen values and brief learning reflections, and can be cleared via browser settings. This is not a secure vault.
- The repository is public. Exported Markdown and JSON should be reviewed and redacted before committing.
- There is no hidden use of cloud inference or an external LLM. The tutor is a transparent scenario engine, not a conversational model.

## Product extension path

After actual learning feedback and module coverage improve, consider an opt-in server-based tutor backed by a constrained knowledge base, source retrieval, and per-answer citations. A real model should disclose its version, retrieval scope, uncertainties, operational costs, and data-processing boundaries. Do not add a secret model key to client-side code.