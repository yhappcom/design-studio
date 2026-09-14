from __future__ import annotations
import base64, hashlib, io, json, math, subprocess
from pathlib import Path

import freetype
import numpy as np
from PIL import Image
from fontTools.ttLib import TTFont, TTCollection
from fontTools.pens.boundsPen import BoundsPen

OUT=Path('.')
JSON_PATH=OUT/'T005-mixed-script-results.json'
SVG_PATH=OUT/'T005-mixed-script-evidence.svg'

FONT_REQUESTS={
 'Inter':'Inter:style=Regular',
 'Roboto':'Roboto:style=Regular',
 'NotoSans':'Noto Sans:style=Regular',
 'NotoSansCJK_KR':'Noto Sans CJK KR:style=Regular',
 'NanumGothic':'NanumGothic:style=Regular',
 'NanumBarunGothic':'NanumBarunGothic:style=Regular',
}
PAIRS=[
 ('Inter','NotoSansCJK_KR'),
 ('Inter','NanumGothic'),
 ('Inter','NanumBarunGothic'),
 ('NotoSans','NotoSansCJK_KR'),
 ('Roboto','NotoSansCJK_KR'),
]
STRINGS=[
 'Flight 7C1234A · 비행 737-8 · RKPC→RKSI',
 '총 비행시간 6,842+35 / Block 123:45',
 '비행기록 상세 / Flight record detail',
 '국제 분산 커버드콜 수익전략 포트폴리오 / $11,242 +1.8%',
]

def fc_match(pattern:str)->str:
    return subprocess.check_output(['fc-match','-f','%{file}',pattern], text=True).strip()

def family_name(font):
    n=font['name'].getName(1,3,1) or font['name'].getName(1,1,0)
    return str(n) if n else ''

def name_string(font, name_id):
    n=font['name'].getName(name_id,3,1) or font['name'].getName(name_id,1,0)
    return str(n) if n else ''

def resolve(label,pattern):
    path=fc_match(pattern)
    idx=0
    if path.lower().endswith('.ttc'):
        col=TTCollection(path)
        target=pattern.split(':',1)[0].lower()
        hits=[]
        for i,f in enumerate(col.fonts):
            fam=family_name(f)
            if target in fam.lower(): hits.append((i,fam))
        if not hits: raise RuntimeError((label,path,target,[family_name(f) for f in col.fonts]))
        exact=[h for h in hits if h[1].lower()==target]
        idx=(exact or hits)[0][0]
    return path,idx

def load_tt(path,idx):
    return TTCollection(path).fonts[idx] if path.lower().endswith('.ttc') else TTFont(path)

def glyph_bbox(tt,ch):
    name=tt.getBestCmap().get(ord(ch))
    if not name:return None
    gs=tt.getGlyphSet(); pen=BoundsPen(gs); gs[name].draw(pen)
    return pen.bounds

def ft_face(path,idx): return freetype.Face(path,idx)

def render_char(path,idx,ch,ppem,flags=None):
    face=ft_face(path,idx); face.set_pixel_sizes(0,ppem)
    if flags is None: flags=freetype.FT_LOAD_RENDER|freetype.FT_LOAD_TARGET_LIGHT
    face.load_char(ch,flags); s=face.glyph; b=s.bitmap
    if b.rows and b.width:
        arr=np.array(b.buffer,dtype=np.uint8).reshape((b.rows,b.pitch))[:,:b.width]
    else: arr=np.zeros((0,0),dtype=np.uint8)
    return arr, {'advance':s.advance.x/64.0,'linear':s.linearHoriAdvance/65536.0,
                 'left':s.bitmap_left,'top':s.bitmap_top,'rows':b.rows,'width':b.width,
                 'coverage':round(float(arr.sum()/255),3) if arr.size else 0.0,
                 'strong':int((arr>=128).sum()) if arr.size else 0}

def is_hangul(ch):
    return 0xAC00<=ord(ch)<=0xD7A3 or 0x1100<=ord(ch)<=0x11FF or 0x3130<=ord(ch)<=0x318F

def supports(tt,ch): return ord(ch) in tt.getBestCmap()

