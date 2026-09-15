"""W003 reproducible Chromium validation harness.

Run from repository root after installing Playwright and Chromium:
    python research/web/W003-responsive-recomposition-playwright.py

The harness distinguishes viewport-owned and container-owned adaptation at the
same viewport, then stresses narrow viewport, bilingual text, focus/source
sequence, and local table overflow. It writes measured evidence to
W003-responsive-recomposition-results.json; this source file alone is not PASS.
"""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "W003-responsive-recomposition-specimen.html"
OUT = ROOT / "W003-responsive-recomposition-results.json"
CASES = [("wide",1180,False),("mid",820,False),("narrow",390,False),("narrow_long",390,True)]
LONG = "After-tax cumulative distributions and recovery status / 세후 누적 분배금과 원금 회수 상태를 비교하는 매우 긴 현지화 레이블"
EXPECTED_FOCUS = ["Add transaction","Export","Compare portfolios","More actions","Transaction table, horizontally scrollable when needed"]


def metrics(page, name):
    return page.evaluate("""(name) => {
      const q=s=>document.querySelector(s), qa=s=>[...document.querySelectorAll(s)];
      const mainVO=q('section .viewport-owned'), asideVO=q('aside .viewport-owned');
      const mainCO=q('section .container-owned'), asideCO=q('aside .container-owned'), tw=q('.table-wrap');
      const cols=e=>getComputedStyle(e).gridTemplateColumns.split(' ').filter(Boolean).length;
      const label=e=>e.getAttribute('aria-label') || e.textContent.trim();
      return {name,viewport:innerWidth,document_scroll_width:document.documentElement.scrollWidth,
        main_viewport_owned_width:mainVO.getBoundingClientRect().width,aside_viewport_owned_width:asideVO.getBoundingClientRect().width,
        main_container_owned_width:mainCO.getBoundingClientRect().width,aside_container_owned_width:asideCO.getBoundingClientRect().width,
        main_viewport_owned_cols:cols(mainVO),aside_viewport_owned_cols:cols(asideVO),main_container_owned_cols:cols(mainCO),aside_container_owned_cols:cols(asideCO),
        table_client_width:tw.clientWidth,table_scroll_width:tw.scrollWidth,table_local_overflow:tw.scrollWidth>tw.clientWidth,
        focus_sequence:qa('button,[tabindex="0"]').map(label)};
    }""", name)


def main():
    results={"engine":None,"cases":[],"assertions":[]}
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True); results["engine"]=browser.version; page=browser.new_page(); html=HTML.read_text(encoding="utf-8")
        for name,width,long_text in CASES:
            page.set_viewport_size({"width":width,"height":900}); page.set_content(html,wait_until="load")
            if long_text: page.locator('.metric span').evaluate_all("(els,text)=>els.forEach(e=>e.textContent=text)",LONG)
            m=metrics(page,name); results["cases"].append(m)
            checks={"document_fits_viewport":m["document_scroll_width"]<=width,"table_overflow_is_local":m["table_local_overflow"] and m["document_scroll_width"]<=width,"focus_source_sequence_stable":m["focus_sequence"]==EXPECTED_FOCUS}
            if name=="wide": checks.update({"same_viewport_different_allocation":m["main_container_owned_width"]>m["aside_container_owned_width"],"container_query_recomposes_locally":m["main_container_owned_cols"]==2 and m["aside_container_owned_cols"]==1,"viewport_rule_cannot_see_local_difference":m["main_viewport_owned_cols"]==m["aside_viewport_owned_cols"]==2})
            if name=="narrow": checks["page_global_media_recomposition"]=m["main_viewport_owned_cols"]==m["aside_viewport_owned_cols"]==1
            results["assertions"].extend({"case":name,"assertion":k,"pass":bool(v)} for k,v in checks.items())
        browser.close()
    results["summary"]={"passed":sum(x["pass"] for x in results["assertions"]),"total":len(results["assertions"]),"all_pass":all(x["pass"] for x in results["assertions"])}
    OUT.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8"); print(json.dumps(results["summary"],indent=2))

if __name__=="__main__": main()
