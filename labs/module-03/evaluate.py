"""Educational, deterministic Module 03 requirement-to-control gate evaluator.

It only classifies the fictional facts supplied in JSON. It cannot observe a
live system, prove a real air gap, issue a legal conclusion or certify a vendor.
"""
import json
import sys
from pathlib import Path

BOUNDARIES = {"approved_named_sites", "single_premises", "air_gapped"}
NETWORKS = {"disconnected", "isolated", "private_links", "allowlist", "internet"}
EVIDENCE = {"missing", "asserted", "configured", "tested_unreviewed", "reviewed", "adverse", "expired"}
BOOLEANS = ("external_management_path", "offsite_derivative_attempt",
            "offline_licence_available", "capacity_feasible")


def evaluate_case(row):
    if not isinstance(row, dict):
        return {"id": "<invalid>", "disposition": "INVALID", "errors": ["not a case object"]}
    ident = row.get("id", "<missing>")
    candidate = row.get("candidate")
    claims = row.get("claims")
    errors = []
    if not isinstance(ident, str) or not ident.strip():
        errors.append("id must be nonempty")
    if row.get("boundary") not in BOUNDARIES:
        errors.append("invalid boundary")
    if not isinstance(row.get("business_owner"), str) or not row["business_owner"].strip():
        errors.append("business owner is required")
    if not isinstance(row.get("authority"), str) or not row["authority"].strip():
        errors.append("requirement issuer is required")
    if not isinstance(candidate, dict):
        candidate = {}
        errors.append("candidate must be an object")
    for field in BOOLEANS:
        if type(candidate.get(field)) is not bool:
            errors.append(field + " must be boolean")
    if candidate.get("network_mode") not in NETWORKS:
        errors.append("invalid network mode")
    if not isinstance(candidate.get("compute_site"), str) or not candidate.get("compute_site"):
        errors.append("compute site is required")
    if row.get("boundary") in {"single_premises", "air_gapped"}:
        if not isinstance(row.get("required_site"), str) or not row["required_site"]:
            errors.append("named premises are required")
    if row.get("boundary") == "approved_named_sites":
        if not isinstance(row.get("approved_sites"), list) or not row["approved_sites"] or not all(isinstance(x, str) and x for x in row["approved_sites"]):
            errors.append("approved sites are required")
    if not isinstance(claims, list) or not claims:
        claims = []
        errors.append("at least one traceability claim is required")
    ids = []
    for claim in claims:
        if not isinstance(claim, dict):
            errors.append("claim must be an object")
            continue
        for field in ("id", "owner", "control", "test"):
            if not isinstance(claim.get(field), str) or not claim[field].strip():
                errors.append("claim must contain " + field)
        if claim.get("evidence") not in EVIDENCE:
            errors.append("invalid evidence status")
        if not isinstance(claim.get("test_id", ""), str):
            errors.append("test_id must be a string")
        ids.append(claim.get("id"))
    if len(set(ids)) != len(ids):
        errors.append("duplicate claim ID")
    if errors:
        return {"id": ident, "disposition": "INVALID", "errors": errors}

    boundary = row["boundary"]
    failures = []
    if boundary == "approved_named_sites" and candidate["compute_site"] not in row["approved_sites"]:
        failures.append("compute_outside_approved_sites")
    if boundary in {"single_premises", "air_gapped"} and candidate["compute_site"] != row["required_site"]:
        failures.append("compute_outside_named_premises")
    if boundary in {"single_premises", "air_gapped"} and candidate["offsite_derivative_attempt"]:
        failures.append("offsite_restricted_derivative_attempt")
    if boundary == "air_gapped":
        if candidate["network_mode"] != "disconnected":
            failures.append("network_connectivity_in_air_gap")
        if candidate["external_management_path"]:
            failures.append("external_management_path_in_air_gap")
    failures.extend("adverse_" + claim["id"] for claim in claims if claim["evidence"] == "adverse")

    infeasibility = []
    if not candidate["capacity_feasible"]:
        infeasibility.append("required_capacity_unavailable")
    if boundary in {"single_premises", "air_gapped"} and not candidate["offline_licence_available"]:
        infeasibility.append("offline_model_rights_unavailable")

    missing = []
    reported_reviewed = 0
    for claim in claims:
        if claim["evidence"] == "reviewed" and claim.get("test_id", "").strip():
            reported_reviewed += 1
        else:
            missing.append(claim["id"] + ": " + claim["evidence"] + " (missing accepted test)")
    if failures:
        decision = "BLOCKED"
    elif infeasibility:
        decision = "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS"
    elif missing:
        decision = "UNVERIFIED"
    else:
        decision = "REVIEW_REQUIRED"
    return {"id": ident, "fictional_only": True, "boundary": boundary,
            "disposition": decision, "hard_failures": sorted(set(failures)),
            "feasibility_gaps": infeasibility,
            "scenario_reported_coverage": f"{reported_reviewed}/{len(claims)}",
            "unreviewed_claims": missing,
            "warning": "Synthetic inputs and declared evidence are NOT real-world verification"}


def evaluate_portfolio(data):
    if not isinstance(data, dict) or not isinstance(data.get("workloads"), list) or not data["workloads"]:
        raise ValueError("workloads must be a non-empty list")
    records = [evaluate_case(row) for row in data["workloads"]]
    ids = [r["id"] for r in records]
    if len(set(ids)) != len(ids):
        raise ValueError("workload IDs must be unique")
    return {"notice": "SYNTHETIC LEARNING LAB; NOT CERTIFICATION", "results": records}


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("cases.json")
    try:
        report = evaluate_portfolio(json.loads(path.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}))
        return 2
    print(json.dumps(report, indent=2))
    return 2 if any(item["disposition"] == "INVALID" for item in report["results"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
