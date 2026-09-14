import asyncio, base64, hashlib, json, platform, sys, time
from pathlib import Path
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
import fontTools
from playwright.async_api import async_playwright

OUT=Path('/tmp/t016'); OUT.mkdir(exist_ok=True)
TEXT='AB7C101 HL8301 99,999+59 가각 비행기록'
FIXED=2082844800  # 1970-01-01 in OpenType epoch

def rect_glyph(adv):
    pen=TTGlyphPen(None)
    if adv > 0:
        pen.moveTo((50,0)); pen.lineTo((max(60,adv-50),0)); pen.lineTo((max(60,adv-50),700)); pen.lineTo((50,700)); pen.closePath()
    return pen.glyph()

def build_font(path, family, scale=1.0):
    chars=sorted(set(TEXT))
    cmap={ord(c):f'u{ord(c):04X}' for c in chars if c!=' '}
    order=['.notdef','space']+list(cmap.values())
    fb=FontBuilder(1000,isTTF=True)
    fb.setupGlyphOrder(order)
    glyphs={'.notdef':rect_glyph(round(500*scale)),'space':TTGlyphPen(None).glyph()}
    metrics={'.notdef':(round(500*scale),0),'space':(round(300*scale),0)}
    for cp,g in cmap.items():
        base=420 if cp>=0xAC00 else 460
        adv=round(base*scale)
        glyphs[g]=rect_glyph(adv); metrics[g]=(adv,0)
    fb.setupGlyf(glyphs); fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=800,descent=-200,lineGap=0)
    fb.setupCharacterMap(cmap)
    fb.setupNameTable({'familyName':family,'styleName':'Regular','uniqueFontIdentifier':family+' Regular','fullName':family+' Regular','psName':family.replace(' ','')+'-Regular','version':'Version 1.000'})
    fb.setupOS2(sTypoAscender=800,sTypoDescender=-200,sTypoLineGap=0,usWinAscent=800,usWinDescent=200)
    fb.setupPost(); fb.setupMaxp();
    ttf=path.with_suffix('.ttf'); fb.save(ttf)
    f=TTFont(ttf,recalcTimestamp=False); f['head'].created=FIXED; f['head'].modified=FIXED; f.recalcTimestamp=False; f.save(ttf)
    f=TTFont(ttf,recalcTimestamp=False); f.flavor='woff2'; f.recalcTimestamp=False; f.save(path)
    return path.read_bytes()

primary=build_font(OUT/'primary.woff2','T016Primary',1.0)
fallback=build_font(OUT/'fallback.woff2','T016Fallback',1.25)

def sha(b): return hashlib.sha256(b).hexdigest()
def data_uri(b): return 'data:font/woff2;base64,'+base64.b64encode(b).decode()

FALLBACK_URI=data_uri(fallback)

