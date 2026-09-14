# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/color/`
Next new-study ID: `C004`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist studies color to improve real app, web, and product decisions. Research volume, token count, palette count, or curriculum speed are not success metrics.

When a project arrives, the specialist must convert accumulated knowledge into project-specific guidance on palette systems, semantic color, data-visualization color, luminance/contrast, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research may resume immediately. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, data visualization, statistics, or implementation knowledge may be studied when it materially improves Color judgment or project usefulness.

## Current specialist-team awareness

Design Studio currently has four official peer roles:

1. Typography / Type Design Specialist;
2. Color Specialist;
3. Layout, Spatial & Interaction Specialist;
4. Web Design Specialist.

Color retains canonical ownership of color science, color systems, color accessibility, gamut/color management, palette/ramp/semantic systems, data-visualization color, and device/viewing-condition questions. Web Design is the main real-browser/page integration partner; Layout/Interaction owns spatial hierarchy and state/action semantics; Type owns typography structure, numerals, labels and rendering.

Before substantial work, Color reads all four specialist statuses and related peer evidence. New research includes `RELATED DOMAIN CHECK`; useful results are recorded under `HANDOFFS TO OTHER SPECIALISTS`.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**
Overall state: **CRITIQUE**

The Color program now spans basic UI color, color science, color-management foundations, perceptual authoring, web override behavior, semantic token architecture, and data-visualization color systems. Foundation is not passed because spectral, rendered, browser, ICC/CMM, physical-display, environmental, CVD/human-task, and multi-project transfer validations remain incomplete.

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
- existing product-design Color exercises 005, 009, 010, 012, 013, and 016.

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts |
| Encoded RGB → linear-light → XYZ | PRACTICE | verify against authoritative datasets/tooling |
| LMS / observer models | IN STUDY / PRACTICE | official spectral integration and same-spectrum observer comparison |
| Chromatic adaptation / white points | PRACTICE | ICC/CMM round-trip and bounded CAT comparison dataset |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | CRITIQUE | browser/device validation and production fallback behavior |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | IN STUDY / TRANSFER VALIDATION | real browser forced-colors/theme/system-color tests; browser/device differences |
| Semantic color/token architecture | IN STUDY / PROJECT-READINESS SYNTHESIS | implement token graph + pair matrix in representative products; multi-theme/platform/browser transfer; semantic-collision critique |
| Data-visualization color systems | IN STUDY / NUMERICAL PRACTICE | rendered categorical/sequential/diverging examples; CVD/human-task evidence; dark/light and browser/device validation; multi-project transfer |

## Latest completed block — C003

`C003-data-visualization-color-systems.md` establishes a project-facing method for choosing and validating chart/data color from the semantics of the data rather than from palette preference.

Key additions:

- separates **qualitative/categorical**, **sequential**, and **diverging** palettes by data meaning;
- makes a diverging midpoint an explicit semantic commitment rather than a decorative center;
- rejects rainbow-like low→high encoding as a default because visual gradients can be nonuniform and misleading;
- adds a numerical practice comparing ColorBrewer YlGnBu's monotonic relative-luminance path with a synthetic equal-hue HSV rainbow whose luminance repeatedly reverses;
- distinguishes zero, midpoint/reference, missing, not-applicable, pending, suppressed, and overflow states;
- treats direct labels, shape, pattern, line style, position, and grouping as redundant channels rather than assuming a “colorblind-safe palette” is sufficient by itself;
- separates data identity/magnitude color from hover/selected/focus/filter interaction states;
- defines finance-specific transfer examples for P&L, yield/recovery, ticker comparison, and target deviation without turning those examples into universal MintTap palettes;
- adds a production validation protocol for CVD, small marks, light/dark, interaction state, gamut, browser/device/export, and real interpretation tasks.

Evidence level: **source study + numerical practice + project-readiness synthesis**. No rendered/CVD/human/browser/device PASS is claimed.

## Previous completed block — C002

`C002-semantic-color-role-token-architecture.md` converts prior Color science and palette work into a product-facing system method.

