from pathlib import Path
import tempfile, json, hashlib, shutil
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.ttLib import TTFont
from fontTools import subset
import fontTools

UPM = 1000
RESULTS = Path("T012-mark-mkmk-anchor-release-contract-results.json")


def rect(x0, y0, x1, y1):
    p = TTGlyphPen(None)
    p.moveTo((x0, y0)); p.lineTo((x1, y0)); p.lineTo((x1, y1)); p.lineTo((x0, y1)); p.closePath()
    return p.glyph()


def build(path):
    order = [".notdef", "A", "acutecomb", "dotabovecomb"]
    glyphs = {
        ".notdef": rect(50, 0, 450, 700),
        "A": rect(80, 0, 520, 700),
        "acutecomb": rect(60, 0, 140, 180),
        "dotabovecomb": rect(70, 0, 130, 60),
    }
    metrics = {".notdef": (500, 50), "A": (600, 80), "acutecomb": (0, 60), "dotabovecomb": (0, 70)}
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap({65: "A", 0x301: "acutecomb", 0x307: "dotabovecomb"})
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=850, descent=-250)
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, usWinAscent=900, usWinDescent=250, usWeightClass=400)
    fb.setupNameTable({"familyName": "T012 Research", "styleName": "Regular", "uniqueFontIdentifier": "T012Research-Regular", "fullName": "T012 Research Regular", "psName": "T012Research-Regular"})
    fb.setupPost(); fb.setupMaxp(); fb.save(path)
    f = TTFont(path)
    addOpenTypeFeaturesFromString(f, """
languagesystem DFLT dflt;
languagesystem latn dflt;
markClass acutecomb <anchor 100 0> @TOP;
markClass dotabovecomb <anchor 100 0> @TOP;
feature mark {
  pos base A <anchor 300 700> mark @TOP;
} mark;
feature mkmk {
  pos mark acutecomb <anchor 100 220> mark @TOP;
} mkmk;
""")
    f["head"].flags |= 2
    f.recalcTimestamp = False
    f.save(path)


def subset_font(src, dst, features):
    opts = subset.Options()
    opts.layout_features = features
    opts.layout_scripts = ["*"]
    opts.name_IDs = ["*"]
    opts.name_legacy = True
    opts.name_languages = ["*"]
    opts.recalc_timestamp = False
    s = subset.Subsetter(options=opts)
    s.populate(text="A\u0301\u0307")
    f = TTFont(src)
    s.subset(f)
    f.recalcTimestamp = False
    f.save(dst)


def make_woff2(src, dst):
    f = TTFont(src)
    f.flavor = "woff2"
    f.recalcTimestamp = False
    f.save(dst)


def bindings(font):
    out = []
    if "GPOS" not in font:
        return out
    t = font["GPOS"].table
    if not t.FeatureList or not t.ScriptList:
        return out
    tags = [r.FeatureTag for r in t.FeatureList.FeatureRecord]
    for sr in t.ScriptList.ScriptRecord:
        script = sr.Script
        if script.DefaultLangSys:
            for idx in script.DefaultLangSys.FeatureIndex:
                out.append((sr.ScriptTag, "dflt", tags[idx]))
        for lr in script.LangSysRecord:
            for idx in lr.LangSys.FeatureIndex:
                out.append((sr.ScriptTag, lr.LangSysTag, tags[idx]))
    return sorted(out)


def anchor(a):
    return None if a is None else [a.XCoordinate, a.YCoordinate]


def mark_semantics(font):
    result = {"mark_to_base": [], "mark_to_mark": []}
    if "GPOS" not in font:
        return result
    t = font["GPOS"].table
    if not t.LookupList:
        return result
    for lookup in t.LookupList.Lookup:
        for st in lookup.SubTable:
            if lookup.LookupType == 4:
                marks = [{"glyph": g, "class": r.Class, "anchor": anchor(r.MarkAnchor)} for g, r in zip(st.MarkCoverage.glyphs, st.MarkArray.MarkRecord)]
                bases = [{"glyph": g, "anchors": [anchor(a) for a in r.BaseAnchor]} for g, r in zip(st.BaseCoverage.glyphs, st.BaseArray.BaseRecord)]
                result["mark_to_base"].append({"marks": marks, "bases": bases})
            elif lookup.LookupType == 6:
                mark1 = [{"glyph": g, "class": r.Class, "anchor": anchor(r.MarkAnchor)} for g, r in zip(st.Mark1Coverage.glyphs, st.Mark1Array.MarkRecord)]
                mark2 = [{"glyph": g, "anchors": [anchor(a) for a in r.Mark2Anchor]} for g, r in zip(st.Mark2Coverage.glyphs, st.Mark2Array.Mark2Record)]
                result["mark_to_mark"].append({"mark1": mark1, "mark2": mark2})
    return result


