# T006 — Production Outline Audit: Source Topology, Cubic→Quadratic Export, and Raster Transfer

Status: **FOUNDATION / PRACTICE + CRITIQUE — manually auditable outline subset, failure→revision, CFF/TTF export fidelity, and raster-transfer evidence established; family/interpolation/platform production validation still OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Reproducible source: `research/type/T006-production-outline-audit.py`  
Measured data: `research/type/T006-production-outline-results.json`  
Evidence artifact: `research/type/T006-production-outline-evidence.svg`

## Purpose

T002–T005 established that glyph form, source metrics, renderer behavior, numeric systems, and mixed-script fallback must be validated rather than inferred. The largest remaining Type-foundation gap was different: the studio still lacked a **small source subset whose outline topology itself was deliberately audited as production data**.

T006 asks:

> What must be true of editable source contours before the studio may trust an export, and what can still change when a technically clean cubic source is converted to CFF or TrueType outlines?

This is not a product font and not a brand proposal. The subset exists to practice production judgment on `H O n o` while keeping the geometry small enough to inspect point-by-point.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `research/type/003-stroke-contrast-bezier-optics.md`;
  - T002 raster redraw cycle;
  - T003 compiled renderer matrix;
  - T004 numeral/punctuation research font;
  - T005 Latin/Korean fallback study.
- Reusable finding:
  - vector validity and raster quality are separate gates;
  - missing extrema, wrong joins, or unstable source geometry cannot be repaired reliably by spacing or renderer assumptions;
  - export/runtime behavior must be measured after source decisions.
- Replication / challenge / transfer opportunity:
  - turn the earlier outline-quality theory into an explicit source audit plus cubic→quadratic export experiment.
- Dependency / overlap:
  - broader family spacing, interpolation, hinting, platform/browser validation, and multilingual coverage remain separate gates.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md` through C007;
  - `research/color/C006-semantic-token-transfer-two-contexts.md`;
  - `research/color/C007-fixed-geometry-color-density-salience.md`.
- Reusable finding:
  - actual rendered glyph coverage matters to foreground/background performance; nominal color values alone do not describe perceived text; C007 also shows that Color experiments need typography held fixed when isolating color-driven salience/density.
- Replication / challenge / transfer opportunity:
  - T006 provides another fixed-geometry renderer comparison that can later be composited into C006-style foreground/surface conditions or transferred into C007 while keeping geometry/type condition explicit.
- Dependency / overlap:
  - **Not materially relevant to source-topology acceptance itself after checking.** Color becomes relevant again at rendered-role validation.

### Layout / Interaction
- Evidence checked:
  - latest `progress/LAYOUT_STATUS.md`;
  - `research/layout/L004-tabular-numerals-dense-comparison-transfer.md`;
  - L003/L004 Type→Layout transfer summaries.
- Reusable finding:
  - font/runtime changes can alter intrinsic width, wrapping, and dense-data geometry even when the Layout policy is unchanged;
  - Layout has already shown that final Type behavior must be tested at the client/layout layer.
- Replication / challenge / transfer opportunity:
  - later ensure production outline/export revisions do not unexpectedly change metrics, width contracts, or compact rendering in L003/L004 contexts.
- Dependency / overlap:
  - T006 keeps advances fixed and does not claim a Layout result.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web owns final page/browser font loading, feature application, zoom, fallback, and device validation.
- Implementation / application validation opportunity:
  - compare CFF/TTF or production webfont builds in actual browser stacks after a real W study exists.
- Dependency / overlap:
  - no substantive `W###` result exists at T006 start; no browser claim is inferred.

### Other / cross-cutting / future specialist
- Evidence checked:
  - Google Fonts Outline Quality;
  - current Glyphs Handbook sections on editing paths, extrema, path direction, overlap removal, and export;
  - fontTools `cu2qu` documentation.
- Reusable finding:
  - contour direction, extrema, closed paths, non-redundant geometry, and export testing are production concerns;
  - cubic→quadratic conversion is a controlled approximation, not a literal topology copy.
- Dependency / overlap:
  - FontBakery, variable-font compatibility, full family QA, and cross-platform application tests remain later production gates.

### Overlap decision
- **PRACTICE + REPLICATION + METHOD COMPARISON + FAILURE ANALYSIS**.
- Why:
  - Study 003 already states the theory. T006 deliberately re-tests it as source data, generated binaries, and renderer evidence rather than producing another summary.

---

## 1. SOURCE — “minimum points” does not mean “fewest possible points”

Google Fonts' current Outline Quality guide treats production outlines as technical data consumed by operating systems, browsers, applications, printers, hinting, and build tooling. Its checklist warns about:

- wrong contour direction;
- missing extrema;
- open paths;
- almost-straight and short accidental segments;
- duplicate/overlaying geometry;
- zero-length handles;
- fractional coordinates in the Google Fonts production context;
- over-complex construction;
- uncontrolled overlaps and self-crossing behavior.

Source:
- https://googlefonts.github.io/gf-guide/outlines.html

Glyphs likewise describes nodes on extrema as good practice because some rendering, hinting, offsetting, and interpolation operations depend on them, while also noting that export-time tools may add extrema in specific workflows.

Sources:
- https://handbook.glyphsapp.com/editing-paths/
- https://handbook.glyphsapp.com/filters/remove-overlap/
- https://handbook.glyphsapp.com/export/

### SYNTHESIS

“Use fewer points” is incomplete advice.

The production objective is:

> use the **minimum useful topology that expresses the intended curve, includes technically meaningful control points, and survives the intended build/interpolation/rendering pipeline**.

A two-segment ellipse can contain fewer nodes than a four-segment ellipse and still be a worse production source if its important extrema exist only inside segments and the winding is wrong.

---

## 2. Controlled source subset

T006 uses 1000 UPM cubic source outlines for:

- `H` — straight-segment control;
- `O` — round form with counter and overshoot;
- `n` — curve-to-straight transitions and shoulder structure;
- `o` — lowercase round with counter.

All final source coordinates are integers.

The script audits:

- contour direction by signed area and declared outer/counter role;
- internal cubic extrema;
- zero-length handles;
- fractional coordinate values;
- very short segments;
- near-axis accidental misalignment;
- self-intersection/invalid contour geometry;
- overlap area among same-role contours;
- bounds and source structure.

The audit is **study-specific QA**, not a replacement for FontBakery, fontmake, editor validation, or a production family QA suite.

---

## 3. Failure → revision A: `H` overlap

### v0

The first `H` is intentionally authored as three separate outer rectangles:

- left stem;
- right stem;
- crossbar.

All three contour directions are individually valid, but the crossbar overlaps the stems.

Measured same-role overlap area:

`3600 units²`

### Failure

This source may rasterize into an apparently correct H, yet it delegates contour-union behavior to later build/export logic.

The important point is methodological: **a rendered preview can hide source-topology debt**.

### Revision

The revised `H` uses one merged 12-on-curve contour with no same-role overlap.

Disposition:

- `H.v0`: **REJECT as the clean static-source control for this exercise**;
- revised `H`: **PASS the bounded T006 source audit**, not production-family PASS.

### Important nuance

`H.v0` and revised `H` do not demonstrate that overlaps are always forbidden. Variable-font and component workflows may intentionally retain overlaps. The correct decision depends on the production pipeline.

The rule learned here is:

> **intentional overlap must be an explicit source/build decision, not accidental geometry that happens to look correct in one preview.**

---

## 4. Failure → revision B: `O` extrema and winding

### v0

The first `O` uses two cubic segments for the outer contour and two for the counter.

It is visually capable of forming an ellipse-like shape with only left/right on-curve points, but the audit finds:

- outer top extremum internal to a cubic segment;
- outer bottom extremum internal to a cubic segment;
- counter top extremum internal to a cubic segment;
- counter bottom extremum internal to a cubic segment;
- outer contour uses the wrong PostScript winding direction;
- counter contour uses the wrong PostScript winding direction.

Total internal extrema detected:

`4`

### Revision

The final `O` uses four cubic segments per contour with explicit top/right/bottom/left extrema and opposite winding between outer and counter.

The final cubic source uses:

- outer: 4 curve segments, 5 recorded on-curve points including the repeated close point, 8 off-curve controls;
- counter: the same structural pattern;
- no internal extrema;
- no zero handles;
- integer coordinates;
- correct PostScript contour direction;
- no invalid/self-crossing contour.

### STUDIO JUDGMENT

This is a direct counterexample to “fewer nodes are automatically better.”

The v0 O is **topologically cheaper but technically weaker** for this production hypothesis.

---

## 5. Revised source audit result

The final `H O n o` subset passes every bounded source check implemented by T006:

| Glyph | Direction | Internal extrema | Zero handles | Fractional values | Same-role overlap | Invalid/self-crossing | T006 source audit |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| H | correct | 0 | 0 | 0 | 0 | no | PASS |
| O | correct outer/counter | 0 | 0 | 0 | 0 | no | PASS |
| n | correct | 0 | 0 | 0 | 0 | no | PASS |
| o | correct outer/counter | 0 | 0 | 0 | 0 | no | PASS |

### Scope limit

This does **not** prove:

- optical quality across a complete alphabet;
- weight/family coherence;
- interpolation compatibility;
- components/diacritics;
- hinting suitability;
- production spacing/kerning;
- platform quality;
- human reading quality.

