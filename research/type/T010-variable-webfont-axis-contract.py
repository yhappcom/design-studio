"""T010 variable-font packaging/subsetting axis-semantics contract.

Research-only. Builds a two-master TrueType variable font with wght, named
instances, STAT and a deliberately non-linear avar mapping; packages to WOFF2,
subsets to H, and creates an adversarial package with avar removed.

Generated binaries are temporary outputs, not product assets.
Dependencies: fontTools with WOFF2/Brotli support.
"""
from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

import fontTools
from fontTools import subset
from fontTools.designspaceLib import AxisDescriptor, DesignSpaceDocument, SourceDescriptor
from fontTools.fontBuilder import FontBuilder
from fontTools.otlLib.builder import buildStatTable
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables._f_v_a_r import NamedInstance
from fontTools.varLib import build as varlib_build
from fontTools.varLib.instancer import instantiateVariableFont

UPM = 1000
RESULTS = Path("T010-variable-webfont-axis-contract-results.json")


def rect(x0, y0, x1, y1):
    pen = TTGlyphPen(None)
    pen.moveTo((x0, y0)); pen.lineTo((x1, y0)); pen.lineTo((x1, y1)); pen.lineTo((x0, y1)); pen.closePath()
    return pen.glyph()


def empty_glyph():
    return TTGlyphPen(None).glyph()


def h_glyph(stem):
    pen = TTGlyphPen(None)
    x0, x1, lo, hi = 50, 550, 315, 385
    a, b = x0 + stem, x1 - stem
    points = [(x0,0),(a,0),(a,lo),(b,lo),(b,0),(x1,0),(x1,700),(b,700),(b,hi),(a,hi),(a,700),(x0,700)]
    pen.moveTo(points[0])
    for point in points[1:]: pen.lineTo(point)
    pen.closePath()
    return pen.glyph()


def o_glyph(inset):
    pen = TTGlyphPen(None)
    pen.moveTo((50,0)); pen.lineTo((550,0)); pen.lineTo((550,700)); pen.lineTo((50,700)); pen.closePath()
    # reverse inner contour direction
    pen.moveTo((50+inset,inset)); pen.lineTo((50+inset,700-inset)); pen.lineTo((550-inset,700-inset)); pen.lineTo((550-inset,inset)); pen.closePath()
    return pen.glyph()


def build_master(path: Path, weight: int):
    stem = 70 if weight == 300 else 130
    inset = 60 if weight == 300 else 120
    h_adv = 620 if weight == 300 else 680
    o_adv = 620 if weight == 300 else 660
    glyphs = {'.notdef': rect(50,0,450,700), 'space': empty_glyph(), 'H': h_glyph(stem), 'O': o_glyph(inset)}
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(['.notdef','space','H','O'])
    fb.setupCharacterMap({0x20:'space',0x48:'H',0x4F:'O'})
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics({'.notdef':(500,50),'space':(300,0),'H':(h_adv,50),'O':(o_adv,50)})
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupOS2(sTypoAscender=800,sTypoDescender=-200,sTypoLineGap=0,usWinAscent=900,usWinDescent=200,usWeightClass=weight)
    fb.setupNameTable({'familyName':'T010 Research','styleName':f'W{weight}','uniqueFontIdentifier':f'T010-{weight}','fullName':f'T010 Research {weight}','psName':f'T010Research-{weight}'})
    fb.setupPost(); fb.setupMaxp(); fb.save(path)


def build_vf(work: Path) -> Path:
    light, bold = work/'master-300.ttf', work/'master-700.ttf'
    build_master(light,300); build_master(bold,700)
    ds = DesignSpaceDocument()
    axis = AxisDescriptor(); axis.name='Weight'; axis.tag='wght'; axis.minimum=300; axis.default=300; axis.maximum=700; ds.addAxis(axis)
    for path, weight, name in ((light,300,'light'),(bold,700,'bold')):
        src = SourceDescriptor(); src.path=str(path); src.name=name; src.familyName='T010 Research'; src.styleName=f'W{weight}'; src.location={'Weight':weight}; ds.addSource(src)
    dspath = work/'T010.designspace'; ds.write(dspath)
    vf, _, _ = varlib_build(str(dspath))
    for weight, name in ((300,'Light'),(500,'Medium'),(700,'Bold')):
        inst = NamedInstance(); inst.subfamilyNameID=vf['name'].addName(name); inst.coordinates={'wght':weight}; inst.postscriptNameID=0xFFFF; vf['fvar'].instances.append(inst)
    buildStatTable(vf,[dict(tag='wght',name='Weight',values=[dict(value=300,name='Light'),dict(value=500,name='Medium'),dict(value=700,name='Bold')])])
    avar = newTable('avar'); avar.majorVersion=1; avar.minorVersion=0
    # Non-linear positive half: normalized +0.5 maps to +0.35.
    avar.segments={'wght':{-1.0:-1.0,0.0:0.0,0.5:0.35,1.0:1.0}}; vf['avar']=avar
    out=work/'T010-VF.ttf'; vf.save(out); return out


