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


            # Actual browser geometry: inspect nested elements, not just slide boxes.
            for width in (1280, 390, 320):
                page.set_viewport_size({"width": width, "height": 900})
                nested = page.locator("section.slide").evaluate_all(
                    """slides => slides.map((slide, index) => {
                        const names = ['.mast', '.eyebrow', 'h2', '.answer', '.decision', 'footer'];
                        const blocks = names.map(name => {
                            const e = slide.querySelector(name);
                            if (!e) return {name, missing:true};
                            const r = e.getBoundingClientRect(), st = getComputedStyle(e);
                            return {name, top:r.top, bottom:r.bottom, height:r.height,
                                font:parseFloat(st.fontSize), visible:st.visibility !== 'hidden'};
                        });
                        const collisions = [];
                        for(let k=1; k<blocks.length; k++) {
                            if(blocks[k].missing || blocks[k-1].missing) continue;
                            if(blocks[k].top < blocks[k-1].bottom - 3)
                                collisions.push(blocks[k-1].name + ' overlaps ' + blocks[k].name);
                        }
                        return {index:index+1, blocks, collisions};
                    })"""
                )
                assert all(not entry["collisions"] and all(
                    not block.get("missing") and block.get("visible") and block["height"] > 3
                    for block in entry["blocks"]) for entry in nested), (
                    f"Nested content overlap / invisible text at {width}px: {nested}"
                )
                if width == 320:
                    assert all(next(b for b in entry["blocks"] if b["name"] == ".answer")["font"] >= 14
                               and next(b for b in entry["blocks"] if b["name"] == "footer")["font"] >= 12
                               for entry in nested), "Critical mobile text smaller than accepted 14px/12px bounds"

            # Accessibility semantics: every slide must expose a unique named region,
            # with one visible question heading. This is DOM evidence, not an
            # assistive-technology or tagged-PDF certification.
            semantics = page.evaluate("""() => ({
                lang: document.documentElement.lang,
                mainCount: document.querySelectorAll('main').length,
                navLabel: document.querySelector('nav.toolbar')?.getAttribute('aria-label'),
                slides: [...document.querySelectorAll('section.slide')].map(s => {
                    const heading = s.querySelector('h2');
                    return {id: heading?.id, label: s.getAttribute('aria-labelledby'),
                        text: heading?.textContent?.trim(), visible: !!heading?.getClientRects().length};
                }),
                linkName: document.querySelector('nav.toolbar a')?.textContent?.trim(),
                buttonName: document.querySelector('nav.toolbar button')?.getAttribute('aria-label')
            })""")
            assert semantics["lang"] == "en" and semantics["mainCount"] == 1, semantics
            assert semantics["navLabel"] and semantics["linkName"] and semantics["buttonName"], semantics
            ids = [s["id"] for s in semantics["slides"]]
            assert len(ids) == 8 and len(set(ids)) == 8 and all(ids), semantics
            assert all(s["label"] == s["id"] and s["visible"] and s["text"].endswith("?")
                       for s in semantics["slides"]), semantics

            # Keyboard navigation: the first two controls must be reachable in DOM order.
            page.set_viewport_size({"width": 390, "height": 900})
            page.keyboard.press("Tab")
            first = page.evaluate("document.activeElement?.tagName + ':' + (document.activeElement?.getAttribute('href') || '')")
            assert first.startswith("A:"), f"Expected chapter link first in tab order, got {first!r}"
            page.keyboard.press("Tab")
            second = page.evaluate("document.activeElement?.tagName")
            assert second == "BUTTON", f"Expected print button second in tab order, got {second!r}"

            # Reflow proxy: a 390px CSS viewport at 200% browser zoom has
            # approximately 195 CSS pixels of available layout width. Applying
            # CSS zoom to the root instead scales a fixed layout and creates
            # misleading document overflow; test the narrower layout directly.
            # This remains automated reflow coverage, not manual browser zoom QA.
            page.set_viewport_size({"width": 195, "height": 900})
            zoom_metrics = page.evaluate("""() => ({
                docOverflowX: document.documentElement.scrollWidth - document.documentElement.clientWidth,
                slides: [...document.querySelectorAll('section.slide')].map((slide, index) => ({
                    index: index + 1,
                    overflowX: slide.scrollWidth - slide.clientWidth,
                    overflowY: slide.scrollHeight - slide.clientHeight
                }))
            })""")
            assert zoom_metrics["docOverflowX"] <= 2, f"Horizontal document overflow at 195px reflow proxy: {zoom_metrics}"
            assert all(m["overflowX"] <= 2 and m["overflowY"] <= 2 for m in zoom_metrics["slides"]), (
                f"Slide clipping at 195px reflow proxy: {zoom_metrics}"
            )

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
                assert "DECISIONTEST" in "".join(text.split()), (
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
