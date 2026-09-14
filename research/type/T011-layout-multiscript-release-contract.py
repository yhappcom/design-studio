from pathlib import Path
import tempfile, json, hashlib, shutil
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.ttLib import TTFont
from fontTools import subset
import fontTools

UPM = 1000
RESULTS = Path("T011-layout-multiscript-release-contract-results.json")


def rect(x0, y0, x1, y1):
    p = TTGlyphPen(None)
    p.moveTo((x0, y0)); p.lineTo((x1, y0)); p.lineTo((x1, y1)); p.lineTo((x0, y1)); p.closePath()
    return p.glyph()


def empty():
    return TTGlyphPen(None).glyph()


def build(path):
    order = [".notdef", "space", "A", "V", "i", "i.loclTRK", "uniD55C"]
    glyphs = {
        ".notdef": rect(50, 0, 450, 700), "space": empty(),
        "A": rect(80, 0, 520, 700), "V": rect(70, 0, 530, 700),
        "i": rect(180, 0, 300, 700), "i.loclTRK": rect(160, 0, 320, 700),
        "uniD55C": rect(60, -40, 840, 760),
    }
    metrics = {
        ".notdef": (500, 50), "space": (300, 0),
        "A": (600, 80), "V": (600, 70),
        "i": (380, 180), "i.loclTRK": (380, 160),
        "uniD55C": (900, 60),
    }
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap({32: "space", 65: "A", 86: "V", 105: "i", 0xD55C: "uniD55C"})
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=820, descent=-220, lineGap=20)
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, sTypoLineGap=0,
                usWinAscent=900, usWinDescent=250, usWeightClass=400)
    fb.setupNameTable({"familyName": "T011 Research", "styleName": "Regular",
                       "uniqueFontIdentifier": "T011Research-Regular",
                       "fullName": "T011 Research Regular", "psName": "T011Research-Regular"})
    fb.setupPost(); fb.setupMaxp(); fb.save(path)

    f = TTFont(path)
    addOpenTypeFeaturesFromString(f, """
languagesystem DFLT dflt;
languagesystem latn dflt;
languagesystem latn TRK;
languagesystem hang dflt;
feature kern { pos A V -80; } kern;
feature locl {
  script latn;
  language TRK;
  sub i by i.loclTRK;
} locl;
""")
    f["head"].flags |= 2
    f.recalcTimestamp = False
    f.save(path)


def make_woff2(src, dst):
    f = TTFont(src); f.flavor = "woff2"; f.recalcTimestamp = False; f.save(dst)


def subset_font(src, dst, features):
    opts = subset.Options()
    opts.layout_features = features
    opts.layout_scripts = ["*"]
    opts.name_IDs = ["*"]; opts.name_legacy = True; opts.name_languages = ["*"]
    opts.recalc_bounds = True; opts.recalc_timestamp = False
    s = subset.Subsetter(options=opts)
    s.populate(text="AVi한")
    f = TTFont(src); s.subset(f); f.recalcTimestamp = False; f.save(dst)


def mutate_hhea(src, dst):
    f = TTFont(src); f["hhea"].ascent += 80; f.recalcTimestamp = False; f.save(dst)


def feature_bindings(font, table_tag):
    if table_tag not in font: return []
    table = font[table_tag].table
    if not table.FeatureList or not table.ScriptList: return []
    tags = [r.FeatureTag for r in table.FeatureList.FeatureRecord]
    out = []
    for sr in table.ScriptList.ScriptRecord:
        script = sr.Script
        if script.DefaultLangSys:
            for idx in script.DefaultLangSys.FeatureIndex:
                out.append((sr.ScriptTag, "dflt", tags[idx]))
        for lr in script.LangSysRecord:
            for idx in lr.LangSys.FeatureIndex:
                out.append((sr.ScriptTag, lr.LangSysTag, tags[idx]))
    return sorted(out)


def kern_pairs(font):
    out = []
    if "GPOS" not in font: return out
    table = font["GPOS"].table
    if not table.LookupList: return out
    for lookup in table.LookupList.Lookup:
        for st in lookup.SubTable:
            if getattr(st, "Format", None) == 1 and hasattr(st, "PairSet"):
                for left, pairset in zip(st.Coverage.glyphs, st.PairSet):
                    for rec in pairset.PairValueRecord:
                        xadv = rec.Value1.XAdvance if rec.Value1 and rec.Value1.XAdvance is not None else 0
                        out.append((left, rec.SecondGlyph, xadv))
    return sorted(out)


def locl_semantics(font):
    out = []
    if "GSUB" not in font: return out
    table = font["GSUB"].table
    if not table.LookupList: return out
    widths = font["hmtx"].metrics
    for lookup in table.LookupList.Lookup:
        for st in lookup.SubTable:
            if hasattr(st, "mapping"):
                for src, dst in st.mapping.items():
                    out.append({"source": src, "target": dst,
                                "source_advance": widths[src][0], "target_advance": widths[dst][0]})
    return out


