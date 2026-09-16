"""T021 R4D full-family promotion harness.

Transfers the accepted R4C shared grammar into the bounded 36/36 operational
family. Kerning remains OFF. This is research evidence, not human readability
or production-font evidence.
"""
from pathlib import Path
import json
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import Image, ImageDraw, ImageFont

UPM=1000; CAP=700; XH=500; STEM=82
OUT=Path('/tmp/t021-logmate-r4d'); OUT.mkdir(exist_ok=True)
UPPER='ABCDEFGHIJKLMNOPRSTUVX'; LOWER='nol'; DIGITS='0123456789'
AIRPORTS=['ICN','NRT','SIN','JFK','LHR','CDG','HND','DXB','FRA','LAX']
IDENTIFIERS=['KE704','BA117','AF264','B737-900','B737-8','A320-200','HL8301','N12345','G-EUOH']
NUMERIC=['00:45','02:18','09:55','12:40','1,284:35','9,999:59','1','11','111','8','88','888']
AMBIG=['5S','S5','555','SSS','0O','O0','000','OOO','1Il','lI1','111','III','lll','8B','B8','888','BBB']
SPACING=['HHOO','HOHOHO','nono','noon','AVAVA','TOTO','LITIL']
STRINGS=AIRPORTS+IDENTIFIERS+NUMERIC+AMBIG+SPACING

def rect(p,x0,y0,x1,y1):
 p.moveTo((x0,y0)); p.lineTo((x1,y0)); p.lineTo((x1,y1)); p.lineTo((x0,y1)); p.closePath()
def poly(p,pts):
 p.moveTo(pts[0]);
 for q in pts[1:]: p.lineTo(q)
 p.closePath()
def oval(p,x0,y0,x1,y1,t=82):
 # quadratic oval, clockwise outer / reverse inner
 mx=(x0+x1)/2; my=(y0+y1)/2; k=.56
 p.moveTo((mx,y1)); p.qCurveTo((x1,y1),(x1,my)); p.qCurveTo((x1,y0),(mx,y0)); p.qCurveTo((x0,y0),(x0,my)); p.qCurveTo((x0,y1),(mx,y1)); p.closePath()
 ix0=x0+t; ix1=x1-t; iy0=y0+t; iy1=y1-t; imx=(ix0+ix1)/2; imy=(iy0+iy1)/2
 p.moveTo((imx,iy1)); p.qCurveTo((ix0,iy1),(ix0,imy)); p.qCurveTo((ix0,iy0),(imx,iy0)); p.qCurveTo((ix1,iy0),(ix1,imy)); p.qCurveTo((ix1,iy1),(imx,iy1)); p.closePath()
def bowl_right(p,x0,y0,x1,y1,t=82):
 # flat stem side + rounded right side, explicit counter
 my=(y0+y1)/2
 p.moveTo((x0,y0)); p.lineTo((x0,y1)); p.lineTo((x1-t,y1)); p.qCurveTo((x1,y1),(x1,my)); p.qCurveTo((x1,y0),(x1-t,y0)); p.closePath()
 p.moveTo((x0+t,y0+t)); p.lineTo((x1-t-15,y0+t)); p.qCurveTo((x1-t,y0+t),(x1-t,my)); p.qCurveTo((x1-t,y1-t),(x1-t-15,y1-t)); p.lineTo((x0+t,y1-t)); p.closePath()
