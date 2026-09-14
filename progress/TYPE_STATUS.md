# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/type/`  
Next new-study ID: `T008`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume or curriculum speed is not the objective.

For live projects, accumulated evidence must become project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, density, localization, fallback, source/build quality, scaling, rendering, accessibility, implementation trade-offs, validation and failure conditions.

Self-directed research remains ACTIVE. Adjacent Color, Layout/Interaction, Web, Accessibility, Human Factors, localization, browser/platform and implementation knowledge may be studied when it materially improves Type judgment, replication, transfer validation or project usefulness.

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
- manually auditable production-style single-master outlines with CFF/TTF export/raster transfer;
- two-master variable-font compatibility, generated-topology failure/revision, and adversarial point-correspondence validation.

Remaining Foundation gaps include broader production glyph-family coherence, components/diacritics, three-master/multi-axis compatibility, production build/binary/release QA, hinting strategy, browser/platform/device transfer, mixed-script line layout, human recognition/reading evidence and production-fidelity transfer.

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
- `research/type/T007-variable-interpolation-build-proof.py`
- `research/type/T007-variable-interpolation-results.json`
- `research/type/T007-variable-interpolation-evidence.svg`

Generated experimental font binaries remain local outputs; they are not product assets and are not source authority.

---

## Latest completed block — T007 multi-master interpolation compatibility

`T007-variable-interpolation-source-compatibility.md` extends T006 from clean single-master source/build QA into a bounded two-master `wght 300–700` variable-font experiment.

### Failure A — independent cubic→quadratic conversion

Both cubic masters are structurally related, but independent adaptive `Cu2QuPen` conversion produces different generated quadratic topology for `O`:

- wght 300 `O`: `[16,16]` points by contour;
- wght 700 `O`: `[16,12]`.

In tested FontTools `4.63.0`, `varLib` logs:

`glyph O has incompatible masters; skipping`

but still emits a variable font.

Measured `gvar` tuple counts:

- `H=1`;
- `O=0`;
- `n=1`;
- `o=1`.

The emitted `O` therefore freezes at its default-master advance/geometry/raster state at wght 300, 500 and 700.

Professional consequence: **successful VF build is not proof that every required glyph varies.** Build warnings and expected variation coverage are release gates.

### Revision — shared conversion

Converting corresponding cubic curves together with `Cu2QuMultiPen` produces `[16,16]` in both `O` masters and restores one `gvar` tuple for `O`.

Measured instances:

- wght 300: advance `600`, black area `104,025.67`, 20ppem coverage `41.17`;
- wght 500: advance `610`, black area `176,096.37`, coverage `69.67`;
- wght 700: advance `620`, black area `230,545.65`, coverage `91.24`.

The bounded midpoint lies between endpoint black areas and the metric interpolates intentionally.

Professional consequence: multi-master conversion should optimize for **family compatibility**, not independent per-master point economy.

### Adversarial review — same point count is still insufficient

A third build deliberately rotates the Bold `O` counter start point 180° while keeping both master point counts `[16,16]`.

The VF builds, `gvar` exists, and simple count checks pass. Yet the wght 500 midpoint becomes malformed:

- midpoint black area `274,626.45`, **+19.12% above** the Bold endpoint;
- midpoint 20ppem raster coverage `108.74`, **+19.18% above** the Bold endpoint coverage.

Professional consequence: **point-count compatibility is necessary, not sufficient.** Corresponding point indices must represent corresponding structural locations. Endpoint-only QA is also insufficient.

### T007 production contract

Variable outline approval now requires layered checks:

1. source correspondence — contours, order, start points, extrema/landmarks, node roles, components;
2. generated-outline compatibility — point structure, no skipped glyphs, expected variation coverage, explained build warnings;
3. metric interpolation — advances/sidebearings/phantom points vary intentionally;
4. intermediate geometry — inspect endpoints and meaningful intermediate instances for mass/counter/kink/crossing failures;
5. target rendering/use — compact raster, target platforms, Layout regression, Color/background transfer and human evidence where relevant.

### Evidence level

**PRACTICE + CRITIQUE / two-master TrueType + FontTools varLib/gvar + FreeType evidence.**

