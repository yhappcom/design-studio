from playwright.sync_api import sync_playwright
from pathlib import Path
import json
from PIL import Image
from io import BytesIO
import numpy as np

HTML=Path("L006-layer-ownership-specimen.html").read_text()
CH="/usr/bin/chromium"
OUT=Path("L006-layer-ownership-results-summary.json")

def shot(page,sel):
    return page.locator(sel).screenshot()

def diff(a,b):
    A=np.asarray(Image.open(BytesIO(a)).convert("RGB"))
    B=np.asarray(Image.open(BytesIO(b)).convert("RGB"))
    return float(np.any(A!=B,axis=2).mean())

def center(page,sel):
    b=page.locator(sel).bounding_box()
    return b["x"]+b["width"]/2,b["y"]+b["height"]/2

with sync_playwright() as p:
    br=p.chromium.launch(headless=True,executable_path=CH)
    page=br.new_page(viewport={"width":1100,"height":1100},device_scale_factor=1)
    page.set_content(HTML)
    out={"chromium":br.version,"pairs":{},"assertions":[]}

    for n,a,b,la,lb in [
        ("popover","#popBroken","#popRevised","#pbLayer","#prLayer"),
        ("sticky","#stickyBroken","#stickyRevised","#sbLayer","#srLayer"),
        ("sheet","#sheetBroken","#sheetRevised","#shbLayer","#shrLayer")]:
        out["pairs"][n]={
            "workspace_diff":diff(shot(page,a+" .workspace"),shot(page,b+" .workspace")),
            "layer_diff":diff(shot(page,la),shot(page,lb))
        }

    for n,c,l in [
        ("popover_broken","#popBroken","#pbLayer .fgAction"),
        ("popover_revised","#popRevised","#prLayer .fgAction"),
        ("sticky_broken","#stickyBroken","#sbLayer .fgAction"),
        ("sticky_revised","#stickyRevised","#srLayer .fgAction"),
        ("sheet_broken","#sheetBroken","#shbLayer .fgAction"),
        ("sheet_revised","#sheetRevised","#shrLayer .fgAction")]:
        x,y=center(page,l)
        out[n+"_hit"]=page.evaluate("([x,y])=>document.elementFromPoint(x,y)?.className",[x,y])
        page.mouse.click(x,y)
        out[n+"_counts"]=page.evaluate("(s)=>{const c=document.querySelector(s);return {bg:+c.dataset.bg,fg:+c.dataset.fg}}",c)

    page.locator("#shbLayer .fgAction").focus()
    seq=[page.evaluate("()=>document.activeElement.className")]
    for key in ("Shift+Tab","Shift+Tab"):
        page.keyboard.press(key)
        seq.append(page.evaluate("()=>document.activeElement.className"))
    out["sheet_broken_tab_sequence"]=seq
    out["sheet_broken_escaped_to_background"]=any(x in ("bgAction sheetbg","bgInput") for x in seq[1:])

    page.locator("#shrLayer .fgAction").focus()
    seq=[page.evaluate("()=>document.activeElement.className")]
    for key in ("Shift+Tab","Shift+Tab","Tab","Tab","Tab","Tab"):
        page.keyboard.press(key)
        seq.append(page.evaluate("()=>document.activeElement.className"))
    out["sheet_revised_tab_sequence"]=seq
    out["sheet_revised_focus_contained"]=all(x in ("fgAction","cancel") for x in seq)
    out["sheet_revised_bg_inert"]=page.evaluate("()=>sheetRevised.querySelector('.sheetBg').inert")

    def A(name,cond):
        out["assertions"].append({"name":name,"pass":bool(cond)})

    for n,v in out["pairs"].items():
        A(n+"_workspace_pixels_equal",v["workspace_diff"]==0)
        A(n+"_layer_pixels_equal",v["layer_diff"]==0)

    A("popover_broken_activates_background",out["popover_broken_counts"]=={"bg":1,"fg":0})
    A("popover_revised_activates_foreground",out["popover_revised_counts"]=={"bg":0,"fg":1})
    A("sticky_broken_activates_background",out["sticky_broken_counts"]=={"bg":1,"fg":0})
    A("sticky_revised_activates_foreground",out["sticky_revised_counts"]=={"bg":0,"fg":1})
    A("sheet_broken_activates_background",out["sheet_broken_counts"]=={"bg":1,"fg":0})
    A("sheet_revised_activates_foreground",out["sheet_revised_counts"]=={"bg":0,"fg":1})
    A("sheet_broken_keyboard_escapes",out["sheet_broken_escaped_to_background"])
    A("sheet_revised_background_inert",out["sheet_revised_bg_inert"])
    A("sheet_revised_keyboard_contained",out["sheet_revised_focus_contained"])

    out["pass_count"]=sum(a["pass"] for a in out["assertions"])
    out["total"]=len(out["assertions"])
    OUT.write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    br.close()
