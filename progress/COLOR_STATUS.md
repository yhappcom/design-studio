# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/color/`  
Next new-study ID: `C006`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Color research exists to improve real app, web, and product decisions. Research volume, palette count, token count, or curriculum speed are not success metrics.

When a project arrives, this specialist must convert accumulated knowledge into project-specific guidance on palette systems, semantic color, data-visualization color, colorimetry, luminance/contrast, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research remains ACTIVE. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, statistics, display technology, or implementation knowledge may be studied when it materially improves Color judgment, independent validation, transfer testing, or project usefulness.

## Current specialist-team awareness

Design Studio has four official peer roles:

1. Typography / Type Design Specialist;
2. Color Specialist;
3. Layout, Spatial & Interaction Specialist;
4. Web Design Specialist.

Color owns canonical color science, color systems, color accessibility, gamut/color management, palette/ramp/semantic systems, data-visualization color, and device/viewing-condition questions. Type owns typography structure/rendering; Layout/Interaction owns spatial hierarchy and state/action semantics; Web Design owns complete web integration and real browser/device validation.

Before substantial work, Color reads all four specialist statuses and materially related peer evidence. New research includes `RELATED DOMAIN CHECK`; useful results are recorded under `HANDOFFS TO OTHER SPECIALISTS`.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**  
Overall state: **CRITIQUE**

The Color program now spans UI color, colorimetry/observer models, chromatic adaptation, ICC/CMM production-path validation, perceptual spaces/difference, gamut mapping, ramp authoring, web override behavior, semantic token architecture, data-visualization color, and controlled observer-conditional metamerism practice.

Foundation is **not passed**. Full checksum-verified spectral datasets, current cone-fundamental numerical validation, high-precision/real-profile/cross-CMM production proof, browser/device evidence, physical-display/environmental tests, CVD/human-task evidence, and multi-project transfer remain incomplete.

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
- retained product-design Color exercises 005, 009, 010, 012, 013, and 016.

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts |
| Encoded RGB → linear-light → XYZ | PRACTICE / CRITIQUE | production-path and wider-space cross-checks; device/browser transfer |
| Spectral colorimetry / observer models | PRACTICE / CRITIQUE | C004 1931 integration/scaling/metamer + 1931↔1964 proof complete; full smooth/measured spectra, independently hash-verified current files, current CIE 2006 LMS/cone comparison, physical-device validation pending |
| Chromatic adaptation / ICC color management | **PRACTICE / CRITIQUE** | C005 v4 profile `chad`/colorant reconstruction and actual CMM comparison complete; float/16-bit transforms, real device/output profiles, cross-CMM, soft proof and physical-output validation pending |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | CRITIQUE | browser/device validation and production fallback behavior |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | IN STUDY / TRANSFER VALIDATION | real browser forced-colors/theme/system-color tests; browser/device differences |
| Semantic color/token architecture | IN STUDY / PROJECT-READINESS SYNTHESIS | implement token graph + pair matrix in materially different products; multi-theme/platform/browser transfer; collision critique |
| Data-visualization color systems | IN STUDY / NUMERICAL PRACTICE | rendered categorical/sequential/diverging examples; CVD/human-task evidence; light/dark, browser/device and multi-project validation |

## Latest completed block — C005

`C005-icc-cmm-roundtrip-validation.md` converts Study 012's chromatic-adaptation theory into an actual profile/CMM execution and a documented failure-analysis cycle.

### Controlled environment

- Python `3.13.5`
- Pillow `12.3.0`
- Pillow `ImageCms`
- LittleCMS reported by ImageCms: `2.19`
- generated sRGB v4.4 monitor profile connected through XYZ PCS
- generated Lab identity profile used as a controlled D50 observation path

### Profile architecture evidence

The generated sRGB profile reports media white `[0.9642, 1.0, 0.8249]` and exposes a D65→D50 `chad` matrix.

Applying that `chad` to the standard sRGB D65 white returns D50 to floating-point precision. Applying the same `chad` to the standard sRGB D65 primary matrix reconstructs the profile's stored D50 red/green/blue colorants with maximum absolute residual:

`4.44 × 10⁻16`.

Professional consequence: the controlled profile is internally coherent with the ICC v4 architecture studied in Study 012.

### CMM vs independent colorimetry

A 17-step/channel RGB cube (`4,913` colors) compared:

`8-bit sRGB → inverse transfer → XYZ D65 → profile chad → XYZ D50 → hand CIELAB`

against:

`8-bit sRGB → ICC profile → LittleCMS relative-colorimetric transform → 8-bit Lab`.

Maximum absolute CMM-vs-hand differences:

- `L*`: `0.19773`
- `a*`: `0.50508`
- `b*`: `0.50513`

