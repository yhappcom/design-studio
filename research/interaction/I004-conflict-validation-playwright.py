"""I004 controlled concurrent-edit conflict state-machine validation.

This is interaction evidence, not a production sync/database implementation.
"""
import asyncio, json
from playwright.async_api import async_playwright

HTML = r'''<!doctype html><meta charset="utf-8"><style>
body{font-family:system-ui,sans-serif;margin:24px;max-width:760px}button,input,textarea{font:inherit}input,textarea{display:block;width:100%;margin:.35rem 0 1rem}.panel{border:1px solid #999;padding:12px;margin-top:12px}.conflict[hidden]{display:none}.actions{display:flex;gap:8px;flex-wrap:wrap}.status{min-height:1.5em}
</style><main><h1>Concurrent edit specimen</h1><div class="status" id="status" role="status"></div><label>Title<input id="title"></label><label>Notes<textarea id="notes"></textarea></label><div class="actions"><button id="save">Save</button><button id="refresh">Refresh</button></div><section id="conflict" class="panel conflict" hidden tabindex="-1"><h2>Conflict detected</h2><div id="conflictText"></div><div class="actions"><button id="autoMerge" hidden>Merge non-overlapping changes</button><button id="useMine" hidden>Use my version</button><button id="useRemote" hidden>Use remote version</button><button id="keepCopy" hidden>Keep my changes as a new record</button><button id="discard" hidden>Discard my changes</button></div></section></main><script>
let server,client,base,serverCopy;
const $=id=>document.getElementById(id);
function resetServer(){server={id:'r1',version:1,deleted:false,title:'Flight 101',notes:'Routine'};serverCopy=null;loadClient();}
function loadClient(){base=structuredClone(server);client=structuredClone(server);$('title').value=client.title;$('notes').value=client.notes;$('conflict').hidden=true;$('status').textContent='';}
function localFromUI(){client.title=$('title').value;client.notes=$('notes').value;}
function changedFields(a,b){return ['title','notes'].filter(k=>a[k]!==b[k]);}
function remoteUpdate(patch){server={...server,...patch,version:server.version+1};}
function remoteDelete(){server={...server,deleted:true,version:server.version+1};}
function naiveWholeSave(){localFromUI();server={...server,title:client.title,notes:client.notes,deleted:false,version:server.version+1};base=structuredClone(server);$('status').textContent='Saved';}
function conditionalSave(){localFromUI();if(server.version===base.version&&!server.deleted){server={...server,title:client.title,notes:client.notes,version:server.version+1};base=structuredClone(server);$('status').textContent='Saved';return true;}showConflict();return false;}
function showConflict(){const localChanges=changedFields(base,client);const remoteChanges=server.deleted?['__deleted__']:changedFields(base,server);const overlap=localChanges.filter(x=>remoteChanges.includes(x));$('conflict').hidden=false;for(const id of ['autoMerge','useMine','useRemote','keepCopy','discard'])$(id).hidden=true;
 if(server.deleted){$('conflictText').textContent='This record was deleted elsewhere. Your unsaved draft is preserved.';$('keepCopy').hidden=false;$('discard').hidden=false;}
 else if(overlap.length===0){$('conflictText').textContent='Remote and local changes affect different fields.';$('autoMerge').hidden=false;}
 else{$('conflictText').textContent=`Both versions changed: ${overlap.join(', ')}. Remote title: ${server.title}. Your title: ${client.title}.`;$('useMine').hidden=false;$('useRemote').hidden=false;}
 $('conflict').focus();}
$('save').onclick=()=>conditionalSave();$('refresh').onclick=()=>loadClient();
$('autoMerge').onclick=()=>{localFromUI();const localChanges=changedFields(base,client);const merged=structuredClone(server);for(const k of localChanges)merged[k]=client[k];server={...merged,version:server.version+1};base=structuredClone(server);client=structuredClone(server);$('title').value=client.title;$('notes').value=client.notes;$('conflict').hidden=true;$('status').textContent='Merged and saved';$('save').focus();};
$('useMine').onclick=()=>{localFromUI();server={...server,title:client.title,notes:client.notes,version:server.version+1};base=structuredClone(server);$('conflict').hidden=true;$('status').textContent='Your version saved';$('title').focus();};
$('useRemote').onclick=()=>{client=structuredClone(server);base=structuredClone(server);$('title').value=client.title;$('notes').value=client.notes;$('conflict').hidden=true;$('status').textContent='Remote version kept';$('title').focus();};
$('keepCopy').onclick=()=>{localFromUI();serverCopy={id:'r2',version:1,deleted:false,title:client.title,notes:client.notes};$('conflict').hidden=true;$('status').textContent='Draft kept as a new record';$('title').focus();};
$('discard').onclick=()=>{client=structuredClone(server);base=structuredClone(server);$('conflict').hidden=true;$('status').textContent='Draft discarded';$('save').focus();};
window.api={resetServer,loadClient,remoteUpdate,remoteDelete,naiveWholeSave,conditionalSave,get:()=>({server:structuredClone(server),client:structuredClone(client),base:structuredClone(base),copy:serverCopy?structuredClone(serverCopy):null})};resetServer();
</script>'''

