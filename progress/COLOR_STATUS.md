# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/color/`  
Next new-study ID: `C009`

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

The Color program now spans UI color, colorimetry/observer models, chromatic adaptation, ICC/CMM production-path validation, perceptual spaces/difference, gamut mapping, ramp authoring, web override behavior, semantic token architecture, two-context semantic transfer, rendered data-visualization color, controlled observer-conditional metamerism, and fixed-geometry rendered salience/density transfer.

Foundation is **not passed**. Human/CVD-observer evidence, full checksum-verified spectral datasets, current cone-fundamental numerical validation, higher-precision/real-profile/cross-CMM production proof, broader browser/device evidence, physical-display/environmental tests, localization/Type chart transfer, and production-fidelity project transfer remain incomplete.

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

Retained earlier Color exercises remain under `product-design/exercises/`.

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
| Color-driven visual density / salience | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C007 fixed-geometry rendered proof complete; human perceived-clutter/search/comparison, CVD, localization/Type, cross-browser/device and physical-environment validation pending |
| Data-visualization color systems | **PRACTICE / CRITIQUE** | C008 rendered categorical/sequential/diverging light-dark failure→revision proof complete; human interpretation, real CVD observers, forced-colors, production chart library, Type/localization, cross-browser/device and multi-project validation pending |

## Latest completed block — C008

`C008-rendered-data-visualization-color-validation.md` converts C003 from numerical/project-readiness theory into matched browser-rendered chart evidence.

### Controlled setup

One specimen contains:

- a five-series categorical line chart with Series C selected;
- a 9-step sequential heat strip plus `6×6px` small-mark row;
- a diverging variance chart with values `[-3, 0, +2, +5, +8, +12, N/A]`.

Four matched conditions are rendered:

- light / failure;
- light / revised;
- dark / failure;
- dark / revised.

Environment:

- Chromium `144.0.7559.96`;
- viewport `1280×820`;
- DPR 1;
- SVG rendering.

All panel/chart rectangles remain identical across conditions.

### Categorical failure → revision

Failure:

- `1.5px` hue-only lines;
- no markers;
- no direct labels;
- selected Series C has identity `#2C7BB6` but is recolored to interaction accent `#E69F00`.

Revision:

- `2.5px` identity lines;
- distinct dash/marker strategies;
- direct end labels;
- selected Series C retains identity `#009E73` and receives a separate selection halo.

Professional conclusion: **data identity and interaction emphasis are separate semantic axes.** Selection should not silently rewrite category identity unless that loss is explicitly acceptable.

### CVD diagnostic

Minimum pairwise Oklab distances among five series colors:

| Model | Failure | Revised |
| --- | ---: | ---: |
| Normal | `0.16961` | `0.15582` |
| Protanopia simulation | `0.04507` | `0.09554` |
| Deuteranopia simulation | `0.03302` | `0.07609` |
| Tritanopia simulation | `0.04056` | `0.08542` |

The revised palette slightly reduces the normal-model minimum while materially increasing the minimum under all three severity-1 Machado simulations. This is a useful **trade-off**, not a universal threshold.

CVD simulation and Oklab distance are diagnostics only; they are not real-observer identification evidence.

### Sequential failure → light/dark revision

Failure rainbow Oklab-L path:

`0.4520 → 0.6152 → 0.9054 → 0.8751 → 0.8664 → 0.8907 → 0.9680 → 0.7319 → 0.6280`

Direction reversals: `3`.

Revised light YlGnBu path:

`0.9904 → 0.9542 → 0.8960 → 0.7926 → 0.7171 → 0.6179 → 0.4837 → 0.3795 → 0.2604`

Direction reversals: `0`.

Revised dark context-specific low-yellow/olive → high-blue/cyan path:

`0.2789 → 0.3770 → 0.4589 → 0.5367 → 0.6117 → 0.6981 → 0.7742 → 0.8483 → 0.9300`

Direction reversals: `0`.

Professional conclusion: dark-theme data color should preserve **analytical ordering and semantic endpoints**, not literal pixels. A separate dark mapping can change luminance strategy without inverting the meaning of low/high.

The `6×6px` row is a render stress case only; human small-mark discriminability remains OPEN.

### Diverging midpoint + missing-data failure → revision

