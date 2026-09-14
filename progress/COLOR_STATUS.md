# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/color/`  
Next new-study ID: `C012`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Color research exists to improve real app, web, and product decisions. Research volume, palette count, token count, or curriculum speed are not success metrics.

When a project arrives, accumulated evidence must become project-specific guidance on palette systems, semantic color, data-visualization color, colorimetry, luminance/contrast, rendered text-color robustness, visual salience, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, ICC/color-management pipelines, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research remains ACTIVE. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, statistics, display technology, frontend/browser behavior, and implementation knowledge may be studied when it materially improves Color judgment, replication, transfer validation, or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**  
Overall state: **CRITIQUE**  
Foundation: **NOT PASSED**

The Color program now spans UI color, luminance/contrast, colorimetry and observer models, chromatic adaptation, ICC/CMM production paths, perceptual spaces/difference, gamut mapping, perceptual ramp authoring, browser/user overrides, semantic token architecture, multi-context semantic transfer, data-visualization color, observer-conditional metamerism, fixed-geometry salience/density transfer, Type→Color rendered-role transfer, high-precision Display-P3→sRGB production validation, and forced-colors state/SVG transfer.

Major unresolved gates remain: human/CVD-observer evidence, independently verified complete spectral/cone datasets, real device/output profiles, cross-CMM proof, browser/OS wide-gamut and real high-contrast transfer, soft-proof/print evidence, physical-display/environmental testing, production webfont/load behavior, and production-fidelity multi-project transfer.

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
- `research/color/C011-forced-colors-semantic-data-resilience.md`
- `research/color/C011-forced-colors-semantic-data-specimen.html`
- `research/color/C011-forced-colors-semantic-data-playwright.py`
- `research/color/C011-forced-colors-semantic-data-results.json`

Retained earlier Color exercises remain under `product-design/exercises/`.

---

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts; human salience/reading evidence |
| Encoded RGB → linear-light → XYZ | PRACTICE / CRITIQUE | wider production/browser/device transfer |
| Spectral colorimetry / observer models | PRACTICE / CRITIQUE | C004 sparse-line integration/metamer + 1931↔1964 proof complete; full smooth/measured spectra, independently hash-verified current files, current CIE 2006 LMS/cone comparison, physical-device validation pending |
| Chromatic adaptation / ICC color management | PRACTICE / PRODUCTION-PATH VALIDATION | C005 D50 PCS/`chad` + C010 float/16/8-bit P3→sRGB proof complete; real output/device profiles, second CMM, soft proof/print and physical-output validation pending |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | PRACTICE / CRITIQUE | C010 destination-gamut/precision separation complete; actual browser/OS/device P3 fallback and product acceptance behavior pending |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | **PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION** | C001 + I003 + C011 controlled Chromium evidence; real Windows High Contrast, multi-browser/OS/AT/production-token validation pending |
| Semantic color/token architecture | PRACTICE / TRANSFER VALIDATION | C006 two-context graph/collision/pair-matrix proof complete; production component/theme/browser and real-project transfer pending |
| Color-driven visual density / salience | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C007 + independent Layout L005 compatible findings; human perceived-clutter/search/comparison, cross-browser/device and physical-environment validation pending |
| Data-visualization color systems | **PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION** | C008 rendered light/dark + C011 forced-colors SVG transfer complete; human interpretation, real CVD observers, production chart library, canvas, multi-browser/device and multi-project validation pending |
| Type-dependent Color rendering / text-role transfer | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C009 weight/fallback/DPR/contrast-margin proof complete; human readability, production webfont loading, broader scripts/platforms/devices/environment pending |

---

## Latest completed block — C011 forced-colors semantic/data resilience

`C011-forced-colors-semantic-data-resilience.md` extends C001 and C008 and independently transfer-validates Interaction I003.

### Controlled environment

- Chromium `144.0.7559.96`;
- Playwright forced-colors emulation;
- headless Linux;
- viewport `1200×720`;
- DPR `1`;
- HTML state/focus specimens plus inline SVG charts;
- computed-style and raster screenshot evidence.

