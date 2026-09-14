# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/color/`  
Next new-study ID: `C010`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Color research exists to improve real app, web, and product decisions. Research volume, palette count, token count, or curriculum speed are not success metrics.

When a project arrives, this specialist must convert accumulated knowledge into project-specific guidance on palette systems, semantic color, data-visualization color, colorimetry, luminance/contrast, rendered text-color robustness, visual salience, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research remains ACTIVE. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, statistics, display technology, or implementation knowledge may be studied when it materially improves Color judgment, independent validation, transfer testing, or project usefulness.

## Current specialist-team awareness

Design Studio has four official peer roles:

1. Typography / Type Design Specialist;
2. Color Specialist;
3. Layout, Spatial & Interaction Specialist;
4. Web Design Specialist.

Color owns canonical color science, color systems, color accessibility, gamut/color management, palette/ramp/semantic systems, data-visualization color, color-driven salience/feature-field analysis, rendered Color-role consequences, and device/viewing-condition questions. Type owns font/glyph construction, metrics, fallback and rendering; Layout/Interaction owns spatial hierarchy and state/action semantics; Web Design owns complete web integration and production browser/device validation.

Before substantial work, Color reads all four specialist statuses and materially related peer evidence. New research includes `RELATED DOMAIN CHECK`; useful results are recorded under `HANDOFFS TO OTHER SPECIALISTS`.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**  
Overall state: **CRITIQUE**  
Foundation: **NOT PASSED**

The Color program now spans UI color, luminance/contrast, colorimetry/observer models, chromatic adaptation, ICC/CMM production paths, perceptual spaces/difference, gamut mapping, ramp authoring, web override behavior, semantic token architecture, multi-context semantic transfer, rendered data-visualization color, observer-conditional metamerism, fixed-geometry salience/density transfer, and Type→Color rendered-role transfer.

Major unresolved gates remain: human/CVD-observer evidence, independently verified complete spectral/cone datasets, higher-precision/real-profile/cross-CMM production proof, broader browser/device evidence, physical-display/environmental tests, production webfont/load behavior, and production-fidelity multi-project transfer.

## Canonical evidence already established

### Legacy Color studies
- `research/color/008-color-luminance-contrast-hierarchy.md`
- `research/color/010-color-science-colorimetry-foundations.md`
- `research/color/011-lms-cone-fundamentals-observer-models.md`
- `research/color/012-chromatic-adaptation-white-points.md`
- `research/color/013-perceptual-color-spaces-difference.md`
- `research/color/016-color-gamut-wide-gamut-mapping.md`
- `research/color/017-perceptual-ramp-authoring.md`

### C-series
- `research/color/C001-web-color-user-override-resilience.md`
- `research/color/C002-semantic-color-role-token-architecture.md`
- `research/color/C003-data-visualization-color-systems.md`
- `research/color/C004-spectral-integration-observer-metamerism.md`
- `research/color/C005-icc-cmm-roundtrip-validation.md`
- `research/color/C005-icc-cmm-roundtrip-validation.py`
- `research/color/C005-icc-cmm-results.json`
- `research/color/C006-semantic-token-transfer-two-contexts.md`
- `research/color/C006-semantic-token-transfer-two-contexts.py`
- `research/color/C006-semantic-token-transfer-results.json`
- `research/color/C007-fixed-geometry-color-density-salience.md`
- `research/color/C007-fixed-geometry-color-density-specimen.html`
- `research/color/C007-fixed-geometry-color-density-playwright.py`
- `research/color/C007-fixed-geometry-color-density-results.json`
- `research/color/C008-rendered-data-visualization-color-validation.md`
- `research/color/C008-rendered-data-visualization-specimen.html`
- `research/color/C008-rendered-data-visualization-playwright.py`
- `research/color/C008-rendered-data-visualization-results.json`
- `research/color/C009-type-rendering-color-contrast-transfer.md`
- `research/color/C009-type-color-rendering-specimen.html`
- `research/color/C009-type-color-rendering-playwright.py`
- `research/color/C009-type-color-rendering-results.json`

