"""T021 family-architecture reset.

METHOD COMPARISON after R4E falsified serial local patching as a sufficient
family-building strategy. Two complete operational-family hypotheses are
defined from architecture tokens before glyph construction. Kerning stays OFF.
The harness is deterministic research evidence, not human readability proof.
"""
from pathlib import Path
import importlib.util, json
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import Image, ImageDraw, ImageFont

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('r4d', HERE/'T021-r4d-full-family-promotion-harness.py')
r4d=importlib.util.module_from_spec(spec); spec.loader.exec_module(r4d)
OUT=Path('/tmp/t021-family-architecture-reset'); OUT.mkdir(exist_ok=True)
UPM=1000; CAP=700; XH=500
UPPER=r4d.UPPER; LOWER=r4d.LOWER; DIGITS=r4d.DIGITS
STRINGS=r4d.STRINGS; AMBIG=r4d.AMBIG; AIRPORTS=r4d.AIRPORTS; IDENTIFIERS=r4d.IDENTIFIERS; NUMERIC=r4d.NUMERIC; SPACING=r4d.SPACING

ARCH={
 'A': {'name':'restrained-humanist-technical-proportional','stem':76,'round_stem':82,'cap_overshoot':12,'x_overshoot':10,'aperture':132,'corner':20,'join':16,'diag_comp':8,'terminal':'square-soft','figure_width':548,'zero':'plain'},
 'B': {'name':'engineered-operational-semi-mono','stem':84,'round_stem':88,'cap_overshoot':10,'x_overshoot':8,'aperture':160,'corner':10,'join':22,'diag_comp':12,'terminal':'square','figure_width':570,'zero':'slash'}
}
WIDTH_A={'A':600,'B':602,'C':594,'D':616,'E':548,'F':530,'G':624,'H':612,'I':392,'J':510,'K':594,'L':535,'M':690,'N':626,'O':614,'P':580,'R':600,'S':574,'T':560,'U':616,'V':600,'X':598}
WIDTH_B={c:600 for c in UPPER}; WIDTH_B.update({'I':430,'M':680,'J':560,'T':580})

def rect(p,x0,y0,x1,y1): r4d.rect(p,x0,y0,x1,y1)
def poly(p,pts): r4d.poly(p,pts)
def ring(p,x0,y0,x1,y1,t): r4d.oval(p,x0,y0,x1,y1,t)

def bowl(p,x0,y0,x1,y1,t):
    my=(y0+y1)/2
    p.moveTo((x0,y0)); p.lineTo((x0,y1)); p.lineTo((x1-t,y1)); p.qCurveTo((x1,y1),(x1,my)); p.qCurveTo((x1,y0),(x1-t,y0)); p.closePath()
    p.moveTo((x0+t,y0+t)); p.lineTo((x1-t-12,y0+t)); p.qCurveTo((x1-t,y0+t),(x1-t,my)); p.qCurveTo((x1-t,y1-t),(x1-t-12,y1-t)); p.lineTo((x0+t,y1-t)); p.closePath()

