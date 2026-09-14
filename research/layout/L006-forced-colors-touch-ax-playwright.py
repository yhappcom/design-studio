from playwright.sync_api import sync_playwright
from PIL import Image
import io, json, math
HTML=open('/mnt/data/l006fc/L006-forced-touch-ax-specimen.html',encoding='utf-8').read()
results={'environment':{},'forced_colors':{},'touch_implicit_capture':{},'accessibility_tree':{},'assertions':[]}

def check(name, condition, observed=None):
    results['assertions'].append({'name':name,'pass':bool(condition),'observed':observed})

def boundary_signal(png_bytes, rect, bg_rgb):
    im=Image.open(io.BytesIO(png_bytes)).convert('RGB')
    left=int(round(rect['x'])); top=int(round(rect['y'])); right=int(round(rect['x']+rect['width']))
    y0=max(0,top-3); y1=max(0,top)
    total=0; diff=0; colors={}
    for y in range(y0,y1):
        for x in range(left,right):
            p=im.getpixel((x,y)); total+=1
            if p!=bg_rgb: diff+=1
            colors[p]=colors.get(p,0)+1
    return {'diff_pixels':diff,'total_pixels':total,'diff_fraction':diff/total if total else None,'unique_colors':len(colors)}

def parse_rgb(s):
    nums=[int(float(v.strip())) for v in s[s.find('(')+1:s.find(')')].split(',')[:3]]
    return tuple(nums)

def ax_simplify(nodes):
    out=[]
    for n in nodes:
        if n.get('ignored'): continue
        role=n.get('role',{}).get('value'); name=n.get('name',{}).get('value') or ''
        if role in ('generic','none','RootWebArea','StaticText','InlineTextBox'): continue
        out.append({'role':role,'name':name})
    return out

