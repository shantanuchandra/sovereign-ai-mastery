#!/usr/bin/env python3
"""Synthetic control-plane exercise. No LLM, network, OAuth or enterprise connector."""
from __future__ import annotations
import copy
import hashlib
import hmac
import json
import secrets
import threading
from dataclasses import dataclass, replace

ARTIFACTS = ("prompts", "outputs", "weights", "embeddings", "ocr", "speech", "diagnostics",
             "logs", "telemetry", "backups", "support", "activation", "updates", "recovery")
POLICY = "bank-a-v1"


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def boundary_state(declaration):
    """Validate a *declared* physical-site-only, offline policy; not actual facility evidence."""
    if not isinstance(declaration, dict):
        return "UNVERIFIED"
    conflicts = declaration.get("site") not in (None, "BANK-A") or declaration.get("network") not in (None, "offline") or declaration.get("operator") not in (None, "onsite")
    paths = declaration.get("artifacts")
    if isinstance(paths, dict):
        conflicts = conflicts or any(value not in (None, "BANK-A") for value in paths.values())
    if conflicts:
        return "BLOCKED"
    if declaration.get("site") != "BANK-A" or declaration.get("network") != "offline" or declaration.get("operator") != "onsite":
        return "UNVERIFIED"
    if not isinstance(paths, dict) or set(paths) != set(ARTIFACTS) or any(paths[a] != "BANK-A" for a in ARTIFACTS):
        return "UNVERIFIED"
    if declaration.get("offline_media_reviewed") is not True:
        return "UNVERIFIED"
    return "DECLARED_ONLY"


def fixture_boundary():
    return {"site": "BANK-A", "network": "offline", "operator": "onsite",
            "artifacts": {name: "BANK-A" for name in ARTIFACTS}, "offline_media_reviewed": True}


@dataclass(frozen=True)
class Action:
    request_id: str
    tenant: str
    user: str
    agent: str
    tool: str
    resource: str
    version: int
    params: dict
    policy: str = POLICY


@dataclass(frozen=True)
class Grant:
    grant_id: str
    action_digest: str
    approver: str
    expires: int
    signature: str


class Denied(Exception):
    pass


