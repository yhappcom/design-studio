# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T010`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume or curriculum speed is not the objective.

For live projects, accumulated evidence must become project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, density, localization, fallback, source/build quality, release packaging, scaling, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The Type program now has evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, single-master outline QA, two-master interpolation compatibility, generated-variable-font binary release QA, and **distribution-transformation QA for subsetting + WOFF2 feature/metric preservation**.

Remaining Foundation gaps include broader glyph-family coherence, components/diacritics/anchors, three-master/multi-axis/CFF2 work, external broad QA/sanitizer integration, complete naming/STAT/avar family metadata, shaping/browser/platform/device transfer, hinting strategy, mixed-script line layout and human reading/recognition evidence.

---

## Canonical evidence

### Research

- `research/type/001-type-as-system.md`
- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/003-stroke-contrast-bezier-optics.md`
- `research/type/005-numerals-punctuation-systems.md`
- `research/type/009-typography-as-information-architecture.md`
- `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`
- `research/type/T002-raster-proof-redraw-cycle.md`
- `research/type/T003-minimal-font-renderer-matrix.md`
- `research/type/T004-native-numeral-punctuation-renderer-proof.md`
- `research/type/T005-latin-korean-mixed-script-fallback.md`
- `research/type/T006-production-outline-audit.md`
- `research/type/T007-variable-interpolation-source-compatibility.md`
- `research/type/T008-production-build-release-qa.md`
- `research/type/T009-webfont-subset-feature-contract.md`

### Reproducibility / evidence artifacts

T002–T008 retain their existing Python/JSON/SVG artifacts. T009 adds:

- `research/type/T009-webfont-subset-feature-contract.py`
- `research/type/T009-webfont-subset-feature-contract-results.json`

Generated experimental font binaries remain local outputs; they are not product assets and are not source authority.

---

## Latest completed block — T009 webfont packaging/subsetting feature contract

T009 extends T008 from generated-binary sanity into release distribution transformation.

### SOURCE

- fontTools' subsetter treats retained OpenType layout features as part of glyph closure; glyph variants reachable through preserved GSUB features are retained.
- OpenType 1.9.1 registers `tnum` as **Tabular Figures**.

### Controlled research font

The bounded static TrueType contains proportional `one/two` plus equal-width `one.tnum/two.tnum` alternates, with GSUB `tnum` mapping the proportional glyphs to `600u` tabular outputs.

Artifacts tested:

1. source TTF;
2. source WOFF2;
3. feature-aware subset TTF;
4. layout-feature-dropping subset TTF;
5. feature-aware subset WOFF2;
6. feature-dropping subset WOFF2.

Acceptance contract: `tnum` present + two GSUB outputs + both actual outputs retain equal `600u` advances.

### Failure → revision A — QA checker false failure

The first checker assumed post-subset glyph names `one.tnum` and `two.tnum` must survive literally. fontTools preserved the substitutions but renamed the non-Unicode alternates to generated names.

The name-based checker therefore failed a functionally preserved feature.

Revision: inspect actual GSUB output glyphs and their advances rather than requiring source glyph names.

**STUDIO JUDGMENT:** release QA should test semantic/product contracts, not unstable internal identifiers unless those identifiers themselves are part of a real downstream contract.

### Failure → revision B — parseable but functionally broken subset

The feature-aware subset preserved:

- `tnum`;
- two substitution outputs;
- equal `600u` output advances;
- the same bounded contract after WOFF2 packaging.

A deliberate subset with layout features dropped remained parseable in both TTF and WOFF2 forms but had:

- no `tnum` feature;
- zero GSUB outputs;
- no tabular equal-width contract.

Measured artifact sizes in this tiny research font:

- source TTF `1084 B` → source WOFF2 `440 B`;
- feature-aware subset TTF `1008 B` → WOFF2 `436 B`;
- feature-dropping subset TTF `908 B` → WOFF2 `400 B`.

The byte deltas are not generalizable. The transferable result is that a smaller, readable artifact can still violate the product typography contract.

### SYNTHESIS

T006–T009 now support this release hierarchy:

1. source/design validity;
2. interpolation/build compatibility;
3. binary/spec sanity;
4. **distribution transformation contract** — subsetting/WOFF2/app packaging + required feature/glyph/metric retention;
5. target shaping/rendering/layout integration;
6. human/product validation.

No earlier gate substitutes for the next.

### OPEN / limitation

External `fontbakery`, `fontspector`, and `ots-sanitize` were unavailable in the execution environment. T009 does **not** simulate their results. External broad QA remains open for T010 or the first environment where those executables are available.

T009 also does not establish HarfBuzz/browser shaping, CSS feature application, variable-font packaging, production-family Unicode partitioning, GPOS/mark/kerning preservation, cross-machine reproducibility or human comparison performance.

### Evidence level

**PRACTICE + CRITIQUE / original research font + GSUB `tnum` + TTF→WOFF2 + feature-aware vs feature-dropping subset mutation + QA-checker failure→revision.**

T009 is **not PASS**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | broader coherent family extension and role transfer |
| Bézier / outline discipline | PRACTICE / CRITIQUE | diagonals/complex curves/components/diacritics and broader family proof |
| Multi-master / interpolation | PRACTICE / CRITIQUE | three-master/multi-axis/avar/components/CFF2/overlap strategy |
| Optical correction | PRACTICE / CRITIQUE | broader family/axis/platform intended-size proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | CoreText/DirectWrite/Skia/browser/device + hinting strategy |
| Spacing before kerning | PRACTICE / CRITIQUE | broad family spacing, GPOS/kerning and runtime shaping |
| Numerals / punctuation | PRACTICE / CRITIQUE | T009 preserves bounded `tnum`; production figures, browser shaping, localization and human evidence remain |
| Typography as information architecture | CRITIQUE | production reflow, localization and enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | real loading/failure/script fallback, metric overrides, zoom/reflow |
| Mixed-script / fallback | PRACTICE / CRITIQUE | target-platform shaping/line boxes/Korean breaking/weight integration/human evidence |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T009 cover source→interpolation→binary QA→bounded package/subset contract; external QA, broader features/scripts/family metadata and target integration remain open |

---

## Peer evidence currently affecting Type

### Color

Color is through **C009**. Its controlled Chromium evidence confirms that exact Type weight/fallback/DPR can materially change rendered text while semantic Color pairs stay fixed.

T009 consequence: Color transfer should identify the exact **shipped/subset** artifact, not only a source/release-candidate font before packaging.

### Layout / Interaction

Layout/Interaction is through **L006 / I004**. L004 remains directly relevant: tabular figures improve comparison alignment while increasing intrinsic width.

T009 consequence: a subset can silently remove the Type feature on which the Layout contract depends. Regression must use the exact packaged artifact.

### Web Design

Web still lists `W001` as next; no substantive `W###` evidence exists.

