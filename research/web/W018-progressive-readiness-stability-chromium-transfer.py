import json
from playwright.sync_api import sync_playwright
HTML='''<!doctype html><meta charset=utf-8><style>
*{box-sizing:border-box} body{font:16px system-ui;margin:0;padding:16px;max-width:100%} .case{border:1px solid;padding:12px;margin:12px 0;overflow-wrap:anywhere}.row{display:flex;gap:8px;flex-wrap:wrap}.good .slot{min-height:72px}.bad .slot{min-height:0}button{min-height:44px;max-width:100%;white-space:normal}.status{min-height:1.5em}:focus-visible{outline:3px solid;outline-offset:2px}
</style><main><h1>Operational records</h1>
<section class='case bad' id='bad'><h2>Unreserved async</h2><div class=slot></div><div class=row><button disabled>Confirm synchronized operational record after verification</button></div><p class=status>Loading…</p></section>
<section class='case good' id='good'><h2>Reserved async</h2><div class=slot aria-busy=true>Preparing record…</div><div class=row><button disabled>Confirm synchronized operational record after verification</button></div><p class=status>Loading…</p></section></main>
<script>
window.events=[]; const mark=x=>events.push([x,performance.now()]);
new PerformanceObserver(l=>{for(const e of l.getEntries()) if(!e.hadRecentInput) window.cls=(window.cls||0)+e.value}).observe({type:'layout-shift',buffered:true});
requestAnimationFrame(()=>mark('first-frame'));
setTimeout(()=>{document.querySelector('#bad .slot').innerHTML='<strong>Flight KE704</strong><br>ICN → NRT · 02:18';document.querySelector('#good .slot').innerHTML='<strong>Flight KE704</strong><br>ICN → NRT · 02:18';mark('data-visible')},120);
setTimeout(()=>{for(const x of document.querySelectorAll('.slot'))x.removeAttribute('aria-busy'); for(const b of document.querySelectorAll('button'))b.disabled=false; for(const s of document.querySelectorAll('.status'))s.textContent='Ready to confirm'; mark('task-ready')},260);
</script>'''
with sync_playwright() as p:
 b=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1280,'height':720}); page.set_content(HTML); page.wait_for_timeout(450)
 ev=page.evaluate('events'); cls=page.evaluate('window.cls||0'); first=dict(ev)['first-frame']; visible=dict(ev)['data-visible']; ready=dict(ev)['task-ready']
 p2=b.new_page(viewport={'width':1280,'height':720}); p2.set_content(HTML)
 expr="() => Object.fromEntries(['bad','good'].map(id=>[id,document.querySelector('#'+id+' button').getBoundingClientRect().top-document.querySelector('#'+id).getBoundingClientRect().top]))"
 before=p2.evaluate(expr); p2.wait_for_timeout(180); after=p2.evaluate(expr); shifts={k:round(abs(after[k]-before[k]),2) for k in before}
 p3=b.new_page(viewport={'width':320,'height':900}); p3.set_content(HTML); p3.evaluate("document.documentElement.style.fontSize='200%'"); p3.wait_for_timeout(450)
 overflow=p3.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth'); buttons=p3.evaluate("[...document.querySelectorAll('button')].map(b=>({w:b.getBoundingClientRect().width,sw:b.scrollWidth,txt:b.innerText}))")
 p3.keyboard.press('Tab'); p3.keyboard.press('Tab'); focus=p3.evaluate("document.activeElement.tagName==='BUTTON'")
 checks={'first_frame_before_data':first<visible,'data_visible_before_task_ready':visible<ready,'bad_layout_shift_exceeds_good':shifts['bad']>shifts['good'],'good_shift_zero_or_small':shifts['good']<=1,'narrow_200pct_no_horizontal_overflow':not overflow,'long_button_labels_fit':all(x['sw']<=x['w']+1 for x in buttons),'keyboard_focus_reaches_button':focus,'task_ready_not_inferred_from_first_frame':ready-first>100}
 out={'browser':b.version,'events_ms':{k:round(v,2) for k,v in ev},'layout_shift_button_top_px':shifts,'cls_observed':cls,'stress':{'viewport_css_px':[320,900],'root_font_size':'200%','horizontal_overflow':overflow,'buttons':buttons},'checks':checks,'pass':sum(checks.values()),'total':len(checks)}
 print(json.dumps(out,indent=2)); b.close()
