"""L005 fixed-geometry Color -> Layout transfer harness.

Purpose
- hold DOM/content/geometry constant;
- vary only color-token assignments;
- render in Chromium;
- verify geometry equality;
- calculate simple image-feature proxies in OKLab plus bounded contrast checks.

Important: these proxies are NOT Rosenholtz Feature Congestion and are NOT human
perceived-complexity/search-performance evidence.
"""
from __future__ import annotations

import json
from io import BytesIO
from pathlib import Path

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

CHROMIUM = "/usr/bin/chromium"
OUT = Path("L005-color-density-salience-results-summary.json")
VIEWPORT = {"width": 1280, "height": 900}

VARIANTS = {
    "neutral_minimal": {
        "--canvas": "#F7F9FA", "--surface": "#FFFFFF", "--row-alt": "#FFFFFF",
        "--border": "#C8D0D6", "--text": "#152028", "--secondary": "#52616B",
        "--selected": "#F1F4F5", "--action": "#344054", "--actionText": "#FFFFFF",
        "--positive": "#344054", "--negative": "#344054", "--successBg": "#F3F5F6",
        "--successFg": "#344054", "--reviewBg": "#F3F5F6", "--reviewFg": "#344054",
        "--pausedBg": "#F3F5F6", "--pausedFg": "#344054", "--focus": "#344054",
    },
    "role_separated": {
        "--canvas": "#F7F9FA", "--surface": "#FFFFFF", "--row-alt": "#FFFFFF",
        "--border": "#7D8C97", "--text": "#152028", "--secondary": "#52616B",
        "--selected": "#E7F8F6", "--action": "#155EEF", "--actionText": "#FFFFFF",
        "--positive": "#167A4B", "--negative": "#B42318", "--successBg": "#EAF7F0",
        "--successFg": "#167A4B", "--reviewBg": "#FFF4D6", "--reviewFg": "#7A5300",
        "--pausedBg": "#FDECEA", "--pausedFg": "#9A271D", "--focus": "#1D4ED8",
    },
    "chroma_overloaded": {
        "--canvas": "#F7F9FA", "--surface": "#FFFFFF", "--row-alt": "#FFF3FB",
        "--border": "#8C6AE8", "--text": "#152028", "--secondary": "#7D3C98",
        "--selected": "#DDFBF6", "--action": "#6F42C1", "--actionText": "#FFFFFF",
        "--positive": "#00A36C", "--negative": "#E63973", "--successBg": "#D7F8E9",
        "--successFg": "#006B48", "--reviewBg": "#FFF0B8", "--reviewFg": "#805D00",
        "--pausedBg": "#FFD8E5", "--pausedFg": "#9B1B4C", "--focus": "#FF7A00",
    },
    "luminance_overloaded": {
        "--canvas": "#FFFFFF", "--surface": "#E8E8E8", "--row-alt": "#CFCFCF",
        "--border": "#3F3F3F", "--text": "#111111", "--secondary": "#2F2F2F",
        "--selected": "#B8B8B8", "--action": "#1A1A1A", "--actionText": "#FFFFFF",
        "--positive": "#111111", "--negative": "#111111", "--successBg": "#EFEFEF",
        "--successFg": "#111111", "--reviewBg": "#BDBDBD", "--reviewFg": "#111111",
        "--pausedBg": "#6E6E6E", "--pausedFg": "#FFFFFF", "--focus": "#000000",
    },
    "semantic_collision": {
        "--canvas": "#F7F9FA", "--surface": "#FFFFFF", "--row-alt": "#FFFFFF",
        "--border": "#70B9B1", "--text": "#152028", "--secondary": "#52616B",
        "--selected": "#D8F5F1", "--action": "#0F766E", "--actionText": "#FFFFFF",
        "--positive": "#0F766E", "--negative": "#B42318", "--successBg": "#D8F5F1",
        "--successFg": "#116F66", "--reviewBg": "#E8F7F5", "--reviewFg": "#116F66",
        "--pausedBg": "#FDECEA", "--pausedFg": "#9A271D", "--focus": "#0F766E",
    },
}