T009 handoff: Web should use the exact feature-audited WOFF2/subset artifact and independently test `@font-face`, CSS `font-variant-numeric`, fallback, zoom/DPR, localization, responsive geometry and target browsers/devices.

---

## Active next queue

Choose by expected project value, not study count.

1. **T010 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; classify universal/spec/vendor-policy findings and retain studio-specific contract checks.
2. **Variable-font packaging/subsetting** — test `fvar`/`gvar`/`STAT`/`avar`, named instances and required features through WOFF2/subset transforms.
3. **Broader feature/metric release QA** — GPOS/kerning, marks/anchors, `locl`, vertical metrics and multi-script closure.
4. **Broaden variable-family compatibility** — three masters, multiple axes, components/diacritics, overlap strategy and CFF2.
5. **Browser/platform transfer of T001–T009** when substantive Web or a live target stack exists.
6. **Type→Layout regression** with exact shipped artifacts at known wrap/column/density thresholds.
7. **Type→Color transfer** with exact package/build/axis/render condition pinned.
8. **Target-platform mixed-script proof** for Flutter/CoreText/Skia/DirectWrite when project value justifies it.
9. **Human evidence** after rendering/layout conditions are stable enough to test recognition and reading meaningfully.

---

## Open research-quality gaps

- external FontBakery/Fontspector/OTS integration and exception policy;
- variable-font WOFF2/subsetting and variation-table retention;
- GPOS/kerning/mark/`locl`/multi-script subset closure;
- complete naming/style-linking/STAT AxisValue/avar metadata;
- three-master and multi-axis contour/point correspondence;
- CFF2 variable outlines;
- variable-font overlap/source strategy;
- components/diacritics/anchors and broader language coverage;
- complex production curves beyond `H O n o`;
- manual/native hinting or justified hintless strategy;
- cross-machine/toolchain reproducibility and release provenance;
- CoreText, DirectWrite, Android/Skia, Flutter and browser transfer;
- mixed-script line-box construction and Korean line breaking;
- weight matching and family coherence across Latin/Korean roles;
- human recognition/reading evidence;
- release-artifact regression evidence against Layout and Color contracts.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

- Rendered Color validation should pin the exact shipped/subset font artifact and, for variable fonts, axis instance.
- T009 makes no Color threshold/readability claim.

### Layout / Interaction

- L004's tabular-numeral geometry can be invalidated by subsetting while the font remains readable.
- Validate packaged production artifacts rather than relying only on source-font metrics/features.

### Web Design

- Integrate the exact feature-audited WOFF2/subset artifact.
- Reproduce `tnum` through CSS shaping and test loading/fallback/localization/zoom/DPR/browser/device behavior.
- T009 is not browser PASS.

## Handoff rule

When another specialist requests Type evidence, answer with canonical Type evidence or new investigation as appropriate. Do not silently replace peer ownership or edit peer canonical files without authorization.

---

## Latest checkpoint

- `T002`: raster failure→redraw cycle completed.
- `T003`: compiled TrueType + FreeType renderer matrix completed.
- `T004`: research numeral/punctuation system + renderer-aware tabular stress completed.
- `T005`: Latin/Korean fallback metrics/raster/reflow transfer completed.
- `T006`: production-style source audit + CFF/TTF conversion/raster transfer completed.
- `T007`: two-master interpolation incompatibility + shared-conversion repair + adversarial correspondence proof completed.
- `T008`: production build/release QA baseline completed.
- `T009`: TTF→WOFF2/subset feature-contract proof completed; feature-dropping artifacts remain parseable yet fail `tnum`; checker corrected from glyph-name dependence to semantic GSUB-output metrics.
- `Source/build/release pipeline` remains **PRACTICE / CRITIQUE**, now spanning source, interpolation, binary QA and bounded distribution transformation.
- Next Type study ID: `T010`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
