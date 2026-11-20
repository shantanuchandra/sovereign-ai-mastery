#!/usr/bin/env python3
"""Render Module 02's original HTML deck as a verified eight-page PDF for the site.

This is a static teaching artifact, not a tagged accessible PDF or a legal/compliance
certificate. The full HTML deck and linked chapter remain the reading alternatives.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "social/module-02/CAROUSEL.html"
OUTPUT = ROOT / "dist/social/module-02/QUESTIONS.pdf"


def main():
    assert HTML.is_file(), f"HTML deck missing: {HTML}"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.route("**/*", lambda route: route.continue_()
                       if route.request.url.startswith("file:") else route.abort())
            page.goto(HTML.as_uri(), wait_until="load")
            page.emulate_media(media="print")
            page.pdf(path=str(OUTPUT), print_background=True, prefer_css_page_size=True)
        finally:
            browser.close()

    pdf = PdfReader(str(OUTPUT))
    assert len(pdf.pages) == 8, "Expected exactly eight slide pages"
    for number, page in enumerate(pdf.pages, 1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        assert abs(width - 576) <= 1.0 and abs(height - 720) <= 1.0, (
            f"Page {number} is not 8x10 inches: {width}x{height}")
        txt = page.extract_text() or ""
        assert len(txt.strip()) > 120, f"Page {number} lacks extractable text"
        assert f"{number:02d} / 08" in txt, f"Slide number absent from page {number}"
        assert "DECISIONTEST" in "".join(txt.split()), f"Decision section absent from page {number}"
    print(f"Verified {len(pdf.pages)} pages, 8x10 inches, extractable text: {OUTPUT}")


if __name__ == "__main__":
    main()
