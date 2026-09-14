"""T004 numeral/punctuation research font and FreeType measurement experiment.

Research only. This script builds a non-production TTF with an original
low-contrast constructed numeral system, proportional defaults, tabular
alternates, zero alternatives, ambiguity controls, and punctuation.

Dependencies: fontTools, freetype-py, numpy, shapely.
Outputs:
  T004-NumeralResearch.ttf
  T004-NumeralResearch.ttx
  T004-results.json

Raster contact sheets used during the study were generated from the same font
in the local inspection environment. They are not emitted by this canonical
script; the persistent evidence layer is the compiled-font source method plus
the measured JSON and summarized SVG evidence committed alongside it.
"""
from __future__ import annotations

import json, math
from pathlib import Path
import freetype
import numpy as np
from shapely.affinity import translate
from shapely.geometry import LineString, Point, Polygon
from shapely.geometry.polygon import orient
from shapely.ops import unary_union
from fontTools.fontBuilder import FontBuilder
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

UPM = 1000
OUT = Path(".")
FONT = OUT / "T004-NumeralResearch.ttf"
TTX = OUT / "T004-NumeralResearch.ttx"
RESULTS = OUT / "T004-results.json"
STROKE = 82

DIGITS = ["zero","one","two","three","four","five","six","seven","eight","nine"]
PROP_ADV = {"zero":600,"one":480,"two":570,"three":560,"four":600,
            "five":560,"six":580,"seven":560,"eight":590,"nine":580}
OPT_OFF = {"zero":0,"one":8,"two":-4,"three":-6,"four":0,
           "five":-4,"six":0,"seven":-7,"eight":0,"nine":0}
TAB_ADV = 620

def stroke(points, width=STROKE):
    return LineString(points).buffer(width/2, cap_style=1, join_style=1, resolution=12)

def ellipse(cx, cy, rx, ry, width=STROKE, n=128):
    pts=[(cx+rx*math.cos(2*math.pi*i/n), cy+ry*math.sin(2*math.pi*i/n))
         for i in range(n+1)]
    return stroke(pts, width)

def arc(cx, cy, rx, ry, a0, a1, width=STROKE, n=96):
    pts=[(cx+rx*math.cos(a), cy+ry*math.sin(a))
         for a in np.linspace(math.radians(a0), math.radians(a1), n)]
    return stroke(pts, width)

def circle(cx, cy, r):
    return Point(cx,cy).buffer(r, resolution=16)

def cubic(p0,p1,p2,p3,n=64):
    out=[]
    for t in np.linspace(0,1,n):
        m=1-t
        out.append((m**3*p0[0]+3*m*m*t*p1[0]+3*m*t*t*p2[0]+t**3*p3[0],
                    m**3*p0[1]+3*m*m*t*p1[1]+3*m*t*t*p2[1]+t**3*p3[1]))
    return out

def ellipse_polygon(cx,cy,rx,ry,n=128):
    return Polygon([(cx+rx*math.cos(2*math.pi*i/n),cy+ry*math.sin(2*math.pi*i/n))
                    for i in range(n)])

def to_glyph(geom, simplify=.6):
    geom=geom.simplify(simplify, preserve_topology=True)
    pen=TTGlyphPen(None)
    polys=[geom] if geom.geom_type=="Polygon" else list(geom.geoms)
    for poly in polys:
        p=orient(poly, sign=-1.0)
        for ring in [p.exterior, *p.interiors]:
            pts=list(ring.coords)[:-1]
            if len(pts)<3: continue
            pen.moveTo(pts[0])
            for pt in pts[1:]: pen.lineTo(pt)
            pen.closePath()
    return pen.glyph()

def centered(g, adv, off=0):
    x0,_,x1,_=g.bounds
    return translate(g, xoff=(adv/2+off)-(x0+x1)/2)

def digit_geoms():
    g={}
    g["zero"]=ellipse(300,350,200,310)
    g["one"]=unary_union([stroke([(300,650),(300,70)]),
                          stroke([(300,650),(220,585)]),
                          stroke([(200,70),(410,70)])])
    top=[(300+205*math.cos(a),520+150*math.sin(a))
         for a in np.linspace(math.radians(205),math.radians(10),80)]
    g["two"]=stroke(top+[(470,430),(150,90),(500,90)])
    g["three"]=unary_union([arc(285,510,185,150,140,-140),
                            arc(285,230,190,165,140,-140)])
    g["four"]=unary_union([stroke([(420,660),(140,250),(510,250)]),
                           stroke([(420,660),(420,55)])])
    g["five"]=unary_union([stroke([(500,650),(160,650),(150,390),(260,390)]),
                           arc(290,225,190,165,140,-140)])
    g["six"]=unary_union([ellipse(300,245,185,175),
                          stroke(cubic((135,300),(110,520),(190,650),(440,675),72))])
    g["seven"]=stroke([(135,650),(500,650),(235,60)])
    g["eight"]=unary_union([ellipse(300,505,165,145),ellipse(300,205,180,165)])
    g["nine"]=unary_union([ellipse(300,455,185,175),
                           stroke(cubic((465,405),(485,245),(430,125),(210,60),72))])
    return g

