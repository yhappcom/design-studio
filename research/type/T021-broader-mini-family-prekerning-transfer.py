"""T021 broader mini-family pre-kerning transfer harness.

Builds A/B/C H/O/n/o/A/V/T/L/I research fonts and measures target-size strings.
Research-only; no kerning, browser, native, or human-quality claim.
"""
from pathlib import Path
import json
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from PIL import ImageFont

UPM=1000
OUT=Path("/tmp/t021-family")
OUT.mkdir(exist_ok=True)
HYP={
"A":{"stem":90,"H_aw":600,"H_lsb":55,"O_aw":610,"O_lsb":45,"n_aw":520,"n_lsb":48,"o_aw":530,"o_lsb":42,"cap_aw":600,"cap_lsb":50},
"B":{"stem":85,"H_aw":620,"H_lsb":65,"O_aw":620,"O_lsb":55,"n_aw":540,"n_lsb":58,"o_aw":540,"o_lsb":50,"cap_aw":620,"cap_lsb":60},
"C":{"stem":82,"H_aw":650,"H_lsb":75,"O_aw":650,"O_lsb":65,"n_aw":565,"n_lsb":68,"o_aw":570,"o_lsb":60,"cap_aw":650,"cap_lsb":70},
}
STRINGS=["HAVAL","AVAVA","TAVAT","LITIL","HOnonO","nono","noon","onno"]
def rect(p,x0,y0,x1,y1):
 p.moveTo((x0,y0));p.lineTo((x1,y0));p.lineTo((x1,y1));p.lineTo((x0,y1));p.closePath()
def poly(p,pts):
 p.moveTo(pts[0])
 for q in pts[1:]: p.lineTo(q)
 p.closePath()
def new_curve_pen():
 tt=TTGlyphPen(None); return tt,Cu2QuPen(tt,max_err=1.0,reverse_direction=False)
def ellipse(p,x0,y0,x1,y1,inner=False):
 k=.55228475;cx=(x0+x1)/2;cy=(y0+y1)/2;rx=(x1-x0)/2;ry=(y1-y0)/2
 pts=[(cx+rx,cy),(cx+rx,cy+k*ry),(cx+k*rx,cy+ry),(cx,cy+ry),(cx-k*rx,cy+ry),(cx-rx,cy+k*ry),(cx-rx,cy),(cx-rx,cy-k*ry),(cx-k*rx,cy-ry),(cx,cy-ry),(cx+k*rx,cy-ry),(cx+rx,cy-k*ry)]
 p.moveTo(pts[0]);seq=[(11,10,9),(8,7,6),(5,4,3),(2,1,0)] if inner else [(1,2,3),(4,5,6),(7,8,9),(10,11,0)]
 for a,b,c in seq:p.curveTo(pts[a],pts[b],pts[c])
 p.closePath()
def glyph_H(d):
 p=TTGlyphPen(None);s=d["stem"];l=d["H_lsb"];w=d["H_aw"]-2*l
 rect(p,l,0,l+s,700);rect(p,l+w-s,0,l+w,700);rect(p,l,305,l+w,390);return p.glyph()
def glyph_O(d,lower=False):
 tt,p=new_curve_pen();aw=d["o_aw"] if lower else d["O_aw"];l=d["o_lsb"] if lower else d["O_lsb"];h=500 if lower else 700;ov=10 if lower else 12;s=d["stem"]
 ellipse(p,l,-ov,aw-l,h+ov);ellipse(p,l+s,s-ov,aw-l-s,h+ov-s,True);return tt.glyph()
def glyph_n(d):
 tt,p=new_curve_pen();s=d["stem"];l=d["n_lsb"];aw=d["n_aw"];r=aw-52
 rect(p,l,0,l+s,500);rect(p,r-s,0,r,350);p.moveTo((l+s,350));p.lineTo((l+s,500));p.curveTo((l+s+90,515),(r-s-20,505),(r-s,420));p.lineTo((r-s,350));p.closePath();return tt.glyph()
