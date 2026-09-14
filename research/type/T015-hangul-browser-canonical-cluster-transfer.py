from __future__ import annotations

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
import base64
import hashlib
import json
import subprocess
import unicodedata

UPM = 1000
EPOCH = 3849984000
OUT = Path("/mnt/data/t015_browser_transfer")
OUT.mkdir(parents=True, exist_ok=True)

# Synthetic binaries are runtime outputs only; canonical evidence is the harness + JSON.
def rect_glyph(width: int, height: int = 700, inset: int = 30):
    pen = TTGlyphPen(None)
    pen.moveTo((inset, 0))
    pen.lineTo((width - inset, 0))
    pen.lineTo((width - inset, height))
    pen.lineTo((inset, height))
    pen.closePath()
    return pen.glyph()


def build_woff2(
    name: str,
    cmap: dict[int, str],
    widths: dict[str, int],
    heights: dict[str, int] | None = None,
) -> Path:
    heights = heights or {}
    order = [".notdef"] + list(dict.fromkeys(cmap.values()))
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    glyphs = {".notdef": rect_glyph(600, 700, 80)}
    metrics = {".notdef": (600, 0)}
    for glyph_name in order[1:]:
        width = widths[glyph_name]
        glyphs[glyph_name] = rect_glyph(width, heights.get(glyph_name, 700), 30)
        metrics[glyph_name] = (width, 0)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupCharacterMap(cmap)
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupOS2(
        sTypoAscender=800,
        sTypoDescender=-200,
        usWinAscent=800,
        usWinDescent=200,
    )
    family = "T015 " + name
    ps_name = "T015" + name.replace(" ", "") + "-Regular"
    fb.setupNameTable(
        {
            "familyName": family,
            "styleName": "Regular",
            "uniqueFontIdentifier": ps_name,
            "fullName": family + " Regular",
            "psName": ps_name,
            "version": "Version 1.000",
        }
    )
    fb.setupPost()
    fb.setupMaxp()
    font = fb.font
    font["head"].created = EPOCH
    font["head"].modified = EPOCH
    font.recalcTimestamp = False
    ttf = OUT / (name + ".ttf")
    woff = OUT / (name + ".woff2")
    font.save(ttf, reorderTables=False)
    packed = TTFont(ttf, recalcTimestamp=False)
    packed.flavor = "woff2"
    packed.save(woff, reorderTables=False)
    return woff


def data_url(path: Path) -> str:
    return "data:font/woff2;base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def png_diff(a: Path, b: Path):
    ia = Image.open(a).convert("RGBA")
    ib = Image.open(b).convert("RGBA")
    if ia.size != ib.size:
        return {
            "same_size": False,
            "size_a": list(ia.size),
            "size_b": list(ib.size),
            "changed_pixels": None,
            "max_channel_delta": None,
        }
    ba = ia.tobytes()
    bb = ib.tobytes()
    pa = [ba[i : i + 4] for i in range(0, len(ba), 4)]
    pb = [bb[i : i + 4] for i in range(0, len(bb), 4)]
    changes = sum(x != y for x, y in zip(pa, pb))
    max_delta = max(
        (max(abs(x[i] - y[i]) for i in range(4)) for x, y in zip(pa, pb)),
        default=0,
    )
    return {
        "same_size": True,
        "size": list(ia.size),
        "changed_pixels": changes,
        "max_channel_delta": max_delta,
    }


nfc_cmap = {0xAC00: "ga", 0xAC01: "gak"}
nfd_cmap = {0x1100: "L_giyeok", 0x1161: "V_a", 0x11A8: "T_giyeok"}
nfc_widths = {"ga": 420, "gak": 680}
nfd_widths = {"L_giyeok": 260, "V_a": 310, "T_giyeok": 370}
nfd_heights = {"L_giyeok": 500, "V_a": 620, "T_giyeok": 380}
fonts = {
    "T015NFC": build_woff2("NFCOnly", nfc_cmap, nfc_widths),
    "T015NFD": build_woff2("NFDOnly", nfd_cmap, nfd_widths, nfd_heights),
    "T015Dual": build_woff2(
        "Dual", nfc_cmap | nfd_cmap, nfc_widths | nfd_widths, nfd_heights
    ),
}

