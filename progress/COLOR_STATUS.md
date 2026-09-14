# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/color/`  
Next new-study ID: `C011`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Color research exists to improve real app, web, and product decisions. Research volume, palette count, token count, or curriculum speed are not success metrics.

When a project arrives, accumulated evidence must become project-specific guidance on palette systems, semantic color, data-visualization color, colorimetry, luminance/contrast, rendered text-color robustness, visual salience, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, ICC/color-management pipelines, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research remains ACTIVE. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, statistics, display technology, frontend/browser behavior, and implementation knowledge may be studied when it materially improves Color judgment, replication, transfer validation, or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**  
Overall state: **CRITIQUE**  
Foundation: **NOT PASSED**

The Color program now spans UI color, luminance/contrast, colorimetry and observer models, chromatic adaptation, ICC/CMM production paths, perceptual spaces/difference, gamut mapping, perceptual ramp authoring, browser/user overrides, semantic token architecture, multi-context semantic transfer, data-visualization color, observer-conditional metamerism, fixed-geometry salience/density transfer, Type→Color rendered-role transfer, and high-precision Display-P3→sRGB production validation.

Major unresolved gates remain: human/CVD-observer evidence, independently verified complete spectral/cone datasets, real device/output profiles, cross-CMM proof, browser/OS wide-gamut transfer, soft-proof/print evidence, physical-display/environmental testing, production webfont/load behavior, and production-fidelity multi-project transfer.

---

## Canonical evidence

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
- `research/color/C010-high-precision-p3-srgb-color-management.md`
- `research/color/C010-high-precision-p3-srgb-color-management.py`
- `research/color/C010-high-precision-p3-srgb-results.json`

Retained earlier Color exercises remain under `product-design/exercises/`.

---

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts; human salience/reading evidence |
| Encoded RGB → linear-light → XYZ | PRACTICE / CRITIQUE | wider production/browser/device transfer |
| Spectral colorimetry / observer models | PRACTICE / CRITIQUE | C004 sparse-line integration/metamer + 1931↔1964 proof complete; full smooth/measured spectra, independently hash-verified current files, current CIE 2006 LMS/cone comparison, physical-device validation pending |
| Chromatic adaptation / ICC color management | **PRACTICE / PRODUCTION-PATH VALIDATION** | C005 D50 PCS/`chad` + C010 float/16/8-bit P3→sRGB proof complete; real output/device profiles, second CMM, soft proof/print and physical-output validation pending |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | **PRACTICE / CRITIQUE** | C010 destination-gamut/precision separation complete; actual browser/OS/device P3 fallback and product acceptance behavior pending |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | IN STUDY / TRANSFER VALIDATION | Interaction I003 independently confirms key failure mechanism in Chromium; real OS/multi-browser/AT/production token validation still open |
| Semantic color/token architecture | PRACTICE / TRANSFER VALIDATION | C006 two-context graph/collision/pair-matrix proof complete; production component/theme/browser and real-project transfer pending |
| Color-driven visual density / salience | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C007 + independent Layout L005 compatible findings; human perceived-clutter/search/comparison, cross-browser/device and physical-environment validation pending |
| Data-visualization color systems | PRACTICE / CRITIQUE | C008 rendered categorical/sequential/diverging light-dark proof complete; human interpretation, real CVD observers, forced-colors, production chart library, cross-browser/device and multi-project validation pending |
| Type-dependent Color rendering / text-role transfer | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C009 weight/fallback/DPR/contrast-margin proof complete; human readability, production webfont loading, broader scripts/platforms/devices/environment pending |

---

## Latest completed block — C010 high-precision Display-P3→sRGB production path

`C010-high-precision-p3-srgb-color-management.md` extends C005 beyond an 8-bit Lab observation path.

### Controlled environment

- Python `3.13.5`;
- Pillow `12.3.0`;
- LittleCMS `2.19`;
- generated Display-P3-like ICC v4.4 matrix/shaper profile;
- LittleCMS built-in sRGB destination;
- relative-colorimetric intent;
- `TYPE_RGB_DBL`, RGB16 and RGB8 paths;
- 33 steps/channel = `35,937` encoded Display-P3 samples.

This is controlled CMM evidence. It is not measured-device P3 evidence.

### Float CMM versus independent colorimetry

For the `16,879` samples whose independent CSS-style sRGB result lies inside `[0,1]`:

- max absolute channel difference: `8.53 × 10⁻8`;
- mean absolute difference: `1.20 × 10⁻8`;
- 95th percentile: `3.56 × 10⁻8`.

Professional consequence: within this bounded in-gamut matrix/shaper transform, the float CMM and independent D65 P3→sRGB calculation agree extremely closely.

Do not generalize this to every ICC profile, LUT profile, CMM, rendering intent, print path or physical device.

### Encoded grid gamut result

`19,058 / 35,937` samples produced at least one CSS-style sRGB component outside `[0,1]`.