def glyph_A(d):
 p=TTGlyphPen(None);s=d["stem"];l=d["cap_lsb"];r=d["cap_aw"]-l;mid=(l+r)/2
 poly(p,[(l,0),(l+s,0),(mid,700),(mid-s,700)]);poly(p,[(r-s,0),(r,0),(mid+s,700),(mid,700)]);rect(p,l+105,270,r-105,345);return p.glyph()
def glyph_V(d):
 p=TTGlyphPen(None);s=d["stem"];l=d["cap_lsb"];r=d["cap_aw"]-l;mid=(l+r)/2
 poly(p,[(l,700),(l+s,700),(mid+25,0),(mid-55,0)]);poly(p,[(r-s,700),(r,700),(mid+55,0),(mid-25,0)]);return p.glyph()
def glyph_T(d):
 p=TTGlyphPen(None);s=d["stem"];l=d["cap_lsb"];r=d["cap_aw"]-l;mid=(l+r)/2
 rect(p,l,615,r,700);rect(p,mid-s/2,0,mid+s/2,700);return p.glyph()
def glyph_L(d):
 p=TTGlyphPen(None);s=d["stem"];l=d["cap_lsb"];r=d["cap_aw"]-l
 rect(p,l,0,l+s,700);rect(p,l,0,r,85);return p.glyph()
def glyph_I(d):
 p=TTGlyphPen(None);s=d["stem"];l=d["cap_lsb"];r=d["cap_aw"]-l;mid=(l+r)/2
 rect(p,l,615,r,700);rect(p,l,0,r,85);rect(p,mid-s/2,0,mid+s/2,700);return p.glyph()
def build(tag,d):
 order=[".notdef","H","O","n","o","A","V","T","L","I","space"];glyphs={};p=TTGlyphPen(None);rect(p,50,0,450,700);glyphs[".notdef"]=p.glyph()
 glyphs.update(H=glyph_H(d),O=glyph_O(d),n=glyph_n(d),o=glyph_O(d,True),A=glyph_A(d),V=glyph_V(d),T=glyph_T(d),L=glyph_L(d),I=glyph_I(d),space=TTGlyphPen(None).glyph())
 fb=FontBuilder(UPM,isTTF=True);fb.setupGlyphOrder(order);fb.setupCharacterMap({ord(c):c for c in "HOn oAVTLI".replace(" ","")}|{32:"space"});fb.setupGlyf(glyphs)
 metrics={".notdef":(500,50),"H":(d["H_aw"],d["H_lsb"]),"O":(d["O_aw"],d["O_lsb"]),"n":(d["n_aw"],d["n_lsb"]),"o":(d["o_aw"],d["o_lsb"]),"space":(250,0)}
 for c in "AVTLI":metrics[c]=(d["cap_aw"],d["cap_lsb"])
 fb.setupHorizontalMetrics(metrics);fb.setupHorizontalHeader(ascent=800,descent=-200);fb.setupOS2(sTypoAscender=800,sTypoDescender=-200,usWinAscent=800,usWinDescent=200);fb.setupNameTable({"familyName":f"T021 Family {tag}","styleName":"Regular","uniqueFontIdentifier":f"T021-Family-{tag}","fullName":f"T021 Family {tag} Regular","psName":f"T021-Family-{tag}-Regular"});fb.setupPost();fb.setupMaxp();path=OUT/f"T021-Family-{tag}.ttf";fb.save(path);return path
fonts={k:build(k,v) for k,v in HYP.items()};res={"upm":UPM,"kerning":False,"sizes_px":[14,17,24],"strings":STRINGS,"hypotheses":HYP,"measurements":{}}
for px in (14,17,24):
 res["measurements"][str(px)]={}
 for s in STRINGS:
  res["measurements"][str(px)][s]={tag:round(ImageFont.truetype(str(path),px).getlength(s),4) for tag,path in fonts.items()}
(OUT/"T021-broader-mini-family-results.json").write_text(json.dumps(res,indent=2),encoding="utf-8");print(json.dumps(res,indent=2))