async def main():
    result={"study":"I004","assertions":[]}
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,executable_path="/usr/bin/chromium")
        page=await browser.new_page()
        await page.set_content(HTML)
        async def check(name, condition, detail=None):
            result["assertions"].append({"name":name,"pass":bool(condition),"detail":detail})

        # Naive lost update.
        await page.evaluate("""server={id:'r1',version:2,deleted:false,title:'Flight 101A',notes:'Routine'};base={id:'r1',version:1,deleted:false,title:'Flight 101',notes:'Routine'};client=structuredClone(base);title.value=client.title;notes.value='Weather diversion';api.naiveWholeSave();""")
        state=await page.evaluate("api.get()")
        await check("naive whole-record save loses concurrent title",state["server"]["title"]=="Flight 101" and state["server"]["notes"]=="Weather diversion",state["server"])

        # Disjoint conflict and merge.
        await page.evaluate("api.resetServer();api.remoteUpdate({title:'Flight 101A'})")
        await page.fill("#notes","Weather diversion")
        await page.click("#save")
        await check("stale save detects conflict",not await page.is_hidden("#conflict"))
        await check("local draft preserved on conflict",await page.input_value("#notes")=="Weather diversion")
        await check("disjoint conflict exposes merge not overwrite choices",(not await page.is_hidden("#autoMerge")) and await page.is_hidden("#useMine"))
        await page.click("#autoMerge")
        state=await page.evaluate("api.get()")
        await check("disjoint auto-merge preserves both changes",state["server"]["title"]=="Flight 101A" and state["server"]["notes"]=="Weather diversion",state["server"])
        await check("post-merge focus returns to Save",await page.evaluate("document.activeElement.id")=="save")

        # Same field conflict.
        await page.evaluate("api.resetServer();api.remoteUpdate({title:'Flight 101A'})")
        await page.fill("#title","Flight 101B")
        await page.click("#save")
        state=await page.evaluate("api.get()")
        await check("same-field conflict does not auto-write",state["server"]["title"]=="Flight 101A" and state["server"]["version"]==2,state["server"])
        await check("same-field conflict preserves local value",await page.input_value("#title")=="Flight 101B")
        text=await page.text_content("#conflictText")
        await check("same-field resolution exposes both versions","Flight 101A" in text and "Flight 101B" in text,text)
        await check("blocking conflict focuses conflict region",await page.evaluate("document.activeElement.id")=="conflict")
        await page.click("#useMine")
        state=await page.evaluate("api.get()")
        await check("explicit local resolution commits against current version",state["server"]["title"]=="Flight 101B" and state["server"]["version"]==3,state["server"])
        await check("resolution focus returns to edited field",await page.evaluate("document.activeElement.id")=="title")

        # Delete vs edit.
        await page.evaluate("api.resetServer();api.remoteDelete()")
        await page.fill("#notes","Important offline note")
        await page.click("#save")
        await check("delete-vs-edit is distinguished from field conflict","deleted elsewhere" in (await page.text_content("#conflictText")))
        await check("delete conflict preserves unsaved draft",await page.input_value("#notes")=="Important offline note")
        await check("delete conflict offers keep-copy",not await page.is_hidden("#keepCopy"))
        await page.click("#keepCopy")
        state=await page.evaluate("api.get()")
        await check("keep-copy creates separate identity and leaves original deleted",state["copy"]["id"]=="r2" and state["copy"]["notes"]=="Important offline note" and state["server"]["deleted"],{"server":state["server"],"copy":state["copy"]})
        await check("keep-copy restores focus to retained draft field",await page.evaluate("document.activeElement.id")=="title")

        result["pass_count"]=sum(x["pass"] for x in result["assertions"])
        result["total"]=len(result["assertions"])
        result["chromium"]=browser.version
        await browser.close()
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":
    asyncio.run(main())
