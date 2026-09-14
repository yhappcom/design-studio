# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/color/`  
Next new-study ID: `C008`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Color research exists to improve real app, web, and product decisions. Research volume, palette count, token count, or curriculum speed are not success metrics.

When a project arrives, this specialist must convert accumulated knowledge into project-specific guidance on palette systems, semantic color, data-visualization color, colorimetry, luminance/contrast, visual salience, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research remains ACTIVE. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, statistics, display technology, or implementation knowledge may be studied when it materially improves Color judgment, independent validation, transfer testing, or project usefulness.

## Current specialist-team awareness

Design Studio has four official peer roles:

1. Typography / Type Design Specialist;
2. Color Specialist;
3. Layout, Spatial & Interaction Specialist;
4. Web Design Specialist.

Color owns canonical color science, color systems, color accessibility, gamut/color management, palette/ramp/semantic systems, data-visualization color, color-driven salience/feature-field analysis, and device/viewing-condition questions. Type owns typography structure/rendering; Layout/Interaction owns spatial hierarchy and state/action semantics; Web Design owns complete web integration and real browser/device validation.

Before substantial work, Color reads all four specialist statuses and materially related peer evidence. New research includes `RELATED DOMAIN CHECK`; useful results are recorded under `HANDOFFS TO OTHER SPECIALISTS`.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**  
Overall state: **CRITIQUE**

The Color program now spans UI color, colorimetry/observer models, chromatic adaptation, ICC/CMM production-path validation, perceptual spaces/difference, gamut mapping, ramp authoring, web override behavior, semantic token architecture, two-context semantic transfer, data-visualization color, controlled observer-conditional metamerism, and fixed-geometry rendered salience/density transfer.

Foundation is **not passed**. Human/CVD evidence, full checksum-verified spectral datasets, current cone-fundamental numerical validation, higher-precision/real-profile/cross-CMM production proof, broader browser/device evidence, physical-display/environmental tests, and production-fidelity project transfer remain incomplete.

## Canonical evidence already established

- `research/color/008-color-luminance-contrast-hierarchy.md`
- `research/color/010-color-science-colorimetry-foundations.md`
- `research/color/011-lms-cone-fundamentals-observer-models.md`
- `research/color/012-chromatic-adaptation-white-points.md`
- `research/color/013-perceptual-color-spaces-difference.md`
- `research/color/016-color-gamut-wide-gamut-mapping.md`
- `research/color/017-perceptual-ramp-authoring.md`
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
- retained product-design Color exercises 005, 009, 010, 012, 013, and 016.

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts; human salience/reading evidence |
| Encoded RGB → linear-light → XYZ | PRACTICE / CRITIQUE | production-path and wider-space cross-checks; device/browser transfer |
| Spectral colorimetry / observer models | PRACTICE / CRITIQUE | C004 1931 integration/scaling/metamer + 1931↔1964 proof complete; full smooth/measured spectra, independently hash-verified current files, current CIE 2006 LMS/cone comparison, physical-device validation pending |
| Chromatic adaptation / ICC color management | PRACTICE / CRITIQUE | C005 v4 profile `chad`/colorant reconstruction and CMM comparison complete; float/16-bit transforms, real device/output profiles, cross-CMM, soft proof and physical-output validation pending |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | CRITIQUE | browser/device validation and production fallback behavior |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | IN STUDY / TRANSFER VALIDATION | Interaction I003 independently confirms key failure mechanism in Chromium; real OS/multi-browser/AT/production token validation still open |
| Semantic color/token architecture | PRACTICE / TRANSFER VALIDATION | C006 two-context graph/collision/pair-matrix practice complete; rendered component combinations, CVD/grayscale, multi-theme/platform/browser and real-project transfer pending |
| Color-driven visual density / salience | **PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION** | C007 fixed-geometry rendered proof complete; human perceived-clutter/search/comparison, CVD, localization/Type, cross-browser/device and physical-environment validation pending |
| Data-visualization color systems | IN STUDY / NUMERICAL PRACTICE | rendered categorical/sequential/diverging examples; CVD/human-task evidence; light/dark, browser/device and multi-project validation |

## Latest completed block — C007

`C007-fixed-geometry-color-density-salience.md` answers the Layout L002 handoff by holding information and geometry constant while varying only color treatment.

### Peer evidence consumed

- Type is now through **T005**; mixed Latin/Korean fallback can materially alter geometry, so C007 deliberately fixes typography/language and does not attribute Type variation to Color.
- Layout/Interaction is through **L004/I004**. L002 supplies the density-isolation method; I003 independently validates Color C001's warning that fill/shadow-only state cues can collapse in Chromium forced colors.
- Web remains pre-W001 at the latest sync; no Web production evidence is invented.

