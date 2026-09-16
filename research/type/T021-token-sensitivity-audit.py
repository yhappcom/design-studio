"""T021 executable architecture-token sensitivity audit.

Perturb one architecture token at a time, rebuild the exact bounded family, and
compare glyph outline/metric fingerprints. The strict result is FULL only when
all required consumers change; PARTIAL and NONE remain gate failures.
"""
from pathlib import Path
import copy, hashlib, importlib.util, json
from fontTools.ttLib import TTFont
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('complete', HERE/'T021-family-architecture-reset-complete-harness.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
reset=m.reset
OUT=Path('/tmp/t021-token-sensitivity'); OUT.mkdir(exist_ok=True); reset.OUT=OUT
CONSUMERS={
 'stem':set('HIEFLTABDPRNUJK')|set('123457'), 'round_stem':set('Oo0BDPR8'),
 'cap_overshoot':set('OCGSU0'), 'x_overshoot':set('o'), 'aperture':set('CGS5'),
 'corner':set('CGS5EF'), 'join':set('BDPR8'), 'diag_comp':set('AVXKRN247'),
 'terminal':set('CGS5EF'), 'figure_width':set('0123456789'), 'zero':set('0')}
PERTURB={'stem':9,'round_stem':9,'cap_overshoot':7,'x_overshoot':7,'aperture':23,
 'corner':7,'join':7,'diag_comp':7,'terminal':'round','figure_width':31,'zero':'slash'}
def fingerprint(path):
 f=TTFont(path); out={}
 for g in f.getGlyphOrder():
  data=f['glyf'][g].compile(f['glyf']); aw,lsb=f['hmtx'][g]
  out[g]=hashlib.sha256(data+f'{aw},{lsb}'.encode()).hexdigest()
 return out
base_arch=copy.deepcopy(reset.ARCH['A']); reset.ARCH['A']=copy.deepcopy(base_arch)
base_path,_=reset.build('A'); base=fingerprint(base_path); results={}
for token,delta in PERTURB.items():
 trial=copy.deepcopy(base_arch)
 if isinstance(delta,int): trial[token]+=delta
 else: trial[token]=delta if trial[token]!=delta else ('plain' if delta=='slash' else 'square')
 reset.ARCH['A']=trial; p,_=reset.build('A'); fp=fingerprint(p)
 changed=sorted(g for g in base if g in fp and base[g]!=fp[g]); required=CONSUMERS[token]
 hit=set(changed)&required; missing=required-hit
 state='FULL' if hit==required else ('PARTIAL' if hit else 'NONE')
 results[token]={'baseline':base_arch[token],'trial':trial[token],'changed_glyphs':changed,
  'required_consumers':sorted(required),'required_consumers_changed':sorted(hit),
  'required_consumers_unchanged':sorted(missing),'state':state,'gate_pass':state=='FULL'}
reset.ARCH['A']=base_arch
summary={'revision':'T021-token-sensitivity-audit-2','method':'single-token perturbation + glyf/hmtx fingerprint; FULL requires every required consumer to change','kerning':False,'results':results,
 'full_tokens':sorted(k for k,v in results.items() if v['state']=='FULL'),
 'partial_tokens':sorted(k for k,v in results.items() if v['state']=='PARTIAL'),
 'none_tokens':sorted(k for k,v in results.items() if v['state']=='NONE'),
 'all_declared_tokens_full':all(v['gate_pass'] for v in results.values()),'drawing_claim':False,'human_claim':False}
(OUT/'T021-token-sensitivity-results.json').write_text(json.dumps(summary,indent=2),encoding='utf-8'); print(json.dumps(summary,indent=2))
