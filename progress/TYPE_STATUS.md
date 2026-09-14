# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/type/`  
Next new-study ID: `T007`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web, and product decisions. Research volume or curriculum speed is not the objective.

For live projects, accumulated evidence must become project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, density, localization, fallback, source/build quality, scaling, rendering, accessibility, implementation trade-offs, validation and failure conditions.

Self-directed research remains ACTIVE. Adjacent Color, Layout/Interaction, Web, Accessibility, Human Factors, localization, browser/platform and implementation knowledge may be studied when it materially improves Type judgment, replication, transfer validation or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The Type program now has evidence at several distinct layers:

- source/type-system foundations and metrics;
- raster failure→redraw cycles;
- compiled-font renderer comparison;
- complete research numerals/punctuation with proportional/tabular behavior;
- Latin/Korean fallback and vertical-metric comparison;
- a manually auditable production-style outline subset with cubic→CFF/TTF export and raster-transfer evidence.

Remaining Foundation gaps include multi-master/interpolation compatibility, production build/binary QA, hinting strategy, broader glyph-family coherence, browser/platform/device transfer, mixed-script line layout, human recognition/reading evidence and full-family production proof.

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

### Type-owned reproducibility/evidence artifacts

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

Generated experimental font binaries remain local outputs; they are not product assets and are not treated as source authority.

---

## Latest completed block — T006 production outline audit

`T006-production-outline-audit.md` converts the earlier outline-quality theory into a bounded source→build→binary→raster practice cycle.

### Source subset

The controlled 1000-UPM cubic source contains `H O n o` and explicitly audits:

- contour direction;
- internal cubic extrema;
- zero-length handles;
- integer/fractional coordinate policy;
- accidental short/near-axis segments;
- self-intersection/invalid geometry;
- same-role overlap;
- bounds and source structure.

The audit is study-specific QA, not a substitute for a full font-production QA suite.

### Failure → revision A — overlapping H

`H.v0` uses separate left stem, right stem and crossbar contours. They individually have valid winding but produce **3600 units²** of same-role overlap.

The revised H merges the black shape into one clean contour with no same-role overlap.

Professional consequence: a correct-looking preview can hide source-topology debt. Overlap is not universally forbidden, but it must be an explicit source/build strategy rather than accidental geometry.

### Failure → revision B — O extrema and winding

`O.v0` uses two cubic segments for the outer shape and two for the counter. The audit detects:

- four internal top/bottom extrema in total;
- wrong PostScript winding for both outer and counter.

The revised O uses explicit cardinal extrema, integer controls, correct opposite winding and no internal extrema.

Professional consequence: **minimum useful topology is not the same as the fewest possible nodes**. Removing meaningful extrema to lower point count is not production discipline.

### Revised source result

Final `H O n o` all pass the bounded T006 source checks:

- correct declared contour direction;
- zero internal extrema;
- zero zero-length handles;
- zero fractional coordinate values;
- zero same-role overlap;
- no flattened self-intersection/invalid contour.

This is a local audit PASS only; it is not family or production PASS.

### CFF versus TrueType export

The same clean cubic source is exported as:

- CFF cubic outlines;
- TrueType quadratic outlines via fontTools `Cu2QuPen`, requested `max_err = 0.5` font unit and TrueType winding reversal.

Measured approximate source→TTF polyline differences:

- `H`: `0.000u`;
- `O`: `0.436u`;
- `n`: `0.363u`;
- `o`: `0.355u`.

Measured absolute filled-area drift:

- `H`: `0.000%`;
- `O`: `+0.069%`;
- `n`: `-0.043%`;
- `o`: `+0.162%`.

CFF preserved the sampled cubic geometry exactly in this controlled build.

The quadratic binary point structure is materially different from the editable cubic source: e.g. TTF `O` uses 44 points and `o` 40 points. The generated quadratic topology is therefore an output representation, not automatically the preferred editable-master topology.

### Raster transfer

CFF and TTF outputs were rendered with FreeType 2.13.2, no hinting, light grayscale target, at 14/20/48 ppem.

Bounding dimensions stayed equal in the tested pairings, but coverage did not. Largest measured difference:

`o @ 20ppem: approximately +2.49% TTF coverage versus CFF`

This extends T003's conclusion: source geometry, format conversion and rasterizer are separate layers. Sub-unit geometric differences can still cross compact pixel-coverage thresholds.

### Evidence level

**PRACTICE + CRITIQUE / source topology + generated CFF/TTF + FreeType transfer evidence.**

T006 does not establish variable-master compatibility, production build QA, hinting, browser/platform/device behavior or full-family optical quality.

---

## Previous key blocks

### T005 — Latin/Korean fallback

Measured Inter/Roboto/Noto/Nanum control pairings. Same nominal size did not imply equal Hangul/Latin body size or metric spans. Blind Latin x-height matching was rejected as a generic Hangul fallback-normalization method. One L002 long Korean label varied from 486px to 503px under different Korean fallbacks with the same Inter primary in the controlled unshaped measurement.

### T004 — numerals / punctuation

Complete research `0–9`, proportional defaults, fixed-cell tabular alternates, `tnum`, zero alternatives, ambiguity controls and punctuation. Colon v0 failed compact raster presence and was redrawn. Equal source tabular widths were shown not to guarantee equal lower-level raw hinted advances in every mode.

### T003 — compiled renderer matrix

Established that one outline/metric decision can behave differently under no-hint, normal autohint, light autohint and client positioning. Compact custom type requires target-renderer validation.

### T002 — raster redraw cycle

Established the first controlled Type failure→redraw→re-proof cycle and was later limited/refined by T003 renderer evidence.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | broader coherent family extension and role transfer |
| Bézier / outline discipline | **PRACTICE / CRITIQUE** | T006 clean source audit exists; diagonals/complex curves/components, multi-master compatibility, interpolation/build/binary QA remain open |
| Optical correction | PRACTICE / CRITIQUE | target family/platform decisions and broader intended-size proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | FreeType CFF/TTF evidence exists; hinting and CoreText/DirectWrite/Skia/browser/device matrix open |
| Spacing before kerning | PRACTICE / CRITIQUE | broad alphabet/family spacing and runtime shaping open |
| Numerals / punctuation | PRACTICE / CRITIQUE | production curves, browser feature application, human recognition and broader punctuation/language coverage open |
| Typography as information architecture | CRITIQUE | production reflow, localization and enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | actual loading/failure/script fallback, metric overrides, zoom/reflow and data stability in Web |
| Mixed-script / fallback | PRACTICE / CRITIQUE | browser/platform shaping/line boxes, Korean breaking, weight integration and human evidence open |
| Source/build production pipeline | **PRACTICE / CRITIQUE** | T006 single-master source→CFF/TTF path exists; multi-master/variable compatibility, reproducible production build, FontBakery/binary QA and release engineering open |

---

## Peer evidence currently affecting Type

### Color

Color is now through **C007**.

Relevant findings:

- C006 provides explicit finance/operational semantic foreground/surface systems ready for real Type transfer;
- C007 holds geometry/type fixed and shows color-driven feature load can change materially without Layout changes;
- C007 also rejects `desaturate = declutter` as a universal rule because strong luminance segmentation can remain visually forceful.

Type consequence:

- T003–T006 raster/coverage evidence should later be placed into Color-defined foreground/background conditions rather than judged only black-on-white;
- when Color is the variable, font geometry/render state must be controlled explicitly.

Type does not infer human salience or contrast thresholds from Color's image-statistics proxies.

### Layout / Interaction

Layout/Interaction is through **L004 / I004**.

Relevant Type transfers already established by that specialist:

- L003: Latin/Korean fallback can move real wrap thresholds and require semantic-lane recomposition;
- L004: Chromium `tabular-nums` equalized tested digit/decimal layout positions, but the wider intrinsic numeric width caused overflow in a fixed 88px Inter numeric column until Layout allocated intrinsic width;
- I004 adds local/remote values, version metadata, preserved drafts and conflict messages as future localization/wrapping stress contexts.

Type consequence:

- production outline/build changes must preserve advance/sidebearing contracts deliberately;
- a Type change can be technically clean yet still require Layout regression tests near fixed-width/wrap thresholds.

