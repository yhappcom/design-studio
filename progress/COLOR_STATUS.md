# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/color/`  
Next new-study ID: `C005`

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

The Color program now spans UI color, colorimetry and observer models, chromatic adaptation, perceptual spaces/difference, gamut mapping, ramp authoring, web override behavior, semantic token architecture, data-visualization color, and controlled observer-conditional metamerism practice.

Foundation is **not passed**. Full checksum-verified spectral datasets, current cone-fundamental numerical validation, ICC/CMM production proof, browser/device evidence, physical-display/environmental tests, CVD/human-task evidence, and multi-project transfer remain incomplete.

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
- retained product-design Color exercises 005, 009, 010, 012, 013, and 016.

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts |
| Encoded RGB → linear-light → XYZ | PRACTICE | authoritative/toolchain cross-check and production-path validation |
| Spectral colorimetry / observer models | **PRACTICE / CRITIQUE** | C004 1931 integration/scaling/metamer + 1931↔1964 proof complete; full smooth/measured spectra, independently hash-verified current files, current CIE 2006 LMS/cone comparison, and physical-device validation pending |
| Chromatic adaptation / white points | PRACTICE | ICC/CMM round-trip and bounded Bradford/CAT02/CAT16 comparison |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | CRITIQUE | browser/device validation and production fallback behavior |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | IN STUDY / TRANSFER VALIDATION | real browser forced-colors/theme/system-color tests; browser/device differences |
| Semantic color/token architecture | IN STUDY / PROJECT-READINESS SYNTHESIS | implement token graph + pair matrix in materially different products; multi-theme/platform/browser transfer; collision critique |
| Data-visualization color systems | IN STUDY / NUMERICAL PRACTICE | rendered categorical/sequential/diverging examples; CVD/human-task evidence; light/dark, browser/device and multi-project validation |

## Latest completed block — C004

`C004-spectral-integration-observer-metamerism.md` converts the largest remaining conceptual colorimetry gap into controlled numerical practice.

### Evidence added

- sampled CIE 1931 2° CMFs from a public mirror whose included CIE metadata matches the current CIE-published 1931 dataset checksum;
- explicit rejection of an older 1964 mirror whose metadata checksum did not match the current CIE-published checksum;
- use of a separate 1964 mirror carrying metadata matching the current CIE-published checksum, with row-level values used for the observer comparison;
- CIE 1931 sparse-spectrum integration;
- `2.5×` spectrum-scaling proof showing XYZ magnitude scaling while `x,y` chromaticity remains unchanged;
- a constructed metamer pair using different wavelength sets that matches CIE 1931 XYZ to machine precision;
- re-evaluation of those same spectra under CIE 1964 10°, where the match separates materially;
- explicit rejection of a current CIE 2006 LMS numerical claim because checksum-verified current LMS data were not established in this environment.

### Controlled metamer result

Spectrum A used 450/530/610 nm unit-weight line bins. Spectrum B used 470/550/650 nm with solved weights.

Under CIE 1931 2°:

`XYZ_A = XYZ_B = [1.504300, 1.403000, 1.814610]`

within machine-precision residual.

Under CIE 1964 10°:

- A: `[1.637673, 1.492627, 2.025251]`
- B: `[1.555476323665, 1.533832735677, 1.851930797816]`
- `xy` separation ≈ `0.0210906`
- B `Y` is ≈ `2.7606%` higher than A.

Professional conclusion: **a colorimetric match is conditional on the observer/system that defines it.** This does not predict two particular individuals and does not authorize replacement of the observer/model embedded in production standards.

Evidence level: **PRACTICE + REPLICATION / controlled standardized-observer numerical evidence**. Not physical-device, individual-observer, or production PASS.

## Previous project-facing blocks

### C003 — data visualization

Established data-type-driven choice among qualitative/categorical, sequential and diverging systems; meaningful diverging midpoint requirements; rainbow failure analysis; numerical monotonicity practice; redundant coding; missing/reference/state separation; and production validation criteria.

### C002 — semantic color/token architecture

Established `primitive → semantic role → optional component role → context resolution`, pair contracts, domain-status vs interaction-state separation, and semantic-collision review.

### C001 — Web override resilience

Established forced-colors/system-color/theme resilience requirements and a Color→Web implementation-validation matrix.

## Peer evidence currently affecting Color

### Typography / Type

Type is now through **T004**. T004 provides a complete research numeral/punctuation system, proportional/tabular metrics, zero alternatives, actual FreeType evidence, and a compact colon failure→redraw cycle.

Color consequences:

- chart labels, numeric readouts and dense status text should not be validated with placeholder typography only;
- T003/T004 alpha/raster evidence is a strong future transfer case for light/dark/reduced-contrast/environmental Color testing;
- compact punctuation and marked-zero cases can expose viewing-condition failures that swatch-level contrast misses.

### Layout / Interaction

I001 now has a running Chromium validation specimen with a documented failure→revision→re-proof cycle and 14/14 controlled assertions. State meaning, route focus, pending/error/success, status and recovery are structurally defined before visual encoding.

Color consequences:

- current location/focus/pending/error/success remain strong C001/C002 forced-color transfer targets;
- do not use color to repair an unclear state model;
- L002 remains a useful controlled test for color-driven perceived density by holding geometry fixed while varying luminance/chroma.

### Web Design

At the latest synchronization, Web remains Stage 1 / not yet baselined and no substantive `W###` study is available. **Do not invent Web evidence.**

C001–C003 and Studies 016/017 already provide concrete Color→Web validation contracts for user overrides, semantic token/theme resolution, chart color, wide-gamut/OkLCh/P3 behavior and device/browser fallback.

C004 adds a boundary condition: Web implementation must follow the observer/color-space definitions of governing CSS/sRGB/P3 standards; research observer comparisons are not substitutes for platform definitions.

## Incoming dependencies

- Type may require measured contrast/luminance/viewing-condition evidence for real text, numerals and chart labels.
- Layout & Interaction may require state/focus color contracts, luminance hierarchy, color-vision independence, chart-density evidence and environmental constraints.
- Web Design may require semantic token, chart palette, forced/system-color, gamut/fallback and device/viewing-condition guidance.

## Cross-domain opportunities

### Type

Composite T003/T004 renderer alpha evidence under Color-defined light/dark/background/environment conditions; test compact numerals/punctuation and chart-label roles rather than abstract text samples.

### Layout / Interaction

Use I001 semantic states and L002 matched geometry to test color without redefining state or layout. Useful cases include current-location/focus/error/pending/success under hue removal/forced colors and density comparisons with geometry fixed.

### Web Design

When W### work exists, transfer-test C001–C003 and Studies 016/017 in real browsers. C004 should inform risk framing for wide-gamut/narrow-primary devices but should not be used to redefine CSS colorimetry.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. Extend C004 from sparse lines to complete smooth/measured spectra with independently hash-verified current CIE datasets; complete a current CIE 2006 LMS/cone-fundamental comparison only after provenance is verified.
2. Convert C002 into practice with semantic token graphs and pair/contrast matrices for at least two materially different products, recording collisions and rejected architectures.
3. Convert C003 into rendered practice: categorical + sequential + diverging visualizations in light/dark conditions with grayscale/CVD/small-mark/state critique and at least one failure→revision cycle.
4. Validate D65↔D50 adaptation through a real ICC CMM/profile round trip and compare managed conversion with hand calculation.
5. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not declare a universal winner.
6. Validate non-text/focus/ramp and T003/T004 transfer evidence on physical displays under controlled bright/low-light conditions.
7. Transfer C001/C002/C003 and Studies 016/017 into real browser validation when substantive Web evidence becomes available.
8. Continue advanced data-visualization work later into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization.
9. Build automated token/palette QA only when it validates real design decisions rather than becoming tooling for its own sake.
10. Open `C005` for the next substantial new Color question when justified.

## Open research-quality gaps

- full checksum-verified spectral integration on complete smooth/measured spectra;
- current CIE 2006 LMS/cone-fundamental numerical comparison and broader observer-diversity evidence;
- ICC/CMM and profile-based production validation;
- real browser implementation evidence for modern CSS color, gamut mapping, forced/system colors and token resolution;
- C002 multi-product semantic-system practice;
- C003 rendered/CVD/human-task evidence;
- physical-display/environmental testing;
- cyclic/uncertainty/bivariate/advanced data visualization;
- automated Color QA tied to product acceptance criteria;
- cultural/localization evidence beyond generic color folklore;
- multi-project transfer evidence at production fidelity.

## Current handoffs to other specialists

### Typography / Type

- C004 adds display/viewing-system dependence to the later transfer of T003/T004 renderer evidence.
- Validate C002 foreground roles and C003 axes/labels/numerals with actual font metrics/rasterization.
- Scope limit: Color does not define font construction, metrics or hinting.

### Layout / Interaction

- C004 does not alter the rule that state semantics must survive without hue alone.
- Use I001 states as controlled semantic targets for C001/C002; use L002 to separate color-driven clutter from geometry-driven density.
- Scope limit: Color does not redefine navigation/state/task semantics.

### Web Design

- Implement and challenge C001/C002/C003 in actual page/component/chart systems when Web research begins.
- Test P3/OkLCh/CSS gamut and fallback behavior from Studies 016/017.
- C004 warning: do not substitute alternate observer research into CSS/sRGB/P3 definitions; use it only to identify device/spectral risk that may need additional validation.
- Return browser/device/framework confirmations, limitations, contradictions or transfer failures explicitly.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim peer ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `C001`: Web color override resilience and validation matrix.
- `C002`: semantic color/token architecture and project-readiness method.
- `C003`: data-type-driven visualization color systems and numerical scale practice.
- `C004`: CIE 1931 spectral integration/scaling/metamer practice, 1931↔1964 observer comparison, and dataset-provenance audit.
- `Spectral colorimetry / observer models` advances to **PRACTICE / CRITIQUE**, not PASS.
- Next Color study ID: `C005`.
- Overall Color state remains **CRITIQUE / Foundation NOT PASSED**.