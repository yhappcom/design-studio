"""T007 multi-master interpolation/source compatibility experiment.

Research-only Type Design evidence. Builds two-master TrueType controls in three
conditions:
1) masters converted independently from cubic to quadratic;
2) masters converted together with Cu2QuMultiPen for interpolation-compatible
   quadratic topology;
3) equal point counts with deliberately wrong contour start-point
   correspondence.

The script builds variable fonts with fontTools.varLib, instantiates wght
300/500/700, measures glyph geometry/metrics, and raster-checks O at 20 ppem.

Generated font binaries are local experimental outputs, not product assets.
Dependencies: fontTools, freetype-py, numpy.
"""
from __future__ import annotations

import io
import json
import logging
import tempfile
from pathlib import Path

import freetype
import fontTools
import numpy as np
from fontTools.designspaceLib import AxisDescriptor, DesignSpaceDocument, SourceDescriptor
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.cu2quPen import Cu2QuMultiPen, Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
from fontTools.varLib import build as varlib_build
from fontTools.varLib.instancer import instantiateVariableFont

UPM = 1000
MAX_ERR = 2.0
OUT = Path(".")
RESULTS = OUT / "T007-variable-interpolation-results.json"


def rect_cmd(x0, y0, x1, y1):
    return [("M", (x0, y0)), ("L", (x1, y0)), ("L", (x1, y1)), ("L", (x0, y1)), ("Z",)]


def ellipse_cmd(cx, cy, rx, ry, clockwise=False):
    k = 0.5522847498
    hx, hy = rx * k, ry * k
    if not clockwise:
        return [
            ("M", (cx + rx, cy)),
            ("C", (cx + rx, cy + hy), (cx + hx, cy + ry), (cx, cy + ry)),
            ("C", (cx - hx, cy + ry), (cx - rx, cy + hy), (cx - rx, cy)),
            ("C", (cx - rx, cy - hy), (cx - hx, cy - ry), (cx, cy - ry)),
            ("C", (cx + hx, cy - ry), (cx + rx, cy - hy), (cx + rx, cy)),
            ("Z",),
        ]
    return [
        ("M", (cx + rx, cy)),
        ("C", (cx + rx, cy - hy), (cx + hx, cy - ry), (cx, cy - ry)),
        ("C", (cx - hx, cy - ry), (cx - rx, cy - hy), (cx - rx, cy)),
        ("C", (cx - rx, cy + hy), (cx - hx, cy + ry), (cx, cy + ry)),
        ("C", (cx + hx, cy + ry), (cx + rx, cy + hy), (cx + rx, cy)),
        ("Z",),
    ]


def rotate_closed_commands(commands, segment_shift):
    curves = commands[1:-1]
    points = [commands[0][1]] + [curve[3] for curve in curves]
    shift = segment_shift % len(curves)
    out = [("M", points[shift])]
    for j in range(len(curves)):
        out.append(curves[(shift + j) % len(curves)])
    out.append(("Z",))
    return out


def H_cmd(stem=70, cross=70):
    x0, x1, cy = 50, 550, 350
    left1, right0 = x0 + stem, x1 - stem
    return [
        ("M", (x0, 0)),
        ("L", (left1, 0)),
        ("L", (left1, cy - cross / 2)),
        ("L", (right0, cy - cross / 2)),
        ("L", (right0, 0)),
        ("L", (x1, 0)),
        ("L", (x1, 700)),
        ("L", (right0, 700)),
        ("L", (right0, cy + cross / 2)),
        ("L", (left1, cy + cross / 2)),
        ("L", (left1, 700)),
        ("L", (x0, 700)),
        ("Z",),
    ]


def n_cmd(stem=70, outer_right=470, top=500, shoulder=420):
    return [
        ("M", (50, 0)),
        ("L", (50 + stem, 0)),
        ("L", (50 + stem, 300)),
        ("C", (50 + stem, 380), (190, shoulder), (285, shoulder)),
        ("C", (350, shoulder), (outer_right - stem, 385), (outer_right - stem, 300)),
        ("L", (outer_right - stem, 0)),
        ("L", (outer_right, 0)),
        ("L", (outer_right, 325)),
        ("C", (outer_right, 450), (390, top), (290, top)),
        ("C", (200, top), (150, 465), (50 + stem, 405)),
        ("L", (50 + stem, 500)),
        ("L", (50, 500)),
        ("Z",),
    ]


