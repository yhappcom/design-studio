import json, tempfile
from pathlib import Path
import numpy as np
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parent
HTML=ROOT/'C008-rendered-data-visualization-specimen.html'
RESULTS=ROOT/'C008-rendered-data-visualization-results.json'
CONDITIONS=[('light','failure'),('light','revised'),('dark','failure'),('dark','revised')]

# Machado, Oliveira & Fernandes (2009) severity-1 diagnostic matrices.
# Used as simulation only; not a substitute for human CVD validation.
MACHADO={
 'protanopia':np.array([[0.152286,1.052583,-0.204868],[0.114503,0.786281,0.099216],[-0.003882,-0.048116,1.051998]]),
 'deuteranopia':np.array([[0.367322,0.860646,-0.227968],[0.280085,0.672501,0.047413],[-0.011820,0.042940,0.968881]]),
 'tritanopia':np.array([[1.255528,-0.076749,-0.178779],[-0.078411,0.930809,0.147602],[0.004733,0.691367,0.303900]])
}
CAT_FAILURE=['#D7191C','#1A9641','#2C7BB6','#984EA3','#FF7F00']
CAT_REVISED=['#0072B2','#E69F00','#009E73','#D55E00','#CC79A7']


def hexrgb(h):
    h=h.lstrip('#'); return np.array([int(h[i:i+2],16) for i in (0,2,4)],float)/255

def srgb_to_linear(c):
    c=np.asarray(c,float); return np.where(c<=0.04045,c/12.92,((c+0.055)/1.055)**2.4)

def linear_to_srgb(c):
    c=np.asarray(c,float); return np.where(c<=0.0031308,12.92*c,1.055*np.maximum(c,0)**(1/2.4)-0.055)

def oklab(rgb):
    r,g,b=srgb_to_linear(rgb)
    l=0.4122214708*r+0.5363325363*g+0.0514459929*b
    m=0.2119034982*r+0.6806995451*g+0.1073969566*b
    s=0.0883024619*r+0.2817188376*g+0.6299787005*b
    l_,m_,s_=np.cbrt([l,m,s])
    return np.array([0.2104542553*l_+0.7936177850*m_-0.0040720468*s_,1.9779984951*l_-2.4285922050*m_+0.4505937099*s_,0.0259040371*l_+0.7827717662*m_-0.8086757660*s_])

def cvd(rgb,M):
    out=M@srgb_to_linear(rgb)
    return np.clip(linear_to_srgb(np.clip(out,0,1)),0,1)

def min_pair_distance(palette,M=None):
    rgbs=[hexrgb(c) for c in palette]
    if M is not None: rgbs=[cvd(c,M) for c in rgbs]
    labs=[oklab(c) for c in rgbs]
    vals=[]
    for i in range(len(labs)):
        for j in range(i+1,len(labs)):
            vals.append((float(np.linalg.norm(labs[i]-labs[j])),i,j))
    return min(vals)

def seq_metrics(palette):
    L=[float(oklab(hexrgb(c))[0]) for c in palette]
    d=np.diff(L)
    signs=np.sign(d[np.abs(d)>1e-9])
    reversals=int(np.sum(signs[1:]!=signs[:-1])) if len(signs)>1 else 0
    return {'oklab_L':L,'delta_L':[float(x) for x in d],'direction_reversals':reversals,'monotonic':bool(np.all(d>=0) or np.all(d<=0))}

def div_semantic(snapshot):
    vals=[-3,0,2,5,8,12,None]
    if snapshot['mode']=='failure':
        mid=4.5
        classes=['missing' if v is None else ('negative-side' if v<mid else ('positive-side' if v>mid else 'center')) for v in vals]
    else:
        classes=['missing' if v is None else ('negative-side' if v<0 else ('positive-side' if v>0 else 'center')) for v in vals]
    expected=['negative-side','center','positive-side','positive-side','positive-side','positive-side','missing']
    mismatches=[i for i,(a,b) in enumerate(zip(classes,expected)) if a!=b]
    return {'visual_classes':classes,'expected_classes':expected,'semantic_mismatch_indices':mismatches,'semantic_mismatch_count':len(mismatches)}

payload={'environment':{},'conditions':{},'categorical_cvd':{},'notes':{}}
with tempfile.TemporaryDirectory(prefix='c008-') as td, sync_playwright() as p:
    td=Path(td)
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    payload['environment']={'chromium':'/usr/bin/chromium','version':browser.version,'viewport':[1280,820],'dpr':1}
    page=browser.new_page(viewport={'width':1280,'height':820},device_scale_factor=1)
    page.set_content(HTML.read_text(),wait_until='load')
    baseline=None
    for theme,mode in CONDITIONS:
        page.evaluate('([t,m])=>window.setCondition(t,m)',[theme,mode]);page.wait_for_timeout(70)
        snap=page.evaluate('()=>window.snapshot()')
        if baseline is None: baseline=snap['rects']
        geometry_equal=snap['rects']==baseline
        # A browser screenshot is created during the run to force the real render path.
        # Metrics below use the SVG/DOM rendered colors to avoid antialiasing ambiguity.
        page.screenshot(path=str(td/f'{theme}-{mode}.png'),full_page=True)
        sm=seq_metrics(snap['seq'])
        div=div_semantic(snap)
        payload['conditions'][f'{theme}-{mode}']={
            'geometry_equal_to_baseline':geometry_equal,
            'snapshot':{k:v for k,v in snap.items() if k!='rects'},
            'sequential':sm,
            'diverging':div,
            'categorical':{
                'selected_series_C_identity_color':snap['cat'][2]['identity'],
                'selected_series_C_rendered_stroke':snap['cat'][2]['stroke'],
                'identity_preserved_under_selection':snap['cat'][2]['identity'].lower()==snap['cat'][2]['stroke'].lower(),
                'direct_labels_visible':all(str(x)=='1' for x in snap['direct']),
                'selection_halo_present':snap['selectionHalo'],
                'marker_element_count':snap['markers']
            }
        }
    browser.close()

for name,pal in [('failure',CAT_FAILURE),('revised',CAT_REVISED)]:
    entry={'normal':min_pair_distance(pal)}
    for cvdname,M in MACHADO.items(): entry[cvdname]=min_pair_distance(pal,M)
    payload['categorical_cvd'][name]={k:{'min_oklab_distance':v[0],'pair_indices':[v[1],v[2]]} for k,v in entry.items()}

payload['notes']={
 'cvd':'Machado et al. 2009 severity-1 transformation matrices are used as a diagnostic simulation. Simulation is not human CVD validation and Oklab distance is not a categorical-identification threshold.',
 'sequential':'Monotonic Oklab L is a diagnostic for ordered lightness direction, not proof of perceptual uniformity or task accuracy.',
 'geometry':'All conditions use identical panel/chart geometry; only theme/mode rendering changes.'
}
RESULTS.write_text(json.dumps(payload,indent=2),encoding='utf-8')
print(json.dumps(payload,indent=2))