ROWS = [
    ["Alpha Income Portfolio", "Active", "$12,884", "+3.8%"],
    ["Global Yield Strategy", "Review", "$8,104", "-1.2%"],
    ["Long Duration Income Basket", "Active", "$18,220", "+0.6%"],
    ["Technology Enhanced Income", "Active", "$14,052", "+2.4%"],
    ["Monthly Distribution Core", "Paused", "$9,994", "-0.4%"],
    ["International Covered Call", "Active", "$11,242", "+1.8%"],
    ["High Volatility Income Sleeve", "Review", "$7,880", "-3.1%"],
    ["Retirement Income Stability", "Active", "$16,530", "+0.2%"],
    ["Tactical Opportunity Basket", "Active", "$10,402", "+4.9%"],
    ["Capital Recovery Monitor", "Review", "$6,884", "-0.9%"],
    ["Long-Term Reinvestment Plan", "Active", "$13,290", "+1.1%"],
    ["Tax Adjustment Watchlist", "Active", "$5,960", "+0.1%"],
]

HTML = r'''<!doctype html><meta charset="utf-8"><style>
*{box-sizing:border-box}:root{font-family:Arial,sans-serif;font-size:16px}body{margin:0;background:var(--canvas);color:var(--text)}
.app{width:1120px;margin:24px auto;padding:20px;background:var(--surface);border:1px solid var(--border)}
.toolbar{display:flex;gap:10px;align-items:center;margin-bottom:18px}.title{font-weight:700;font-size:20px;margin-right:auto}
button{font:inherit}.toolbar button,.open{background:var(--action);color:var(--actionText);border:2px solid var(--border);border-radius:6px}.toolbar button{height:44px;padding:0 14px}.open{height:40px}.toolbar button:focus,.open:focus{outline:3px solid var(--focus);outline-offset:2px}
.summary{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:18px}.card{min-height:76px;border:1px solid var(--border);padding:12px;background:var(--surface)}.label{font-size:13px;color:var(--secondary)}.big{font-size:22px;font-weight:700;margin-top:6px}
.table{border:1px solid var(--border)}.row{display:grid;grid-template-columns:2fr .8fr .8fr .65fr 90px;gap:10px;align-items:center;min-height:54px;padding:6px 10px;border-bottom:1px solid var(--border);background:var(--surface)}.row:nth-child(even){background:var(--row-alt)}.row.selected{background:var(--selected);border-left:4px solid var(--focus);padding-left:7px}.row:last-child{border-bottom:0}.head{font-weight:700;min-height:44px;background:var(--surface)!important}
.status{display:inline-flex;align-items:center;justify-content:center;min-height:30px;padding:4px 8px;border-radius:999px;font-weight:650}.active{background:var(--successBg);color:var(--successFg)}.review{background:var(--reviewBg);color:var(--reviewFg)}.paused{background:var(--pausedBg);color:var(--pausedFg)}.metric,.change{text-align:right;font-variant-numeric:tabular-nums}.pos{color:var(--positive);font-weight:700}.neg{color:var(--negative);font-weight:700}
</style><body><main class=app><div class=toolbar><div class=title>Portfolio comparison</div><button>Filter</button><button>Sort</button></div><section class=summary><div class=card><div class=label>Total value</div><div class=big>$128,442</div></div><div class=card><div class=label>Monthly income</div><div class=big>$2,184</div></div><div class=card><div class=label>Recovery</div><div class=big>38.4%</div></div></section><section class=table><div class="row head"><div>Name</div><div>Status</div><div style="text-align:right">Value</div><div style="text-align:right">Change</div><div></div></div><div id=rows></div></section></main><script>
const data=__ROWS__;rows.innerHTML=data.map((r,i)=>`<div class="row ${i===5?'selected':''}"><div>${r[0]}</div><div><span class="status ${r[1]==='Active'?'active':r[1]==='Review'?'review':'paused'}">${r[1]}</span></div><div class=metric>${r[2]}</div><div class="change ${r[3].startsWith('+')?'pos':'neg'}">${r[3]}</div><button class=open>Open</button></div>`).join('');
window.geom=()=>[...document.querySelectorAll('.app,.toolbar,.summary,.card,.table,.row,.status,.open')].map((e,i)=>{const r=e.getBoundingClientRect();return[e.className||e.tagName,i,+r.x.toFixed(2),+r.y.toFixed(2),+r.width.toFixed(2),+r.height.toFixed(2)]});
</script>'''.replace("__ROWS__", json.dumps(ROWS))