Retained earlier Color exercises remain under `product-design/exercises/`.

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts; human salience/reading evidence |
| Encoded RGB → linear-light → XYZ | PRACTICE / CRITIQUE | production-path and wider-space cross-checks; device/browser transfer |
| Spectral colorimetry / observer models | PRACTICE / CRITIQUE | C004 sparse-line integration/metamer + 1931↔1964 proof complete; full smooth/measured spectra, independently hash-verified current files, current CIE 2006 LMS/cone comparison, physical-device validation pending |
| Chromatic adaptation / ICC color management | PRACTICE / CRITIQUE | C005 v4 profile `chad`/colorant reconstruction and CMM comparison complete; float/high-bit-depth transforms, real output profiles, cross-CMM, soft proof and physical-output validation pending |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | CRITIQUE | browser/device validation and production fallback behavior |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | IN STUDY / TRANSFER VALIDATION | Interaction I003 independently confirms key failure mechanism in Chromium; real OS/multi-browser/AT/production token validation still open |
| Semantic color/token architecture | PRACTICE / TRANSFER VALIDATION | C006 two-context graph/collision/pair-matrix practice complete; production component/theme/browser and real-project transfer pending |
| Color-driven visual density / salience | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C007 + independent Layout L005 compatible findings; human perceived-clutter/search/comparison, CVD, localization, cross-browser/device and physical-environment validation pending |
| Data-visualization color systems | PRACTICE / CRITIQUE | C008 rendered categorical/sequential/diverging light-dark failure→revision proof complete; human interpretation, real CVD observers, forced-colors, production chart library, Type/localization, cross-browser/device and multi-project validation pending |
| Type-dependent Color rendering / text-role transfer | **PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION** | C009 weight/fallback/DPR/contrast-margin proof complete; human readability, production webfont load/failure, broader scripts, CoreText/DirectWrite/Skia/Flutter, physical-device/environment and real-project validation pending |

## Latest completed block — C009

`C009-type-rendering-color-contrast-transfer.md` transfer-tests Type T005/T006 against Color contrast-role assumptions.

### Controlled environment

- Chromium `144.0.7559.96` on Linux;
- Playwright Python;
- 14 CSS px text;
- DPR `1` and `2`;
- installed Inter, Noto Sans CJK KR and NanumGothic confirmed;
- four declared foreground/background pairs from `4.542:1` to `7.345:1`.

The screenshot metrics are deliberately **non-normative diagnostics**. WCAG conformance remains based on the declared foreground/background pair; antialiased screenshot pixels are not substituted for the normative calculation.

### Same Color pair, different Type weight

Light-near pair `#767676` on white: nominal ratio `4.542:1`.

At DPR1:

| Type | Coverage density | Strong-core share | Median composited-pixel diagnostic |
| --- | ---: | ---: | ---: |
| Inter Thin 100 | `0.0606` | `0.0000` | `1.41:1` |
| Inter Regular 400 | `0.1970` | `0.1101` | `2.19:1` |
| Inter SemiBold 600 | `0.2579` | `0.1710` | `2.68:1` |

Regular produced about `3.25×` the normalized coverage density of Thin in this bounded rendering, while all three retained the same declared Color pair.

Professional consequence: **same numerical pair contract does not imply equivalent practical rendered prominence.**

### More contrast helps, but does not replace Type

Inter Regular / DPR1:

- near pair `4.542:1` → median screenshot-pixel diagnostic `2.19:1`;
- strong pair `7.005:1` → `2.61:1`.

The stronger Color pair improves the rendered pixel distribution. But Inter Thin's strong-core share remained `0` at DPR1 even after moving to the stronger pair.

Professional consequence: when small text is weak, investigate Type weight/stroke/size/fallback and Color together. Do not automatically darken a global semantic token to repair a Type problem.

### DPR transfer

Inter Regular / light-near:

- DPR1 strong-core share `0.1101`; median composited diagnostic `2.19:1`;
- DPR2 strong-core share `0.1547`; median composited diagnostic `3.41:1`.

The CSS Type and Color values did not change. One renderer/DPR therefore cannot be universalized into device proof.

### Korean fallback transfer

