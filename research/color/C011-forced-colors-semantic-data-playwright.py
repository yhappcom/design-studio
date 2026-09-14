from __future__ import annotations
import io, json
from pathlib import Path
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

HERE=Path(__file__).resolve().parent
HTML=HERE/'C011-forced-colors-semantic-data-specimen.html'
OUT=HERE/'C011-forced-colors-semantic-data-results.json'
AUTHOR=[(214,39,40),(44,160,44),(31,119,180),(148,103,189)]

def all_styles(page, sel):
    return page.eval_on_selector_all(sel, '''els=>els.map(e=>{const s=getComputedStyle(e);return {text:e.textContent.trim(),color:s.color,backgroundColor:s.backgroundColor,borderColor:s.borderColor,stroke:s.stroke,strokeWidth:s.strokeWidth,strokeDasharray:s.strokeDasharray,fill:s.fill,forcedColorAdjust:s.forcedColorAdjust,visibility:s.visibility,display:s.display}})''')

def one_style(page, sel):
    return page.eval_on_selector(sel, '''e=>{const s=getComputedStyle(e);return {color:s.color,backgroundColor:s.backgroundColor,borderColor:s.borderColor,outlineStyle:s.outlineStyle,outlineWidth:s.outlineWidth,outlineColor:s.outlineColor,boxShadow:s.boxShadow,forcedColorAdjust:s.forcedColorAdjust}}''')

def raster_counts(page, sel):
    png=page.locator(sel).screenshot()
    arr=np.asarray(Image.open(io.BytesIO(png)).convert('RGB'))
    return {'%d,%d,%d'%c:int(np.all(arr==c,axis=2).sum()) for c in AUTHOR}

