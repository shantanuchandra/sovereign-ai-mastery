# Module 19 lab: evidence before opportunity ranking

Educational deterministic fixture, authored 2026-11-28. All five sectors, roles, interview lines, numeric inputs and declarations are invented. No real buyer research, legal determination, market estimate or physical facility test occurs.

## Run locally

Python 3.11+ standard library; Apple Silicon baseline supported, CPU only. No Docker, GPU, download, network endpoint, paid account or secret. External service spend: zero; existing equipment and learner time excluded. Allow 60–90 minutes to inspect and mutate inputs. Run from repository root:

```bash
python3 labs/module-19/discovery.py
python3 -m unittest discover -s labs/module-19 -p 'test_*.py' -v
```

Compare stdout with `observed-discovery-run.json`, retained from an actual run. To refresh after an intentional fixture change:

```bash
python3 labs/module-19/discovery.py > labs/module-19/observed-discovery-run.json
```

Do not refresh merely to hide a test failure. Explain changed semantics and preserve the evidence state.

## Mechanism and expected result

`fixtures()` builds five independent dictionaries. Required evidence covers pain, buyer, baseline, alternatives and sovereignty. Each record needs declared observed state, source, owner and checked string. The strings are provenance fields, not authenticated documents or validated expiry dates. An author can forge every field. `evaluate()` copies no data into an external store and does not mutate its input.

Known contradiction or boundary conflict dominates incomplete evidence. The required inventory includes prompts, documents, OCR, speech, responses, embeddings, weights, logs, telemetry, backups, support, updates, recovery, media, diagnostics, metrics, registry, keys, activation, failover and administration. Every provided path, including unexpected diagnostics keys, is scanned for a non-onsite destination under premises/airgap rules. Missing protected paths remain unknown; malformed path inventory cannot conceal a known external operator or connected network. Airgap additionally requires disconnected networking, offline-update review and media review. A false review blocks, an absent review stays unknown. For approved-region cases, only a declared region review is evaluated; no specific service region, contract or actual placement is inspected.

Only complete eligible declarations receive a weighted score. Weights: value .35, feasibility .25, adoption .20, economics .20; numeric inputs 0–5, with booleans, NaN, infinity, strings and out-of-range inputs, including arbitrary-size integers, rejected as unknown. Range validation precedes the floating-point finiteness check to avoid overflow converting huge integers. A non-dictionary top-level input returns UNKNOWN with case:invalid. Scores need a reference to one of the required observed evidence records. This does not validate that evidence substantively supports the magnitude: a human must inspect the mapping. Sovereignty necessity never changes desirability.

| Opportunity | Expected state | Score | Next action |
|---|---|---:|---|
| FIN | ELIGIBLE_FOR_DISCOVERY | 3.15 | Validate with real buyer |
| HEALTH | UNKNOWN | null | Collect baseline evidence |
| TEL | ELIGIBLE_FOR_DISCOVERY | 3.15 | Validate managed alternative |
| GOV | BLOCKED | null | Resolve external telemetry |
| IND | BLOCKED | null | Resolve connected airgap proposal |

The stable eligible backlog is FIN, TEL, tied score ordered by identifier. Sector is descriptive metadata; segment derives from operating boundary. None is a sales recommendation.

## Experiments and acceptance

1. Trace one evidence item to the opportunity, score reference and output gap.
2. Remove HEALTH's missing baseline and explain why invented optimism cannot repair it.
3. Change FIN telemetry to external and delete its buyer record. BLOCKED must dominate UNKNOWN and no score may appear.
4. Change IND to disconnected, set every path/operator onsite and pass both offline reviews. It becomes eligible only as a synthetic declaration. It has not become physically verified.
5. Lower FIN economics by one point. Score changes by .20 if all gates still pass. Switching required necessity to preferred leaves the score unchanged.
6. Add an unexpected external diagnostics route to a premises case. It must block.
7. Complete the separate `OPPORTUNITY_ASSESSMENT.md` without treating fixture scores as market evidence.

Tests exercise artifact loops, contradiction loops, malformed inputs, numeric adverse cases, input immutability and equality to the retained actual observation. No customer data, consent recordings, contact details or confidential notes should be added. Production research requires authorized handling, restricted access, retention, real baseline/evaluation and qualified review. No identity enforcement, network isolation, legal compliance, real research authentication, expiry validation, durable workflow or market sizing is implemented. Manual and independent review NOT COMPLETED; Module 04 remains HOLD.