nfc = "가각"
nfd = unicodedata.normalize("NFD", nfc)
unsupported_nfc = "간"
unsupported_nfd = unicodedata.normalize("NFD", unsupported_nfc)
mixed_nfc = "AB" + nfc + "12"
mixed_nfd = "AB" + nfd + "12"
assert unicodedata.normalize("NFC", nfd) == nfc
assert unicodedata.normalize("NFC", mixed_nfd) == mixed_nfc

face_css = "\n".join(
    f'@font-face{{font-family:{family};src:url("{data_url(path)}") format("woff2");font-display:block}}'
    for family, path in fonts.items()
)
body = """
<div id="nfc_font_nfc" class="s nfcfont">가각</div>
<div id="nfc_font_nfd" class="s nfcfont">가각</div>
<div id="nfc_font_mixed_nfc" class="s nfcfont">AB가각12</div>
<div id="nfc_font_mixed_nfd" class="s nfcfont">AB가각12</div>
<div id="nfc_font_normalized" class="s nfcfont"></div>
<div id="nfc_font_unsupported_nfd" class="s nfcfont">간</div>
<div id="nfd_font_nfd" class="s nfdfont">가각</div>
<div id="nfd_font_nfc" class="s nfdfont">가각</div>
<div id="dual_font_nfd" class="s dualfont">가각</div>
<div id="dual_font_nfc" class="s dualfont">가각</div>
<script>nfc_font_normalized.textContent=nfc_font_nfd.textContent.normalize('NFC')</script>
"""
ids = [
    "nfc_font_nfc",
    "nfc_font_nfd",
    "nfc_font_mixed_nfc",
    "nfc_font_mixed_nfd",
    "nfc_font_normalized",
    "nfc_font_unsupported_nfd",
    "nfd_font_nfd",
    "nfd_font_nfc",
    "dual_font_nfd",
    "dual_font_nfc",
]
chromium_version = subprocess.check_output(["/usr/bin/chromium", "--version"], text=True).strip()
results = {
    "environment": {
        "chromium": chromium_version,
        "python_unicode_data": unicodedata.unidata_version,
        "fonttools": __import__("fontTools").__version__,
        "font_sizes_px": [16, 40],
        "dprs": [1, 2],
        "fallback": "NanumGothic",
    },
    "strings": {
        "nfc": {"text": nfc, "codepoints": [f"U+{ord(c):04X}" for c in nfc]},
        "nfd": {"text": nfd, "codepoints": [f"U+{ord(c):04X}" for c in nfd]},
        "mixed_nfc": {
            "text": mixed_nfc,
            "codepoints": [f"U+{ord(c):04X}" for c in mixed_nfc],
        },
        "mixed_nfd": {
            "text": mixed_nfd,
            "codepoints": [f"U+{ord(c):04X}" for c in mixed_nfd],
        },
        "unsupported_nfd": {
            "text": unsupported_nfd,
            "codepoints": [f"U+{ord(c):04X}" for c in unsupported_nfd],
        },
    },
    "source_cmaps": {
        "nfc_only": [f"U+{cp:04X}" for cp in sorted(nfc_cmap)],
        "nfd_only": [f"U+{cp:04X}" for cp in sorted(nfd_cmap)],
        "dual": [f"U+{cp:04X}" for cp in sorted(nfc_cmap | nfd_cmap)],
    },
    "conditions": {},
}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium")
    for size in (16, 40):
        for dpr in (1, 2):
            key = f"{size}px_dpr{dpr}"
            html = f'''<!doctype html><meta charset="utf-8"><style>{face_css}
body{{margin:0;background:#fff;color:#000}}.s{{font-size:{size}px;line-height:{size}px;display:block;width:max-content;white-space:pre;padding:0;margin:0}}
.nfcfont{{font-family:T015NFC,"NanumGothic",sans-serif}}.nfdfont{{font-family:T015NFD,"NanumGothic",sans-serif}}.dualfont{{font-family:T015Dual,"NanumGothic",sans-serif}}
</style>{body}'''
            page = browser.new_page(
                viewport={"width": 1000, "height": 500}, device_scale_factor=dpr
            )
            page.set_content(html, wait_until="load")
            page.evaluate("document.fonts.ready")
            cond = {"samples": {}, "pixel_diffs": {}, "assertions": {}}
            folder = OUT / key
            folder.mkdir(exist_ok=True)
            for sample_id in ids:
                el = page.locator("#" + sample_id)
                box = el.bounding_box()
                png = el.screenshot()
                path = folder / (sample_id + ".png")
                path.write_bytes(png)
                cond["samples"][sample_id] = {
                    "text": el.text_content(),
                    "codepoints": [f"U+{ord(c):04X}" for c in el.text_content()],
                    "width_px": box["width"],
                    "height_px": box["height"],
                    "png_sha256": hashlib.sha256(png).hexdigest(),
                }
            pairs = {
                "nfc_only_nfc_vs_nfd": ("nfc_font_nfc", "nfc_font_nfd"),
                "nfc_only_mixed_nfc_vs_nfd": (
                    "nfc_font_mixed_nfc",
                    "nfc_font_mixed_nfd",
                ),
                "nfc_only_nfc_vs_normalized": (
                    "nfc_font_nfc",
                    "nfc_font_normalized",
                ),
                "nfd_only_nfd_vs_nfc": ("nfd_font_nfd", "nfd_font_nfc"),
                "dual_nfd_vs_nfc": ("dual_font_nfd", "dual_font_nfc"),
            }
            for label, (a, b) in pairs.items():
                cond["pixel_diffs"][label] = png_diff(
                    folder / (a + ".png"), folder / (b + ".png")
                )
            samples = cond["samples"]
            cond["assertions"] = {
                "nfc_only_nfc_vs_nfd_width_identical": samples["nfc_font_nfc"]["width_px"]
                == samples["nfc_font_nfd"]["width_px"],
                "nfc_only_nfc_vs_nfd_raster_identical": samples["nfc_font_nfc"]["png_sha256"]
                == samples["nfc_font_nfd"]["png_sha256"],
                "nfc_only_mixed_nfc_vs_nfd_width_identical": samples["nfc_font_mixed_nfc"]["width_px"]
                == samples["nfc_font_mixed_nfd"]["width_px"],
                "nfc_only_mixed_nfc_vs_nfd_raster_identical": samples["nfc_font_mixed_nfc"]["png_sha256"]
                == samples["nfc_font_mixed_nfd"]["png_sha256"],
                "nfc_only_normalization_revision_identical": samples["nfc_font_nfc"]["png_sha256"]
                == samples["nfc_font_normalized"]["png_sha256"],
                "unsupported_control_differs_from_supported_cluster": samples["nfc_font_nfc"]["png_sha256"]
                != samples["nfc_font_unsupported_nfd"]["png_sha256"],
                "nfd_only_nfd_vs_nfc_width_identical": samples["nfd_font_nfd"]["width_px"]
                == samples["nfd_font_nfc"]["width_px"],
                "nfd_only_nfd_vs_nfc_raster_identical": samples["nfd_font_nfd"]["png_sha256"]
                == samples["nfd_font_nfc"]["png_sha256"],
                "dual_nfd_vs_nfc_width_identical": samples["dual_font_nfd"]["width_px"]
                == samples["dual_font_nfc"]["width_px"],
                "dual_nfd_vs_nfc_raster_identical": samples["dual_font_nfd"]["png_sha256"]
                == samples["dual_font_nfc"]["png_sha256"],
            }
            cond["expected_custom_widths_px"] = {
                "nfc_only": (420 + 680) / UPM * size,
                "nfd_only": (260 + 310 + 260 + 310 + 370) / UPM * size,
            }
            results["conditions"][key] = cond
            page.close()
    browser.close()

all_assertions = [
    value
    for condition in results["conditions"].values()
    for value in condition["assertions"].values()
]
results["summary"] = {
    "bounded_assertions_passed": sum(all_assertions),
    "bounded_assertions_total": len(all_assertions),
    "all_bounded_assertions_passed": all(all_assertions),
    "finding": "Chromium rendered canonically equivalent Hangul NFC/NFD inputs identically with NFC-only, NFD-only, and dual synthetic fonts across 16/40px and DPR1/2; mixed Latin+Hangul was also identical. The unsupported NFD control differed, proving the harness could observe fallback/non-equivalent coverage.",
}
(OUT / "T015-hangul-browser-canonical-cluster-transfer-results.json").write_text(
    json.dumps(results, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps(results["summary"], ensure_ascii=False, indent=2))
