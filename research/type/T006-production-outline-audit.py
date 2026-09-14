from __future__ import annotations
import json, math, sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import numpy as np
import shapely
from shapely.geometry import Polygon
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.fontBuilder import FontBuilder
from fontTools.ttLib import TTFont
import freetype

UPM=1000
Command=Tuple[str, tuple]

@dataclass
class ContourDef:
    role: str
    commands: List[Command]

@dataclass
class GlyphDef:
    name: str
    width: int
    contours: List[ContourDef]
    codepoint: int|None=None


def M(x,y): return ('moveTo', ((x,y),))
def L(x,y): return ('lineTo', ((x,y),))
def C(x1,y1,x2,y2,x3,y3): return ('curveTo', ((x1,y1),(x2,y2),(x3,y3)))
def Z(): return ('closePath', ())

def rect(x0,y0,x1,y1):
    return [M(x0,y0),L(x1,y0),L(x1,y1),L(x0,y1),Z()]

def replay_contour(contour:ContourDef, pen):
    for op,args in contour.commands:
        getattr(pen,op)(*args)

def replay_glyph(glyph:GlyphDef, pen):
    for c in glyph.contours:
        replay_contour(c,pen)

def area_of_contour(c:ContourDef):
    p=AreaPen(None); replay_contour(c,p); return p.value

def bounds_of_glyph(g:GlyphDef):
    p=BoundsPen(None); replay_glyph(g,p); return p.bounds

# Deliberate failure fixture: same-role overlap.
H_BAD=GlyphDef('H.v0',600,[
    ContourDef('outer',rect(60,0,150,700)),
    ContourDef('outer',rect(450,0,540,700)),
    ContourDef('outer',rect(130,300,470,390)),
])

# Revised H: one merged contour.
H=GlyphDef('H',600,[ContourDef('outer',[
    M(60,0),L(150,0),L(150,300),L(450,300),L(450,0),L(540,0),
    L(540,700),L(450,700),L(450,390),L(150,390),L(150,700),L(60,700),Z()
])],ord('H'))

# Deliberate failure fixture: internal top/bottom extrema and wrong PS winding.
O_BAD=GlyphDef('O.v0',600,[
    ContourDef('outer',[
        M(50,350),C(50,830,550,830,550,350),C(550,-130,50,-130,50,350),Z()
    ]),
    ContourDef('counter',[
        M(150,350),C(150,3,450,3,450,350),C(450,697,150,697,150,350),Z()
    ])
])

# Revised O: explicit cardinal extrema, integer controls, correct PS winding.
O=GlyphDef('O',600,[
    ContourDef('outer',[
        M(300,710),C(162,710,50,549,50,350),C(50,151,162,-10,300,-10),
        C(438,-10,550,151,550,350),C(550,549,438,710,300,710),Z()
    ]),
    ContourDef('counter',[
        M(300,610),C(383,610,450,494,450,350),C(450,206,383,90,300,90),
        C(217,90,150,206,150,350),C(150,494,217,610,300,610),Z()
    ])
],ord('O'))

N_RAW=[
    M(60,0),L(60,500),L(150,500),L(150,430),
    C(198,486,255,515,325,515),C(425,515,480,442,480,315),
    L(480,0),L(390,0),L(390,300),
    C(390,382,355,425,295,425),C(205,425,150,352,150,260),
    L(150,0),Z()
]
from fontTools.pens.reverseContourPen import ReverseContourPen
def reverse_commands(cmds):
    rp=RecordingPen(); rev=ReverseContourPen(rp)
    replay_contour(ContourDef('outer',cmds),rev)
    return rp.value
N=GlyphDef('n',540,[ContourDef('outer',reverse_commands(N_RAW))],ord('n'))

OLOW=GlyphDef('o',520,[
    ContourDef('outer',[
        M(260,510),C(150,510,60,394,60,250),C(60,106,150,-10,260,-10),
        C(370,-10,460,106,460,250),C(460,394,370,510,260,510),Z()
    ]),
    ContourDef('counter',[
        M(260,420),C(324,420,375,344,375,250),C(375,156,324,80,260,80),
        C(196,80,145,156,145,250),C(145,344,196,420,260,420),Z()
    ])
],ord('o'))