class GatedAgent:
    """In-memory single-process reference; fixtures stand in for trusted infrastructure."""
    def __init__(self, boundary=None):
        self.boundary = copy.deepcopy(fixture_boundary() if boundary is None else boundary)
        self.policy = POLICY
        self.users = {"alice": {"tenant": "A", "role": "operator"},
                      "bea": {"tenant": "A", "role": "approver"},
                      "bob": {"tenant": "B", "role": "operator"},
                      "ben": {"tenant": "B", "role": "approver"}}
        self.agents = {"agent-A": {"tenant": "A", "users": {"alice"}},
                       "agent-B": {"tenant": "B", "users": {"bob"}}}
        # Opaque fixture handles, not real bearer tokens or secrets. Only the trusted test setup issues them.
        self.sessions = {"session-A": "alice", "session-B": "bob", "review-A": "bea", "review-B": "ben"}
        self.credentials = {"credential-A": {"tenant": "A", "agent": "agent-A", "aud": "ticket-service", "scopes": {"ticket.read", "ticket.close"}, "expires": 2000},
                            "credential-B": {"tenant": "B", "agent": "agent-B", "aud": "ticket-service", "scopes": {"ticket.read", "ticket.close"}, "expires": 2000}}
        self.tickets = {"A-1": {"tenant": "A", "version": 1, "status": "open", "body": "Synthetic BANK-A maintenance ticket"},
                        "B-1": {"tenant": "B", "version": 1, "status": "open", "body": "Synthetic tenant-B ticket"}}
        self._key = secrets.token_bytes(32)
        self._grants = {}
        self._spent = set()
        self._requests = set()
        self.audit = []
        self.audit_available = True
        self.tool_calls = 0
        self._lock = threading.Lock()

    def _event(self, action, status, reason):
        if not self.audit_available:
            raise Denied("audit_unavailable")
        # Fixed reason codes and digest only; never serialize tokens, params, prompt, body or approval signature.
        self.audit.append({"request_digest": digest(action.request_id), "action_digest": self._audit_digest(action),
                           "tenant": action.tenant if action.tenant in ("A", "B") else "unknown",
                           "status": status, "reason": reason})

    @staticmethod
    def _audit_digest(action):
        try:
            return digest(action.__dict__)
        except (ValueError, TypeError):
            return "unserializable-rejected-input"

    def _check(self, action, session, credential, now):
        if type(now) is not int or now < 0:
            raise Denied("invalid_clock")
        if not isinstance(action, Action) or type(action.version) is not int or action.version < 1:
            raise Denied("invalid_schema")
        if not all(isinstance(v, str) for v in (action.request_id, action.tenant, action.user, action.agent, action.tool, action.resource, action.policy, session, credential)):
            raise Denied("invalid_schema")
        if not isinstance(action.request_id, str) or not 1 <= len(action.request_id) <= 64:
            raise Denied("invalid_request_id")
        if action.tenant not in ("A", "B") or action.tool not in ("ticket.read", "ticket.close"):
            raise Denied("tool_or_tenant_denied")
        if not isinstance(action.params, dict) or action.params != ({} if action.tool == "ticket.read" else {"status": "closed"}):
            raise Denied("invalid_parameters")
        state = boundary_state(self.boundary)
        if state != "DECLARED_ONLY":
            raise Denied("boundary_" + state.lower())
        if action.policy != self.policy:
            raise Denied("stale_policy")
        user = self.users.get(self.sessions.get(session))
        if not user or self.sessions[session] != action.user or user["tenant"] != action.tenant or user["role"] != "operator":
            raise Denied("user_denied")
        agent = self.agents.get(action.agent)
        if not agent or agent["tenant"] != action.tenant or action.user not in agent["users"]:
            raise Denied("agent_denied")
        cred = self.credentials.get(credential)
        if not cred or cred["tenant"] != action.tenant or cred["agent"] != action.agent or cred["aud"] != "ticket-service" or action.tool not in cred["scopes"] or type(cred["expires"]) is not int or now >= cred["expires"]:
            raise Denied("credential_denied")
        ticket = self.tickets.get(action.resource)
        if not ticket or ticket["tenant"] != action.tenant:
            raise Denied("resource_denied")
        if ticket["version"] != action.version:
            raise Denied("stale_resource")
        if (action.tenant, action.request_id) in self._requests:
            raise Denied("request_replay")

    def _sign(self, grant_id, action_digest, approver, expires):
        payload = canonical([grant_id, action_digest, approver, expires]).encode()
        return hmac.new(self._key, payload, hashlib.sha256).hexdigest()

    def approve(self, action, session, credential, reviewer_session, now, ttl=60):
        """Trusted reviewer UI must show exact action and obtain real consent; not modeled here."""
        action = copy.deepcopy(action)
        with self._lock:
            self._check(action, session, credential, now)
            if not isinstance(reviewer_session, str):
                raise Denied("approver_denied")
            reviewer_id = self.sessions.get(reviewer_session)
            reviewer = self.users.get(reviewer_id)
            if not reviewer or reviewer["role"] != "approver" or reviewer["tenant"] != action.tenant or reviewer_id == action.user:
                raise Denied("approver_denied")
            if type(ttl) is not int or not 1 <= ttl <= 300 or action.tool != "ticket.close":
                raise Denied("approval_scope_denied")
            grant_id, action_digest, expires = secrets.token_hex(16), digest(action.__dict__), now + ttl
            grant = Grant(grant_id, action_digest, reviewer_id, expires, self._sign(grant_id, action_digest, reviewer_id, expires))
            self._event(action, "APPROVED", "bound_exact_action")
            self._grants[grant_id] = grant
            return grant

    def invoke(self, action, session, credential, now, grant=None):
        # Freeze mutable parameter input to prevent caller-side changes between validation and execution.
        action = copy.deepcopy(action)
        with self._lock:
            try:
                self._check(action, session, credential, now)
                if action.tool == "ticket.close":
                    if not isinstance(grant, Grant) or type(grant.expires) is not int or not all(isinstance(v, str) for v in (grant.grant_id, grant.action_digest, grant.approver, grant.signature)):
                        raise Denied("approval_required")
                    expected = self._sign(grant.grant_id, grant.action_digest, grant.approver, grant.expires)
                    if not hmac.compare_digest(expected, grant.signature) or self._grants.get(grant.grant_id) != grant:
                        raise Denied("approval_invalid")
                    reviewer = self.users.get(grant.approver)
                    if not reviewer or reviewer["role"] != "approver" or reviewer["tenant"] != action.tenant:
                        raise Denied("approver_revoked")
                    if now >= grant.expires or grant.action_digest != digest(action.__dict__) or grant.grant_id in self._spent:
                        raise Denied("approval_expired_mismatched_or_spent")
                # This record is intent, not success. Failure to append blocks invocation.
                self._event(action, "AUTHORIZED", "validated_before_tool")
                if grant is not None and action.tool == "ticket.close":
                    self._spent.add(grant.grant_id)
                self._requests.add((action.tenant, action.request_id))
                self.tool_calls += 1
                ticket = self.tickets[action.resource]
                if action.tool == "ticket.close":
                    ticket["status"] = "closed"
                    ticket["version"] += 1
                result = {"status": ticket["status"], "version": ticket["version"]}
                self._event(action, "COMPLETED", "synthetic_tool_returned")
                return result
            except Denied as exc:
                if isinstance(action, Action):
                    self._event(action, "DENIED", str(exc))
                raise


def example(tool="ticket.close", request_id="demo-close"):
    return Action(request_id, "A", "alice", "agent-A", tool, "A-1", 1, {} if tool == "ticket.read" else {"status": "closed"})


def demo():
    engine = GatedAgent()
    action = example()
    outcomes = []
    for name, candidate, grant in [("no_approval", action, None)]:
        try:
            engine.invoke(candidate, "session-A", "credential-A", 1000, grant)
        except Denied as exc:
            outcomes.append({"case": name, "decision": "DENIED", "reason": str(exc)})
    grant = engine.approve(action, "session-A", "credential-A", "review-A", 1000)
    result = engine.invoke(action, "session-A", "credential-A", 1001, grant)
    outcomes.append({"case": "exact_approved_action", "decision": "COMPLETED", "result": result})
    for name, candidate in [("replay", action), ("cross_tenant", replace(example(request_id="other"), resource="B-1"))]:
        try:
            engine.invoke(candidate, "session-A", "credential-A", 1002, grant)
        except Denied as exc:
            outcomes.append({"case": name, "decision": "DENIED", "reason": str(exc)})
    return {"scope": "synthetic-control-test-only", "boundary": boundary_state(engine.boundary), "tool_calls": engine.tool_calls, "outcomes": outcomes, "audit": engine.audit}


if __name__ == "__main__":
    print(json.dumps(demo(), indent=2))
