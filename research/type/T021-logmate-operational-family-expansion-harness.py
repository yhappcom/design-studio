"""T021 LogMate operational-family expansion harness — R3 ambiguity revision.

Research-only bounded font. Kerning stays OFF. R3 separates ambiguity-critical
5/S and 0/O constructions and emits deterministic 14/17/24 px specimen PNGs.
"""
from pathlib import Path
import json
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import Image, ImageDraw, ImageFont

UPM=1000; CAP=700; XH=500; STEM=82
OUT=Path('/tmp/t021-logmate-expanded-r3'); OUT.mkdir(exist_ok=True)
UPPER='ABCDEFGHIJKLMNOPRSTUVX'; LOWER='nol'; DIGITS='0123456789'; PUNCT='-:,'
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
def contour(p,pts):
 p.moveTo(pts[0]);
 for q in pts[1:]: p.lineTo(q)
 p.closePath()
def ring(p,x0,y0,x1,y1,t=STEM):
 contour(p,[(x0,y0),(x1,y0),(x1,y1),(x0,y1)])
 contour(p,[(x0+t,y0+t),(x0+t,y1-t),(x1-t,y1-t),(x1-t,y0+t)])
def open_round(p,x0,y0,x1,y1,t=STEM,kind='C'):
 rect(p,x0,y0,x0+t,y1); rect(p,x0,y1-t,x1,y1); rect(p,x0,y0,x1,y0+t)
 if kind=='G': rect(p,(x0+x1)//2,300,x1,300+t); rect(p,x1-t,300,x1,455)
def bowl(p,x0,y0,x1,y1,mid=False):
 rect(p,x0,y0,x0+STEM,y1); rect(p,x0,y1-STEM,x1-STEM,y1); rect(p,x0,y0,x1-STEM,y0+STEM); rect(p,x1-STEM,y0+STEM,x1,y1-STEM)
 if mid: rect(p,x0,310,x1-STEM,390)
def glyph_upper(c,aw,lsb):
 p=TTGlyphPen(None); r=aw-lsb; m=(lsb+r)/2
 if c=='O': ring(p,lsb,-10,r,CAP+10)
 elif c in 'CG': open_round(p,lsb,-10,r,CAP+10,kind=c)
 elif c=='D': bowl(p,lsb,0,r,CAP)
 elif c=='B': bowl(p,lsb,0,r,CAP,mid=True)
 elif c=='R': bowl(p,lsb,310,r,CAP); rect(p,lsb,0,lsb+STEM,CAP); poly(p,[(lsb+STEM,330),(lsb+STEM+70,330),(r,0),(r-STEM,0)])
 elif c=='S':
  # R3: diagonal transition shoulders make S structurally distinct from digit 5.
  rect(p,lsb+55,615,r,CAP); rect(p,lsb+55,0,r-55,STEM); rect(p,lsb+25,310,r-25,390)
  poly(p,[(lsb+55,615),(lsb+55+STEM,615),(lsb+STEM,390),(lsb+25,390)])
  poly(p,[(r-25,310),(r-STEM,310),(r-55-STEM,STEM),(r-55,STEM)])
 elif c=='U': rect(p,lsb,STEM,lsb+STEM,CAP); rect(p,r-STEM,STEM,r,CAP); rect(p,lsb,0,r,STEM)
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
 elif c=='P': bowl(p,lsb,310,r,CAP); rect(p,lsb,0,lsb+STEM,CAP)
 else: raise ValueError(f'No explicit uppercase construction for {c}')
 return p.glyph()
def glyph_lower(c):
 p=TTGlyphPen(None); aw=540; l=55; r=aw-55
 if c=='l': rect(p,170,0,170+STEM,CAP); rect(p,145,0,320,STEM)
 elif c=='n': rect(p,l,0,l+STEM,XH); rect(p,r-STEM,0,r,365); rect(p,l+STEM,418,r-STEM,XH); rect(p,r-STEM,330,r,XH)
 elif c=='o': ring(p,l,-8,r,XH+8,76)
 else: raise ValueError(c)
 return p.glyph(),(aw,l)
def glyph_digit(c):
 p=TTGlyphPen(None); aw=560; l=55; r=505; m=280
 if c=='0':
  # R3: slashed zero creates an internal distinction from uppercase O.
  ring(p,l,-8,r,CAP+8,76); poly(p,[(l+110,80),(l+165,80),(r-110,CAP-80),(r-165,CAP-80)])
 elif c=='1': rect(p,m-42,0,m+42,CAP); rect(p,140,0,420,STEM); poly(p,[(170,535),(m-42,CAP),(m+42,CAP),(m+42,535)])
 elif c=='2': rect(p,l,615,r,CAP); rect(p,r-STEM,330,r,615); rect(p,l,300,r,382); rect(p,l,STEM,l+STEM,300); rect(p,l,0,r,STEM)
 elif c=='3': rect(p,l,615,r,CAP); rect(p,l+55,310,r,390); rect(p,l,0,r,STEM); rect(p,r-STEM,0,r,CAP)
 elif c=='4': rect(p,r-STEM,0,r,CAP); rect(p,l,270,r,352); poly(p,[(l,352),(r-STEM,700),(r,700),(l+STEM,352)])
 elif c=='5': rect(p,l,615,r,CAP); rect(p,l,310,r,390); rect(p,l,0,r,STEM); rect(p,l,310,l+STEM,CAP); rect(p,r-STEM,0,r,310)
 elif c=='6': rect(p,l,0,l+STEM,CAP); rect(p,l,615,r-40,CAP); rect(p,l,310,r,390); rect(p,l,0,r,STEM); rect(p,r-STEM,0,r,310)
 elif c=='7': rect(p,l,615,r,CAP); poly(p,[(r-STEM,615),(r,615),(m,0),(m-STEM,0)])
 elif c=='8': ring(p,l,310,r,CAP+8,72); ring(p,l,-8,r,390,72)
 elif c=='9': rect(p,r-STEM,0,r,CAP); rect(p,l+40,615,r,CAP); rect(p,l,310,r,390); rect(p,l,390,l+STEM,CAP)
 else: raise ValueError(c)
 return p.glyph(),(aw,l)
def build():
 glyphs={}; metrics={}; cmap={}; order=['.notdef']; p=TTGlyphPen(None); rect(p,50,0,450,CAP); glyphs['.notdef']=p.glyph(); metrics['.notdef']=(500,50)
 widths={'A':610,'B':615,'C':600,'D':625,'E':570,'F':550,'G':630,'H':620,'I':420,'J':530,'K':610,'L':560,'M':700,'N':635,'O':620,'P':600,'R':620,'S':590,'T':580,'U':625,'V':610,'X':610}; assert set(UPPER)==set(widths)
 for c in UPPER:
  aw=widths[c]; l=55 if c in 'OCGDSBU' else 60; glyphs[c]=glyph_upper(c,aw,l); metrics[c]=(aw,l); cmap[ord(c)]=c; order.append(c)
 for c in LOWER:
  g,m=glyph_lower(c); glyphs[c]=g; metrics[c]=m; cmap[ord(c)]=c; order.append(c)
 for c in DIGITS:
  g,m=glyph_digit(c); glyphs[c]=g; metrics[c]=m; cmap[ord(c)]=c; order.append(c)
 for c,name,aw in [('-','hyphen',400),(':','colon',300),(',','comma',300)]:
  p=TTGlyphPen(None)
  if c=='-': rect(p,70,305,330,370)
  elif c==':': rect(p,108,400,190,482); rect(p,108,135,190,217)
  else: rect(p,108,45,190,127); poly(p,[(145,45),(190,45),(125,-85),(80,-85)])
  glyphs[name]=p.glyph(); metrics[name]=(aw,0); cmap[ord(c)]=name; order.append(name)
 p=TTGlyphPen(None); glyphs['space']=p.glyph(); metrics['space']=(250,0); cmap[32]='space'; order.append('space')
 p=TTGlyphPen(None); rect(p,60,0,142,CAP); rect(p,60,615,570,CAP); rect(p,60,310,520,390); rect(p,60,0,570,STEM); poly(p,[(300,760),(390,850),(475,850),(365,760)]); glyphs['Eacute']=p.glyph(); metrics['Eacute']=(570,60); cmap[0x00C9]='Eacute'; order.append('Eacute')
 fb=FontBuilder(UPM,isTTF=True); fb.setupGlyphOrder(order); fb.setupCharacterMap(cmap); fb.setupGlyf(glyphs); fb.setupHorizontalMetrics(metrics); fb.setupHorizontalHeader(ascent=900,descent=-200); fb.setupOS2(sTypoAscender=900,sTypoDescender=-200,usWinAscent=900,usWinDescent=200); fb.setupNameTable({'familyName':'T021 LogMate Balanced Expanded','styleName':'Regular','uniqueFontIdentifier':'T021-LogMate-Balanced-Expanded-R3','fullName':'T021 LogMate Balanced Expanded R3','psName':'T021-LogMate-Balanced-Expanded-R3'}); fb.setupPost(); fb.setupMaxp(); path=OUT/'T021-LogMate-Balanced-Expanded-R3.ttf'; fb.save(path); return path,cmap

def specimen(path,px):
 font=ImageFont.truetype(str(path),px); lines=['AMBIGUITY  '+ '   '.join(AMBIG[:8]), 'AMBIGUITY  '+ '   '.join(AMBIG[8:]), 'AIRPORTS   '+ '   '.join(AIRPORTS), 'IDENTIFIERS  '+ '   '.join(IDENTIFIERS), 'NUMERIC    '+ '   '.join(NUMERIC), 'SPACING    '+ '   '.join(SPACING)]
 widths=[font.getlength(x) for x in lines]; line_h=max(px+10,int(px*1.8)); im=Image.new('L',(int(max(widths)+30),line_h*len(lines)+20),255); d=ImageDraw.Draw(im)
 for i,line in enumerate(lines): d.text((15,10+i*line_h),line,font=font,fill=0)
 out=OUT/f'T021-R3-specimen-{px}px.png'; im.save(out); return out.name

path,cmap=build(); required=set(''.join(STRINGS)); missing=sorted(ch for ch in required if ord(ch) not in cmap)
res={'revision':'R3-ambiguity','upm':UPM,'kerning':False,'artifact':path.name,'declared_uppercase':UPPER,'required_unique_nonspace':len(required-{' '}),'covered_unique_nonspace':len((required-{' '})-set(missing)),'missing':missing,'sizes_px':[14,17,24],'specimens':{},'measurements':{}}
for px in (14,17,24):
 f=ImageFont.truetype(str(path),px); res['measurements'][str(px)]={s:round(f.getlength(s),4) for s in STRINGS}; res['specimens'][str(px)]=specimen(path,px)
(OUT/'T021-logmate-operational-family-expansion-R3-results.json').write_text(json.dumps(res,indent=2),encoding='utf-8'); print(json.dumps(res,indent=2))
