"""W003 reproducible Chromium validation harness.

Run from repository root after installing Playwright and Chromium:
    python research/web/W003-responsive-recomposition-playwright.py

The harness intentionally distinguishes viewport-owned and container-owned
adaptation at the same viewport, then stresses narrow viewport, bilingual text,
focus/source sequence, and local table overflow. It writes measured evidence to
W003-responsive-recomposition-results.json; this source file alone is not PASS.
"""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "W003-responsive-recomposition-specimen.html"
OUT = ROOT / "W003-responsive-recomposition-results.json"

CASES = [
    ("wide", 1180, False),
    ("mid", 820, False),
    ("narrow", 390, False),
    ("narrow_long", 390, True),
]

LONG = "After-tax cumulative distributions and recovery status / 세후 누적 분배금과 원금 회수 상태를 비교하는 매우 긴 현지화 레이블"


def metrics(page, name):
    return page.evaluate("""(name) => {
      const q = s => document.querySelector(s);
      const qa = s => [...document.querySelectorAll(s)];
      const rect = e => e.getBoundingClientRect();
      const mainVO = q('section .viewport-owned');
      const asideVO = q('aside .viewport-owned');
      const mainCO = q('section .container-owned');
      const asideCO = q('aside .container-owned');
      const tw = q('.table-wrap');
      const focusables = qa('button,[tabindex="0"]').map(e => e.textContent.trim() || e.getAttribute('aria-label'));
      const cols = e => getComputedStyle(e).gridTemplateColumns.split(' ').filter(Boolean).length;
      return {
        name,
        viewport: innerWidth,
        document_scroll_width: document.documentElement.scrollWidth,
        main_viewport_owned_width: rect(mainVO).width,
        aside_viewport_owned_width: rect(asideVO).width,
        main_container_owned_width: rect(mainCO).width,
        aside_container_owned_width: rect(asideCO).width,
        main_viewport_owned_cols: cols(mainVO),
        aside_viewport_owned_cols: cols(asideVO),
        main_container_owned_cols: cols(mainCO),
        aside_container_owned_cols: cols(asideCO),
        table_client_width: tw.clientWidth,
        table_scroll_width: tw.scrollWidth,
        table_local_overflow: tw.scrollWidth > tw.clientWidth,
        focus_sequence: focusables,
        source_sequence: qa('button,[tabindex="0"]').map(e => e.outerHTML.slice(0,80)),
      };
    }""", name)


def main():
    results = {"engine": None, "cases": [], "assertions": []}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        results["engine"] = browser.version
        page = browser.new_page()
        html = HTML.read_text(encoding="utf-8")
        for name, width, long_text in CASES:
            page.set_viewport_size({"width": width, "height": 900})
            page.set_content(html, wait_until="load")
            if long_text:
                page.locator('.metric span').evaluate_all("(els, text) => els.forEach(e => e.textContent=text)", LONG)
            m = metrics(page, name)
            results["cases"].append(m)

            checks = {
                "document_fits_viewport": m["document_scroll_width"] <= width,
                "table_overflow_is_local": m["table_local_overflow"] and m["document_scroll_width"] <= width,
                "focus_source_sequence_stable": m["focus_sequence"] == ["Add transaction", "Export", "Compare portfolios", "More actions", "Transaction table, horizontally scrollable when needed"],
            }
            if name == "wide":
                checks["same_viewport_different_allocation"] = m["main_container_owned_width"] > m["aside_container_owned_width"]
                checks["container_query_recomposes_locally"] = m["main_container_owned_cols"] == 2 and m["aside_container_owned_cols"] == 1
                checks["viewport_rule_cannot_see_local_difference"] = m["main_viewport_owned_cols"] == m["aside_viewport_owned_cols"] == 2
            if name == "narrow":
                checks["page_global_media_recomposition"] = m["main_viewport_owned_cols"] == m["aside_viewport_owned_cols"] == 1
            for key, value in checks.items():
                results["assertions"].append({"case": name, "assertion": key, "pass": bool(value)})
        browser.close()

    results["summary"] = {
        "passed": sum(x["pass"] for x in results["assertions"]),
        "total": len(results["assertions"]),
        "all_pass": all(x["pass"] for x in results["assertions"]),
    }
    OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results["summary"], indent=2))


if __name__ == "__main__":
    main()
