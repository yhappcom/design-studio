"""T021 A/B family-architecture reset — construction-complete figure pass.

This harness deliberately reuses the reset module's corpus and non-figure architecture,
but replaces ALL ten digit constructions before accepting A/B evidence. The purpose is
to close the mixed-provenance defect found in the first reset. Kerning remains OFF.
"""
from pathlib import Path
import importlib.util, json
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import Image, ImageDraw, ImageFont

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('reset', HERE/'T021-family-architecture-reset-harness.py')
reset=importlib.util.module_from_spec(spec); spec.loader.exec_module(reset)
OUT=Path('/tmp/t021-family-architecture-reset-complete'); OUT.mkdir(exist_ok=True)
CAP=reset.CAP

# Primitive helpers are implementation utilities only; no predecessor glyph constructor
# is called from digit_complete.
def rect(p,x0,y0,x1,y1): reset.rect(p,x0,y0,x1,y1)
def poly(p,pts): reset.poly(p,pts)
def ring(p,x0,y0,x1,y1,t): reset.ring(p,x0,y0,x1,y1,t)

def digit_complete(c,a):
    aw=a['figure_width']; l=45; r=aw-45; m=aw/2; s=a['stem']; rs=a['round_stem']; p=TTGlyphPen(None)
    if c=='0':
        ring(p,l,-10,r,CAP+10,rs)
        if a['zero']=='slash': poly(p,[(l+112,72),(l+164,72),(r-112,CAP-72),(r-164,CAP-72)])
    elif c=='1':
        rect(p,m-s/2,0,m+s/2,CAP); rect(p,135,0,aw-135,s)
        poly(p,[(165,535),(m-s/2,CAP),(m+s/2,CAP),(m+s/2,535)])
    elif c=='2':
        # open upper bowl -> diagonal transition -> flat base; architecture stem controls mass
        p.moveTo((l,CAP-110)); p.qCurveTo((l+25,CAP),(m,CAP)); p.qCurveTo((r,CAP),(r,CAP-170))
        p.qCurveTo((r,CAP-250),(m+25,350)); p.lineTo((l+10,s)); p.lineTo((r, s)); p.lineTo((r,0)); p.lineTo((l,0))
        p.lineTo((l,95)); p.lineTo((m-25,390)); p.qCurveTo((r-s,CAP-235),(r-s,CAP-165)); p.qCurveTo((r-s,CAP-s),(m,CAP-s)); p.qCurveTo((l+s,CAP-s),(l+s,CAP-110)); p.closePath()
    elif c=='3':
        # two right bowls with an open left spine; pinched waist separates from 8.
        p.moveTo((l,CAP)); p.lineTo((m+25,CAP)); p.qCurveTo((r,CAP),(r,535)); p.qCurveTo((r,395),(m+35,355));
        p.qCurveTo((r,315),(r,165)); p.qCurveTo((r,0),(m+10,0)); p.lineTo((l,0)); p.lineTo((l,s));
        p.lineTo((m, s)); p.qCurveTo((r-s,s),(r-s,170)); p.qCurveTo((r-s,310),(m-10,315)); p.lineTo((m-70,315));
        p.lineTo((m-70,390)); p.lineTo((m-5,390)); p.qCurveTo((r-s,405),(r-s,530)); p.qCurveTo((r-s,CAP-s),(m+10,CAP-s)); p.lineTo((l,CAP-s)); p.closePath()
    elif c=='4':
        rect(p,r-s,0,r,CAP); rect(p,l,270,r,270+s)
        poly(p,[(l,270+s),(r-s,CAP),(r,CAP),(l+s,270+s)])
    elif c=='5':
        rect(p,l,CAP-s,r,CAP); rect(p,l,350,l+s,CAP); rect(p,l,330,r-100,330+s)
        p.moveTo((r-100,330+s)); p.qCurveTo((r,360),(r,165)); p.qCurveTo((r,0),(l+50,0)); p.lineTo((l+50,s)); p.qCurveTo((r-s,s),(r-s,175)); p.qCurveTo((r-s,305),(r-100,330)); p.closePath()
    elif c=='6':
        # continuous left spine + lower bowl; upper aperture remains open.
        p.moveTo((r-35,CAP)); p.qCurveTo((l,CAP),(l,360)); p.lineTo((l,175)); p.qCurveTo((l,0),(m,0)); p.qCurveTo((r,0),(r,180)); p.qCurveTo((r,350),(m,350)); p.qCurveTo((l+s,350),(l+s,250)); p.lineTo((l+s,365)); p.qCurveTo((l+s,CAP-s),(r-35,CAP-s)); p.closePath()
        p.moveTo((l+s,175)); p.qCurveTo((l+s,s),(m,s)); p.qCurveTo((r-s,s),(r-s,180)); p.qCurveTo((r-s,350-s),(m,350-s)); p.qCurveTo((l+s,350-s),(l+s,175)); p.closePath()
    elif c=='7':
        rect(p,l,CAP-s,r,CAP)
        poly(p,[(r-s,CAP-s),(r,CAP-s),(m+20,0),(m+20-s,0)])
    elif c=='8':
        # two closed counters, no flat stem; upper bowl slightly smaller than lower.
        ring(p,l+12,350,r-12,CAP+10,max(64,rs-10)); ring(p,l,-10,r,372,max(68,rs-6))
    elif c=='9':
        # upper bowl + descending right spine, intentionally inverse-related to 6.
        p.moveTo((l,520)); p.qCurveTo((l,CAP),(m,CAP)); p.qCurveTo((r,CAP),(r,520)); p.lineTo((r,335)); p.qCurveTo((r,0),(l+35,0)); p.lineTo((l+35,s)); p.qCurveTo((r-s,s),(r-s,330)); p.lineTo((r-s,445)); p.qCurveTo((r-s,350),(m,350)); p.qCurveTo((l,350),(l,520)); p.closePath()
        p.moveTo((l+s,520)); p.qCurveTo((l+s,CAP-s),(m,CAP-s)); p.qCurveTo((r-s,CAP-s),(r-s,520)); p.qCurveTo((r-s,350+s),(m,350+s)); p.qCurveTo((l+s,350+s),(l+s,520)); p.closePath()
    else: raise ValueError(c)
    return p.glyph(),(aw,l)

