import json, pathlib
from playwright.sync_api import sync_playwright

HTML = pathlib.Path('L006-pointer-capture-touch-lost-invoker-specimen.html').read_text()
OUT = pathlib.Path('L006-pointer-capture-touch-lost-invoker-results.json')
checks = []

def ck(name, cond, detail=None):
    checks.append({'name': name, 'pass': bool(cond), 'detail': detail})

def center(box):
    return box['x'] + box['width'] / 2, box['y'] + box['height'] / 2

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path='/usr/bin/chromium')

    # A. Broken: pointer capture survives modal opening.
    page = browser.new_page(viewport={'width': 1000, 'height': 760})
    page.set_content(HTML)
    x, y = center(page.locator('#dragTarget').bounding_box())
    page.mouse.move(x, y)
    page.mouse.down()
    page.mouse.move(x + 8, y + 4)
    before = page.evaluate('api.snapshot()')
    page.evaluate('api.openDragDialog()')
    dx, dy = center(page.locator('#dragDialogAction').bounding_box())
    page.mouse.move(dx, dy, steps=3)
    page.mouse.up()
    broken = page.evaluate('api.snapshot()')
    ck('pointer capture active before modal', any('gotcapture' in e for e in before['events']), before)
    ck('modal inertness does not cancel pre-existing captured stream in this Chromium run', broken['counts']['dragMove'] > before['counts']['dragMove'] and broken['counts']['dragUp'] == 1, broken)
    ck('broken underlying gesture can still commit after modal appears', broken['counts']['dragCommit'] == 1 and broken['dragOpen'], broken)

    # B. Revised: cancel/release underlying gesture before modal transition.
    pageR = browser.new_page(viewport={'width': 1000, 'height': 760})
    pageR.set_content(HTML)
    x, y = center(pageR.locator('#dragTarget').bounding_box())
    pageR.mouse.move(x, y)
    pageR.mouse.down()
    pageR.mouse.move(x + 8, y + 4)
    pageR.evaluate('api.cancelDragAndOpenDialog()')
    dx, dy = center(pageR.locator('#dragDialogAction').bounding_box())
    pageR.mouse.move(dx, dy, steps=3)
    pageR.mouse.up()
    pageR.wait_for_timeout(0)
    revised = pageR.evaluate('api.snapshot()')
    ck('revised policy explicitly releases capture before modal', any('gesture-canceled-before-modal' in e for e in revised['events']) and any('lostcapture' in e for e in revised['events']), revised)
    ck('revised policy prevents underlying drag commit after modal transition', revised['counts']['dragCommit'] == 0, revised)

    # C. Nested dismiss stack.
    pageS = browser.new_page(viewport={'width': 1000, 'height': 760})
    pageS.set_content(HTML)
    pageS.locator('#openStack').click()
    pageS.locator('#openStackPop').click()
    s0 = pageS.evaluate('api.snapshot()')
    pageS.keyboard.press('Escape')
    s1 = pageS.evaluate('api.snapshot()')
    pageS.keyboard.press('Escape')
    s2 = pageS.evaluate('api.snapshot()')
    ck('nested popover initially open inside modal', s0['stackOpen'] and s0['popOpen'], s0)
    ck('first Escape dismisses topmost popover before dialog', s1['stackOpen'] and not s1['popOpen'], s1)
    ck('second Escape dismisses parent dialog', not s2['stackOpen'], s2)
    ck('nested stack dismissal restores focus to parent invoker', s2['activeId'] == 'openStack', s2)

    # D. Lost invoker without app fallback.
    page2 = browser.new_page(viewport={'width': 1000, 'height': 760})
    page2.set_content(HTML)
    page2.locator('#openLost').click()
    page2.evaluate('api.removeLostInvoker()')
    page2.locator('#closeLost').click()
    page2.wait_for_timeout(20)
    lost_broken = page2.evaluate('api.snapshot()')
    ck('lost invoker does not automatically move focus to logical sibling', lost_broken['activeId'] != 'fallback', lost_broken)

    # E. Explicit lost-invoker fallback policy.
    page3 = browser.new_page(viewport={'width': 1000, 'height': 760})
    page3.set_content(HTML)
    page3.locator('#openLost').click()
    page3.evaluate('api.applyLostFallback(); api.removeLostInvoker()')
    page3.locator('#closeLost').click()
    page3.wait_for_timeout(20)
    lost_fix = page3.evaluate('api.snapshot()')
    ck('explicit lost-invoker policy restores logical fallback', lost_fix['activeId'] == 'fallback', lost_fix)

    # F. Touch overlap with popover.
    mobile = browser.new_context(viewport={'width': 1000, 'height': 760}, has_touch=True)
    tp = mobile.new_page()
    tp.set_content(HTML)
    tp.evaluate('api.showTouchPopover()')
    b = tp.locator('#touchPopAction').bounding_box()
    tx, ty = center(b)
    hit = tp.evaluate('([x,y])=>{const e=document.elementFromPoint(x,y);return e?e.id:null}', [tx, ty])
    tp.touchscreen.tap(tx, ty)
    ts = tp.evaluate('api.snapshot()')
    ck('touch hit-test resolves to popover foreground', hit == 'touchPopAction', {'hit': hit, 'box': b})
    ck('touch activates popover action only', ts['counts']['touchPop'] == 1 and ts['counts']['touchUnder'] == 0, ts)

    out = {
        'study': 'L006 higher fidelity layer ownership',
        'chromium': browser.version,
        'checks': checks,
        'pass_count': sum(c['pass'] for c in checks),
        'total': len(checks),
        'observations': {
            'capture_broken': broken,
            'capture_revised': revised,
            'nested': [s0, s1, s2],
            'lost_broken': lost_broken,
            'lost_fixed': lost_fix,
            'touch': ts,
        },
    }
    OUT.write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(json.dumps(out, indent=2))
    browser.close()