It proves only that the small source subset has moved from uncontrolled research geometry to a more explicit production-style topology audit.

---

## 6. SOURCE — cubic and TrueType quadratic outlines are different production representations

Google Fonts documents that PostScript/CFF outlines use cubic curves while TrueType uses quadratic curves, with opposite contour-direction conventions for outer/counter forms.

Source:
- https://googlefonts.github.io/gf-guide/outlines.html

fontTools `cu2qu` converts cubic Bézier curves to quadratic splines under a requested tolerance. Its algorithm may split one cubic into multiple quadratic segments to stay within the error bound; when converting multiple compatible masters together, it can preserve interpolation compatibility.

Source:
- https://fonttools.readthedocs.io/en/latest/cu2qu/index.html

### T006 build

The same clean cubic source is exported two ways:

1. **OpenType/CFF** — cubic source replayed into CFF charstrings;
2. **TrueType/glyf** — cubic source passed through `Cu2QuPen` with `max_err = 0.5` font unit and `reverse_direction=True`.

Generated binaries are local experiment outputs and are **not committed** as product assets.

---

## 7. Export fidelity result

### CFF

For all four glyphs, the dense polyline comparison between source and reopened CFF outlines reports:

`0.000 units`

in the T006 sampled comparison.

Bounds and signed area are also preserved in this build.

This is expected because the experiment keeps a cubic→cubic path.

### TrueType

The quadratic export changes topology materially while remaining geometrically close.

| Glyph | Approx. symmetric polyline distance from source | Absolute filled-area drift | TTF points |
| --- | ---: | ---: | ---: |
| H | 0.000 u | 0.000% | 12 |
| O | 0.436 u | +0.069% | 44 |
| n | 0.363 u | -0.043% | 21 |
| o | 0.355 u | +0.162% | 40 |

The polyline distance is a **sampling-based corroboration metric**, not the mathematical definition of `cu2qu` tolerance. The actual conversion was requested at a 0.5-unit maximum-error setting.

### SYNTHESIS

A TTF export can be visually faithful while possessing a very different point structure from its editable cubic source.

Therefore:

- do not judge source quality by decompiling one binary and counting points;
- do not assume an exported quadratic topology should become the editable master topology;
- preserve authoritative source geometry separately from generated binaries;
- test the actual exported format because conversion is part of production behavior.

---

## 8. Raster transfer — tiny geometric differences can still produce pixel differences

Both local binaries were rendered through FreeType 2.13.2 with no hinting and a light grayscale target at 14, 20, and 48 ppem.

The CFF and TTF glyphs retained the same raster bounding dimensions in every tested case, but coverage was not numerically identical.

Largest measured coverage difference:

`o @ 20ppem: approximately +2.49% TTF coverage versus CFF`

Other examples:

- `O @ 14ppem`: approximately `+1.32%`;
- `o @ 14ppem`: approximately `-1.56%`;
- `n @ 20ppem`: approximately `+0.62%`.

### TRANSFER VALIDATION

This reinforces T003 rather than replacing it:

> **source geometry → outline-format conversion → rasterizer → pixel coverage** is a pipeline.

Even when source/TTF geometric deviation is well below one font unit in the sampled proof, the raster output can differ by whole-pixel coverage decisions at compact sizes.

### Scope limit

These are FreeType/no-hint results only. They are not predictions for CoreText, DirectWrite, Skia, Flutter, browsers, or manually hinted TrueType fonts.

---

## 9. What T006 changes in studio practice

### Before T006

The studio had strong rules about good paths, but its compiled research fonts were primarily **behavioral research instruments**. Their procedural outlines were not sufficient evidence for production-source discipline.

### After T006

A custom type project should separate at least four QA layers:

1. **editable source topology** — curve structure, extrema, direction, overlaps, components, integer/grid policy;
2. **build conversion** — cubic/CFF vs quadratic/TTF, decomposition/overlap removal, tolerance, interpolation compatibility;
3. **binary QA** — tables, contours, metrics, shaping, feature availability;
4. **render/use QA** — actual target renderer, size, density, platform, browser/app, localization, accessibility.

Passing layer 1 is necessary but does not grant layers 2–4.

---

## 10. Project-readiness test

### Apply this knowledge when

- commissioning or drawing a custom family;
- preparing an existing custom font source for production;
- converting cubic sources to TTF;
- debugging glyphs that look correct in the editor but fail in exported fonts;
- planning variable/static build pipelines;
- deciding whether overlaps/components should remain in source or be decomposed/merged at export.

### Do not over-apply it when

