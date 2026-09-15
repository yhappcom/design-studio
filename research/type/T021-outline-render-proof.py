"""T021 reproducible custom-outline proof generator.

Builds three bounded H/O/n/o research fonts from explicit outline geometry and
renders control strings at 14/17/24 px with Pillow/FreeType. Kerning is absent.
This is research evidence, not a production font pipeline.
"""
from pathlib import Path
import json
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import Image, ImageDraw, ImageFont

UPM=1000
OUT=Path("/tmp/t021")
OUT.mkdir(exist_ok=True)
HYP={
 "A":{"stem":90,"H_aw":600,"H_lsb":55,"O_aw":610,"O_lsb":45,"n_aw":520,"n_lsb":48,"o_aw":530,"o_lsb":42},
 "B":{"stem":85,"H_aw":620,"H_lsb":65,"O_aw":620,"O_lsb":55,"n_aw":540,"n_lsb":58,"o_aw":540,"o_lsb":50},
 "C":{"stem":82,"H_aw":650,"H_lsb":75,"O_aw":650,"O_lsb":65,"n_aw":565,"n_lsb":68,"o_aw":570,"o_lsb":60},
}
STRINGS=["HHOO","HHOH","OOHO","HOHOHO","nono","noon","onno","HOnonO","HnOoH"]

def rect(p,x0,y0,x1,y1):
 p.moveTo((x0,y0));p.lineTo((x1,y0));p.lineTo((x1,y1));p.lineTo((x0,y1));p.closePath()
def ellipse(p,x0,y0,x1,y1,inner=False):
 # cubic approximation; reverse winding for inner counter
 k=.55228475; cx=(x0+x1)/2; cy=(y0+y1)/2; rx=(x1-x0)/2; ry=(y1-y0)/2
 pts=[(cx+rx,cy),(cx+rx,cy+k*ry),(cx+k*rx,cy+ry),(cx,cy+ry),(cx-k*rx,cy+ry),(cx-rx,cy+k*ry),(cx-rx,cy),(cx-rx,cy-k*ry),(cx-k*rx,cy-ry),(cx,cy-ry),(cx+k*rx,cy-ry),(cx+rx,cy-k*ry)]
 if inner:
  p.moveTo(pts[0]);p.curveTo(pts[11],pts[10],pts[9]);p.curveTo(pts[8],pts[7],pts[6]);p.curveTo(pts[5],pts[4],pts[3]);p.curveTo(pts[2],pts[1],pts[0]);p.closePath()
 else:
  p.moveTo(pts[0]);p.curveTo(pts[1],pts[2],pts[3]);p.curveTo(pts[4],pts[5],pts[6]);p.curveTo(pts[7],pts[8],pts[9]);p.curveTo(pts[10],pts[11],pts[0]);p.closePath()

def glyph_H(d):
 p=TTGlyphPen(None); s=d['stem']; l=d['H_lsb']; w=d['H_aw']-2*l
 rect(p,l,0,l+s,700);rect(p,l+w-s,0,l+w,700);rect(p,l,305,l+w,390);return p.glyph()
def glyph_O(d,lower=False):
 p=TTGlyphPen(None); aw=d['o_aw'] if lower else d['O_aw']; l=d['o_lsb'] if lower else d['O_lsb']; h=500 if lower else 700; ov=10 if lower else 12; s=d['stem'];
 ellipse(p,l,-ov,aw-l,h+ov);ellipse(p,l+s,s-ov,aw-l-s,h+ov-s,True);return p.glyph()
def glyph_n(d):
 p=TTGlyphPen(None); s=d['stem']; l=d['n_lsb']; aw=d['n_aw']; r=aw-52
 rect(p,l,0,l+s,500);rect(p,r-s,0,r,360);rect(p,l+s,415,r-s,500);return p.glyph()

def build(tag,d):
 order=['.notdef','H','O','n','o','space']; glyphs={}
 p=TTGlyphPen(None);rect(p,50,0,450,700);rect(p,120,70,380,630);glyphs['.notdef']=p.glyph()
 glyphs.update(H=glyph_H(d),O=glyph_O(d),n=glyph_n(d),o=glyph_O(d,True));glyphs['space']=TTGlyphPen(None).glyph()
 fb=FontBuilder(UPM,isTTF=True);fb.setupGlyphOrder(order);fb.setupCharacterMap({72:'H',79:'O',110:'n',111:'o',32:'space'});fb.setupGlyf(glyphs)
 metrics={'.notdef':(500,50),'H':(d['H_aw'],d['H_lsb']),'O':(d['O_aw'],d['O_lsb']),'n':(d['n_aw'],d['n_lsb']),'o':(d['o_aw'],d['o_lsb']),'space':(250,0)}
 fb.setupHorizontalMetrics(metrics);fb.setupHorizontalHeader(ascent=800,descent=-200);fb.setupOS2(sTypoAscender=800,sTypoDescender=-200,usWinAscent=800,usWinDescent=200);fb.setupNameTable({'familyName':f'T021 {tag}','styleName':'Regular','uniqueFontIdentifier':f'T021-{tag}','fullName':f'T021 {tag} Regular','psName':f'T021-{tag}-Regular'});fb.setupPost();fb.setupMaxp()
 path=OUT/f'T021-{tag}.ttf';fb.save(path);return path

def render(fonts):
 W=1500; rowh=46; H=70+len(STRINGS)*rowh*3
 im=Image.new('L',(W,H),255); dr=ImageDraw.Draw(im); y=20
 for s in STRINGS:
  dr.text((15,y),s,fill=0,font=ImageFont.truetype(str(fonts['B']),17)); y+=rowh
  for px in (14,17,24):
   x=230
   dr.text((15,y),f'{px}px',fill=0,font=ImageFont.truetype(str(fonts['B']),14))
   for tag in 'ABC':
    f=ImageFont.truetype(str(fonts[tag]),px); dr.text((x,y),s,fill=0,font=f); x+=390
   y+=rowh
 return im
fonts={k:build(k,v) for k,v in HYP.items()}; img=render(fonts);img.save(OUT/'T021-outline-render-proof.png')
results={'upm':UPM,'kerning':False,'sizes_px':[14,17,24],'strings':STRINGS,'hypotheses':HYP,'notes':['Custom research outlines generated for H/O/n/o.','A/B/C differ in stem and sidebearing/advance hypotheses.','Raster proof uses Pillow FreeType; no browser/native/human claim.']}
(OUT/'T021-outline-render-results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))