def controls():
    return {
      "O":ellipse(300,350,225,315),
      "I":unary_union([stroke([(300,650),(300,50)]),
                       stroke([(185,650),(415,650)]),
                       stroke([(180,50),(420,50)])]),
      "l":stroke([(280,690),(280,120),*cubic((280,120),(280,65),(305,45),(350,45),24)[1:]]),
      "S":stroke(cubic((455,590),(390,690),(150,675),(145,515),45)
                 +cubic((145,515),(150,380),(465,395),(455,210),45)[1:]
                 +cubic((455,210),(445,65),(195,25),(125,120),45)[1:]),
      "B":unary_union([stroke([(150,650),(150,50)]),
                       arc(250,505,190,145,100,-100),
                       arc(250,205,200,165,100,-100)])
    }

def punctuation():
    return {
      "colon":unary_union([circle(160,245,42),circle(160,455,42)]),
      "colon.v0":unary_union([circle(160,245,25),circle(160,455,25)]),
      "plus":unary_union([stroke([(135,350),(445,350)],74),stroke([(290,195),(290,505)],74)]),
      "period":circle(150,70,43),
      "comma":unary_union([circle(160,85,43),stroke(cubic((165,65),(160,5),(135,-55),(100,-95),24),48)]),
      "slash":stroke([(125,-35),(435,735)],66),
      "hyphen":stroke([(105,310),(395,310)],66),
      "minus":stroke([(90,350),(510,350)],70),
    }

def empty():
    return TTGlyphPen(None).glyph()

def metric(g, adv):
    return (adv, int(round(g.bounds[0])))

def build_font():
    dg=digit_geoms()
    prop={n:centered(dg[n],PROP_ADV[n],OPT_OFF[n]) for n in DIGITS}
    tab={n+".tnum":centered(dg[n],TAB_ADV,OPT_OFF[n]) for n in DIGITS}

    outer=ellipse_polygon(300,350,241,351)
    zero_slash=unary_union([dg["zero"],stroke([(135,80),(465,620)],52).intersection(outer)])
    zero_dot=unary_union([dg["zero"],circle(300,350,38)])

    glyphs={".notdef":to_glyph(Polygon([(50,0),(450,0),(450,700),(50,700)])),
            "space":empty()}
    metrics={".notdef":(500,50),"space":(300,0)}
    order=[".notdef","space"]
    cmap={0x20:"space"}

    for i,n in enumerate(DIGITS):
        for name,g,adv,cp in [(n,prop[n],PROP_ADV[n],0x30+i),
                              (n+".tnum",tab[n+".tnum"],TAB_ADV,0xE100+i)]:
            glyphs[name]=to_glyph(g); metrics[name]=metric(g,adv)
            order.append(name); cmap[cp]=name

    zero_alts={
      "zero.slash":(centered(zero_slash,PROP_ADV["zero"]),PROP_ADV["zero"],0xE120),
      "zero.dot":(centered(zero_dot,PROP_ADV["zero"]),PROP_ADV["zero"],0xE121),
      "zero.tnum.slash":(centered(zero_slash,TAB_ADV),TAB_ADV,0xE122),
      "zero.tnum.dot":(centered(zero_dot,TAB_ADV),TAB_ADV,0xE123),
    }
    for name,(g,adv,cp) in zero_alts.items():
        glyphs[name]=to_glyph(g); metrics[name]=metric(g,adv)
        order.append(name); cmap[cp]=name

    cadv={"O":640,"I":500,"l":430,"S":570,"B":600}
    ccps={"O":0x4F,"I":0x49,"l":0x6C,"S":0x53,"B":0x42}
    for n,g0 in controls().items():
        g=centered(g0,cadv[n],-5 if n=="l" else 0)
        glyphs[n]=to_glyph(g); metrics[n]=metric(g,cadv[n])
        order.append(n); cmap[ccps[n]]=n

    padv={"colon":320,"colon.v0":320,"plus":580,"comma":300,"period":300,
          "slash":560,"hyphen":500,"minus":600}
    pcps={"colon":0x3A,"plus":0x2B,"comma":0x2C,"period":0x2E,
          "slash":0x2F,"hyphen":0x2D,"minus":0x2212,"colon.v0":0xE130}
    for n,g0 in punctuation().items():
        g=centered(g0,padv[n])
        glyphs[n]=to_glyph(g); metrics[n]=metric(g,padv[n])
        order.append(n); cmap[pcps[n]]=n

    fb=FontBuilder(UPM,isTTF=True)
    fb.setupGlyphOrder(order); fb.setupCharacterMap(cmap); fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=820,descent=-220,lineGap=0)
    fb.setupOS2(sTypoAscender=820,sTypoDescender=-220,sTypoLineGap=0,
                usWinAscent=850,usWinDescent=250,sxHeight=500,sCapHeight=700,
                usWeightClass=400,usWidthClass=5)
    fb.setupNameTable({"familyName":"T004 Numeral Research","styleName":"Regular",
      "uniqueFontIdentifier":"T004 Numeral Research Regular 20260914",
      "fullName":"T004 Numeral Research Regular",
      "psName":"T004-NumeralResearch-Regular","version":"Version 0.001"})
    fb.setupPost(); fb.setupMaxp(); fb.save(FONT)

    font=TTFont(FONT)
    addOpenTypeFeaturesFromString(font, """
languagesystem DFLT dflt;
feature tnum {
 sub zero by zero.tnum; sub one by one.tnum; sub two by two.tnum;
 sub three by three.tnum; sub four by four.tnum; sub five by five.tnum;
 sub six by six.tnum; sub seven by seven.tnum; sub eight by eight.tnum;
 sub nine by nine.tnum;
} tnum;
feature zero { sub zero by zero.slash; sub zero.tnum by zero.tnum.slash; } zero;
feature cv01 { sub zero by zero.dot; sub zero.tnum by zero.tnum.dot; } cv01;
""")
    font.save(FONT); font.saveXML(TTX)