def master_cubic(weight):
    if weight == 300:
        contours = {
            "H": [H_cmd(65, 60)],
            "O": [ellipse_cmd(300, 350, 250, 360, False), ellipse_cmd(300, 350, 190, 300, True)],
            "n": [n_cmd(65, 455, 500, 415)],
            "o": [ellipse_cmd(260, 250, 210, 260, False), ellipse_cmd(260, 250, 160, 210, True)],
        }
        metrics = {"H": 580, "O": 600, "n": 520, "o": 500}
    elif weight == 700:
        contours = {
            "H": [H_cmd(120, 105)],
            "O": [ellipse_cmd(300, 350, 250, 360, False), ellipse_cmd(300, 350, 120, 140, True)],
            "n": [n_cmd(115, 480, 510, 425)],
            "o": [ellipse_cmd(260, 250, 210, 260, False), ellipse_cmd(260, 250, 120, 170, True)],
        }
        metrics = {"H": 640, "O": 620, "n": 580, "o": 540}
    else:
        raise ValueError(weight)
    return contours, metrics


def draw_commands(pen, commands):
    for cmd in commands:
        op = cmd[0]
        if op == "M":
            pen.moveTo(cmd[1])
        elif op == "L":
            pen.lineTo(cmd[1])
        elif op == "C":
            pen.curveTo(cmd[1], cmd[2], cmd[3])
        elif op == "Z":
            pen.closePath()
        else:
            raise ValueError(op)


def compile_independent(contours):
    pen = TTGlyphPen(None)
    qpen = Cu2QuPen(pen, MAX_ERR, reverse_direction=True)
    for contour in contours:
        draw_commands(qpen, contour)
    return pen.glyph()


def compile_shared(contours_a, contours_b):
    pen_a, pen_b = TTGlyphPen(None), TTGlyphPen(None)
    mpen = Cu2QuMultiPen([pen_a, pen_b], MAX_ERR, reverse_direction=True)
    for a, b in zip(contours_a, contours_b):
        assert len(a) == len(b)
        for ca, cb in zip(a, b):
            assert ca[0] == cb[0]
            if ca[0] == "M":
                mpen.moveTo([(ca[1],), (cb[1],)])
            elif ca[0] == "L":
                mpen.lineTo([(ca[1],), (cb[1],)])
            elif ca[0] == "C":
                mpen.curveTo([(ca[1], ca[2], ca[3]), (cb[1], cb[2], cb[3])])
            elif ca[0] == "Z":
                mpen.closePath()
    return pen_a.glyph(), pen_b.glyph()


def contour_point_counts(glyph):
    counts = []
    start = 0
    for end in glyph.endPtsOfContours:
        counts.append(end - start + 1)
        start = end + 1
    return counts


def empty_glyph():
    return TTGlyphPen(None).glyph()


def build_master(path, glyphs, metrics, weight):
    order = [".notdef", "space", "H", "O", "n", "o"]
    notdef = compile_independent([rect_cmd(50, 0, 450, 700)])
    all_glyphs = {".notdef": notdef, "space": empty_glyph(), **glyphs}
    hmtx = {".notdef": (500, 0), "space": (300, 0)}
    for name in ("H", "O", "n", "o"):
        hmtx[name] = (metrics[name], 0)
    cmap = {0x20: "space", 0x48: "H", 0x4F: "O", 0x6E: "n", 0x6F: "o"}

    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(all_glyphs)
    fb.setupHorizontalMetrics(hmtx)
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupOS2(
        sTypoAscender=800,
        sTypoDescender=-200,
        sTypoLineGap=0,
        usWinAscent=900,
        usWinDescent=200,
        usWeightClass=weight,
    )
    fb.setupNameTable(
        {
            "familyName": "T007 Research",
            "styleName": f"W{weight}",
            "uniqueFontIdentifier": f"T007Research-{weight}",
            "fullName": f"T007 Research {weight}",
            "psName": f"T007Research-{weight}",
        }
    )
    fb.setupPost()
    fb.setupMaxp()
    fb.save(path)