Failure centers the color scale at observed range midpoint `+4.5` instead of the domain reference `0`.

For `[-3, 0, +2, +5, +8, +12, N/A]`, failure visual classes are:

`negative, negative, negative, positive, positive, positive, missing`

instead of:

`negative, center, positive, positive, positive, positive, missing`.

Mismatch count: `2` (`0` and `+2`).

Failure also maps `N/A` to the midpoint color, making missing data resemble a valid neutral value.

Revision:

- explicit zero midpoint;
- independent scaling on unequal negative/positive ranges;
- signed value labels;
- zero/reference line;
- `N/A` cross/outline outside the quantitative scale.

Revised mismatch count: `0` in light and dark.

Professional conclusion: **a diverging midpoint is part of the data model, not a palette convenience.** Missing data must not silently enter the numeric scale.

### Evidence level

**PRACTICE + CRITIQUE / controlled Chromium SVG rendering + failure→revision + bounded CVD/ordering/semantic diagnostics.**

Not PASS: human interpretation, real CVD observers, forced-colors, production chart libraries, actual Type/localization, cross-browser/device/export, physical viewing, and multi-project transfer remain incomplete.

## Previous completed block — C007

C007 holds dense interface content/geometry constant while changing only Color. Its key controlled result is that chroma-overloaded treatment greatly increases distributed chroma variation, while a zero-chroma high-contrast monochrome control can create even stronger luminance segmentation. Therefore `desaturate = declutter` is rejected as a universal rule.

C007's semantic-sparse condition retained strong local primary-action separation while using much less page-wide chroma. Human clutter/task claims remain OPEN.

## Previous project/science blocks

### C006 — semantic token transfer

Two materially different product archetypes reject overloaded brand/action/selection/status mappings and confirm that the semantic-role **method** transfers while literal palettes do not.

### C005 — ICC/CMM production path

A real LittleCMS profile path validates the D65→D50 ICC architecture within the tested observation precision and separates low-bit-depth round-trip loss from CMM/adaptation error.

### C004 — observer/metamer practice

A constructed CIE 1931 metamer pair separates under CIE 1964 10°, demonstrating that colorimetric match is conditional on the specified observer/system.

### C003 — data visualization source framework

C003 defines categorical/sequential/diverging semantics, meaningful midpoint, rainbow failure analysis, redundant coding, missing/reference/state separation and production validation criteria. C008 now supplies the first controlled rendered proof.

### C002/C001 — semantic architecture / override resilience

C002 establishes primitive→semantic→optional component→context resolution and pair contracts. C001's forced-color failure hypothesis has been independently supported by Interaction I003 in Chromium.

## Peer evidence currently affecting Color

### Typography / Type

Type is through **T005**.

Color consequences:

- mixed Latin/Korean fallback can alter chart label size, width, line box and apparent mass while colors remain unchanged;
- T004 numerals/punctuation and T005 fallback strings are now direct C008 transfer targets;
- a direct-label chart only remains color-robust if the labels themselves survive actual Type/localization conditions.

### Layout / Interaction

Layout/Interaction is through **L005/I004** at the latest synchronization.

Important new overlap:

- `L005-color-driven-density-salience-transfer.md` independently studied a fixed-geometry finance surface and reached a compatible diagnosis: spatial density, feature variability, semantic emphasis distribution, and semantic collision must be separated. This is independent confirmation of the C007 problem framing, not evidence that either study has human-clutter PASS.
- I003 confirms that fill/shadow-only state semantics can collapse under Chromium forced colors.
- L004 shows that numeric font features can alter dense comparison geometry even when data values are unchanged.
- I004 adds conflict/deleted/merged state semantics that future Color work may encode but must not define.

For C008 specifically, I003 reinforces the rule that chart selection/focus/current states need structural redundancy beyond authored color.

### Web Design

At the latest synchronization, Web still lists `W001` as the next study and no substantive `W###` evidence exists. **Do not invent Web evidence.**

C008 now adds an SVG/light-dark/CVD/state chart-transfer contract to the existing Color→Web handoffs.

## Incoming dependencies

