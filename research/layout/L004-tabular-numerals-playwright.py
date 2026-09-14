"""L004 Type→Layout transfer: tabular numerals in dense comparison surfaces.

Measures installed control fonts in Chromium. No font binaries are stored.
Outputs raw JSON to stdout; the committed summary records the controlled run.
"""
import asyncio, json
from playwright.async_api import async_playwright

FONTS = ["Inter", "Roboto", "Noto Sans"]
SIZES = [14, 16, 20, 32]
VALUES = ["+1111.11", "-8888.88", "+6060.60", "+1234.56", "-9876.54"]
DENSE_VALUES = ["$11,242.88", "$18,888.88", "$9,111.11", "$12,606.60"]

HTML = r'''<!doctype html><meta charset="utf-8"><style>
*{box-sizing:border-box}body{margin:0;padding:24px}.chars span{display:inline-block}
.table{width:360px;border:1px solid #999}.row{display:grid;grid-template-columns:minmax(0,1fr) 88px;gap:8px;align-items:center;border-bottom:1px solid #ddd;padding:4px 8px}.row:last-child{border-bottom:0}.num{text-align:right;white-space:nowrap;overflow:visible}.robust .row{grid-template-columns:minmax(0,1fr) max-content}.label{min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
</style><div id="root"></div>'''

async def main():
    out = {"study": "L004", "environment": {}, "fonts": {}, "dense_cell_16px": {}}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, executable_path="/usr/bin/chromium")
        page = await browser.new_page(viewport={"width": 1200, "height": 900})
        await page.set_content(HTML)
        out["environment"] = {
            "chromium": browser.version,
            "css_supports_tabular_nums": await page.evaluate("CSS.supports('font-variant-numeric','tabular-nums')"),
            "font_availability": {f: await page.evaluate("f=>document.fonts.check(`16px '${f}'`)", f) for f in FONTS},
        }

        for font in FONTS:
            out["fonts"][font] = {}
            for size in SIZES:
                result = {}
                for mode, variant in [("proportional", "proportional-nums"), ("tabular", "tabular-nums")]:
                    await page.evaluate("""([font,size,variant])=>{document.querySelector('#root').innerHTML=`<div id='t' class='chars' style=\"display:inline-block;white-space:nowrap;font-family:'${font}';font-size:${size}px;font-variant-numeric:${variant}\">${[0,1,2,3,4,5,6,7,8,9].map(x=>`<span>${x}</span>`).join('')}</div>`}""", [font, size, variant])
                    widths = await page.eval_on_selector_all("#t span", "els=>els.map(e=>e.getBoundingClientRect().width)")

                    rows = "".join(
                        f"<div class='numrow' style=\"font-family:'{font}';font-size:{size}px;font-variant-numeric:{variant};width:160px;text-align:right;white-space:nowrap\">"
                        + "".join(f"<span class='ch'>{c}</span>" for c in value)
                        + "</div>"
                        for value in VALUES
                    )
                    await page.evaluate("html=>document.querySelector('#root').innerHTML=html", rows)
                    decimals = await page.eval_on_selector_all(".numrow", """rows=>rows.map(r=>{const dot=[...r.querySelectorAll('.ch')].find(x=>x.textContent==='.');const rr=r.getBoundingClientRect(),dr=dot.getBoundingClientRect();return dr.left-rr.left;})""")
                    result[mode] = {
                        "digit_widths": widths,
                        "digit_spread": max(widths) - min(widths),
                        "decimal_x": decimals,
                        "decimal_spread": max(decimals) - min(decimals),
                    }
                out["fonts"][font][str(size)] = result

        for font in FONTS:
            out["dense_cell_16px"][font] = {}
            for mode, variant in [("proportional", "proportional-nums"), ("tabular", "tabular-nums")]:
                for policy in ["naive", "robust"]:
                    rows = "".join(
                        f"<div class='row'><div class='label'>Portfolio {i+1} long comparison label</div><div class='num' data-v='{v}'>{v}</div></div>"
                        for i, v in enumerate(DENSE_VALUES)
                    )
                    classes = "table robust" if policy == "robust" else "table"
                    html = f"<div class='{classes}' style=\"font-family:'{font}';font-size:16px;font-variant-numeric:{variant}\">{rows}</div>"
                    await page.evaluate("html=>document.querySelector('#root').innerHTML=html", html)
                    cells = await page.eval_on_selector_all(".num", """els=>els.map(e=>({value:e.dataset.v,width:e.getBoundingClientRect().width,scrollWidth:e.scrollWidth,clientWidth:e.clientWidth,overflow:e.scrollWidth>e.clientWidth+0.5}))""")
                    out["dense_cell_16px"][font][f"{mode}_{policy}"] = {
                        "cells": cells,
                        "overflow_count": sum(1 for x in cells if x["overflow"]),
                        "max_scroll_width": max(x["scrollWidth"] for x in cells),
                    }

        await browser.close()
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
