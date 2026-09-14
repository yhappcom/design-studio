import asyncio
import json
from playwright.async_api import async_playwright

LONG_LABEL = "국제 분산 커버드콜 수익전략 포트폴리오 / $11,242 +1.8%"

STACKS = {
    "Inter_NotoCJK": '"Inter", "Noto Sans CJK KR", sans-serif',
    "Inter_NanumGothic": '"Inter", "NanumGothic", sans-serif',
    "Inter_NanumBarun": '"Inter", "NanumBarunGothic", sans-serif',
    "Noto_NotoCJK": '"Noto Sans", "Noto Sans CJK KR", sans-serif',
}

ROWS = [
    ["알파 월분배 인컴 포트폴리오 장기추적", "운용 중", "$12,884", "+3.8%"],
    ["글로벌 고배당 인컴 전략 검토대상", "검토 필요", "$8,104", "-1.2%"],
    ["장기 듀레이션 인컴 바스켓 비교대상", "운용 중", "$18,220", "+0.6%"],
    ["기술주 기반 커버드콜 인컴 포트폴리오", "운용 중", "$14,052", "+2.4%"],
    ["월분배 핵심 자산배분 포트폴리오", "일시 중지", "$9,994", "-0.4%"],
    ["국제 분산 커버드콜 수익전략 포트폴리오", "운용 중", "$11,242", "+1.8%"],
    ["고변동성 인컴 슬리브 위험점검 필요", "검토 필요", "$7,880", "-3.1%"],
    ["은퇴 현금흐름 안정성 중심 포트폴리오", "운용 중", "$16,530", "+0.2%"],
    ["전술적 기회 포착 자산 바스켓", "운용 중", "$10,402", "+4.9%"],
    ["원금회수율 집중 모니터링 포트폴리오", "검토 필요", "$6,884", "-0.9%"],
    ["장기 자동재투자 성과추적 포트폴리오", "운용 중", "$13,290", "+1.1%"],
    ["세금 정산 및 환급 추적 관심목록", "운용 중", "$5,960", "+0.1%"],
]

