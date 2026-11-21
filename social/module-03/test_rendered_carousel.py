#!/usr/bin/env python3
"""Module 03 browser/PDF smoke test. Synthetic content only; no network requests."""
from pathlib import Path
from tempfile import TemporaryDirectory
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

HTML = Path(__file__).with_name("CAROUSEL.html")

def main():
    assert HTML.is_file()
    with TemporaryDirectory(prefix="module03-qa-") as temp, sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file:") else route.abort())
            page.goto(HTML.resolve().as_uri())
            headings = page.locator("section.slide h2").all_text_contents()
            assert len(headings) == 8 and all(h.strip().endswith("?") for h in headings), headings
            for width in (1280, 390, 320, 195):
                page.set_viewport_size({"width": width, "height": 900})
                metrics = page.evaluate("""() => ({
                    documentX: document.documentElement.scrollWidth - document.documentElement.clientWidth,
                    slides: [...document.querySelectorAll('section.slide')].map(s => ({
                        x: s.scrollWidth - s.clientWidth,
                        y: s.scrollHeight - s.clientHeight,
                        heading: !!s.querySelector('h2')?.getClientRects().length,
                        label: s.getAttribute('aria-labelledby'),
                        id: s.querySelector('h2')?.id
                    }))
                })""")
                if metrics["documentX"] > 2:
                    offenders = page.evaluate("""() => {
                        const limit = document.documentElement.clientWidth;
                        return [...document.querySelectorAll('body *')].map(el => {
                            const r = el.getBoundingClientRect();
                            const css = getComputedStyle(el);
                            return {tag: el.tagName.toLowerCase(), id: el.id,
                                className: typeof el.className === 'string' ? el.className : '',
                                right: Math.round(r.right * 100) / 100,
                                left: Math.round(r.left * 100) / 100,
                                scrollWidth: el.scrollWidth, clientWidth: el.clientWidth,
                                minWidth: css.minWidth, overflowX: css.overflowX};
                        }).filter(x => x.right > limit + 2 || x.left < -2)
                          .sort((a, b) => b.right - a.right).slice(0, 15);
                    }""")
                    print(f"OVERFLOW DIAGNOSTIC width={width} metrics={metrics} offenders={offenders}", flush=True)
                assert metrics["documentX"] <= 2, (width, metrics)
                assert all(s["x"] <= 2 and s["y"] <= 2 and s["heading"]
                           and s["label"] == s["id"] for s in metrics["slides"]), (width, metrics)
            page.set_viewport_size({"width": 390, "height": 900})
            page.keyboard.press("Tab")
            assert page.evaluate("document.activeElement.tagName") == "A", "Chapter link not keyboard reachable"
            page.set_viewport_size({"width": 1280, "height": 900})
            page.emulate_media(media="print")
            path = Path(temp) / "module03.pdf"
            page.pdf(path=str(path), print_background=True, prefer_css_page_size=True)
            pdf = PdfReader(str(path))
            assert len(pdf.pages) == 8, f"Expected 8 PDF pages; got {len(pdf.pages)}"
            for i, p in enumerate(pdf.pages, 1):
                extracted = p.extract_text() or ""
                assert len(extracted.strip()) > 100, (i, extracted[:200])
                assert headings[i-1].strip() in " ".join(extracted.split()), (i, extracted[:250])
            print("PASS: 8 question slides; browser overflow at 1280/390/320/195 CSS px; named headings; keyboard link; 8 text-extractable PDF pages")
            print("Limit: automated smoke test, not manual visual inspection or screen-reader certification")
        finally:
            browser.close()

if __name__ == "__main__":
    main()
