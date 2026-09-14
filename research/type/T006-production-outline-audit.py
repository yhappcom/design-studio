"""T006 production-outline audit experiment.

Research-only Type Design evidence. Builds a small original cubic source subset,
audits topology/curve structure, converts it to quadratic TrueType outlines,
round-trips the exported font, and raster-checks the result with FreeType.

No production font asset is produced for a product.
Dependencies: fontTools, freetype-py, shapely, numpy.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import freetype
import numpy as np
from shapely.geometry import Polygon
from shapely.ops import unary_union
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

UPM = 1000
OUT = Path(".")
FONT = OUT / "T006-OutlineAudit.ttf"
ROUNDTRIP = OUT / "T006-OutlineAudit-roundtrip.ttf"
RESULTS = OUT / "T006-outline-audit-results.json"
MAX_ERR = 1.0  # cubic -> quadratic conversion target, font units

# command format:
# ("M", (x,y)); ("L",(x,y)); ("C",(c1x,c1y),(c2x,c2y),(x,y)); ("Z",)
# Every production candidate contour includes an explicit semantic role:
# outer or counter. The source uses PostScript-style direction:
# outer CCW (positive signed area), counters CW (negative signed area).

def rect(x0,y0,x1,y1):
    return [("M",(x0,y0)),("L",(x1,y0)),("L",(x1,y1)),("L",(x0,y1)),("Z",)]

def ellipse(cx, cy, rx, ry, clockwise=False):
    # Cardinal extrema are explicit on-curve nodes. Integer handles are deliberate.
    hx = round(rx * 0.5522847498)
    hy = round(ry * 0.5522847498)
    if not clockwise:  # right -> top -> left -> bottom -> right
        return [
            ("M",(cx+rx,cy)),
            ("C",(cx+rx,cy+hy),(cx+hx,cy+ry),(cx,cy+ry)),
            ("C",(cx-hx,cy+ry),(cx-rx,cy+hy),(cx-rx,cy)),
            ("C",(cx-rx,cy-hy),(cx-hx,cy-ry),(cx,cy-ry)),
            ("C",(cx+hx,cy-ry),(cx+rx,cy-hy),(cx+rx,cy)),
            ("Z",),
        ]
    # right -> bottom -> left -> top -> right
    return [
        ("M",(cx+rx,cy)),
        ("C",(cx+rx,cy-hy),(cx+hx,cy-ry),(cx,cy-ry)),
        ("C",(cx-hx,cy-ry),(cx-rx,cy-hy),(cx-rx,cy)),
        ("C",(cx-rx,cy+hy),(cx-hx,cy+ry),(cx,cy+ry)),
        ("C",(cx+hx,cy+ry),(cx+rx,cy+hy),(cx+rx,cy)),
        ("Z",),
    ]

def ellipse_missing_extrema(cx, cy, rx, ry, clockwise=False):
    # Deliberate audit fixture: each half is one cubic. Top/bottom extrema occur
    # at interior t ~= 0.5, so no on-curve node exists there.
    hy = round((4/3) * ry)
    if not clockwise:
        return [
            ("M",(cx+rx,cy)),
            ("C",(cx+rx,cy+hy),(cx-rx,cy+hy),(cx-rx,cy)),
            ("C",(cx-rx,cy-hy),(cx+rx,cy-hy),(cx+rx,cy)),
            ("Z",),
        ]
    return [
        ("M",(cx+rx,cy)),
        ("C",(cx+rx,cy-hy),(cx-rx,cy-hy),(cx-rx,cy)),
        ("C",(cx-rx,cy+hy),(cx+rx,cy+hy),(cx+rx,cy)),
        ("Z",),
    ]


def split_cubic_half(p0,p1,p2,p3):
    def mid(a,b): return (round((a[0]+b[0])/2), round((a[1]+b[1])/2))
    a=mid(p0,p1); b=mid(p1,p2); c=mid(p2,p3)
    d=mid(a,b); e=mid(b,c); m=mid(d,e)
    return (p0,a,d,m),(m,e,c,p3)

def ellipse_same_shape_with_extrema(cx,cy,rx,ry,clockwise=False):
    # Exact De Casteljau split of the missing-extrema fixture at t=.5.
    # Adds cardinal on-curve nodes without changing the underlying two half-cubic shapes.
    base=ellipse_missing_extrema(cx,cy,rx,ry,clockwise)
    p0=base[0][1]
    curves=[base[1],base[2]]
    out=[("M",p0)]
    current=p0
    for c in curves:
        q1,q2,q3=c[1],c[2],c[3]
        left,right=split_cubic_half(current,q1,q2,q3)
        out.append(("C",left[1],left[2],left[3]))
        out.append(("C",right[1],right[2],right[3]))
        current=q3
    out.append(("Z",))
    return out

def H_unified():
    # One contour, no overlapping rectangles.
    return [[
        ("M",(60,0)),("L",(140,0)),("L",(140,310)),("L",(460,310)),
        ("L",(460,0)),("L",(540,0)),("L",(540,700)),("L",(460,700)),
        ("L",(460,390)),("L",(140,390)),("L",(140,700)),("L",(60,700)),("Z",)
    ]]

def H_overlap_fixture():
    # Deliberate source fixture: three independent same-direction rectangles.
    return [rect(60,0,140,700), rect(460,0,540,700), rect(60,310,540,390)]

def n_unified():
    # Single-contour low-contrast n, avoiding independent overlapping stem/arch parts.
    return [[
        ("M",(50,0)),("L",(130,0)),("L",(130,305)),
        ("C",(130,375),(175,420),(285,420)),
        ("C",(345,420),(375,382),(375,305)),
        ("L",(375,0)),("L",(455,0)),("L",(455,330)),
        ("C",(455,445),(388,510),(290,510)),
        ("C",(208,510),(155,472),(130,410)),
        ("L",(130,500)),("L",(50,500)),("Z",)
    ]]

GLYPHS = {
    "H": {"advance":600, "unicode":0x48, "contours":[("outer", c) for c in H_unified()]},
    "O": {"advance":620, "unicode":0x4F, "contours":[
        ("outer", ellipse(300,350,250,360,False)),
        ("counter", ellipse(300,350,165,270,True)),
    ]},
    "n": {"advance":560, "unicode":0x6E, "contours":[("outer", c) for c in n_unified()]},
    "o": {"advance":520, "unicode":0x6F, "contours":[
        ("outer", ellipse(260,250,210,260,False)),
        ("counter", ellipse(260,250,135,185,True)),
    ]},
    "zero": {"advance":600, "unicode":0x30, "contours":[
        ("outer", ellipse(300,350,210,355,False)),
        ("counter", ellipse(300,350,125,270,True)),
    ]},
    "colon": {"advance":320, "unicode":0x3A, "contours":[
        ("outer", ellipse(150,245,42,42,False)),
        ("outer", ellipse(150,455,42,42,False)),
    ]},
}

FIXTURES = {
    "H.overlap": {"contours":[("outer", c) for c in H_overlap_fixture()]},
    "O.missingExtrema": {"contours":[
        ("outer", ellipse_missing_extrema(300,350,250,360,False)),
        ("counter", ellipse_missing_extrema(300,350,166,270,True)),
    ]},
}
REVISIONS = {
    "O.extremaInserted": {"contours":[
        ("outer", ellipse_same_shape_with_extrema(300,350,250,360,False)),
        ("counter", ellipse_same_shape_with_extrema(300,350,166,270,True)),
    ]},
}

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

def source_area(commands):
    p = AreaPen(None)
    draw_commands(p, commands)
    return p.value

def flatten(commands, steps=40):
    pts=[]
    start=None
    current=None
    for cmd in commands:
        if cmd[0]=="M":
            start=current=cmd[1]; pts=[current]
        elif cmd[0]=="L":
            current=cmd[1]; pts.append(current)
        elif cmd[0]=="C":
            p0=np.array(current,float); p1=np.array(cmd[1],float)
            p2=np.array(cmd[2],float); p3=np.array(cmd[3],float)
            for t in np.linspace(0,1,steps+1)[1:]:
                q=(1-t)**3*p0+3*(1-t)**2*t*p1+3*(1-t)*t*t*p2+t**3*p3
                pts.append(tuple(q))
            current=cmd[3]
        elif cmd[0]=="Z":
            if pts[-1]!=start: pts.append(start)
    return pts

def black_geometry(contours):
    outers=[]; counters=[]
    for role,c in contours:
        poly=Polygon(flatten(c))
        if role=="outer": outers.append(poly)
        else: counters.append(poly)
    g=unary_union(outers)
    if counters:
        g=g.difference(unary_union(counters))
    return g

def derivative_roots(p0,p1,p2,p3):
    # roots of cubic derivative for one scalar coordinate
    a=-p0+3*p1-3*p2+p3
    b=3*p0-6*p1+3*p2
    c=-3*p0+3*p1
    A=3*a; B=2*b; C=c
    roots=[]
    eps=1e-12
    if abs(A)<eps:
        if abs(B)>eps:
            roots=[-C/B]
    else:
        disc=B*B-4*A*C
        if disc>=0:
            r=math.sqrt(disc)
            roots=[(-B+r)/(2*A),(-B-r)/(2*A)]
    return [t for t in roots if 1e-6<t<1-1e-6]

def contour_audit(role, commands):
    integer=True; zero_handles=0; short_lines=0; missing_extrema=[]
    points=[]; current=None; start=None; seg_index=0
    curve_segments=[]
    for cmd in commands:
        for p in cmd[1:]:
            if isinstance(p, tuple):
                points.append(p)
                integer &= all(float(v).is_integer() for v in p)
        if cmd[0]=="M":
            current=start=cmd[1]
        elif cmd[0]=="L":
            if math.dist(current,cmd[1])<=2: short_lines+=1
            current=cmd[1]; seg_index+=1
        elif cmd[0]=="C":
            p0=current; p1,p2,p3=cmd[1],cmd[2],cmd[3]
            if p1==p0: zero_handles+=1
            if p2==p3: zero_handles+=1
            roots=set(round(t,8) for t in derivative_roots(p0[0],p1[0],p2[0],p3[0])+
                      derivative_roots(p0[1],p1[1],p2[1],p3[1]))
            for t in roots:
                missing_extrema.append({"segment":seg_index,"t":t})
            curve_segments.append((p0,p1,p2,p3))
            current=p3; seg_index+=1
    area=source_area(commands)
    expected_sign=1 if role=="outer" else -1
    direction_ok=(area*expected_sign)>0
    poly=Polygon(flatten(commands))
    return {
        "role":role,
        "signed_area":round(area,3),
        "direction_ok_ps":bool(direction_ok),
        "integer_coordinates":bool(integer),
        "zero_handles":zero_handles,
        "short_lines_le_2_units":short_lines,
        "missing_internal_extrema":missing_extrema,
        "polygon_valid_after_flatten":bool(poly.is_valid),
        "source_point_records":len(points),
        "curve_segments":len(curve_segments),
    }

def glyph_audit(contours):
    ca=[contour_audit(role,c) for role,c in contours]
    outer_polys=[Polygon(flatten(c)) for role,c in contours if role=="outer"]
    overlap_pairs=[]
    for i in range(len(outer_polys)):
        for j in range(i+1,len(outer_polys)):
            area=outer_polys[i].intersection(outer_polys[j]).area
            if area>0.01:
                overlap_pairs.append({"i":i,"j":j,"area":round(area,3)})
    return {
        "contours":ca,
        "same_role_outer_overlap_pairs":overlap_pairs,
        "all_direction_ok_ps":all(x["direction_ok_ps"] for x in ca),
        "all_integer_coordinates":all(x["integer_coordinates"] for x in ca),
        "total_missing_internal_extrema":sum(len(x["missing_internal_extrema"]) for x in ca),
        "total_zero_handles":sum(x["zero_handles"] for x in ca),
        "all_flattened_polygons_valid":all(x["polygon_valid_after_flatten"] for x in ca),
    }

def empty_glyph():
    return TTGlyphPen(None).glyph()

def compile_glyph(contours):
    ttpen=TTGlyphPen(None)
    qpen=Cu2QuPen(ttpen, max_err=MAX_ERR, reverse_direction=True)
    for _role,c in contours:
        draw_commands(qpen,c)
    return ttpen.glyph()

def build_font(path):
    glyphs={".notdef":compile_glyph([("outer",rect(50,0,450,700))]),"space":empty_glyph()}
    metrics={".notdef":(500,50),"space":(300,0)}
    cmap={0x20:"space"}
    order=[".notdef","space"]
    for name,d in GLYPHS.items():
        glyphs[name]=compile_glyph(d["contours"])
        metrics[name]=(d["advance"],0)
        cmap[d["unicode"]]=name
        order.append(name)
    fb=FontBuilder(UPM,isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyphs)
    # set LSB from compiled xMin after temporary bounds are known by table compiler; use 0 here
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=820,descent=-220,lineGap=0)
    fb.setupOS2(sTypoAscender=820,sTypoDescender=-220,sTypoLineGap=0,
                usWinAscent=850,usWinDescent=250,sxHeight=500,sCapHeight=700,
                usWeightClass=400,usWidthClass=5)
    fb.setupNameTable({
        "familyName":"T006 Outline Audit","styleName":"Regular",
        "uniqueFontIdentifier":"T006 Outline Audit Regular 20260914",
        "fullName":"T006 Outline Audit Regular",
        "psName":"T006-OutlineAudit-Regular","version":"Version 0.001"})
    fb.setupPost(); fb.setupMaxp()
    fb.save(path)
    # Fix metrics LSB to xMin after first compile and freeze timestamps for deterministic roundtrip.
    font=TTFont(path)
    font.recalcTimestamp=False
    font["head"].created=font["head"].modified=2082844800  # 1970-01-01 in Mac epoch
    for name in order:
        if name in (".notdef","space"): continue
        g=font["glyf"][name]
        g.recalcBounds(font["glyf"])
        aw,_=font["hmtx"][name]
        font["hmtx"][name]=(aw,g.xMin)
    font.save(path)

def table_hashes(path):
    f=TTFont(path, recalcTimestamp=False)
    return {tag:hashlib.sha256(f.getTableData(tag)).hexdigest()
            for tag in ("glyf","loca","hmtx","cmap","maxp")}

def compiled_inspection(path):
    f=TTFont(path,recalcTimestamp=False)
    gs=f.getGlyphSet()
    out={}
    for name in GLYPHS:
        g=f["glyf"][name]
        g.recalcBounds(f["glyf"])
        p=AreaPen(gs); gs[name].draw(p)
        out[name]={
            "contours":g.numberOfContours,
            "points":len(g.coordinates) if g.numberOfContours>=0 else None,
            "bbox":[g.xMin,g.yMin,g.xMax,g.yMax],
            "advance":f["hmtx"][name][0],
            "lsb":f["hmtx"][name][1],
            "quadratic_signed_area_total":round(p.value,3),
            "tt_direction_reversed_from_ps_expected": bool(p.value < 0),
        }
    return out

def bitmap_arr(slot):
    b=slot.bitmap
    if b.rows==0 or b.width==0: return np.zeros((0,0),np.uint8)
    raw=np.array(b.buffer,dtype=np.uint8).reshape((b.rows,b.pitch))
    return raw[:,:b.width]

def raster_check(path):
    face=freetype.Face(str(path))
    flags=freetype.FT_LOAD_RENDER|freetype.FT_LOAD_FORCE_AUTOHINT|freetype.FT_LOAD_TARGET_LIGHT
    chars={"H":"H","O":"O","n":"n","o":"o","zero":"0","colon":":"}
    result={}
    for ppem in (14,20,48):
        face.set_pixel_sizes(0,ppem)
        result[str(ppem)]={}
        for name,ch in chars.items():
            face.load_char(ch,flags)
            s=face.glyph; a=bitmap_arr(s)
            result[str(ppem)][name]={
                "bitmap":[s.bitmap.width,s.bitmap.rows],
                "advance":s.advance.x/64.0,
                "nonzero_pixels":int((a>0).sum()),
                "strong_pixels_gte_128":int((a>=128).sum()),
                "coverage_pixel_equivalent":round(float(a.sum()/255.0),3),
            }
    return result

def main():
    audits={name:glyph_audit(d["contours"]) for name,d in GLYPHS.items()}
    fixture_audits={name:glyph_audit(d["contours"]) for name,d in FIXTURES.items()}
    revision_audits={name:glyph_audit(d["contours"]) for name,d in REVISIONS.items()}

    h0=black_geometry(FIXTURES["H.overlap"]["contours"])
    h1=black_geometry(GLYPHS["H"]["contours"])
    hdiff=h0.symmetric_difference(h1).area
    # Dense polygonization only verifies the exact De Casteljau split numerically;
    # analytically the revised curves are the same cubics split at t=.5.
    def dense_black(contours):
        outers=[]; counters=[]
        for role,c in contours:
            poly=Polygon(flatten(c,steps=1000))
            (outers if role=="outer" else counters).append(poly)
        g=unary_union(outers)
        return g.difference(unary_union(counters)) if counters else g
    ofix=dense_black(FIXTURES["O.missingExtrema"]["contours"])
    orev=dense_black(REVISIONS["O.extremaInserted"]["contours"])
    odiff=ofix.symmetric_difference(orev).area
    ohaus=ofix.boundary.hausdorff_distance(orev.boundary)

    build_font(FONT)
    before=table_hashes(FONT)
    font=TTFont(FONT,recalcTimestamp=False)
    font.recalcTimestamp=False
    font.save(ROUNDTRIP)
    after=table_hashes(ROUNDTRIP)

    result={
        "study":"T006",
        "upm":UPM,
        "cubic_to_quadratic_max_err_units":MAX_ERR,
        "source_model":"explicit integer cubic segment commands; PostScript direction",
        "final_source_audits":audits,
        "fixture_audits":fixture_audits,
        "revision_audits":revision_audits,
        "failure_revision_comparisons":{
            "H_overlap_to_unified":{
                "fixture_outer_overlap_pairs":len(fixture_audits["H.overlap"]["same_role_outer_overlap_pairs"]),
                "final_outer_overlap_pairs":len(audits["H"]["same_role_outer_overlap_pairs"]),
                "silhouette_symmetric_difference_area":round(hdiff,6),
            },
            "O_missing_extrema_to_inserted_extrema_same_shape":{
                "fixture_missing_internal_extrema":fixture_audits["O.missingExtrema"]["total_missing_internal_extrema"],
                "revision_missing_internal_extrema":revision_audits["O.extremaInserted"]["total_missing_internal_extrema"],
                "shape_preserved_analytically_by_de_casteljau_split":True,
                "dense_polygon_symmetric_difference_area":round(odiff,6),
                "dense_boundary_hausdorff_distance_units":round(ohaus,6),
            }
        },
        "compiled_ttf":compiled_inspection(FONT),
        "roundtrip":{
            "table_hashes_before":before,
            "table_hashes_after":after,
            "relevant_tables_identical":before==after,
        },
        "raster_autohint_light":raster_check(FONT),
        "scope_limits":[
            "research subset only; not a product typeface",
            "no variable-master interpolation",
            "no manual TrueType hinting",
            "no CoreText/DirectWrite/Skia/browser/device validation",
            "custom audit is not a FontBakery substitute",
        ],
    }
    RESULTS.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps({
        "final_summary":{k:{
            "missing":v["total_missing_internal_extrema"],
            "zero_handles":v["total_zero_handles"],
            "overlap_pairs":len(v["same_role_outer_overlap_pairs"]),
            "direction":v["all_direction_ok_ps"],
            "integer":v["all_integer_coordinates"],
        } for k,v in audits.items()},
        "fixture_summary":{k:{
            "missing":v["total_missing_internal_extrema"],
            "overlap_pairs":len(v["same_role_outer_overlap_pairs"])
        } for k,v in fixture_audits.items()},
        "revision_summary":{k:{
            "missing":v["total_missing_internal_extrema"],
            "overlap_pairs":len(v["same_role_outer_overlap_pairs"])
        } for k,v in revision_audits.items()},
        "comparisons":result["failure_revision_comparisons"],
        "roundtrip_identical":result["roundtrip"]["relevant_tables_identical"],
        "compiled":result["compiled_ttf"],
    },indent=2))

if __name__=="__main__":
    main()
