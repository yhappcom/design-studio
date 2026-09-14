from playwright.sync_api import sync_playwright
import json, pathlib

HTML = pathlib.Path(__file__).with_name('L002-density-validation-specimen.html').read_text()
VIEWPORTS = [('wide',1440,900),('desktop',1024,768),('tablet',768,800),('mobile',390,844)]
POLICIES = ['naive','preserve','adaptive']
DENSITIES = ['compact','intermediate','spacious']
SCALES = [1,1.25,2]
LOCALES = ['en','ko']
rows = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    for viewport_name, width, height in VIEWPORTS:
        page = browser.new_page(viewport={'width': width, 'height': height})
        page.set_content(HTML)
        for policy in POLICIES:
            for density in DENSITIES:
                for scale in SCALES:
                    for locale in LOCALES:
                        page.evaluate("([p,d,s,l])=>setConfig(p,d,s,l)", [policy,density,scale,locale])
                        result = page.evaluate("measure()")
                        result.update(viewport=viewport_name,width=width,height=height,policy=policy,density=density,scale=scale,locale=locale)
                        rows.append(result)
        page.close()
    browser.close()

pathlib.Path(__file__).with_name('L002-density-validation-results.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
print(json.dumps(rows, ensure_ascii=False))
