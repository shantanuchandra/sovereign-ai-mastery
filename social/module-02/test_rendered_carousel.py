#!/usr/bin/env python3
"""Browser-level Module 02 carousel QA, using a local Chromium instance.

Install: python -m pip install playwright pypdf && python -m playwright install chromium
Run: python social/module-02/test_rendered_carousel.py
All material is local/synthetic. The browser is prevented from making network requests.
"""
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import sys

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

HTML = Path(__file__).with_name("CAROUSEL.html")
QUESTIONS = (
    "What must remain under control?",
    "Who can authorize the exception?",
    "Can a local model still send data away?",
    "Does an air gap allow a private link?",
    "Can one maturity score override a hard boundary?",
    "What happens when the local model times out?",
    "Does a documented single-region deployment prove compliance?",
    "What would make you refuse a cheaper architecture?",
)


def main() -> int:
    assert HTML.is_file(), f"Missing source: {HTML}"
    with TemporaryDirectory(prefix="module02-print-") as tmp, sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=1)
            page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file:") else route.abort())
            page.goto(HTML.resolve().as_uri(), wait_until="load")
            headings = page.locator("section.slide h2").all_text_contents()
            assert len(headings) == 8, f"Expected 8 slides, found {len(headings)}"
            assert all(text.strip().endswith("?") for text in headings), headings

            # Actual browser geometry: overflowing slide content is hidden by CSS.
            for width in (1280, 390, 320):
                page.set_viewport_size({"width": width, "height": 900})
                metrics = page.locator("section.slide").evaluate_all(
                    """slides => slides.map((slide, index) => ({
                        index: index + 1,
                        overflowX: slide.scrollWidth - slide.clientWidth,
                        overflowY: slide.scrollHeight - slide.clientHeight,
                        title: slide.querySelector('h2')?.textContent?.trim()
                    }))"""
                )
                clipped = [m for m in metrics if m["overflowX"] > 2 or m["overflowY"] > 2]
                assert not clipped, f"Clipped slide content at {width}px: {clipped}"

            # Export actual PDF, not merely inspect @page rules.
            page.set_viewport_size({"width": 1280, "height": 900})
            page.emulate_media(media="print")
            pdf_path = Path(tmp) / "module-02-questions.pdf"
            page.pdf(path=str(pdf_path), print_background=True, prefer_css_page_size=True)
            pdf = PdfReader(str(pdf_path))
            assert len(pdf.pages) == 8, f"Expected 8 PDF pages, found {len(pdf.pages)}"
            page_text = [(p.extract_text() or "").strip() for p in pdf.pages]
            for i, text in enumerate(page_text):
                assert len(text) > 120, f"PDF page {i + 1} has little extractable text ({len(text)} chars)"
                assert f"{i + 1:02d} / 08" in text, f"Missing slide number on PDF page {i + 1}"
                assert "DECISION TEST" in text, (
                    f"Missing decision footer on PDF page {i + 1}; extracted text follows "
                    f"(first 1200 chars): {text[:1200]!r}"
                )
            print(f"PASS: 8 PDF pages with extractable text; 8 slide headings; no measured slide overflow at 1280/390/320px.")
            print(f"PDF test artifact was temporary at {pdf_path}; not published or claimed visually reviewed.")
            return 0
        finally:
            browser.close()


if __name__ == "__main__":
    sys.exit(main())