def distinct(xs): return len(set(xs))

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium')
    page=browser.new_page(viewport={'width':1200,'height':720},device_scale_factor=1)
    page.set_content(HTML.read_text(),wait_until='load')
    page.focus('#naive-focus')
    normal={
      'naiveStatus':all_styles(page,'#naive-status .chip'),
      'robustStatus':all_styles(page,'#robust-status .chip'),
      'naiveDefaultSeries':all_styles(page,'#naive svg:not(.force-auto) .series'),
      'naiveAutoSeries':all_styles(page,'#naive-auto-svg .series'),
      'robustSeries':all_styles(page,'#robust svg .series'),
      'robustLabels':all_styles(page,'#robust svg .label'),
      'naiveFocus':one_style(page,'#naive-focus'),'robustFocus':one_style(page,'#robust-focus'),'optout':one_style(page,'#optout')}
    normalRaster={'default':raster_counts(page,'#naive svg:not(.force-auto)'),'auto':raster_counts(page,'#naive-auto-svg'),'robust':raster_counts(page,'#robust svg')}

    page.emulate_media(forced_colors='active')
    page.focus('#naive-focus')
    naiveForcedFocus=one_style(page,'#naive-focus')
    page.focus('#robust-focus')
    forced={
      'forced':page.evaluate('matchMedia("(forced-colors: active)").matches'),
      'naiveStatus':all_styles(page,'#naive-status .chip'),
      'robustStatus':all_styles(page,'#robust-status .chip'),
      'naiveDefaultSeries':all_styles(page,'#naive svg:not(.force-auto) .series'),
      'naiveAutoSeries':all_styles(page,'#naive-auto-svg .series'),
      'robustSeries':all_styles(page,'#robust svg .series'),
      'robustLabels':all_styles(page,'#robust svg .label'),
      'robustFocus':one_style(page,'#robust-focus'),'optout':one_style(page,'#optout')}
    forcedRaster={'default':raster_counts(page,'#naive svg:not(.force-auto)'),'auto':raster_counts(page,'#naive-auto-svg'),'robust':raster_counts(page,'#robust svg')}

    A={}
    A['forced_media_active']=forced['forced'] is True
    A['naive_status_distinct_normally']=distinct([x['backgroundColor'] for x in normal['naiveStatus']])==3
    A['naive_status_collapses_forced']=distinct([x['backgroundColor'] for x in forced['naiveStatus']])==1
    A['robust_status_visible_labels']=[x['text'] for x in forced['robustStatus']]==['Pending','Failed','Confirmed']
    A['robust_status_structural_borders_survive']=all(x['borderColor']!='rgba(0, 0, 0, 0)' for x in forced['robustStatus'])
    A['naive_default_svg_series_distinct_normally']=distinct([x['stroke'] for x in normal['naiveDefaultSeries']])==4
    A['naive_default_svg_preserves_author_colors_forced']=all(v>0 for v in forcedRaster['default'].values())
    A['naive_default_svg_uses_preserve_parent_color']=all(x['forcedColorAdjust']=='preserve-parent-color' for x in forced['naiveDefaultSeries'])
    A['naive_auto_svg_series_distinct_normally']=distinct([x['stroke'] for x in normal['naiveAutoSeries']])==4
    A['naive_auto_svg_author_colors_removed_forced']=all(v==0 for v in forcedRaster['auto'].values())
    A['robust_series_have_four_dash_patterns']=distinct([x['strokeDasharray'] for x in forced['robustSeries']])==4
    A['robust_selected_series_keeps_extra_width']=float(forced['robustSeries'][2]['strokeWidth'].replace('px',''))>float(forced['robustSeries'][0]['strokeWidth'].replace('px',''))
    A['robust_direct_labels_visible']=all(x['display']!='none' and x['visibility']!='hidden' for x in forced['robustLabels'])
    A['naive_focus_shadow_exists_normal']=normal['naiveFocus']['boxShadow']!='none'
    A['naive_focus_shadow_removed_forced']=naiveForcedFocus['boxShadow']=='none'
    A['naive_focus_no_outline_fallback']=naiveForcedFocus['outlineStyle']=='none' or naiveForcedFocus['outlineWidth']=='0px'
    A['robust_focus_outline_survives']=forced['robustFocus']['outlineStyle']!='none' and forced['robustFocus']['outlineWidth']!='0px'
    A['optout_preserves_authored_policy']=forced['optout']['forcedColorAdjust']=='none'
    A['optout_color_not_forced_to_canvastext']=forced['optout']['color']==normal['optout']['color']
    A['optout_background_not_forced_to_canvas']=forced['optout']['backgroundColor']==normal['optout']['backgroundColor']
    A['robust_svg_author_colors_removed_but_redundancy_survives']=all(v==0 for v in forcedRaster['robust'].values()) and distinct([x['strokeDasharray'] for x in forced['robustSeries']])==4

    result={'study':'C011','environment':{'engine':'Chromium','version':browser.version,'viewport':[1200,720],'dpr':1,'forced_colors':'Playwright emulation active'},
      'html_status':{'normal_backgrounds':[x['backgroundColor'] for x in normal['naiveStatus']],'forced_backgrounds':[x['backgroundColor'] for x in forced['naiveStatus']],'robust_visible_labels':[x['text'] for x in forced['robustStatus']]},
      'svg':{'default_path_forced_color_adjust':[x['forcedColorAdjust'] for x in forced['naiveDefaultSeries']],'default_forced_raster_authored_color_counts':forcedRaster['default'],'explicit_auto_forced_raster_authored_color_counts':forcedRaster['auto'],'robust_auto_forced_raster_authored_color_counts':forcedRaster['robust'],'robust_dash_patterns':[x['strokeDasharray'] for x in forced['robustSeries']],'robust_stroke_widths':[x['strokeWidth'] for x in forced['robustSeries']],'robust_labels':[x['text'] for x in forced['robustLabels']]},
      'focus':{'naive_normal_box_shadow':normal['naiveFocus']['boxShadow'],'naive_forced_box_shadow':naiveForcedFocus['boxShadow'],'naive_forced_outline':[naiveForcedFocus['outlineStyle'],naiveForcedFocus['outlineWidth']],'robust_forced_outline':[forced['robustFocus']['outlineStyle'],forced['robustFocus']['outlineWidth'],forced['robustFocus']['outlineColor']]},
      'optout':{'forced_color_adjust':forced['optout']['forcedColorAdjust'],'forced_color':forced['optout']['color'],'forced_background':forced['optout']['backgroundColor'],'normal_color':normal['optout']['color'],'normal_background':normal['optout']['backgroundColor']},
      'assertions':A,'pass_count':sum(A.values()),'assertion_count':len(A),
      'interpretation_boundaries':['Chromium forced-colors emulation is implementation evidence, not Windows High Contrast, Firefox, Safari, OS, AT or production-device proof.','For SVG, getComputedStyle can retain authored stroke values even when the forced used value is different; raster evidence is used to verify actual rendering.','Computed styles and screenshots show browser color replacement behavior; they do not establish human comprehension.','forced-color-adjust:none preserving authored colors does not imply accessibility and should not be a default escape hatch.','Dash, marker geometry, stroke width and direct labels are redundant channels in this specimen, not universal chart encodings.']}
    OUT.write_text(json.dumps(result,indent=2))
    assert result['pass_count']==result['assertion_count'], result
    print(json.dumps({'pass_count':result['pass_count'],'assertion_count':result['assertion_count']},indent=2))
    browser.close()
