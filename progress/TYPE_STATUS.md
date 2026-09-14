# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/type/`  
Next new-study ID: `T009`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume or curriculum speed is not the objective.

For live projects, accumulated evidence must become project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, density, localization, fallback, source/build quality, scaling, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The Type program now has evidence across:

- type-system/anatomy/metrics foundations;
- raster failure→redraw cycles;
- compiled-font renderer comparison;
- research numerals/punctuation with proportional/tabular behavior;
- Latin/Korean fallback and vertical-metric comparison;
- production-style single-master outline/source audit with CFF/TTF export transfer;
- two-master variable-font compatibility and adversarial point-correspondence validation;
- **generated-variable-font release QA with specification-oriented binary checks, real failure→revision evidence, mutation testing and bounded reproducible-build proof.**

Remaining Foundation gaps include broader production glyph-family coherence, components/diacritics/anchors, three-master/multi-axis compatibility, external broad QA/sanitizer integration, complete naming/STAT/avar family metadata, hinting strategy, browser/platform/device transfer, mixed-script line layout, human recognition/reading evidence and production-fidelity transfer.

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

### Reproducibility / evidence artifacts

- `research/type/T002-raster-proof-redraw-cycle.svg`
- `research/type/T003-minimal-research-font-renderer-matrix.py`
- `research/type/T003-minimal-font-renderer-matrix.svg`
- `research/type/T004-numeral-punctuation-research-font.py`
- `research/type/T004-numeral-punctuation-results.json`
- `research/type/T004-numeral-punctuation-evidence.svg`
- `research/type/T005-mixed-script-fallback-proof.py`
- `research/type/T005-mixed-script-results.json`
- `research/type/T005-mixed-script-evidence.svg`
- `research/type/T006-production-outline-audit.py`
- `research/type/T006-production-outline-results.json`
- `research/type/T006-production-outline-evidence.svg`
- `research/type/T007-variable-interpolation-build-proof.py`
- `research/type/T007-variable-interpolation-results.json`
- `research/type/T007-variable-interpolation-evidence.svg`
- `research/type/T008-production-build-qa.py`
- `research/type/T008-production-build-qa-results.json`
- `research/type/T008-production-build-qa-evidence.svg`

Generated experimental font binaries remain local outputs; they are not product assets and are not source authority.

---

## Latest completed block — T008 production build / release QA baseline

T008 extends T006/T007 from source/interpolation correctness into generated-binary release checks.

### Real failure found in the previous research builder

The T007 interpolation experiment was valid for its stated question, but its research masters used `LSB = 0` while the glyph contours had `xMin = 50`. The emitted variable TrueType therefore had:

- `head.flags = 1` — required bit 1 was not set;
- `H O n o` at sampled `wght 300/500/700` with `LSB 0 != xMin 50`;
- **12 sampled LSB/xMin failures plus the head-flag failure.**

This establishes that interpolation evidence and release-binary compliance are separate gates.

### Revision

The T008 builder normalizes master LSBs to actual `xMin`, sets the required head flag state, rebuilds and re-audits the VF.

Revised bounded result:

- `head.flags = 3`;
- all sampled `H O n o` at `wght 300/500/700`: `LSB = 50`, `xMin = 50`;
- required base/variable tables present;
- `wght 300 / 300 / 700` axis confirmed;
- STAT/fvar axis correspondence confirmed;
- name IDs `1,2,3,4,6,256` present;
- one `gvar` tuple for each research glyph;
- whole-font checksum `0xB1B0AFBA`;
- **zero failures under the bounded T008 release contract.**

### Mutation proof

Removing `STAT` from the corrected binary leaves it parseable and leaves tested variation/metrics intact, but the checker correctly rejects it with:

`missing_required_table:STAT`

Professional consequence: **“font opens” and “instances render” are weaker conditions than “release contract satisfied.”**

### Reproducible-build correction

T008 also discovered that merely assigning fixed `head` timestamps was insufficient because FontTools could recalculate them during save. The revised procedure explicitly disables timestamp recalculation when performing the reproducibility probe.

Two corrected same-environment builds produced the identical SHA-256:

`e3354d493cba74f03c857f022d529f8d03e7ae91c948beb79b32b126f1213119`

This is bounded same-environment evidence, not cross-machine/toolchain reproducibility proof.

### Release-gate hierarchy established

1. source/design validity;
2. build/interpolation compatibility;
3. binary/spec sanity;
4. design regression at real instances/metrics/rendering;
5. external broad QA + target browser/OS/device/project validation.

No earlier gate substitutes for a later one.

### Evidence level