### Controlled rendered specimen

Four variants share the same DOM/content/typography/spacing/border geometry and viewport:

1. `neutral` — low-chroma control;
2. `overloaded` — distributed chromatic surfaces, status fills, row tinting and data colors;
3. `high-contrast-mono` — zero-chroma but strong luminance striping/boundaries;
4. `semantic-sparse` — neutral structure with localized action/selection/status/data color.

Chromium `144.0.7559.96`, viewport `1024×900`, DPR 1.

All tracked geometry comparisons report **identical to neutral = true**.

### Overloaded vs semantic-sparse

- mean Oklab chroma: `0.01763` vs `0.00403` → `4.37×`;
- share of pixels with `C > 0.04`: `13.31%` vs `1.36%` → `9.82×`;
- mean adjacent chroma difference: `0.003573` vs `0.001674` → `2.13×`;
- mean adjacent lightness difference differs only about `+5.0%`;
- study-specific local feature-variability proxy: `0.03249` vs `0.02937` → `+10.6%`.

Interpretation: under fixed geometry, the overloaded condition produces much more distributed chroma variation. **Do not translate the proxy percentage into a human-clutter or performance percentage.**

### Method challenge — desaturation is not a decluttering law

`high-contrast-mono` has effectively zero chroma but, versus `semantic-sparse`:

- mean adjacent lightness difference is about `+59.5%`;
- Oklab L standard deviation about `+51.3%`;
- local feature-variability proxy about `+63.5%`.

Professional consequence: **less chroma does not necessarily mean a calmer or less segmented interface.** Luminance contrast, boundaries, striping and repeated high-contrast surfaces can create a strong competing feature field without hue.

### Sparse color can retain focal strength

Primary-vs-normal button region Oklab distance:

- overloaded `0.4189`;
- semantic-sparse `0.4285`.

The sparse condition therefore retained a strong localized focal-action difference in this within-study metric while using much less page-wide chroma.

This is not a validated human salience threshold; action-finding time remains OPEN.

### Evidence level

**PRACTICE + CROSS-DOMAIN TRANSFER VALIDATION / controlled Chromium rendering + Oklab image statistics + explicit method limits.**

Not PASS: perceived clutter, search/comparison accuracy, eye movement, CVD, localization, cross-browser/device, physical glare/low-light and production-page evidence remain open.

## Previous key blocks

### C006 — semantic token transfer

Two materially different product archetypes reject overloaded brand/action/selection/status mappings and confirm that the semantic-role **method** transfers while literal palettes do not. Pair-contract checks are reproducible; rendered/human/device validation remains incomplete.

### C005 — ICC/CMM production path

A real LittleCMS profile path reconstructs D50 colorants from the sRGB profile `chad` and agrees with independent D65→D50→Lab calculations within the tested 8-bit Lab quantization envelope. Low-bit-depth intermediate round-trip loss is explicitly separated from CMM/adaptation error.

### C004 — observer/metamer practice

Controlled CIE 1931 spectral integration constructs a metamer pair that separates under CIE 1964 10°, demonstrating that a colorimetric match is conditional on the specified observer/system.

### C003 — data visualization

Establishes categorical/sequential/diverging semantics, meaningful diverging midpoint, rainbow failure analysis, monotonicity practice, redundant coding and missing/reference/state separation. Rendered/CVD/human evidence remains open.

### C002/C001 — semantic architecture and override resilience

C002 establishes primitive→semantic→optional component→context resolution and pair contracts. C001 establishes user/browser color-override failure hypotheses, now partially independently validated by Interaction I003.

## Peer evidence currently affecting Color

### Typography / Type

Type is through **T005**.

Color consequences:

- mixed Latin/Korean fallback can change body size, width, line-box behavior and apparent mass while a color token stays identical;
- T004 numerals/punctuation and T005 fallback strings are the next realistic text transfer targets for C006/C007/C003;
- nominal contrast should not be treated as complete compact-type validation.

### Layout / Interaction

Layout/Interaction is through **L004/I004**.

Relevant consequences:

- L002 supplies the fixed-geometry density baseline used by C007;
- L003/L004 show typography and numeric feature settings can change wrapping/column fit, reinforcing the need to hold them fixed in Color experiments;
- I003 confirms C001's forced-color failure mechanism in controlled Chromium;
- I004 adds local/remote/conflict/deleted/merged semantics that Color may encode later but must not define.

### Web Design

At the latest synchronization, Web still lists `W001` as the next study and no substantive `W###` evidence exists. **Do not invent Web evidence.**

