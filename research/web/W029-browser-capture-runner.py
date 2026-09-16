#!/usr/bin/env python3
"""W029 browser execution runner for W027/W028.
Requires Playwright Python and at least one installed browser engine.
Produces JSON evidence only from executed browser sessions; no synthetic PASS data.
"""
import json, time, pathlib, subprocess, sys
from contextlib import contextmanager

ROOT=pathlib.Path(__file__).resolve().parent
OUT=ROOT/'W029-browser-capture-results.json'
BACKEND=ROOT/'W028-controlled-origin-backend.py'
BASE='http://127.0.0.1:8028/w027'

@contextmanager
def backend():
    p=subprocess.Popen([sys.executable,str(BACKEND)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    time.sleep(.5)
    try: yield
    finally: p.terminate(); p.wait(timeout=3)

def rect(el):
    return el.bounding_box()

def run_engine(pw,name):
    engine=getattr(pw,name)
    browser=engine.launch(headless=True)
    results=[]
    try:
        for width,height,label in [(1280,800,'baseline'),(320,640,'narrow')]:
            page=browser.new_page(viewport={'width':width,'height':height})
            page.goto(BASE+'?route=start',wait_until='networkidle')
            page.locator('#review').click(); page.go_back(); page.go_forward()
            history_ok='route=review' in page.url
            for mode in ['confirm','reject','drop-before','drop-after']:
                page.goto(BASE,wait_until='networkidle')
                page.locator('#mode').select_option(mode)
                page.locator('#dispatch').click()
                page.wait_for_timeout(150)
                immediate=page.locator('#state').inner_text()
                page.locator('#reconcile').click(); page.wait_for_timeout(150)
                reconciled=page.locator('#state').inner_text()
                dispatch=page.locator('#dispatch'); dispatch.focus()
                d=rect(dispatch); s=rect(page.locator('.sticky'))
                overlap=bool(d and s and d['y']+d['height']>s['y'] and d['y']<s['y']+s['height'])
                body_width=page.evaluate('document.documentElement.scrollWidth')
                results.append({'engine':name,'viewport':label,'width':width,'mode':mode,'immediate':immediate,'reconciled':reconciled,'history_ok':history_ok,'scrollWidth':body_width,'horizontalOverflow':body_width>width,'focusedDispatchStickyOverlap':overlap})
            page.close()
    finally: browser.close()
    return results

def main():
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        raise SystemExit('BLOCKED: Playwright Python unavailable: '+repr(e))
    evidence={'schema':'W029-v1','generatedAt':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'runs':[],'blockedEngines':[]}
    with backend(), sync_playwright() as pw:
        for name in ['chromium','firefox','webkit']:
            try: evidence['runs'].extend(run_engine(pw,name))
            except Exception as e: evidence['blockedEngines'].append({'engine':name,'error':repr(e)})
    OUT.write_text(json.dumps(evidence,indent=2),encoding='utf-8')
    print(json.dumps({'runs':len(evidence['runs']),'blockedEngines':evidence['blockedEngines']},indent=2))
if __name__=='__main__': main()
