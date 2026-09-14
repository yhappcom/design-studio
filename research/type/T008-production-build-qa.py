"""T008 production-build/release QA baseline.

Consumes the canonical T007 research builder, then audits the emitted variable
TrueType at binary/metadata/instance level. Reproduces two release-blocking
conditions:
1) T007's research masters use LSB=0 while xMin>0 and leave head.flags bit 1
   unset, violating the OpenType TrueType-variable-font requirement that
   left sidebearing equals xMin and bit 1 is set.
2) a deliberately stripped STAT table produces a structurally readable font
   that fails the variable-font required-table contract.

Then revises the master metrics/head flags, rebuilds, and re-runs the audit.

Generated font binaries remain temporary research outputs, not product assets.
Dependencies: fontTools, freetype-py, numpy, sibling T007 research script.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import struct
import tempfile
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

HERE = Path(__file__).resolve().parent
T007_PATH = HERE / "T007-variable-interpolation-build-proof.py"
RESULTS = Path("T008-production-build-qa-results.json")
EXPECTED_AXIS = {"tag": "wght", "min": 300.0, "default": 300.0, "max": 700.0}
CRITICAL_GLYPHS = ("H", "O", "n", "o")

spec = importlib.util.spec_from_file_location("t007_research", T007_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot load {T007_PATH}")
t007 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t007)


def whole_font_checksum(path: Path) -> int:
    data = path.read_bytes()
    if len(data) % 4:
        data += b"\0" * (4 - len(data) % 4)
    total = 0
    for i in range(0, len(data), 4):
        total = (total + struct.unpack(">I", data[i:i+4])[0]) & 0xFFFFFFFF
    return total


def contour_xmin(glyph, glyf_table):
    if glyph.isComposite():
        glyph.recalcBounds(glyf_table)
    elif glyph.numberOfContours != 0:
        glyph.recalcBounds(glyf_table)
    return getattr(glyph, "xMin", None)


def normalize_master_for_variable(path: Path):
    font = TTFont(path)
    glyf = font["glyf"]
    metrics = font["hmtx"].metrics

    changed = {}
    for name in font.getGlyphOrder():
        glyph = glyf[name]
        x_min = contour_xmin(glyph, glyf)
        if x_min is None:
            continue
        advance, old_lsb = metrics[name]
        metrics[name] = (advance, x_min)
        changed[name] = {"old_lsb": old_lsb, "new_lsb": x_min}

    # OpenType head requirement for variable TrueType outlines:
    # bit 1 set (LSB equals xMin), bit 5 clear.
    font["head"].flags |= 1 << 1
    font["head"].flags &= ~(1 << 5)

    # Fixed timestamp keeps this bounded research build reproducible when the
    # same sources/toolchain are used. This is a studio experiment, not a
    # recommendation that all production pipelines must use this exact value.
    font["head"].created = 3800000000
    font["head"].modified = 3800000000
    # TTFont.save() normally recalculates head.modified. Disable that behavior
    # explicitly; assigning a fixed timestamp alone is not sufficient.
    font.recalcTimestamp = False
    font.save(path)
    return changed


def build_pair(work: Path, prefix: str, normalize=False):
    light_cubic, light_metrics = t007.master_cubic(300)
    bold_cubic, bold_metrics = t007.master_cubic(700)
    light_glyphs, bold_glyphs = {}, {}
    for glyph in light_cubic:
        light_glyphs[glyph], bold_glyphs[glyph] = t007.compile_shared(
            light_cubic[glyph], bold_cubic[glyph]
        )

    light = work / f"{prefix}-300.ttf"
    bold = work / f"{prefix}-700.ttf"
    t007.build_master(light, light_glyphs, light_metrics, 300)
    t007.build_master(bold, bold_glyphs, bold_metrics, 700)

    changes = {}
    if normalize:
        changes["300"] = normalize_master_for_variable(light)
        changes["700"] = normalize_master_for_variable(bold)

    designspace = work / f"{prefix}.designspace"
    variable = work / f"{prefix}-VF.ttf"
    t007.write_designspace(light, bold, designspace)
    log = t007.build_variable(designspace, variable)
    if normalize:
        # varLib carries the default master's flags, but normalize the final
        # head timestamp explicitly for deterministic binary comparison.
        f = TTFont(variable)
        f["head"].created = 3800000000
        f["head"].modified = 3800000000
        f.recalcTimestamp = False
        f.save(variable)
    return variable, log, changes


def audit_font(path: Path):
    font = TTFont(path)
    tags = set(font.keys())
    failures = []
    warnings = []

    required_base = {"cmap", "head", "hhea", "hmtx", "maxp", "name", "OS/2", "post", "glyf", "loca"}
    required_variable = {"fvar", "STAT", "gvar"}
    for tag in sorted(required_base | required_variable):
        if tag not in tags:
            failures.append(f"missing_required_table:{tag}")

    if "head" in font:
        flags = font["head"].flags
        if not (flags & (1 << 1)):
            failures.append("head_bit1_not_set")
        if flags & (1 << 5):
            failures.append("head_bit5_must_be_clear")
        if font["head"].magicNumber != 0x5F0F3CF5:
            failures.append("head_magic_number_invalid")

    axis_records = []
    if "fvar" in font:
        for axis in font["fvar"].axes:
            rec = {
                "tag": axis.axisTag,
                "min": axis.minValue,
                "default": axis.defaultValue,
                "max": axis.maxValue,
                "name_id": axis.axisNameID,
            }
            axis_records.append(rec)
        target = next((a for a in axis_records if a["tag"] == EXPECTED_AXIS["tag"]), None)
        if target is None:
            failures.append("missing_expected_wght_axis")
        else:
            for key in ("min", "default", "max"):
                if float(target[key]) != EXPECTED_AXIS[key]:
                    failures.append(f"wght_{key}_mismatch")

    stat_axes = []
    if "STAT" in font:
        stat = font["STAT"].table
        if getattr(stat, "DesignAxisRecord", None):
            stat_axes = [
                {"tag": a.AxisTag, "name_id": a.AxisNameID, "ordering": a.AxisOrdering}
                for a in stat.DesignAxisRecord.Axis
            ]
        if "fvar" in font:
            fvar_tags = [a["tag"] for a in axis_records]
            stat_tags = [a["tag"] for a in stat_axes]
            if fvar_tags != stat_tags:
                failures.append("STAT_fvar_axis_mismatch")

    name_ids = sorted({record.nameID for record in font["name"].names})
    for required_name_id in (1, 2, 3, 4, 6):
        if required_name_id not in name_ids:
            failures.append(f"missing_name_id:{required_name_id}")
    if "fvar" in font:
        for axis in font["fvar"].axes:
            try:
                axis_name = font["name"].getName(axis.axisNameID, 3, 1)
            except Exception:
                axis_name = None
            if axis_name is None:
                failures.append(f"unresolvable_axis_name_id:{axis.axisNameID}")

    gvar_counts = {}
    if "gvar" in font:
        for glyph in CRITICAL_GLYPHS:
            count = len(font["gvar"].variations.get(glyph, []))
            gvar_counts[glyph] = count
            if count == 0:
                failures.append(f"critical_glyph_has_no_variation:{glyph}")

    instance_checks = {}
    if all(tag in font for tag in ("fvar", "glyf", "hmtx")):
        for weight in (300, 500, 700):
            instance = instantiateVariableFont(font, {"wght": weight}, inplace=False, overlap=False)
            glyf = instance["glyf"]
            rows = {}
            for glyph_name in CRITICAL_GLYPHS:
                glyph = glyf[glyph_name]
                x_min = contour_xmin(glyph, glyf)
                advance, lsb = instance["hmtx"][glyph_name]
                equal = x_min is not None and lsb == x_min
                rows[glyph_name] = {
                    "advance": advance,
                    "lsb": lsb,
                    "xMin": x_min,
                    "lsb_equals_xMin": equal,
                }
                if not equal:
                    failures.append(f"instance_{weight}_lsb_xmin_mismatch:{glyph_name}")
            instance_checks[str(weight)] = rows

    if "OS/2" in font and "fvar" in font:
        default_wght = next((a.defaultValue for a in font["fvar"].axes if a.axisTag == "wght"), None)
        if default_wght is not None and font["OS/2"].usWeightClass != round(default_wght):
            warnings.append("OS2_weight_does_not_match_default_wght")

    checksum = whole_font_checksum(path)
    if checksum != 0xB1B0AFBA:
        failures.append(f"whole_font_checksum_invalid:{checksum:#x}")

    return {
        "path": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "tables": sorted(tags),
        "head_flags": font["head"].flags if "head" in font else None,
        "axis_records": axis_records,
        "stat_axes": stat_axes,
        "name_ids": name_ids,
        "gvar_tuple_counts": gvar_counts,
        "instance_checks": instance_checks,
        "whole_font_checksum": f"{checksum:#010x}",
        "failures": sorted(set(failures)),
        "warnings": sorted(set(warnings)),
        "pass": not failures,
    }


def timestamp_control_probe(source: Path, work: Path):
    fixed = 3800000000

    automatic = TTFont(source)
    automatic["head"].created = fixed
    automatic["head"].modified = fixed
    automatic.recalcTimestamp = True
    automatic_path = work / "timestamp-auto.ttf"
    automatic.save(automatic_path)
    automatic_saved = TTFont(automatic_path)["head"].modified

    controlled = TTFont(source)
    controlled["head"].created = fixed
    controlled["head"].modified = fixed
    controlled.recalcTimestamp = False
    controlled_path = work / "timestamp-fixed.ttf"
    controlled.save(controlled_path)
    controlled_saved = TTFont(controlled_path)["head"].modified

    return {
        "requested_modified": fixed,
        "automatic_recalc_saved_modified": automatic_saved,
        "automatic_recalc_overrode_requested": automatic_saved != fixed,
        "disabled_recalc_saved_modified": controlled_saved,
        "disabled_recalc_preserved_requested": controlled_saved == fixed,
    }


def strip_stat(source: Path, target: Path):
    font = TTFont(source)
    if "STAT" in font:
        del font["STAT"]
    font.save(target)


def main():
    with tempfile.TemporaryDirectory(prefix="t008_") as td:
        work = Path(td)

        baseline_vf, baseline_log, _ = build_pair(work, "baseline", normalize=False)
        baseline = audit_font(baseline_vf)

        revised_vf, revised_log, normalization = build_pair(work, "revised", normalize=True)
        revised = audit_font(revised_vf)

        stripped = work / "revised-no-STAT.ttf"
        strip_stat(revised_vf, stripped)
        stripped_audit = audit_font(stripped)

        # Rebuild the normalized font once more to test binary reproducibility
        # under fixed source/toolchain/timestamps.
        revised2_vf, revised2_log, _ = build_pair(work, "revised2", normalize=True)
        revised2 = audit_font(revised2_vf)

        results = {
            "environment": {
                "fonttools_version": t007.fontTools.__version__,
                "freetype_version": ".".join(map(str, t007.freetype.version())),
                "upm": t007.UPM,
                "source_dependency": T007_PATH.name,
            },
            "baseline_from_T007_builder": baseline,
            "revision": {
                "master_lsb_normalization": normalization,
                "audit": revised,
            },
            "deliberate_STAT_removal": stripped_audit,
            "reproducibility": {
                "first_sha256": revised["sha256"],
                "second_sha256": revised2["sha256"],
                "binary_identical": revised["sha256"] == revised2["sha256"],
                "timestamp_control_probe": timestamp_control_probe(revised_vf, work),
            },
            "build_logs": {
                "baseline_contains_incompatible_warning": "incompatible masters" in baseline_log,
                "revised_contains_incompatible_warning": "incompatible masters" in revised_log,
                "revised2_contains_incompatible_warning": "incompatible masters" in revised2_log,
            },
            "scope_limits": [
                "Research-only H/O/n/o family with one wght axis.",
                "Studio-specific checker; not a replacement for FontBakery, OTS, OS/browser validation or foundry release engineering.",
                "No hinting, GSUB/GPOS, components, marks, CFF2, avar, named instances or multi-axis family.",
                "Name strings are research placeholders and are not a production naming system.",
            ],
        }

        RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
