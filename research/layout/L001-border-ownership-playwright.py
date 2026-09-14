from __future__ import annotations
from pathlib import Path
from io import BytesIO
import hashlib, json, random
from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright

CHROMIUM='/usr/bin/chromium'
BASE=Path(__file__).resolve().parent
HTML=(BASE/'L001-border-ownership-specimen.html').read_text(encoding='utf-8')
OUT=BASE/'L001-border-ownership-results-summary.json'
IDS=['B0','E-L','E-R','T-L','T-R','C-L','C-R','X-L','X-R']
PAIRS=[('E-L','E-R'),('T-L','T-R'),('C-L','C-R'),('X-L','X-R')]

def sha(im):
    return hashlib.sha256(im.tobytes()).hexdigest()

def diff_fraction(a,b):
    d=ImageChops.difference(a,b).convert('L')
    hist=d.histogram(); changed=sum(hist[1:]); return changed/(a.width*a.height)

def main():
    out={'study':'L001-border-ownership','stimuli':{},'pair_checks':{},'randomized_human_protocol_orders':[]}
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path=CHROMIUM)
        page=browser.new_page(viewport={'width':1280,'height':900},device_scale_factor=1)
        page.set_content(HTML)
        out['chromium']=browser.version
        imgs={}
        for sid in IDS:
            el=page.locator(f'[data-id="{sid}"]')
            png=el.screenshot()
            im=Image.open(BytesIO(png)).convert('RGB')
            imgs[sid]=im
            crop=im.crop((140,82,220,142))
            out['stimuli'][sid]={'size':im.size,'local_crop_sha256':sha(crop)}
        base=imgs['B0']
        for a,b in PAIRS:
            ca=imgs[a].crop((140,82,220,142)); cb=imgs[b].crop((140,82,220,142))
            ra=imgs[a].copy(); rb=imgs[b].copy()
            white=Image.new('RGB',(80,60),'white')
            ra.paste(white,(140,82)); rb.paste(white,(140,82))
            out['pair_checks'][f'{a}_vs_{b}']={
              'local_crop_identical': ca.tobytes()==cb.tobytes(),
              'local_crop_diff_fraction': diff_fraction(ca,cb),
              'remote_context_diff_fraction': diff_fraction(ra,rb),
            }
        basecrop=base.crop((140,82,220,142))
        out['all_local_crops_equal_baseline']=all(imgs[s].crop((140,82,220,142)).tobytes()==basecrop.tobytes() for s in IDS)
        for seed in [101,202,303,404]:
            r=random.Random(seed); order=IDS[:]; r.shuffle(order); out['randomized_human_protocol_orders'].append({'seed':seed,'order':order})
        browser.close()
    OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