def srgb_to_oklab(rgb8: np.ndarray):
    rgb = rgb8 / 255.0
    lin = np.where(rgb <= .04045, rgb / 12.92, ((rgb + .055) / 1.055) ** 2.4)
    r, g, b = lin[..., 0], lin[..., 1], lin[..., 2]
    l = .4122214708*r + .5363325363*g + .0514459929*b
    m = .2119034982*r + .6806995451*g + .1073969566*b
    s = .0883024619*r + .2817188376*g + .6299787005*b
    l_, m_, s_ = np.cbrt(l), np.cbrt(m), np.cbrt(s)
    L = .2104542553*l_ + .7936177850*m_ - .0040720468*s_
    a = 1.9779984951*l_ - 2.4285922050*m_ + .4505937099*s_
    bb = .0259040371*l_ + .7827717662*m_ - .8086757660*s_
    return L, np.sqrt(a*a + bb*bb)


def analyze_png(png: bytes):
    arr = np.asarray(Image.open(BytesIO(png)).convert("RGB"))
    L, C = srgb_to_oklab(arr)
    gx, gy = np.abs(np.diff(L, 1)), np.abs(np.diff(L, 0))
    cx, cy = np.abs(np.diff(C, 1)), np.abs(np.diff(C, 0))
    return {
        "L_mean": float(L.mean()), "L_std": float(L.std()),
        "C_mean": float(C.mean()), "C_std": float(C.std()),
        "high_chroma_fraction_C_gt_0_06": float((C > .06).mean()),
        "high_chroma_fraction_C_gt_0_10": float((C > .10).mean()),
        "luminance_gradient_mean": float((gx.mean()+gy.mean())/2),
        "chroma_gradient_mean": float((cx.mean()+cy.mean())/2),
    }


def relative_luminance(value: str):
    vals = [int(value[i:i+2], 16)/255 for i in (1,3,5)]
    vals = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in vals]
    return .2126*vals[0] + .7152*vals[1] + .0722*vals[2]


def contrast(a: str, b: str):
    x, y = relative_luminance(a), relative_luminance(b)
    return (max(x, y)+.05)/(min(x, y)+.05)


def main():
    out = {"study":"L005", "viewport":[1280,900], "variants":{}}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=CHROMIUM)
        page = browser.new_page(viewport=VIEWPORT, device_scale_factor=1)
        page.set_content(HTML)
        out["chromium"] = browser.version
        base_geometry = None
        for name, t in VARIANTS.items():
            page.evaluate("t=>{for(const[k,v]of Object.entries(t))document.documentElement.style.setProperty(k,v)}", t)
            page.evaluate("document.body.offsetHeight")
            geom = page.evaluate("geom()")
            if base_geometry is None: base_geometry = geom
            m = analyze_png(page.screenshot(full_page=False))
            m["token_unique_values"] = len(set(t.values()))
            pairs = {
                "text_surface": contrast(t["--text"], t["--surface"]),
                "secondary_surface": contrast(t["--secondary"], t["--surface"]),
                "action_text_surface": contrast(t["--actionText"], t["--action"]),
                "active_status": contrast(t["--successFg"], t["--successBg"]),
                "review_status": contrast(t["--reviewFg"], t["--reviewBg"]),
                "paused_status": contrast(t["--pausedFg"], t["--pausedBg"]),
            }
            out["variants"][name] = {
                "metrics": m,
                "contrast_ratios": pairs,
                "min_declared_text_contrast": min(pairs.values()),
                "geometry_matches_base": geom == base_geometry,
            }
        out["geometry_equal"] = all(v["geometry_matches_base"] for v in out["variants"].values())
        browser.close()
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