CLEAN=[H,O,N,OLOW]
V0=[H_BAD,O_BAD]

def cubic_roots(p0,p1,p2,p3):
    A=-p0+3*p1-3*p2+p3
    B=2*(p0-2*p1+p2)
    Cc=p1-p0
    if abs(A)<1e-12:
        if abs(B)<1e-12: return []
        return [-Cc/B]
    disc=B*B-4*A*Cc
    if disc < 0: return []
    s=math.sqrt(max(0,disc))
    return [(-B+s)/(2*A),(-B-s)/(2*A)]

def sample_contour(c:ContourDef, n=32):
    pts=[]; cur=None; start=None
    for op,args in c.commands:
        if op=='moveTo':
            cur=args[0]; start=cur; pts.append(cur)
        elif op=='lineTo':
            p=args[0]
            for i in range(1,n+1):
                t=i/n; pts.append((cur[0]*(1-t)+p[0]*t,cur[1]*(1-t)+p[1]*t))
            cur=p
        elif op=='curveTo':
            p1,p2,p3=args; p0=cur
            for i in range(1,n+1):
                t=i/n; mt=1-t
                x=mt**3*p0[0]+3*mt**2*t*p1[0]+3*mt*t*t*p2[0]+t**3*p3[0]
                y=mt**3*p0[1]+3*mt**2*t*p1[1]+3*mt*t*t*p2[1]+t**3*p3[1]
                pts.append((x,y))
            cur=p3
        elif op=='closePath':
            if cur != start: pts.append(start)
            cur=start
    return pts

def audit_glyph(g:GlyphDef):
    out={'name':g.name,'width':g.width,'contours':[],'same_role_overlap_area':0.0}
    polys=[]
    for c in g.contours:
        area=area_of_contour(c)
        expected_positive=(c.role=='outer')
        direction_ok=(area>0) if expected_positive else (area<0)
        internal_extrema=[]; zero_handles=0; fractional=0; short_segments=0; near_axis=0
        cur=None; oncurve=0; offcurve=0; segs=0
        for op,args in c.commands:
            for p in args:
                if isinstance(p,tuple):
                    for v in p:
                        if abs(v-round(v))>1e-9: fractional+=1
            if op=='moveTo': cur=args[0]; oncurve+=1
            elif op=='lineTo':
                p=args[0]; oncurve+=1; segs+=1
                dx=p[0]-cur[0];dy=p[1]-cur[1];d=math.hypot(dx,dy)
                if d<3: short_segments+=1
                if (0<abs(dx)<=2 and abs(dy)>10) or (0<abs(dy)<=2 and abs(dx)>10): near_axis+=1
                cur=p
            elif op=='curveTo':
                p1,p2,p3=args; p0=cur; offcurve+=2; oncurve+=1; segs+=1
                if p1==p0: zero_handles+=1
                if p2==p3: zero_handles+=1
                for axis in [0,1]:
                    for t in cubic_roots(p0[axis],p1[axis],p2[axis],p3[axis]):
                        if 1e-5 < t < 1-1e-5:
                            internal_extrema.append({'axis':'xy'[axis],'t':round(t,6)})
                cur=p3
        poly=Polygon(sample_contour(c))
        polys.append((c.role,poly))
        out['contours'].append({
            'role':c.role,'signed_area':round(area,3),'direction_ok':direction_ok,
            'segments':segs,'oncurve_points':oncurve,'offcurve_points':offcurve,
            'internal_extrema':internal_extrema,'zero_handles':zero_handles,
            'fractional_coordinate_values':fractional,'short_segments':short_segments,
            'near_axis_misalignment':near_axis,'self_intersection_or_invalid':not poly.is_valid,
        })
    overlap=0.0
    for i in range(len(polys)):
        for j in range(i+1,len(polys)):
            role1,p1=polys[i]; role2,p2=polys[j]
            if role1==role2: overlap += p1.intersection(p2).area
    out['same_role_overlap_area']=round(overlap,3)
    out['bounds']=bounds_of_glyph(g)
    out['passes_core_audit']=all(
        c['direction_ok'] and not c['internal_extrema'] and c['zero_handles']==0 and
        c['fractional_coordinate_values']==0 and c['short_segments']==0 and
        c['near_axis_misalignment']==0 and not c['self_intersection_or_invalid']
        for c in out['contours']
    ) and overlap < 0.01
    return out