Not PASS: only two masters, one axis, original research glyphs, no components/diacritics, CFF2, hinting, browser/platform/device or human validation.

---

## Previous key blocks

### T006 — production outline audit

`H O n o` source topology audit with overlap/extrema/winding failure→revision; cubic CFF vs quadratic TrueType export comparison; FreeType no-hint compact raster transfer. Demonstrated that source cleanliness, conversion and raster output are separate gates.

### T005 — Latin/Korean fallback

Measured Inter/Roboto/Noto/Nanum control pairings. Equal nominal size did not imply equal Hangul/Latin body size or metric spans. Blind Latin x-height matching was rejected as a generic Hangul fallback-normalization method. Long localized labels materially changed measured width under fallback choice.

### T004 — numerals / punctuation

Complete research `0–9`, proportional/tabular alternates, `tnum`, zero strategies, ambiguity controls and punctuation; compact colon failure→redraw; lower-level renderer evidence showed equal source tabular widths are not the complete runtime alignment story.

### T003 / T002

T003 established renderer/hinting/positioning dependence using compiled TrueType. T002 established the first controlled Type failure→redraw→re-proof cycle.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | broader coherent family extension and role transfer |
| Bézier / outline discipline | **PRACTICE / CRITIQUE** | T006/T007 topology evidence exists; diagonals/complex curves/components/diacritics and broader family proof open |
| Multi-master / interpolation | **PRACTICE / CRITIQUE** | T007 two-master one-axis proof complete; three-master/multi-axis/avar/components/CFF2/overlap strategy and release QA open |
| Optical correction | PRACTICE / CRITIQUE | broader family/axis/platform intended-size proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | FreeType static/variable evidence exists; hinting and CoreText/DirectWrite/Skia/browser/device matrix open |
| Spacing before kerning | PRACTICE / CRITIQUE | broad alphabet/family spacing, kerning and runtime shaping open |
| Numerals / punctuation | PRACTICE / CRITIQUE | production curves, browser feature application, human recognition and localization-sensitive coverage open |
| Typography as information architecture | CRITIQUE | production reflow, localization and enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | actual loading/failure/script fallback, metric overrides, zoom/reflow and data stability in Web |
| Mixed-script / fallback | PRACTICE / CRITIQUE | browser/platform shaping/line boxes, Korean breaking, weight integration and human evidence open |
| Source/build production pipeline | **PRACTICE / CRITIQUE** | T006 single-master and T007 variable baseline exist; reproducible release QA, binary checks, naming/axis metadata, FontBakery and production automation open |

---

## Peer evidence currently affecting Type

### Color

Current `progress/COLOR_STATUS.md` reports next study `C010`; Color has advanced beyond the C006/C007 transfer evidence originally consumed by T006/T007.

Type-relevant standing rules remain:

- actual rendered glyph mass/coverage matters when evaluating Color foreground roles;
- Color-driven salience experiments require Type geometry/build/instance to be held fixed explicitly;
- T007 adds a new control requirement: future Color transfer must record the exact variable-font build and axis instance, because malformed interpolation can change black mass while color tokens remain identical.

Re-read current Color canonical evidence before opening the next Color-coupled Type study rather than assuming C007 is the latest result.

### Layout / Interaction

Current `progress/LAYOUT_STATUS.md` reports next IDs `L007` / `I005`; Layout has advanced beyond the earlier L003/L004 transfers.

Established Type-facing evidence still applies:

- L003: fallback can cross wrap thresholds;
- L004: browser tabular figures can improve comparison alignment while increasing intrinsic width;
- later Layout work continues to treat actual rendered Type output as a spatial input.

T007 consequence:

- interpolated advances/sidebearings must be regression-tested near constrained Layout thresholds;
- a skipped variation glyph may freeze width unexpectedly;
- malformed intermediate instances can change apparent/actual density even when endpoint layouts pass.

### Web Design

Current Web status still lists `W001` as next; no substantive `W###` evidence is available.

Type→Web transfer contracts now include:

- T001 — loading/failure/script fallback and reflow;
- T003 — compact renderer/metric behavior;
- T004 — `tnum`, zero/punctuation and numeric alignment risk;
- T005 — Korean fallback/metrics/long localized strings;
- T006 — source vs generated CFF/TTF and compact raster behavior;
- T007 — variable-font variation coverage, metric interpolation and malformed-intermediate failure conditions.

Do not invent browser evidence. Future Web validation should use actual delivered font builds and sample endpoint plus intermediate axis values.

---

## Active next queue

Choose by expected project value, not study count.

1. **T008 — production build/release QA baseline**: add deterministic checks for expected tables/axes/variation coverage, naming/metric sanity, warnings/failures and representative instances; investigate FontBakery or equivalent without turning tooling into the objective.
2. **Broaden variable-family compatibility**: three masters, non-linear mapping/`avar`, multiple axes, components/diacritics, overlap policy and CFF2 when that adds decision value.
3. **Broader production-outline audit**: diagonals, `S`, bowl+stem forms, figures, punctuation, components and marks.
4. **Browser/platform transfer of T001/T003/T004/T005/T006/T007** when substantive Web or a live target stack exists.
5. **Type→Layout production regression** at known wrap/column/density thresholds using real built instances.
6. **Type→Color transfer** with exact font build/axis/render condition pinned while varying Color conditions.
7. **Target-platform mixed-script proof** for Flutter/CoreText/Skia/DirectWrite when a live project requires it.
8. **Human evidence** only after target rendering/layout conditions are stable enough to test recognition and mixed-script balance meaningfully.

---

## Open research-quality gaps

- production build/release automation and binary QA;
- FontBakery or equivalent broad QA integrated with studio-specific checks;
- naming/STAT/avar/axis metadata and instance sanity;
- three-master and multi-axis contour/point correspondence;
- CFF2 variable outlines;
- variable-font overlap/source strategy;
- components/diacritics/anchors and broader language coverage;
- complex production curves beyond `H O n o`;
- kerning/layout-feature interpolation;
- manual/native hinting or justified hintless strategy;
- CoreText, DirectWrite, Android/Skia, Flutter and browser transfer;
- mixed-script line-box construction and Korean line breaking on target stacks;
- weight matching and family coherence across Latin/Korean roles;
- human recognition/reading evidence;
- regression evidence that variable/static build changes preserve Layout contracts;
- Color/viewing-condition transfer with exact Type build/instance controlled.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

- T007 shows malformed intermediate correspondence can produce about **+19% black-area/coverage overshoot** versus the Bold endpoint in the bounded proof while nominal foreground color could remain unchanged.
- Future Type→Color transfer should pin exact variable font build and axis value.
- Scope limit: no Color perceptual/contrast threshold is claimed.

### Layout / Interaction

- Independent conversion can freeze a glyph's advance unexpectedly when variation is skipped; compatible conversion restored intentional `600→610→620` O advance interpolation.
- Same-count malformed correspondence can still distort intermediate mass.
- Regression-test real built instances near width/wrap/density thresholds; T007 does not define the Layout policy.

### Web Design

- A VF file loading successfully is insufficient. In the tested build one glyph was omitted from `gvar` while the font still existed.
- Browser QA should verify critical glyph variation, endpoint/intermediate weights, width behavior and real delivered webfont instances rather than checking file-load success alone.
- Scope limit: T007 itself is not browser evidence.

## Handoff rule

When another specialist requests Type evidence, answer with canonical Type evidence or new investigation as appropriate. Do not silently replace peer ownership or edit peer canonical files without authorization.

---

## Latest checkpoint

- `T002`: raster failure→redraw cycle completed.
- `T003`: compiled TrueType + FreeType renderer matrix completed.
- `T004`: research numeral/punctuation system + renderer-aware tabular stress completed.
- `T005`: Latin/Korean fallback metrics/raster/reflow transfer completed.
- `T006`: production-style source audit + CFF/TTF conversion/raster transfer completed.
- `T007`: two-master interpolation incompatibility, shared-conversion repair and same-point-count adversarial correspondence proof completed.
- `Multi-master / interpolation` enters **PRACTICE / CRITIQUE**, not PASS.
- `Source/build production pipeline` remains **PRACTICE / CRITIQUE**, now with single-master and variable-family evidence.
- Next Type study ID: `T008`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
