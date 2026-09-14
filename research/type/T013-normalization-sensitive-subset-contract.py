from pathlib import Path
import tempfile, json, hashlib, shutil, unicodedata
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.ttLib import TTFont
from fontTools import subset
import fontTools

UPM = 1000
RESULTS = Path("T013-normalization-sensitive-subset-contract-results.json")
RAW = "A\u0301\u0307"
NFD = unicodedata.normalize("NFD", RAW)
NFC = unicodedata.normalize("NFC", RAW)

def rect(x0, y0, x1, y1):
    p = TTGlyphPen(None)
    p.moveTo((x0, y0)); p.lineTo((x1, y0)); p.lineTo((x1, y1)); p.lineTo((x0, y1)); p.closePath()
    return p.glyph()

def build(path):
    order = [".notdef", "A", "Aacute", "acutecomb", "dotabovecomb"]
    glyphs = {
        ".notdef": rect(50, 0, 450, 700),
        "A": rect(80, 0, 520, 700),
        "Aacute": rect(80, 0, 520, 880),
        "acutecomb": rect(60, 0, 140, 180),
        "dotabovecomb": rect(70, 0, 130, 60),
    }
    metrics = {
        ".notdef": (500, 50), "A": (600, 80), "Aacute": (600, 80),
        "acutecomb": (0, 60), "dotabovecomb": (0, 70)
    }
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap({0x0041: "A", 0x00C1: "Aacute", 0x0301: "acutecomb", 0x0307: "dotabovecomb"})
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=900, descent=-250)
    fb.setupOS2(sTypoAscender=850, sTypoDescender=-200, usWinAscent=950, usWinDescent=250, usWeightClass=400)
    fb.setupNameTable({
        "familyName": "T013 Research", "styleName": "Regular",
        "uniqueFontIdentifier": "T013Research-Regular",
        "fullName": "T013 Research Regular", "psName": "T013Research-Regular"
    })
    fb.setupPost(); fb.setupMaxp(); fb.save(path)
    f = TTFont(path)
    addOpenTypeFeaturesFromString(f, """
languagesystem DFLT dflt;
languagesystem latn dflt;
markClass acutecomb <anchor 100 0> @TOP;
markClass dotabovecomb <anchor 100 0> @TOP;
feature mark {
  pos base A <anchor 300 700> mark @TOP;
  pos base Aacute <anchor 300 880> mark @TOP;
} mark;
feature mkmk {
  pos mark acutecomb <anchor 100 220> mark @TOP;
} mkmk;
""")
    f["head"].flags |= 2
    f.recalcTimestamp = False
    f.save(path)

def subset_font(src, dst, text):
    opts = subset.Options()
    opts.layout_features = ["*"]
    opts.layout_scripts = ["*"]
    opts.name_IDs = ["*"]
    opts.name_legacy = True
    opts.name_languages = ["*"]
    opts.recalc_timestamp = False
    s = subset.Subsetter(options=opts)
    s.populate(text=text)
    f = TTFont(src)
    s.subset(f)
    f.recalcTimestamp = False
    f.save(dst)

def make_woff2(src, dst):
    f = TTFont(src)
    f.flavor = "woff2"
    f.recalcTimestamp = False
    f.save(dst)

def anchor(a):
    return None if a is None else [a.XCoordinate, a.YCoordinate]

def semantics(font):
    out = {"mark_to_base": [], "mark_to_mark": []}
    if "GPOS" not in font or not font["GPOS"].table.LookupList:
        return out
    for lookup in font["GPOS"].table.LookupList.Lookup:
        for st in lookup.SubTable:
            if lookup.LookupType == 4:
                out["mark_to_base"].append({
                    "marks": [{"glyph": g, "class": r.Class, "anchor": anchor(r.MarkAnchor)}
                              for g, r in zip(st.MarkCoverage.glyphs, st.MarkArray.MarkRecord)],
                    "bases": [{"glyph": g, "anchors": [anchor(a) for a in r.BaseAnchor]}
                              for g, r in zip(st.BaseCoverage.glyphs, st.BaseArray.BaseRecord)],
                })
            elif lookup.LookupType == 6:
                out["mark_to_mark"].append({
                    "mark1": [{"glyph": g, "class": r.Class, "anchor": anchor(r.MarkAnchor)}
                              for g, r in zip(st.Mark1Coverage.glyphs, st.Mark1Array.MarkRecord)],
                    "mark2": [{"glyph": g, "anchors": [anchor(a) for a in r.Mark2Anchor]}
                              for g, r in zip(st.Mark2Coverage.glyphs, st.Mark2Array.Mark2Record)],
                })
    return out

def cpseq(s):
    return [f"U+{ord(c):04X}" for c in s]