def write_designspace(light_path, bold_path, path):
    ds = DesignSpaceDocument()
    axis = AxisDescriptor()
    axis.name = "Weight"
    axis.tag = "wght"
    axis.minimum = 300
    axis.default = 300
    axis.maximum = 700
    ds.addAxis(axis)
    for font_path, weight, name in ((light_path, 300, "light"), (bold_path, 700, "bold")):
        source = SourceDescriptor()
        source.path = str(font_path)
        source.name = name
        source.familyName = "T007 Research"
        source.styleName = f"W{weight}"
        source.location = {"Weight": weight}
        ds.addSource(source)
    ds.write(path)


def build_variable(designspace_path, output_path):
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger = logging.getLogger("fontTools.varLib")
    old_level = logger.level
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    try:
        vf, _, _ = varlib_build(str(designspace_path))
        vf.save(output_path)
    finally:
        logger.removeHandler(handler)
        logger.setLevel(old_level)
    return stream.getvalue()


def glyph_area(font, name):
    glyph_set = font.getGlyphSet()
    pen = AreaPen(glyph_set)
    glyph_set[name].draw(pen)
    return abs(pen.value)


def instance_metrics(vf_path, workdir, glyph="O", ppem=20):
    rows = []
    for weight in (300, 500, 700):
        vf = TTFont(vf_path)
        instance = instantiateVariableFont(vf, {"wght": weight}, inplace=False, overlap=False)
        static_path = workdir / f"{Path(vf_path).stem}-{weight}.ttf"
        instance.save(static_path)
        face = freetype.Face(str(static_path))
        face.set_pixel_sizes(0, ppem)
        flags = freetype.FT_LOAD_RENDER | freetype.FT_LOAD_NO_HINTING | freetype.FT_LOAD_TARGET_LIGHT
        face.load_char("O", flags)
        bitmap = face.glyph.bitmap
        arr = np.asarray(bitmap.buffer, dtype=np.uint8)
        coverage = float(arr.sum() / 255.0) if arr.size else 0.0
        rows.append(
            {
                "wght": weight,
                "advance": instance["hmtx"][glyph][0],
                "black_area": glyph_area(instance, glyph),
                "coverage_20ppem": coverage,
                "bitmap_width": bitmap.width,
                "bitmap_rows": bitmap.rows,
            }
        )
    return rows


def gvar_count(vf_path, glyph):
    font = TTFont(vf_path)
    return len(font["gvar"].variations.get(glyph, []))