def package_woff2(src: Path, dst: Path):
    font=TTFont(src); font.flavor='woff2'; font.save(dst)


def subset_to_h(src: Path, dst: Path):
    font=TTFont(src)
    options=subset.Options(); options.name_IDs=['*']; options.name_legacy=True; options.name_languages=['*']
    sub=subset.Subsetter(options=options); sub.populate(unicodes=[0x48]); sub.subset(font); font.save(dst)


def mutate_drop_avar(src: Path, dst: Path):
    font=TTFont(src)
    if 'avar' in font: del font['avar']
    font.save(dst)


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def axis_summary(font: TTFont):
    a=font['fvar'].axes[0]
    return {'tag':a.axisTag,'min':a.minValue,'default':a.defaultValue,'max':a.maxValue}


def named_instances(font: TTFont):
    return [dict(i.coordinates) for i in font['fvar'].instances]


def avar_summary(font: TTFont):
    if 'avar' not in font: return None
    return {tag:{str(k):v for k,v in seg.items()} for tag,seg in font['avar'].segments.items()}


def instance_advances(path: Path):
    out={}
    for weight in (300,500,700):
        font=TTFont(path)
        inst=instantiateVariableFont(font, {'wght':weight}, inplace=False)
        out[str(weight)]={g:inst['hmtx'][g][0] for g in ('H',) if g in inst.getGlyphOrder()}
    return out


def inspect(path: Path):
    font=TTFont(path)
    required=['fvar','gvar','STAT','avar']
    return {
        'file':path.name,'bytes':path.stat().st_size,'sha256':sha256(path),'flavor':font.flavor,
        'tables':sorted(font.keys()),'required_variation_tables':{t:(t in font) for t in required},
        'axis':axis_summary(font),'named_instances':named_instances(font),'avar':avar_summary(font),
        'glyph_order':font.getGlyphOrder(),'gvar_glyphs':sorted(font['gvar'].variations.keys()),
        'instance_advances':instance_advances(path),
    }


def contract(result):
    tabs=result['required_variation_tables']
    axis=result['axis']; instances=result['named_instances']; avar=result['avar']
    return {
        'required_tables':all(tabs.values()),
        'axis_range':axis=={'tag':'wght','min':300.0,'default':300.0,'max':700.0},
        'named_instances':instances==[{'wght':300.0},{'wght':500.0},{'wght':700.0}],
        'nonlinear_avar':avar is not None and abs(avar['wght']['0.5']-0.3499755859375)<1e-9,
        'mid_H_advance':result['instance_advances']['500'].get('H'),
    }


def main():
    with tempfile.TemporaryDirectory(prefix='t010_') as td:
        work=Path(td)
        source=build_vf(work)
        source_w2=work/'T010-VF.woff2'; package_woff2(source,source_w2)
        subset_ttf=work/'T010-H-subset.ttf'; subset_to_h(source,subset_ttf)
        subset_w2=work/'T010-H-subset.woff2'; package_woff2(subset_ttf,subset_w2)
        bad_ttf=work/'T010-H-subset-no-avar.ttf'; mutate_drop_avar(subset_ttf,bad_ttf)
        bad_w2=work/'T010-H-subset-no-avar.woff2'; package_woff2(bad_ttf,bad_w2)
        paths=[source,source_w2,subset_ttf,subset_w2,bad_w2]
        artifacts={p.name:inspect(p) for p in paths}
        checks={name:contract(data) for name,data in artifacts.items()}
        good=checks[subset_w2.name]; bad=checks[bad_w2.name]
        results={
            'environment':{'fonttools':fontTools.__version__},
            'experiment':{'axis':'wght 300/300/700','named_instances':[300,500,700],'avar_contract':{'normalized_0.5':0.35},'subset_unicode':['U+0048 H']},
            'artifacts':artifacts,'checks':checks,
            'key_comparison':{
                'good_subset_woff2_mid_H_advance':good['mid_H_advance'],
                'no_avar_subset_woff2_mid_H_advance':bad['mid_H_advance'],
                'advance_delta_units':bad['mid_H_advance']-good['mid_H_advance'],
                'good_contract_pass':all(v for k,v in good.items() if k!='mid_H_advance'),
                'bad_contract_pass':all(v for k,v in bad.items() if k!='mid_H_advance'),
                'bad_font_parseable':True,
            },
            'tool_availability':{'fontbakery':False,'fontspector':False,'ots_sanitize':False,'network_install_attempt':'failed: name resolution unavailable'},
        }
        RESULTS.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        print(json.dumps(results['key_comparison'],indent=2))
        print('subset tables',artifacts[subset_w2.name]['tables'])
        print('bad tables',artifacts[bad_w2.name]['tables'])
        print('results',RESULTS.resolve())

if __name__=='__main__': main()