def audit(path):
    f = TTFont(path)
    cmap = f.getBestCmap(); kp = kern_pairs(f); locl = locl_semantics(f)
    hhea = {"ascent": f["hhea"].ascent, "descent": f["hhea"].descent, "lineGap": f["hhea"].lineGap}
    os2 = {"sTypoAscender": f["OS/2"].sTypoAscender, "sTypoDescender": f["OS/2"].sTypoDescender,
           "sTypoLineGap": f["OS/2"].sTypoLineGap, "usWinAscent": f["OS/2"].usWinAscent,
           "usWinDescent": f["OS/2"].usWinDescent}
    bindings = {"GPOS": feature_bindings(f, "GPOS"), "GSUB": feature_bindings(f, "GSUB")}
    contract = {
        "latin_A_present": 65 in cmap, "latin_V_present": 86 in cmap,
        "latin_i_present": 105 in cmap, "hangul_han_present": 0xD55C in cmap,
        "kern_AV_minus80": ("A", "V", -80) in kp,
        "locl_latn_TRK_bound": ("latn", "TRK ", "locl") in bindings["GSUB"],
        "locl_alternate_closure": len(locl) == 1 and locl[0]["source_advance"] == 380 and locl[0]["target_advance"] == 380,
        "vertical_metrics_exact": hhea == {"ascent": 820, "descent": -220, "lineGap": 20}
            and os2 == {"sTypoAscender": 800, "sTypoDescender": -200, "sTypoLineGap": 0,
                        "usWinAscent": 900, "usWinDescent": 250},
    }
    return {"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "size": path.stat().st_size, "flavor": f.flavor, "tables": sorted(set(f.keys())),
            "glyphs": f.getGlyphOrder(), "cmap_codepoints": sorted(cmap.keys()),
            "feature_bindings": bindings, "kern_pairs": kp, "locl_semantics": locl,
            "hhea": hhea, "os2": os2, "contract": contract,
            "contract_pass": all(contract.values()), "parseable": True}


def main():
    tools = {n: shutil.which(n) for n in ["fontbakery", "fontspector", "ots-sanitize", "hb-shape"]}
    with tempfile.TemporaryDirectory(prefix="t011_") as td:
        d = Path(td)
        source = d / "source.ttf"; build(source)
        source_woff2 = d / "source.woff2"; make_woff2(source, source_woff2)
        preserve = d / "subset-preserve.ttf"; subset_font(source, preserve, ["*"])
        preserve_woff2 = d / "subset-preserve.woff2"; make_woff2(preserve, preserve_woff2)
        drop = d / "subset-drop-layout.ttf"; subset_font(source, drop, [])
        drop_woff2 = d / "subset-drop-layout.woff2"; make_woff2(drop, drop_woff2)
        metric_mut = d / "subset-metric-mutated.ttf"; mutate_hhea(preserve, metric_mut)
        metric_mut_woff2 = d / "subset-metric-mutated.woff2"; make_woff2(metric_mut, metric_mut_woff2)

        artifacts = {k: audit(p) for k, p in [
            ("source_ttf", source), ("source_woff2", source_woff2),
            ("subset_preserve_ttf", preserve), ("subset_preserve_woff2", preserve_woff2),
            ("subset_drop_layout_ttf", drop), ("subset_drop_layout_woff2", drop_woff2),
            ("subset_metric_mutated_ttf", metric_mut), ("subset_metric_mutated_woff2", metric_mut_woff2),
        ]}
        results = {
            "environment": {"fonttools": fontTools.__version__, "external_tools": tools},
            "contract_definition": {"characters": ["A", "V", "i", "한"], "kern": "A V = -80 font units",
                "locl": "latn/TRK locl maps i to alternate with retained 380-unit advance",
                "vertical_metrics": {"hhea": {"ascent": 820, "descent": -220, "lineGap": 20},
                    "OS/2": {"sTypoAscender": 800, "sTypoDescender": -200, "sTypoLineGap": 0,
                             "usWinAscent": 900, "usWinDescent": 250}}},
            "artifacts": artifacts,
            "derived": {
                "normal_woff2_preserves_contract": artifacts["source_woff2"]["contract_pass"],
                "feature_aware_subset_preserves_contract": artifacts["subset_preserve_ttf"]["contract_pass"] and artifacts["subset_preserve_woff2"]["contract_pass"],
                "layout_drop_parseable_but_contract_fails": artifacts["subset_drop_layout_woff2"]["parseable"] and not artifacts["subset_drop_layout_woff2"]["contract_pass"],
                "layout_drop_keeps_requested_cmap_but_loses_kern_locl": all(artifacts["subset_drop_layout_woff2"]["contract"][k] for k in ["latin_A_present", "latin_V_present", "latin_i_present", "hangul_han_present"]) and not artifacts["subset_drop_layout_woff2"]["contract"]["kern_AV_minus80"] and not artifacts["subset_drop_layout_woff2"]["contract"]["locl_latn_TRK_bound"],
                "metric_mutation_parseable_but_contract_fails": artifacts["subset_metric_mutated_woff2"]["parseable"] and not artifacts["subset_metric_mutated_woff2"]["contract_pass"],
                "metric_mutation_hhea_ascent_delta": artifacts["subset_metric_mutated_woff2"]["hhea"]["ascent"] - artifacts["subset_preserve_woff2"]["hhea"]["ascent"],
            },
            "scope_limits": [
                "Research-only seven-glyph static TrueType; not a production Latin/Hangul family.",
                "Structural OpenType inspection only; HarfBuzz/hb-shape and browser shaping were unavailable in this environment.",
                "The Hangul glyph is a simple research rectangle used only to prove cmap/script subset retention, not Hangul design quality or shaping.",
                "No mark/mkmk anchors, complex-script shaping, variable axes, CFF2, hinting, CoreText/DirectWrite/Skia/browser or human evidence.",
                "FontBakery/Fontspector/OTS were unavailable; no external sanitizer PASS is claimed.",
            ],
        }
        RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
