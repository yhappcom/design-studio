# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/color/`
Next new-study ID: `C003`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist studies color to improve real app, web, and product decisions. Research volume, token count, or curriculum speed are not success metrics.

When a project arrives, the specialist must convert accumulated knowledge into project-specific guidance on palette systems, semantic color, luminance/contrast, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research may resume immediately. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, data visualization, or implementation knowledge may be studied when it materially improves Color judgment or project usefulness.

## Current specialist-team awareness

Design Studio currently has four official peer roles:

1. Typography / Type Design Specialist;
2. Color Specialist;
3. Layout, Spatial & Interaction Specialist;
4. Web Design Specialist.

Color retains canonical ownership of color science, color systems, color accessibility, gamut/color management, palette/ramp/semantic systems, and device/viewing-condition questions. Web Design is the main real-browser/page integration partner; Layout/Interaction owns state/action semantics; Type owns typography structure and rendering.

Before substantial work, Color reads all four specialist statuses and related peer evidence. New research includes `RELATED DOMAIN CHECK`; useful results are recorded under `HANDOFFS TO OTHER SPECIALISTS`.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**
Overall state: **CRITIQUE**

The Color program now spans basic UI color, color science, color management foundations, perceptual authoring, web override behavior, and semantic color-system architecture. Foundation is not passed because spectral, rendered, browser, ICC/CMM, physical-display, environmental, and multi-project transfer validations remain incomplete.

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

## Latest completed block — C002

`C002-semantic-color-role-token-architecture.md` converts prior Color science and palette work into a product-facing system method.

Key additions:

- distinguishes **base/primitive → semantic/role → optional component → context resolution**;
- treats foreground/background/boundary/focus relationships as explicit **pair contracts**, not isolated accessible swatches;
- separates domain/status semantics from interaction states;
- identifies semantic collisions such as brand = action = selected = success;
- separates stable semantic role from light/dark/high-contrast/forced-color/platform resolution;
- uses DTCG 2025.10 stable Community Group specifications as token-architecture evidence while explicitly noting they are not W3C Standards;
- compares Apple and Material role-oriented systems without adopting either as the universal MintTap vocabulary;
- adds a project-readiness decision framework, alternatives, trade-offs, failure modes, required inputs, and validation plan.

Evidence level: source-grounded study + project-readiness synthesis. No implementation or multi-project PASS is claimed.

## Primary ownership

Color primarily owns:

- color perception, luminance and contrast;
- colorimetry, observer models, illuminants, XYZ, Lab/LCh, Oklab/OkLCh and color difference;
- adaptation, gamut, gamut mapping, wide gamut and color management;
- palette/ramp construction, semantic color systems and brand-color behavior;
- color-specific accessibility, environmental conditions and display/device validation.

This is primary ownership, not a learning restriction.

## Incoming dependencies

- Type may require measured contrast/luminance evidence for realistic text roles and viewing contexts.
- Layout & Interaction may require state/focus contrast, luminance hierarchy, color-vision independence, semantic-color constraints, gamut and environmental evidence.
- Web Design may require palette/ramp logic, token architecture, semantic-color contracts, system/forced-colors guidance, gamut/fallback expectations, and device/viewing-condition evidence.

## Useful external findings

### From Type

`T001` strengthens the requirement to validate nominally unchanged text colors under real fallback, x-height/weight, wrapping, zoom and mixed-script conditions. Color should not treat text contrast as detached from actual typography.

### From Layout & Interaction

`L002` distinguishes information, visual, interaction and navigation/temporal density. This matters to Color because apparent clutter can be driven by contrast/chroma/feature variability rather than element count alone. Interaction Study 015 confirms that state semantics precede Color encoding.

### From Web Design

At the latest synchronization, Web remains Stage 1 / not yet baselined and no substantive `W###` study is available. Do not invent Web evidence. C001 and C002 now provide concrete Color→Web validation contracts for browser/user overrides, semantic tokens, theme resolution, pair contracts and wide-gamut behavior.

## Cross-domain opportunities

### Typography / Type

Use real primary/secondary/numeric/status text roles, fallback states, scaling, and localization to validate foreground semantic roles and pair contracts.

### Layout / Interaction

Use real surface structures and state models to test whether hierarchy and status remain clear when hue/chroma are reduced, substituted, or removed. Hold geometry constant when investigating whether perceived density or visual mass is color-driven.

### Web Design

High-value transfer targets:

- C001: `color-scheme`, forced colors, system colors, focus, native controls, semantic-state resilience;
- C002: primitive→semantic→component token resolution, pair contracts, theme modifiers, semantic collision handling;
- Study 016/017: Display P3/OkLCh CSS behavior, gamut mapping/fallback, ramp rendering.

Web should return confirmation, limitation, contradiction, or transfer failure rather than silently changing the Color model.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. Close the strongest remaining scientific Foundation gap with official CIE spectral integration and observer comparison.
2. Convert C002 into practice by building a semantic token graph and contrast/pair matrix for at least two materially different product contexts; record collisions and rejected architectures.
3. Transfer C001/C002 and Studies 016/017 into real browser validation with Web Design when `W###` work becomes available.
4. Validate D65↔D50 adaptation through an actual ICC CMM/profile round trip and compare managed conversion with hand calculation.
5. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not generalize one winner beyond the studied conditions.
6. Validate non-text/focus/ramp work on physical displays under controlled bright and low-light conditions using realistic Type and Layout/Interaction contexts.
7. Begin dedicated categorical/sequential/diverging data-visualization color research as a major project-readiness gap.
8. Continue cross-domain replication, contradiction review and transfer validation when it materially improves project decisions.
9. Open `C003` for the next substantial new Color question when justified.

## Open research-quality gaps

- official spectral-data integration and observer-model comparison;
- real browser implementation evidence for modern CSS color, gamut mapping, forced/system colors and token resolution;
- C002 multi-project semantic-system practice and token/contrast audit evidence;
- ICC/CMM and profile-based production validation;
- physical-display/environmental testing with controlled documentation;
- categorical/sequential/diverging data-visualization systems;
- stronger empirical evidence for visual salience/hierarchy where model-space regularity is insufficient;
- automated color-token QA and production validation;
- cultural/localization evidence beyond general guidance;
- stronger integration with Type, Layout/Interaction and future Web evidence in realistic projects.

## Current handoffs to other specialists

### Typography / Type

- Validate C002 semantic foreground roles with actual text hierarchy, weight/size, fallback and zoom/localization states.
- C001 remains relevant because user/browser palette replacement changes rendered foreground/background conditions even when Type roles stay constant.

### Layout / Interaction

- Define state semantics before Color assigns visual roles; separate domain status from hover/focus/selected/pending/committed states.
- Use C002 semantic-collision review to detect when one hue is carrying unrelated behavioral meanings.
- L002 provides a useful controlled transfer case: hold geometry constant while varying luminance/chroma to test color-driven perceived density.

### Web Design

- Implement and challenge C001/C002 in actual page/component systems.
- Validate role resolution across light/dark, forced colors, system colors, native/custom controls and focus states.
- Test CSS P3/OkLCh rendering and fallback from Studies 016/017.
- Return browser/device/framework limitations as explicit evidence.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim canonical ownership of peer domains and do not edit their files without authorization.

## Latest checkpoint

- `C001` established Web color override resilience and a Color→Web browser-validation matrix.
- `C002` established a project-facing semantic color/token architecture method and project-readiness test.
- Next Color study ID advanced to `C003`.
- Overall Color state remains **CRITIQUE**, not PASS.