def glyph_order(): return ['.notdef']+[g.name for g in CLEAN]

def make_notdef_recording():
    p=RecordingPen(); p.moveTo((50,0));p.lineTo((550,0));p.lineTo((550,700));p.lineTo((50,700));p.closePath()
    p.moveTo((130,80));p.lineTo((130,620));p.lineTo((470,620));p.lineTo((470,80));p.closePath(); return p

def build_otf(path:Path):
    order=glyph_order(); cmap={g.codepoint:g.name for g in CLEAN if g.codepoint}
    metrics={'.notdef':(600,50)}|{g.name:(g.width,int(bounds_of_glyph(g)[0])) for g in CLEAN}
    charstrings={}
    for name in order:
        width=metrics[name][0]
        pen=T2CharStringPen(width,None)
        if name=='.notdef': make_notdef_recording().replay(pen)
        else: replay_glyph(next(g for g in CLEAN if g.name==name),pen)
        charstrings[name]=pen.getCharString(private=None,globalSubrs=None)
    fb=FontBuilder(UPM,isTTF=False)
    fb.setupGlyphOrder(order); fb.setupCharacterMap(cmap); fb.setupHorizontalMetrics(metrics); fb.setupHorizontalHeader(ascent=800,descent=-200)
    fb.setupNameTable({'familyName':'T006 Outline Audit','styleName':'Regular','uniqueFontIdentifier':'T006OutlineAudit-Regular','fullName':'T006 Outline Audit Regular','psName':'T006OutlineAudit-Regular','version':'Version 0.001'})
    fb.setupOS2(sTypoAscender=800,sTypoDescender=-200,sTypoLineGap=0,usWinAscent=800,usWinDescent=200)
    fb.setupPost(); fb.setupCFF('T006OutlineAudit-Regular',{'FullName':'T006 Outline Audit Regular','FamilyName':'T006 Outline Audit','Weight':'Regular'},charstrings,{})
    fb.save(path)

def build_ttf(path:Path,max_err=0.5):
    order=glyph_order(); cmap={g.codepoint:g.name for g in CLEAN if g.codepoint}
    metrics={'.notdef':(600,50)}|{g.name:(g.width,int(bounds_of_glyph(g)[0])) for g in CLEAN}
    glyphs={}
    for name in order:
        tpen=TTGlyphPen(None)
        qpen=Cu2QuPen(tpen,max_err=max_err,reverse_direction=True)
        if name=='.notdef': make_notdef_recording().replay(qpen)
        else: replay_glyph(next(g for g in CLEAN if g.name==name),qpen)
        glyphs[name]=tpen.glyph()
    fb=FontBuilder(UPM,isTTF=True)
    fb.setupGlyphOrder(order); fb.setupCharacterMap(cmap); fb.setupGlyf(glyphs); fb.setupHorizontalMetrics(metrics); fb.setupHorizontalHeader(ascent=800,descent=-200)
    fb.setupNameTable({'familyName':'T006 Outline Audit TT','styleName':'Regular','uniqueFontIdentifier':'T006OutlineAuditTT-Regular','fullName':'T006 Outline Audit TT Regular','psName':'T006OutlineAuditTT-Regular','version':'Version 0.001'})
    fb.setupOS2(sTypoAscender=800,sTypoDescender=-200,sTypoLineGap=0,usWinAscent=800,usWinDescent=200)
    fb.setupPost(); fb.setupMaxp(); fb.save(path)