Key additions:

- distinguishes **base/primitive → semantic/role → optional component → context resolution**;
- treats foreground/background/boundary/focus relationships as explicit **pair contracts**, not isolated accessible swatches;
- separates domain/status semantics from interaction states;
- identifies semantic collisions such as brand = action = selected = success;
- separates stable semantic role from light/dark/high-contrast/forced-color/platform resolution;
- uses DTCG 2025.10 stable Community Group specifications as token-architecture evidence while explicitly noting they are not W3C Standards;
- compares Apple and Material role-oriented systems without adopting either as the universal MintTap vocabulary.

Evidence level: source-grounded study + project-readiness synthesis. No implementation or multi-project PASS is claimed.

## Primary ownership

Color primarily owns:

- color perception, luminance and contrast;
- colorimetry, observer models, illuminants, XYZ, Lab/LCh, Oklab/OkLCh and color difference;
- adaptation, gamut, gamut mapping, wide gamut and color management;
- palette/ramp construction, semantic color systems, brand-color behavior and data-visualization color;
- color-specific accessibility, environmental conditions and display/device validation.

This is primary ownership, not a learning restriction.

## Incoming dependencies

- Type may require measured contrast/luminance evidence for realistic text roles, chart labels, numeric readouts and viewing contexts.
- Layout & Interaction may require state/focus contrast, luminance hierarchy, color-vision independence, semantic-color constraints, chart-density evidence, gamut and environmental evidence.
- Web Design may require palette/ramp logic, token architecture, semantic-color contracts, data-visualization palette semantics, system/forced-colors guidance, gamut/fallback expectations, and device/viewing-condition evidence.

## Useful external findings

### From Type

Type has advanced through `T003`, including a compiled TrueType + FreeType renderer matrix. T003 demonstrates that outline/metric/rendering behavior is context dependent and explicitly hands Color renderer alpha coverage for future foreground/background transfer tests.

Color consequence:

- do not validate text/chart-label color against placeholder typography only;
- small chart labels and thin legends must be tested with actual rasterized typography;
- apparent weight and coverage can alter the practical visual result even when the nominal color value is unchanged.

### From Layout & Interaction

`L002` distinguishes information, visual, interaction and navigation/temporal density. This matters to Color because apparent clutter can be driven by contrast/chroma/feature variability rather than element count alone.

`I001` adds explicit navigation/history/focus-restoration semantics and requires current location, selection and focus to remain distinguishable without color-only encoding. C001/C002/C003 should therefore avoid collisions between data-series color and navigation/selection/focus color.

### From Web Design

At the latest synchronization, Web remains Stage 1 / not yet baselined and no substantive `W###` study is available. Do not invent Web evidence.

C001, C002 and C003 now provide concrete Color→Web validation contracts for:

- browser/user color overrides;
- semantic token/theme resolution;
- wide-gamut/P3/OkLCh behavior;
- SVG/canvas/CSS chart color;
- light/dark chart mappings;
- direct labels/legends;
- interaction-state separation;
- forced-colors and alternate representation.

## Cross-domain opportunities

### Typography / Type

Use real primary/secondary/numeric/status/chart-label roles, fallback states, scaling, and localization to validate foreground semantic roles, pair contracts, legends, axes and direct labels.

A high-value transfer from T003 is to composite real renderer alpha maps under representative Color foreground/background conditions and compare compact-size legibility across light/dark surfaces.

### Layout / Interaction

Use real surface structures, data density and state models to test whether hierarchy and chart interpretation remain clear when hue/chroma are reduced, substituted, or removed.

High-value controlled tests:

- hold chart geometry/data constant while changing chroma/luminance to measure color-driven visual density;
- keep data palette fixed while adding hover/selected/focus states to test semantic collision;
- compare direct labeling, legend use, faceting and filtering when categorical color count grows.

### Web Design

High-value transfer targets:

- C001: `color-scheme`, forced colors, system colors, focus, native controls, semantic-state resilience;
- C002: primitive→semantic→component token resolution, pair contracts, theme modifiers, semantic collision handling;
- C003: SVG/canvas/CSS categorical/sequential/diverging palettes, direct labels, small marks, light/dark transfer, forced colors and alternate representation;
- Studies 016/017: Display P3/OkLCh CSS behavior, gamut mapping/fallback, ramp rendering.

Web should return confirmation, limitation, contradiction, or transfer failure rather than silently changing the Color model.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. Close the strongest remaining scientific Foundation gap with official CIE spectral integration and observer comparison.
2. Convert C002 into practice by building a semantic token graph and contrast/pair matrix for at least two materially different product contexts; record collisions and rejected architectures.
3. Convert C003 into rendered practice: one categorical, one sequential and one diverging visualization in light/dark contexts, with grayscale/CVD/small-mark/interaction-state critique and at least one failure→revision cycle.
4. Transfer C001/C002/C003 and Studies 016/017 into real browser validation with Web Design when `W###` evidence becomes available.
5. Validate D65↔D50 adaptation through an actual ICC CMM/profile round trip and compare managed conversion with hand calculation.
6. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not generalize one winner beyond the studied conditions.
7. Validate non-text/focus/ramp work on physical displays under controlled bright and low-light conditions using realistic Type and Layout/Interaction contexts.
8. Continue data-visualization research later into cyclic scales, uncertainty, bivariate maps, heatmaps and multi-color gamut optimization after Foundation evidence is stronger.
9. Continue cross-domain replication, contradiction review and transfer validation when it materially improves project decisions.
10. Open `C004` for the next substantial new Color question when justified.

## Open research-quality gaps

- official spectral-data integration and observer-model comparison;
- real browser implementation evidence for modern CSS color, gamut mapping, forced/system colors and token resolution;
- C002 multi-project semantic-system practice and token/contrast audit evidence;
- C003 rendered/CVD/human-task/light-dark/browser-device evidence;
- ICC/CMM and profile-based production validation;
- physical-display/environmental testing with controlled documentation;
- cyclic, uncertainty, bivariate and advanced data-visualization systems;
- stronger empirical evidence for visual salience/hierarchy where model-space regularity is insufficient;
- automated color-token and chart-palette QA;
- cultural/localization evidence beyond general guidance;
- stronger integration with Type, Layout/Interaction and future Web evidence in realistic projects.

## Current handoffs to other specialists

### Typography / Type

- Validate C002 semantic foreground roles with actual text hierarchy, weight/size, fallback and zoom/localization states.
- Use T003 renderer evidence to test actual alpha coverage under Color-defined foreground/background conditions.
- C003 adds axes, legends, data labels, direct labels and numeric readouts as realistic Type stress contexts.
- Scope limit: Color does not define type metrics or font selection.

### Layout / Interaction

- Define state semantics before Color assigns visual roles; separate domain status from hover/focus/selected/pending/committed states.
- Use C002 semantic-collision review to detect when one hue carries unrelated behavioral meanings.
- L002 provides a controlled transfer case: hold geometry constant while varying luminance/chroma to test color-driven perceived density.
- C003 adds chart-specific tests: direct label vs legend, categorical-color count, focus/selection overlays, missing/reference states and faceting/filtering alternatives.

### Web Design

- Implement and challenge C001/C002/C003 in actual page/component/chart systems.
- Validate role resolution across light/dark, forced colors, system colors, native/custom controls and focus states.
- Test SVG/canvas/CSS chart palettes and alternate representation under forced colors.
- Test CSS P3/OkLCh rendering and fallback from Studies 016/017.
- Return browser/device/framework limitations as explicit evidence.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim canonical ownership of peer domains and do not edit their files without authorization.

## Latest checkpoint

- `C001` established Web color override resilience and a Color→Web browser-validation matrix.
- `C002` established a project-facing semantic color/token architecture method and project-readiness test.
- `C003` established data-type-driven palette selection, numerical ordered-scale practice, data-color failure modes and a chart validation protocol.
- Next Color study ID advanced to `C004`.
- Overall Color state remains **CRITIQUE**, not PASS.