def bitmap(slot):
    b=slot.bitmap
    if not b.rows or not b.width: return np.zeros((0,0),dtype=np.uint8)
    return np.array(b.buffer,dtype=np.uint8).reshape((b.rows,b.pitch))[:,:b.width]

MODES={
 "no-hint":freetype.FT_LOAD_RENDER|freetype.FT_LOAD_NO_HINTING|freetype.FT_LOAD_TARGET_NORMAL,
 "autohint-normal":freetype.FT_LOAD_RENDER|freetype.FT_LOAD_FORCE_AUTOHINT|freetype.FT_LOAD_TARGET_NORMAL,
 "autohint-light":freetype.FT_LOAD_RENDER|freetype.FT_LOAD_FORCE_AUTOHINT|freetype.FT_LOAD_TARGET_LIGHT,
}

def measure(face,ch,ppem,flags):
    face.set_pixel_sizes(0,ppem); face.load_char(ch,flags)
    s=face.glyph; a=bitmap(s)
    return {"advance":s.advance.x/64.0,"linear":s.linearHoriAdvance/65536.0,
            "coverage":round(float(a.sum()/255),3),"strong":int((a>=128).sum())}

def run_measurements():
    font=TTFont(FONT)
    face=freetype.Face(str(FONT))
    tags=[r.FeatureTag for r in font["GSUB"].table.FeatureList.FeatureRecord]
    out={"study":"T004","upm":UPM,"feature_tags":tags,
         "default":"proportional lining research figures","tabular_advance":TAB_ADV}
    out["source_advances"]={
      "proportional":[font["hmtx"][n][0] for n in DIGITS],
      "tabular":[font["hmtx"][n+".tnum"][0] for n in DIGITS]}
    out["tabular_raw_hinted_advances"]={}
    for ppem in (14,20,48):
        out["tabular_raw_hinted_advances"][str(ppem)]={}
        for mode,flags in MODES.items():
            vals=[measure(face,chr(0xE100+i),ppem,flags)["advance"] for i in range(10)]
            out["tabular_raw_hinted_advances"][str(ppem)][mode]=vals

    out["colon_redraw"]={}
    out["zero_mark_signal"]={}
    for ppem in (14,20,48):
        out["colon_redraw"][str(ppem)]={}
        out["zero_mark_signal"][str(ppem)]={}
        for mode in ("no-hint","autohint-light"):
            c0=measure(face,chr(0xE130),ppem,MODES[mode])
            c1=measure(face,":",ppem,MODES[mode])
            z=measure(face,"0",ppem,MODES[mode])
            zs=measure(face,chr(0xE120),ppem,MODES[mode])
            zd=measure(face,chr(0xE121),ppem,MODES[mode])
            out["colon_redraw"][str(ppem)][mode]={"v0":c0,"v1":c1}
            out["zero_mark_signal"][str(ppem)][mode]={
              "slash_extra_coverage":round(zs["coverage"]-z["coverage"],3),
              "slash_extra_strong":zs["strong"]-z["strong"],
              "dot_extra_coverage":round(zd["coverage"]-z["coverage"],3),
              "dot_extra_strong":zd["strong"]-z["strong"]}
    RESULTS.write_text(json.dumps(out,indent=2),encoding="utf-8")

def main():
    build_font()
    run_measurements()
    print("wrote", FONT, TTX, RESULTS)

if __name__=="__main__":
    main()