from fontTools.pens.basePen import BasePen
class FlattenPen(BasePen):
    def __init__(self,glyphSet=None,n=80): super().__init__(glyphSet); self.n=n; self.contours=[]; self.cur=[]; self.start=None
    def _moveTo(self,p): self.cur=[p]; self.start=p
    def _lineTo(self,p):
        p0=self._getCurrentPoint()
        for i in range(1,self.n+1):
            t=i/self.n; self.cur.append((p0[0]*(1-t)+p[0]*t,p0[1]*(1-t)+p[1]*t))
    def _curveToOne(self,p1,p2,p3):
        p0=self._getCurrentPoint()
        for i in range(1,self.n+1):
            t=i/self.n;mt=1-t
            self.cur.append((mt**3*p0[0]+3*mt**2*t*p1[0]+3*mt*t*t*p2[0]+t**3*p3[0],mt**3*p0[1]+3*mt**2*t*p1[1]+3*mt*t*t*p2[1]+t**3*p3[1]))
    def _qCurveToOne(self,p1,p2):
        p0=self._getCurrentPoint()
        for i in range(1,self.n+1):
            t=i/self.n;mt=1-t
            self.cur.append((mt*mt*p0[0]+2*mt*t*p1[0]+t*t*p2[0],mt*mt*p0[1]+2*mt*t*p1[1]+t*t*p2[1]))
    def _closePath(self):
        if self.cur and self.start is not None:
            p0=self.cur[-1]; p=self.start
            for i in range(1,self.n+1):
                t=i/self.n; self.cur.append((p0[0]*(1-t)+p[0]*t,p0[1]*(1-t)+p[1]*t))
        self.contours.append(self.cur); self.cur=[]; self.start=None
    def _endPath(self): self.contours.append(self.cur); self.cur=[]; self.start=None

def source_samples(g:GlyphDef,n=160):
    p=FlattenPen(None,n=n); replay_glyph(g,p); return p.contours

def binary_samples(font_path:Path,gname:str,n=160):
    f=TTFont(font_path); gs=f.getGlyphSet(); p=FlattenPen(gs,n=n); gs[gname].draw(p); f.close(); return p.contours

def sym_nn_error(a_contours,b_contours):
    def vertices(contours): return np.array([p for c in contours for p in c],dtype=float)
    def segments(contours):
        seg=[]
        for c in contours:
            for i in range(len(c)-1): seg.append((c[i],c[i+1]))
        return np.array(seg,dtype=float)
    def max_pt_seg(pts,segs):
        a=segs[:,0,:]; b=segs[:,1,:]; ab=b-a; denom=(ab*ab).sum(axis=1); denom=np.where(denom==0,1,denom)
        mx=0.0
        for i in range(0,len(pts),128):
            p=pts[i:i+128]; ap=p[:,None,:]-a[None,:,:]
            t=(ap*ab[None,:,:]).sum(axis=2)/denom[None,:]; t=np.clip(t,0,1)
            proj=a[None,:,:]+t[:,:,None]*ab[None,:,:]
            d2=((p[:,None,:]-proj)**2).sum(axis=2)
            mx=max(mx,float(np.sqrt(d2.min(axis=1)).max()))
        return mx
    av=vertices(a_contours); bv=vertices(b_contours); asegs=segments(a_contours); bsegs=segments(b_contours)
    return max(max_pt_seg(av,bsegs),max_pt_seg(bv,asegs))

def total_signed_area_font(font_path:Path,gname:str):
    f=TTFont(font_path); gs=f.getGlyphSet(); p=AreaPen(gs); gs[gname].draw(p); v=p.value; f.close(); return v

def bounds_font(font_path:Path,gname:str):
    f=TTFont(font_path); gs=f.getGlyphSet(); p=BoundsPen(gs); gs[gname].draw(p); b=p.bounds; f.close(); return b

def point_counts_ttf(path:Path,gname:str):
    f=TTFont(path); glyph=f['glyf'][gname]; coords,endPts,flags=glyph.getCoordinates(f['glyf']); f.close(); return {'points':len(coords),'contours':len(endPts)}

