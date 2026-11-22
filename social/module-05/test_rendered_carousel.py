#!/usr/bin/env python3
"""Automated rendered reflow smoke test for the unpublished Module 05 HTML carousel.

Requires Playwright Chromium. This is *not* a screen-reader, contrast or tagged-PDF
audit and cannot close Module 04 or Module 05 independent accessibility gates.
"""
from __future__ import annotations

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "social/module-05/CAROUSEL.html"


def main() -> None:
    assert HTML.is_file(), "Unpublished question-deck HTML missing"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.route(
                "**/*",
                lambda route: route.continue_()
                if route.request.url.startswith("file:") else route.abort()
            )
            for width in (1280, 390, 320):
                page.set_viewport_size({"width": width, "height": 900})
                page.goto(HTML.resolve().as_uri(), wait_until="load")
                assert page.locator("section.slide").count() == 8
                result = page.evaluate(
                    """() => {
                      const viewport = document.documentElement.clientWidth;
                      const pageWidth = document.documentElement.scrollWidth;
                      const offenders = [];
                      document.querySelectorAll('section.slide').forEach((slide, index) => {
                        const container = slide.getBoundingClientRect();
                        const textNodes = slide.querySelectorAll(
                          'h2, p, .ask, .graph, .juris, .warning, .check-list, .footer'
                        );
                        textNodes.forEach(node => {
                          const r = node.getBoundingClientRect();
                          if (r.right > container.right + 2 ||
                              r.left < container.left - 2 ||
                              r.bottom > container.bottom + 2 ||
                              r.top < container.top - 2) {
                            offenders.push({
                              slide: index + 1,
                              selector: node.tagName.toLowerCase() +
                                (node.className ? '.' + String(node.className).replaceAll(' ', '.') : ''),
                              top: Math.round(r.top), bottom: Math.round(r.bottom),
                              slideBottom: Math.round(container.bottom)
                            });
                          }
                        });
                      });
                      return {viewport, pageWidth, offenders};
                    }"""
                )
                assert result["pageWidth"] <= result["viewport"] + 1, (
                    f"{width}px: horizontal scrolling: {result}"
                )
                assert not result["offenders"], (
                    f"{width}px: learner content clipped by slide: {result['offenders']}"
                )
                print(f"PASS {width}px: eight slides with no measured content clipping or horizontal scroll")

            page.set_viewport_size({"width": 1280, "height": 900})
            page.goto(HTML.resolve().as_uri(), wait_until="load")
            page.keyboard.press("Tab")
            focus = page.evaluate(
                """() => {
                  const target = document.activeElement;
                  const style = getComputedStyle(target);
                  return {
                    tag: target.tagName,
                    outline: style.outlineStyle,
                    width: parseFloat(style.outlineWidth) || 0,
                    label: (target.textContent || '').trim()
                  };
                }"""
            )
            assert focus["tag"] in ("A", "BUTTON"), f"Tab did not reach a link or control: {focus}"
            assert focus["outline"] != "none" and focus["width"] >= 2, (
                f"Keyboard focus not visibly outlined: {focus}"
            )
            print("PASS keyboard Tab focus: visible 2px+ outline")
        finally:
            browser.close()
    print("Automated Chromium checks only. Manual zoom/AT/PDF reading-order review NOT COMPLETED.")


if __name__ == "__main__":
    main()