def upper(c,aw,lsb,a):
    s=a['stem']; rs=a['round_stem']; r=aw-lsb; m=(lsb+r)/2; ov=a['cap_overshoot']; ap=a['aperture']
    p=TTGlyphPen(None)
    if c=='O': ring(p,lsb,-ov,r,CAP+ov,rs)
    elif c in 'CG':
        y0=-ov; y1=CAP+ov; my=(y0+y1)/2; xe=r-ap
        p.moveTo((xe,y1)); p.qCurveTo((lsb,y1),(lsb,my)); p.qCurveTo((lsb,y0),(xe,y0)); p.lineTo((xe,y0+rs)); p.qCurveTo((lsb+rs,y0+rs),(lsb+rs,my)); p.qCurveTo((lsb+rs,y1-rs),(xe,y1-rs)); p.closePath()
        if c=='G': rect(p,m+20,300,r,378); rect(p,r-s,300,r,445)
    elif c=='D': rect(p,lsb,0,lsb+s,CAP); bowl(p,lsb,0,r,CAP,rs)
    elif c=='B': rect(p,lsb,0,lsb+s,CAP); bowl(p,lsb,350,r-12,CAP,rs-4); bowl(p,lsb,0,r,360,rs)
    elif c in 'PR':
        rect(p,lsb,0,lsb+s,CAP); bowl(p,lsb,320,r,CAP,rs)
        if c=='R': poly(p,[(lsb+s,335),(lsb+s+74,335),(r,0),(r-s,0)])
    elif c=='S':
        # Architecture-level S: continuous opposing shoulders, no rectangular 5 grammar.
        p.moveTo((r-20,CAP)); p.qCurveTo((lsb,CAP),(lsb,470)); p.qCurveTo((lsb,355),(m-18,325)); p.qCurveTo((r,285),(r,150)); p.qCurveTo((r,0),(lsb+18,0)); p.lineTo((lsb+18,rs)); p.qCurveTo((r-rs,rs),(r-rs,158)); p.qCurveTo((r-rs,220),(m+18,250)); p.qCurveTo((lsb+rs,290),(lsb+rs,465)); p.qCurveTo((lsb+rs,CAP-rs),(r-20,CAP-rs)); p.closePath()
    elif c=='U':
        rect(p,lsb,130,lsb+s,CAP); rect(p,r-s,130,r,CAP); p.moveTo((lsb,130)); p.qCurveTo((m,-ov),(r,130)); p.lineTo((r-s,130)); p.qCurveTo((m,70),(lsb+s,130)); p.closePath()
    elif c=='H': rect(p,lsb,0,lsb+s,CAP); rect(p,r-s,0,r,CAP); rect(p,lsb,310,r,310+s)
    elif c=='N': rect(p,lsb,0,lsb+s,CAP); rect(p,r-s,0,r,CAP); poly(p,[(lsb+s,CAP),(lsb+2*s,CAP),(r-s,0),(r-2*s,0)])
    elif c=='M': rect(p,lsb,0,lsb+s,CAP); rect(p,r-s,0,r,CAP); poly(p,[(lsb+s,CAP),(lsb+2*s,CAP),(m,350),(m,230)]); poly(p,[(r-2*s,CAP),(r-s,CAP),(m,350),(m,230)])
    elif c=='A': poly(p,[(lsb,0),(lsb+s,0),(m,CAP),(m-s,CAP)]); poly(p,[(r-s,0),(r,0),(m+s,CAP),(m,CAP)]); rect(p,lsb+112,280,r-112,350)
    elif c=='V': poly(p,[(lsb,CAP),(lsb+s,CAP),(m+28,0),(m-48,0)]); poly(p,[(r-s,CAP),(r,CAP),(m+48,0),(m-28,0)])
    elif c=='X': poly(p,[(lsb,0),(lsb+s,0),(r,CAP),(r-s,CAP)]); poly(p,[(r-s,0),(r,0),(lsb+s,CAP),(lsb,CAP)])
    elif c=='K': rect(p,lsb,0,lsb+s,CAP); poly(p,[(lsb+s,330),(r-s,CAP),(r,CAP),(lsb+s,398)]); poly(p,[(lsb+s,370),(r,0),(r-s,0),(lsb+s,302)])
    elif c in 'EF': rect(p,lsb,0,lsb+s,CAP); rect(p,lsb,CAP-s,r,CAP); rect(p,lsb,310,r-28,310+s); (rect(p,lsb,0,r,s) if c=='E' else None)
    elif c=='L': rect(p,lsb,0,lsb+s,CAP); rect(p,lsb,0,r,s)
    elif c=='I': rect(p,lsb,CAP-s,r,CAP); rect(p,lsb,0,r,s); rect(p,m-s/2,0,m+s/2,CAP)
    elif c=='T': rect(p,lsb,CAP-s,r,CAP); rect(p,m-s/2,0,m+s/2,CAP)
    elif c=='J': rect(p,lsb,CAP-s,r,CAP); rect(p,r-s,80,r,CAP); rect(p,lsb+40,0,r,s); rect(p,lsb+40,0,lsb+40+s,175)
    else: raise ValueError(c)
    return p.glyph()

def lower(c,a):
    s=a['stem']; rs=max(70,a['round_stem']-6); aw=520 if a is ARCH['A'] else 560; l=52; r=aw-52; p=TTGlyphPen(None)
    if c=='l': rect(p,170,0,170+s,CAP); rect(p,145,0,305,s)
    elif c=='o': ring(p,l,-a['x_overshoot'],r,XH+a['x_overshoot'],rs)
    elif c=='n':
        rect(p,l,0,l+s,XH); rect(p,r-s,0,r,355); p.moveTo((l+s,350)); p.qCurveTo(((l+r)/2,515),(r,350)); p.lineTo((r-s,350)); p.qCurveTo(((l+r)/2,425),(l+s,322)); p.closePath()
    return p.glyph(),(aw,l)

