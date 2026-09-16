"""Semantic sensitivity audit for T021 normalized architecture.

Mandatory consumers must change under a single-token perturbation. Protected
consumers must not change. Conditional consumers are reported, not forced.
"""
from pathlib import Path
import copy, hashlib, importlib.util, json, shutil
from fontTools.ttLib import TTFont
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('n', HERE/'T021-normalized-architecture-harness.py')
n=importlib.util.module_from_spec(spec); spec.loader.exec_module(n)
OUT=Path('/tmp/t021-normalized-sensitivity'); OUT.mkdir(exist_ok=True)
CONTRACT={
 'stem': {'mandatory':set('HIEFLT'), 'conditional':set('ABDP RNUJK'.replace(' ',''))|set('1345'), 'protected':set()},
 'round_stem': {'mandatory':set('Oo0BDPR8'), 'conditional':set(), 'protected':set()},
 'cap_overshoot': {'mandatory':set('OCG0'), 'conditional':set('U'), 'protected':set('o')},
 'x_overshoot': {'mandatory':set('o'), 'conditional':set(), 'protected':set('O0')},
 'aperture': {'mandatory':set('CG'), 'conditional':set('S5'), 'protected':set('O0')},
 'diag_comp': {'mandatory':set('AVXKR247'), 'conditional':set('NM'), 'protected':set('O0')},
 'terminal_policy': {'mandatory':set('CGEF5S'), 'conditional':set(), 'protected':set('O0')},
 'bowl_join': {'mandatory':set('BDPR8'), 'conditional':set('69'), 'protected':set('O0')},
 'shoulder_tension': {'mandatory':set('n'), 'conditional':set('S'), 'protected':set('o')},
 'figure_width_mode': {'mandatory':set('0123456789'), 'conditional':set(), 'protected':set('O')},
 'zero_treatment': {'mandatory':set('0'), 'conditional':set(), 'protected':set('O')},
}
PERTURB={'stem':9,'round_stem':9,'cap_overshoot':7,'x_overshoot':7,'aperture':23,'diag_comp':7,'terminal_policy':'square','bowl_join':7,'shoulder_tension':0.09,'figure_width_mode':31,'zero_treatment':'slash'}
def fp(path):
 f=TTFont(path); out={}
 for g in f.getGlyphOrder():
  data=f['glyf'][g].compile(f['glyf']); aw,lsb=f['hmtx'][g]; out[g]=hashlib.sha256(data+f'{aw},{lsb}'.encode()).hexdigest()
 return out
def build_with(a, label):
 old=copy.deepcopy(n.ARCH['A']); n.ARCH['A']=a; d=OUT/label; d.mkdir(exist_ok=True); p,_=n.build('A',d); n.ARCH['A']=old; return p
base=copy.deepcopy(n.ARCH['A']); basefp=fp(build_with(base,'base')); results={}
for token,c in CONTRACT.items():
 trial=copy.deepcopy(base); delta=PERTURB[token]
 if isinstance(delta,(int,float)): trial[token]+=delta
 else: trial[token]=delta if trial[token]!=delta else ('soft' if delta=='square' else 'plain')
 changed={g for g,h in fp(build_with(trial,token)).items() if g in basefp and h!=basefp[g]}
 mandatory=c['mandatory']; protected=c['protected']; conditional=c['conditional']; mh=mandatory & changed; ph=protected & changed; ch=conditional & changed
 passed=(mh==mandatory and not ph)
 results[token]={'baseline':base[token],'trial':trial[token],'mandatory':sorted(mandatory),'mandatory_changed':sorted(mh),'mandatory_unchanged':sorted(mandatory-mh),'protected':sorted(protected),'protected_changed':sorted(ph),'conditional':sorted(conditional),'conditional_changed':sorted(ch),'all_changed':sorted(changed),'gate_pass':passed}
summary={'revision':'T021-normalized-semantic-sensitivity-1','method':'single-token perturbation; all mandatory change; protected remain invariant; conditional reported','results':results,'passed_tokens':sorted(k for k,v in results.items() if v['gate_pass']),'failed_tokens':sorted(k for k,v in results.items() if not v['gate_pass']),'semantic_full':all(v['gate_pass'] for v in results.values()),'drawing_claim':False,'human_claim':False}
(OUT/'T021-normalized-semantic-sensitivity-results.json').write_text(json.dumps(summary,indent=2),encoding='utf-8'); print(json.dumps(summary,indent=2))
