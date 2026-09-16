"""T021 R2 structural-collision audit.

Static, deterministic audit of ambiguity-critical construction recipes in the
canonical R2 generator. This does not measure human recognition or raster
quality. It asks a narrower prerequisite question: do distinct characters rely
on materially distinct construction topology before spacing/kerning?
"""
import json
from pathlib import Path

OUT = Path('/tmp/t021-r2-structural-audit')
OUT.mkdir(exist_ok=True)

# Normalized construction signatures derived directly from
# T021-logmate-operational-family-expansion-harness.py R2 source.
# Coordinate/width differences are intentionally removed so topology collisions
# cannot be hidden by advance-width differences.
signatures = {
    'S': ('top','middle','bottom','left-upper','right-lower'),
    '5': ('top','middle','bottom','left-upper','right-lower'),
    'D': ('left-full','top','bottom','right-full'),
    'O': ('left-full','top','bottom','right-full'),
    '0': ('left-full','top','bottom','right-full'),
    'I': ('top','bottom','center-stem'),
    '1': ('center-stem','base','upper-flag'),
    'l': ('narrow-stem','foot'),
    '8': ('upper-ring','lower-ring'),
    'B': ('left-full','top','middle','bottom','right-upper','right-lower'),
}

pairs = ['5S','DO','0O','1I','1l','8B']
rows = []
for pair in pairs:
    a,b = pair
    same = signatures[a] == signatures[b]
    rows.append({
        'pair': pair,
        'same_normalized_topology': same,
        'a_signature': signatures[a],
        'b_signature': signatures[b],
    })

result = {
    'revision': 'R2-structural-source-audit',
    'scope': 'ambiguity-critical and control pairs; static source topology only',
    'pairs': rows,
    'exact_topology_collisions': [r['pair'] for r in rows if r['same_normalized_topology']],
    'drawing_gate': 'FAIL' if any(r['same_normalized_topology'] for r in rows) else 'OPEN',
    'human_recognition_claim': False,
    'raster_quality_claim': False,
    'kerning_eligible': False,
}

path = OUT / 'T021-r2-structural-collision-audit-results.json'
path.write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