### Web Design

At the latest sync, Web still lists `W001` as next and no substantive `W###` evidence exists.

Current Type→Web transfer contracts now include:

- T001 — loading/failure/script fallback and reflow;
- T003 — compact renderer/metric behavior;
- T004 — `tnum`, zero/punctuation and numeric alignment risk;
- T005 — Korean fallback/metrics/long localized strings;
- T006 — editable source vs generated CFF/TTF and compact raster-transfer behavior.

Do not invent Web evidence. Actual delivered webfont builds, browsers, zoom/DPR and page systems remain Web validation work.

---

## Active next queue

Choose by expected project value, not study count.

1. **T007 — multi-master interpolation/source compatibility + reproducible build QA**: create a small two-master family, reproduce an incompatibility failure, establish compatible contour/point order, build interpolated/variable output and validate metrics/instances/raster behavior.
2. **Browser/platform transfer of T001/T003/T004/T005/T006** when substantive Web or a live target stack is available.
3. **Type→Layout production regression transfer** using L003/L004 thresholds when source/build changes affect width, fallback or compact rendering.
4. **Type→Color transfer** using actual T003–T006 renderer output under C006/C007 conditions with geometry and semantic roles controlled.
5. **Broader production-outline audit** of diagonals, `S`, bowl+stem forms, figures, punctuation, components and diacritics after T007 establishes the source/build system.
6. **Target-platform mixed-script proof** for Flutter/CoreText/Skia/DirectWrite when a live project requires it.
7. **Human evidence** only after target rendering/layout conditions are stable enough to test recognition and mixed-script balance meaningfully.
8. Continue useful replication, contradiction review, method comparison or project-specific work when it materially improves decisions.

---

## Open research-quality gaps

- multi-master contour/point compatibility and interpolation proof;
- variable-font overlap/source strategy;
- reproducible production build pipeline and release QA;
- FontBakery/broader binary QA;
- complex production curves beyond `H O n o`;
- components/diacritics and broader language coverage;
- manual/native hinting or justified hintless strategy;
- CoreText, DirectWrite, Android/Skia, Flutter and browser transfer;
- browser validation of T001/T003/T004/T005/T006;
- mixed-script line-box construction and Korean line breaking on target stacks;
- weight matching and family coherence across Latin/Korean roles;
- human recognition/reading evidence;
- regression evidence that outline/build revisions preserve Layout contracts;
- Color/viewing-condition transfer of real renderer coverage.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

- T006 demonstrates that CFF/TTF conversion changed compact raster coverage by up to about 2.49% in the bounded no-hint proof while the nominal foreground color would remain identical.
- Use actual renderer output when validating compact foreground roles; do not infer a contrast/environment threshold from T006 itself.

### Layout / Interaction

- T006 separates source cleanliness from runtime geometry. Production outline/build revisions must preserve advance/sidebearing contracts and should be regression-tested near L003/L004 wrap/column thresholds.
- T006 itself keeps advances fixed and does not make a new Layout-policy claim.

### Web Design

- The shipped webfont is generated output, not equivalent to an editor/source preview. Format conversion and target rasterization can change compact results.
- Future Web validation should use the actual delivered font build and page stack, not the source SVG/editor appearance.

## Handoff rule

When another specialist requests Type evidence, answer with canonical Type evidence or new investigation as appropriate. Do not silently replace peer ownership or edit peer canonical files without authorization.

---

## Latest checkpoint

- `T002`: raster failure→redraw cycle completed.
- `T003`: compiled TrueType + FreeType renderer matrix completed.
- `T004`: complete research numeral/punctuation system + renderer-aware tabular stress completed.
- `T005`: Latin/Korean fallback metrics/raster/reflow transfer completed.
- `T006`: production-style `H O n o` source audit, overlap/extrema/winding failure→revision, CFF/TTF conversion and raster-transfer proof completed.
- `Bézier / outline discipline` advances to **PRACTICE / CRITIQUE**, not PASS.
- `Source/build production pipeline` begins at **PRACTICE / CRITIQUE**, not PASS.
- Next Type study ID: `T007`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