def html(adjusted=False):
    adjust='size-adjust:80%;' if adjusted else ''
    return f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:T016Primary;src:url(https://font.test/primary.woff2) format("woff2");font-display:swap}}
@font-face{{font-family:T016Fallback;src:url({FALLBACK_URI}) format("woff2");{adjust}}}
body{{margin:0;font-family:sans-serif}}
.probe{{font-family:T016Fallback,sans-serif;font-size:32px;line-height:1.2;display:inline-block;white-space:nowrap}}
.row{{font-family:T016Fallback,sans-serif;font-size:32px;line-height:1.2;width:500px}}
.use{{font-family:T016Primary,T016Fallback,sans-serif}}
.marker{{width:10px;height:10px}}
</style><div id=p class=probe>{TEXT}</div><div id=r class=row>{TEXT}</div><div id=m class=marker></div>'''

async def snapshot(page):
    return await page.evaluate('''()=>({
      fontSetStatus:document.fonts.status,
      primaryCheck:document.fonts.check('32px T016Primary'),
      fallbackCheck:document.fonts.check('32px T016Fallback'),
      probeWidth:+p.getBoundingClientRect().width.toFixed(4),
      rowHeight:+r.getBoundingClientRect().height.toFixed(4),
      markerTop:+m.getBoundingClientRect().top.toFixed(4),
      computedFamily:getComputedStyle(p).fontFamily
    })''')

async def run_case(browser, adjusted, outcome):
    page=await browser.new_page(viewport={'width':900,'height':500})
    requests=[]
    async def route_handler(route):
        requests.append(route.request.url)
        if outcome=='success':
            await asyncio.sleep(1.0)
            await route.fulfill(status=200,content_type='font/woff2',body=primary)
        else:
            await route.abort()
    await page.route('https://font.test/**',route_handler)
    await page.set_content(html(adjusted),wait_until='domcontentloaded')
    await page.evaluate('document.fonts.ready')  # settle embedded fallback
    baseline=await snapshot(page)
    await page.evaluate("()=>{p.classList.add('use');r.classList.add('use')}")
    if outcome=='success':
        await asyncio.sleep(.25)
        during=await snapshot(page)
        await page.evaluate('document.fonts.ready')
        settled=await snapshot(page)
    else:
        await page.evaluate('document.fonts.ready')
        during=None
        settled=await snapshot(page)
    await page.close()
    return {'adjusted':adjusted,'outcome':outcome,'requests':requests,'baseline':baseline,'during':during,'settled':settled}

async def main():
 async with async_playwright() as pw:
    browser=await pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium')
    cases=[]
    for adjusted in (False,True):
        for outcome in ('success','failure'):
            cases.append(await run_case(browser,adjusted,outcome))
    version=browser.version
    await browser.close()

    # bounded assertions
    u_success=next(c for c in cases if not c['adjusted'] and c['outcome']=='success')
    a_success=next(c for c in cases if c['adjusted'] and c['outcome']=='success')
    u_fail=next(c for c in cases if not c['adjusted'] and c['outcome']=='failure')
    a_fail=next(c for c in cases if c['adjusted'] and c['outcome']=='failure')
    assertions={
      'unadjusted_during_is_fallback': u_success['during']['primaryCheck'] is False and u_success['during']['fontSetStatus']=='loading',
      'unadjusted_success_swaps': u_success['settled']['primaryCheck'] is True,
      'unadjusted_swap_changes_width_gt_20': abs(u_success['during']['probeWidth']-u_success['settled']['probeWidth'])>20,
      'unadjusted_swap_changes_row_height': u_success['during']['rowHeight']!=u_success['settled']['rowHeight'],
      'adjusted_during_is_fallback': a_success['during']['primaryCheck'] is False and a_success['during']['fontSetStatus']=='loading',
      'adjusted_success_swaps': a_success['settled']['primaryCheck'] is True,
      'adjusted_width_delta_lt_0_1': abs(a_success['during']['probeWidth']-a_success['settled']['probeWidth'])<0.1,
      'adjusted_row_height_stable': a_success['during']['rowHeight']==a_success['settled']['rowHeight'],
      'failure_primary_check_false': u_fail['settled']['primaryCheck'] is False and a_fail['settled']['primaryCheck'] is False,
      'failure_unadjusted_retains_wide_fallback': u_fail['settled']['probeWidth']>a_fail['settled']['probeWidth']+20,
      'failure_adjusted_matches_primary_geometry_lt_0_1': abs(a_fail['settled']['probeWidth']-a_success['settled']['probeWidth'])<0.1,
      'one_primary_request_per_case': all(len(c['requests'])==1 for c in cases),
    }
    result={
      'environment':{'python':sys.version.split()[0],'fontTools':fontTools.__version__,'chromium':version,'platform':platform.platform()},
      'artifacts':{'primary_sha256':sha(primary),'fallback_sha256':sha(fallback),'primary_bytes':len(primary),'fallback_bytes':len(fallback)},
      'design':{'text':TEXT,'font_size_px':32,'row_width_px':500,'delay_ms':1000,'early_sample_ms':250,'fallback_scale':1.25,'adjusted_size_adjust':'80%'},
      'cases':cases,
      'assertions':assertions,
      'assertions_true':sum(assertions.values()),'assertions_total':len(assertions)
    }
    (OUT/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=False,indent=2))

asyncio.run(main())