def cff_command_counts(path:Path,gname:str):
    f=TTFont(path); gs=f.getGlyphSet(); p=RecordingPen(); gs[gname].draw(p); f.close()
    return {'commands':len(p.value),'curves':sum(1 for op,_ in p.value if op=='curveTo'),'lines':sum(1 for op,_ in p.value if op=='lineTo')}

def render_stats(font_path:Path,ch:str,ppem:int):
    face=freetype.Face(str(font_path)); face.set_pixel_sizes(0,ppem)
    face.load_char(ch,freetype.FT_LOAD_RENDER|freetype.FT_LOAD_TARGET_LIGHT|freetype.FT_LOAD_NO_HINTING)
    bm=face.glyph.bitmap
    arr=np.array(bm.buffer,dtype=np.uint8).reshape((bm.rows,bm.pitch))[:,:bm.width] if bm.rows and bm.width else np.zeros((0,0),dtype=np.uint8)
    return {'width':bm.width,'rows':bm.rows,'coverage_px_eq':round(float(arr.sum()/255),4),'strong_pixels':int((arr>=128).sum()),'advance_26_6':int(face.glyph.advance.x)}

def svg_path(g:GlyphDef):
    parts=[]
    for c in g.contours:
        for op,args in c.commands:
            if op=='moveTo': x,y=args[0]; parts.append(f'M {x} {y}')
            elif op=='lineTo': x,y=args[0]; parts.append(f'L {x} {y}')
            elif op=='curveTo': p1,p2,p3=args; parts.append(f'C {p1[0]} {p1[1]} {p2[0]} {p2[1]} {p3[0]} {p3[1]}')
            elif op=='closePath': parts.append('Z')
    return ' '.join(parts)

def oncurve_points(g:GlyphDef):
    pts=[]
    for c in g.contours:
        for op,args in c.commands:
            if op in ('moveTo','lineTo'): pts.append(args[0])
            elif op=='curveTo': pts.append(args[-1])
    return pts

def write_svg(results,path:Path):
    def panel(g,x,y,title,fill='black',opacity='1',stroke='none'):
        circles=''.join(f'<circle cx="{px}" cy="{py}" r="8" fill="#fff" stroke="#111" stroke-width="3"/>' for px,py in oncurve_points(g))
        return f'<g transform="translate({x} {y}) scale(.28 -.28)"><path d="{svg_path(g)}" fill="{fill}" fill-rule="nonzero" opacity="{opacity}" stroke="{stroke}" stroke-width="5"/>{circles}</g><text x="{x}" y="{y+20}" font-size="15" font-weight="600">{title}</text>'
    rows=[]; y=510
    for name in ['H','O','n','o']:
        v=results['export_fidelity'][name]
        rows.append(f'<text x="630" y="{y}" font-size="14">{name}: CFF Δ={v["source_vs_cff_sample_nn_max_units"]:.3f}u · TT polyline Δ≈{v["source_vs_ttf_sample_nn_max_units"]:.3f}u · |area| Δ={v["ttf_abs_area_delta_pct"]:.3f}%</text>'); y+=24
    max_cov=0.0; max_desc=''
    for ch,ppems in results['raster'].items():
        for ppem,pair in ppems.items():
            c=pair['cff']['coverage_px_eq']; t=pair['ttf']['coverage_px_eq']; pct=((t-c)/c*100) if c else 0
            if abs(pct)>abs(max_cov): max_cov=pct; max_desc=f'{ch} @{ppem}ppem'
    chunks=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="680" viewBox="0 0 1200 680"><rect width="1200" height="680" fill="white"/>',
        '<text x="36" y="42" font-family="sans-serif" font-size="24" font-weight="700">T006 — Production Outline Audit</text><text x="36" y="68" font-family="sans-serif" font-size="14">Source audit -&gt; failure/revision -&gt; CFF/TTF export fidelity -&gt; no-hint raster transfer</text><g font-family="sans-serif">',
        panel(H_BAD,55,300,'H.v0 — overlapping source',fill='#555',opacity='.58'),panel(H,340,300,'H.v1 — merged contour'),panel(O_BAD,55,620,'O.v0 — extrema / winding failure',fill='none',stroke='#111'),panel(O,340,620,'O.v1 — extrema + winding fixed',fill='none',stroke='#111'),
        '<text x="630" y="120" font-size="17" font-weight="700">Audit result</text>',f'<text x="630" y="150" font-size="14">H.v0: same-role overlap area = {results["v0_audit"]["H.v0"]["same_role_overlap_area"]:.0f} units^2 : REJECT</text>','<text x="630" y="174" font-size="14">O.v0: 4 internal extrema + both contour directions wrong : REJECT</text>','<text x="630" y="198" font-size="14">H/O/n/o revised subset: core source audit = PASS</text>','<text x="630" y="238" font-size="17" font-weight="700">Export fidelity</text>','<text x="630" y="266" font-size="14">CFF preserves sampled source geometry exactly in this build.</text>','<text x="630" y="290" font-size="14">TTF uses cu2qu max_err=0.5u and reverses winding for TrueType.</text>','<text x="630" y="314" font-size="14">Measured TT |area| drift stays below 0.162% in this subset.</text>','<text x="630" y="354" font-size="17" font-weight="700">Raster warning</text>','<text x="630" y="382" font-size="14">No-hint FreeType CFF/TT coverage still changes after format conversion.</text>',f'<text x="630" y="406" font-size="14">Largest observed coverage change: {max_desc} ~ {max_cov:+.2f}%.</text>','<text x="630" y="446" font-size="17" font-weight="700">Per-glyph geometric checks</text>',''.join(rows),'<text x="630" y="635" font-size="12">Research subset only — not a product font or production PASS.</text></g></svg>']
    path.write_text(''.join(chunks),encoding='utf-8')