def ax_has(nodes, role, name):
    return any(n['role']==role and n['name']==name for n in nodes)

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium')
    results['environment']['chromium_version']=browser.version

    ctx=browser.new_context(viewport={'width':800,'height':900}); pg=ctx.new_page(); pg.set_content(HTML); pg.evaluate("fcOpen('broken')")
    normal=pg.evaluate('fcState()'); results['forced_colors']['broken_normal']=normal
    check('FC1 broken normal shadow is present', normal['styles']['shadow']!='none', normal['styles']['shadow'])
    ctx.close()

    forced_data={}
    for variant in ['broken','revised','optout']:
        ctx=browser.new_context(viewport={'width':800,'height':900}); pg=ctx.new_page(); pg.set_content(HTML); pg.emulate_media(forced_colors='active'); pg.evaluate(f"fcOpen('{variant}')"); pg.wait_for_timeout(30)
        st=pg.evaluate('fcState()'); png=pg.screenshot(); sig=boundary_signal(png,st['panelRect'],parse_rgb(st['bodyBg']))
        pg.mouse.click(st['hit']['x'],st['hit']['y']); after=pg.evaluate('fcState()')
        forced_data[variant]={'before':st,'boundary_signal':sig,'after_counts':after['counts']}
        ctx.close()
    results['forced_colors']['forced']=forced_data
    b=forced_data['broken']; r=forced_data['revised']; o=forced_data['optout']
    check('FC2 forced-colors removes broken shadow', b['before']['styles']['shadow']=='none', b['before']['styles']['shadow'])
    check('FC3 broken panel surface merges with page Canvas', b['before']['styles']['bg']==b['before']['bodyBg'], {'panel':b['before']['styles']['bg'],'body':b['before']['bodyBg']})
    check('FC4 broken has no structural outline', b['before']['styles']['outlineWidth']=='0px', b['before']['styles'])
    check('FC5 broken top boundary signal disappears', b['boundary_signal']['diff_pixels']==0, b['boundary_signal'])
    check('FC6 broken visual-cue loss does not change hit owner', b['before']['hit']['id']=='fc-front', b['before']['hit'])
    check('FC7 broken forced-colors activation still goes foreground only', b['after_counts']=={'front':1,'back':0}, b['after_counts'])
    check('FC8 revised structural outline remains', r['before']['styles']['outlineWidth']=='3px' and r['before']['styles']['outlineStyle']=='solid', r['before']['styles'])
    check('FC9 revised boundary signal survives forced colors', r['boundary_signal']['diff_pixels']==r['boundary_signal']['total_pixels'] and r['boundary_signal']['total_pixels']>0, r['boundary_signal'])
    check('FC10 revised activation remains foreground only', r['after_counts']=={'front':1,'back':0}, r['after_counts'])
    check('FC11 opt-out reports forced-color-adjust none', o['before']['styles']['forcedColorAdjust']=='none', o['before']['styles']['forcedColorAdjust'])
    check('FC12 opt-out preserves author shadow in emulation', o['before']['styles']['shadow']!='none', o['before']['styles']['shadow'])
    check('FC13 opt-out boundary signal remains, diagnostic only', o['boundary_signal']['diff_pixels']>0, o['boundary_signal'])

    def run_touch(mode):
        ctx=browser.new_context(viewport={'width':800,'height':900},has_touch=True,is_mobile=True)
        pg=ctx.new_page(); pg.set_content(HTML); pg.evaluate('touchReset()')
        box=pg.locator('#touch-drag').bounding_box(); x=box['x']+50; y=box['y']+50
        cdp=ctx.new_cdp_session(pg)
        def send(tp,xx,yy):
            pts=[] if tp=='touchEnd' else [{'x':xx,'y':yy,'radiusX':2,'radiusY':2,'force':0.5,'id':1}]
            cdp.send('Input.dispatchTouchEvent',{'type':tp,'touchPoints':pts})
        send('touchStart',x,y); send('touchMove',x+4,y+4); pg.wait_for_timeout(30)
        before=pg.evaluate('touchState()')
        pg.evaluate('touchOpenBroken()' if mode=='broken' else 'touchOpenRevised()')
        after_open=pg.evaluate('touchState()')
        d=pg.locator('#touch-dialog').bounding_box(); tx=d['x']+d['width']/2; ty=d['y']+d['height']/2
        send('touchMove',tx,ty); send('touchEnd',tx,ty); pg.wait_for_timeout(30)
        after=pg.evaluate('touchState()'); ctx.close(); return {'before':before,'after_open':after_open,'after':after}
    tb=run_touch('broken'); tr=run_touch('revised'); results['touch_implicit_capture']={'broken':tb,'revised':tr}
    check('T1 touch pointerdown has implicit capture', tb['before']['captured'] is True and any(e['t']=='pointerdown' and e['type']=='touch' and e['cap'] for e in tb['before']['log']), tb['before'])
    check('T2 gotpointercapture observed for touch', any(e['t']=='gotpointercapture' for e in tb['before']['log']), tb['before']['log'])
    check('T3 modal entry alone leaves implicit capture active', tb['after_open']['captured'] is True and tb['after_open']['modal'] is True, tb['after_open'])
    check('T4 broken captured touch stream continues to background after modal entry', any(e['t']=='pointermove' and e['cap'] for e in tb['after']['log'][len(tb['before']['log']):]) and any(e['t']=='pointerup' and e['cap'] for e in tb['after']['log']), tb['after']['log'])
    check('T5 broken touch gesture commits background mutation', tb['after']['commit']==1, tb['after']['commit'])
    check('T6 revised policy releases implicit capture before modal interaction', tr['after_open']['captured'] is False and tr['after_open']['cancelled'] is True, tr['after_open'])
    check('T7 revised touch gesture produces no background commit', tr['after']['commit']==0, tr['after'])

    ctx=browser.new_context(viewport={'width':800,'height':900}); pg=ctx.new_page(); pg.set_content(HTML); cdp=ctx.new_cdp_session(pg); cdp.send('Accessibility.enable')
    def snap(): return ax_simplify(cdp.send('Accessibility.getFullAXTree')['nodes'])
    base=snap(); pg.click('#ax-open-pop'); pop=snap(); pg.evaluate("axPop.hidePopover()")
    pg.click('#ax-open-dialog'); dialog=snap(); pg.click('#ax-open-nested'); nested=snap(); pg.evaluate("axNested.hidePopover(); axDialog.close()"); pg.wait_for_timeout(20); closed=snap()
    results['accessibility_tree']={'base':base,'popover':pop,'dialog':dialog,'nested':nested,'closed':closed}
    check('AX1 baseline background action exposed', ax_has(base,'button','Background action'), base)
    check('AX2 non-modal popover region/action exposed', ax_has(pop,'region','Quick tools') and ax_has(pop,'button','Popover action'), pop)
    check('AX3 non-modal popover keeps background action exposed', ax_has(pop,'button','Background action'), pop)
    check('AX4 modal dialog role/name exposed', ax_has(dialog,'dialog','Confirm task'), dialog)
    check('AX5 modal removes background action from exposed AX tree', not ax_has(dialog,'button','Background action'), dialog)
    check('AX6 nested popover is exposed inside modal', ax_has(nested,'region','Nested tools') and ax_has(nested,'button','Nested action'), nested)
    check('AX7 nested popover does not re-expose page background', not ax_has(nested,'button','Background action'), nested)
    check('AX8 closing modal restores page background to exposed AX tree', ax_has(closed,'button','Background action'), closed)
    ctx.close(); browser.close()