def digit(c,a):
    aw=a['figure_width']; l=45; r=aw-45; m=aw/2; s=a['stem']; rs=a['round_stem']; p=TTGlyphPen(None)
    if c=='0':
        ring(p,l,-10,r,CAP+10,rs)
        if a['zero']=='slash': poly(p,[(l+112,72),(l+164,72),(r-112,CAP-72),(r-164,CAP-72)])
    elif c=='1': rect(p,m-s/2,0,m+s/2,CAP); rect(p,135,0,aw-135,s); poly(p,[(165,535),(m-s/2,CAP),(m+s/2,CAP),(m+s/2,535)])
    elif c=='8': ring(p,l,345,r,CAP+10,rs-8); ring(p,l,-10,r,365,rs-4)
    elif c=='5':
        rect(p,l,CAP-s,r,CAP); rect(p,l,350,l+s,CAP); rect(p,l,330,r-100,330+s); p.moveTo((r-100,330+s)); p.qCurveTo((r,360),(r,165)); p.qCurveTo((r,0),(l+50,0)); p.lineTo((l+50,s)); p.qCurveTo((r-s,s),(r-s,175)); p.qCurveTo((r-s,305),(r-100,330)); p.closePath()
    else:
        # Remaining figures retain one coordinated rectilinear operational grammar.
        old=r4d.digit(c)[0]; return old,(aw,l)
    return p.glyph(),(aw,l)

def build(key):
    a=ARCH[key]; widths=WIDTH_A if key=='A' else WIDTH_B; glyphs={}; metrics={}; cmap={}; order=['.notdef']; p=TTGlyphPen(None); rect(p,50,0,450,CAP); glyphs['.notdef']=p.glyph(); metrics['.notdef']=(500,50)
    for c in UPPER:
        aw=widths[c]; l=52 if c in 'OCGDSBU' else 58; glyphs[c]=upper(c,aw,l,a); metrics[c]=(aw,l); cmap[ord(c)]=c; order.append(c)
    for c in LOWER:
        g,m=lower(c,a); glyphs[c]=g; metrics[c]=m; cmap[ord(c)]=c; order.append(c)
    for c in DIGITS:
        g,m=digit(c,a); glyphs[c]=g; metrics[c]=m; cmap[ord(c)]=c; order.append(c)
    for c,name,aw in [('-','hyphen',390),(':','colon',290),(',','comma',290)]:
        p=TTGlyphPen(None)
        if c=='-': rect(p,68,305,322,368)
        elif c==':': rect(p,104,400,186,482); rect(p,104,135,186,217)
        else: rect(p,104,45,186,127); poly(p,[(142,45),(186,45),(122,-82),(82,-82)])
        glyphs[name]=p.glyph(); metrics[name]=(aw,0); cmap[ord(c)]=name; order.append(name)
    p=TTGlyphPen(None); glyphs['space']=p.glyph(); metrics['space']=(245 if key=='A' else 260,0); cmap[32]='space'; order.append('space')
    fb=FontBuilder(UPM,isTTF=True); fb.setupGlyphOrder(order); fb.setupCharacterMap(cmap); fb.setupGlyf(glyphs); fb.setupHorizontalMetrics(metrics); fb.setupHorizontalHeader(ascent=900,descent=-200); fb.setupOS2(sTypoAscender=900,sTypoDescender=-200,usWinAscent=900,usWinDescent=200); fam=f'T021 Architecture {key}'; fb.setupNameTable({'familyName':fam,'styleName':'Regular','uniqueFontIdentifier':fam.replace(' ', '-'),'fullName':fam,'psName':fam.replace(' ', '-')}); fb.setupPost(); fb.setupMaxp(); path=OUT/f'T021-architecture-{key}.ttf'; fb.save(path); return path,cmap

def specimen(path,key,px):
    f=ImageFont.truetype(str(path),px); lines=['AMBIGUITY  '+'   '.join(AMBIG[:8]),'AMBIGUITY  '+'   '.join(AMBIG[8:]),'AIRPORTS   '+'   '.join(AIRPORTS),'IDENTIFIERS  '+'   '.join(IDENTIFIERS),'NUMERIC    '+'   '.join(NUMERIC),'SPACING    '+'   '.join(SPACING)]
    lh=max(px+10,int(px*1.8)); w=int(max(f.getlength(x) for x in lines)+30); im=Image.new('L',(w,lh*len(lines)+20),255); d=ImageDraw.Draw(im)
    for i,line in enumerate(lines): d.text((15,10+i*lh),line,font=f,fill=0)
    out=OUT/f'T021-architecture-{key}-{px}px.png'; im.save(out,optimize=False); return out.name

required=set(''.join(STRINGS))-{' '}; results={}
for key in ('A','B'):
    path,cmap=build(key); chars={chr(k) for k in cmap}; specs={str(px):specimen(path,key,px) for px in (14,17,24)}
    results[key]={'architecture':ARCH[key],'font':path.name,'coverage':len(required & chars),'missing':sorted(required-chars),'specimens':specs}
summary={'revision':'family-architecture-reset-AB','reason':'METHOD COMPARISON after R4E incremental repair falsification','kerning':False,'required_unique_nonspace':len(required),'architectures':results,'same_corpus':True,'sizes_px':[14,17,24],'human_claim':False,'spacing_gate':'blocked pending drawing critique'}
(OUT/'T021-family-architecture-reset-results.json').write_text(json.dumps(summary,indent=2),encoding='utf-8'); print(json.dumps(summary,indent=2))