This is bounded Chromium evidence, not Windows High Contrast, Firefox/Safari, AT, or production-device PASS.

### HTML state-color collapse

Naive pending/failed/confirmed fills were distinct in normal mode but all resolved to white in the forced-color rendering used by this specimen. The robust variant retained visible text labels and structural border/symbol distinctions.

Professional consequence: semantic state must survive when literal state fill is replaced.

### Focus failure/revision

Naive focus used only a box-shadow glow with outline removed. Under forced colors:

- `box-shadow: none`;
- outline remained absent.

The revised focus retained a `3px` structural outline whose literal color was system/browser resolved.

Professional consequence: shadow/glow must not be the only focus channel.

### SVG contradiction refinement

Default inline SVG did **not** behave like ordinary HTML state fills.

Chromium reported `forced-color-adjust: preserve-parent-color` on the default SVG paths and raster evidence retained all four authored series colors:

- red exact pixels: `827`;
- green: `881`;
- blue: `920`;
- purple: `913`.

This refines the earlier broad hypothesis: **forced colors does not automatically collapse every SVG chart series.**

### Explicit SVG `auto`

When C011 set `forced-color-adjust:auto` on the SVG and descendants, screenshot raster analysis found zero exact pixels for all four authored series colors.

Important implementation lesson: `getComputedStyle(...).stroke` still exposed the authored stroke values in this run, while the actual raster used different forced colors. The specification's computed-vs-used distinction therefore matters in practical QA.

Professional consequence: source/computed-style inspection alone can miss real forced-color substitution.

### Revised chart after color removal

The robust `auto` chart retained:

- four dash patterns;
- four marker geometries;
- direct series labels;
- explicit `C selected` label;
- selected series width `6px` versus `3px` peers.

Data identity and selection therefore remained structurally represented even after author colors were removed.

### Opt-out result

`forced-color-adjust:none` preserved the authored `#A8F0E9` on `#0D1317` specimen. This proves author control, **not accessibility**.

Studio rule: no global opt-out. Use `none` only for a bounded element with explicit accessibility reasoning and its own validation.

### Automated result

Final harness: **21 / 21 bounded assertions PASS.**

The passing assertions cover reproduced failures and revised resilience; they do not constitute production or human-comprehension PASS.

### Evidence level

**PRACTICE + CROSS-DOMAIN TRANSFER VALIDATION / controlled Chromium forced-colors + SVG used-value raster verification + failure→revision.**

Not PASS: no real Windows High Contrast, Firefox/Safari/Edge matrix, AT, human identification tasks, production chart library/canvas, localized direct-label proof, or physical-device evidence.

---

## Previous key blocks

### C010 — high-precision Display-P3→sRGB

35,937 P3 samples were tested through LittleCMS float/16-bit/8-bit paths. In-gamut float output agreed with independent colorimetry to about `10^-8`; extended float reversibility was separated from bounded destination delivery; cross-profile differences were measured without mislabeling them as cross-CMM/device proof.

### C009 — Type→Color rendered-role transfer

Same foreground/background pair can produce materially different raster mass under weight/fallback/DPR. Korean fallback can change width, coverage and wrap while Color remains unchanged. Contrast conformance and rendered robustness remain separate gates.

### C008 — rendered data visualization

Categorical identity/selection, sequential ordering, diverging midpoint/missing-data, light/dark remapping and CVD diagnostics have controlled rendered failure→revision evidence. C011 now adds forced-colors SVG transfer.

### C007 — fixed-geometry salience/density

Distributed chroma can change the rendered feature field without geometry changes; zero-chroma high-luminance segmentation can remain visually forceful. `desaturate = declutter` is rejected as a universal rule.

### C006 — semantic token transfer

Two materially different product archetypes confirm that semantic-role method transfers while literal palettes do not. Brand/action/selection/focus/status collisions are explicitly rejected.

### C005/C004/C001–C003

C005 covers ICC v4 D50 PCS/CMM diagnostics; C004 covers observer-conditional metamerism; C001 covers user/browser color override resilience; C002 semantic token architecture; C003 data-visualization source semantics.

---

## Peer evidence currently affecting Color