This `53.03%` figure is **not** a P3-vs-sRGB gamut-volume ratio. The grid is uniform in encoded RGB, not a perceptually uniform volume estimate.

### Unbounded float result

LittleCMS unbounded output contained:

- `18,418` components below zero;
- `5,161` components above one.

Despite this, float sRGB→P3 round-trip across all samples remained extremely close:

- max absolute P3 error: `4.05 × 10⁻7`;
- mean absolute error: `1.33 × 10⁻8`.

Professional consequence: **numerical reversibility of an extended representation does not mean the bounded destination device can reproduce the original color.**

### Extended-range semantics failure

For Display-P3 green `[0,1,0]`:

- independent CSS-style extended sRGB ≈ `[-0.511605, 1.018266, -0.310675]`;
- LittleCMS unbounded sRGB ≈ `[-2.906227, 1.018266, -1.015978]`.

The in-gamut transform is not contradicted. The difference exposes different extended-range curve/extrapolation semantics.

Studio rule: when negative or >1 RGB values cross systems, record color space, encoded/linear status, transfer function, numeric range, extrapolation rule, and clipping/gamut-mapping stage. “Extended sRGB float” alone is not a complete interchange contract.

### `NONEGATIVES` is not gamut mapping

`cmsFLAGS_NONEGATIVES` changed at least one component for about `45.41%` of the sampled grid, but values above one remained possible. It suppresses negative output; it does not choose a perceptually appropriate in-gamut substitute and is not a complete P3→sRGB delivery policy.

### 16-bit versus 8-bit delivery

Against clipped float output at corresponding quantized input:

- RGB16 max normalized difference: `7.63 × 10⁻6`;
- RGB8 max normalized difference: `0.0019608`, essentially half an 8-bit code step.

A 4,097-sample in-gamut gradient retained:

- `4,097` unique RGB16 triplets;
- `485` unique RGB8 triplets.

The 8-bit input itself also collapsed to `485` triplets. This is an encoding-resolution demonstration, not evidence of CMM failure.

### Independent profile check

An installed Artifex Software sRGB ICC v2.1 profile was compared against the LittleCMS built-in sRGB destination on the in-gamut subset:

- SHA-256 `eddaf344b5edea13269e0d20055f335610e5e0b6e33e6e536f2701bc18c5f7d5`;
- maximum output difference ≈ `0.0018998`;
- mean ≈ `0.0000649`.

This proves only that two profile definitions are not numerically identical under the same CMM. It is **cross-profile**, not cross-CMM or physical-device evidence.

### Evidence level

**PRACTICE + PRODUCTION-PATH VALIDATION / float + 16-bit + 8-bit LittleCMS P3→sRGB + independent matrix comparison + independent on-disk profile check.**

Not PASS: no measured display/output profile, second CMM, browser/OS P3 path, soft proof, print, instrumented physical display, or production-project acceptance study.

---

## Previous key blocks

### C009 — Type→Color rendered-role transfer

Same foreground/background pair can produce materially different raster mass under weight/fallback/DPR. Korean fallback can change width, coverage and wrap while Color remains unchanged. Contrast conformance and rendered robustness remain separate gates.

### C008 — rendered data visualization

Categorical identity/selection, sequential ordering, diverging midpoint/missing-data, light/dark remapping and CVD diagnostics have controlled rendered failure→revision evidence. Human/CVD-observer and production chart transfer remain open.

### C007 — fixed-geometry salience/density

Distributed chroma can change the rendered feature field without geometry changes; zero-chroma high-luminance segmentation can remain visually forceful. `desaturate = declutter` is rejected as a universal rule.

### C006 — semantic token transfer

Two materially different product archetypes confirm that semantic-role method transfers while literal palettes do not. Brand/action/selection/focus/status collisions are explicitly rejected.

### C005 — ICC/CMM D65→D50 path

Real v4 profile architecture, `chad`, D50 PCS colorants and 4,913-color CMM-vs-hand comparison were validated through an 8-bit Lab observation buffer. C010 now closes the major float/high-bit-depth gap for one bounded P3→sRGB path.

### C004 — observer/metamer practice

A constructed CIE 1931 metamer pair separates under CIE 1964 10°, confirming that colorimetric match is conditional on the specified observer/system.

### C001–C003

C001 covers user/browser override resilience, C002 semantic token architecture, and C003 the source framework for categorical/sequential/diverging data color.

---

## Peer evidence currently affecting Color

### Typography / Type

Type is now through **T014** and next ID is T015.

Important current consequences:

- T005/C009 already establish fallback/raster dependence beneath fixed Color roles;
- T007–T012 extend Type evidence into variable fonts, release/package contracts, webfont subsets and mark behavior;
- T013/T014 add normalization-sensitive Latin/Hangul subset closure, including deterministic Hangul NFC↔NFD package evidence;
- Color must evaluate the actual shipped glyph/fallback state before treating localized text appearance as a Color-only problem.

