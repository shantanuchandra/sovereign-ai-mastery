#!/usr/bin/env python3
"""Deterministic synthetic discovery, not buyer verification or compliance scoring."""
import copy
import json
import math
from pathlib import Path

CRITERIA = {"value": .35, "feasibility": .25, "adoption": .20, "economics": .20}
ARTIFACTS = ("prompts", "documents", "ocr", "speech", "responses", "embeddings", "weights", "logs", "telemetry", "backups", "support", "updates", "recovery", "media", "diagnostics", "metrics", "registry", "keys", "activation", "failover", "admin")
REQUIRED = ("pain", "buyer", "baseline", "alternatives", "sovereignty")


def evaluate(case):
    """Known contradictions dominate unknowns; unknowns never become numeric zero."""
    conflicts, unknown = [], []
    if not isinstance(case, dict):
        case = {}
        unknown.append("case:invalid")
    evidence = case.get("evidence")
    if not isinstance(evidence, dict):
        evidence = {}
        unknown.append("evidence:invalid")
    for key in REQUIRED:
        item = evidence.get(key)
        if not isinstance(item, dict):
            unknown.append(f"evidence:{key}")
            continue
        if item.get("state") == "contradicted":
            conflicts.append(f"contradicted:{key}")
        elif item.get("state") != "observed" or not all(isinstance(item.get(k), str) and item[k].strip() for k in ("source", "owner", "checked")):
            unknown.append(f"evidence:{key}")
    boundary, proposal = case.get("boundary"), case.get("proposal")
    if boundary not in ("premises", "approved-region", "airgap"):
        unknown.append("boundary")
    if not isinstance(proposal, dict):
        proposal = {}
        unknown.append("proposal")
    paths = proposal.get("paths")
    if not isinstance(paths, dict):
        paths = {}
        unknown.append("paths")
    if boundary in ("premises", "airgap"):
        # Scan every provided route, including extra routes, before completeness checks.
        for artifact, location in paths.items():
            if isinstance(location, str) and location not in ("onsite", "unknown", ""):
                conflicts.append(f"external:{artifact}")
            elif not isinstance(location, str) or location in ("unknown", ""):
                unknown.append(f"path:{artifact}:invalid-or-unknown")
        for artifact in ARTIFACTS:
            if paths.get(artifact) != "onsite":
                unknown.append(f"path:{artifact}")
        if proposal.get("operator") not in (None, "unknown", "onsite"):
            conflicts.append("external:operator")
        elif proposal.get("operator") != "onsite":
            unknown.append("operator")
    if boundary == "airgap":
        if proposal.get("network") not in (None, "unknown", "disconnected"):
            conflicts.append("airgap:network")
        elif proposal.get("network") != "disconnected":
            unknown.append("network")
        for key in ("offline_update_review", "media_review"):
            if proposal.get(key) is False:
                conflicts.append(f"airgap:{key}")
            elif proposal.get(key) is not True:
                unknown.append(key)
    elif boundary == "approved-region":
        if proposal.get("region_review") is False:
            conflicts.append("region:rejected")
        elif proposal.get("region_review") is not True:
            unknown.append("region_review")
    scores = case.get("scores")
    if not isinstance(scores, dict):
        scores = {}
    values = {}
    for name in CRITERIA:
        item = scores.get(name)
        # Numeric input requires an actual observed evidence reference, not a confidence multiplier.
        if not isinstance(item, dict) or item.get("evidence") not in REQUIRED or item.get("evidence") not in evidence:
            unknown.append(f"score:{name}")
            continue
        ref = evidence[item["evidence"]]
        x = item.get("value")
        if not isinstance(ref, dict) or ref.get("state") != "observed":
            unknown.append(f"score:{name}:unobserved")
        elif type(x) not in (int, float) or not 0 <= x <= 5 or not math.isfinite(x):
            unknown.append(f"score:{name}:invalid")
        else:
            values[name] = x
    necessity = case.get("necessity")
    if necessity not in ("required", "preferred", "not-established"):
        unknown.append("necessity")
        necessity = "not-established"
    if necessity == "required" and (not isinstance(evidence.get("sovereignty"), dict) or evidence["sovereignty"].get("state") != "observed"):
        unknown.append("necessity:unsupported")
    state = "BLOCKED" if conflicts else "UNKNOWN" if unknown else "ELIGIBLE_FOR_DISCOVERY"
    # No rankings for blocked/unknown opportunities, even when supplied scores look favorable.
    score = round(sum(values[k] * w for k, w in CRITERIA.items()), 2) if state == "ELIGIBLE_FOR_DISCOVERY" else None
    segment = {"premises": "physical-site", "airgap": "disconnected-site", "approved-region": "approved-managed"}.get(boundary if isinstance(boundary, str) else "", "unclassified")
    return {"id": case.get("id", "unknown"), "state": state, "desirability": score, "sovereignty_necessity": necessity,
            "segment": segment, "conflicts": sorted(set(conflicts)), "unknowns": sorted(set(unknown)),
            "assurance": "SYNTHETIC_DECLARATIONS_ONLY", "next_action": "resolve conflict" if conflicts else "collect evidence" if unknown else "validate with real buyer"}


def fixtures():
    base = {"synthetic": True, "boundary": "premises", "necessity": "required",
            "evidence": {k: {"state": "observed", "source": f"synthetic-interview:{k}", "owner": "fictional buyer", "checked": "2026-11-28"} for k in REQUIRED},
            "proposal": {"paths": {k: "onsite" for k in ARTIFACTS}, "operator": "onsite", "network": "restricted"},
            "scores": {"value": {"value": 4, "evidence": "pain"}, "feasibility": {"value": 3, "evidence": "baseline"}, "adoption": {"value": 3, "evidence": "buyer"}, "economics": {"value": 2, "evidence": "alternatives"}}}
    result = []
    for ident, sector, job in (("FIN", "finance", "policy lookup"), ("HEALTH", "healthcare", "staff procedure retrieval"), ("TEL", "telecom", "ticket summarization"), ("GOV", "government", "case file retrieval"), ("IND", "industry", "maintenance instructions")):
        row = copy.deepcopy(base)
        row.update(id=ident, sector=sector, job=job)
        result.append(row)
    result[1]["evidence"]["baseline"]["state"] = "unknown"
    result[2].update(boundary="approved-region", necessity="preferred")
    result[2]["proposal"].update(region_review=True)
    result[3]["proposal"]["paths"]["telemetry"] = "external"
    result[4].update(boundary="airgap")
    result[4]["proposal"].update(network="internet", offline_update_review=True, media_review=True)
    return result


def run():
    results = [evaluate(c) for c in fixtures()]
    ranked = sorted((r for r in results if r["desirability"] is not None), key=lambda r: (-r["desirability"], r["id"]))
    return {"scope": "five invented interviews, no market estimate", "results": results, "eligible_backlog": [r["id"] for r in ranked]}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2, allow_nan=False))