- Type may require measured color/viewing-condition evidence for real text, numerals, direct chart labels and localized labels.
- Layout & Interaction may require state/focus color contracts, color-vision independence, chart-density/salience evidence, and environmental constraints.
- Web Design may require semantic tokens, chart palettes, forced/system-color behavior, SVG/canvas/browser transfer, gamut/fallback, ICC asset/export and real page color-density guidance.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **C009 candidate — Type/localization transfer into Color:** apply T004/T005 numeric/Korean evidence to C006/C008 roles; test direct labels, legends, signed numbers, status text, wrapping, and selected/focused combinations without changing semantic Color jobs.
2. Extend C008 with forced-colors/high-contrast and alternate representation, using I003 as the state-resilience baseline; do not wait for Web if an independent Color check is useful, but label it Color-owned validation.
3. Extend C007/C008 with human tasks when participants are available: known-item search, series identification, value comparison, action finding, missing/reference interpretation; keep performance separate from preference/workload.
4. Extend C005 with float/high-bit-depth transforms, real/independent profiles, P3→sRGB and display→print paths, soft proof and a second CMM/toolchain where practical.
5. Extend C004 to complete smooth/measured spectra with independently hash-verified current CIE datasets; perform current CIE 2006 LMS comparison only after provenance is verified.
6. Compare Bradford/CAT02/CAT16 on explicitly bounded datasets; do not declare a universal winner.
7. Validate non-text/focus/ramp, chart, and Type transfer evidence on physical displays under controlled bright/low-light conditions.
8. Transfer C001–C008 and Studies 016/017 into real Web/browser validation when substantive W### evidence becomes available.
9. Continue data-visualization research into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization after the current rendered/human gaps are addressed.
10. Build automated Color QA only when tied to real product acceptance criteria; no simulation/proxy becomes a generic score without human validation.

## Open research-quality gaps

- C008 human interpretation/search/comparison and real-CVD-observer evidence;
- C008 forced-colors/chart-library/Type/localization/cross-browser/device/export transfer;
- C007 human perceived-clutter/search/comparison evidence;
- C006 real-project/rendered human validation;
- float/high-bit-depth ICC/CMM validation and actual source/destination profiles;
- P3→sRGB, display→print, soft-proof and cross-CMM evidence;
- full checksum-verified spectral integration on complete smooth/measured spectra;
- current CIE 2006 LMS/cone-fundamental numerical comparison and broader observer-diversity evidence;
- physical-display/environmental testing;
- cultural/localization evidence beyond generic color folklore;
- production-fidelity multi-project transfer evidence.

## Current handoffs to other specialists

### Typography / Type

- C008 now relies on direct labels, signed numeric text and `N/A` to avoid color-only semantics. These are high-value T004/T005 transfer cases.
- Test small chart labels, Korean long labels, fallback changes, tabular/proportional numerals, signs and punctuation while Color semantics remain fixed.
- Scope limit: Color does not define font metrics, fallback, feature settings or hinting.

### Layout / Interaction

- C008 categorical result: selection should preserve data identity and add a separate emphasis channel rather than replacing the series color.
- C008 diverging result: zero/reference/missing are data semantics that chart layout/interaction must preserve.
- L005 independently confirms the value of separating geometry, feature variability and semantic collision in dense surfaces.
- I003 remains the forced-color/state-resilience baseline for future chart work.
- Scope limit: Color does not define chart navigation, brushing, tooltip, focus order or interaction-state semantics.

### Web Design

- C008 supplies a reproducible SVG light/dark failure→revision specimen and chart-color acceptance matrix.
- Future Web validation should test real SVG/canvas libraries, responsive containers, browser zoom, forced/system colors, keyboard/focus/hover, production Type, multiple browsers/OS/devices, P3/sRGB and export.
- Continue C001/C002/C006 semantic/override transfer, C007 dense-page color transfer, Studies 016/017 wide-gamut transfer, and C005 embedded-profile/export transfer.
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
- `C007`: fixed-geometry rendered Color→Layout transfer; overloaded chroma vs semantic sparsity; zero-chroma luminance-overload contradiction control.
- `C008`: rendered categorical/sequential/diverging chart validation across light/dark, CVD diagnostic, selection-identity failure, semantic midpoint and missing-data revision.
- `Data-visualization color systems` advances to **PRACTICE / CRITIQUE**, not PASS.
- Next Color study ID: `C009`.
- Overall Color state remains **CRITIQUE / Foundation NOT PASSED**.