results['summary']={'passed':sum(1 for a in results['assertions'] if a['pass']),'total':len(results['assertions'])}
def event_types(state): return [e['t'] for e in state['log']]
def ax_pairs(nodes): return [f"{n['role']}::{n['name']}" for n in nodes]
public_results={
  'environment':results['environment'],
  'forced_colors':{
    'broken_normal_shadow':results['forced_colors']['broken_normal']['styles']['shadow'],
    'broken_forced':{'shadow':b['before']['styles']['shadow'],'background':b['before']['styles']['bg'],'page_background':b['before']['bodyBg'],'outline_width':b['before']['styles']['outlineWidth'],'boundary_signal':b['boundary_signal'],'hit_owner':b['before']['hit']['id'],'activation':b['after_counts']},
    'revised_forced':{'shadow':r['before']['styles']['shadow'],'outline_width':r['before']['styles']['outlineWidth'],'outline_style':r['before']['styles']['outlineStyle'],'outline_color':r['before']['styles']['outlineColor'],'boundary_signal':r['boundary_signal'],'hit_owner':r['before']['hit']['id'],'activation':r['after_counts']},
    'optout_forced':{'forced_color_adjust':o['before']['styles']['forcedColorAdjust'],'shadow':o['before']['styles']['shadow'],'boundary_signal':o['boundary_signal']}
  },
  'touch_implicit_capture':{
    'broken':{'before_captured':tb['before']['captured'],'after_modal_captured':tb['after_open']['captured'],'events':event_types(tb['after']),'commit':tb['after']['commit']},
    'revised':{'before_captured':tr['before']['captured'],'after_modal_captured':tr['after_open']['captured'],'cancelled':tr['after_open']['cancelled'],'events':event_types(tr['after']),'commit':tr['after']['commit']}
  },
  'accessibility_tree':{k:ax_pairs(v) for k,v in results['accessibility_tree'].items()},
  'assertions':[{'name':a['name'],'pass':a['pass']} for a in results['assertions']],
  'summary':results['summary']
}
open('/mnt/data/l006fc/L006-forced-touch-ax-results-summary.json','w',encoding='utf-8').write(json.dumps(public_results,ensure_ascii=False,indent=2))
print(json.dumps(results['summary']))
for a in results['assertions']:
    print(('PASS' if a['pass'] else 'FAIL'),a['name'])
