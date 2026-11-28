#!/usr/bin/env python3
"""Single-process synthetic API-flow prototype. No HTTP or authentication."""
import copy
import json
from pathlib import Path

PRINCIPALS = {"fixture-a": {"tenant": "tenant-a", "role": "owner"},
              "fixture-b": {"tenant": "tenant-b", "role": "owner"},
              "fixture-reader": {"tenant": "tenant-a", "role": "reader"}}
ARTIFACTS = ("prompts", "responses", "ocr", "speech", "embeddings", "weights", "logs", "traces", "metrics", "backups", "support", "updates", "activation", "recovery", "media")
NONLOCAL = {"external", "remote", "cloud", "off-site", "offsite", "domestic-cloud", "public-cloud", "vendor", "managed-cloud"}
CONNECTED = {"connected", "internet", "online", "internet-enabled", "remote", "external"}
TRACE = {"R1": "test_cross_tenant", "R2": "test_idempotent_retry", "R3": "test_stage_skip", "R4": "test_boundary_conflict", "R5": "test_airgap", "R6": "test_missing_evidence"}

def boundary(plan):
    """Known conflicts dominate incomplete evidence. Values are declarations only."""
    conflicts, missing = [], []
    if not isinstance(plan, dict):
        return {"status": "UNVERIFIED", "reasons": ["plan"]}
    paths = plan.get("paths", {})
    if not isinstance(paths, dict):
        paths = {}
        missing.append("paths")
    # Inspect extra supplied routes too; an incomplete inventory cannot hide a conflict.
    for name, value in paths.items():
        if isinstance(value, str) and value in NONLOCAL: conflicts.append(str(name))
        elif value != "on-site": missing.append(str(name))
    for name in ARTIFACTS:
        if name not in paths: missing.append(name)
    if isinstance(plan.get("operator"), str) and plan["operator"] in NONLOCAL: conflicts.append("operator")
    elif plan.get("operator") != "on-site": missing.append("operator")
    if plan.get("airgap") is True:
        if isinstance(plan.get("network"), str) and plan["network"] in CONNECTED: conflicts.append("network")
        elif plan.get("network") != "disconnected": missing.append("network")
        if plan.get("media_review") is False: conflicts.append("media_review")
        elif plan.get("media_review") is not True: missing.append("media_review")
    elif plan.get("airgap") is not False: missing.append("airgap")
    return {"status": "BLOCKED" if conflicts else "UNVERIFIED" if missing else "DECLARED_ONLY", "reasons": sorted(set(conflicts or missing))}

def local_plan():
    return {"paths": dict.fromkeys(ARTIFACTS, "on-site"), "operator": "on-site", "airgap": True, "network": "disconnected", "media_review": True}

class FlowError(ValueError):
    pass

class Platform:
    def __init__(self):
        self.records, self.replays, self.events = {}, {}, []

    def call(self, principal, tenant, operation, payload=None, key=None):
        # A trusted test harness supplies a fixture handle. It is not a credential.
        who = PRINCIPALS.get(principal)
        if who is None or who["tenant"] != tenant:
            raise FlowError("DENIED_SCOPE")
        if operation not in {"create", "configure", "validate", "activate", "read"}:
            raise FlowError("UNKNOWN_OPERATION")
        if operation == "read":
            if tenant not in self.records: raise FlowError("NOT_FOUND")
            return copy.deepcopy(self.records[tenant])
        if who["role"] != "owner": raise FlowError("DENIED_ROLE")
        if not isinstance(payload, dict) or not isinstance(key, str) or not 1 <= len(key) <= 80:
            raise FlowError("INVALID_REQUEST")
        # Reject unrecognized properties rather than accepting a supplied tenant/approval.
        allowed = {"create": {"name"}, "configure": {"plan"}, "validate": {"acceptance"}, "activate": set()}[operation]
        if set(payload) != allowed: raise FlowError("INVALID_PROPERTIES")
        try: canonical = json.dumps(payload, sort_keys=True, allow_nan=False)
        except (TypeError, ValueError): raise FlowError("INVALID_JSON") from None
        replay_id = (tenant, key)
        fingerprint = (operation, canonical)
        if replay_id in self.replays:
            old, result = self.replays[replay_id]
            if old != fingerprint: raise FlowError("IDEMPOTENCY_CONFLICT")
            return copy.deepcopy(result)
        if operation == "create":
            if tenant in self.records: raise FlowError("ALREADY_EXISTS")
            if not isinstance(payload["name"], str) or not 1 <= len(payload["name"]) <= 40: raise FlowError("INVALID_NAME")
            record = {"stage": "REQUESTED", "name": payload["name"], "tenant": tenant}
        else:
            if tenant not in self.records: raise FlowError("NOT_FOUND")
            record = copy.deepcopy(self.records[tenant])
            required = {"configure": "REQUESTED", "validate": "CONFIGURED", "activate": "VALIDATED"}[operation]
            if record["stage"] != required: raise FlowError("INVALID_TRANSITION")
            if operation == "configure":
                decision = boundary(payload["plan"])
                if decision["status"] != "DECLARED_ONLY": raise FlowError(decision["status"] + ":" + ",".join(decision["reasons"]))
                record.update(stage="CONFIGURED", plan=copy.deepcopy(payload["plan"]))
            elif operation == "validate":
                # A known changed boundary takes precedence over incomplete acceptance declarations.
                if boundary(record["plan"])["status"] != "DECLARED_ONLY": raise FlowError("BOUNDARY_CHANGED")
                evidence = payload["acceptance"]
                if not isinstance(evidence, dict) or set(evidence) != set(TRACE) or any(v is not True for v in evidence.values()):
                    raise FlowError("UNVERIFIED_ACCEPTANCE")
                record.update(stage="VALIDATED", acceptance=copy.deepcopy(evidence))
            else:
                if boundary(record["plan"])["status"] != "DECLARED_ONLY": raise FlowError("BOUNDARY_CHANGED")
                if set(record.get("acceptance", {})) != set(TRACE) or any(v is not True for v in record["acceptance"].values()): raise FlowError("UNVERIFIED_ACCEPTANCE")
                record["stage"] = "ACTIVE_FIXTURE"
        self.records[tenant] = record
        result = {"tenant": tenant, "stage": record["stage"], "assurance": "SYNTHETIC_ONLY"}
        self.events.append({"tenant": tenant, "operation": operation, "stage": record["stage"]})
        self.replays[replay_id] = (fingerprint, copy.deepcopy(result))
        return result

def demo():
    platform = Platform()
    steps = []
    for op, data in [("create", {"name": "Synthetic bank"}), ("configure", {"plan": local_plan()}), ("validate", {"acceptance": dict.fromkeys(TRACE, True)}), ("activate", {})]:
        steps.append(platform.call("fixture-a", "tenant-a", op, data, op))
    retry = platform.call("fixture-a", "tenant-a", "activate", {}, "activate")
    bad = local_plan(); bad["paths"]["traces"] = "external"
    return {"steps": steps, "retry": retry, "event_count": len(platform.events), "external_trace": boundary(bad), "traceability": TRACE, "limitations": "In-memory trusted fixture; no HTTP, real authentication, facility assurance, actual acceptance evidence or production launch."}

if __name__ == "__main__":
    result = demo()
    path = Path(__file__).with_name("observed-platform-run.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
