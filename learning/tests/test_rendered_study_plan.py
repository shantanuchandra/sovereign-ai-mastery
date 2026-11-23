#!/usr/bin/env python3
"""Exercise study progress and generated Module 05 routes in the actual browser."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import os
import unittest
from playwright.sync_api import sync_playwright, expect

ROOT=Path(__file__).resolve().parents[2]
KEY='sovereign-study-plan-v1'

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*_args):
        pass

class StudyPlanBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(ROOT/'dist')))
        cls.thread=Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.origin=f'http://127.0.0.1:{cls.server.server_port}'
        cls.pw=sync_playwright().start();cls.browser=cls.pw.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.pw.stop();cls.server.shutdown();cls.server.server_close();cls.thread.join()

    def setUp(self):
        self.context=self.browser.new_context(viewport={'width':1280,'height':900},reduced_motion='reduce')
        self.page=self.context.new_page();self.errors=[];self.external=[]
        self.page.on('pageerror',lambda e:self.errors.append(str(e)))
        def route(r):
            if r.request.url.startswith(self.origin+'/'):
                r.continue_()
            else:
                self.external.append(r.request.url);r.abort()
        self.context.route('**/*',route)

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors,[])
        self.assertEqual(self.external,[])

    def open(self,suffix='#module-05'):
        self.page.goto(self.origin+'/learning/schedule.html'+suffix,wait_until='networkidle')
        expect(self.page.locator('#plan-progress')).to_contain_text('study hours marked complete')

    def test_filter_hash_persistence_and_actual_export(self):
        self.open()
        expect(self.page.locator('#plan-module')).to_have_value('05')
        self.assertEqual(self.page.locator('[data-module]:visible').count(),1)
        self.page.locator('#m05-h01').check()
        self.page.reload(wait_until='networkidle')
        expect(self.page.locator('#m05-h01')).to_be_checked()
        expect(self.page.locator('#plan-progress')).to_have_text('1 of 240 study hours marked complete')
        self.page.select_option('#plan-module','24')
        self.assertEqual(self.page.url.split('#')[1],'module-24')
        self.page.locator('#m24-h10').check()
        with self.page.expect_download() as event:
            self.page.click('#export-plan')
        result=Path(event.value.path()).read_text()
        self.assertEqual(result.count('\n## Module '),24)
        self.assertEqual(result.count('- [x]'),2)
        self.assertEqual(result.count('- [ ]'),238)
        self.assertIn('No competency certification or publication approval',result)

    def test_invalid_saved_data_unknown_ids_and_unknown_hash(self):
        self.page.add_init_script(f"localStorage.setItem('{KEY}',JSON.stringify(['m05-h02','bad','<script>',24]));")
        self.open('#module-99')
        expect(self.page.locator('#plan-module')).to_have_value('all')
        expect(self.page.locator('#plan-progress')).to_have_text('1 of 240 study hours marked complete')
        self.assertEqual(self.page.locator('[data-module]:visible').count(),24)
        self.page.evaluate(f"localStorage.setItem('{KEY}','invalid json')")
        # A fresh context tests a corrupt value without the earlier initialization script.
        fresh=self.browser.new_context();page=fresh.new_page()
        try:
            page.add_init_script(f"localStorage.setItem('{KEY}','invalid json')")
            page.goto(self.origin+'/learning/schedule.html')
            expect(page.locator('#plan-status')).to_contain_text('Saved progress is unavailable')
            expect(page.locator('#plan-progress')).to_have_text('0 of 240 study hours marked complete')
        finally:
            fresh.close()

    def test_denied_storage_remains_usable_and_exportable(self):
        self.page.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('unavailable')}})")
        self.open()
        self.page.locator('#m05-h01').check()
        expect(self.page.locator('#plan-status')).to_contain_text('could not be saved')
        with self.page.expect_download() as event:
            self.page.click('#export-plan')
        self.assertIn('Completed: 1 / 240',Path(event.value.path()).read_text())

    def test_shared_notes_load_only_after_explicit_click(self):
        requests=[]
        def notes(route):
            requests.append((route.request.url,route.request.method))
            route.fulfill(status=404,body='{}',headers={'access-control-allow-origin':'*'})
        self.page.route('https://api.github.com/**',notes)
        self.open()
        self.assertEqual(requests,[])
        self.page.click('#sync-now')
        expect(self.page.locator('#sync-status')).to_have_text('GitHub notes loaded')
        self.assertEqual(len(requests),1)
        self.assertEqual(requests[0][1],'GET')

    def test_mobile_keyboard_and_module_routes(self):
        self.open()
        self.page.locator('#m05-h01').focus();self.page.keyboard.press('Space')
        expect(self.page.locator('#m05-h01')).to_be_checked()
        for route in ['/learning/schedule.html#module-05','/modules/05-laws-regulation-jurisdiction.html',
                      '/labs/module-05/index.html','/social/module-05/POST.html']:
            for width in (1280,390,320):
                self.page.set_viewport_size({'width':width,'height':900})
                self.page.goto(self.origin+route,wait_until='networkidle')
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth'),2,(route,width))
        directory=os.environ.get('STUDIO_QA_SCREENSHOTS')
        if directory:
            output=Path(directory);output.mkdir(parents=True,exist_ok=True)
            self.open();self.page.screenshot(path=str(output/'study-plan-mobile.png'))
            self.page.goto(self.origin+'/modules/05-laws-regulation-jurisdiction.html',wait_until='networkidle')
            self.page.screenshot(path=str(output/'module05-mobile.png'))

if __name__=='__main__':
    unittest.main(verbosity=2)