def render_mixed(primary,fallback,text,ppem=20,pad=12):
    primary_path,primary_idx,primary_tt=primary
    fallback_path,fallback_idx,fallback_tt=fallback
    glyphs=[]; x=0.0; top=0; bottom=0
    for ch in text:
        use=fallback if is_hangul(ch) else primary
        if not supports(use[2],ch):
            use=fallback if supports(fallback_tt,ch) else primary
        arr,m=render_char(use[0],use[1],ch,ppem)
        glyphs.append((x,arr,m))
        if arr.size:
            top=max(top,m['top']); bottom=max(bottom,m['rows']-m['top'])
        x += m['advance']
    width=int(math.ceil(x))+2*pad; height=max(52,top+bottom+2*pad)
    baseline=pad+top
    img=Image.new('L',(width,height),255)
    for gx,arr,m in glyphs:
        if not arr.size: continue
        tile=Image.fromarray(255-arr,'L')
        img.paste(tile,(int(round(pad+gx+m['left'])), int(round(baseline-m['top']))),tile.point(lambda p:255-p))
    return img, {'advance':round(x,3),'ink_top':top,'ink_bottom':bottom,'ink_height':top+bottom,'height':height,'baseline':baseline}

def png_data_uri(img):
    buf=io.BytesIO(); img.save(buf,format='PNG')
    return 'data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()

resolved={}
for label,pattern in FONT_REQUESTS.items():
    path,idx=resolve(label,pattern); tt=load_tt(path,idx); o=tt['OS/2']; h=tt['hhea']; upm=tt['head'].unitsPerEm
    rec={'pattern':pattern,'path':path,'face_index':idx,'family':family_name(tt),
         'full_name':name_string(tt,4),'version':name_string(tt,5),
         'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'upm':upm,
         'metrics':{'sTypoAscender':o.sTypoAscender,'sTypoDescender':o.sTypoDescender,'sTypoLineGap':o.sTypoLineGap,
                    'hheaAscender':h.ascent,'hheaDescender':h.descent,'hheaLineGap':h.lineGap,
                    'usWinAscent':o.usWinAscent,'usWinDescent':o.usWinDescent,
                    'sxHeight':getattr(o,'sxHeight',None),'sCapHeight':getattr(o,'sCapHeight',None),
                    'useTypoMetrics':bool(o.fsSelection&(1<<7))},
         'glyphs':{}}
    for ch in ['H','x','0','O','가','한','글','비','행']:
        bb=glyph_bbox(tt,ch)
        if bb:
            arr,rm=render_char(path,idx,ch,20)
            rec['glyphs'][ch]={'bbox':bb,'raster20':rm}
    resolved[label]={'path':path,'idx':idx,'tt':tt,'record':rec}

results={'study':'T005','method':'FreeType light-target per-character fallback; no shaping engine',
         'fonts':{k:v['record'] for k,v in resolved.items()},'pairs':{}}
images=[]
for p,f in PAIRS:
    P=resolved[p]; F=resolved[f]
    pm=P['record']['metrics']; fm=F['record']['metrics']; pup=P['record']['upm']; fup=F['record']['upm']
    pxh=(pm['sxHeight']/pup) if pm['sxHeight'] else None; fxh=(fm['sxHeight']/fup) if fm['sxHeight'] else None
    factor=(pxh/fxh) if pxh and fxh else None
    pairrec={'primary':p,'fallback':f,
             'xheight_ratio_primary':round(pxh,4) if pxh else None,
             'xheight_ratio_fallback':round(fxh,4) if fxh else None,
             'xheight_match_scale_for_fallback':round(factor,4) if factor else None,
             'primary_typo_span_em':round((pm['sTypoAscender']-pm['sTypoDescender']+pm['sTypoLineGap'])/pup,4),
             'fallback_typo_span_em':round((fm['sTypoAscender']-fm['sTypoDescender']+fm['sTypoLineGap'])/fup,4),
             'primary_hhea_span_em':round((pm['hheaAscender']-pm['hheaDescender']+pm['hheaLineGap'])/pup,4),
             'fallback_hhea_span_em':round((fm['hheaAscender']-fm['hheaDescender']+fm['hheaLineGap'])/fup,4),
             'strings':{}}
    for text in STRINGS:
        img,met=render_mixed((P['path'],P['idx'],P['tt']),(F['path'],F['idx'],F['tt']),text,20)
        pairrec['strings'][text]=met
        if text==STRINGS[0]: images.append((f'{p} + {f}',img,met))
    if factor:
        base=[]; adj=[]; adj_ppem=max(1,int(round(20*factor)))
        for ch in '가한글':
            _,m=render_char(F['path'],F['idx'],ch,20); base.append(m['rows'])
            _,m2=render_char(F['path'],F['idx'],ch,adj_ppem); adj.append(m2['rows'])
        pairrec['hangul_rows_20ppem']=base
        pairrec['xheight_adjusted_ppem_rounded']=adj_ppem
        pairrec['hangul_rows_adjusted']=adj
    results['pairs'][p+' + '+f]=pairrec