Light-near / DPR1 / identical Korean string:

- Inter + Noto Sans CJK KR: width `362.97px`, normalized coverage density `0.1940`, strong-core share `0.1188`;
- Inter + NanumGothic: width `367.72px`, coverage density `0.1671`, strong-core share `0.0670`.

At a fixed `365px` border-box the Noto fallback remained one line (`32.80px` high), while NanumGothic wrapped to two lines (`49.59px`). Color values were unchanged.

Professional consequence: a Color token does not normalize cross-font/script appearance or spatial footprint. Solve Type/Layout fallback issues before inventing locale-specific Color compensation.

### Evidence level

**PRACTICE + CROSS-DOMAIN TRANSFER VALIDATION / controlled Chromium render + explicit normative-vs-diagnostic separation.**

Not PASS: no human readability/low-vision study, physical-device/ambient test, CoreText/DirectWrite/Skia/Flutter equivalence, real webfont loading/swap/failure, broader-script validation or production-project evidence.

## Previous key blocks

### C008 — rendered data visualization

Categorical identity/selection, sequential ordering, diverging midpoint/missing-data, light/dark remapping and CVD diagnostics have controlled rendered failure→revision evidence. Human/CVD-observer and production chart transfer remain open.

### C007 — fixed-geometry Color density/salience

With geometry fixed, distributed chroma changes the rendered feature field; a zero-chroma high-luminance-contrast control can create even stronger segmentation. `desaturate = declutter` is rejected as a universal rule. Layout L005 independently reached a compatible diagnosis with a complementary method.

### C006 — semantic token transfer

Two materially different product archetypes confirm that semantic-role **method** transfers while literal palettes do not. Brand/action/selection/focus/status collisions are explicitly rejected and pair contracts are reproducible.

### C005 — ICC/CMM production path

A real LittleCMS path validates the studied v4 D65→D50 architecture within observation precision and separates low-bit-depth intermediate loss from CMM/adaptation error.

### C004 — observer/metamer practice

A constructed CIE 1931 metamer pair separates under CIE 1964 10°, confirming that colorimetric match is conditional on the specified observer/system.

### C001–C003

C001 covers user/browser override resilience, C002 semantic token architecture, and C003 the source framework for categorical/sequential/diverging data color.

## Peer evidence currently affecting Color

### Typography / Type

Type is now through **T006**.

Relevant consequences:

- T005 proves mixed Latin/Korean fallback changes metrics, body size, width and raster coverage;
- T006 adds source→CFF/TTF→FreeType evidence showing technically clean outline/export paths can still change raster coverage;
- C009 confirms these dependencies matter downstream to a fixed Color role.

Color must not silently take over font selection, fallback, weight, hinting or outline decisions.

### Layout / Interaction

Layout/Interaction is through **L005/I004** at the latest synchronized evidence used for this block.

Relevant consequences:

- L003/L004 show fallback and numeral features can cross wrapping/track thresholds;
- L005 independently confirms the C007-style separation of spatial density, feature variability, emphasis distribution and semantic collision;
- I003 confirms fill/shadow-only state semantics can collapse under Chromium forced colors;
- I004 adds local/remote/conflict/deleted/merged semantics that Color may encode but must not define.

C009's fixed-width Korean wrap result reinforces that Color must not be used to disguise a Type/Layout failure.

### Web Design

At the latest synchronization, Web still lists `W001` as the next study and no substantive `W###` evidence exists. **Do not invent Web evidence.**

C009 adds a future Web validation contract: real `@font-face`, `font-display`, webfont failure/swap, browser/OS rendering, zoom, device, theme and localized-string testing while semantic Color roles remain fixed.

## Incoming dependencies