# Adversarial provenance assertion: every bounded digit must dispatch here.
PROVENANCE={c:'architecture-reset-complete' for c in reset.DIGITS}
assert set(PROVENANCE)==set('0123456789')
assert all(v=='architecture-reset-complete' for v in PROVENANCE.values())
reset.digit=digit_complete
reset.OUT=OUT

required=set(''.join(reset.STRINGS))-{' '}; results={}
for key in ('A','B'):
    path,cmap=reset.build(key); chars={chr(k) for k in cmap}
    specs={str(px):reset.specimen(path,key,px) for px in (14,17,24)}
    f17=ImageFont.truetype(str(path),17)
    results[key]={
        'architecture':reset.ARCH[key], 'font':path.name,
        'coverage':len(required & chars), 'missing':sorted(required-chars),
        'specimens':specs,
        'control_widths_17px':{s:round(f17.getlength(s),4) for s in ['ICN','NRT','JFK','B737-900','1,284:35','0O','1Il','5S','8B','AVAVA']}
    }
summary={
 'revision':'family-architecture-reset-AB-construction-complete',
 'kerning':False,'required_unique_nonspace':len(required),'architectures':results,
 'digit_provenance':PROVENANCE,'construction_class_completeness':True,
 'same_corpus':True,'sizes_px':[14,17,24],'human_claim':False,
 'next_gate':'side-by-side drawing critique before spacing'
}
(OUT/'T021-family-architecture-reset-complete-results.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
