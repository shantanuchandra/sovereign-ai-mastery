#!/usr/bin/env python3
"""Export the synthetic Module 11 teaching deck. Not a tagged accessible PDF."""
import re
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "social/module-11/CAROUSEL.html"
OUTPUT = ROOT / "dist/social/module-11/QUESTIONS.pdf"

def normalize_pdf_heading(text):
    """Normalize PDF hyphen line wraps without dropping heading words."""
    text = re.sub(r"(?<=\w)-[ \t]*\n[ \t]*(?=\w)", "-", text)
    return " ".join(text.split())


def main():
    assert normalize_pdf_heading("named-\nfactory rule?") == "named-factory rule?"
    assert normalize_pdf_heading("two words\nnext line") == "two words next line"
    assert HTML.is_file()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file:") else route.abort())
            page.goto(HTML.resolve().as_uri(), wait_until="load")
            headings = page.locator("section.slide h2").all_text_contents()
            assert len(headings) == 8
            page.emulate_media(media="print")
            page.pdf(path=str(OUTPUT), print_background=True, prefer_css_page_size=True)
        finally:
            browser.close()
    pdf = PdfReader(str(OUTPUT))
    assert len(pdf.pages) == 8, f"Expected 8 pages, got {len(pdf.pages)}"
    for i, p in enumerate(pdf.pages):
        assert abs(float(p.mediabox.width) - 576) <= 1
        assert abs(float(p.mediabox.height) - 720) <= 1
        extracted = normalize_pdf_heading(p.extract_text() or "")
        assert len(extracted) > 100, f"Missing text on page {i+1}"
        assert normalize_pdf_heading(headings[i]) in extracted, f"Heading missing on page {i+1}"
    print(f"Verified 8 pages, 8x10 inches and extractable text: {OUTPUT}")
    print("Not a tagged PDF or assistive-technology certification")

if __name__ == "__main__":
    main()