- Type may require Color-defined foreground/surface/environment conditions for actual production roles and scripts.
- Layout & Interaction may require Color evidence for state/focus roles, chart/dense-surface salience and environmental conditions.
- Web Design may require semantic token, data-color, forced/system-color, gamut/fallback, ICC asset/export and Type-dependent Color-role validation guidance.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **C010 candidate — higher-precision production color management:** extend C005 beyond 8-bit Lab observation with high-bit-depth/float paths where supported, independently sourced or real profiles, P3→sRGB destination-gamut behavior, and explicit clipping/mapping/precision separation.
2. Extend C004 to complete smooth/measured spectra with independently hash-verified current CIE datasets; complete current CIE 2006 LMS/cone comparison only after provenance is verified.
3. Extend C008 with forced-colors/high-contrast/alternate representation using I003 as the state-resilience baseline.
4. Extend C007/C008/C009 with human tasks when participants are available: search, comparison, series identification, text-role recognition, missing/reference interpretation; keep performance separate from preference/workload.
5. Validate non-text/focus/ramp/chart/Type transfer on physical displays under controlled bright/low-light conditions.
6. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not declare a universal winner.
7. Transfer C001–C009 and Studies 016/017 into real Web/browser validation when substantive W### evidence becomes available.
8. Continue advanced data visualization into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization after current rendered/human gaps are addressed.
9. Expand observer-diversity and metamerism practice only with traceable datasets and explicit production relevance.
10. Build automated Color QA only when tied to real project acceptance criteria; no screenshot/raster/salience/CVD proxy becomes a generic score without validation.

## Open research-quality gaps

- C009 human readability/low-vision, production font-loading, broader-script, platform/device/environment transfer;
- C008 human interpretation/search/comparison, real CVD observers, forced-colors/chart-library/Type/localization/cross-browser/device/export transfer;
- C007 human perceived-clutter/search/comparison evidence;
- C006 production-fidelity real-project transfer;
- float/high-bit-depth ICC/CMM validation and actual source/destination profiles;
- P3→sRGB, display→print, soft-proof and cross-CMM evidence;
- full checksum-verified spectral integration on complete smooth/measured spectra;
- current CIE 2006 LMS/cone-fundamental numerical comparison and broader observer-diversity evidence;
- physical-display/environmental testing;
- cultural/localization evidence beyond generic color folklore;
- production-fidelity multi-project evidence.

## Current handoffs to other specialists

### Typography / Type

- C009 confirms that the same semantic foreground token does not normalize weight/fallback raster mass.
- Inter Thin/Regular/SemiBold differed materially at 14px; Noto/Nanum fallback changed width, coverage and a 365px wrap threshold.
- This is **CONFIRMATION + TRANSFER** of T005/T006 into Color roles, not a font-quality ranking.
- Scope limit: Color does not define font construction, fallback, hinting or preferred weight.

### Layout / Interaction

- C009 shows fallback can change the amount and distribution of colored ink without any Color-token change.
- Diagnose pair contract, glyph coverage and geometry separately before changing spacing or Color.
- Confirms L003/L004/L005 separation logic; no human optimal-density claim.

### Web Design

- Reproduce C009 with production `@font-face`, `font-display`, font-load/failure/swap states, target browsers/OSes, zoom, physical devices/themes and localized strings.
- Continue C001/C002/C006 semantic/override transfer, C007 dense-page transfer, C008 chart transfer, Studies 016/017 wide-gamut transfer and C005 profile/export transfer.
- Return confirmation, limitation, contradiction or transfer failure explicitly.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim peer ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `C001`: Web color override resilience and validation matrix.
- `C002`: semantic color/token architecture and project-readiness method.
- `C003`: data-type-driven visualization color framework.
- `C004`: CIE 1931 spectral integration/scaling/metamer practice and 1931↔1964 observer comparison.
- `C005`: v4 ICC profile/CMM D65→D50 validation and precision failure diagnosis.
- `C006`: two-context semantic-token transfer, collision rejection and pair matrices.
- `C007`: fixed-geometry Color→Layout salience/density transfer.
- `C008`: rendered categorical/sequential/diverging chart validation across light/dark with CVD and semantic midpoint diagnostics.
- `C009`: Type→Color rendered transfer; nominal contrast versus raster coverage/fallback/DPR and WCAG-vs-rendered evidence separation.
- `Type-dependent Color rendering / text-role transfer` enters **PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION**, not PASS.
- Next Color study ID: `C010`.
- Overall Color state remains **CRITIQUE / Foundation NOT PASSED**.
