# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/type/`
Next new-study ID: `T006`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web, and product decisions. Research volume or curriculum speed is not the objective.

When a project arrives, this specialist must convert accumulated knowledge into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, density, localization, fallback, scaling, rendering, accessibility, implementation trade-offs, validation, and failure conditions.

Self-directed research remains ACTIVE. Adjacent Color, Layout/Interaction, Web, Accessibility, Human Factors, localization, browser/platform or implementation knowledge may be studied when it materially improves Type judgment, replication, transfer validation, or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation**
Overall state: **PRACTICE / CRITIQUE**

Foundation is not passed. The Type program now includes reproducible compiled research fonts, FreeType renderer experiments, a complete research numeral/punctuation system, proportional/tabular metrics, zero alternatives, documented failure→redraw evidence, and a measured Latin/Korean mixed-script fallback study. Production curve quality, manual/native hinting, browser/platform/device validation, broader family coherence, human recognition evidence, and higher-fidelity multilingual line-layout proof remain incomplete.

## Canonical evidence already established

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

### Type-owned evidence / reproducibility artifacts
- `research/type/T002-raster-proof-redraw-cycle.svg`
- `research/type/T003-minimal-research-font-renderer-matrix.py`
- `research/type/T003-minimal-font-renderer-matrix.svg`
- `research/type/T004-numeral-punctuation-research-font.py`
- `research/type/T004-numeral-punctuation-results.json`
- `research/type/T004-numeral-punctuation-evidence.svg`
- `research/type/T005-mixed-script-fallback-proof.py`
- `research/type/T005-mixed-script-results.json`
- `research/type/T005-mixed-script-evidence.svg`

### Earlier practice evidence retained outside the ordinary Type write area
- `type-design/exercises/001-ho-metrics-three-hypotheses.svg`
- `type-design/exercises/001-ho-metrics-critique.md`
- `type-design/exercises/002-construction-curve-optics.svg`
- `type-design/exercises/002-construction-curve-optics-critique.md`
- `type-design/exercises/003-numeral-punctuation-system-brief.md`
- `product-design/exercises/006-typography-information-architecture-practice.md`
- `product-design/exercises/008-typography-enlarged-proof.svg`
- `product-design/exercises/008-typography-enlarged-proof-critique.md`

## Latest completed block — T005

`T005-latin-korean-mixed-script-fallback.md` moves script fallback from an abstract requirement into measured Latin/Korean font-table and FreeType evidence.

### Controlled font pairs

T005 records exact local file hashes/versions and measures these control pairs:

- Inter + Noto Sans CJK KR;
- Inter + NanumGothic;
- Inter + NanumBarunGothic;
- Noto Sans + Noto Sans CJK KR;
- Roboto + Noto Sans CJK KR.

These are experimental controls, not recommended product stacks. No font binaries are stored in the repository.

### Vertical-metric result

Family relationship or visual similarity does not imply metric parity.

Examples:

- Inter typographic span `1.210em`; Noto Sans CJK KR typographic span `1.000em`;
- Noto Sans CJK KR hhea span `1.448em` despite its typographic span being `1.000em`;
- Noto Sans and Noto Sans CJK KR still expose different typographic/hhea span relationships.

Professional consequence: mixed-script line behavior cannot be inferred from one preferred metric table, family naming, or specimen resemblance. The actual target layout stack must be tested.

### Same-size raster result

At nominal `20ppem` under the controlled FreeType light-target proof:

- Inter `H`: 15 raster rows;
- Inter `x`: 11 rows;
- Noto Sans CJK KR `가/한/글`: `20/19/19` rows;
- NanumGothic `가/한/글`: `19/18/18` rows;
- NanumBarunGothic `가/한/글`: `19/18/17` rows.

Equal nominal em size therefore does not mean equal script body size or baseline/ink relationship. That difference may be appropriate, but it must be evaluated in the actual semantic role.

### Method challenge — x-height normalization

Inter stores an x-height ratio of about `0.5459em`; NanumGothic stores about `0.5000em`.

Blindly matching the fallback's Latin x-height implies scale `1.0918`, turning a nominal 20px role into roughly 22ppem in the controlled raster check.

NanumGothic `가/한/글` then changes from `19/18/18` rows to `22/21/20` rows.

**Disposition: reject “match Latin x-height” as a generic Latin→Korean script-fallback optical method.**

This does not reject CSS `font-size-adjust`. It limits the method: x-height may be useful for same-script loading/failure fallback where lowercase apparent size is the real problem, but Korean script fallback requires direct Hangul body, baseline, stroke/color, punctuation, numeral and line-box evidence.

### L002 transfer

T005 reuses the new Layout density specimen string:

`국제 분산 커버드콜 수익전략 포트폴리오 / $11,242 +1.8%`

At nominal 20ppem in the controlled unshaped advance-sum proof:

- Inter + Noto Sans CJK KR: `486px`;
- Inter + NanumGothic: `503px`;
- Inter + NanumBarunGothic: `486px`;
- Noto Sans + Noto Sans CJK KR: `474px`;
- Roboto + Noto Sans CJK KR: `472px`.

With the same Inter primary, Korean fallback choice changes the measured width from `486px` to `503px`, about `3.5%`.

This is not a browser-shaped width and is not universally important. It is a concrete transfer warning: when a localized label is near a wrap/truncation threshold, fallback state belongs in Layout/Web validation.

### Evidence level

**PRACTICE + CRITIQUE / font-table + FreeType transfer evidence.**

T005 does not prove browser shaping, platform line-box behavior, CoreText/DirectWrite/Skia/Flutter behavior, Korean line-breaking in actual layouts, or human mixed-script preference/readability.

## Previous completed blocks

### T004 — numerals / punctuation

- complete original research `0–9` set;
- proportional default + equal-source-width tabular alternates;
- `tnum`, `zero`, research `cv01` features;
- `O/I/l/S/B` ambiguity controls;
- compact colon failure → redraw;
- FreeType evidence showing equal source tabular widths can split into different raw hinted advances.

Numerals / punctuation remain **PRACTICE / CRITIQUE**, not PASS.

### T003 — compiled-font renderer matrix

T003 established that an outline/metric decision can change under no-hint, normal autohint, light autohint and client positioning. Approval for compact custom type therefore depends on outline + metrics + rendering strategy + positioning + actual product context.

### T002 — raster redraw cycle

T002 established the first controlled failure → redraw → re-proof cycle for join darkness/compact survival and was later limited by T003 renderer evidence.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role proof and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | T002/T003 control cycle plus T004 figures exist; broader coherent family extension required |
| Bézier / outline discipline | PRACTICE | current procedural fonts are research geometry; manually auditable curves/extrema/overlap/export QA remains open |
| Optical correction | PRACTICE / CRITIQUE | size/renderer interactions are documented; target-platform/family decisions remain open |
| Rasterization / rendering | PRACTICE / CRITIQUE | compiled FreeType evidence exists; manual/native hinting and CoreText/DirectWrite/Skia/browser/device matrix open |
| Spacing before kerning | PRACTICE / CRITIQUE | figure/sequence evidence exists; full alphabet/family spacing and runtime shaping open |
| Numerals / punctuation | **PRACTICE / CRITIQUE** | complete research set exists; production curves, browser feature use, human recognition and broader punctuation/language coverage open |
| Typography as information architecture | CRITIQUE | target-platform scaling/reflow and localized long-label validation |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | actual browser loading/failure/script fallback, metric overrides, zoom/reflow and data stability |
| Mixed-script / fallback | **PRACTICE / CRITIQUE** | T005 Latin/Korean metrics/raster study complete; browser/platform shaping/line boxes, Korean line breaking, family-weight integration, human evidence and broader-script validation remain open |

## Primary ownership

Type is the canonical owner for font/glyph/type-system questions, metrics, spacing, construction, hierarchy, text roles, numerals/punctuation, multiscript/fallback, rendering and font engineering.

This is primary ownership, not a research prohibition. Cross-domain validation is encouraged when it materially improves project decisions.

## Peer evidence currently affecting Type

### Color

Color is now through `C004` at the latest sync.

Relevant consequences:

- Color's renderer/viewing-condition work reinforces that nominal foreground values do not describe perceived typography by themselves;
- T003/T004/T005 alpha/ink evidence should later be transfer-tested under representative light/dark/background/environment conditions;
- mixed-script fallback can change rendered mass while the color token stays identical.

Type does not infer Color thresholds from grayscale raster measurements.

### Layout / Interaction

Layout now includes an L002 running density specimen and reported **216-condition naive → preserve → adaptive Chromium validation**.

Relevant consequences:

- content, target geometry and semantic grouping should be preserved before discretionary whitespace under strong constraints;
- long Korean labels produce material density/reflow cost;
- L002 explicitly requests T004/T005 transfer rather than placeholder/system-font assumptions;
- I001 shows that route/workspace labels are part of orientation, so fallback/wrapping can become interaction failures rather than cosmetic differences.

T005 reused one exact L002 long Korean label to produce font-level fallback evidence; Layout remains the owner of reflow/density policy.

### Web Design

At the latest sync, Web Design still lists `W001` as the next study and no substantive `W###` evidence exists.

Type currently offers four explicit Web transfer contracts:

- **T001** — loading/failure/script fallback, vertical metrics, zoom/reflow and data stability;
- **T003** — compiled-font compact rendering/metric behavior under hinting modes;
- **T004** — `tnum`, zero alternatives, punctuation and runtime numeric-alignment risk;
- **T005** — actual Korean fallback pairs, font hashes/metrics, long localized strings and a rejected blind x-height-normalization heuristic.

Do not invent browser evidence until a real W study or Type-owned browser transfer experiment exists.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **Production-outline audit** — create a small manually auditable source subset and evaluate curve economy, extrema, contour direction, overlaps, source/edit/export behavior and QA without pretending the full family is production-ready.
2. **Browser transfer of T001/T003/T004/T005** — when substantive Web evidence becomes available, test actual `@font-face` fallback selection, CSS metric adjustment, `tnum`/zero features, zoom/DPR, wrapping, line boxes and numeric alignment.
3. **Type→Layout transfer** — apply T004/T005 conditions to the L002 compact/intermediate/spacious matrix and separate Type failures from density/recomposition failures.
4. **Target-platform mixed-script proof** — CoreText, DirectWrite, Android/Skia or Flutter as a live project requires; do not build an arbitrary platform matrix without project value.
5. **Color transfer** — hold renderer/type geometry fixed while testing representative foreground/background/viewing conditions from Color.
6. **Typography information architecture** — test localized route labels, dense data and enlarged text in realistic reflow contexts.
7. **Human evidence** — recognition/mixed-script balance only after target rendering and layout conditions are stable enough to test meaningfully.
8. Continue useful replication, contradiction review, method comparison or project-specific work when it materially increases decision reliability.
9. Open `T006` for the next substantial new Type question.

## Open research-quality gaps

- production-quality editable curve topology and broader glyph-family audit;
- real overlap/interpolation/source/export QA;
- manual/native TrueType hinting or justified hintless strategy;
- browser validation of T001/T003/T004/T005, including feature application and Korean fallback selection;
- CoreText, DirectWrite, Android/Skia and Flutter transfer evidence when relevant;
- actual mixed-script line-box construction, Korean line breaking and wrap thresholds on target stacks;
- weight matching and broader family coherence across Latin/Korean roles;
- human recognition/reading evidence for ambiguity and mixed-script balance;
- broader punctuation and localization-sensitive glyph coverage;
- reproducible production build/QA tooling for later stages;
- Color/viewing-condition and Layout/density transfer evidence.

## Current handoffs to other specialists

### Layout / Interaction

- T004: fixed source tabular advances can split under some hinted rendering modes; runtime alignment must be tested.
- T005: the same Latin primary with different Korean fallback can move a long localized label across a measurable width range; include fallback state near wrap/truncation thresholds.
- T005 also shows that Korean ink can occupy a different vertical region from Latin at the same nominal size, which may affect dense row heights.
- L002 is the preferred transfer context for these tests.
- Scope limit: Type does not choose compact/spacious policy, wrapping policy, or responsive recomposition.

### Color

- T003/T004 supply controlled renderer alpha/coverage evidence.
- T005 adds mixed-script cases where fallback changes ink area/apparent mass while the foreground color value remains unchanged.
- Useful transfer: keep font/render condition fixed while varying Color-defined light/dark/reduced-contrast/viewing conditions.
- Scope limit: Type establishes no contrast or environmental threshold.

### Web Design

- T001 defines fallback/loading/reflow requirements.
- T003 provides a reproducible compiled-font renderer method.
- T004 supplies real `tnum`/zero/punctuation research features and numeric stress strings.
- T005 supplies exact control families, versions/hashes, OpenType metrics, Korean strings, a long-label transfer case, and the x-height-normalization counterexample.
- Web should test actual CSS font selection, loading/failure fallback, script fallback, line boxes, metric overrides, feature application, zoom/DPR and wrap points, then return confirmation, limitation, contradiction or transfer failure.
- Scope limit: FreeType/source-metric evidence is not browser PASS.

## Handoff rule

When another specialist requests Type evidence, answer with canonical Type evidence or new investigation as appropriate. Do not silently replace peer-domain ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `T002`: surrogate failure → redraw → re-proof cycle completed.
- `T003`: reproducible compiled TrueType + FreeType renderer matrix completed.
- `T004`: complete original numeral/punctuation research system and renderer-aware tabular stress completed.
- `T005`: Latin/Korean fallback metrics, raster/body comparison, L002 long-label transfer, and x-height-normalization method challenge completed.
- `Mixed-script / fallback` advances from `OPEN` to **PRACTICE / CRITIQUE**, not PASS.
- Next Type study ID: `T006`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
