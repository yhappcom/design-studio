"""L001 optical-centering raster validation.

This measures screenshot darkness centroids, not human perceived optical center.
The 48px hit target stays fixed; only the visual child is translated.
"""
from __future__ import annotations

import json, math
from io import BytesIO
from pathlib import Path

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

CHROMIUM = "/usr/bin/chromium"
TARGET = 48
SIZES = [16, 24, 32, 40]
DPRS = [1, 2]
OUT = Path("L001-optical-centering-results-raw.json")

SHAPES = {
    "play": '<polygon points="7,4 19,12 7,20" fill="black"/>',
    "chevron": '<polyline points="8,5 15,12 8,19" fill="none" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "send": '<polygon points="4,5 21,12 4,19 8.5,12" fill="black"/>',
    "asym_mark": '<path d="M5 5 H13 V9 H19 V19 H9 V15 H5 Z" fill="black"/>',
    "badge_object": '<circle cx="11" cy="13" r="7" fill="black"/><circle cx="18.5" cy="5.5" r="3.2" fill="black"/>',
    "bookmark": '<path d="M7 4 H17 V21 L12 17 L7 21 Z" fill="black"/>',
}

BASE = '''<!doctype html><style>
*{box-sizing:border-box}body{margin:0;background:#fff}.target{width:48px;height:48px;display:grid;place-items:center}.visual{width:Spx;height:Spx}svg{display:block;width:100%;height:100%}
</style><div class=target><div class=visual><svg viewBox="0 0 24 24">SHAPE</svg></div></div>'''


def darkness_centroid(png: bytes):
    arr = np.asarray(Image.open(BytesIO(png)).convert("L"), dtype=float)
    weight = 255 - arr
    total = weight.sum()
    y, x = np.indices(weight.shape)
    return float((x*weight).sum()/total), float((y*weight).sum()/total), float(total/255)


def measure(page, dpr: int, ox: int, oy: int):
    page.eval_on_selector(
        ".visual",
        '(e,v)=>e.style.transform=`translate(${v[0]}px,${v[1]}px)`',
        [ox, oy],
    )
    cx, cy, ink = darkness_centroid(page.screenshot())
    # The screenshot centroid uses device-pixel sample centers. Remove the half-pixel term
    # before converting to CSS-pixel error around the 48px target center.
    center = 24*dpr - .5
    ex, ey = (cx-center)/dpr, (cy-center)/dpr
    return {
        "offset_x_css": ox,
        "offset_y_css": oy,
        "err_x_css": ex,
        "err_y_css": ey,
        "err_radius_css": math.hypot(ex, ey),
        "ink_equivalent_css_px": ink/(dpr*dpr),
    }


def main():
    out = {
        "study": "L001 optical-centering raster validation",
        "target_css_px": TARGET,
        "method": "darkness-weighted screenshot centroid; rounded correction only",
        "shapes": {},
    }
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=CHROMIUM)
        out["chromium"] = browser.version
        for name, svg in SHAPES.items():
            out["shapes"][name] = {}
            for size in SIZES:
                out["shapes"][name][str(size)] = {}
                for dpr in DPRS:
                    page = browser.new_page(
                        viewport={"width": TARGET, "height": TARGET},
                        device_scale_factor=dpr,
                    )
                    page.set_content(BASE.replace("Spx", f"{size}px").replace("SHAPE", svg))
                    zero = measure(page, dpr, 0, 0)
                    ox = int(round(-zero["err_x_css"]))
                    oy = int(round(-zero["err_y_css"]))
                    corrected = measure(page, dpr, ox, oy)
                    out["shapes"][name][str(size)][f"dpr{dpr}"] = {
                        "zero": zero,
                        "rounded_candidate": corrected,
                    }
                    page.close()
        browser.close()
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