def has_all(cmap, s):
    return all(ord(c) in cmap for c in s)

def audit(path):
    f = TTFont(path)
    cmap = f.getBestCmap()
    sem = semantics(f)
    hmtx = f["hmtx"].metrics

    A = cmap.get(0x0041)
    Aacute = cmap.get(0x00C1)
    acute = cmap.get(0x0301)
    dot = cmap.get(0x0307)

    def mtb(mark_g, base_g, mark_anchor, base_anchor):
        if not mark_g or not base_g:
            return False
        for item in sem["mark_to_base"]:
            mark_ok = any(r["glyph"] == mark_g and r["anchor"] == mark_anchor for r in item["marks"])
            base_ok = any(r["glyph"] == base_g and base_anchor in r["anchors"] for r in item["bases"])
            if mark_ok and base_ok:
                return True
        return False

    def mtm(mark1_g, mark2_g, mark1_anchor, mark2_anchor):
        if not mark1_g or not mark2_g:
            return False
        for item in sem["mark_to_mark"]:
            m1 = any(r["glyph"] == mark1_g and r["anchor"] == mark1_anchor for r in item["mark1"])
            m2 = any(r["glyph"] == mark2_g and mark2_anchor in r["anchors"] for r in item["mark2"])
            if m1 and m2:
                return True
        return False

    nfd_contract = {
        "coverage": has_all(cmap, NFD),
        "zero_advance_marks": bool(acute and dot and hmtx[acute][0] == 0 and hmtx[dot][0] == 0),
        "acute_to_A": mtb(acute, A, [100, 0], [300, 700]),
        "dot_to_acute": mtm(dot, acute, [100, 0], [100, 220]),
    }
    nfc_contract = {
        "coverage": has_all(cmap, NFC),
        "zero_advance_dot": bool(dot and hmtx[dot][0] == 0),
        "dot_to_Aacute": mtb(dot, Aacute, [100, 0], [300, 880]),
    }
    return {
        "file": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "size": path.stat().st_size,
        "flavor": f.flavor,
        "glyphs": f.getGlyphOrder(),
        "cmap": {f"U+{cp:04X}": g for cp, g in sorted(cmap.items())},
        "nfd_contract": nfd_contract,
        "nfd_pass": all(nfd_contract.values()),
        "nfc_contract": nfc_contract,
        "nfc_pass": all(nfc_contract.values()),
        "semantics": sem,
    }

def main():
    tools = {n: shutil.which(n) for n in ["fontbakery", "fontspector", "ots-sanitize", "hb-shape"]}
    with tempfile.TemporaryDirectory(prefix="t013_") as td:
        d = Path(td)
        source = d / "source.ttf"
        build(source)

        modes = {"nfd_only": NFD, "nfc_only": NFC, "dual": NFD + NFC}
        artifacts = {}
        source_woff2 = d / "source.woff2"
        make_woff2(source, source_woff2)
        artifacts["source_woff2"] = audit(source_woff2)

        for name, text in modes.items():
            ttf = d / f"{name}.ttf"
            subset_font(source, ttf, text)
            woff2 = d / f"{name}.woff2"
            make_woff2(ttf, woff2)
            artifacts[name + "_woff2"] = audit(woff2)

        results = {
            "environment": {
                "python_unicodedata_version": unicodedata.unidata_version,
                "fonttools": fontTools.__version__,
                "external_tools": tools,
            },
            "normalization": {
                "raw": cpseq(RAW),
                "NFD": cpseq(NFD),
                "NFC": cpseq(NFC),
                "canonically_equivalent": unicodedata.normalize("NFC", NFD) == unicodedata.normalize("NFC", NFC),
            },
            "artifacts": artifacts,
            "derived": {
                "nfd_only_passes_nfd_fails_nfc": artifacts["nfd_only_woff2"]["nfd_pass"] and not artifacts["nfd_only_woff2"]["nfc_pass"],
                "nfc_only_passes_nfc_fails_nfd": artifacts["nfc_only_woff2"]["nfc_pass"] and not artifacts["nfc_only_woff2"]["nfd_pass"],
                "dual_passes_both": artifacts["dual_woff2"]["nfd_pass"] and artifacts["dual_woff2"]["nfc_pass"],
                "all_packages_parseable": all(a["size"] > 0 for a in artifacts.values()),
            },
            "scope_limits": [
                "Structural cmap/GPOS package audit only; no HarfBuzz/browser shaping was available.",
                "Synthetic Latin normalization specimen; not production complex-script or canonical-combining-class stress evidence.",
                "No guarantee that every product must support both NFC and NFD. The required contract depends on the product text-normalization boundary.",
                "External FontBakery/Fontspector/OTS unavailable; no sanitizer PASS claimed.",
            ],
        }
        RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