def open_c(p,x0,y0,x1,y1,t=82,gbar=False):
 my=(y0+y1)/2; gap=125
 p.moveTo((x1-gap,y1)); p.qCurveTo((x0,y1),(x0,my)); p.qCurveTo((x0,y0),(x1-gap,y0)); p.lineTo((x1-gap,y0+t)); p.qCurveTo((x0+t,y0+t),(x0+t,my)); p.qCurveTo((x0+t,y1-t),(x1-gap,y1-t)); p.closePath()
 if gbar: rect(p,(x0+x1)//2,300,x1,382); rect(p,x1-82,300,x1,455)
def upper(c,aw,lsb):
 p=TTGlyphPen(None); r=aw-lsb; m=(lsb+r)/2
 if c=='O': oval(p,lsb,-12,r,CAP+12,88)
 elif c in 'CG': open_c(p,lsb,-12,r,CAP+12,82,c=='G')
 elif c=='D': rect(p,lsb,0,lsb+STEM,CAP); bowl_right(p,lsb,0,r,CAP,88)
 elif c=='B':
  rect(p,lsb,0,lsb+STEM,CAP); bowl_right(p,lsb,350,r-18,CAP,78); bowl_right(p,lsb,0,r,360,84)
 elif c=='P': rect(p,lsb,0,lsb+STEM,CAP); bowl_right(p,lsb,320,r,CAP,82)
 elif c=='R':
  rect(p,lsb,0,lsb+STEM,CAP); bowl_right(p,lsb,320,r,CAP,82); poly(p,[(lsb+STEM,335),(lsb+STEM+70,335),(r,0),(r-STEM,0)])
 elif c=='S':
  # continuous-ish opposing curved shoulders, structurally unlike 5
  p.moveTo((r-35,CAP)); p.qCurveTo((lsb+15,CAP),(lsb+35,430)); p.qCurveTo((lsb+45,345),(m,330)); p.qCurveTo((r-10,310),(r-35,0)); p.lineTo((r-125,0)); p.qCurveTo((r-80,220),(m,245)); p.qCurveTo((lsb+115,265),(lsb+125,430)); p.qCurveTo((lsb+115,615),(r-35,615)); p.closePath()
 elif c=='U':
  rect(p,lsb,125,lsb+STEM,CAP); rect(p,r-STEM,125,r,CAP); p.moveTo((lsb,125)); p.qCurveTo((m,-20),(r,125)); p.lineTo((r-STEM,125)); p.qCurveTo((m,70),(lsb+STEM,125)); p.closePath()
 elif c=='H': rect(p,lsb,0,lsb+STEM,CAP); rect(p,r-STEM,0,r,CAP); rect(p,lsb,310,r,390)
 elif c=='M': rect(p,lsb,0,lsb+STEM,CAP); rect(p,r-STEM,0,r,CAP); poly(p,[(lsb+STEM,CAP),(lsb+2*STEM,CAP),(m,365),(m,245)]); poly(p,[(r-2*STEM,CAP),(r-STEM,CAP),(m,365),(m,245)])
 elif c=='N': rect(p,lsb,0,lsb+STEM,CAP); rect(p,r-STEM,0,r,CAP); poly(p,[(lsb+STEM,CAP),(lsb+2*STEM,CAP),(r-STEM,0),(r-2*STEM,0)])
 elif c=='A': poly(p,[(lsb,0),(lsb+STEM,0),(m,CAP),(m-STEM,CAP)]); poly(p,[(r-STEM,0),(r,0),(m+STEM,CAP),(m,CAP)]); rect(p,lsb+115,280,r-115,355)
 elif c=='V': poly(p,[(lsb,CAP),(lsb+STEM,CAP),(m+30,0),(m-50,0)]); poly(p,[(r-STEM,CAP),(r,CAP),(m+50,0),(m-30,0)])
 elif c=='X': poly(p,[(lsb,0),(lsb+STEM,0),(r,CAP),(r-STEM,CAP)]); poly(p,[(r-STEM,0),(r,0),(lsb+STEM,CAP),(lsb,CAP)])
 elif c=='K': rect(p,lsb,0,lsb+STEM,CAP); poly(p,[(lsb+STEM,330),(r-STEM,CAP),(r,CAP),(lsb+STEM,395)]); poly(p,[(lsb+STEM,370),(r,0),(r-STEM,0),(lsb+STEM,305)])
 elif c in 'EF': rect(p,lsb,0,lsb+STEM,CAP); rect(p,lsb,615,r,CAP); rect(p,lsb,310,r-30,390); (rect(p,lsb,0,r,STEM) if c=='E' else None)
 elif c=='L': rect(p,lsb,0,lsb+STEM,CAP); rect(p,lsb,0,r,STEM)
 elif c=='I': rect(p,lsb,615,r,CAP); rect(p,lsb,0,r,STEM); rect(p,m-STEM/2,0,m+STEM/2,CAP)
 elif c=='T': rect(p,lsb,615,r,CAP); rect(p,m-STEM/2,0,m+STEM/2,CAP)
 elif c=='J': rect(p,lsb,615,r,CAP); rect(p,r-STEM,80,r,CAP); rect(p,lsb+45,0,r,STEM); rect(p,lsb+45,0,lsb+45+STEM,180)
 else: raise ValueError(c)
 return p.glyph()
def lower(c):
 p=TTGlyphPen(None); aw=540; l=55; r=485
 if c=='l': rect(p,170,0,252,CAP); rect(p,145,0,320,82)
 elif c=='o': oval(p,l,-10,r,XH+10,78)
 elif c=='n':
  rect(p,l,0,l+82,XH); rect(p,r-82,0,r,360); p.moveTo((l+82,360)); p.qCurveTo((250,520),(r,360)); p.lineTo((r-82,360)); p.qCurveTo((250,430),(l+82,330)); p.closePath()
 return p.glyph(),(aw,l)
def digit(c):
 p=TTGlyphPen(None); aw=560; l=45; r=515; m=280
 if c=='0': oval(p,l,-12,r,CAP+12,88); poly(p,[(l+115,80),(l+170,80),(r-115,CAP-80),(r-170,CAP-80)])
 elif c=='1': rect(p,m-42,0,m+42,CAP); rect(p,140,0,420,82); poly(p,[(170,535),(m-42,CAP),(m+42,CAP),(m+42,535)])
 elif c=='5':
  rect(p,l,615,r,CAP); rect(p,l,350,l+82,CAP); rect(p,l,330,r-105,412); p.moveTo((r-105,412)); p.qCurveTo((r+5,360),(r,165)); p.qCurveTo((r,0),(l+55,0)); p.lineTo((l+55,82)); p.qCurveTo((r-82,82),(r-82,175)); p.qCurveTo((r-82,315),(r-105,330)); p.closePath()
 elif c=='8': oval(p,l,345,r,CAP+12,76); oval(p,l,-12,r,365,80)
 elif c=='2': rect(p,l,615,r,CAP); rect(p,r-STEM,330,r,615); rect(p,l,300,r,382); rect(p,l,82,l+82,300); rect(p,l,0,r,82)
 elif c=='3': rect(p,l,615,r,CAP); rect(p,l+55,310,r,390); rect(p,l,0,r,82); rect(p,r-82,0,r,CAP)
 elif c=='4': rect(p,r-82,0,r,CAP); rect(p,l,270,r,352); poly(p,[(l,352),(r-82,700),(r,700),(l+82,352)])
 elif c=='6': rect(p,l,0,l+82,CAP); rect(p,l,615,r-40,CAP); rect(p,l,310,r,390); rect(p,l,0,r,82); rect(p,r-82,0,r,310)
 elif c=='7': rect(p,l,615,r,CAP); poly(p,[(r-82,615),(r,615),(m,0),(m-82,0)])
 elif c=='9': rect(p,r-82,0,r,CAP); rect(p,l+40,615,r,CAP); rect(p,l,310,r,390); rect(p,l,390,l+82,CAP)
 return p.glyph(),(aw,l)

def build():
 glyphs={}; metrics={}; cmap={}; order=['.notdef']; p=TTGlyphPen(None); rect(p,50,0,450,CAP); glyphs['.notdef']=p.glyph(); metrics['.notdef']=(500,50)
 widths={'A':610,'B':615,'C':600,'D':625,'E':570,'F':550,'G':630,'H':620,'I':420,'J':530,'K':610,'L':560,'M':700,'N':635,'O':620,'P':600,'R':620,'S':590,'T':580,'U':625,'V':610,'X':610}
 for c in UPPER:
  aw=widths[c]; l=55 if c in 'OCGDSBU' else 60; glyphs[c]=upper(c,aw,l); metrics[c]=(aw,l); cmap[ord(c)]=c; order.append(c)
 for c in LOWER:
  g,m=lower(c); glyphs[c]=g; metrics[c]=m; cmap[ord(c)]=c; order.append(c)
 for c in DIGITS:
  g,m=digit(c); glyphs[c]=g; metrics[c]=m; cmap[ord(c)]=c; order.append(c)
 for c,name,aw in [('-','hyphen',400),(':','colon',300),(',','comma',300)]:
  p=TTGlyphPen(None)
  if c=='-': rect(p,70,305,330,370)
  elif c==':': rect(p,108,400,190,482); rect(p,108,135,190,217)
  else: rect(p,108,45,190,127); poly(p,[(145,45),(190,45),(125,-85),(80,-85)])
  glyphs[name]=p.glyph(); metrics[name]=(aw,0); cmap[ord(c)]=name; order.append(name)
 p=TTGlyphPen(None); glyphs['space']=p.glyph(); metrics['space']=(250,0); cmap[32]='space'; order.append('space')
 p=TTGlyphPen(None); rect(p,60,0,142,CAP); rect(p,60,615,570,CAP); rect(p,60,310,520,390); rect(p,60,0,570,82); poly(p,[(300,760),(390,850),(475,850),(365,760)]); glyphs['Eacute']=p.glyph(); metrics['Eacute']=(570,60); cmap[0x00C9]='Eacute'; order.append('Eacute')
 fb=FontBuilder(UPM,isTTF=True); fb.setupGlyphOrder(order); fb.setupCharacterMap(cmap); fb.setupGlyf(glyphs); fb.setupHorizontalMetrics(metrics); fb.setupHorizontalHeader(ascent=900,descent=-200); fb.setupOS2(sTypoAscender=900,sTypoDescender=-200,usWinAscent=900,usWinDescent=200); fb.setupNameTable({'familyName':'T021 LogMate R4D','styleName':'Regular','uniqueFontIdentifier':'T021-LogMate-R4D','fullName':'T021 LogMate R4D','psName':'T021-LogMate-R4D'}); fb.setupPost(); fb.setupMaxp(); path=OUT/'T021-LogMate-R4D.ttf'; fb.save(path); return path,cmap

def specimen(path,px):
 f=ImageFont.truetype(str(path),px); lines=['AMBIGUITY  '+'   '.join(AMBIG[:8]),'AMBIGUITY  '+'   '.join(AMBIG[8:]),'AIRPORTS   '+'   '.join(AIRPORTS),'IDENTIFIERS  '+'   '.join(IDENTIFIERS),'NUMERIC    '+'   '.join(NUMERIC),'SPACING    '+'   '.join(SPACING)]
 widths=[f.getlength(x) for x in lines]; lh=max(px+10,int(px*1.8)); im=Image.new('L',(int(max(widths)+30),lh*len(lines)+20),255); d=ImageDraw.Draw(im)
 for i,line in enumerate(lines): d.text((15,10+i*lh),line,font=f,fill=0)
 out=OUT/f'T021-R4D-specimen-{px}px.png'; im.save(out,optimize=False); return out.name

path,cmap=build(); required=set(''.join(STRINGS)); missing=sorted(ch for ch in required if ord(ch) not in cmap)
res={'revision':'R4D-full-family-promotion','upm':UPM,'kerning':False,'artifact':path.name,'required_unique_nonspace':len(required-{' '}),'covered_unique_nonspace':len((required-{' '})-set(missing)),'missing':missing,'sizes_px':[14,17,24],'specimens':{},'measurements':{}}
for px in (14,17,24):
 f=ImageFont.truetype(str(path),px); res['measurements'][str(px)]={s:round(f.getlength(s),4) for s in STRINGS}; res['specimens'][str(px)]=specimen(path,px)
(OUT/'T021-r4d-full-family-results.json').write_text(json.dumps(res,indent=2),encoding='utf-8'); print(json.dumps(res,indent=2))
