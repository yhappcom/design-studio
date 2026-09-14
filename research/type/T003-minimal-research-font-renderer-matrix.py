"""T003 reproducible research-font and FreeType renderer experiment.

Research only. This does not produce a production font.

Dependencies:
    fontTools
    freetype-py
    Pillow
    numpy

Outputs when run locally:
    T003-MinimalResearch.ttf
    T003-MinimalResearch.ttx
    T003-results.json
    PNG glyph samples for the renderer matrix

The experiment preserves the T002 R0/R1 lowercase-n contour difference while
placing both into one minimal quadratic TrueType font with identical source
advance widths. R1 is mapped to U+E000 solely for research comparison.
"""

from __future__ import annotations

import json
from pathlib import Path

import freetype
import numpy as np
from PIL import Image
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

UPM = 1000
OUT_DIR = Path(".")
FONT_PATH = OUT_DIR / "T003-MinimalResearch.ttf"
TTX_PATH = OUT_DIR / "T003-MinimalResearch.ttx"
RESULTS_PATH = OUT_DIR / "T003-results.json"


def empty_glyph():
    return TTGlyphPen(None).glyph()


def rectangle(x0: int, y0: int, x1: int, y1: int):
    pen = TTGlyphPen(None)
    pen.moveTo((x0, y0))
    pen.lineTo((x1, y0))
    pen.lineTo((x1, y1))
    pen.lineTo((x0, y1))
    pen.closePath()
    return pen.glyph()


def exercise_point(x: float, y: float) -> tuple[float, float]:
    """Map Exercise 002 SVG coordinates into a 1000 UPM font space.

    Exercise 002 lowercase uses y=650..900 as x-height-to-baseline. We map that
    250-unit interval to a 500-unit x-height and reverse SVG's downward y axis.
    """
    return ((x - 100) * 2, (900 - y) * 2)


def n_glyph(version: str):
    pen = TTGlyphPen(None)

    # Shared 76-unit stem; x-height is 500.
    pen.moveTo((40, 0))
    pen.lineTo((116, 0))
    pen.lineTo((116, 500))
    pen.lineTo((40, 500))
    pen.closePath()

    # Preserve the cubic study geometry, then convert to TrueType quadratics.
    q = Cu2QuPen(pen, max_err=0.6, reverse_direction=False)
    p = exercise_point

    if version == "R0":
        q.moveTo(p(158, 735))
        q.curveTo(p(200, 668), p(295, 666), p(328, 736))
        q.curveTo(p(338, 757), p(341, 785), p(341, 820))
        q.lineTo(p(341, 900))
        q.lineTo(p(303, 900))
        q.lineTo(p(303, 810))
        q.curveTo(p(303, 743), p(280, 712), p(237, 712))
        q.curveTo(p(194, 712), p(158, 750), p(158, 815))
        q.closePath()
    elif version == "R1":
        q.moveTo(p(158, 748))
        q.curveTo(p(196, 684), p(288, 677), p(327, 739))
        q.curveTo(p(338, 758), p(341, 787), p(341, 820))
        q.lineTo(p(341, 900))
        q.lineTo(p(303, 900))
        q.lineTo(p(303, 810))
        q.curveTo(p(303, 750), p(280, 715), p(238, 715))
        q.curveTo(p(198, 715), p(170, 746), p(158, 795))
        q.closePath()
    else:
        raise ValueError(version)

    return pen.glyph()


def ellipse_glyph(cx, cy, rx, ry, inner_rx, inner_ry):
    """Simple control ellipse with a reversed inner contour."""
    k = 0.5522847498
    pen = TTGlyphPen(None)
    q = Cu2QuPen(pen, max_err=0.6, reverse_direction=False)

    q.moveTo((cx + rx, cy))
    q.curveTo((cx + rx, cy + k * ry), (cx + k * rx, cy + ry), (cx, cy + ry))
    q.curveTo((cx - k * rx, cy + ry), (cx - rx, cy + k * ry), (cx - rx, cy))
    q.curveTo((cx - rx, cy - k * ry), (cx - k * rx, cy - ry), (cx, cy - ry))
    q.curveTo((cx + k * rx, cy - ry), (cx + rx, cy - k * ry), (cx + rx, cy))
    q.closePath()

    q.moveTo((cx + inner_rx, cy))
    q.curveTo((cx + inner_rx, cy - k * inner_ry), (cx + k * inner_rx, cy - inner_ry), (cx, cy - inner_ry))
    q.curveTo((cx - k * inner_rx, cy - inner_ry), (cx - inner_rx, cy - k * inner_ry), (cx - inner_rx, cy))
    q.curveTo((cx - inner_rx, cy + k * inner_ry), (cx - k * inner_rx, cy + inner_ry), (cx, cy + inner_ry))
    q.curveTo((cx + k * inner_rx, cy + inner_ry), (cx + inner_rx, cy + k * inner_ry), (cx + inner_rx, cy))
    q.closePath()
    return pen.glyph()


