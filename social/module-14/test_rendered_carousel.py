#!/usr/bin/env python3
"""Module 14 rendered accessibility smoke checks; not manual assistive-tech certification."""
from pathlib import Path
from tempfile import TemporaryDirectory
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
from export_pdf import normalize_pdf_heading

HTML = Path(__file__).with_name("CAROUSEL.html")

def main():
    with TemporaryDirectory(prefix="module14-render-") as temp, sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file:") else route.abort())
            page.goto(HTML.resolve().as_uri(), wait_until="load")
            headings = page.locator("section.slide h2").all_text_contents()
            assert len(headings) == 8 and all(h.strip().endswith("?") for h in headings)
            page.set_viewport_size({"width": 320, "height": 900})
            probe = page.evaluate("""() => {
                const p = document.createElement('div');
                p.style.cssText = 'position:absolute;left:315px;top:0;width:40px;height:1px';
                document.body.appendChild(p);
                const d = document.documentElement.scrollWidth - document.documentElement.clientWidth;
                p.remove();
                return d;
            }""")
            assert probe > 2, f"Overflow detector did not detect mutation: {probe}"
            for width in (1280, 390, 320):
                page.set_viewport_size({"width": width, "height": 900})
                metrics = page.evaluate("""() => ({
                    documentX: document.documentElement.scrollWidth - document.documentElement.clientWidth,
                    slides: [...document.querySelectorAll('section.slide')].map(s => ({
                        x: s.scrollWidth - s.clientWidth,
                        y: s.scrollHeight - s.clientHeight,
                        label: s.getAttribute('aria-labelledby'),
                        id: s.querySelector('h2')?.id,
                        visible: !!s.querySelector('h2')?.getClientRects().length
                    }))
                })""")
                assert metrics["documentX"] <= 2, (width, metrics)
                assert all(s["x"] <= 2 and s["y"] <= 2 and s["visible"]
                           and s["label"] == s["id"] for s in metrics["slides"]), (width, metrics)
            page.set_viewport_size({"width": 390, "height": 900})
            page.keyboard.press("Tab")
            assert page.evaluate("document.activeElement.tagName") == "A", "Chapter link not keyboard reachable"
            page.set_viewport_size({"width": 1280, "height": 900})
            page.emulate_media(media="print")
            print_overflow = page.locator('section.slide').evaluate_all('(slides)=>slides.map(s=>s.scrollHeight-s.clientHeight)')
            assert all(y <= 2 for y in print_overflow), ('Print clipping',print_overflow)
            output = Path(temp) / "module14.pdf"
            page.pdf(path=str(output), print_background=True, prefer_css_page_size=True)
            pdf = PdfReader(str(output))
            assert len(pdf.pages) == 8
            for i, p in enumerate(pdf.pages):
                assert abs(float(p.mediabox.width) - 576) <= 1
                assert abs(float(p.mediabox.height) - 720) <= 1
                extracted = normalize_pdf_heading(p.extract_text() or "")
                assert len(extracted) > 100 and normalize_pdf_heading(headings[i]) in extracted, i + 1
            print("PASS: Module 14 question headings, browser reflow 1280/390/320px, overflow mutation, keyboard link, 8-page extractable PDF")
            print("Limit: no 200% zoom, manual contrast, screen-reader, or tagged-PDF reading-order verification")
        finally:
            browser.close()

if __name__ == "__main__":
    main()
