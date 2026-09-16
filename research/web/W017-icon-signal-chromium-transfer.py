import json
from playwright.sync_api import sync_playwright

HTML='''<style>button{min-width:32px;min-height:32px;color:rgb(20,20,20);border:1px solid currentColor}button:focus-visible{outline:2px solid currentColor;outline-offset:2px}.toolbar{display:flex;gap:8px;flex-wrap:wrap}.warn{color:rgb(150,0,0)}@media(forced-colors:active){button{border:1px solid ButtonText}.warn{color:CanvasText}}</style><div class=toolbar><button id=edit><svg aria-hidden=true focusable=false width=16 height=16><path fill=currentColor d="M0 0h16v16H0z"/></svg><span>Edit record</span></button><button id=more aria-label="More actions"><svg aria-hidden=true focusable=false width=16 height=16><circle fill=currentColor cx=8 cy=8 r=6/></svg></button><button id=disc aria-expanded=false aria-controls=details><svg aria-hidden=true focusable=false width=16 height=16><path fill=currentColor d="M0 0h16v16H0z"/></svg><span>Details</span></button></div><div id=details hidden>Detail region</div><p id=warning class=warn><span aria-hidden=true>!</span> Sync failed. Retry after checking connection.</p><script>disc.onclick=()=>{const e=disc.getAttribute('aria-expanded')==='true';disc.setAttribute('aria-expanded',String(!e));details.hidden=e}</script>'''
checks=[]
def ck(n,o,v): checks.append({'name':n,'pass':bool(o),'observed':v})
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium'); page=b.new_page(); page.set_content(HTML)
    for sel in ['#edit','#more','#disc']:
        snap=page.locator(sel).aria_snapshot(); ck(sel+' named button','button' in snap and any(x in snap for x in ['Edit record','More actions','Details']),snap)
    ck('decorative SVG hidden',page.locator('svg[aria-hidden=true]').count()==3,page.locator('svg[aria-hidden=true]').count())
    for sel in ['#edit','#more','#disc']:
        box=page.locator(sel).bounding_box(); ck(sel+' target >=24',box['width']>=24 and box['height']>=24,box)
    page.click('#disc'); ck('disclosure programmatic state',page.locator('#disc').get_attribute('aria-expanded')=='true' and page.locator('#details').is_visible(),{'expanded':page.locator('#disc').get_attribute('aria-expanded'),'visible':page.locator('#details').is_visible()})
    page.set_viewport_size({'width':320,'height':500}); page.evaluate("document.documentElement.style.fontSize='200%'"); ck('200% labels remain visible',page.locator('#edit span').is_visible() and page.locator('#disc span').is_visible(),True)
    page.evaluate("document.activeElement.blur()"); page.keyboard.press('Tab'); outline=page.evaluate("getComputedStyle(document.activeElement).outlineStyle"); ck('keyboard focus visible',outline!='none',outline)
    page.emulate_media(forced_colors='active'); border=page.evaluate("getComputedStyle(edit).borderTopStyle"); warn=page.locator('#warning').inner_text(); ck('forced colors retains boundary',border!='none',border); ck('warning meaning has text','Sync failed' in warn,warn)
    out={'browser':b.version,'mode':'set_content DOM + forced-colors emulation; no network navigation','checks':checks,'passed':sum(x['pass'] for x in checks),'total':len(checks)}; b.close()
print(json.dumps(out,indent=2))
