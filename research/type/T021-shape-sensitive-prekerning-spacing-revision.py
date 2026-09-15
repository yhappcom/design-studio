"""T021 shape-sensitive pre-kerning spacing revision harness.
Research-only. Builds A/B/C mini-families with per-glyph cap metrics; kerning remains OFF.
"""
from pathlib import Path
import json
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from PIL import ImageFont

UPM=1000
OUT=Path("/tmp/t021-shape-spacing"); OUT.mkdir(exist_ok=True)
HYP={
"A":{"stem":90,"H":(600,55),"O":(610,45),"n":(520,48),"o":(530,42),"A":(590,42),"V":(590,42),"T":(570,34),"L":(535,55),"I":(350,48)},
"B":{"stem":85,"H":(620,65),"O":(620,55),"n":(540,58),"o":(540,50),"A":(610,50),"V":(610,50),"T":(585,40),"L":(550,62),"I":(365,52)},
"C":{"stem":82,"H":(650,75),"O":(650,65),"n":(565,68),"o":(570,60),"A":(635,58),"V":(635,58),"T":(610,46),"L":(575,70),"I":(385,58)}}
STRINGS=["HAVAL","AVAVA","TAVAT","LITIL","HOnonO","nono","noon","onno"]
def rect(p,x0,y0,x1,y1): p.moveTo((x0,y0));p.lineTo((x1,y0));p.lineTo((x1,y1));p.lineTo((x0,y1));p.closePath()
def poly(p,pts):
 p.moveTo(pts[0])
 for q in pts[1:]: p.lineTo(q)
 p.closePath()
def curvepen():
 tt=TTGlyphPen(None); return tt,Cu2QuPen(tt,max_err=1.0,reverse_direction=False)
def ellipse(p,x0,y0,x1,y1,inner=False):
 k=.55228475;cx=(x0+x1)/2;cy=(y0+y1)/2;rx=(x1-x0)/2;ry=(y1-y0)/2
 pts=[(cx+rx,cy),(cx+rx,cy+k*ry),(cx+k*rx,cy+ry),(cx,cy+ry),(cx-k*rx,cy+ry),(cx-rx,cy+k*ry),(cx-rx,cy),(cx-rx,cy-k*ry),(cx-k*rx,cy-ry),(cx,cy-ry),(cx+k*rx,cy-ry),(cx+rx,cy-k*ry)]
 p.moveTo(pts[0]);seq=[(11,10,9),(8,7,6),(5,4,3),(2,1,0)] if inner else [(1,2,3),(4,5,6),(7,8,9),(10,11,0)]
 for a,b,c in seq:p.curveTo(pts[a],pts[b],pts[c])
 p.closePath()
def H(d):
 p=TTGlyphPen(None);s=d['stem'];aw,l=d['H'];w=aw-2*l;rect(p,l,0,l+s,700);rect(p,l+w-s,0,l+w,700);rect(p,l,305,l+w,390);return p.glyph()
def O(d,lower=False):
 tt,p=curvepen();g='o' if lower else 'O';aw,l=d[g];h=500 if lower else 700;ov=10 if lower else 12;s=d['stem'];ellipse(p,l,-ov,aw-l,h+ov);ellipse(p,l+s,s-ov,aw-l-s,h+ov-s,True);return tt.glyph()
def n(d):
 tt,p=curvepen();s=d['stem'];aw,l=d['n'];r=aw-52;rect(p,l,0,l+s,500);rect(p,r-s,0,r,350);p.moveTo((l+s,350));p.lineTo((l+s,500));p.curveTo((l+s+90,515),(r-s-20,505),(r-s,420));p.lineTo((r-s,350));p.closePath();return tt.glyph()
def A(d):
 p=TTGlyphPen(None);s=d['stem'];aw,l=d['A'];r=aw-l;m=(l+r)/2;poly(p,[(l,0),(l+s,0),(m,700),(m-s,700)]);poly(p,[(r-s,0),(r,0),(m+s,700),(m,700)]);rect(p,l+100,270,r-100,345);return p.glyph()
def V(d):
 p=TTGlyphPen(None);s=d['stem'];aw,l=d['V'];r=aw-l;m=(l+r)/2;poly(p,[(l,700),(l+s,700),(m+25,0),(m-55,0)]);poly(p,[(r-s,700),(r,700),(m+55,0),(m-25,0)]);return p.glyph()
def T(d):
 p=TTGlyphPen(None);s=d['stem'];aw,l=d['T'];r=aw-l;m=(l+r)/2;rect(p,l,615,r,700);rect(p,m-s/2,0,m+s/2,700);return p.glyph()
def L(d):
 p=TTGlyphPen(None);s=d['stem'];aw,l=d['L'];r=aw-l;rect(p,l,0,l+s,700);rect(p,l,0,r,85);return p.glyph()
def I(d):
 p=TTGlyphPen(None);s=d['stem'];aw,l=d['I'];r=aw-l;m=(l+r)/2;rect(p,l,615,r,700);rect(p,l,0,r,85);rect(p,m-s/2,0,m+s/2,700);return p.glyph()
def build(tag,d):
 order=['.notdef','H','O','n','o','A','V','T','L','I','space'];p=TTGlyphPen(None);rect(p,50,0,450,700)
 glyphs={'.notdef':p.glyph(),'H':H(d),'O':O(d),'n':n(d),'o':O(d,True),'A':A(d),'V':V(d),'T':T(d),'L':L(d),'I':I(d),'space':TTGlyphPen(None).glyph()}
 fb=FontBuilder(UPM,isTTF=True);fb.setupGlyphOrder(order);fb.setupCharacterMap({ord(c):c for c in 'HOn oAVTLI'.replace(' ','')}|{32:'space'});fb.setupGlyf(glyphs)
 metrics={'.notdef':(500,50),'space':(250,0)}
 for g in 'HOn oAVTLI'.replace(' ',''):metrics[g]=d[g]
 fb.setupHorizontalMetrics(metrics);fb.setupHorizontalHeader(ascent=800,descent=-200);fb.setupOS2(sTypoAscender=800,sTypoDescender=-200,usWinAscent=800,usWinDescent=200);fb.setupNameTable({'familyName':f'T021 Shape {tag}','styleName':'Regular','uniqueFontIdentifier':f'T021-Shape-{tag}','fullName':f'T021 Shape {tag} Regular','psName':f'T021-Shape-{tag}-Regular'});fb.setupPost();fb.setupMaxp();path=OUT/f'T021-Shape-{tag}.ttf';fb.save(path);return path
fonts={k:build(k,v) for k,v in HYP.items()};res={'upm':UPM,'kerning':False,'sizes_px':[14,17,24],'strings':STRINGS,'hypotheses':HYP,'measurements':{}}
for px in (14,17,24):
 res['measurements'][str(px)]={}
 for s in STRINGS:res['measurements'][str(px)][s]={tag:round(ImageFont.truetype(str(path),px).getlength(s),4) for tag,path in fonts.items()}
(OUT/'results.json').write_text(json.dumps(res,indent=2),encoding='utf-8');print(json.dumps(res,indent=2))