Those limits align with the tested 8-bit Lab quantization step, so the observed CMM output is consistent with the independent calculation within the precision of the observation buffer.

### Failure → diagnosis → revision

The same grid was round-tripped through `sRGB 8-bit → Lab 8-bit → sRGB 8-bit`.

Observed:

- maximum single-channel error: `36` RGB codes;
- mean absolute channel error: `1.5289`;
- 95th percentile: `7`;
- exact RGB recovery: `8.24%`;
- all channels within ±1: `47.26%`;
- all channels within ±2: `60.51%`.

The first shortcut diagnosis — “the CMM/adaptation is inaccurate” — was rejected because the direct CMM-vs-hand Lab comparison agreed to the expected 8-bit Lab quantization envelope.

Revised diagnosis: the round-trip mixes low-precision Lab quantization, nonlinear RGB re-encoding, gamut-boundary sensitivity and the transform path. Profile-managed does not mean lossless.

### Matrix-comparison discipline

C005 also found a small difference between the Study 012 published ICC D65→D50 matrix and the generated profile's `chad`. Rather than calling it a contradiction, the matrices were traced to slightly different adopted-white constants/rounding. New studio rule: **compare white definitions and generation assumptions before comparing CAT matrix coefficients.**

Evidence level: **PRACTICE + PRODUCTION-PATH VALIDATION / real LittleCMS profile transform and failure analysis**. Not high-precision, real-device/profile, cross-CMM or production PASS.

## Previous completed block — C004

`C004-spectral-integration-observer-metamerism.md` supplies controlled CIE 1931 spectral integration, scaling, a constructed CIE 1931 metamer pair, CIE 1931↔1964 observer comparison and dataset-provenance audit.

Professional conclusion: a colorimetric match is conditional on the observer/system defining the match; this does not predict individual observers and does not replace the observer model embedded in production standards.

## Project-facing blocks

### C003 — data visualization

Established data-type-driven choice among qualitative/categorical, sequential and diverging systems; meaningful diverging midpoint requirements; rainbow failure analysis; numerical monotonicity practice; redundant coding; missing/reference/state separation; and production validation criteria.

### C002 — semantic color/token architecture

Established `primitive → semantic role → optional component role → context resolution`, pair contracts, domain-status vs interaction-state separation, and semantic-collision review.

### C001 — Web override resilience

Established forced-colors/system-color/theme resilience requirements and a Color→Web implementation-validation matrix.

## Peer evidence currently affecting Color

### Typography / Type

Type is through **T004**. T004 provides a complete research numeral/punctuation system, proportional/tabular metrics, zero alternatives, actual FreeType evidence, and a compact colon failure→redraw cycle.

Color consequences:

- chart labels, numeric readouts and dense status text should not be validated with placeholder typography only;
- T003/T004 alpha/raster evidence is a strong future transfer case for light/dark/reduced-contrast/environmental Color testing;
- C005 adds a downstream layer: even correctly rasterized type can still be altered by export/profile/precision decisions in screenshots and marketing assets.

### Layout / Interaction

Layout has advanced L002 through a **216-condition Chromium density/reflow validation**. Naive compactness produced clipped/hidden content and below-contract controls; preserve/adaptive policies retained critical content and interaction geometry while exposing or reducing the true spatial cost. L002 now explicitly hands Color a fixed-geometry transfer target.

I001 remains a running state/navigation specimen with a documented failure→revision→re-proof cycle and 14/14 controlled assertions.

Color consequences:

- use L002 fixed/adaptive geometry to test color-driven visual density without changing layout;
- use I001 current-location/focus/pending/error/success as C001/C002 semantic-color targets;
- do not use color to repair unclear geometry or state models.

### Web Design

At the latest synchronization, Web remains Stage 1 / not yet baselined and no substantive `W###` study is available. **Do not invent Web evidence.**

C001–C003 and Studies 016/017 provide browser/theme/gamut contracts. C005 adds a concrete asset/export color-management handoff: profile-tagged images, screenshots, P3/sRGB assets, canvas/export paths and profile retention/stripping should be tested in real browsers once Web research begins.

## Incoming dependencies

- Type may require measured contrast/luminance/viewing-condition and downstream asset-pipeline evidence for real text, numerals and chart labels.
- Layout & Interaction may require state/focus color contracts, luminance hierarchy, color-vision independence, chart-density evidence and environmental constraints.
- Web Design may require semantic token, chart palette, forced/system-color, gamut/fallback, ICC asset/export and device/viewing-condition guidance.

## Cross-domain opportunities

### Type

Composite T003/T004 renderer alpha evidence under Color-defined light/dark/background/environment conditions, then carry representative raster assets through controlled profile/export pipelines to separate renderer failure from color-management failure.