HTML = r'''<!doctype html><html lang="ko"><meta charset="utf-8"><style>
:root{--fs:1;--row-pad:4px;--gap:6px;--control-h:44px;--page-pad:16px;font-size:calc(16px * var(--fs))}
*{box-sizing:border-box}body{margin:0;color:#111;background:#fff;font-family:var(--stack)}
.app{padding:var(--page-pad);max-width:1180px;margin:auto}.table{border:1px solid #aaa}
.row{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,.9fr) minmax(0,.8fr) minmax(0,.8fr) minmax(76px,.55fr);gap:var(--gap);align-items:center;padding:var(--row-pad) 10px;border-bottom:1px solid #ddd}
.cell{min-width:0;overflow-wrap:anywhere}.header{font-weight:700;background:#f3f3f3}.action{justify-self:end;min-height:var(--control-h);font:inherit;padding:6px 10px}.metric,.change{font-variant-numeric:tabular-nums}
body[data-density="intermediate"]{--row-pad:8px;--gap:10px;--page-pad:24px}body[data-density="spacious"]{--row-pad:14px;--gap:16px;--page-pad:32px}
@media(max-width:720px){.row.header{display:none}.row.data-row{grid-template-columns:minmax(0,1fr) auto;grid-template-areas:'name action' 'status status' 'metric change';align-items:start}.name{grid-area:name;font-weight:650}.status{grid-area:status}.metric{grid-area:metric}.change{grid-area:change;text-align:right}.action{grid-area:action}.status,.metric,.change{display:grid;grid-template-columns:auto 1fr;gap:6px}.status::before{content:'상태';font-size:.75em;font-weight:600}.metric::before{content:'평가액';font-size:.75em;font-weight:600}.change::before{content:'변동';font-size:.75em;font-weight:600}.app{max-width:none}}
body[data-policy="robust"][data-scale="1.25"] .row.data-row,body[data-policy="robust"][data-scale="2"] .row.data-row{grid-template-areas:'name name' 'status action' 'metric change'}
</style><body data-density="compact" data-scale="1" data-policy="base"><main class="app"><section class="table"><div class="row header"><div>포트폴리오</div><div>상태</div><div>평가액</div><div>변동</div><div></div></div><div id="rows"></div></section></main><script>
const data=__ROWS__;
function render(){rows.innerHTML=data.map((r,i)=>`<div class="row data-row" data-i="${i}"><div class="name cell">${r[0]}</div><div class="status cell">${r[1]}</div><div class="metric cell">${r[2]}</div><div class="change cell">${r[3]}</div><button class="action">열기</button></div>`).join('')};render();
window.configure=(stack,density,scale,policy)=>{document.documentElement.style.setProperty('--stack',stack);document.documentElement.style.setProperty('--fs',scale);document.body.dataset.density=density;document.body.dataset.scale=String(scale);document.body.dataset.policy=policy};
window.measure=()=>{const rs=[...document.querySelectorAll('.data-row')],names=[...document.querySelectorAll('.name')];const lineInfo=names.map(el=>{const cs=getComputedStyle(el),fs=parseFloat(cs.fontSize),lh=cs.lineHeight==='normal'?fs*1.2:parseFloat(cs.lineHeight),h=el.getBoundingClientRect().height;return {lines:Math.max(1,Math.round(h/lh)),height:h}});const hs=rs.map(r=>r.getBoundingClientRect().height);return {scrollRatio:document.documentElement.scrollHeight/document.documentElement.clientHeight,avgRowHeight:hs.reduce((a,b)=>a+b,0)/hs.length,wrappedNames:lineInfo.filter(x=>x.lines>1).length,targetLongLabelLines:lineInfo[5].lines,horizontalOverflow:document.documentElement.scrollWidth>document.documentElement.clientWidth};};
</script></body></html>'''.replace("__ROWS__", json.dumps(ROWS, ensure_ascii=False))


async def direct_widths(page):
    await page.set_content('<!doctype html><meta charset="utf-8"><span id="t" style="font-size:20px;white-space:nowrap"></span>')
    output = {}
    for name, stack in STACKS.items():
        width = await page.evaluate(
            "([stack,text])=>{const e=document.querySelector('#t');e.style.fontFamily=stack;e.textContent=text;return e.getBoundingClientRect().width}",
            [stack, LONG_LABEL],
        )
        threshold = None
        for w in range(430, 521):
            lines = await page.evaluate(
                "([stack,text,w])=>{const e=document.querySelector('#t');e.style.fontFamily=stack;e.style.whiteSpace='normal';e.style.lineHeight='24px';e.style.width=w+'px';e.textContent=text;return Math.round(e.getBoundingClientRect().height/24)}",
                [stack, LONG_LABEL, w],
            )
            if lines == 1:
                threshold = w
                break
        output[name] = {"width": width, "oneLineThreshold": threshold}
    return output


async def layout_matrix(page):
    await page.set_content(HTML)
    out = []
    for policy in ["base", "robust"]:
        for width, height in [(500, 800), (390, 844)]:
            await page.set_viewport_size({"width": width, "height": height})
            for scale in [1.25, 2]:
                for density in ["compact", "intermediate", "spacious"]:
                    for stack_name, stack in STACKS.items():
                        await page.evaluate("([s,d,f,p])=>configure(s,d,f,p)", [stack, density, scale, policy])
                        metrics = await page.evaluate("measure()")
                        metrics.update({"policy": policy, "width": width, "height": height, "scale": scale, "density": density, "stack": stack_name})
                        out.append(metrics)
    return out


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
        page = await browser.new_page(viewport={"width": 800, "height": 600})
        result = {
            "study": "L003",
            "browser": await browser.version(),
            "directWidths": await direct_widths(page),
            "matrix": await layout_matrix(page),
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
