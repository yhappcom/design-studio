# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T011`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume or curriculum speed is not the objective.

For live projects, accumulated evidence must become project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, density, localization, fallback, source/build quality, release packaging, variable-axis behavior, scaling, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The Type program now has evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, single-master outline QA, two-master interpolation compatibility, generated-variable-font binary release QA, static webfont feature/subset QA, and **variable-font WOFF2/subset axis-semantics QA**.

Remaining Foundation gaps include broader glyph-family coherence, components/diacritics/anchors, three-master/multi-axis/CFF2 work, external broad QA/sanitizer integration, complete naming/style-linking/STAT/avar family metadata, broader OpenType feature closure, shaping/browser/platform/device transfer, hinting strategy, mixed-script line layout and human reading/recognition evidence.

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
- `research/type/T010-variable-webfont-axis-contract.md`

### Reproducibility / evidence artifacts

T002–T009 retain their existing Python/JSON/SVG artifacts. T010 adds:

- `research/type/T010-variable-webfont-axis-contract.py`
- `research/type/T010-variable-webfont-axis-contract-results.json`

Generated experimental font binaries remain local outputs; they are not product assets and are not source authority.

---

## Latest completed block — T010 variable webfont axis contract

T010 extends T009's distribution-transformation QA from required GSUB/metrics into variable-font axis semantics.

### SOURCE

- `fvar` defines variable axes, user-space ranges/defaults and named instances.
- `gvar` carries TrueType glyph variation data.
- `STAT` is part of the required variable-font style-attribute model.
- `avar` is optional, but when present remaps normalized axis coordinates.
- fontTools applies `avar` when normalizing user-space coordinates for variable-font instancing.

### Controlled variable font

The bounded two-master TrueType VF uses:

- `wght 300 / default 300 / 700`;
- named instances `300 / 500 / 700`;
- explicit `STAT` values;
- deliberately non-linear `avar`: normalized `+0.5 → approximately +0.35`;
- source glyphs `.notdef`, `space`, `H`, `O`;
- H advances `620u` at 300 and `680u` at 700.

Artifacts tested:

1. source variable TTF;
2. source variable WOFF2;
3. H-only subset variable TTF;
4. H-only subset variable WOFF2;
5. adversarial H-only subset WOFF2 with `avar` deliberately removed.

### RESULT A — packaging/subsetting preserved the bounded contract

Normal WOFF2 packaging preserved `fvar/gvar/STAT/avar`, axis range, named instances and the non-linear mapping.

Normal H-only subsetting correctly reduced glyph/gvar closure to `.notdef` + `H` while retaining the same variation semantics.

Across source TTF, source WOFF2, subset TTF and subset WOFF2, H advances remained:

- `wght 300`: `620u`;
- `wght 500`: `641u`;
- `wght 700`: `680u`.

### Failure — parseable variable WOFF2 with changed axis meaning

The adversarial subset removes only `avar` and remains parseable. It still retains:

- `fvar`;
- `gvar`;
- `STAT`;
- the same visible `wght 300/300/700` range;
- named instances `300/500/700`;
- the same endpoint advances `620u` and `680u`.

But H at user-space `wght=500` changes:

- intended package with `avar`: **641u**;
- package without `avar`: **650u**;
- delta: **+9u**.

### Critical distinction

`avar` is optional in OpenType. Therefore absence of `avar` does not by itself mean that a general-purpose sanitizer should reject the font.

In this study, however, `avar` is part of the **authored product axis contract**. Dropping it changes the meaning of the same user coordinate.

### SYNTHESIS

T008–T010 distinguish three release-QA layers:

1. binary/spec/sanitizer validity;
2. distribution transformation integrity;
3. product-semantic integrity — required features, metrics, variable-axis mappings and representative instances.

A broad validator cannot infer every product-specific semantic contract. A studio checker cannot replace broad standards/vendor QA.

### STUDIO JUDGMENT

Production variable-font release gates should combine:

`external broad QA + product-specific semantic assertions + exact shipped-artifact target integration tests`.

For intentionally non-linear axes, representative user-space coordinates should be regression-tested after packaging/subsetting.

### OPEN / external QA limitation

`fontbakery`, `fontspector`, and `ots-sanitize` were not available in the execution environment. A network installation attempt failed due unavailable name resolution.

T010 does **not** simulate those results or claim external sanitizer PASS. This remains the first priority for T011 or the first environment where the executables are available.

T010 also does not establish browser CSS axis behavior, multi-axis/three-master behavior, `avar` v2, CFF2, GPOS/mark/`locl` closure, cross-toolchain WOFF2 equivalence, target-platform rendering or human evidence.

### Evidence level

**PRACTICE + CRITIQUE / two-master VF + WOFF2 + subset closure + named instances + non-linear `avar` + adversarial mapping removal + representative metric regression.**