def audit(path):
    f = TTFont(path)
    cmap = f.getBestCmap()
    sem = mark_semantics(f)
    b = bindings(f)
    hmtx = f["hmtx"].metrics
    A_g, acute_g, dot_g = cmap.get(65), cmap.get(0x301), cmap.get(0x307)

    def has_mtb():
        for item in sem["mark_to_base"]:
            if any(r["glyph"] == acute_g and r["anchor"] == [100, 0] for r in item["marks"]) and any(r["glyph"] == A_g and [300, 700] in r["anchors"] for r in item["bases"]):
                return True
        return False

    def has_mtm():
        for item in sem["mark_to_mark"]:
            if any(r["glyph"] == dot_g and r["anchor"] == [100, 0] for r in item["mark1"]) and any(r["glyph"] == acute_g and [100, 220] in r["anchors"] for r in item["mark2"]):
                return True
        return False

    contract = {
        "cmap_A": 65 in cmap,
        "cmap_acute": 0x301 in cmap,
        "cmap_dotabove": 0x307 in cmap,
        "combining_zero_advances": hmtx[cmap[0x301]][0] == 0 and hmtx[cmap[0x307]][0] == 0,
        "mark_bound_latn": ("latn", "dflt", "mark") in b,
        "mkmk_bound_latn": ("latn", "dflt", "mkmk") in b,
        "mark_to_base_anchor_contract": has_mtb(),
        "mark_to_mark_anchor_contract": has_mtm(),
    }
    return {
        "file": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "size": path.stat().st_size,
        "flavor": f.flavor,
        "glyphs": f.getGlyphOrder(),
        "bindings": b,
        "semantics": sem,
        "advances": {g: hmtx[g][0] for g in f.getGlyphOrder() if g in hmtx},
        "contract": contract,
        "contract_pass": all(contract.values()),
    }


def main():
    tools = {n: shutil.which(n) for n in ["fontbakery", "fontspector", "ots-sanitize", "hb-shape"]}
    with tempfile.TemporaryDirectory(prefix="t012_") as td:
        d = Path(td)
        source = d / "source.ttf"
        build(source)
        paths = {}
        for name, features in [("preserve", ["*"]), ("drop_mark", ["mkmk"]), ("drop_mkmk", ["mark"]), ("drop_layout", [])]:
            ttf = d / f"{name}.ttf"
            subset_font(source, ttf, features)
            paths[name + "_ttf"] = ttf
            woff = d / f"{name}.woff2"
            make_woff2(ttf, woff)
            paths[name + "_woff2"] = woff
        source_woff2 = d / "source.woff2"
        make_woff2(source, source_woff2)
        paths = {"source_ttf": source, "source_woff2": source_woff2, **paths}
        artifacts = {k: audit(v) for k, v in paths.items()}
        results = {
            "environment": {"fonttools": fontTools.__version__, "external_tools": tools},
            "contract_definition": {
                "text": "A + U+0301 COMBINING ACUTE + U+0307 COMBINING DOT ABOVE",
                "mark": "acutecomb attach [100,0] -> A base anchor [300,700]",
                "mkmk": "dotabovecomb attach [100,0] -> acutecomb mark2 anchor [100,220]",
                "combining_advances": "0 units",
            },
            "artifacts": artifacts,
            "derived": {
                "source_woff2_pass": artifacts["source_woff2"]["contract_pass"],
                "preserving_subset_pass": artifacts["preserve_woff2"]["contract_pass"],
                "drop_mark_parseable_cmap_intact_but_chain_fails": all(artifacts["drop_mark_woff2"]["contract"][k] for k in ["cmap_A", "cmap_acute", "cmap_dotabove", "combining_zero_advances", "mkmk_bound_latn", "mark_to_mark_anchor_contract"]) and not artifacts["drop_mark_woff2"]["contract"]["mark_bound_latn"] and not artifacts["drop_mark_woff2"]["contract"]["mark_to_base_anchor_contract"],
                "drop_mkmk_parseable_cmap_intact_but_chain_fails": all(artifacts["drop_mkmk_woff2"]["contract"][k] for k in ["cmap_A", "cmap_acute", "cmap_dotabove", "combining_zero_advances", "mark_bound_latn", "mark_to_base_anchor_contract"]) and not artifacts["drop_mkmk_woff2"]["contract"]["mkmk_bound_latn"] and not artifacts["drop_mkmk_woff2"]["contract"]["mark_to_mark_anchor_contract"],
                "drop_layout_keeps_unicode_but_loses_attachment_semantics": all(artifacts["drop_layout_woff2"]["contract"][k] for k in ["cmap_A", "cmap_acute", "cmap_dotabove", "combining_zero_advances"]) and not any(artifacts["drop_layout_woff2"]["contract"][k] for k in ["mark_bound_latn", "mkmk_bound_latn", "mark_to_base_anchor_contract", "mark_to_mark_anchor_contract"]),
            },
            "scope_limits": [
                "Structural GPOS inspection only; no HarfBuzz/browser shaping was available.",
                "Synthetic Latin combining-mark specimen, not production diacritic or complex-script design evidence.",
                "No cursive attachment, ligature marks, Indic/Arabic shaping, variation, CFF2, hinting, platform/device or human evidence.",
                "External FontBakery/Fontspector/OTS unavailable; no sanitizer PASS claimed.",
            ],
        }
        RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