def build_font(path: Path) -> None:
    glyphs = {
        ".notdef": rectangle(50, 0, 450, 700),
        "space": empty_glyph(),
        "n": n_glyph("R0"),
        "n.alt": n_glyph("R1"),
        "O": ellipse_glyph(300, 350, 250, 370, 165, 285),
        "o": ellipse_glyph(260, 250, 210, 265, 135, 190),
    }

    h_pen = TTGlyphPen(None)
    for x0, x1 in ((60, 140), (460, 540)):
        h_pen.moveTo((x0, 0))
        h_pen.lineTo((x1, 0))
        h_pen.lineTo((x1, 700))
        h_pen.lineTo((x0, 700))
        h_pen.closePath()
    h_pen.moveTo((60, 310))
    h_pen.lineTo((540, 310))
    h_pen.lineTo((540, 390))
    h_pen.lineTo((60, 390))
    h_pen.closePath()
    glyphs["H"] = h_pen.glyph()

    order = [".notdef", "space", "H", "O", "n", "n.alt", "o"]
    metrics = {
        ".notdef": (500, 50),
        "space": (300, 0),
        "H": (600, 60),
        "O": (600, 50),
        "n": (560, 40),
        "n.alt": (560, 40),
        "o": (520, 50),
    }

    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap({
        0x20: "space",
        0x48: "H",
        0x4F: "O",
        0x6E: "n",
        0x6F: "o",
        0xE000: "n.alt",  # research-only mapping
    })
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=800, descent=-200, lineGap=0)
    fb.setupOS2(
        sTypoAscender=800,
        sTypoDescender=-200,
        sTypoLineGap=0,
        usWinAscent=850,
        usWinDescent=250,
        sxHeight=500,
        sCapHeight=700,
        usWeightClass=400,
        usWidthClass=5,
    )
    fb.setupNameTable({
        "familyName": "T003 Minimal Research",
        "styleName": "Regular",
        "uniqueFontIdentifier": "T003 Minimal Research Regular 20260914",
        "fullName": "T003 Minimal Research Regular",
        "psName": "T003-MinimalResearch-Regular",
        "version": "Version 0.001",
    })
    fb.setupPost()
    fb.setupMaxp()
    fb.save(path)


def bitmap_array(bitmap) -> np.ndarray:
    if bitmap.rows == 0 or bitmap.width == 0:
        return np.zeros((1, 1), dtype=np.uint8)
    raw = np.array(bitmap.buffer, dtype=np.uint8).reshape((bitmap.rows, bitmap.pitch))
    return raw[:, : bitmap.width]


def render(face, charcode: int, ppem: int, flags: int):
    face.set_pixel_sizes(0, ppem)
    face.load_char(chr(charcode), flags)
    slot = face.glyph
    arr = bitmap_array(slot.bitmap)
    c_slot = slot._FT_GlyphSlot.contents

    return arr, {
        "width": slot.bitmap.width,
        "rows": slot.bitmap.rows,
        "left": slot.bitmap_left,
        "top": slot.bitmap_top,
        "advance": slot.advance.x / 64.0,
        "linear_advance": slot.linearHoriAdvance / 65536.0,
        "lsb_delta": c_slot.lsb_delta / 64.0,
        "rsb_delta": c_slot.rsb_delta / 64.0,
    }


def main() -> None:
    build_font(FONT_PATH)

    # XML round-trip source snapshot for inspectable table/glyph data.
    font = TTFont(FONT_PATH)
    font.saveXML(TTX_PATH)

    modes = {
        "no-hint": freetype.FT_LOAD_RENDER | freetype.FT_LOAD_NO_HINTING | freetype.FT_LOAD_TARGET_NORMAL,
        "autohint-normal": freetype.FT_LOAD_RENDER | freetype.FT_LOAD_FORCE_AUTOHINT | freetype.FT_LOAD_TARGET_NORMAL,
        "autohint-light": freetype.FT_LOAD_RENDER | freetype.FT_LOAD_FORCE_AUTOHINT | freetype.FT_LOAD_TARGET_LIGHT,
    }

    face = freetype.Face(str(FONT_PATH))
    results = []

    for ppem in (14, 16, 24, 48):
        for mode, flags in modes.items():
            for label, charcode in (("R0", 0x006E), ("R1", 0xE000)):
                arr, metrics = render(face, charcode, ppem, flags)
                record = {
                    "ppem": ppem,
                    "mode": mode,
                    "glyph": label,
                    "coverage_pixel_equivalent": round(float(arr.sum() / 255.0), 3),
                    "strong_pixels_gte_128": int((arr >= 128).sum()),
                    "nonzero_pixels": int((arr > 0).sum()),
                    **metrics,
                }
                results.append(record)
                Image.fromarray(255 - arr, mode="L").save(
                    OUT_DIR / f"T003-{ppem}-{mode}-{label}.png"
                )

    RESULTS_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")

    # Basic inspectability report.
    inspected = TTFont(FONT_PATH)
    print("UPM", inspected["head"].unitsPerEm)
    print("xHeight", inspected["OS/2"].sxHeight)
    for name in ("n", "n.alt"):
        glyph = inspected["glyf"][name]
        print(
            name,
            "contours", glyph.numberOfContours,
            "points", len(glyph.coordinates),
            "bbox", (glyph.xMin, glyph.yMin, glyph.xMax, glyph.yMax),
            "advance", inspected["hmtx"][name][0],
        )


if __name__ == "__main__":
    main()