def main():
    with tempfile.TemporaryDirectory(prefix="t007_") as td:
        work = Path(td)
        light_cubic, light_metrics = master_cubic(300)
        bold_cubic, bold_metrics = master_cubic(700)

        # A. independent conversion: same cubic segmentation, separate adaptive
        # conversion. O ends up with incompatible quadratic point counts.
        independent_light = {k: compile_independent(v) for k, v in light_cubic.items()}
        independent_bold = {k: compile_independent(v) for k, v in bold_cubic.items()}
        build_master(work / "independent-300.ttf", independent_light, light_metrics, 300)
        build_master(work / "independent-700.ttf", independent_bold, bold_metrics, 700)
        write_designspace(work / "independent-300.ttf", work / "independent-700.ttf", work / "independent.designspace")
        independent_log = build_variable(work / "independent.designspace", work / "independent-vf.ttf")

        # B. shared conversion: corresponding cubic curves are converted together.
        shared_light, shared_bold = {}, {}
        for glyph in light_cubic:
            shared_light[glyph], shared_bold[glyph] = compile_shared(light_cubic[glyph], bold_cubic[glyph])
        build_master(work / "shared-300.ttf", shared_light, light_metrics, 300)
        build_master(work / "shared-700.ttf", shared_bold, bold_metrics, 700)
        write_designspace(work / "shared-300.ttf", work / "shared-700.ttf", work / "shared.designspace")
        shared_log = build_variable(work / "shared.designspace", work / "shared-vf.ttf")

        # C. correspondence failure: keep equal point counts, but rotate the
        # Bold O counter start point by 180 degrees before shared conversion.
        mis_bold_cubic = {k: [list(cmds) for cmds in v] for k, v in bold_cubic.items()}
        mis_bold_cubic["O"] = [
            bold_cubic["O"][0],
            rotate_closed_commands(bold_cubic["O"][1], 2),
        ]
        mis_light, mis_bold = {}, {}
        for glyph in light_cubic:
            mis_light[glyph], mis_bold[glyph] = compile_shared(light_cubic[glyph], mis_bold_cubic[glyph])
        build_master(work / "mis-300.ttf", mis_light, light_metrics, 300)
        build_master(work / "mis-700.ttf", mis_bold, bold_metrics, 700)
        write_designspace(work / "mis-300.ttf", work / "mis-700.ttf", work / "mis.designspace")
        mis_log = build_variable(work / "mis.designspace", work / "mis-vf.ttf")

        results = {
            "environment": {
                "upm": UPM,
                "fonttools_version": fontTools.__version__,
                "cu2qu_max_err": MAX_ERR,
                "freetype_version": ".".join(map(str, freetype.version())),
            },
            "independent_conversion": {
                "master_point_counts": {
                    "300": {g: contour_point_counts(independent_light[g]) for g in ("H", "O", "n", "o")},
                    "700": {g: contour_point_counts(independent_bold[g]) for g in ("H", "O", "n", "o")},
                },
                "varlib_warning_contains_incompatible_O": "glyph O has incompatible masters; skipping" in independent_log,
                "gvar_tuple_counts": {g: gvar_count(work / "independent-vf.ttf", g) for g in ("H", "O", "n", "o")},
                "O_instances": instance_metrics(work / "independent-vf.ttf", work),
            },
            "shared_conversion": {
                "master_point_counts": {
                    "300": {g: contour_point_counts(shared_light[g]) for g in ("H", "O", "n", "o")},
                    "700": {g: contour_point_counts(shared_bold[g]) for g in ("H", "O", "n", "o")},
                },
                "gvar_tuple_counts": {g: gvar_count(work / "shared-vf.ttf", g) for g in ("H", "O", "n", "o")},
                "O_instances": instance_metrics(work / "shared-vf.ttf", work),
            },
            "wrong_correspondence": {
                "description": "Bold O counter start point rotated 180 degrees; point counts remain equal.",
                "master_point_counts": {
                    "300": contour_point_counts(mis_light["O"]),
                    "700": contour_point_counts(mis_bold["O"]),
                },
                "gvar_tuple_count_O": gvar_count(work / "mis-vf.ttf", "O"),
                "O_instances": instance_metrics(work / "mis-vf.ttf", work),
            },
            "scope_limits": [
                "Two masters only; one wght axis.",
                "Original research outlines, not a production family.",
                "No components, diacritics, kerning, hinting, CFF2, browser, CoreText, DirectWrite, Skia or Flutter validation.",
                "FreeType raster check is no-hint grayscale at 20 ppem.",
            ],
        }

        shared = results["shared_conversion"]["O_instances"]
        wrong = results["wrong_correspondence"]["O_instances"]
        shared_mid, shared_bold = shared[1], shared[2]
        wrong_mid, wrong_bold = wrong[1], wrong[2]
        results["derived"] = {
            "shared_midpoint_area_between_endpoints": shared[0]["black_area"] < shared_mid["black_area"] < shared_bold["black_area"],
            "wrong_midpoint_area_vs_bold_percent": (wrong_mid["black_area"] / wrong_bold["black_area"] - 1) * 100,
            "wrong_midpoint_coverage_vs_bold_percent": (wrong_mid["coverage_20ppem"] / wrong_bold["coverage_20ppem"] - 1) * 100,
        }

        RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
