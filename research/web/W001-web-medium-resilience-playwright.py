from pathlib import Path
import json
import shutil
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
html = (HERE / "W001-web-medium-resilience-specimen.html").read_text(encoding="utf-8")
viewports = [1280, 768, 320]
results = []

with sync_playwright() as p:
    launch_kwargs = {"headless": True}
    system_chromium = shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")
    if system_chromium:
        launch_kwargs.update(executable_path=system_chromium, args=["--no-sandbox"])
    browser = p.chromium.launch(**launch_kwargs)

    for width in viewports:
        page = browser.new_page(viewport={"width": width, "height": 900})
        # set_content is intentional: the research runner may prohibit local HTTP/file navigation.
        page.set_content(html, wait_until="load")
        for variant in ("fixed", "fluid"):
            page.locator("body").evaluate("(b, v) => b.dataset.test = v", variant)
            data = page.locator(f"#{variant}").evaluate("""(root) => {
              const shell = root.querySelector('.shell');
              const nav = root.querySelector('nav');
              const hero = root.querySelector('.hero');
              const actions = [...root.querySelectorAll('.actions a')];
              const sr = shell.getBoundingClientRect();
              const viewportWidth = document.documentElement.clientWidth;
              return {
                shell_left: Math.round(sr.left * 100) / 100,
                shell_right: Math.round(sr.right * 100) / 100,
                shell_width: Math.round(sr.width * 100) / 100,
                shell_overflows_viewport: sr.right > viewportWidth + 0.5 || sr.left < -0.5,
                document_horizontal_overflow: document.documentElement.scrollWidth > viewportWidth + 1,
                nav_overflow: nav.scrollWidth > nav.clientWidth + 1,
                hero_overflow: hero.scrollWidth > hero.clientWidth + 1,
                actions_in_viewport: actions.every(a => {
                  const r = a.getBoundingClientRect();
                  return r.left >= -0.5 && r.right <= viewportWidth + 0.5;
                }),
                action_count: actions.length,
                max_action_right: Math.round(Math.max(...actions.map(a => a.getBoundingClientRect().right)) * 100) / 100,
                viewport_width: viewportWidth
              };
            }""")
            data["variant"] = variant
            data["requested_viewport"] = width
            results.append(data)
        page.close()

    # Semantic/unstyled transfer check at narrow width.
    page = browser.new_page(viewport={"width": 320, "height": 900})
    page.set_content(html, wait_until="load")
    page.locator("style").evaluate_all("els => els.forEach(e => e.remove())")
    styleless = page.locator("body").evaluate("""(body) => {
      const links = [...body.querySelectorAll('a')];
      const headings = [...body.querySelectorAll('h2,h3')];
      return {
        horizontal_overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
        link_count: links.length,
        visible_link_count: links.filter(a => { const r=a.getBoundingClientRect(); return r.width>0 && r.height>0; }).length,
        heading_count: headings.length,
        visible_heading_count: headings.filter(h => { const r=h.getBoundingClientRect(); return r.width>0 && r.height>0; }).length
      };
    }""")
    page.close()
    browser.close()

summary = {
    "engine": "Chromium via Playwright set_content",
    "conditions": results,
    "styleless_320": styleless,
    "bounded_assertions": {
        "fixed_overflows_at_768": next(r for r in results if r["variant"] == "fixed" and r["requested_viewport"] == 768)["shell_overflows_viewport"],
        "fixed_overflows_at_320": next(r for r in results if r["variant"] == "fixed" and r["requested_viewport"] == 320)["shell_overflows_viewport"],
        "fluid_fits_1280": not next(r for r in results if r["variant"] == "fluid" and r["requested_viewport"] == 1280)["shell_overflows_viewport"],
        "fluid_fits_768": not next(r for r in results if r["variant"] == "fluid" and r["requested_viewport"] == 768)["shell_overflows_viewport"],
        "fluid_fits_320": not next(r for r in results if r["variant"] == "fluid" and r["requested_viewport"] == 320)["shell_overflows_viewport"],
        "fluid_actions_reachable_320": next(r for r in results if r["variant"] == "fluid" and r["requested_viewport"] == 320)["actions_in_viewport"],
        "fixed_actions_not_all_reachable_320": not next(r for r in results if r["variant"] == "fixed" and r["requested_viewport"] == 320)["actions_in_viewport"],
        "unstyled_linearizes_without_horizontal_overflow": not styleless["horizontal_overflow"],
        "unstyled_keeps_all_links_and_headings_visible": styleless["visible_link_count"] == styleless["link_count"] and styleless["visible_heading_count"] == styleless["heading_count"]
    }
}

(HERE / "W001-web-medium-resilience-results.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(json.dumps(summary, indent=2, ensure_ascii=False))