- a project uses a proven system/vendor font without modifying its outlines;
- the product problem is hierarchy, fallback, density, or loading rather than custom outline production;
- a visual defect is clearly a spacing/layout/color/rendering issue rather than a source-contour issue.

### Required project inputs

Before prescribing a source-outline workflow, collect:

1. authoritative editable source format;
2. target static/variable outputs;
3. CFF/TTF/webfont requirements;
4. target renderers/platforms and compact sizes;
5. hinting strategy;
6. whether overlaps/components must remain compatible across masters;
7. interpolation/axis plan;
8. glyph/language coverage;
9. build toolchain;
10. regression/QA requirements and whether metric stability is product-critical.

### Concrete decisions this can change

- node/extrema strategy;
- whether an overlap remains editable-source structure or is manually merged;
- whether a glyph needs redraw before export;
- cubic→quadratic tolerance;
- whether generated TTF topology is treated as output rather than source;
- whether a binary can ship after build-only inspection;
- which font changes require Layout/Web regression tests because metrics or compact raster behavior may move.

### Failure conditions

Reject or rework when:

1. a clean preview is used to excuse wrong path direction or accidental overlap;
2. “minimum nodes” deletes technically meaningful extrema;
3. zero handles, duplicate points, tiny accidental segments, self-intersections, or near-axis mistakes are ignored because the outline looks acceptable at 1000% zoom;
4. cubic→quadratic conversion is assumed to be topology-preserving;
5. generated binary topology is edited as though it were the authoritative cubic source without a defined workflow;
6. source audit is called production PASS without interpolation, build, binary, target-renderer, and family-level evidence;
7. an outline change silently shifts advance/sidebearing contracts that Layout relies on;
8. raster regressions at compact target sizes are dismissed because geometric deviation is numerically small.

---

## 11. What remains OPEN

- manually audited `S`, diagonals, bowls+stems, punctuation, and figures at production-source quality;
- component and diacritic workflows;
- multiple-master compatibility and interpolation topology;
- variable-font overlap/source strategy;
- fontmake or equivalent reproducible production build;
- FontBakery and broader binary QA;
- manual/native hinting or a justified hintless strategy;
- CoreText/DirectWrite/Skia/browser/device transfer;
- regression proof that production outline revisions preserve metrics and Layout contracts;
- full-family optical consistency and human reading evidence.

**Bézier / outline discipline may advance from PRACTICE to PRACTICE / CRITIQUE, but Foundation remains NOT PASSED.**

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - fewer nodes are not inherently better; required extrema and source semantics matter;
  - cubic→quadratic export can preserve shape closely while changing topology dramatically;
  - small geometric differences still create compact raster differences.
- Canonical section:
  - Sections 3–8.
- Confirmation / contradiction / transfer note:
  - confirms Study 003 and extends T003 with an explicit source→CFF/TTF production path.
- Scope limit:
  - only `H O n o`, one master, one weight, no hinting.

### Color
- Useful finding/context:
  - CFF/TTF coverage differed by up to ~2.49% in the controlled no-hint raster proof while nominal color would remain identical.
- Canonical section:
  - Section 8.
- Confirmation / contradiction / transfer note:
  - confirms that real glyph coverage should be used when Color validates compact text roles.
- Scope limit:
  - no light/dark/contrast/environment threshold tested.

### Layout / Interaction
- Useful finding/context:
  - production outline/build changes must preserve width/sidebearing contracts deliberately; source cleanliness alone says nothing about final column/reflow behavior.
- Canonical section:
  - Sections 7–10.
- Confirmation / contradiction / transfer note:
  - consistent with L003/L004: final Type behavior remains a Layout input and must be regression-tested near thresholds.
- Scope limit:
  - T006 keeps advances fixed and does not test a page or table.

### Web Design
- Useful finding/context:
  - a browser-facing font file is generated output, not equivalent to the editable source; CFF/TTF conversion and compact rasterization can introduce measurable differences.
- Web application / validation consequence:
  - test the actual delivered WOFF/WOFF2/TTF/CFF-derived webfont build, not a source-editor screenshot.
- Confirmation / contradiction / transfer note:
  - prepares a browser-production transfer contract for future W### work.
- Scope limit:
  - no browser/webfont test performed here.

---

## Next Type question

The highest-value continuation is **T007 — multi-master interpolation/source compatibility + reproducible build QA**:

- create two deliberately related masters for a small subset;
- define compatible point/contour order intentionally;
- reproduce at least one incompatibility failure;
- build an interpolated/variable output with fontTools/varLib or an equivalent open toolchain;
- verify extrema, contour order, overlap strategy, metrics, instance interpolation, and raster output;
- keep generated binaries as evidence outputs rather than confusing them with source authority.

This extends T006 from **one clean master** to **a system that must remain editable and compatible across variation**.
