#!/usr/bin/env python3
"""Chromium smoke test of unpublished built Module 05 reader, not a manual AT audit."""
from __future__ import annotations

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "dist/modules/05-laws-regulation-jurisdiction.html"


def main() -> None:
    if not PAGE.is_file():
        raise RuntimeError("Build draft reader first: python scripts/build_site.py")
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.route("**/*", lambda route: route.continue_()
                       if route.request.url.startswith("file:") else route.abort())
            for width in (1280, 390, 320):
                page.set_viewport_size({"width": width, "height": 900})
                page.goto(PAGE.resolve().as_uri(), wait_until="load")
                headings = page.locator("main .prose h3").all_text_contents()
                assert len([x for x in headings if x.strip().startswith("5.")]) == 8, (
                    f"{width}px rendered section count mismatch: {headings}"
                )
                diagram = page.locator("figure.diagram-rendered img")
                assert diagram.count() >= 1, f"{width}px: missing static visual"
                assert diagram.first.get_attribute("alt"), "Missing nonempty diagram alt text"
                assert diagram.first.evaluate("(img) => img.complete && img.naturalWidth > 0"), (
                    f"{width}px: diagram fails to render with JavaScript/network unavailable"
                )
                metrics = page.evaluate("""() => {
                    const main = document.querySelector('main.book-page');
                    const doc = document.documentElement;
                    const region = document.querySelector('figure.diagram-rendered .diagram-viewport');
                    return {
                        viewport: doc.clientWidth,
                        documentScrollWidth: doc.scrollWidth,
                        mainWidth: main.getBoundingClientRect().width,
                        diagramScrollRegion: Boolean(region),
                        visibleHeading: Boolean(document.querySelector('main .prose h1'))
                    };
                }""")
                assert metrics["visibleHeading"], f"{width}px: missing visible chapter H1"
                assert metrics["diagramScrollRegion"], f"{width}px: diagram is not in a scroll region"
                # Some wide evidence tables may have intentionally horizontal
                # scrolling in their own containers, but never the whole page.
                assert metrics["documentScrollWidth"] <= metrics["viewport"] + 2, (
                    f"{width}px: page-level horizontal overflow: {metrics}"
                )
                print(f"PASS built reader {width}px: 8 sections, offline SVG, no page overflow")

            page.set_viewport_size({"width": 1280, "height": 900})
            page.goto(PAGE.resolve().as_uri(), wait_until="load")
            page.keyboard.press("Tab")
            focus = page.evaluate("""() => {
                const el = document.activeElement;
                return {label: el.textContent.trim(), tag: el.tagName,
                        href: el.getAttribute('href')};
            }""")
            assert focus["tag"] == "A" and focus["href"] == "#main", (
                f"Skip to chapter not first keyboard focus: {focus}"
            )
            print("PASS keyboard first Tab reaches Skip to chapter")
        finally:
            browser.close()
    print("Browser smoke test only: no independent screen reader, 200% zoom, PDF tag or legal check.")


if __name__ == "__main__":
    main()
