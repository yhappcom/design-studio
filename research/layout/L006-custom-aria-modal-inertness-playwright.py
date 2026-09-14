from playwright.sync_api import sync_playwright
from pathlib import Path
import json
HTML=Path('/mnt/data/l006aria/specimen.html').read_text(encoding='utf-8')
R={'environment':{},'broken':{},'revised':{},'assertions':[]}
def ck(name,cond,obs=None): R['assertions'].append({'name':name,'pass':bool(cond),'observed':obs})
def ax_info(nodes):
    out=[]
    for n in nodes:
        if n.get('ignored'): continue
        role=n.get('role',{}).get('value'); name=n.get('name',{}).get('value') or ''
        if role in ('generic','none','RootWebArea','StaticText','InlineTextBox'): continue
        props={p['name']:p.get('value',{}).get('value') for p in n.get('properties',[])}
        out.append({'role':role,'name':name,'properties':props})
    return out
def find(nodes,role,name):
    return next((n for n in nodes if n['role']==role and n['name']==name),None)
with sync_playwright() as p:
    b=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium')
    R['environment']['chromium_version']=b.version
    for mode in ('broken','revised'):
        c=b.new_context(viewport={'width':900,'height':700}); pg=c.new_page(); pg.set_content(HTML)
        cdp=c.new_cdp_session(pg); cdp.send('Accessibility.enable')
        pg.evaluate('openBroken()' if mode=='broken' else 'openRevised()'); pg.wait_for_timeout(20)
        ax=ax_info(cdp.send('Accessibility.getFullAXTree')['nodes']); initial=pg.evaluate('state()')
        pg.locator('#confirm').focus(); pg.keyboard.press('Shift+Tab'); rev1=pg.evaluate('state()'); pg.keyboard.press('Shift+Tab'); rev2=pg.evaluate('state()')
        pg.locator('#cancel').focus(); pg.keyboard.press('Tab'); fwd1=pg.evaluate('state()')
        box=pg.locator('#danger').bounding_box(); x=box['x']+box['width']/2; y=box['y']+box['height']/2
        hit=pg.evaluate('([x,y])=>{const e=document.elementFromPoint(x,y);return {id:e&&e.id,tag:e&&e.tagName,className:e&&e.className}}',[x,y])
        pg.mouse.click(x,y); after_click=pg.evaluate('state()')
        if mode=='revised':
            pg.locator('#cancel').click(); pg.wait_for_timeout(10); after_close=pg.evaluate('state()')
        else: after_close=None
        R[mode]={'initial':initial,'ax':ax,'reverse':[rev1,rev2],'forward':[fwd1],'background_point':{'x':x,'y':y,'hit':hit},'after_click':after_click,'after_close':after_close}
        c.close()
    b.close()
br,rv=R['broken'],R['revised']; bd=find(br['ax'],'dialog','Confirm deletion'); rd=find(rv['ax'],'dialog','Confirm deletion'); bg=find(br['ax'],'button','Background destructive action')
ck('B1 broken ARIA dialog is exposed with modal=true', bd is not None and bd['properties'].get('modal') is True, bd)
ck('B2 aria-modal alone does not make application DOM inert', br['initial']['appInert'] is False, br['initial'])
ck('B3 background destructive action remains exposed and focusable in Chromium AX tree', bg is not None and bg['properties'].get('focusable') is True, bg)
ck('B4 broken reverse Tab escapes dialog to background controls', br['reverse'][0]['active']=='danger' and br['reverse'][1]['active']=='open', br['reverse'])
ck('B5 broken forward Tab leaves dialog task', br['forward'][0]['active'] not in ('confirm','cancel'), br['forward'])
ck('B6 broken visual backdrop does not own outside-dialog background point', br['background_point']['hit']['id']=='danger', br['background_point'])
ck('B7 broken background destructive action activates despite aria-modal=true', br['after_click']['counts']['bg']==1, br['after_click'])
ck('R1 revised dialog remains exposed with modal=true', rd is not None and rd['properties'].get('modal') is True, rd)
ck('R2 revised application background is actually inert', rv['initial']['appInert'] is True, rv['initial'])
ck('R3 revised inert background is absent from Chromium AX tree', find(rv['ax'],'button','Background destructive action') is None and find(rv['ax'],'textbox','Record name ') is None, rv['ax'])
ck('R4 revised reverse traversal stays within dialog controls', [s['active'] for s in rv['reverse']]==['cancel','confirm'], rv['reverse'])
ck('R5 revised forward traversal cycles to first dialog control', rv['forward'][0]['active']=='confirm', rv['forward'])
ck('R6 revised backdrop owns outside-dialog point and blocks underlying action', rv['background_point']['hit']['id']!='danger' and rv['after_click']['counts']['bg']==0, {'hit':rv['background_point'],'after':rv['after_click']})
ck('R7 revised close restores focus to logical invoker', rv['after_close']['active']=='open' and rv['after_close']['appInert'] is False, rv['after_close'])
R['summary']={'passed':sum(a['pass'] for a in R['assertions']),'total':len(R['assertions'])}
Path('/mnt/data/l006aria/results.json').write_text(json.dumps(R,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(R['summary']))
for a in R['assertions']: print(('PASS' if a['pass'] else 'FAIL'),a['name'])
