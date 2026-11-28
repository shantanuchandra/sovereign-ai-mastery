#!/usr/bin/env python3
"""Exercise the built Studio in Chromium, with no external service requests."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import json
import os
import unittest

from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[2]
STORAGE = "sovereign-ai-learning-studio-v1"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


class StudioBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert (ROOT / "dist/learning/index.html").exists(), "Build the site first"
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT / "dist")))
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.origin = f"http://127.0.0.1:{cls.server.server_port}"
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.context = self.browser.new_context(viewport={"width": 1280, "height": 900}, reduced_motion="reduce")
        self.page = self.context.new_page()
        self.errors = []
        self.external = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))

        def route(request):
            if request.request.url.startswith(self.origin + "/"):
                request.continue_()
            else:
                self.external.append(request.request.url)
                request.abort()

        self.context.route("**/*", route)
        self.open()

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors, [], "Uncaught browser exceptions")
        self.assertEqual(self.external, [], "Studio attempted external network access")

    def open(self):
        self.page.goto(self.origin + "/learning/", wait_until="networkidle")
        expect(self.page.locator("#flow-register .flow-card").first).to_be_visible()

    def scenario(self, name):
        self.page.select_option("#scenario-library", name)
        self.page.click("#apply-scenario")

    def missed_location(self):
        self.scenario("speech")
        self.page.locator('[data-qid="location"] [data-choice="0"]').click()
        expect(self.page.locator('[data-qid="remediation-location"]')).to_be_visible()

    def download(self, button):
        with self.page.expect_download() as event:
            self.page.click(button)
        return Path(event.value.path()).read_text()

    def test_new_module_feedback_followups_and_both_downloads(self):
        self.scenario("factory")
        for qid,slug in [('rag-permissions','12-sovereign-rag-systems'),('optimization-evidence','13-fine-tuning-optimization-evaluation'),('agent-approval','14-agents-apis-enterprise-integrations')]:
            self.page.locator(f'[data-qid="{qid}"] [data-choice="0"]').click()
            expect(self.page.locator(f'[data-qid="{qid}"] .feedback a')).to_have_attribute('href','../modules/'+slug+'.html')
            expect(self.page.locator(f'[data-qid="remediation-{qid}"]')).to_be_visible()
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator('#tutor-progress')).to_have_text('3 of 7 answered')
        md=self.download('#download-md')
        data=self.download('#download-json')
        for slug in ['12-sovereign-rag-systems','13-fine-tuning-optimization-evaluation','14-agents-apis-enterprise-integrations']:
            self.assertIn(slug,md)
            self.assertIn(slug,data)
        self.assertEqual(md.count('Follow-up result: Not attempted'),3)

    def test_all_dropdowns_and_scenarios_match_the_engine(self):
        expected = self.page.evaluate("""async () => {
            const e = await import('./studio-engine.mjs');
            return {labels:e.LABELS, presets:e.PRESETS, names:e.PRESET_LABELS};
        }""")
        for key, labels in expected["labels"].items():
            actual = self.page.locator(f'#{key} option').evaluate_all("els => Object.fromEntries(els.map(e => [e.value,e.textContent]))")
            self.assertEqual(actual, labels)
        self.assertEqual(self.page.locator("#scenario-library option").count(), 21)
        self.assertEqual(self.page.locator("#workload option").count(), 26)
        for name, inputs in expected["presets"].items():
            self.scenario(name)
            for key, value in inputs.items():
                expect(self.page.locator(f"#{key}")).to_have_value(value)
        self.assertEqual(self.page.locator("#counter-key option").count(), 10)

    def test_security_custody_operations_guidance_and_exports(self):
        self.page.set_viewport_size({'width':1600,'height':1000})
        self.scenario('factory')
        for number in ['15','16','17']:
            expect(self.page.locator(f'#lesson-links a[href*="/modules/{number}-"]')).to_be_visible()
        expect(self.page.locator('#approval-gates')).to_contain_text('indirect prompt injection')
        expect(self.page.locator('#approval-gates')).to_contain_text('Encryption and attestation do not establish physical residency')
        expect(self.page.locator('#approval-gates')).to_contain_text('SLO and error-budget denominators')
        journal=self.download('#download-md')
        record=json.loads(self.download('#download-json'))
        for number in ['15','16','17']:
            self.assertIn('/'+number+'-',journal)
            self.assertTrue(any('/'+number+'-' in row['url'] for row in record['blueprint']['lessons']))

    def test_physical_boundaries_and_counterfactual_do_not_authorize_cloud_fallback(self):
        self.scenario("energy")
        expect(self.page.locator("#solution-status")).to_have_text("PROVISIONAL")
        expect(self.page.locator('[data-flow="licensing"]')).to_contain_text("offline activation")
        expect(self.page.locator('[data-flow="updates"]')).to_contain_text("offline media")
        self.page.select_option("#counter-key", "capacity")
        self.page.select_option("#counter-value", "public_cloud")
        expect(self.page.locator("#compare-next")).to_contain_text("Gated")
        expect(self.page.locator("#capacity")).to_have_value("onsite_gpu")
        self.page.click("#apply-counter")
        expect(self.page.locator("#solution-status")).to_have_text("BLOCKED")
        self.assertTrue(all(s == "BLOCKED" for s in self.page.locator(".flow-heading code").all_text_contents()))

    def test_followup_preserves_first_answer_on_reload_and_both_exports(self):
        self.missed_location()
        self.page.locator('[data-qid="remediation-location"] [data-choice="0"]').click()
        expect(self.page.locator("#tutor-summary")).to_contain_text("1 of 1 follow-up")
        self.page.locator("#reflection").fill("Test the OCR fallback with synthetic pages.")
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator('[data-qid="location"] .answer.selected')).to_contain_text("Permit it")
        expect(self.page.locator('[data-qid="remediation-location"] .feedback')).to_contain_text("Reasoning supported")
        expect(self.page.locator("#reflection")).to_have_value("Test the OCR fallback with synthetic pages.")
        md = self.download("#download-md")
        self.assertIn("Data-flow register", md)
        self.assertIn("Needs review", md)
        self.assertIn("Follow-up result: Correct reasoning", md)
        data = json.loads(self.download("#download-json"))
        self.assertEqual(data["version"], "1.2.0")
        self.assertTrue(any(f["id"] == "speech" for f in data["blueprint"]["flows"]))
        review = data["review"]["challenges"][0]
        self.assertFalse(review["feedback"]["ok"])
        self.assertTrue(review["followUp"]["feedback"]["ok"])

    def test_restart_and_constraint_changes_clear_both_attempt_types(self):
        self.missed_location()
        self.page.locator('[data-qid="remediation-location"] [data-choice="0"]').click()
        self.page.click("#restart-challenges")
        expect(self.page.locator("#tutor-progress")).to_have_text("0 of 7 answered")
        expect(self.page.locator(".remediation")).to_have_count(0)
        self.page.locator('[data-qid="location"] [data-choice="0"]').click()
        self.page.select_option("#data", "synthetic")
        expect(self.page.locator(".remediation")).to_have_count(0)
        saved = self.page.evaluate("key => JSON.parse(localStorage.getItem(key))", STORAGE)
        self.assertEqual(saved["answers"], {})
        self.assertEqual(saved["remediationAnswers"], {})

    def test_historical_and_invalid_saved_answers_are_not_replayed(self):
        self.missed_location()
        self.page.locator("#reflection").fill("Keep this reflection.")
        self.page.evaluate("""key => {
            const saved=JSON.parse(localStorage.getItem(key));
            saved.quizVersion='1.1.0'; localStorage.setItem(key,JSON.stringify(saved));
        }""", STORAGE)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#workload")).to_have_value("speech")
        expect(self.page.locator("#reflection")).to_have_value("Keep this reflection.")
        expect(self.page.locator("#tutor-progress")).to_have_text("0 of 7 answered")
        self.page.evaluate("""key => {
            const saved=JSON.parse(localStorage.getItem(key));
            saved.answers={location:999,operations:'1',evidence:-1};
            saved.remediationAnswers={'remediation-location':0};
            localStorage.setItem(key,JSON.stringify(saved));
        }""", STORAGE)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#tutor-progress")).to_have_text("0 of 7 answered")
        expect(self.page.locator(".remediation")).to_have_count(0)

    def test_malformed_or_disabled_storage_does_not_break_the_studio(self):
        self.page.evaluate("key => localStorage.setItem(key,'{broken')", STORAGE)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#solution-status")).to_have_text("PROVISIONAL")
        self.page.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('Storage disabled')}})")
        self.page.reload(wait_until="networkidle")
        self.scenario("insurance")
        expect(self.page.locator('[data-flow="ocr"]')).to_be_visible()
        self.assertIn("Document OCR", self.download("#download-md"))

    def test_mobile_reflow_and_keyboard_followup(self):
        self.missed_location()
        follow = self.page.locator('[data-qid="remediation-location"] [data-choice="0"]')
        follow.focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator('[data-qid="remediation-location"] .feedback')).to_contain_text("Reasoning supported")
        self.assertEqual(self.page.evaluate("document.activeElement.className"), "feedback-wrap")
        for width in (1440, 1280, 390, 320):
            self.page.set_viewport_size({"width": width, "height": 900})
            overflow = self.page.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
            self.assertLessEqual(overflow, 2, f"Document overflow at {width}px")
            clipped = self.page.locator(".flow-card").evaluate_all("els => els.some(e => e.scrollWidth > e.clientWidth+2)")
            self.assertFalse(clipped, f"Flow card clipped at {width}px")
        self.page.click("#toc-toggle")
        expect(self.page.locator("#book-nav")).to_have_class("rail show")
        expect(self.page.locator("#toc-toggle")).to_have_attribute("aria-expanded", "true")
        self.page.click("#toc-close")
        expect(self.page.locator("#toc-toggle")).to_be_focused()
        expect(self.page.locator("#toc-toggle")).to_have_attribute("aria-expanded", "false")
        self.page.click("#toc-toggle")
        self.page.keyboard.press("Escape")
        expect(self.page.locator("#toc-toggle")).to_have_attribute("aria-expanded", "false")
        screenshots = os.environ.get("STUDIO_QA_SCREENSHOTS")
        if screenshots:
            target = Path(screenshots)
            target.mkdir(parents=True, exist_ok=True)
            self.page.locator('[data-flow="speech"]').screenshot(path=str(target / "studio-mobile-flow.png"))
            self.page.set_viewport_size({"width": 1280, "height": 900})
            self.page.locator('[data-qid="remediation-location"]').screenshot(path=str(target / "studio-followup.png"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
