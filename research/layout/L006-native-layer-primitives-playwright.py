from playwright.sync_api import sync_playwright
from pathlib import Path
import json

HTML=Path("L006-native-layer-primitives-specimen.html").read_text()
OUT=Path("L006-native-layer-primitives-results.json")
CH="/usr/bin/chromium"

def center(page,sel):
    b=page.locator(sel).bounding_box()
    return b["x"]+b["width"]/2,b["y"]+b["height"]/2

with sync_playwright() as p:
    br=p.chromium.launch(headless=True,executable_path=CH)
    page=br.new_page(viewport={"width":900,"height":700})
    page.set_content(HTML)
    out={"chromium":br.version,"assertions":[]}

    def A(name,cond):
        out["assertions"].append({"name":name,"pass":bool(cond)})

    page.click("#openPop")
    out["popover_open"]=page.locator("#pop").evaluate("e=>e.matches(':popover-open')")
    page.locator("#pop").evaluate("e=>{e.style.position='fixed';e.style.margin='0';e.style.left='180px';e.style.top='120px'}")
    bx,by=center(page,"#bgDanger")
    page.locator("#popAction").evaluate("(e,p)=>{const r=e.parentElement.getBoundingClientRect();e.style.left=(p.x-r.left-50)+'px';e.style.top=(p.y-r.top-20)+'px'}",{"x":bx,"y":by})
    out["popover_overlap_hit"]=page.evaluate("([x,y])=>document.elementFromPoint(x,y)?.id",[bx,by])
    page.mouse.click(bx,by)
    out["counts_after_pop_overlap"]=page.evaluate("()=>counts")
    out["popover_background_outside_interactive"]=page.evaluate("()=>!document.querySelector('.stage').inert")
    page.locator("#pop").evaluate("e=>e.hidePopover()")

    page.locator("#openDlg").focus()
    page.click("#openDlg")
    out["dialog_open"]=page.locator("#dlg").evaluate("e=>e.open")
    out["dialog_in_top_layer"]=page.locator("#dlg").evaluate("e=>getComputedStyle(e).display!='none' && e.matches(':modal')")

    bx,by=center(page,"#bgDanger")
    before=page.evaluate("()=>counts.bg")
    page.mouse.click(bx,by)
    after=page.evaluate("()=>counts.bg")
    out["modal_background_click_blocked"]=(before==after)

    page.locator("#dlgPrimary").focus()
    seq=[]
    for key in ["Shift+Tab","Shift+Tab","Tab","Tab","Tab","Tab","Tab"]:
        seq.append(page.evaluate("()=>document.activeElement.id"))
        page.keyboard.press(key)
    seq.append(page.evaluate("()=>document.activeElement.id"))
    out["dialog_focus_sequence"]=seq
    out["dialog_background_controls_not_reached"]=all(x not in {"openPop","openDlg","bgDanger"} for x in seq)
    out["dialog_focus_strictly_inside"]=all(x in {"dlgTitle","dlgPrimary","dlgClose","openNested"} for x in seq)

    page.click("#openNested")
    out["nested_popover_open"]=page.locator("#insidePop").evaluate("e=>e.matches(':popover-open')")
    nx,ny=center(page,"#nestedAction")
    out["nested_hit"]=page.evaluate("([x,y])=>document.elementFromPoint(x,y)?.id",[nx,ny])
    page.mouse.click(nx,ny)
    out["nested_count"]=page.evaluate("()=>counts.nested")
    page.locator("#insidePop").evaluate("e=>e.hidePopover()")

    page.click("#dlgClose")
    out["dialog_closed"]=not page.locator("#dlg").evaluate("e=>e.open")
    out["focus_after_close"]=page.evaluate("()=>document.activeElement.id")

    A("popover_open",out["popover_open"])
    A("popover_overlap_owns_hit",out["popover_overlap_hit"]=="popAction")
    A("popover_overlap_activates_foreground",out["counts_after_pop_overlap"]["pop"]==1 and out["counts_after_pop_overlap"]["bg"]==0)
    A("nonmodal_popover_does_not_inert_page",out["popover_background_outside_interactive"])
    A("dialog_open",out["dialog_open"])
    A("dialog_modal_pseudo_class",out["dialog_in_top_layer"])
    A("dialog_blocks_background_click",out["modal_background_click_blocked"])
    A("dialog_background_controls_not_reached",out["dialog_background_controls_not_reached"])
    A("nested_popover_open_inside_modal",out["nested_popover_open"])
    A("nested_popover_topmost_hit",out["nested_hit"]=="nestedAction")
    A("nested_popover_action_fires",out["nested_count"]==1)
    A("dialog_closes",out["dialog_closed"])
    A("dialog_focus_returns_to_invoker",out["focus_after_close"]=="openDlg")

    out["pass_count"]=sum(x["pass"] for x in out["assertions"])
    out["total"]=len(out["assertions"])
    OUT.write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    br.close()
