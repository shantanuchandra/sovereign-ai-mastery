"""Synthetic Module 04 source-to-deployment decision evaluator.

A public evidence source is NOT proof of a deployment, law, offline licence,
physical air gap or actual customer runtime. All workload observations fictional.
"""
import json
import sys
from pathlib import Path

BOUNDARIES = {"approved_locations", "single_premises", "air_gapped"}
NETWORKS = {"disconnected", "isolated", "private_links", "allowlist", "internet"}
EVIDENCE = {"missing", "asserted", "configured", "tested_unreviewed", "reviewed", "adverse", "expired"}
FIELDS = ("external_management_path", "restricted_offsite_derivative",
          "offline_licence_available", "capacity_feasible")


def evaluate_case(case, source_ids):
    errors = []
    if not isinstance(case, dict):
        return {"id": "<invalid>", "disposition": "INVALID", "errors": ["workload is not an object"]}
    ident = case.get("id", "<missing>")
    for field in ("id", "owner", "authority"):
        if not isinstance(case.get(field), str) or not case[field].strip():
            errors.append("missing " + field)
    boundary = case.get("boundary")
    if boundary not in BOUNDARIES:
        errors.append("unrecognized boundary")
    candidate = case.get("candidate")
    if not isinstance(candidate, dict):
        errors.append("candidate missing")
        candidate = {}
    if candidate.get("network_mode") not in NETWORKS:
        errors.append("unrecognized network mode")
    if not isinstance(candidate.get("compute_site"), str) or not candidate.get("compute_site"):
        errors.append("compute site required")
    for field in FIELDS:
        if type(candidate.get(field)) is not bool:
            errors.append("candidate " + field + " must be a boolean")
    if boundary in {"single_premises", "air_gapped"}:
        if not isinstance(case.get("required_site"), str) or not case["required_site"]:
            errors.append("a named physical premises is mandatory")
    if boundary == "approved_locations":
        sites = case.get("approved_sites")
        if not isinstance(sites, list) or not sites or any(not isinstance(x, str) or not x for x in sites):
            errors.append("approved locations must be a nonempty list of names")
    claims = case.get("claims")
    if not isinstance(claims, list) or not claims:
        errors.append("at least one traceability claim is needed")
        claims = []
    claim_ids = []
    for claim in claims:
        if not isinstance(claim, dict):
            errors.append("claim is not an object")
            continue
        for field in ("id", "source_id", "owner", "control", "test"):
            if not isinstance(claim.get(field), str) or not claim[field].strip():
                errors.append("claim missing " + field)
        if claim.get("source_id") not in source_ids:
            errors.append("claim source missing from source ledger")
        if claim.get("evidence") not in EVIDENCE:
            errors.append("invalid evidence state")
        if not isinstance(claim.get("test_id"), str):
            errors.append("test_id must be a string")
        claim_ids.append(claim.get("id"))
    if len(set(claim_ids)) != len(claim_ids):
        errors.append("duplicate claim ID")
    if errors:
        return {"id": ident, "disposition": "INVALID", "errors": errors}

    gates = []
    site = candidate["compute_site"]
    if boundary == "approved_locations" and site not in case["approved_sites"]:
        gates.append("compute_outside_approved_location")
    if boundary in {"single_premises", "air_gapped"} and site != case["required_site"]:
        gates.append("compute_outside_named_premises")
    if boundary in {"single_premises", "air_gapped"} and candidate["restricted_offsite_derivative"]:
        gates.append("restricted_derivative_attempt_outside_premises")
    if boundary == "air_gapped" and candidate["network_mode"] != "disconnected":
        gates.append("air_gap_has_network_connectivity")
    if boundary == "air_gapped" and candidate["external_management_path"]:
        gates.append("air_gap_has_external_management_path")
    for claim in claims:
        if claim["evidence"] == "adverse":
            gates.append("adverse_test_" + claim["id"])

    infeasible = []
    if not candidate["capacity_feasible"]:
        infeasible.append("permitted_runtime_capacity_unavailable")
    if boundary in {"single_premises", "air_gapped"} and not candidate["offline_licence_available"]:
        infeasible.append("offline_model_licence_unavailable")

    gaps = []
    reviewed = 0
    for claim in claims:
        # Source records only justify claim provenance. A hypothetical reviewed
        # status with test_id is never real verification or compliance approval.
        if claim["evidence"] == "reviewed" and claim["test_id"].strip():
            reviewed += 1
        else:
            gaps.append(claim["id"] + ": evidence " + claim["evidence"] +
                        " requires a reviewer and a versioned observed test")
    if gates:
        decision = "BLOCKED"
    elif infeasible:
        decision = "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS"
    elif gaps:
        decision = "UNVERIFIED"
    else:
        decision = "REVIEW_REQUIRED"
    return {"id": ident, "boundary": boundary,
            "disposition": decision, "hard_failures": sorted(set(gates)),
            "infeasibility": infeasible, "unverified_claims": gaps,
            "scenario_reported_coverage": str(reviewed) + "/" + str(len(claims)),
            "fictional_simulation": True,
            "notice": "Public policy and model announcements never certify a deployment."}


def evaluate_portfolio(data):
    if not isinstance(data, dict) or not isinstance(data.get("source_claims"), list) or not isinstance(data.get("workloads"), list):
        raise ValueError("Expected source_claims and workloads arrays")
    sources = data["source_claims"]
    if not sources or not data["workloads"]:
        raise ValueError("Source and workload arrays must not be empty")
    source_ids = set()
    for source in sources:
        if not isinstance(source, dict):
            raise ValueError("Source must be an object")
        for field in ("id", "jurisdiction", "issuer", "source_url", "instrument",
                      "claim", "reviewed_on", "supports", "does_not_prove"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                raise ValueError("Source missing " + field)
        if not source["source_url"].startswith("https://"):
            raise ValueError("Source URL must use HTTPS")
        if source["id"] in source_ids:
            raise ValueError("Duplicate source ID")
        source_ids.add(source["id"])
    decisions = [evaluate_case(x, source_ids) for x in data["workloads"]]
    ids = [x["id"] for x in decisions]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate workload ID")
    return {"notice": "FICTIONAL EDUCATIONAL SIMULATION. NO LEGAL, VENDOR OR PHYSICAL ASSURANCE.",
            "source_count": len(sources), "results": decisions}


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("cases.json")
    try:
        report = evaluate_portfolio(json.loads(path.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}))
        return 2
    print(json.dumps(report, indent=2))
    return 2 if any(x["disposition"] == "INVALID" for x in report["results"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
