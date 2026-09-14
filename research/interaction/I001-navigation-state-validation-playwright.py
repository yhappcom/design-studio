import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright

HTML = Path(__file__).with_name('I001-navigation-state-validation-specimen.html').read_text(encoding='utf-8')

async def main():
    out = []
    checks = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        page = await browser.new_page()

        async def snap(label):
            st = await page.evaluate('window.__spec.getState()')
            st['label'] = label
            out.append(st)
            return st

        def ck(name, ok, detail=''):
            checks.append({'check': name, 'pass': bool(ok), 'detail': detail})

        await page.set_content(HTML)
        await page.focus('#open-a')
        await page.keyboard.press('Enter')
        st = await snap('keyboard-open-detail')
        ck('route transition focuses heading', st['activeTag'] == 'H1' and st['activeText'] == 'Record A', str(st))

        await page.keyboard.press('Tab')
        st = await snap('tab-after-detail-heading')
        ck('Up reachable immediately after route heading', st['activeId'] == 'up-list', str(st))

        await page.focus('#edit')
        await page.keyboard.press('Enter')
        st = await snap('keyboard-open-edit')
        ck('edit route focuses heading', st['activeTag'] == 'H1' and 'Edit Record A' in st['activeText'], str(st))

        await page.keyboard.press('Tab')
        st = await snap('tab-after-edit-heading')
        ck('Up detail reachable after edit heading', st['activeId'] == 'up-detail', str(st))

        await page.focus('#name')
        await page.fill('#name', 'Changed A')
        await page.focus('#cancel-edit')
        await page.keyboard.press('Enter')
        st = await snap('discard-dialog-open')
        ck('dialog opens and initial focus is inside', st['dialog'] and st['activeId'] == 'discard-cancel', str(st))

        await page.keyboard.press('Escape')
        st = await snap('discard-dialog-escape')
        ck('Escape closes and restores invoker focus', (not st['dialog']) and st['activeId'] == 'cancel-edit', str(st))

        await page.go_back()
        await page.wait_for_timeout(20)
        st = await snap('back-preserves-draft')
        ck('browser Back preserves dirty draft with status', st['view'] == 'detail' and st['drafts'].get('A') == 'Changed A' and 'preserved' in st['status'], str(st))

        await page.click('#nav-reports')
        await page.click('#nav-records')
        st = await snap('workspace-resume-after-back')
        ck('top-level resume preserves object identity', st['view'] == 'detail' and st['selectedId'] == 'A', str(st))

        await page.go_forward()
        await page.wait_for_timeout(20)
        st = await snap('forward-restores-draft')
        if st['view'] != 'edit':
            await page.click('#edit')
            st = await snap('reenter-edit-after-workspace')
        ck('edit draft restored', st['view'] == 'edit' and st['nameValue'] == 'Changed A', str(st))

        await page.click('#save')
        await page.wait_for_timeout(180)
        st = await snap('save-failed')
        ck('failure status separate from retry action', 'failed' in st['status'].lower() and st['statusAction'] == 'Retry' and st['activeId'] == 'retry', str(st))

        await page.keyboard.press('Enter')
        await page.wait_for_timeout(180)
        st = await snap('save-succeeded')
        ck('success retains status and focuses destination heading', st['view'] == 'detail' and st['status'] == 'Saved.' and st['activeTag'] == 'H1', str(st))

        page2 = await browser.new_page()
        await page2.set_content(HTML)
        await page2.evaluate("location.hash='#top=records&view=detail&id=B'; window.__spec.sync()")
        await page2.wait_for_timeout(10)
        st2 = await page2.evaluate('window.__spec.getState()')
        ck('deep-link establishes destination and focus', st2['view'] == 'detail' and st2['selectedId'] == 'B' and st2['activeTag'] == 'H1', str(st2))

        await page2.click('#up-list')
        st3 = await page2.evaluate('window.__spec.getState()')
        ck('Up traverses hierarchy to list', st3['view'] == 'list', str(st3))

        await page2.go_back()
        await page2.wait_for_timeout(20)
        st4 = await page2.evaluate('window.__spec.getState()')
        ck('browser Back traverses history back to deep-link detail', st4['view'] == 'detail' and st4['selectedId'] == 'B', str(st4))

        await browser.close()

    print(json.dumps({'checks': checks, 'states': out}, indent=2))

if __name__ == '__main__':
    asyncio.run(main())
