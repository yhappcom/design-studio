#!/usr/bin/env python3
"""T018 LogMate conservative font candidate audit.

Linux control harness. It resolves installed open-source controls through
fontconfig, records exact hashes/metadata with fontTools, then uses Chromium
through Playwright to measure the LogMate corpus with exact @font-face files.

This is a controlled transfer harness, not Flutter/Android/iOS production proof.
It does not copy font binaries into the repository.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import shutil
import statistics
import subprocess
from pathlib import Path

from fontTools.ttLib import TTFont
from playwright.sync_api import sync_playwright

AIRPORTS = ["ICN", "NRT", "SIN", "JFK", "LHR", "CDG", "HND", "DXB", "FRA", "LAX"]
IDENTIFIERS = [
    "KE704", "BA117", "AF264", "B737-900", "B737-8", "A320-200",
    "HL8301", "N12345", "G-EUOH",
]
TIMES = ["00:45", "02:18", "09:55", "12:40", "1,284:35", "9,999:59"]
COUNTS = ["1", "11", "111", "8", "88", "888"]
PUNCTUATION = [":", "/", "-", ",", "+"]

CANDIDATES = {
    "Roboto": {"regular": "Roboto:style=Regular", "opening": "Roboto:style=Medium", "opening_weight": 500},
    "Inter": {"regular": "Inter:style=Regular", "opening": "Inter:style=SemiBold", "opening_weight": 600},
    "Noto Sans": {"regular": "Noto Sans:style=Regular", "opening": "Noto Sans:style=SemiBold", "opening_weight": 600},
}


def fc_file(pattern: str) -> str:
    value = subprocess.check_output(
        ["fc-match", "-f", "%{file}\n", pattern], text=True
    ).splitlines()[0].strip()
    if not value or not Path(value).exists():
        raise RuntimeError(f"Font not resolved: {pattern}")
    return value


def font_info(path: str) -> dict:
    raw = Path(path).read_bytes()
    font = TTFont(path, lazy=True)

    def name(name_id: int):
        for record in font["name"].names:
            if record.nameID == name_id:
                try:
                    return record.toUnicode()
                except Exception:
                    return str(record.string)
        return None

    features = []
    if "GSUB" in font:
        feature_list = font["GSUB"].table.FeatureList
        if feature_list:
            features = sorted({record.FeatureTag for record in feature_list.FeatureRecord})

    cmap = set()
    for table in font["cmap"].tables:
        if table.isUnicode():
            cmap.update(table.cmap.keys())

    os2 = font["OS/2"]
    return {
        "path": path,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "family": name(1),
        "subfamily": name(2),
        "version": name(5),
        "upm": font["head"].unitsPerEm,
        "weightClass": os2.usWeightClass,
        "xHeight": getattr(os2, "sxHeight", None),
        "capHeight": getattr(os2, "sCapHeight", None),
        "features": features,
        "supports": {
            "accentedLatin_é": 0x00E9 in cmap,
            "cyrillic_Ж": 0x0416 in cmap,
            "arabic_ا": 0x0627 in cmap,
            "hangul_가": 0xAC00 in cmap,
            "combiningAcute": 0x0301 in cmap,
        },
    }


def data_font_url(path: str) -> str:
    return "data:font/ttf;base64," + base64.b64encode(Path(path).read_bytes()).decode("ascii")


def main() -> None:
    chromium = shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")
    if not chromium:
        raise RuntimeError("Chromium executable not found")

    controls = {}
    for candidate, definition in CANDIDATES.items():
        regular = fc_file(definition["regular"])
        opening = fc_file(definition["opening"])
        controls[candidate] = {
            "regular_path": regular,
            "opening_path": opening,
            "opening_weight": definition["opening_weight"],
            "regular": font_info(regular),
            "opening": font_info(opening),
        }

    css = ["body{font-synthesis:none}"]
    family_names = {}
    for index, (candidate, control) in enumerate(controls.items()):
        family = f"T018F{index}"
        family_names[candidate] = family
        css.append(
            f"@font-face{{font-family:'{family}';src:url('{data_font_url(control['regular_path'])}');"
            "font-style:normal;font-weight:400;font-display:block}}"
        )
        css.append(
            f"@font-face{{font-family:'{family}';src:url('{data_font_url(control['opening_path'])}');"
            "font-style:normal;font-weight:600;font-display:block}}"
        )

    html = "<!doctype html><meta charset='utf-8'><style>" + "".join(css) + "</style><body></body>"
    output = {
        "study": "T018",
        "environment": {},
        "controls": {},
        "measurements": {},
    }

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=chromium, headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900}, device_scale_factor=1)
        page.set_content(html, wait_until="load")
        page.evaluate("document.fonts.ready")
        output["environment"]["chromium"] = browser.version

        def width(family: str, text: str, size: float, weight: int = 400, tnum: bool = False) -> float:
            return page.evaluate(
                """([family,text,size,weight,tnum]) => {
                  const span=document.createElement('span');
                  span.textContent=text;
                  span.style.cssText=`position:absolute;visibility:hidden;white-space:pre;display:inline-block;`
                    + `font-family:'${family}';font-size:${size}px;font-weight:${weight};font-synthesis:none;`
                    + (tnum ? 'font-variant-numeric:tabular-nums;' : '');
                  document.body.appendChild(span);
                  const value=span.getBoundingClientRect().width;
                  span.remove(); return value;
                }""",
                [family, text, size, weight, tnum],
            )

        for candidate, control in controls.items():
            family = family_names[candidate]
            airport = {value: width(family, value, 17, 600) for value in AIRPORTS}
            airport_200 = {value: width(family, value, 34, 600) for value in AIRPORTS}
            identifiers = {value: width(family, value, 15) for value in IDENTIFIERS}
            digit_prop = {value: width(family, value, 15) for value in "0123456789"}
            digit_tnum = {value: width(family, value, 15, tnum=True) for value in "0123456789"}
            time_tnum = {value: width(family, value, 15, tnum=True) for value in TIMES}
            punctuation = {value: width(family, value, 15) for value in PUNCTUATION}
            values = list(airport.values())

            fits = {
                "opening_airport_100": {value: measured <= 56 for value, measured in airport.items()},
                "opening_airport_200": {value: measured <= 56 for value, measured in airport_200.items()},
                "opening_time_100": {value: width(family, value, 17, 600, True) <= 68 for value in TIMES[:4]},
                "opening_time_200": {value: width(family, value, 34, 600, True) <= 68 for value in TIMES[:4]},
                "ledger_airport_100": {value: width(family, value, 15) <= 42 for value in AIRPORTS},
                "ledger_airport_200": {value: width(family, value, 30) <= 42 for value in AIRPORTS},
                "ledger_registration_100": {value: width(family, value, 15) <= 76 for value in ["HL8301", "N12345", "G-EUOH"]},
                "ledger_registration_200": {value: width(family, value, 30) <= 76 for value in ["HL8301", "N12345", "G-EUOH"]},
                "ledger_total_100": {value: width(family, value, 15, tnum=True) <= 84 for value in ["1,284:35", "9,999:59"]},
                "ledger_total_200": {value: width(family, value, 30, tnum=True) <= 84 for value in ["1,284:35", "9,999:59"]},
            }

            output["controls"][candidate] = {
                "regular": control["regular"],
                "opening_role_face": control["opening"],
                "modeled_opening_weight": control["opening_weight"],
            }
            output["measurements"][candidate] = {
                "airport_17px": airport,
                "airport_stats": {
                    "min": min(values),
                    "max": max(values),
                    "mean": statistics.mean(values),
                    "range": max(values) - min(values),
                    "range_pct_mean": (max(values) - min(values)) / statistics.mean(values) * 100,
                },
                "identifiers_15px": identifiers,
                "digit_prop_spread_15px": max(digit_prop.values()) - min(digit_prop.values()),
                "digit_tnum_spread_15px": max(digit_tnum.values()) - min(digit_tnum.values()),
                "times_tnum_15px": time_tnum,
                "punctuation_15px": punctuation,
                "fit_failures": {
                    name: [value for value, passes in checks.items() if not passes]
                    for name, checks in fits.items()
                },
            }

        browser.close()

    out_path = Path(__file__).with_name("T018-logmate-conservative-font-candidate-results.json")
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
