from pathlib import Path
import tempfile, json, hashlib, shutil, unicodedata
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
from fontTools import subset
import fontTools

UPM=1000
RESULTS=Path('T014-hangul-normalization-subset-contract-results.json')
SYLLABLES=['가','각']

def rect(x0,y0,x1,y1):
    p=TTGlyphPen(None); p.moveTo((x0,y0)); p.lineTo((x1,y0)); p.lineTo((x1,y1)); p.lineTo((x0,y1)); p.closePath(); return p.glyph()

def cpseq(s): return [f'U+{ord(c):04X}' for c in s]

def build(path):
    order=['.notdef','ga','gak','L_kiyeok','V_a','T_kiyeok']
    glyphs={
      '.notdef':rect(50,0,450,700), 'ga':rect(60,0,940,880), 'gak':rect(60,0,940,880),
      'L_kiyeok':rect(60,100,430,850), 'V_a':rect(430,100,780,850), 'T_kiyeok':rect(200,0,800,180)
    }
    metrics={'.notdef':(1000,50),'ga':(1000,60),'gak':(1000,60),'L_kiyeok':(1000,60),'V_a':(1000,430),'T_kiyeok':(1000,200)}
    fb=FontBuilder(UPM,isTTF=True); fb.setupGlyphOrder(order)
    fb.setupCharacterMap({0xAC00:'ga',0xAC01:'gak',0x1100:'L_kiyeok',0x1161:'V_a',0x11A8:'T_kiyeok'})
    fb.setupGlyf(glyphs); fb.setupHorizontalMetrics(metrics); fb.setupHorizontalHeader(ascent=900,descent=-250)
    fb.setupOS2(sTypoAscender=850,sTypoDescender=-200,usWinAscent=950,usWinDescent=250,usWeightClass=400)
    fb.setupNameTable({'familyName':'T014 Hangul Research','styleName':'Regular','uniqueFontIdentifier':'T014HangulResearch-Regular','fullName':'T014 Hangul Research Regular','psName':'T014HangulResearch-Regular'})
    fb.setupPost(); fb.setupMaxp(); fb.save(path)
    f=TTFont(path); f['head'].flags |= 2; f['head'].created=2082844800; f['head'].modified=2082844800; f.recalcTimestamp=False; f.save(path)

def subset_font(src,dst,text):
    opts=subset.Options(); opts.name_IDs=['*']; opts.name_legacy=True; opts.name_languages=['*']; opts.recalc_timestamp=False
    s=subset.Subsetter(options=opts); s.populate(text=text); f=TTFont(src); s.subset(f); f.recalcTimestamp=False; f.save(dst)

def woff2(src,dst):
    f=TTFont(src); f.flavor='woff2'; f.recalcTimestamp=False; f.save(dst)

def audit(path):
    f=TTFont(path); cmap=f.getBestCmap(); contracts={}
    for syl in SYLLABLES:
      nfc=unicodedata.normalize('NFC',syl); nfd=unicodedata.normalize('NFD',syl)
      contracts[syl]={
        'nfc_sequence':cpseq(nfc),'nfd_sequence':cpseq(nfd),
        'nfc_coverage':all(ord(c) in cmap for c in nfc),
        'nfd_coverage':all(ord(c) in cmap for c in nfd),
        'nfc_glyphs':[cmap.get(ord(c)) for c in nfc],
        'nfd_glyphs':[cmap.get(ord(c)) for c in nfd],
      }
    return {'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'size':path.stat().st_size,'glyphs':f.getGlyphOrder(),'cmap':{f'U+{cp:04X}':g for cp,g in sorted(cmap.items())},'contracts':contracts}

def main():
    tools={n:shutil.which(n) for n in ['fontbakery','fontspector','ots-sanitize','hb-shape']}
    normalized={}
    for syl in SYLLABLES:
      normalized[syl]={'NFC':cpseq(unicodedata.normalize('NFC',syl)),'NFD':cpseq(unicodedata.normalize('NFD',syl)), 'canonically_equivalent':unicodedata.normalize('NFC',unicodedata.normalize('NFD',syl))==syl}
    with tempfile.TemporaryDirectory(prefix='t014_') as td:
      d=Path(td); source=d/'source.ttf'; build(source)
      nfc_text=''.join(unicodedata.normalize('NFC',s) for s in SYLLABLES)
      nfd_text=''.join(unicodedata.normalize('NFD',s) for s in SYLLABLES)
      modes={'nfc_only':nfc_text,'nfd_only':nfd_text,'dual':nfc_text+nfd_text}
      arts={}
      for name,text in modes.items():
        ttf=d/f'{name}.ttf'; subset_font(source,ttf,text); wf=d/f'{name}.woff2'; woff2(ttf,wf); arts[name]=audit(wf)
      d2=d/'repeat'; d2.mkdir(); source2=d2/'source.ttf'; build(source2)
      repeat={}
      for name,text in modes.items():
        ttf2=d2/f'{name}.ttf'; subset_font(source2,ttf2,text); wf2=d2/f'{name}.woff2'; woff2(ttf2,wf2); repeat[name]=audit(wf2)
      reproducibility={name: arts[name]['sha256']==repeat[name]['sha256'] for name in modes}
      def all_form(a,key): return all(v[key] for v in a['contracts'].values())
      derived={
        'nfc_only_passes_nfc_fails_nfd':all_form(arts['nfc_only'],'nfc_coverage') and not all_form(arts['nfc_only'],'nfd_coverage'),
        'nfd_only_passes_nfd_fails_nfc':all_form(arts['nfd_only'],'nfd_coverage') and not all_form(arts['nfd_only'],'nfc_coverage'),
        'dual_passes_both':all_form(arts['dual'],'nfc_coverage') and all_form(arts['dual'],'nfd_coverage'),
        'nfc_only_jamo_missing':[cp for cp in ['U+1100','U+1161','U+11A8'] if cp not in arts['nfc_only']['cmap']],
        'nfd_only_syllables_missing':[cp for cp in ['U+AC00','U+AC01'] if cp not in arts['nfd_only']['cmap']],
        'all_packages_parseable':all(a['size']>0 for a in arts.values()),
        'all_rebuild_hashes_identical':all(reproducibility.values())
      }
      results={'environment':{'python_unicodedata_version':unicodedata.unidata_version,'fonttools':fontTools.__version__,'external_tools':tools},'normalization':normalized,'artifacts':arts,'reproducibility':reproducibility,'derived':derived,'scope_limits':['Structural cmap/subset proof only; no HarfBuzz/browser shaping available.','Synthetic glyph geometry; no claim about production Hangul design quality or actual Jamo composition behavior.','Supporting both NFC and NFD is product-contract dependent; a product that guarantees normalization before shaping may intentionally ship narrower closure.','No FontBakery/Fontspector/OTS sanitizer PASS claimed.']}
      RESULTS.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
