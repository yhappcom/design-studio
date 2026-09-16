"""T021 LogMate operational-family expansion harness.

Builds a bounded Balanced research font for the LogMate operational corpus,
keeps kerning OFF, measures 14/17/24 px strings, checks cmap coverage and
writes deterministic JSON results. Research-only: no human/browser/native
or production-font quality claim.
"""
from pathlib import Path
import json
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from PIL import ImageFont

UPM=1000
OUT=Path('/tmp/t021-logmate-expanded'); OUT.mkdir(exist_ok=True)
STEM=85; CAP=700; XH=500
UPPER='ABCDEFGHIJKLMNOPRSTUVX'  # bounded contract repertoire; Q/W/Y/Z not required
LOWER='nol'
DIGITS='0123456789'
PUNCT='-:,'
AIRPORTS=['ICN','NRT','SIN','JFK','LHR','CDG','HND','DXB','FRA','LAX']
IDENTIFIERS=['KE704','BA117','AF264','B737-900','B737-8','A320-200','HL8301','N12345','G-EUOH']
NUMERIC=['00:45','02:18','09:55','12:40','1,284:35','9,999:59','1','11','111','8','88','888']
AMBIG=['0O','1Il','5S','8B']
SPACING=['HHOO','HOHOHO','nono','noon','AVAVA','TOTO','LITIL']
STRINGS=AIRPORTS+IDENTIFIERS+NUMERIC+AMBIG+SPACING

def rect(p,x0,y0,x1,y1):
 p.moveTo((x0,y0));p.lineTo((x1,y0));p.lineTo((x1,y1));p.lineTo((x0,y1));p.closePath()
def poly(p,pts):
 p.moveTo(pts[0]);
 for q in pts[1:]: p.lineTo(q)
 p.closePath()
def ellipse(p,x0,y0,x1,y1,inner=False):
 k=.55228475;cx=(x0+x1)/2;cy=(y0+y1)/2;rx=(x1-x0)/2;ry=(y1-y0)/2
 pts=[(cx+rx,cy),(cx+rx,cy+k*ry),(cx+k*rx,cy+ry),(cx,cy+ry),(cx-k*rx,cy+ry),(cx-rx,cy+k*ry),(cx-rx,cy),(cx-rx,cy-k*ry),(cx-k*rx,cy-ry),(cx,cy-ry),(cx+k*rx,cy-ry),(cx+rx,cy-k*ry)]
 p.moveTo(pts[0]); seq=[(11,10,9),(8,7,6),(5,4,3),(2,1,0)] if inner else [(1,2,3),(4,5,6),(7,8,9),(10,11,0)]
 for a,b,c in seq:p.curveTo(pts[a],pts[b],pts[c])
 p.closePath()
def curve_pen():
 tt=TTGlyphPen(None);return tt,Cu2QuPen(tt,max_err=1.0,reverse_direction=False)
def boxglyph(aw=620,lsb=60,kind='box'):
 p=TTGlyphPen(None);r=aw-lsb
 if kind=='H': rect(p,lsb,0,lsb+STEM,CAP);rect(p,r-STEM,0,r,CAP);rect(p,lsb,305,r,390)
 elif kind=='L': rect(p,lsb,0,lsb+STEM,CAP);rect(p,lsb,0,r,STEM)
 elif kind=='I': rect(p,lsb,615,r,CAP);rect(p,lsb,0,r,STEM);m=(lsb+r)/2;rect(p,m-STEM/2,0,m+STEM/2,CAP)
 elif kind=='T': rect(p,lsb,615,r,CAP);m=(lsb+r)/2;rect(p,m-STEM/2,0,m+STEM/2,CAP)
 elif kind in 'EF':
  rect(p,lsb,0,lsb+STEM,CAP);rect(p,lsb,615,r,CAP);rect(p,lsb,305,r-(30 if kind=='F' else 0),390)
  if kind=='E':rect(p,lsb,0,r,STEM)
 elif kind=='J': rect(p,lsb,615,r,CAP);rect(p,r-STEM,80,r,CAP);rect(p,lsb+40,0,r-STEM,STEM);rect(p,lsb+40,0,lsb+125,180)
 elif kind=='N': poly(p,[(lsb,0),(lsb+STEM,0),(r,CAP),(r-STEM,CAP)]);rect(p,lsb,0,lsb+STEM,CAP);rect(p,r-STEM,0,r,CAP)
 elif kind=='K': rect(p,lsb,0,lsb+STEM,CAP);poly(p,[(lsb+STEM,330),(r-STEM,CAP),(r,CAP),(lsb+STEM,390)]);poly(p,[(lsb+STEM,370),(r,0),(r-STEM,0),(lsb+STEM,310)])
 elif kind=='X': poly(p,[(lsb,0),(lsb+STEM,0),(r,CAP),(r-STEM,CAP)]);poly(p,[(r-STEM,0),(r,0),(lsb+STEM,CAP),(lsb,CAP)])
 elif kind=='A': m=(lsb+r)/2;poly(p,[(lsb,0),(lsb+STEM,0),(m,CAP),(m-STEM,CAP)]);poly(p,[(r-STEM,0),(r,0),(m+STEM,CAP),(m,CAP)]);rect(p,lsb+105,270,r-105,345)
 elif kind=='V': m=(lsb+r)/2;poly(p,[(lsb,CAP),(lsb+STEM,CAP),(m+25,0),(m-55,0)]);poly(p,[(r-STEM,CAP),(r,CAP),(m+55,0),(m-25,0)])
 else: rect(p,lsb,0,r,CAP)
 return p.glyph()
