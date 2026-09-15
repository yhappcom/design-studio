from playwright.sync_api import sync_playwright
import json

HTML = '''<!doctype html><meta charset="utf-8">
<style>button:focus-visible,[role=button]:focus-visible{outline:3px solid currentColor}</style>
<button id="native" type="button">Save native</button>
<div id="incomplete" role="button" tabindex="0">Save incomplete</div>
<div id="custom" role="button" tabindex="0">Save custom</div>
<script>
for (const id of ['native','incomplete','custom']) {
  window[id+'Count']=0;
  document.getElementById(id).addEventListener('click',()=>window[id+'Count']++);
}
custom.addEventListener('keydown',e=>{
  if(e.key==='Enter'){e.preventDefault(); custom.click()}
  if(e.key===' '){e.preventDefault(); custom.click()}
});
</script>'''

results=[]
def record(name, ok, actual=None):
    results.append({'name':name,'pass':bool(ok),'actual':actual})

with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium', headless=True)
    page=browser.new_page()
    page.set_content(HTML)

    page.evaluate('document.activeElement && document.activeElement.blur()')
    sequence=[]
    for _ in range(3):
        page.keyboard.press('Tab')
        sequence.append(page.evaluate('document.activeElement.id'))
    record('tab_order_native_incomplete_custom', sequence==['native','incomplete','custom'], sequence)

    for control in ['native','incomplete','custom']:
        for key in ['Enter','Space']:
            page.evaluate(f'window.{control}Count=0')
            page.locator('#'+control).focus()
            page.keyboard.press(key)
            count=page.evaluate(f'window.{control}Count')
            expected=0 if control=='incomplete' else 1
            record(f'{control}_{key}_activation', count==expected, count)

    for control in ['native','incomplete','custom']:
        page.evaluate(f'window.{control}Count=0')
        page.locator('#'+control).click()
        count=page.evaluate(f'window.{control}Count')
        record(f'{control}_pointer_activation_once', count==1, count)

    page.set_content(HTML)
    page.keyboard.press('Tab')
    focus=page.locator('#native').evaluate("e=>({active:document.activeElement.id,matches:e.matches(':focus-visible'),outline:getComputedStyle(e).outlineStyle})")
    record('native_focus_visible_outline', focus['active']=='native' and focus['matches'] and focus['outline']!='none', focus)

    for control in ['native','incomplete','custom']:
        snapshot=page.locator('#'+control).aria_snapshot()
        record(f'{control}_aria_button_name', 'button' in snapshot.lower() and 'Save' in snapshot, snapshot)

    version=browser.version
    browser.close()

output={'browser':'Chromium '+version,'assertions':results,'passed':sum(r['pass'] for r in results),'total':len(results)}
print(json.dumps(output,indent=2))