T010 is **not PASS**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | broader coherent family extension and role transfer |
| Bézier / outline discipline | PRACTICE / CRITIQUE | diagonals/complex curves/components/diacritics and broader family proof |
| Multi-master / interpolation | PRACTICE / CRITIQUE | T010 adds packaged axis-mapping proof; three-master/multi-axis/richer avar/components/CFF2/overlap remain |
| Optical correction | PRACTICE / CRITIQUE | broader family/axis/platform intended-size proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | CoreText/DirectWrite/Skia/browser/device + hinting strategy |
| Spacing before kerning | PRACTICE / CRITIQUE | broad family spacing, GPOS/kerning and runtime shaping |
| Numerals / punctuation | PRACTICE / CRITIQUE | T009 preserves bounded `tnum`; production figures, browser shaping, localization and human evidence remain |
| Typography as information architecture | CRITIQUE | production reflow, localization and enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | real loading/failure/script fallback, metric overrides, zoom/reflow |
| Mixed-script / fallback | PRACTICE / CRITIQUE | target-platform shaping/line boxes/Korean breaking/weight integration/human evidence |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T010 cover source→interpolation→binary QA→static feature package contract→variable axis package contract; external QA, broader features/scripts/family metadata and target integration remain open |

---

## Peer evidence currently affecting Type

### Color

Color's C009 controlled Chromium evidence confirms that exact Type weight/fallback/DPR can materially change rendered text while semantic Color pairs stay fixed.

T010 consequence: for a variable font, pinning only `wght=500` is insufficient if the shipped artifact's authored axis mapping differs. Color transfer should identify the exact packaged artifact + axis coordinate + render condition.

### Layout / Interaction

Layout/Interaction is through L006 / I004 in its status. L003/L004 remain directly relevant: fallback and numeral behavior can cross wrap/column thresholds.

T010 consequence: exact delivered artifact + axis mapping are Layout inputs. The `+9u` H drift is proof of font-semantic change, not a claim that every product layout will fail by that amount.

### Web Design

Web still lists `W001` as next; no substantive `W###` evidence exists at this checkpoint.

T010 handoff: Web should load the exact axis-audited WOFF2/subset artifact and independently verify CSS `font-weight` / `font-variation-settings`, style matching, loading/fallback, zoom/DPR and target browsers/devices.

---

## Active next queue

Choose by expected project value, not study count.

1. **T011 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; classify universal/spec/vendor-policy findings separately from studio product-semantic assertions.
2. **Broader feature/metric release QA** — GPOS/kerning, marks/anchors, `locl`, vertical metrics and multi-script closure through packaging/subsetting.
3. **Broaden variable-family compatibility** — three masters, multiple axes, richer `avar`, components/diacritics, overlap strategy and CFF2.
4. **Browser/platform transfer of T001–T010** when substantive Web or a live target stack exists.
5. **Type→Layout regression** using exact shipped artifacts + actual axis mapping at known wrap/column/density thresholds.
6. **Type→Color transfer** using exact package/build/axis/render condition.
7. **Target-platform mixed-script proof** for Flutter/CoreText/Skia/DirectWrite when project value justifies it.
8. **Human evidence** after rendering/layout conditions are stable enough to test recognition and reading meaningfully.

---

## Open research-quality gaps

- external FontBakery/Fontspector/OTS integration and exception policy;
- GPOS/kerning/mark/`locl`/multi-script subset closure;
- complete naming/style-linking/STAT AxisValue/avar metadata;
- three-master and multi-axis contour/point correspondence;
- richer avar / avar v2 behavior;
- CFF2 variable outlines;
- variable-font overlap/source strategy;
- components/diacritics/anchors and broader language coverage;
- complex production curves beyond `H O n o`;
- manual/native hinting or justified hintless strategy;
- cross-machine/toolchain WOFF2/reproducibility and release provenance;
- CoreText, DirectWrite, Android/Skia, Flutter and browser transfer;
- mixed-script line-box construction and Korean line breaking;
- weight matching and family coherence across Latin/Korean roles;
- human recognition/reading evidence;
- release-artifact regression evidence against Layout and Color contracts.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

- T010 strengthens C009: a nominal variable-axis coordinate is not sufficient provenance. Pin exact shipped artifact + axis mapping + renderer/DPR.
- T010 makes no Color threshold/readability claim.

### Layout / Interaction

- Validate exact delivered static/variable artifacts and axis mappings near L003/L004 thresholds.
- T010's `+9u` intermediate advance drift demonstrates a font contract change but does not define Layout failure thresholds.

### Web Design

- Integrate the exact axis-audited WOFF2/subset artifact.
- Reproduce representative axis coordinates through CSS and test actual browser loading/style matching/fallback/zoom/DPR/device behavior.
- T010 is not browser PASS.

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
- `T009`: static TTF→WOFF2/subset feature-contract proof completed.
- `T010`: variable TTF→WOFF2/subset axis-contract proof completed; normal transformation preserved variation semantics, while deliberate `avar` removal stayed parseable yet changed H @ `wght=500` from `641u` to `650u`.
- `Source/build/release pipeline` remains **PRACTICE / CRITIQUE**, now spanning source, interpolation, binary QA, static feature packaging and bounded variable-axis semantic packaging.
- Next Type study ID: `T011`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
