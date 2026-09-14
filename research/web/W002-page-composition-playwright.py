import json
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML = Path(__file__).with_name('W002-page-composition-specimen.html').read_text(encoding='utf-8')
LONG = (
    'After-tax cumulative distribution recovery progress for a multi-portfolio household account with pending adjustments / '
    '세후 누적 분배금 원금회수 진행상태와 미정산 세금조정 내역을 포함한 장기 포트폴리오 요약'
)


def measure(page, width, text_scale=1.0, long_content=False):
    page.set_viewport_size({'width': width, 'height': 1000})
    page.set_content(HTML, wait_until='load')
    if text_scale != 1.0:
        page.evaluate("s => document.documentElement.style.fontSize = `${16*s}px`", text_scale)
        page.add_style_tag(content=f"body{{font-size:{16*text_scale}px}}")
    if long_content:
        page.locator('#direction-a p').first.evaluate('(el, t) => el.textContent=t', LONG)
        page.locator('#direction-b p').first.evaluate('(el, t) => el.textContent=t', LONG)
    return page.evaluate('''() => {
      const doc = document.documentElement;
      const ws = document.querySelector('.workspace');
      const wsKids = [...ws.children].map(e => e.getBoundingClientRect());
      const tw = document.querySelector('.table-wrap');
      const table = tw.querySelector('table');
      const focusables = [...document.querySelectorAll('button,[tabindex="0"]')].map(e => ({tag:e.tagName, text:(e.textContent||'').trim().slice(0,40), top:e.getBoundingClientRect().top}));
      return {
        viewport: innerWidth,
        docScrollWidth: doc.scrollWidth,
        docClientWidth: doc.clientWidth,
        documentHorizontalOverflow: doc.scrollWidth > doc.clientWidth + 1,
        workspaceColumns: getComputedStyle(ws).gridTemplateColumns,
        workspaceChildrenSameRow: Math.abs(wsKids[0].top-wsKids[1].top) < 2,
        tableWrapClientWidth: tw.clientWidth,
        tableScrollWidth: tw.scrollWidth,
        tableLocalOverflow: tw.scrollWidth > tw.clientWidth + 1,
        tableWidth: table.getBoundingClientRect().width,
        tableSemanticTag: table.tagName,
        headerCount: table.querySelectorAll('th').length,
        focusables,
        bodyFontPx: parseFloat(getComputedStyle(document.body).fontSize),
      };
    }''')


def assertions(m, *, expect_same_row, expect_local_overflow=False):
    return {
      'document_has_no_horizontal_overflow': not m['documentHorizontalOverflow'],
      'workspace_row_relation_expected': m['workspaceChildrenSameRow'] == expect_same_row,
      'local_table_overflow_expected': m['tableLocalOverflow'] == expect_local_overflow,
      'table_semantics_preserved': m['tableSemanticTag'] == 'TABLE' and m['headerCount'] == 8,
      'focus_order_source_consistent': [x['tag'] for x in m['focusables']] == ['BUTTON','BUTTON','DIV'],
    }


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True)
    page = browser.new_page()
    cases = []
    specs = [
      ('wide-1280', 1280, 1.0, False, True, False),
      ('threshold-768', 768, 1.0, False, True, True),
      ('narrow-320', 320, 1.0, False, False, True),
      ('narrow-320-long-bilingual', 320, 1.0, True, False, True),
      ('narrow-320-text-200pct', 320, 2.0, True, False, True),
    ]
    for name, width, scale, long_content, same_row, local_overflow in specs:
        measurements = measure(page, width, scale, long_content)
        checks = assertions(
            measurements,
            expect_same_row=same_row,
            expect_local_overflow=local_overflow,
        )
        cases.append({
            'name': name,
            'measurements': measurements,
            'assertions': checks,
            'pass': all(checks.values()),
        })
    out = {
        'engine': browser.version,
        'cases': cases,
        'summary': {
            'assertions_total': sum(len(c['assertions']) for c in cases),
            'assertions_passed': sum(sum(c['assertions'].values()) for c in cases),
            'cases_passed': sum(c['pass'] for c in cases),
            'cases_total': len(cases),
        },
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    Path(__file__).with_name('W002-page-composition-results.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
    )
    browser.close()