### Layout / Interaction

Use L002's fixed adaptive geometry for a controlled Color→Layout transfer: vary luminance/chroma/state roles while holding geometry/content constant. Use I001 semantic states for forced-color and semantic-collision tests.

### Web Design

When W### work exists:

- transfer-test C001–C003 and Studies 016/017 in real browsers;
- test profile-tagged sRGB/P3 image assets, screenshots, canvas/export behavior and profile retention/stripping informed by C005;
- return confirmation, limitation, contradiction or transfer failure rather than silently changing Color assumptions.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. Convert C002 into practice with semantic token graphs and pair/contrast matrices for at least two materially different products, recording collisions and rejected architectures.
2. Use L002's fixed geometry for a Color-driven density/salience transfer study: vary luminance/chroma/semantic-state treatment while keeping geometry/data constant.
3. Convert C003 into rendered practice: categorical + sequential + diverging visualizations in light/dark conditions with grayscale/CVD/small-mark/state critique and at least one failure→revision cycle.
4. Extend C005 with float/16-bit transforms, independently sourced/real output profiles, P3→sRGB and display→print paths, soft proof and a second CMM/toolchain where practical.
5. Extend C004 from sparse lines to complete smooth/measured spectra with independently hash-verified current CIE datasets; complete current CIE 2006 LMS/cone comparison only after provenance is verified.
6. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not declare a universal winner.
7. Validate non-text/focus/ramp and T003/T004 transfer evidence on physical displays under controlled bright/low-light conditions.
8. Transfer C001/C002/C003/C005 and Studies 016/017 into real browser validation when substantive Web evidence becomes available.
9. Continue advanced data visualization later into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization.
10. Open `C006` for the next substantial new Color question when justified.

## Open research-quality gaps

- C002 multi-product semantic-system practice and collision evidence;
- fixed-geometry Color→Layout density/salience transfer using L002;
- C003 rendered/CVD/human-task evidence;
- float/high-bit-depth ICC/CMM validation and actual source/destination profiles;
- P3→sRGB, display→print, soft-proof and cross-CMM evidence;
- full checksum-verified spectral integration on complete smooth/measured spectra;
- current CIE 2006 LMS/cone-fundamental numerical comparison and broader observer-diversity evidence;
- real browser implementation evidence for modern CSS color, gamut mapping, forced/system colors, token resolution and ICC-tagged assets;
- physical-display/environmental testing;
- cyclic/uncertainty/bivariate/advanced data visualization;
- automated Color QA tied to product acceptance criteria;
- cultural/localization evidence beyond generic color folklore;
- multi-project transfer evidence at production fidelity.

## Current handoffs to other specialists

### Typography / Type

- C005 adds downstream color-management/precision risk after glyph rasterization; this complements T003/T004 renderer-layer evidence.
- Validate C002 foreground roles and C003 axes/labels/numerals with actual font metrics/rasterization.
- Scope limit: Color does not define font construction, metrics or hinting.

### Layout / Interaction

- L002 is now a high-value fixed-geometry Color transfer matrix. Color should vary luminance/chroma/state treatment without changing layout before drawing conclusions about visual density.
- I001 state semantics remain the correct target for C001/C002; color should encode, not redefine, pending/error/success/focus/current state.
- C005 adds a diagnostic caution for screenshots/exports: downstream color-management failure must not be mistaken for a geometry/state failure.
- Scope limit: Color does not redefine navigation/state/task semantics.

### Web Design

- Implement and challenge C001/C002/C003 in actual page/component/chart systems when Web research begins.
- Test P3/OkLCh/CSS gamut and fallback behavior from Studies 016/017.
- C005: test embedded-profile sRGB/P3 images, screenshots/exports, canvas paths and profile retention/stripping in actual browsers/OS/device conditions.
- C004: do not substitute alternate observer research into CSS/sRGB/P3 definitions; use it only to identify device/spectral risk.
- Return browser/device/framework confirmations, limitations, contradictions or transfer failures explicitly.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim peer ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `C001`: Web color override resilience and validation matrix.
- `C002`: semantic color/token architecture and project-readiness method.
- `C003`: data-type-driven visualization color systems and numerical scale practice.
- `C004`: CIE 1931 spectral integration/scaling/metamer practice, 1931↔1964 observer comparison, and dataset-provenance audit.
- `C005`: actual v4 ICC profile/CMM D65→D50 validation, 4,913-color CMM-vs-hand comparison, and 8-bit Lab round-trip failure diagnosis.
- `Chromatic adaptation / ICC color management` advances to **PRACTICE / CRITIQUE**, not PASS.
- Next Color study ID: `C006`.
- Overall Color state remains **CRITIQUE / Foundation NOT PASSED**.
