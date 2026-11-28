import copy
import json
import threading
import unittest
from dataclasses import replace
from gated_agent import ARTIFACTS, Action, Denied, GatedAgent, boundary_state, demo, example, fixture_boundary


class GateTests(unittest.TestCase):
    def setUp(self):
        self.e = GatedAgent()
        self.a = example()

    def approval(self, action=None, **kwargs):
        return self.e.approve(action or self.a, "session-A", "credential-A", "review-A", 1000, **kwargs)

    def invoke(self, action=None, grant=None, now=1001, session="session-A", credential="credential-A"):
        return self.e.invoke(action or self.a, session, credential, now, grant)

    def deny(self, **kwargs):
        before = self.e.tool_calls
        with self.assertRaises(Denied):
            self.invoke(**kwargs)
        self.assertEqual(self.e.tool_calls, before)

    def test_read_without_approval(self):
        self.assertEqual(self.invoke(example("ticket.read")), {"status": "open", "version": 1})

    def test_write_requires_approval(self):
        self.deny()
        self.assertEqual(self.e.tickets["A-1"]["status"], "open")

    def test_exact_approved_write(self):
        self.assertEqual(self.invoke(grant=self.approval()), {"status": "closed", "version": 2})
        self.assertEqual([e["status"] for e in self.e.audit], ["APPROVED", "AUTHORIZED", "COMPLETED"])

    def test_forged_user(self):
        self.deny(action=replace(self.a, user="bob"))

    def test_session_from_other_tenant(self):
        self.deny(session="session-B")

    def test_agent_wrong_tenant(self):
        self.deny(action=replace(self.a, agent="agent-B"))

    def test_agent_delegation_revoked(self):
        self.e.agents["agent-A"]["users"].clear()
        self.deny()

    def test_cross_tenant_resource(self):
        self.deny(action=replace(self.a, resource="B-1"))

    def test_cross_tenant_credential(self):
        self.deny(credential="credential-B")

    def test_unknown_credential(self):
        self.deny(credential="not-issued")

    def test_scope_removed(self):
        self.e.credentials["credential-A"]["scopes"] = {"ticket.read"}
        self.deny()

    def test_wrong_audience(self):
        self.e.credentials["credential-A"]["aud"] = "model-gateway"
        self.deny()

    def test_credential_expiry_boundary(self):
        self.deny(now=2000)

    def test_user_cannot_self_approve(self):
        with self.assertRaises(Denied):
            self.e.approve(self.a, "session-A", "credential-A", "session-A", 1000)
        self.assertEqual(self.e.tool_calls, 0)

    def test_approver_other_tenant(self):
        with self.assertRaises(Denied):
            self.e.approve(self.a, "session-A", "credential-A", "review-B", 1000)

    def test_approver_revocation_after_issue(self):
        grant = self.approval()
        self.e.users["bea"]["role"] = "operator"
        self.deny(grant=grant)

    def test_approval_exact_expiry(self):
        self.deny(grant=self.approval(ttl=2), now=1002)

    def test_tampered_signature(self):
        self.deny(grant=replace(self.approval(), signature="0" * 64))

    def test_tampered_expiry(self):
        self.deny(grant=replace(self.approval(), expires=99999))

    def test_signature_wrong_type(self):
        self.deny(grant=replace(self.approval(), signature=123))

    def test_approval_unknown_registry(self):
        grant = self.approval()
        self.e._grants.clear()
        self.deny(grant=grant)

    def test_request_id_mutation(self):
        self.deny(action=replace(self.a, request_id="changed"), grant=self.approval())

    def test_params_mutation(self):
        self.deny(action=replace(self.a, params={"status": "open"}), grant=self.approval())

    def test_resource_changed_after_review(self):
        grant = self.approval()
        self.e.tickets["A-1"]["version"] += 1
        self.deny(grant=grant)

    def test_policy_changed_after_review(self):
        grant = self.approval()
        self.e.policy = "bank-a-v2"
        self.deny(grant=grant)

    def test_replay_after_write(self):
        grant = self.approval()
        self.invoke(grant=grant)
        self.deny(grant=grant)

    def test_read_request_replay(self):
        action = example("ticket.read")
        self.invoke(action)
        self.deny(action=action)

    def test_explicit_spent_grant(self):
        grant = self.approval()
        self.e._spent.add(grant.grant_id)
        self.deny(grant=grant)

    def test_concurrent_replay_one_tool_call(self):
        grant = self.approval()
        results = []
        def run():
            try:
                self.invoke(grant=grant)
                results.append("completed")
            except Denied:
                results.append("denied")
        threads = [threading.Thread(target=run) for _ in range(2)]
        for thread in threads: thread.start()
        for thread in threads: thread.join()
        self.assertCountEqual(results, ["completed", "denied"])
        self.assertEqual(self.e.tool_calls, 1)

    def test_no_shell_tool(self):
        self.deny(action=replace(self.a, tool="shell.exec"))

    def test_no_extra_url_parameter(self):
        self.deny(action=replace(self.a, params={"status": "closed", "callback": "https://example.invalid"}))

    def test_audit_unavailable_blocks_write(self):
        grant = self.approval()
        self.e.audit_available = False
        self.deny(grant=grant)
        self.assertEqual(self.e.tickets["A-1"]["version"], 1)

    def test_audit_omits_raw_params_and_credentials(self):
        self.invoke(grant=self.approval())
        value = json.dumps(self.e.audit)
        for forbidden in ("session-A", "credential-A", "Synthetic", "params", "signature", "demo-close"):
            self.assertNotIn(forbidden, value)
        self.assertTrue(all(len(e["action_digest"]) == 64 for e in self.e.audit))

    def test_invalid_clock(self):
        for now in (True, -1, 1.5, float("nan")):
            with self.subTest(now=now): self.deny(now=now)

    def test_invalid_version(self):
        self.deny(action=replace(self.a, version=True))

    def test_no_favourable_quality_override(self):
        self.e.boundary["site"] = "cloud-region"
        self.e.boundary["quality_score"] = 100
        self.deny()

    def test_each_artifact_external_blocks(self):
        for name in ARTIFACTS:
            with self.subTest(name=name):
                declaration = fixture_boundary()
                declaration["artifacts"][name] = "external"
                self.assertEqual(boundary_state(declaration), "BLOCKED")

    def test_external_path_dominates_missing_metadata(self):
        self.assertEqual(boundary_state({"artifacts": {"ocr": "external"}}), "BLOCKED")

    def test_missing_artifact_unverified(self):
        declaration = fixture_boundary()
        del declaration["artifacts"]["backups"]
        self.assertEqual(boundary_state(declaration), "UNVERIFIED")

    def test_remote_operator_blocked(self):
        declaration = fixture_boundary()
        declaration["operator"] = "remote"
        self.assertEqual(boundary_state(declaration), "BLOCKED")

    def test_online_network_blocked(self):
        declaration = fixture_boundary()
        declaration["network"] = "internet"
        self.assertEqual(boundary_state(declaration), "BLOCKED")

    def test_offline_media_unknown_unverified(self):
        declaration = fixture_boundary()
        declaration["offline_media_reviewed"] = False
        self.assertEqual(boundary_state(declaration), "UNVERIFIED")

    def test_declaration_never_certified(self):
        self.assertEqual(boundary_state(fixture_boundary()), "DECLARED_ONLY")

    def test_demo_real_control_flow(self):
        evidence = demo()
        self.assertEqual(evidence["tool_calls"], 1)
        self.assertEqual([r["decision"] for r in evidence["outcomes"]], ["DENIED", "COMPLETED", "DENIED", "DENIED"])


if __name__ == "__main__":
    unittest.main()