def roundglyph(aw=620,lsb=55,kind='O'):
 tt,p=curve_pen();r=aw-lsb
 if kind in 'ODCGBS':
  ellipse(p,lsb,-12,r,CAP+12);ellipse(p,lsb+STEM,STEM-12,r-STEM,CAP+12-STEM,True)
  # bounded research primitives: open/mask forms are intentionally simple
  if kind=='C': rect(p,r-STEM-10,115,r+5,585)
  if kind=='G': rect(p,r-STEM-10,360,r+5,585);rect(p,(lsb+r)/2,305,r,390)
  if kind=='D': rect(p,lsb,0,lsb+STEM,CAP)
  if kind=='B': rect(p,lsb,0,lsb+STEM,CAP);rect(p,lsb+STEM,305,r,390)
  if kind=='S': rect(p,lsb,260,r,440)
 elif kind=='U':
  rect(p,lsb,150,lsb+STEM,CAP);rect(p,r-STEM,150,r,CAP);ellipse(p,lsb,0,r,300);rect(p,lsb,-20,r,150)
 return tt.glyph()
def lowerglyph(c):
 p=TTGlyphPen(None);aw=540;lsb=55;r=aw-55
 if c=='l': rect(p,lsb,0,lsb+STEM,CAP)
 elif c=='n': rect(p,lsb,0,lsb+STEM,XH);rect(p,r-STEM,0,r,350);rect(p,lsb+STEM,415,r-STEM,500)
 else:
  tt,q=curve_pen();ellipse(q,50,-10,490,510);ellipse(q,135,75,405,425,True);return tt.glyph(),(540,50)
 return p.glyph(),(aw,lsb)
def digitglyph(c):
 aw=560;lsb=55;r=aw-lsb;p=TTGlyphPen(None)
 if c=='0':
  tt,q=curve_pen();ellipse(q,lsb,-8,r,CAP+8);ellipse(q,lsb+STEM,STEM-8,r-STEM,CAP+8-STEM,True);return tt.glyph(),(aw,lsb)
 if c=='1': rect(p,(aw-STEM)/2,0,(aw+STEM)/2,CAP);rect(p,140,0,420,STEM);poly(p,[(190,560),(275,CAP),(360,CAP),(275,520)])
 elif c=='2': rect(p,lsb,0,r,STEM);poly(p,[(lsb,STEM),(r-STEM,615),(r,CAP),(r-STEM,CAP),(lsb,170)])
 elif c=='3': rect(p,lsb+80,615,r,CAP);rect(p,lsb+120,305,r,390);rect(p,lsb+80,0,r,STEM);rect(p,r-STEM,0,r,CAP)
 elif c=='4': rect(p,r-STEM,0,r,CAP);rect(p,lsb,260,r,345);poly(p,[(lsb,345),(r-STEM,700),(r,700),(lsb+STEM,345)])
 elif c=='5': rect(p,lsb,615,r,CAP);rect(p,lsb,305,r,390);rect(p,lsb,0,r,STEM);rect(p,lsb,305,lsb+STEM,CAP);rect(p,r-STEM,0,r,390)
 elif c=='6': rect(p,lsb,0,lsb+STEM,CAP);rect(p,lsb,305,r,390);rect(p,lsb,0,r,STEM);rect(p,r-STEM,0,r,390);rect(p,lsb,615,r,CAP)
 elif c=='7': rect(p,lsb,615,r,CAP);poly(p,[(r-STEM,615),(r,615),(260,0),(175,0)])
 elif c=='8': rect(p,lsb,0,lsb+STEM,CAP);rect(p,r-STEM,0,r,CAP);rect(p,lsb,615,r,CAP);rect(p,lsb,305,r,390);rect(p,lsb,0,r,STEM)
 elif c=='9': rect(p,r-STEM,0,r,CAP);rect(p,lsb,615,r,CAP);rect(p,lsb,305,r,390);rect(p,lsb,305,lsb+STEM,CAP)
 return p.glyph(),(aw,lsb)

