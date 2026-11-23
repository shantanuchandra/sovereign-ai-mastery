#!/usr/bin/env python3
"""Offline educational Module 05 legal/control traceability validator.

This validator checks synthetic worksheet structure and hard boundary logic.
It DOES NOT establish legal applicability, source authenticity, an air gap,
a production configuration, or regulatory compliance.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

VALID_DECISIONS = {"HOLD", "BLOCKED", "PILOT_SYNTHETIC_ONLY", "APPROVED"}
LEGAL_STATES = {"NEEDS_COUNSEL", "APPROVED", "NOT_APPLICABLE"}
BOUNDARIES = {"NONE", "NAMED_PREMISES", "AIR_GAP"}
HARD_GATE_STATES = {"NOT_APPLICABLE", "NOT_VERIFIED", "VERIFIED", "FAILED"}
LICENCE_MODES = {"NOT_APPLICABLE", "UNKNOWN", "OFFLINE_UNVERIFIED", "OFFLINE_VERIFIED", "ONLINE_REQUIRED"}
REQUIRED_FIELDS = {
    "activity_id", "entity", "activity", "data_class", "legal_candidate",
    "control_id", "control_owner", "test_id", "physical_boundary",
    "named_location", "processing_destinations", "backup_destinations",
    "network_paths", "licence_mode", "hard_gate_state", "decision",
}
REQUIRED_LEGAL_FIELDS = {
    "instrument", "source_url", "source_section", "review_status",
    "counsel_approval_id",
}


class ValidationError(ValueError):
    """A synthetic record violates the teaching contract."""


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_document(document: dict[str, Any]) -> dict[str, Any]:
    """Return bounded counts or raise ValidationError; never return 'compliant'."""
    errors: list[str] = []
    if not isinstance(document, dict) or document.get("schema_version") != "1.0":
        raise ValidationError("Expected a document with schema_version 1.0")
    activities = document.get("activities")
    if not isinstance(activities, list) or not activities:
        raise ValidationError("Expected nonempty activities array")

    ids: set[str] = set()
    counts: Counter[str] = Counter()
    for number, row in enumerate(activities, 1):
        tag = f"activities[{number}]"
        if not isinstance(row, dict):
            errors.append(f"{tag}: expected object")
            continue
        missing = sorted(REQUIRED_FIELDS - row.keys())
        if missing:
            errors.append(f"{tag}: missing fields: {', '.join(missing)}")
            continue

        ident = row.get("activity_id")
        if not _nonempty(ident):
            errors.append(f"{tag}: blank activity_id")
        elif ident in ids:
            errors.append(f"{tag}: duplicate activity_id {ident}")
        else:
            ids.add(ident)
            tag = ident

        for key in ("entity", "activity", "data_class", "control_id",
                    "control_owner", "test_id"):
            if not _nonempty(row.get(key)):
                errors.append(f"{tag}: {key} must be nonempty")

        legal = row.get("legal_candidate")
        if not isinstance(legal, dict):
            errors.append(f"{tag}: legal_candidate must be object")
            legal = {}
        for key in REQUIRED_LEGAL_FIELDS - {"counsel_approval_id"}:
            if not _nonempty(legal.get(key)):
                errors.append(f"{tag}: legal_candidate.{key} is missing")
        url = legal.get("source_url")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"{tag}: legal_candidate.source_url must be https URL")
        state = legal.get("review_status")
        approval_id = legal.get("counsel_approval_id")
        if state not in LEGAL_STATES:
            errors.append(f"{tag}: unrecognized legal review status")
        if state == "APPROVED" and not _nonempty(approval_id):
            errors.append(f"{tag}: APPROVED legal review lacks counsel_approval_id")
        if state == "NEEDS_COUNSEL" and approval_id is not None:
            errors.append(f"{tag}: pending counsel entry must not carry approval")
        if state == "NOT_APPLICABLE" and "fictional" not in (
                str(legal.get("instrument", "")) + " " +
                str(legal.get("source_section", ""))).lower():
            errors.append(f"{tag}: NOT_APPLICABLE requires explicit fictional-only rationale")

        decision = row.get("decision")
        if decision not in VALID_DECISIONS:
            errors.append(f"{tag}: unknown decision {decision}")
        else:
            counts[decision] += 1
        if decision == "PILOT_SYNTHETIC_ONLY" and row.get("data_class") != "synthetic_only":
            errors.append(f"{tag}: synthetic pilot cannot include restricted or real data")
        if decision == "APPROVED" and state != "APPROVED":
            errors.append(f"{tag}: approval forbidden before counsel review")
        licence_mode = row.get("licence_mode")
        if licence_mode not in LICENCE_MODES:
            errors.append(f"{tag}: unrecognized licence_mode; do not infer offline capability")
        boundary = row.get("physical_boundary")
        gate = row.get("hard_gate_state")
        if boundary not in BOUNDARIES or gate not in HARD_GATE_STATES:
            errors.append(f"{tag}: invalid boundary or hard_gate_state")
            continue

        destinations: dict[str, list[str]] = {}
        for key in ("processing_destinations", "backup_destinations", "network_paths"):
            value = row.get(key)
            if not isinstance(value, list) or any(not _nonempty(item) for item in value):
                errors.append(f"{tag}: {key} must be a list of nonblank strings")
                destinations[key] = []
            else:
                destinations[key] = value

        if boundary in {"NAMED_PREMISES", "AIR_GAP"}:
            place = row.get("named_location")
            if not _nonempty(place):
                errors.append(f"{tag}: physical boundary needs named_location")
            for key in ("processing_destinations", "backup_destinations"):
                if any(destination != place for destination in destinations[key]):
                    errors.append(f"{tag}: {key} violates named physical location")
                if not destinations[key]:
                    errors.append(f"{tag}: {key} needs a named physical destination")
            # The worksheet does not encode independently verified network endpoints.
            # Under a named-premises requirement, a declared network route
            # is unproven to remain on premises. Fail closed pending evidence.
            # This does not imply that all verified on-site LAN use is forbidden.
            if boundary == "NAMED_PREMISES" and destinations["network_paths"]:
                errors.append(f"{tag}: named premises network paths need verified on-site routing; HOLD until separately evidenced")
            if licence_mode == "ONLINE_REQUIRED":
                errors.append(f"{tag}: physical hard gate forbids required online licence")
            if decision in {"APPROVED", "PILOT_SYNTHETIC_ONLY"} and licence_mode != "OFFLINE_VERIFIED":
                errors.append(f"{tag}: physical release requires separately evidenced offline licence")
            if decision in {"APPROVED", "PILOT_SYNTHETIC_ONLY"} and gate != "VERIFIED":
                errors.append(f"{tag}: no release without separately verified physical evidence")

        if boundary == "AIR_GAP" and destinations["network_paths"]:
            errors.append(f"{tag}: physical air gap prohibits ALL network paths")
        if gate == "FAILED" and decision != "BLOCKED":
            errors.append(f"{tag}: FAILED hard gate requires BLOCKED")
        if boundary == "NONE" and gate != "NOT_APPLICABLE":
            errors.append(f"{tag}: nonphysical workflow must use NOT_APPLICABLE gate")
        if decision == "APPROVED" and gate not in {"VERIFIED", "NOT_APPLICABLE"}:
            errors.append(f"{tag}: hard gate not verified")

    if errors:
        raise ValidationError("; ".join(errors))
    return {
        "status": "SYNTHETIC_SCHEMA_VALIDATED_ONLY",
        "activities_checked": len(activities),
        "decision_counts": dict(sorted(counts.items())),
        "legal_review_needed": sum(
            a["legal_candidate"]["review_status"] == "NEEDS_COUNSEL"
            for a in activities
        ),
        "notice": "No legal, physical, vendor or accessibility assurance inferred.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Local JSON activity map")
    args = parser.parse_args()
    try:
        payload = json.loads(args.path.read_text(encoding="utf-8"))
        result = validate_document(payload)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "REJECTED", "reason": str(exc)}, indent=2))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
