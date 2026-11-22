#!/usr/bin/env python3
"""Draft Module 05 carousel portrait PDF exporter, not a tagged accessible PDF."""
from __future__ import annotations

import re
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "social/module-05/CAROUSEL.html"
OUTPUT = ROOT / "dist/social/module-05/QUESTIONS.pdf"


def normalize(text: str) -> str:
    text = re.sub(r"(?<=\w)-[ \t]*\n[ \t]*(?=\w)", "-", text)
    return " ".join(text.replace("“", '"').replace("”", '"').split()).casefold()


def heading_token_stream(text: str) -> str:
    """Ignore line-break/inline-tag whitespace when comparing PDF headings."""
    return re.sub(r"[^\w]+", "", normalize(text), flags=re.UNICODE)


def main() -> None:
    assert HTML.is_file()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 1024})
            page.route("**/*",
                       lambda route: route.continue_()
                       if route.request.url.startswith("file:") else route.abort())
            page.goto(HTML.resolve().as_uri(), wait_until="load")
            headings = page.locator("section.slide h2").all_text_contents()
            assert len(headings) == 8, f"Expected 8 slide headings, got {len(headings)}"
            page.emulate_media(media="print")
            page.pdf(path=str(OUTPUT), print_background=True, prefer_css_page_size=True)
        finally:
            browser.close()

    pdf = PdfReader(str(OUTPUT))
    assert len(pdf.pages) == 8, f"Expected 8 pages, got {len(pdf.pages)}"
    for index, page in enumerate(pdf.pages):
        assert abs(float(page.mediabox.width) - 576) < 2, "Expected 8in width"
        assert abs(float(page.mediabox.height) - 720) < 2, "Expected 10in height"
        text = normalize(page.extract_text() or "")
        assert len(text) > 90, f"Missing searchable text page {index + 1}"
        candidate = heading_token_stream(headings[index])
        assert candidate in heading_token_stream(text), f"Heading extraction mismatch page {index + 1}: {candidate}"
    print(f"Module 05 PDF draft: {len(pdf.pages)} pages, 8x10 inches, headings extractable")
    print(f"Draft output: {OUTPUT}")
    print("NOT a tagged PDF or manual screen-reader / reading-order verification")


if __name__ == "__main__":
    main()
