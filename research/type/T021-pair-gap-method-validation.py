"""T021 pair-gap method validation using mature-font OUTLINE geometry.

Research-only. This independently checks whether same-y scanline gaps of the
magnitude seen in T021 B are unusual in mature production fonts.
Kerning is not applied in the geometric scanline calculation.
"""
from fontTools.ttLib import TTFont
from fontTools.pens.basePen import BasePen
from pathlib import Path
import hashlib, json

FONTS = {
    "Inter": "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
    "Noto Sans": "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    "Lato": "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
    "DejaVu Sans": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "Liberation Mono": "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
}
PAIRS = ["AV", "VA", "TA", "AT", "LI", "IL"]
FRACTIONS = [0.0, 85/700, 350/700, 615/700, 1.0]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def name_record(tt, name_id):
    for rec in tt["name"].names:
        if rec.nameID == name_id:
            try:
                return rec.toUnicode()
            except Exception:
                pass
    return None


class FlattenPen(BasePen):
    """Flatten outlines to short line segments for scanline intersection.

    64 samples/curve is intentionally high relative to the simple Latin control
    geometry. The result is an outline-geometry approximation, not raster output.
    """
    def __init__(self, glyphSet, steps=64):
        super().__init__(glyphSet)
        self.steps = steps
        self.segments = []
        self.start = None
        self.current = None

    def _moveTo(self, p0):
        self.start = tuple(map(float, p0))
        self.current = self.start

    def _lineTo(self, p1):
        p1 = tuple(map(float, p1))
        if self.current is not None:
            self.segments.append((self.current, p1))
        self.current = p1

    def _curveToOne(self, p1, p2, p3):
        p0 = self.current
        p1, p2, p3 = map(lambda p: tuple(map(float, p)), (p1,p2,p3))
        prev = p0
        for i in range(1, self.steps + 1):
            t = i / self.steps
            u = 1 - t
            q = (
                u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
                u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1],
            )
            self.segments.append((prev, q)); prev = q
        self.current = p3

    def _qCurveToOne(self, p1, p2):
        p0 = self.current
        p1, p2 = map(lambda p: tuple(map(float, p)), (p1,p2))
        prev = p0
        for i in range(1, self.steps + 1):
            t = i / self.steps
            u = 1 - t
            q = (
                u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0],
                u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1],
            )
            self.segments.append((prev, q)); prev = q
        self.current = p2

    def _closePath(self):
        if self.current is not None and self.start is not None and self.current != self.start:
            self.segments.append((self.current, self.start))
        self.current = self.start

    def _endPath(self):
        self.current = None
        self.start = None


def scanline_extent(segments, y, eps=1e-7):
    """Return min/max x intersections at y; handle horizontal segments too."""
    xs = []
    for (x0,y0),(x1,y1) in segments:
        if abs(y1-y0) < eps:
            if abs(y-y0) < eps:
                xs.extend([x0,x1])
            continue
        lo, hi = sorted((y0,y1))
        if y < lo-eps or y > hi+eps:
            continue
        t = (y-y0)/(y1-y0)
        if -eps <= t <= 1+eps:
            xs.append(x0 + t*(x1-x0))
    if not xs:
        return None
    return (min(xs), max(xs))


def glyph_segments(gs, char):
    pen = FlattenPen(gs)
    gs[char].draw(pen)
    return pen.segments


def cap_height(tt, gs):
    cap = getattr(tt["OS/2"], "sCapHeight", None) if "OS/2" in tt else None
    if cap:
        return float(cap)
    segs = glyph_segments(gs, "H")
    return max(max(a[1], b[1]) for a,b in segs)


def metric(tt, glyph_name):
    return tt["hmtx"].metrics[glyph_name]


result = {
    "study": "T021 pair-gap outline method validation",
    "purpose": "CONTRADICTION REVIEW + INDEPENDENT VALIDATION + METHOD COMPARISON",
    "method": "mature-font outline flattening; kerning-off gap=advance(X)+leftBoundary(Y)-rightBoundary(X); 64 samples/curve; normalized per 1000 UPM",
    "fonts": {},
    "t021_B_prior_per1000": {
        "AV": [300.0,296.4,285.0,273.6,270.0],
        "VA": [300.0,296.4,285.0,273.6,270.0],
        "TA": [300.0,320.6,385.0,239.4,260.0],
        "AT": [300.0,320.6,385.0,239.4,260.0],
        "LI": [114.0,114.0,543.0,455.0,455.0],
        "IL": [114.0,114.0,202.0,114.0,114.0],
    },
}

for label, path in FONTS.items():
    tt = TTFont(path)
    gs = tt.getGlyphSet()
    cmap = tt.getBestCmap()
    upm = tt["head"].unitsPerEm
    cap = cap_height(tt, gs)
    ys = [cap*f for f in FRACTIONS]
    char_data = {}
    for ch in sorted(set("".join(PAIRS))):
        gn = cmap[ord(ch)]
        segs = glyph_segments(gs, gn)
        ext = [scanline_extent(segs, y) for y in ys]
        aw, lsb = metric(tt, gn)
        char_data[ch] = {"glyph": gn, "advance": aw, "lsb": lsb, "extents": ext}
    pair_data = {}
    for pair in PAIRS:
        a,b = pair
        vals = []
        for i,y in enumerate(ys):
            ea, eb = char_data[a]["extents"][i], char_data[b]["extents"][i]
            if ea is None or eb is None:
                vals.append(None)
            else:
                gap = char_data[a]["advance"] + eb[0] - ea[1]
                vals.append(round(gap/upm*1000,3))
        pair_data[pair] = {
            "gapPer1000": vals,
            "min": None if all(v is None for v in vals) else min(v for v in vals if v is not None),
            "max": None if all(v is None for v in vals) else max(v for v in vals if v is not None),
        }
    result["fonts"][label] = {
        "path": path,
        "family": name_record(tt,1),
        "version": name_record(tt,5),
        "sha256": sha256(path),
        "upm": upm,
        "capHeight": cap,
        "sampleY": [round(y,3) for y in ys],
        "pairs": pair_data,
    }

Path('/tmp/T021-pair-gap-method-validation-results.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