Color now provides Web with explicit future transfer contracts for semantic tokens, forced colors, data color, wide gamut, ICC-tagged assets, and C007 fixed-geometry color-density behavior.

## Incoming dependencies

- Type may require measured contrast/luminance/viewing-condition and downstream asset-pipeline evidence for real text, numerals and localized labels.
- Layout & Interaction may require state/focus color contracts, color-vision independence, chart-density and salience evidence, and environmental constraints.
- Web Design may require semantic tokens, chart palettes, forced/system-color behavior, gamut/fallback, ICC asset/export and real page color-density guidance.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **C008 candidate — render C003 data visualization practice:** categorical + sequential + diverging examples in matched light/dark contexts; add grayscale/CVD/small-mark/state critique and at least one failure→revision cycle.
2. Extend C007 with human task evidence when participants are available: known-item search, comparison, action finding, error detection; performance separate from preference/workload.
3. Transfer T004/T005 into C006/C007: real numeric/status/secondary roles, Korean fallback, selected+focused+status combinations, without changing semantic Color jobs.
4. Extend C005 with float/high-bit-depth transforms, real/independent profiles, P3→sRGB and display→print paths, soft proof and a second CMM/toolchain where practical.
5. Extend C004 to complete smooth/measured spectra with independently hash-verified current CIE datasets; perform current CIE 2006 LMS comparison only after provenance is verified.
6. Compare Bradford/CAT02/CAT16 on explicitly bounded datasets; do not declare a universal winner.
7. Validate non-text/focus/ramp and Type transfer evidence on physical displays under controlled bright/low-light conditions.
8. Transfer C001–C007 and Studies 016/017 into real Web/browser validation when substantive W### evidence becomes available.
9. Continue advanced data visualization later into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization.
10. Build automated Color QA only when tied to a real project acceptance criterion; do not turn C007's proxy into a generic score without validation.

## Open research-quality gaps

- C007 human perceived-clutter/search/comparison evidence;
- C007 CVD/localization/cross-browser/device/environment transfer;
- C006 rendered/CVD/human-task and real-project validation;
- C003 rendered/CVD/human-task evidence;
- float/high-bit-depth ICC/CMM validation and actual source/destination profiles;
- P3→sRGB, display→print, soft-proof and cross-CMM evidence;
- full checksum-verified spectral integration on complete smooth/measured spectra;
- current CIE 2006 LMS/cone-fundamental numerical comparison and broader observer-diversity evidence;
- real browser implementation evidence for CSS gamut mapping, forced/system colors, token resolution and ICC-tagged assets;
- physical-display/environmental testing;
- cultural/localization evidence beyond generic color folklore;
- production-fidelity multi-project transfer evidence.

## Current handoffs to other specialists

### Typography / Type

- C007 fixes typography to isolate Color; rerun with T004/T005 to test whether color-density conclusions survive real numerals/Korean fallback.
- C006/C003 remain useful numeric/status/chart-label contexts.
- Scope limit: Color does not define font metrics, fallback or hinting.

### Layout / Interaction

- C007 confirms the value of L002's separation between spatial density and color-driven feature load: geometry stayed identical while rendered feature statistics changed.
- C007 also rejects `desaturate = declutter`; luminance segmentation can be stronger than chroma.
- I003 remains the structural redundancy constraint for any sparse semantic color system.
- Scope limit: no human density/task-performance claim; Layout owns density policy and Interaction owns state meaning.

### Web Design

- C007 supplies a four-condition fixed-geometry specimen and reproducible Chromium harness for future real-page reproduction.
- Test with production tokens/components, actual zoom, project Type, forced/system colors, multiple browsers/OS/devices and real page constraints.
- Continue C001/C002/C006 semantic/override transfer, C003 chart transfer, Studies 016/017 wide-gamut transfer, and C005 embedded-profile/export transfer.
- Return confirmation, limitation, contradiction or transfer failure explicitly.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim peer ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `C001`: Web color override resilience and validation matrix.
- `C002`: semantic color/token architecture and project-readiness method.
- `C003`: data-type-driven visualization color systems and numerical scale practice.
- `C004`: CIE 1931 spectral integration/scaling/metamer practice and 1931↔1964 observer comparison.
- `C005`: v4 ICC profile/CMM D65→D50 validation and precision failure diagnosis.
- `C006`: two-context semantic-token transfer, collision rejection and pair matrices.
- `C007`: fixed-geometry rendered Color→Layout transfer; overloaded chroma vs semantic sparsity; zero-chroma high-luminance-contrast contradiction control.
- `Color-driven visual density / salience` enters **PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION**, not PASS.
- Next Color study ID: `C008`.
- Overall Color state remains **CRITIQUE / Foundation NOT PASSED**.
