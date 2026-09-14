from playwright.sync_api import sync_playwright
import json, pathlib, shutil
html=pathlib.Path(__file__).with_name('I002-async-validation-specimen.html').read_text()
results=[]
def check(name, cond, detail=''):
    results.append({'name':name,'pass':bool(cond),'detail':detail})
browser_path = shutil.which('chromium') or shutil.which('chromium-browser') or shutil.which('google-chrome')
if not browser_path:
    raise RuntimeError('No Chromium/Chrome executable found')
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,executable_path=browser_path,args=['--no-sandbox']);page=b.new_page();page.set_content(html)
    # optimistic reversible action
    page.focus('#fav');page.click('#fav');page.wait_for_timeout(10);s=page.evaluate('inspect()')
    check('optimistic immediate visual',s['favPressed']=='true',str(s));check('pending preserves focus',s['active']=='fav',str(s));check('aria busy while saving',s['favBusy']=='true',str(s))
    # repeated activation while pending ignored
    page.click('#fav', force=True);page.wait_for_timeout(100);s=page.evaluate('inspect()');check('duplicate favorite ignored',s['favReq']==1,str(s));check('failed optimistic action rolled back',s['favPressed']=='false' and not s['favRetryHidden'],str(s))
    page.click('#favRetry');page.wait_for_timeout(100);s=page.evaluate('inspect()');check('retry safe favorite succeeds',s['favReq']==2 and s['favPressed']=='true' and s['favStatus']=='Favorite saved.',str(s));check('retry completion restores focus',s['active']=='fav',str(s))
    # high consequence ambiguous outcome
    page.focus('#transfer');page.click('#transfer');page.wait_for_timeout(10);page.click('#transfer', force=True);page.wait_for_timeout(100);s=page.evaluate('inspect()')
    check('duplicate transfer guarded',s['transferCommitCount']==1,str(s));check('lost response -> outcome unknown',s['transferOutcome']=='unknown',str(s));check('unsafe retry not exposed',s['transferRetryHidden'] is True,str(s));check('check status exposed',s['checkHidden'] is False,str(s));check('operation id exists',bool(s['transferOperationId']),str(s))
    page.click('#check');page.wait_for_timeout(80);s=page.evaluate('inspect()');check('status reconciliation confirms',s['transferOutcome']=='confirmed' and s['transferStatus']=='Transfer confirmed.',str(s));check('reconciliation restores focus',s['active']=='transfer',str(s));check('no duplicate commit after reconciliation',s['transferCommitCount']==1,str(s))
    # determinate cancel contract
    page.focus('#exportBtn');page.click('#exportBtn');page.wait_for_timeout(55);s=page.evaluate('inspect()');check('export is determinate and busy',s['exportRunning'] and 0<s['exportValue']<100 and s['exportBusy']=='true',str(s));page.click('#cancel');cancelled=page.evaluate('inspect()');page.wait_for_timeout(180);s=page.evaluate('inspect()');check('cancel actually stops operation',not s['exportRunning'] and s['exportText']=='Export canceled.' and s['exportValue']==cancelled['exportValue'],str(s));check('cancel restores focus',s['active']=='exportBtn',str(s))
    check('status regions did not steal focus',s['active']!='favStatus' and s['active']!='transferStatus' and s['active']!='exportStatus',str(s))
    b.close()
pathlib.Path(__file__).with_name('I002-async-validation-results.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2));print('PASS',sum(r['pass'] for r in results),'/',len(results))
