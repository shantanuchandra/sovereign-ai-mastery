#!/usr/bin/env python3
"""Educational Module 02 gate evaluator. Never certifies actual deployments or laws."""
import json
import sys
from pathlib import Path

DIMENSIONS = ("territorial", "operational", "technological", "legal_contractual")
STAGES = {"M0", "M1", "M2", "M3", "M4"}
EVIDENCE = {"none", "asserted", "configured", "tested_unreviewed", "reviewed", "adverse", "expired"}
BOUNDARIES = {"named_locations", "single_premises", "air_gapped"}
NETWORKS = {"disconnected", "isolated", "allowlist", "private_links", "internet"}
BOOLEAN_FIELDS = ("external_network_path", "restricted_offsite_flow",
                  "capacity_feasible", "offline_licence_available")


def evaluate_case(record):
    """Interpret only supplied *fictional scenario* facts; authenticate no real evidence."""
    if not isinstance(record, dict):
        return {"id": "<unknown>", "disposition": "INVALID", "errors": ["Case is not an object"]}
    case_id = record.get("id", "<missing>")
    errors = []
    if not isinstance(case_id, str) or not case_id.strip():
        errors.append("id must be a non-empty string")
    boundary = record.get("boundary")
    if boundary not in BOUNDARIES:
        errors.append("boundary must be a recognized category")
    candidate = record.get("candidate")
    if not isinstance(candidate, dict):
        errors.append("candidate must be an object")
        candidate = {}
    for field in BOOLEAN_FIELDS:
        if type(candidate.get(field)) is not bool:
            errors.append("candidate." + field + " must be boolean")
    if candidate.get("network") not in NETWORKS:
        errors.append("candidate.network must be a recognized option")
    if not isinstance(candidate.get("compute_site"), str) or not candidate.get("compute_site"):
        errors.append("candidate.compute_site must be a non-empty site ID")
    if boundary in ("single_premises", "air_gapped"):
        if not isinstance(record.get("required_site"), str) or not record.get("required_site"):
            errors.append("required_site must be specified for physical-site boundaries")
    if boundary == "named_locations":
        if not isinstance(record.get("allowed_sites"), list) or not record.get("allowed_sites"):
            errors.append("named_locations require a non-empty allowed_sites array")
    dimensions = record.get("dimensions")
    if not isinstance(dimensions, dict):
        dimensions = {}
        errors.append("dimensions must be an object")
    if set(dimensions) != set(DIMENSIONS):
        errors.append("dimensions must contain exactly the four course dimensions")
    for name in DIMENSIONS:
        dim = dimensions.get(name)
        if not isinstance(dim, dict):
            errors.append("dimension " + name + " must be an object")
            continue
        if dim.get("stage") not in STAGES or dim.get("evidence") not in EVIDENCE:
            errors.append("dimension " + name + " has an invalid stage or evidence state")
        if not isinstance(dim.get("owner"), str) or not dim["owner"].strip():
            errors.append("dimension " + name + " must name an evidence owner")
        if not isinstance(dim.get("test_id", ""), str):
            errors.append("dimension " + name + " test_id must be a string")
    if errors:
        return {"id": case_id, "disposition": "INVALID", "errors": errors}

    # These are literal hypothetical case inputs, not observations of actual infrastructure.
    blockers = []
    site = candidate["compute_site"]
    if boundary == "named_locations" and site not in record["allowed_sites"]:
        blockers.append("compute_site_not_in_approved_locations")
    if boundary in ("single_premises", "air_gapped") and site != record["required_site"]:
        blockers.append("compute_outside_named_physical_premises")
    if boundary in ("single_premises", "air_gapped") and candidate["restricted_offsite_flow"]:
        blockers.append("restricted_data_or_derivative_off_premises")
    if boundary == "air_gapped" and candidate["network"] != "disconnected":
        blockers.append("air_gap_has_network_connectivity")
    if boundary == "air_gapped" and candidate["external_network_path"]:
        blockers.append("air_gap_has_external_network_path")
    # A disclosed adverse result is treated as a blocker for this educational scenario.
    for dim in DIMENSIONS:
        if dimensions[dim]["evidence"] == "adverse":
            blockers.append("adverse_evidence_" + dim)

    feasibility_gaps = []
    if not candidate["capacity_feasible"]:
        feasibility_gaps.append("local_or_approved_compute_capacity_unavailable")
    if boundary in ("single_premises", "air_gapped") and not candidate["offline_licence_available"]:
        feasibility_gaps.append("offline_licence_or_runtime_rights_unavailable")

    missing_evidence = []
    reviewed = 0
    profile = {}
    for dim in DIMENSIONS:
        rec = dimensions[dim]
        profile[dim] = rec["stage"]
        # Even 'reviewed' here is merely a fictional input assertion.
        if rec["evidence"] == "reviewed" and rec["test_id"].strip():
            reviewed += 1
        else:
            missing_evidence.append(dim + ": " + rec["evidence"] + " (review/test gap)")
        if rec["stage"] in ("M3", "M4") and rec["evidence"] != "reviewed":
            missing_evidence.append(dim + ": claimed high maturity without reviewed evidence")

    if blockers:
        disposition = "BLOCKED"
    elif feasibility_gaps:
        disposition = "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS"
    elif missing_evidence:
        disposition = "UNVERIFIED"
    else:
        disposition = "REVIEW_REQUIRED"

    return {
        "id": case_id,
        "fictional_simulation": True,
        "boundary": boundary,
        "disposition": disposition,
        "hard_gate_failures": sorted(set(blockers)),
        "feasibility_gaps": feasibility_gaps,
        "maturity_profile": profile,
        "scenario_reported_coverage": f"{reviewed}/4",
        "unverified_claims": missing_evidence,
        "warning": "Case input and evidence states are fictional; no external observation or certification"
    }


def evaluate_portfolio(data):
    if not isinstance(data, dict) or not isinstance(data.get("workloads"), list):
        raise ValueError("Input must be a JSON object containing workloads array")
    if not data["workloads"]:
        raise ValueError("At least one fictional workload is required")
    records = [evaluate_case(w) for w in data["workloads"]]
    ids = [r["id"] for r in records]
    if len(set(ids)) != len(ids):
        raise ValueError("Workload IDs must be unique")
    return {"notice": "SYNTHETIC EXERCISE ONLY, NOT A COMPLIANCE OR SECURITY ASSESSMENT",
            "results": records}


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("cases.json")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        report = evaluate_portfolio(data)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}))
        return 2
    print(json.dumps(report, indent=2))
    # Expected failing *fictional controls* should not make the instructional CLI fail.
    return 2 if any(r["disposition"] == "INVALID" for r in report["results"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