**PRACTICE + CRITIQUE / generated variable TrueType binary + spec-oriented audit + real failure→revision + deliberate mutation + bounded reproducibility proof.**

T008 is **not PASS**. External FontBakery/Fontspector/OTS execution, complete naming/family release policy, WOFF2/subsetting, multi-axis/CFF2/components/features, cross-machine builds and platform/browser/human evidence remain open.

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
| Spacing before kerning | PRACTICE / CRITIQUE | broad family spacing, kerning and runtime shaping |
| Numerals / punctuation | PRACTICE / CRITIQUE | production curves, browser feature application, human/localization evidence |
| Typography as information architecture | CRITIQUE | production reflow, localization and enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | real loading/failure/script fallback, metric overrides, zoom/reflow |
| Mixed-script / fallback | PRACTICE / CRITIQUE | target-platform shaping/line boxes/Korean breaking/weight integration/human evidence |
| Source/build production pipeline | **PRACTICE / CRITIQUE** | T006–T008 now cover source→interpolation→binary QA; external broad QA, full family metadata/features, packaging and release engineering remain open |

---

## Peer evidence currently affecting Type

### Color

Color is through **C009**. C009 confirms that exact Type weight/fallback/DPR materially changes rendered text behavior while semantic Color pairs stay fixed.

T008 consequence: downstream rendered Color evidence should identify the exact release candidate font build and axis instance. Binary identity does not replace Color validation, but malformed/non-equivalent font artifacts should not be allowed to contaminate that evidence.

### Layout / Interaction

Layout/Interaction is through **L006 / I004**. L004 remains directly relevant: tabular figures can improve comparison alignment while increasing intrinsic width.

T008 consequence: binary/spec QA should catch Type defects before Layout regression, but project-specific metric/feature assertions and actual reflow tests still remain necessary.

### Web Design

Web still lists `W001` as next; no substantive `W###` evidence exists.

Type→Web transfer now includes T008: use the exact release-candidate artifact after binary QA, then independently test real webfont packaging/loading, variable axes/features, fallback, zoom/DPR, localization and responsive behavior.

---

## Active next queue

Choose by expected project value, not study count.

1. **T009 — external broad QA + sanitizer integration**: run FontBakery/Fontspector/OTS or equivalent against the corrected research VF when executable tooling is available; classify spec/universal/vendor-policy findings and preserve project-specific checks rather than treating one profile as universal truth.
2. **Broaden variable-family compatibility**: three masters, `avar`, multiple axes, components/diacritics, overlap strategy and CFF2.
3. **Broader production-outline/family audit**: diagonals, `S`, bowl+stem forms, figures, punctuation, components, marks, anchors and language coverage.
4. **Feature/metric release QA**: GSUB/GPOS/kerning, numerals, vertical metrics, named instances/STAT AxisValues, subsetting/WOFF2.
5. **Browser/platform transfer of T001–T008** when substantive Web or a live target stack exists.
6. **Type→Layout production regression** at known wrap/column/density thresholds using release-identified artifacts.
7. **Type→Color transfer** with exact build/axis/render condition pinned.
8. **Target-platform mixed-script proof** for Flutter/CoreText/Skia/DirectWrite when project value justifies it.
9. **Human evidence** after target rendering/layout conditions are stable enough to test recognition and reading meaningfully.

---

## Open research-quality gaps

- external FontBakery/Fontspector/OTS integration and exception policy;
- WOFF/WOFF2/subsetting release artifacts;
- complete naming/style-linking/STAT AxisValue/avar metadata;
- three-master and multi-axis contour/point correspondence;
- CFF2 variable outlines;
- variable-font overlap/source strategy;
- components/diacritics/anchors and broader language coverage;
- GSUB/GPOS/kerning interpolation and release QA;
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

- T008 establishes that downstream Color rendering tests should identify the exact release-checked font artifact/axis instance.
- This operationalizes C009's Type-dependence but makes no Color threshold claim.

### Layout / Interaction

- T008 caught metric/head defects before spatial integration and formalizes binary QA as an upstream gate.
- Binary PASS does not prove width/reflow/density suitability; actual release instances still require Layout regression where metrics/features matter.

### Web Design

- Integrate the exact release candidate after binary QA, not an arbitrary editor/intermediate font.
- Browser success remains a separate gate: WOFF2, loading/fallback, CSS axes/features, zoom/DPR and device behavior are not established by T008.

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
- `T008`: production build/release QA baseline completed with real LSB/xMin/head failure→revision, `STAT` mutation proof and bounded reproducible-build evidence.
- `Source/build production pipeline` remains **PRACTICE / CRITIQUE**, now covering source, interpolation and binary-QA layers.
- Next Type study ID: `T009`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