### Typography / Type

Type is through **T014**, next ID T015.

Relevant consequences:

- T005/C009 establish fallback/raster dependence beneath fixed Color roles;
- T013/T014 add normalization-sensitive Latin/Hangul package closure;
- C011's direct-label strategy therefore still requires actual production Type/fallback/normalization proof before release.

Color does not own font construction, shaping, fallback, normalization policy or release QA.

### Layout / Interaction

Layout/Interaction is through **L006/I004** at the latest synchronization.

Relevant consequences:

- I003 is directly confirmed and extended by C011;
- L005 independently confirms the C007 separation of spatial density, feature variability and semantic collision;
- L006 shows visual layer appearance and behavioral ownership can diverge, reinforcing the rule that Color must not substitute for interaction ownership;
- I004 adds conflict/merge/recovery semantics that Color may encode but not redefine.

### Web Design

Web still lists **W001** as next and has no substantive W### evidence at this checkpoint. **Do not invent Web PASS.**

C011 adds a concrete Web validation contract for SVG `preserve-parent-color`, explicit `forced-color-adjust:auto`, system colors, opt-out policy, real Windows High Contrast and production chart libraries.

---

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **C012 candidate — complete spectral/cone-data provenance and smooth-spectrum practice:** retry current official CIE numerical datasets; only proceed to CIE 2006 LMS comparison after checksum/provenance verification.
2. Extend C011 into real Windows High Contrast/Edge and additional browser/OS conditions when available; include production SVG/canvas chart libraries and localized labels.
3. Extend C010 with an actual measured/device or independently sourced Display-P3/output profile, second CMM, browser/OS wide-gamut path, and soft-proof/print evidence when available.
4. Extend C007/C008/C009/C011 with human tasks when participants are available: search, comparison, series identification, text-role recognition, missing/reference interpretation; keep performance separate from preference/workload.
5. Validate non-text/focus/ramp/chart/Type transfer on physical displays under controlled bright/low-light conditions.
6. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not declare a universal winner.
7. Transfer C001–C011 and Studies 016/017 into real Web/browser validation when substantive W### evidence becomes available.
8. Continue advanced data visualization into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization after current rendered/human gaps are addressed.
9. Expand observer-diversity/metamerism practice only with traceable datasets and explicit production relevance.
10. Build automated Color QA only when tied to real project acceptance criteria; no screenshot/raster/salience/CVD/CMM/forced-colors proxy becomes a generic score without validation.

---

## Open research-quality gaps

- real Windows High Contrast / Edge and broader browser forced/user-color evidence;
- assistive-technology behavior;
- production SVG/canvas chart-library transfer;
- human readability/low-vision and real-CVD-observer evidence;
- localized/direct-label stress with production fonts and normalization;
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

- C011 uses direct labels as a key non-color chart channel; their robustness depends on exact production fonts, fallback, shaping and normalization.
- C009 remains the main Color-side evidence that fixed semantic foreground pairs do not normalize raster mass.
- Scope limit: no font-quality ranking or shaping recommendation is inferred.

### Layout / Interaction

- C011 independently confirms I003's state/focus failure mechanism and adds data-viz/SVG policy.
- Shadow-only focus again fails; state meaning must survive literal color replacement.
- Color does not redefine Interaction state meaning or layer ownership.

### Web Design

- C011 supplies a specific acceptance matrix for default SVG `preserve-parent-color`, explicit `auto`, `none`, system-color adaptation, focus, and chart redundancy.
- C010 supplies P3/sRGB/browser/device color-management transfer requirements.
- C009 supplies font/fallback/DPR Color-role cases.
- Return confirmations, limits, contradictions or transfer failures when substantive W### work begins.

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
- C010: float/16-bit/8-bit Display-P3→sRGB CMM validation and delivery-boundary semantics.
- **C011: forced-colors HTML state/focus + SVG preserve/auto/opt-out transfer, computed-vs-used-value raster proof, 21/21 bounded assertions.**
- Next Color study ID: **C012**.
- Overall Color state remains **Stage 1 + early Intermediate bridge / CRITIQUE / Foundation NOT PASSED**.