Color does not own font construction, shaping, fallback, normalization policy or release QA.

### Layout / Interaction

Layout/Interaction is through **L006/I004** at the latest synchronization.

Relevant consequences:

- L005 independently confirms the C007 separation of spatial density, feature variability and semantic collision;
- L006 shows visual layer appearance and pointer/focus/semantic ownership can diverge; Color must not use elevation/border treatment as a substitute for interaction ownership;
- I003 remains the forced-colors state-resilience baseline;
- I004 adds conflict/merge/recovery semantics that Color may encode but must not redefine.

### Web Design

Web still lists **W001** as next and has no substantive W### evidence at this checkpoint. **Do not invent Web PASS.**

Color-owned Chromium/CMM evidence remains independent transfer evidence. Complete page/browser/device integration still belongs to Web.

---

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **C011 candidate — forced-colors/high-contrast transfer for semantic/data Color:** extend C001/C008 using Interaction I003; test states, charts, direct labels and alternate representations under Chromium forced-colors while preserving Color/Interaction ownership boundaries.
2. Extend C004 to complete smooth/measured spectra with independently hash-verified current CIE datasets; complete current CIE 2006 LMS/cone comparison only after provenance is verified.
3. Extend C010 with an actual measured/device or independently sourced Display-P3/output profile, second CMM, browser/OS wide-gamut path, and soft-proof/print evidence when available.
4. Extend C007/C008/C009 with human tasks when participants are available: search, comparison, series identification, text-role recognition, missing/reference interpretation; keep performance separate from preference/workload.
5. Validate non-text/focus/ramp/chart/Type transfer on physical displays under controlled bright/low-light conditions.
6. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not declare a universal winner.
7. Transfer C001–C010 and Studies 016/017 into real Web/browser validation when substantive W### evidence becomes available.
8. Continue advanced data visualization into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization after current rendered/human gaps are addressed.
9. Expand observer-diversity/metamerism practice only with traceable datasets and explicit production relevance.
10. Build automated Color QA only when tied to real project acceptance criteria; no screenshot/raster/salience/CVD/CMM proxy becomes a generic score without validation.

---

## Open research-quality gaps

- human readability/low-vision and real-CVD-observer evidence;
- C008 forced-colors/chart-library/cross-browser/device/export transfer;
- C007 human perceived-clutter/search/comparison evidence;
- C006 production-fidelity real-project transfer;
- real measured display/output ICC profiles;
- second CMM/toolchain and soft-proof/print validation;
- browser/OS CSS P3, tagged-image and screenshot/export color-management evidence;
- full checksum-verified spectral integration on complete smooth/measured spectra;
- current CIE 2006 LMS/cone-fundamental numerical comparison and broader observer-diversity evidence;
- physical-display/environmental testing;
- cultural/localization evidence beyond generic color folklore;
- production-fidelity multi-project evidence.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- C009 remains the primary Color-side transfer: same semantic foreground pair does not normalize weight/fallback raster mass.
- C010 adds a downstream asset/reproduction layer: rendered text assets can later be altered by destination gamut, profile definition and delivery precision.
- T013/T014 normalization/fallback state must be known before Color diagnoses Korean text appearance.
- Scope limit: no font-quality ranking or shaping rule is inferred.

### Layout / Interaction

- C010 reinforces layer diagnosis: a destination-gamut/export failure should not be repaired by changing unrelated geometry or interaction semantics.
- L006/I003 state/layer contracts remain independent requirements; Color may encode them but not define ownership.
- Future C011 will transfer I003 into Color-owned forced-colors/data-visualization validation.

### Web Design

- C010 provides a concrete validation contract for CSS `display-p3`, tagged P3/sRGB images, canvas/export, screenshots, profile retention/stripping and wide-gamut devices.
- C009 provides real-font/fallback/DPR Color-role cases.
- C008 provides SVG chart/light-dark/state cases.
- Return browser/device confirmations, limitations or contradictions explicitly when substantive W### work exists.

## Latest checkpoint

- C001: browser/user color override resilience.
- C002: semantic token architecture.
- C003: data-visualization source framework.
- C004: CIE 1931 spectral integration/metamer + 1931↔1964 observer comparison.
- C005: ICC v4 D50 PCS/CMM and low-precision failure diagnosis.
- C006: two-context semantic-token transfer.
- C007: fixed-geometry Color→Layout salience/density transfer.
- C008: rendered categorical/sequential/diverging chart validation.
- C009: Type→Color raster/fallback/DPR transfer.
- **C010: float/16-bit/8-bit Display-P3→sRGB CMM validation, out-of-gamut representation semantics, precision/delivery separation and cross-profile check.**
- Next Color study ID: **C011**.
- Overall Color state remains **Stage 1 + early Intermediate bridge / CRITIQUE / Foundation NOT PASSED**.