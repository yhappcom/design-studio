"""T021 R4E full-family integration + zero-alternative harness.

TRANSFER VALIDATION of R4D. Reuses its bounded corpus/build plumbing, but replaces
C/G/S/P/R with one terminal/join grammar and emits slash-zero + plain-zero
controls. Kerning remains OFF. Human readability is not claimed.
"""
from pathlib import Path
import importlib.util, json, shutil
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import ImageFont

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('r4d', HERE/'T021-r4d-full-family-promotion-harness.py')
r4d=importlib.util.module_from_spec(spec); spec.loader.exec_module(r4d)
OUT=Path('/tmp/t021-logmate-r4e'); OUT.mkdir(exist_ok=True)
r4d.OUT=OUT
STEM=r4d.STEM
# Integrated grammar tokens. Straight terminals remain square; curves terminate
# with the same 82-unit thickness and a 24-unit optical inset. Bowls join stems
# with an 18-unit shoulder inset instead of colliding at the full stem edge.
TERM=82; OPT=24; JOIN=18; APERTURE=150
base_upper=r4d.upper; base_digit=r4d.digit

def integrated_upper(c,aw,lsb):
    if c not in 'CGSPR': return base_upper(c,aw,lsb)
    p=TTGlyphPen(None); r=aw-lsb; m=(lsb+r)/2
    if c in 'CG':
        # open curved form with horizontal terminals; G adds one controlled bar.
        y0=-12; y1=r4d.CAP+12; my=(y0+y1)/2; xend=r-APERTURE
        p.moveTo((xend,y1)); p.qCurveTo((lsb,y1),(lsb,my)); p.qCurveTo((lsb,y0),(xend,y0));
        p.lineTo((xend,y0+TERM)); p.qCurveTo((lsb+TERM,y0+TERM),(lsb+TERM,my)); p.qCurveTo((lsb+TERM,y1-TERM),(xend,y1-TERM)); p.closePath()
        if c=='G': r4d.rect(p,m+OPT,300,r,382); r4d.rect(p,r-TERM,300,r,455)
    elif c=='S':
        # two opposing bowls joined by a controlled diagonal spine; avoids R4D's
        # pinched self-intersection and keeps terminal thickness consistent.
        p.moveTo((r-OPT,r4d.CAP)); p.qCurveTo((lsb+OPT,r4d.CAP),(lsb+OPT,455));
        p.qCurveTo((lsb+OPT,370),(m-30,330)); p.lineTo((m+55,275));
        p.qCurveTo((r-OPT,235),(r-OPT,95)); p.qCurveTo((r-OPT,0),(lsb+OPT,0));
        p.lineTo((lsb+OPT,TERM)); p.qCurveTo((r-TERM-OPT,TERM),(r-TERM-OPT,155));
        p.qCurveTo((r-TERM-OPT,210),(m+20,245)); p.lineTo((m-65,300));
        p.qCurveTo((lsb+TERM+OPT,350),(lsb+TERM+OPT,455));
        p.qCurveTo((lsb+TERM+OPT,r4d.CAP-TERM),(r-OPT,r4d.CAP-TERM)); p.closePath()
    else:
        # P/R: one shared bowl with an explicit stem-to-shoulder join inset.
        r4d.rect(p,lsb,0,lsb+STEM,r4d.CAP)
        y0=320; y1=r4d.CAP; my=(y0+y1)/2; x0=lsb+STEM-JOIN
        p.moveTo((x0,y1)); p.lineTo((r-TERM,y1)); p.qCurveTo((r,y1),(r,my)); p.qCurveTo((r,y0),(r-TERM,y0)); p.lineTo((x0,y0)); p.lineTo((x0+TERM,y0+TERM)); p.lineTo((r-TERM-OPT,y0+TERM)); p.qCurveTo((r-TERM,y0+TERM),(r-TERM,my)); p.qCurveTo((r-TERM,y1-TERM),(r-TERM-OPT,y1-TERM)); p.lineTo((x0+TERM,y1-TERM)); p.closePath()
        if c=='R': r4d.poly(p,[(lsb+STEM,335),(lsb+STEM+78,335),(r,0),(r-STEM,0)])
    return p.glyph()

def plain_zero_digit(c):
    if c!='0': return base_digit(c)
    p=TTGlyphPen(None); aw=560; l=45; r=515
    r4d.oval(p,l,-12,r,r4d.CAP+12,88)
    return p.glyph(),(aw,l)

r4d.upper=integrated_upper
# Primary candidate: slash zero.
r4d.digit=base_digit
primary,_=r4d.build(); primary_path=OUT/'T021-LogMate-R4E-slashzero.ttf'; shutil.copy2(primary,primary_path)
primary_specs={str(px):r4d.specimen(primary_path,px) for px in (14,17,24)}
# Rename generic specimen outputs to stable primary names.
for px,name in list(primary_specs.items()):
    src=OUT/name; dst=OUT/f'T021-R4E-slashzero-{px}px.png'; src.replace(dst); primary_specs[px]=dst.name
# Controlled alternative: identical geometry except zero slash removed.
r4d.digit=plain_zero_digit
plain,_=r4d.build(); plain_path=OUT/'T021-LogMate-R4E-plainzero.ttf'; shutil.copy2(plain,plain_path)
plain_specs={str(px):r4d.specimen(plain_path,px) for px in (14,17,24)}
for px,name in list(plain_specs.items()):
    src=OUT/name; dst=OUT/f'T021-R4E-plainzero-{px}px.png'; src.replace(dst); plain_specs[px]=dst.name

required=set(''.join(r4d.STRINGS))-{' '}; cmap_chars=set(chr(k) for k in r4d.build()[1])
result={
 'revision':'R4E-full-family-integration', 'kerning':False,
 'grammar':{'terminal':TERM,'optical_inset':OPT,'join_inset':JOIN,'aperture':APERTURE},
 'required_unique_nonspace':len(required),'covered_unique_nonspace':len(required & cmap_chars),'missing':sorted(required-cmap_chars),
 'primary':{'zero':'slash','font':primary_path.name,'specimens':primary_specs},
 'control':{'zero':'plain','font':plain_path.name,'specimens':plain_specs},
 'controlled_zero_comparison':'all non-zero glyph geometry identical by construction',
 'sizes_px':[14,17,24], 'human_claim':False, 'kerning_eligible':False
}
(OUT/'T021-r4e-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