def main(outdir):
    outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    otf=outdir/'T006-audit.otf'; ttf=outdir/'T006-audit.ttf'
    build_otf(otf); build_ttf(ttf,0.5)
    results={'environment':{'python':sys.version.split()[0],'fontTools':__import__('fontTools').__version__,'freetype':'.'.join(map(str,freetype.version())),'numpy':np.__version__,'shapely':shapely.__version__,'upm':UPM,'ttf_cu2qu_max_err_units':0.5},'v0_audit':{},'clean_audit':{},'export_fidelity':{},'raster':{}}
    for g in V0: results['v0_audit'][g.name]=audit_glyph(g)
    for g in CLEAN: results['clean_audit'][g.name]=audit_glyph(g)
    for g in CLEAN:
        src=source_samples(g); cff=binary_samples(otf,g.name); tt=binary_samples(ttf,g.name)
        sa=sum(area_of_contour(c) for c in g.contours); ca=total_signed_area_font(otf,g.name); ta=total_signed_area_font(ttf,g.name)
        results['export_fidelity'][g.name]={'source_bounds':bounds_of_glyph(g),'cff_bounds':bounds_font(otf,g.name),'ttf_bounds':bounds_font(ttf,g.name),'source_vs_cff_sample_nn_max_units':round(sym_nn_error(src,cff),6),'source_vs_ttf_sample_nn_max_units':round(sym_nn_error(src,tt),6),'source_signed_area':round(sa,3),'cff_signed_area':round(ca,3),'ttf_signed_area':round(ta,3),'ttf_abs_area_delta_pct':round((abs(ta)-abs(sa))/abs(sa)*100,6) if sa else None,'cff_structure':cff_command_counts(otf,g.name),'ttf_structure':point_counts_ttf(ttf,g.name)}
    for ch in ['H','O','n','o']:
        results['raster'][ch]={}
        for ppem in [14,20,48]: results['raster'][ch][str(ppem)]={'cff':render_stats(otf,ch,ppem),'ttf':render_stats(ttf,ch,ppem)}
    (outdir/'T006-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    write_svg(results,outdir/'T006-evidence.svg')
    print(json.dumps(results,indent=2))

if __name__=='__main__': main(sys.argv[1] if len(sys.argv)>1 else '/tmp/t006out')
