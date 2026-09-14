import asyncio
import json
from playwright.async_api import async_playwright

HTML = r'''<!doctype html><meta charset="utf-8"><style>
body{font:16px system-ui;margin:24px;background:#fff;color:#111}.nav{display:flex;gap:8px;margin-bottom:24px}.tab{padding:10px 14px;border:1px solid transparent;background:#eee;color:#222}.tab.naive.current{background:#1267d6;color:#fff}.tab.robust.current{background:#1267d6;color:#fff;border-inline-start:4px solid currentColor;font-weight:700;text-decoration:underline;text-underline-offset:4px}.focusable{margin:8px;padding:10px 14px;border:1px solid #888;background:#fff}.focus-naive:focus{outline:none;box-shadow:0 0 0 4px rgba(0,120,255,.55)}.focus-robust:focus{outline:3px solid #1267d6;outline-offset:3px;box-shadow:none}.states{display:grid;grid-template-columns:repeat(4,max-content);gap:10px;margin-top:24px}.state{padding:8px 12px;border:1px solid transparent}.naive.pending{background:#fff1a8}.naive.failed{background:#ffd0d0}.naive.unknown{background:#dccbff}.naive.confirmed{background:#c9f0d0}.robust{border-width:2px;border-style:solid}.robust.pending::before{content:'⏳ '}.robust.failed::before{content:'! ';font-weight:800}.robust.unknown::before{content:'? ';font-weight:800}.robust.confirmed::before{content:'✓ ';font-weight:800}
</style><h1>State resilience</h1><section id="naive"><h2>Naive</h2><nav class="nav"><button class="tab naive">Overview</button><button class="tab naive current">Records</button><button class="tab naive">Reports</button></nav><button class="focusable focus-naive">Focus target</button><div class="states"><div class="state naive pending" aria-label="Pending"></div><div class="state naive failed" aria-label="Failed"></div><div class="state naive unknown" aria-label="Outcome unknown"></div><div class="state naive confirmed" aria-label="Confirmed"></div></div></section><section id="robust"><h2>Robust</h2><nav class="nav"><button class="tab robust">Overview</button><button class="tab robust current" aria-current="page">Records</button><button class="tab robust">Reports</button></nav><button class="focusable focus-robust">Focus target</button><div class="states"><div class="state robust pending">Pending</div><div class="state robust failed">Failed</div><div class="state robust unknown">Outcome unknown</div><div class="state robust confirmed">Confirmed</div></div></section>'''


async def snapshot(page, mode):
    await page.emulate_media(forced_colors=mode)
    active = await page.evaluate("matchMedia('(forced-colors: active)').matches")

    async def styles(selector):
        return await page.locator(selector).evaluate_all(
            "els=>els.map(e=>{const s=getComputedStyle(e);return {bg:s.backgroundColor,color:s.color,borderWidth:s.borderInlineStartWidth,borderStyle:s.borderInlineStartStyle,fontWeight:s.fontWeight,textDecoration:s.textDecorationLine,text:e.textContent.trim(),ariaCurrent:e.getAttribute('aria-current'),ariaLabel:e.getAttribute('aria-label')}})"
        )

    await page.locator('#naive .focusable').focus()
    naive_focus = await page.locator('#naive .focusable').evaluate(
        "e=>{const s=getComputedStyle(e);return {outlineStyle:s.outlineStyle,outlineWidth:s.outlineWidth,boxShadow:s.boxShadow}}"
    )
    await page.locator('#robust .focusable').focus()
    robust_focus = await page.locator('#robust .focusable').evaluate(
        "e=>{const s=getComputedStyle(e);return {outlineStyle:s.outlineStyle,outlineWidth:s.outlineWidth,boxShadow:s.boxShadow}}"
    )

    return {
        'forcedMediaActive': active,
        'naiveTabs': await styles('#naive .tab'),
        'robustTabs': await styles('#robust .tab'),
        'naiveStates': await styles('#naive .state'),
        'robustStates': await styles('#robust .state'),
        'naiveFocus': naive_focus,
        'robustFocus': robust_focus,
    }


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        page = await browser.new_page(viewport={'width': 1000, 'height': 700})
        await page.set_content(HTML)
        normal = await snapshot(page, 'none')
        forced = await snapshot(page, 'active')

        checks = []
        def check(name, ok, detail=''):
            checks.append({'name': name, 'pass': bool(ok), 'detail': detail})

        normal_tab_bgs = [x['bg'] for x in normal['naiveTabs']]
        forced_tab_bgs = [x['bg'] for x in forced['naiveTabs']]
        normal_state_bgs = [x['bg'] for x in normal['naiveStates']]
        forced_state_bgs = [x['bg'] for x in forced['naiveStates']]

        check('forced-colors media active', forced['forcedMediaActive'] is True)
        check('naive selected color distinct in normal mode', len(set(normal_tab_bgs)) > 1)
        check('naive selected fill collapses in forced colors', len(set(forced_tab_bgs)) == 1, str(forced_tab_bgs))
        check('naive state colors distinct in normal mode', len(set(normal_state_bgs)) == 4)
        check('naive state fills collapse in forced colors', len(set(forced_state_bgs)) == 1, str(forced_state_bgs))
        check('naive focus glow exists normally', normal['naiveFocus']['boxShadow'] != 'none')
        check('naive focus glow removed in forced colors', forced['naiveFocus']['boxShadow'] == 'none')
        check('naive focus has no structural outline after removal', forced['naiveFocus']['outlineStyle'] == 'none')

        current = forced['robustTabs'][1]
        check('robust current exposes aria-current', current['ariaCurrent'] == 'page')
        check('robust current retains structural border', current['borderStyle'] != 'none' and float(current['borderWidth'].replace('px','')) >= 4)
        check('robust current retains underline', 'underline' in current['textDecoration'])
        check('robust focus outline survives', forced['robustFocus']['outlineStyle'] != 'none' and float(forced['robustFocus']['outlineWidth'].replace('px','')) >= 3)
        check('robust async states retain explicit text', [x['text'] for x in forced['robustStates']] == ['Pending','Failed','Outcome unknown','Confirmed'])
        check('robust async labels remain distinct without fill', len(set(x['text'] for x in forced['robustStates'])) == 4)

        result = {
            'study': 'I003',
            'browser': browser.version,
            'normal': normal,
            'forced': forced,
            'checks': checks,
            'passed': sum(x['pass'] for x in checks),
            'total': len(checks),
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
