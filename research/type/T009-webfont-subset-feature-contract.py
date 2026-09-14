from pathlib import Path
import tempfile, json, hashlib, shutil
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.ttLib import TTFont
from fontTools import subset
import fontTools

UPM = 1000
RESULTS = Path("T009-webfont-subset-feature-contract-results.json")


def rect(x0, y0, x1, y1):
    p = TTGlyphPen(None)
    p.moveTo((x0, y0)); p.lineTo((x1, y0)); p.lineTo((x1, y1)); p.lineTo((x0, y1)); p.closePath()
    return p.glyph()


def empty():
    return TTGlyphPen(None).glyph()


def build(path):
    order = [".notdef", "space", "one", "two", "one.tnum", "two.tnum"]
    glyphs = {
        ".notdef": rect(50, 0, 450, 700), "space": empty(),
        "one": rect(100, 0, 220, 700), "two": rect(80, 0, 420, 700),
        "one.tnum": rect(190, 0, 310, 700), "two.tnum": rect(80, 0, 420, 700),
    }
    metrics = {
        ".notdef": (500, 50), "space": (300, 0),
        "one": (380, 100), "two": (520, 80),
        "one.tnum": (600, 190), "two.tnum": (600, 80),
    }
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap({32: "space", 49: "one", 50: "two"})
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, sTypoLineGap=0,
                usWinAscent=900, usWinDescent=200, usWeightClass=400)
    fb.setupNameTable({"familyName": "T009 Research", "styleName": "Regular",
                       "uniqueFontIdentifier": "T009Research-Regular",
                       "fullName": "T009 Research Regular", "psName": "T009Research-Regular"})
    fb.setupPost(); fb.setupMaxp(); fb.save(path)
    f = TTFont(path)
    addOpenTypeFeaturesFromString(f, "feature tnum { sub one by one.tnum; sub two by two.tnum; } tnum;")
    f["head"].flags |= 2
    f.recalcTimestamp = False
    f.save(path)


def feature_tags(font):
    if "GSUB" not in font: return []
    fl = font["GSUB"].table.FeatureList
    return [] if not fl else [r.FeatureTag for r in fl.FeatureRecord]


def lookup_outputs(font):
    out = []
    if "GSUB" not in font: return out
    for lookup in font["GSUB"].table.LookupList.Lookup:
        for subtable in lookup.SubTable:
            if hasattr(subtable, "mapping"):
                out.extend(subtable.mapping.values())
    return sorted(set(out))


def audit(path):
    f = TTFont(path)
    glyphs = f.getGlyphOrder(); feats = feature_tags(f); outputs = lookup_outputs(f)
    widths = {g: f["hmtx"][g][0] for g in glyphs if g in f["hmtx"].metrics}
    output_widths = [widths.get(g) for g in outputs]
    return {
        "path": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "flavor": f.flavor,
        "tables": sorted(set(f.keys())),
        "glyphs": glyphs,
        "features": feats,
        "gsub_outputs": outputs,
        "tnum_present": "tnum" in feats,
        "tnum_output_count": len(outputs),
        "tnum_output_widths": output_widths,
        "tnum_equal_width": len(outputs) == 2 and len(set(output_widths)) == 1 and output_widths[0] == 600,
        "parseable": True,
        "size": path.stat().st_size,
    }


def make_woff2(src, dst):
    f = TTFont(src); f.flavor = "woff2"; f.save(dst)


def subset_font(src, dst, features):
    opts = subset.Options()
    opts.layout_features = features
    opts.name_IDs = ["*"]; opts.name_legacy = True; opts.name_languages = ["*"]
    opts.recalc_bounds = True; opts.recalc_timestamp = False
    s = subset.Subsetter(options=opts)
    s.populate(text="12")
    f = TTFont(src); s.subset(f); f.save(dst)


def main():
    tools = {n: shutil.which(n) for n in ["fontbakery", "fontspector", "ots-sanitize"]}
    with tempfile.TemporaryDirectory(prefix="t009_") as td:
        d = Path(td)
        src = d / "source.ttf"; build(src)
        source_woff2 = d / "source.woff2"; make_woff2(src, source_woff2)
        preserved = d / "subset-preserve.ttf"; subset_font(src, preserved, ["*"])
        dropped = d / "subset-drop-layout.ttf"; subset_font(src, dropped, [])
        preserved_woff2 = d / "subset-preserve.woff2"; make_woff2(preserved, preserved_woff2)
        dropped_woff2 = d / "subset-drop-layout.woff2"; make_woff2(dropped, dropped_woff2)

        rows = {k: audit(p) for k, p in [
            ("source_ttf", src), ("source_woff2", source_woff2),
            ("subset_preserve_ttf", preserved), ("subset_drop_layout_ttf", dropped),
            ("subset_preserve_woff2", preserved_woff2), ("subset_drop_layout_woff2", dropped_woff2),
        ]}
        contract = {k: (v["tnum_present"] and v["tnum_output_count"] == 2 and v["tnum_equal_width"])
                    for k, v in rows.items()}
        results = {
            "environment": {"fonttools": fontTools.__version__, "external_tools": tools},
            "artifacts": rows,
            "feature_contract_pass": contract,
            "derived": {
                "woff2_preserves_tnum": contract["source_woff2"],
                "feature_aware_subset_preserves_tnum": contract["subset_preserve_ttf"] and contract["subset_preserve_woff2"],
                "layout_feature_drop_remains_parseable_but_breaks_contract": rows["subset_drop_layout_ttf"]["parseable"] and not contract["subset_drop_layout_ttf"],
                "size_bytes": {k: v["size"] for k, v in rows.items()},
            },
            "scope_limits": [
                "Research-only six-glyph static TrueType; no variable axis or production family.",
                "Table/metric inspection only; no HarfBuzz/browser shaping proof.",
                "External FontBakery/Fontspector/OTS unavailable in this execution environment.",
            ],
        }
        RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
