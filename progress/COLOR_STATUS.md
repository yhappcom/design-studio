# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/color/`  
Next new-study ID: `C013`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Color research exists to improve real app, web, and product decisions. Research volume, palette count, token count, or curriculum speed are not success metrics.

When a project arrives, accumulated evidence must become project-specific guidance on palette systems, semantic color, data-visualization color, colorimetry, luminance/contrast, rendered text-color robustness, visual salience, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, ICC/color-management pipelines, spectral/device evidence, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research remains ACTIVE. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, statistics, display technology, frontend/browser behavior, measurement technology, and implementation knowledge may be studied when it materially improves Color judgment, replication, transfer validation, or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**  
Overall state: **CRITIQUE**  
Foundation: **NOT PASSED**

The Color program now spans UI color, luminance/contrast, colorimetry and observer models, chromatic adaptation, ICC/CMM production paths, perceptual spaces/difference, gamut mapping, perceptual ramp authoring, browser/user overrides, semantic token architecture, multi-context semantic transfer, data-visualization color, observer-conditional metamerism, fixed-geometry salience/density transfer, Type→Color rendered-role transfer, high-precision Display-P3→sRGB production validation, forced-colors state/SVG transfer, and **checksum-aware full-spectrum/spectral-sampling practice**.

Major unresolved gates remain: real human/CVD-observer evidence, current CIE 1964 raw-byte verification, resolved current CIE 2006 LMS identity, measured physical SPDs, real device/output profiles, second-CMM proof, browser/OS wide-gamut and real high-contrast transfer, soft-proof/print evidence, physical-display/environmental testing, production webfont/load behavior, and production-fidelity multi-project transfer.

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
- `research/color/C012-spectral-provenance-sampling-resolution.md`
- `research/color/C012-spectral-provenance-sampling-resolution.py`
- `research/color/C012-spectral-provenance-sampling-results.json`

Retained earlier Color exercises remain under `product-design/exercises/`.

---

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts; human salience/reading evidence |
| Encoded RGB → linear-light → XYZ | PRACTICE / CRITIQUE | wider production/browser/device transfer |
| Spectral colorimetry / observer models | **PRACTICE / PROVENANCE VALIDATION / CRITIQUE** | C004 sparse metamer/1931↔1964 proof + C012 current-1931 checksum reconstruction, full 360–830 smooth-SPD integration and sampling stress complete; current-1964 raw MD5, resolved CIE 2006 LMS identity, measured SPDs, instruments, physical device/human validation pending |
| Chromatic adaptation / ICC color management | PRACTICE / PRODUCTION-PATH VALIDATION | C005 D50 PCS/`chad` + C010 float/16/8-bit P3→sRGB proof complete; real output/device profiles, second CMM, soft proof/print and physical-output validation pending |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | PRACTICE / CRITIQUE | C010 destination-gamut/precision separation complete; actual browser/OS/device P3 fallback and product acceptance behavior pending |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C001 + I003 + C011 controlled Chromium evidence; real Windows High Contrast, multi-browser/OS/AT/production-token validation pending |
| Semantic color/token architecture | PRACTICE / TRANSFER VALIDATION | C006 two-context graph/collision/pair-matrix proof complete; production component/theme/browser and real-project transfer pending |
| Color-driven visual density / salience | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C007 + independent Layout L005 compatible findings; human perceived-clutter/search/comparison, cross-browser/device and physical-environment validation pending |
| Data-visualization color systems | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C008 rendered light/dark + C011 forced-colors SVG transfer complete; human interpretation, real CVD observers, production chart library, canvas, multi-browser/device and multi-project validation pending |
| Type-dependent Color rendering / text-role transfer | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C009 weight/fallback/DPR/contrast-margin proof complete; human readability, production webfont loading, broader scripts/platforms/devices/environment pending |

---

## Latest completed block — C012 spectral provenance and sampling resolution

`C012-spectral-provenance-sampling-resolution.md` extends C004 from sparse-line practice into complete synthetic spectra and makes dataset provenance an explicit calculation gate.

### Current CIE 1931 provenance upgraded

Pinned source:

- `wetadigital/physlight` commit `9d076d1074aad7257c04c39581a4d21f97fd2527`;
- Git blob `9b4e3f73b4bb412a762a6d03cb8060bfea652a6e`;
- 471 rows, 360–830 nm, 1 nm.

The connector-normalized LF serialization has MD5 `5a60da02f27032ef3c050dfd1e913f0f`. Reconstructing the CRLF serialization indicated by the pinned blob gives:

`17cca777db64b17170f06f67ce9d3ab7`

which exactly equals the current CIE-published 1931 MD5.

This advances the 1931 evidence from metadata matching to **independently recomputed checksum reconstruction tied to an immutable mirror blob**. The CIE host remains the canonical authority.

### CIE 1964 provenance remains intentionally asymmetric

A known older mirror reports MD5 `6140e032f9326d88c5a0959b29b4d8f3`, which differs from the current CIE-published `cd6135a724480eb8c5e7668bae914445` and is rejected as current authority.

A pinned current-metadata-matched mirror was found at `chran554/pathtracer` commit `ec602c93c253c7d88646e5a7551ac554c75f46d0`, blob `d3040193ae654fe5fc33ea0e1f1a7b24c45fca9c`; its metadata reports the current MD5 and SHA-256 `c800ae88d20868427e09482d7b5c026e7f5001dc00bec18cd9dcd3a0006da396`.

However its raw MD5 was not independently recomputed in this execution, so C012 does **not** claim the same provenance tier as 1931.

### CIE 2006 LMS remains blocked

Accessible pinned LMS copy CRLF reconstruction:

`dba2e9d1f5e6667575aa069832159510`

Current CIE-published MD5:

`27c74cc0f98edecadc02fc71f540b116`

A separate public run reports the same mismatch pair. C012 therefore refuses to publish a current-CIE LMS numerical comparison until authoritative identity is resolved.

### Full 360–830 nm practice

Four synthetic emissive SPDs were integrated over the checksum-strengthened CIE 1931 1 nm table:

- broad warm;
- broad cool;
- narrow display-like diagnostic;
- ultra-narrow laser-like diagnostic.

The broad and narrow-display-like cases were stable under a simple 5 nm phase-offset subsampling diagnostic. The ultra-narrow test was not: worst `Δxy ≈ 0.001920`, with maximum absolute relative Y error about `0.004559` (`0.456%`).

Professional consequence: **neither `5 nm is always enough` nor `5 nm is always inadequate` is defensible.** Spectral bandwidth, peak location, measurement method, instrument response and acceptance tolerance determine whether sample resolution is material.

### Evidence boundary

The 5 nm experiment is a mathematical sampling-grid diagnostic, not a model of spectroradiometer optical bandwidth, wavelength accuracy, stray light or noise. The SPDs are synthetic, not measured devices. `Δxy` is not a perceptual difference metric.

### Evidence level

**PRACTICE + PROVENANCE VALIDATION / current-1931 checksum reconstruction + complete synthetic SPD integration + sampling-resolution stress test.**

Not PASS: current-1964 independent raw hash, resolved CIE 2006 LMS identity, measured physical SPDs, instrument validation, physical displays and human observers remain open.

---

## Previous key blocks

### C011 — forced-colors semantic/data resilience

Controlled Chromium HTML/SVG/focus testing produced 21/21 bounded assertions. Default inline SVG preserved authored paint under `preserve-parent-color`; explicit `forced-color-adjust:auto` changed actual raster used colors even while computed stroke still showed authored values. Structural labels/patterns/markers survived color removal; global `forced-color-adjust:none` was rejected.

### C010 — high-precision Display-P3→sRGB

35,937 P3 samples were tested through LittleCMS float/16-bit/8-bit paths. In-gamut float output agreed with independent colorimetry to about `10^-8`; extended float reversibility was separated from bounded destination delivery; cross-profile differences were measured without mislabeling them as cross-CMM/device proof.

### C009 — Type→Color rendered-role transfer

Same foreground/background pair can produce materially different raster mass under weight/fallback/DPR. Korean fallback can change width, coverage and wrap while Color remains unchanged. Contrast conformance and rendered robustness remain separate gates.

### C008 — rendered data visualization

Categorical identity/selection, sequential ordering, diverging midpoint/missing-data, light/dark remapping and CVD diagnostics have controlled rendered failure→revision evidence. C011 adds forced-colors SVG transfer.

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
- C011 direct labels still require production Type/fallback/normalization proof;
- C012 reinforces the same general discipline: provenance of the input artifact precedes downstream visual interpretation.

Color does not own font construction, shaping, fallback, normalization policy or release QA.

### Layout / Interaction

Layout/Interaction is through **L006/I004** at the latest synchronization.

Relevant consequences:

- I003 is directly confirmed and extended by C011;
- L005 independently confirms C007's separation of spatial density, feature variability and semantic collision;
- L006 shows visual appearance and behavioral ownership can diverge, reinforcing layer-specific diagnosis;
- I004 adds conflict/merge/recovery semantics that Color may encode but not redefine.

### Web Design

Web still lists **W001** as next and has no substantive W### evidence at this checkpoint. **Do not invent Web PASS.**

C010/C011/C012 now give Web three future transfer contracts: wide-gamut/color-management behavior, forced-colors/SVG policy, and actual-device spectral risk screening where narrow-primary brand fidelity matters.

---

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **C013 candidate — resolve/extend spectral observer evidence:** independently hash the current CIE 1964 raw file; resolve the CIE 2006 LMS checksum/file identity if possible; only then compare the same complete spectra across verified observer/cone models.
2. Acquire at least one measured display/LED/projector SPD and instrument metadata, then replace C012's mathematical 5 nm subsampling diagnostic with a real measurement-resolution/bandwidth case when available.
3. Extend C011 into real Windows High Contrast/Edge and additional browser/OS conditions; include production SVG/canvas chart libraries and localized labels.
4. Extend C010 with a measured/device or independently sourced Display-P3/output profile, second CMM, browser/OS wide-gamut path, and soft-proof/print evidence.
5. Extend C007/C008/C009/C011 with human tasks when participants are available: search, comparison, series identification, text-role recognition, missing/reference interpretation; keep performance separate from preference/workload.
6. Validate non-text/focus/ramp/chart/Type transfer on physical displays under controlled bright/low-light conditions.
7. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not declare a universal winner.
8. Transfer C001–C012 and Studies 016/017 into real Web/browser validation when substantive W### evidence becomes available.
9. Continue advanced data visualization into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization after current rendered/human gaps are addressed.
10. Build automated Color QA only when tied to real project acceptance criteria; no screenshot/raster/salience/CVD/CMM/forced-colors/spectral proxy becomes a generic score without validation.

---

## Open research-quality gaps

- current CIE 1964 raw-byte MD5 recomputation;
- resolution of current CIE 2006 LMS published-checksum versus accessible-copy identity;
- verified complete-spectra 1931↔1964↔cone-fundamental comparison;
- measured display/LED/projector SPDs and instrument bandwidth/calibration evidence;
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
- physical-display/environmental testing;
- cultural/localization evidence beyond generic color folklore;
- production-fidelity multi-project evidence.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- C012 adds a Color-side provenance lesson parallel to T013/T014: downstream visual claims should name the exact source artifact/data representation.
- Future physical-display Type proof should record the display/device/viewing condition, not only the semantic foreground/background token.
- Scope limit: C012 makes no font-quality or legibility claim.

### Layout / Interaction

- C012 strengthens layer-specific diagnosis: spectral fidelity does not replace semantic redundancy, focus, navigation or layer ownership.
- C011 remains the direct Color→Interaction forced-colors handoff.
- Scope limit: no user task or Interaction behavior was tested in C012.

### Web Design

- C012 provides a risk screen for when a wide-gamut web/brand problem may justify actual device/SPD evidence rather than only CSS coordinates.
- C011 supplies SVG forced-color acceptance cases; C010 supplies P3/sRGB color-management cases; C009 supplies Type/fallback/DPR Color-role cases.
- Return confirmations, limits, contradictions or transfer failures when substantive W### work begins.

## Latest checkpoint

- C001: browser/user color override resilience.
- C002: semantic token architecture.
- C003: data-visualization source framework.
- C004: CIE 1931 sparse spectral integration/metamer + 1931↔1964 observer comparison.
- C005: ICC v4 D50 PCS/CMM and low-precision failure diagnosis.
- C006: two-context semantic-token transfer.
- C007: fixed-geometry Color→Layout salience/density transfer.
- C008: rendered categorical/sequential/diverging chart validation.
- C009: Type→Color raster/fallback/DPR transfer.
- C010: float/16-bit/8-bit Display-P3→sRGB CMM validation and delivery-boundary semantics.
- C011: forced-colors HTML state/focus + SVG preserve/auto/opt-out transfer, computed-vs-used-value raster proof, 21/21 bounded assertions.
- **C012: current-CIE-1931 checksum reconstruction + complete 360–830 nm synthetic SPD integration + 5 nm phase/spectral-bandwidth stress; current 1964 byte verification and CIE 2006 LMS identity remain explicitly OPEN.**
- Next Color study ID: **C013**.
- Overall Color state remains **Stage 1 + early Intermediate bridge / CRITIQUE / Foundation NOT PASSED**.
