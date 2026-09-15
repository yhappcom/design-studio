"""Deterministic corpus-coverage audit for the current T021 mini-family.

The proven T021 repertoire comes from T021-broader-mini-family-prekerning-transfer.py:
H O n o A V T L I + space. This audit does not infer unbuilt glyphs.
"""
from pathlib import Path
import json, string

AIRPORTS = ["ICN","NRT","SIN","JFK","LHR","CDG","HND","DXB","FRA","LAX"]
IDENTIFIERS = ["KE704","BA117","AF264","B737-900","B737-8","A320-200","HL8301","N12345","G-EUOH"]
NUMERIC = ["00:45","02:18","09:55","12:40","1,284:35","9,999:59","1","11","111","8","88","888"]
AMBIGUITY = ["0O","1Il","5S","8B"]
CURRENT_T021 = set("HOnoAVTLI ")
UPPER = set(string.ascii_uppercase)
DIGITS = set(string.digits)
PUNCT = set("-,:/")

def charset(items):
    return set("".join(items))

def row(name, required):
    covered = required & CURRENT_T021
    missing = required - CURRENT_T021
    return {
        "name": name,
        "required": sorted(required),
        "requiredCount": len(required),
        "covered": sorted(covered),
        "coveredCount": len(covered),
        "coveragePct": round(100 * len(covered) / len(required), 2) if required else 100.0,
        "missing": sorted(missing),
    }

airport = charset(AIRPORTS)
identifier = charset(IDENTIFIERS)
numeric = charset(NUMERIC)
ambiguity = charset(AMBIGUITY)
all_required = airport | identifier | numeric | ambiguity

result = {
    "study": "T021 LogMate operational glyph coverage audit",
    "currentProvenT021Characters": sorted(CURRENT_T021),
    "corpus": {
        "airports": AIRPORTS,
        "identifiers": IDENTIFIERS,
        "numeric": NUMERIC,
        "ambiguity": AMBIGUITY,
    },
    "coverage": [
        row("airport uppercase", airport & UPPER),
        row("identifier uppercase", identifier & UPPER),
        row("identifier digits", identifier & DIGITS),
        row("identifier punctuation", identifier & PUNCT),
        row("numeric digits", numeric & DIGITS),
        row("numeric punctuation", numeric & PUNCT),
        row("ambiguity characters", ambiguity),
        row("all corpus characters", all_required),
    ],
}

Path("/tmp/T021-logmate-operational-glyph-coverage-results.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(json.dumps(result, indent=2, ensure_ascii=False))
