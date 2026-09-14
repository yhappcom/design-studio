import json
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "C009-type-color-rendering-specimen.html"
RESULTS = ROOT / "C009-type-color-rendering-results.json"
SAMPLES = [
    "latin-thin",
    "latin-regular",
    "latin-semibold",
    "ko-noto",
    "ko-nanum",
    "nums",
    "wrap-noto",
    "wrap-nanum",
]
CONDITIONS = [
    ("light-near", "#FFFFFF", "#767676"),
    ("light-strong", "#FFFFFF", "#595959"),
    ("dark-near", "#11161B", "#7A858E"),
    ("dark-strong", "#11161B", "#9CA6AE"),
]


def rgb(hex_color):
    h = hex_color.lstrip("#")
    return np.array([int(h[i : i + 2], 16) for i in (0, 2, 4)], dtype=float)


def srgb_to_linear(values):
    values = np.asarray(values, dtype=float) / 255.0
    return np.where(
        values <= 0.04045,
        values / 12.92,
        ((values + 0.055) / 1.055) ** 2.4,
    )


def luminance(values):
    r, g, b = srgb_to_linear(np.asarray(values, dtype=float))
    return float(0.2126 * r + 0.7152 * g + 0.0722 * b)


def contrast(a, b):
    l1, l2 = sorted([luminance(a), luminance(b)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def rendered_metrics(path, bg_hex, fg_hex):
    arr = np.asarray(Image.open(path).convert("RGB"), dtype=float)
    bg = rgb(bg_hex)
    fg = rgb(fg_hex)
    vector = fg - bg
    denominator = float(np.dot(vector, vector))

    diff = arr - bg
    alpha_proxy = np.clip((diff @ vector) / denominator, 0, 1)
    changed = np.linalg.norm(arr - bg, axis=2) > 1.5

    ys, xs = np.where(changed)
    if len(xs) == 0:
        raise RuntimeError("No rendered ink detected")

    x0, x1 = xs.min(), xs.max() + 1
    y0, y1 = ys.min(), ys.max() + 1
    a = alpha_proxy[y0:y1, x0:x1]
    changed_crop = changed[y0:y1, x0:x1]
    pixels = arr[y0:y1, x0:x1][changed_crop]

    bg_l = luminance(bg)
    pixel_l = np.array([luminance(pixel) for pixel in pixels])
    pixel_ratios = np.where(
        pixel_l >= bg_l,
        (pixel_l + 0.05) / (bg_l + 0.05),
        (bg_l + 0.05) / (pixel_l + 0.05),
    )

    return {
        "ink_bbox_px": [int(x0), int(y0), int(x1 - x0), int(y1 - y0)],
        "nonbg_pixel_count": int(changed_crop.sum()),
        "coverage_density_in_ink_bbox": float(a.sum() / a.size),
        "strong_core_share_bbox_alpha_ge_0_8": float((a >= 0.8).mean()),
        "pixel_contrast_median_nonbg": float(np.median(pixel_ratios)),
        "share_nonbg_pixels_contrast_ge_4_5": float((pixel_ratios >= 4.5).mean()),
    }


payload = {
    "method": {
        "alpha_proxy": (
            "Projection of encoded-RGB screenshot pixels between the declared "
            "background and foreground. This is a grayscale-antialiasing mixture "
            "diagnostic, not CSS opacity or physical-light mixing."
        ),
        "pixel_contrast": (
            "WCAG relative-luminance contrast calculated per already-composited "
            "screenshot pixel against the declared background. Diagnostic only: "
            "WCAG conformance uses declared foreground/background colors and permits "
            "anti-aliasing to be ignored."
        ),
        "scope": (
            "Single Chromium/Linux font environment at DPR 1 and 2. No human "
            "readability, cross-platform, physical-device, or production PASS."
        ),
    },
    "environment": {},
    "conditions": {},
}

with tempfile.TemporaryDirectory(prefix="c009-") as tmp, sync_playwright() as p:
    tmp = Path(tmp)
    for dpr in (1, 2):
        browser = p.chromium.launch(
            headless=True,
            executable_path="/usr/bin/chromium",
            args=["--no-sandbox"],
        )
        page = browser.new_page(
            viewport={"width": 1400, "height": 700},
            device_scale_factor=dpr,
        )
        page.set_content(HTML.read_text(encoding="utf-8"), wait_until="load")
        page.wait_for_timeout(100)

        if not payload["environment"]:
            payload["environment"] = {
                "chromium_executable": "/usr/bin/chromium",
                "chromium_version": browser.version,
                "viewport_css_px": [1400, 700],
                "dpr_values": [1, 2],
                "fonts_check": {
                    "Inter": page.evaluate("document.fonts.check('14px Inter')"),
                    "Noto Sans CJK KR": page.evaluate(
                        "document.fonts.check('14px \\\"Noto Sans CJK KR\\\"')"
                    ),
                    "NanumGothic": page.evaluate(
                        "document.fonts.check('14px NanumGothic')"
                    ),
                },
            }

        for name, bg_hex, fg_hex in CONDITIONS:
            page.evaluate(
                "([background, foreground]) => window.setColors(background, foreground)",
                [bg_hex, fg_hex],
            )
            page.wait_for_timeout(50)
            dom = page.evaluate("window.metrics()")
            key = f"{name}@dpr{dpr}"
            payload["conditions"][key] = {
                "background": bg_hex,
                "foreground": fg_hex,
                "nominal_contrast_ratio": contrast(rgb(bg_hex), rgb(fg_hex)),
                "samples": {},
            }

            for sample_id in SAMPLES:
                path = tmp / f"{key}-{sample_id}.png"
                page.locator(f"#{sample_id}").screenshot(path=str(path))
                payload["conditions"][key]["samples"][sample_id] = {
                    "dom": dom[sample_id],
                    "render": rendered_metrics(path, bg_hex, fg_hex),
                }

        browser.close()


def pick(condition, sample):
    item = payload["conditions"][condition]["samples"][sample]
    return {
        "dom_width": item["dom"]["width"],
        "dom_height": item["dom"]["height"],
        "font_family": item["dom"]["fontFamily"],
        "font_weight": item["dom"]["fontWeight"],
        **item["render"],
    }


summary = {
    "method": payload["method"],
    "environment": payload["environment"],
    "declared_pairs": {
        key: {
            "background": value["background"],
            "foreground": value["foreground"],
            "nominal_contrast_ratio": value["nominal_contrast_ratio"],
        }
        for key, value in payload["conditions"].items()
    },
    "weight_light_near_dpr1": {
        sample: pick("light-near@dpr1", sample)
        for sample in ("latin-thin", "latin-regular", "latin-semibold")
    },
    "weight_light_near_dpr2": {
        sample: pick("light-near@dpr2", sample)
        for sample in ("latin-thin", "latin-regular", "latin-semibold")
    },
    "color_margin_dpr1": {
        "near_regular": pick("light-near@dpr1", "latin-regular"),
        "strong_regular": pick("light-strong@dpr1", "latin-regular"),
        "near_thin": pick("light-near@dpr1", "latin-thin"),
        "strong_thin": pick("light-strong@dpr1", "latin-thin"),
        "dark_near_regular": pick("dark-near@dpr1", "latin-regular"),
        "dark_strong_regular": pick("dark-strong@dpr1", "latin-regular"),
    },
    "fallback_light_near_dpr1": {
        "noto": pick("light-near@dpr1", "ko-noto"),
        "nanum": pick("light-near@dpr1", "ko-nanum"),
    },
    "fallback_light_near_dpr2": {
        "noto": pick("light-near@dpr2", "ko-noto"),
        "nanum": pick("light-near@dpr2", "ko-nanum"),
    },
    "wrap_threshold_365px": {
        "noto_dpr1": pick("light-near@dpr1", "wrap-noto"),
        "nanum_dpr1": pick("light-near@dpr1", "wrap-nanum"),
        "noto_dpr2": pick("light-near@dpr2", "wrap-noto"),
        "nanum_dpr2": pick("light-near@dpr2", "wrap-nanum"),
    },
    "derived": {
        "light_near_dpr1_regular_to_thin_coverage_density_ratio": (
            pick("light-near@dpr1", "latin-regular")["coverage_density_in_ink_bbox"]
            / pick("light-near@dpr1", "latin-thin")["coverage_density_in_ink_bbox"]
        ),
        "light_near_dpr1_semibold_to_regular_coverage_density_ratio": (
            pick("light-near@dpr1", "latin-semibold")["coverage_density_in_ink_bbox"]
            / pick("light-near@dpr1", "latin-regular")["coverage_density_in_ink_bbox"]
        ),
        "light_near_dpr1_noto_to_nanum_coverage_density_ratio": (
            pick("light-near@dpr1", "ko-noto")["coverage_density_in_ink_bbox"]
            / pick("light-near@dpr1", "ko-nanum")["coverage_density_in_ink_bbox"]
        ),
    },
}

RESULTS.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print(RESULTS)