def build():
 glyphs={};metrics={};cmap={};order=['.notdef']
 p=TTGlyphPen(None);rect(p,50,0,450,CAP);glyphs['.notdef']=p.glyph();metrics['.notdef']=(500,50)
 widths={'A':610,'V':610,'T':580,'L':560,'I':420,'H':620,'O':620,'C':600,'D':625,'B':615,'E':570,'F':550,'G':630,'J':530,'K':610,'N':635,'R':620,'S':590,'U':625,'X':610}
 for c in UPPER:
  aw=widths.get(c,610);lsb=55 if c in 'OCGDSBU' else 60
  if c in 'OCGDSBU': g=roundglyph(aw,lsb,c)
  elif c=='R': g=boxglyph(aw,lsb,'H')
  else:g=boxglyph(aw,lsb,c)
  glyphs[c]=g;metrics[c]=(aw,lsb);cmap[ord(c)]=c;order.append(c)
 for c in LOWER:
  g,m=lowerglyph(c);glyphs[c]=g;metrics[c]=m;cmap[ord(c)]=c;order.append(c)
 for c in DIGITS:
  g,m=digitglyph(c);glyphs[c]=g;metrics[c]=m;cmap[ord(c)]=c;order.append(c)
 for c,name,aw in [('-', 'hyphen',400),(':','colon',300),(',','comma',300)]:
  p=TTGlyphPen(None)
  if c=='-':rect(p,70,300,330,365)
  elif c==':':rect(p,105,390,190,475);rect(p,105,120,190,205)
  else:rect(p,105,40,190,125);poly(p,[(145,40),(190,40),(125,-90),(80,-90)])
  glyphs[name]=p.glyph();metrics[name]=(aw,0);cmap[ord(c)]=name;order.append(name)
 p=TTGlyphPen(None);glyphs['space']=p.glyph();metrics['space']=(250,0);cmap[32]='space';order.append('space')
 # É construction evidence: bounded direct E+acute outline, no anchor claim.
 p=TTGlyphPen(None);rect(p,60,0,145,CAP);rect(p,60,615,570,CAP);rect(p,60,305,520,390);rect(p,60,0,570,85);poly(p,[(300,760),(390,850),(475,850),(365,760)]);glyphs['Eacute']=p.glyph();metrics['Eacute']=(570,60);cmap[0x00C9]='Eacute';order.append('Eacute')
 fb=FontBuilder(UPM,isTTF=True);fb.setupGlyphOrder(order);fb.setupCharacterMap(cmap);fb.setupGlyf(glyphs);fb.setupHorizontalMetrics(metrics);fb.setupHorizontalHeader(ascent=900,descent=-200);fb.setupOS2(sTypoAscender=900,sTypoDescender=-200,usWinAscent=900,usWinDescent=200);fb.setupNameTable({'familyName':'T021 LogMate Balanced Expanded','styleName':'Regular','uniqueFontIdentifier':'T021-LogMate-Balanced-Expanded','fullName':'T021 LogMate Balanced Expanded Regular','psName':'T021-LogMate-Balanced-Expanded-Regular'});fb.setupPost();fb.setupMaxp();path=OUT/'T021-LogMate-Balanced-Expanded.ttf';fb.save(path);return path,cmap

path,cmap=build(); required=set(''.join(STRINGS));missing=sorted(ch for ch in required if ord(ch) not in cmap)
res={'upm':UPM,'kerning':False,'artifact':path.name,'required_unique_nonspace':len(required-{' '}),'covered_unique_nonspace':len((required-{' '})-{*missing}),'missing':missing,'sizes_px':[14,17,24],'measurements':{}}
for px in (14,17,24):
 f=ImageFont.truetype(str(path),px);res['measurements'][str(px)]={s:round(f.getlength(s),4) for s in STRINGS}
(OUT/'T021-logmate-operational-family-expansion-results.json').write_text(json.dumps(res,indent=2),encoding='utf-8')
print(json.dumps(res,indent=2))
