"""Deterministic raster verification for the exact T021 R3 research font.
Run after T021-logmate-operational-family-expansion-harness.py.
The main harness already emits specimens; this independent step verifies the
expected R3 artifact and regenerates a second proof set. No human-quality claim.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT=Path('/tmp/t021-logmate-expanded-r3')
FONT=OUT/'T021-LogMate-Balanced-Expanded-R3.ttf'
GROUPS=[
 ('AMBIGUITY',['5S S5 555 SSS','0O O0 000 OOO','1Il lI1 111 III lll','8B B8 888 BBB']),
 ('AIRPORTS',['ICN NRT SIN JFK LHR CDG HND DXB FRA LAX']),
 ('IDENTIFIERS',['KE704 BA117 AF264','B737-900 B737-8 A320-200','HL8301 N12345 G-EUOH']),
 ('TIME / TOTALS',['00:45 02:18 09:55 12:40','1,284:35 9,999:59','1 11 111   8 88 888']),
 ('SPACING',['HHOO HOHOHO','nono noon','AVAVA TOTO LITIL']),
]
if not FONT.exists(): raise FileNotFoundError(FONT)
for px in (14,17,24):
 f=ImageFont.truetype(str(FONT),px); line=max(28,px+14); rows=sum(len(x[1])+1 for x in GROUPS)+2
 im=Image.new('L',(1100,rows*line+30),255); d=ImageDraw.Draw(im); y=15
 d.text((15,y),f'T021 R3 exact candidate — {px}px — kerning OFF research proof',font=f,fill=0); y+=line*2
 for label,items in GROUPS:
  d.text((15,y),label,font=f,fill=0); y+=line
  for s in items: d.text((45,y),s,font=f,fill=0); y+=line
 target=OUT/f'T021-R3-independent-specimen-{px}px.png'; im.save(target,optimize=False); print(f'WROTE {target}')