JSON_PATH.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')

w=1500; h=1220
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
'<rect width="100%" height="100%" fill="#f7f7f5"/>',
'<style>.t{font:700 31px Arial;fill:#111}.h{font:700 20px Arial;fill:#111}.p{font:400 15px Arial;fill:#333}.m{font:400 14px monospace;fill:#222}.s{font:400 13px Arial;fill:#555}.b{fill:#fff;stroke:#d7d7d3}</style>',
'<text x="50" y="52" class="t">T005 — Latin/Korean Script-Fallback Metric &amp; Raster Proof</text>',
'<text x="50" y="80" class="p">Actual installed open-source fonts; FreeType light-target per-character fallback. No browser/shaping PASS is implied.</text>',
'<text x="50" y="125" class="h">A. Metric spans and x-height matching factors</text>',
'<rect x="50" y="145" width="1400" height="250" class="b"/>',
'<text x="75" y="180" class="m">pair                         xh primary/fallback   xh scale   typo span P/F   hhea span P/F</text>']
y=215
for key,rec in results['pairs'].items():
    line=f"{key:<29} {rec['xheight_ratio_primary']:.4f}/{rec['xheight_ratio_fallback']:.4f}       {rec['xheight_match_scale_for_fallback']:.4f}     {rec['primary_typo_span_em']:.3f}/{rec['fallback_typo_span_em']:.3f}       {rec['primary_hhea_span_em']:.3f}/{rec['fallback_hhea_span_em']:.3f}"
    parts.append(f'<text x="75" y="{y}" class="m">{line}</text>'); y+=38
parts.append('<text x="75" y="378" class="s">Different vertical-metric tables can imply materially different spans; actual UA choice remains a browser/platform validation question.</text>')
parts += ['<text x="50" y="445" class="h">B. Mixed-script raster rows at nominal 20 ppem</text>', '<rect x="50" y="465" width="1400" height="420" class="b"/>']
y=500
for label,img,met in images:
    uri=png_data_uri(img); dw=min(img.width,1000); dh=img.height*dw/img.width
    parts.append(f'<text x="75" y="{y}" class="p">{label}</text>')
    parts.append(f'<image x="390" y="{y-25}" width="{dw}" height="{dh}" href="{uri}"/>')
    parts.append(f'<text x="75" y="{y+22}" class="s">advance {met["advance"]}px · ink top/bottom {met["ink_top"]}/{met["ink_bottom"]}px</text>')
    y += 72
parts += ['<text x="50" y="935" class="h">C. Why x-height normalization is not Hangul optical matching</text>', '<rect x="50" y="955" width="1400" height="170" class="b"/>']
y=992
for key in ['Inter + NotoSansCJK_KR','Inter + NanumGothic','NotoSans + NotoSansCJK_KR']:
    r=results['pairs'][key]
    parts.append(f'<text x="75" y="{y}" class="m">{key}: scale {r["xheight_match_scale_for_fallback"]:.4f}; Hangul rows {r["hangul_rows_20ppem"]} → {r["hangul_rows_adjusted"]} at rounded {r["xheight_adjusted_ppem_rounded"]} ppem</text>'); y+=35
parts.append('<text x="75" y="1100" class="s">CSS font-size-adjust is defined around font metrics such as x-height; matching Latin x-height can enlarge or shrink a Korean fallback without proving better Hangul balance.</text>')
parts += ['<text x="50" y="1170" class="p">Evidence level: PRACTICE + TRANSFER VALIDATION PREPARATION. Exact font file hashes and measurements are stored in the companion JSON.</text>', '</svg>']
SVG_PATH.write_text('\n'.join(parts),encoding='utf-8')

print('wrote',JSON_PATH,SVG_PATH)
