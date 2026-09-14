# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/color/`
Next new-study ID: `C002`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist is not studying color for academic self-satisfaction or file accumulation. The purpose of the Color program is to improve real app, web, and product decisions.

When a project arrives, the specialist must be able to convert accumulated knowledge into project-specific guidance on palette systems, semantic color, luminance/contrast, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, and implementation trade-offs.

Self-directed research may resume immediately. Research breadth is not artificially limited to Color-only material: adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, or implementation knowledge may be studied directly when it improves understanding, independent verification, transfer testing, or project quality.

## Current specialist-team awareness

Design Studio currently has four official specialist roles:

1. Typography / Type Design Specialist;
2. Color Specialist;
3. Layout, Spatial & Interaction Specialist;
4. Web Design Specialist.

Web Design is a peer design discipline and an important implementation/transfer-validation partner for Color. It owns real web page/system/browser application; Color retains canonical ownership of color science, color systems, color accessibility, gamut/color management, and device/viewing-condition questions.

Before substantial work, Color must read all four specialist status files and inspect materially related peer evidence. New research uses `RELATED DOMAIN CHECK`; completed work adds `HANDOFFS TO OTHER SPECIALISTS` when useful.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate**
Overall state: **CRITIQUE**

The Color program has progressed beyond basic UI palette work into color science and color-management foundations. It has not passed Foundation because key spectral, rendered, browser, ICC/CMM, physical-display, and environmental validations remain incomplete.

## Canonical evidence already established

- `research/color/008-color-luminance-contrast-hierarchy.md`
- `research/color/010-color-science-colorimetry-foundations.md`
- `research/color/011-lms-cone-fundamentals-observer-models.md`
- `research/color/012-chromatic-adaptation-white-points.md`
- `research/color/013-perceptual-color-spaces-difference.md`
- `research/color/016-color-gamut-wide-gamut-mapping.md`
- `research/color/017-perceptual-ramp-authoring.md`
- `research/color/C001-web-color-user-override-resilience.md`
- `product-design/exercises/005-color-luminance-cross-context-practice.md`
- `product-design/exercises/009-color-nontext-focus-proof.svg`
- `product-design/exercises/009-color-nontext-focus-proof-critique.md`
- `product-design/exercises/010-srgb-linear-xyz-practice.md`
- `product-design/exercises/012-d65-d50-bradford-practice.md`
- `product-design/exercises/013-perceptual-difference-comparison.md`
- `product-design/exercises/016-oklch-gamut-mapping-practice.md`

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display and environmental validation; representative production contexts |
| Encoded RGB → linear-light → XYZ | PRACTICE | verify against authoritative datasets/tooling |
| LMS / observer models | IN STUDY / PRACTICE | spectral integration and observer comparison with official data |
| Chromatic adaptation / white points | PRACTICE | ICC/CMM round-trip and bounded CAT comparison dataset |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope limits |
| Gamut / wide-gamut mapping | CRITIQUE | browser/device validation and production fallback behavior |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | IN STUDY / TRANSFER VALIDATION | real browser forced-colors/theme/system-color tests; browser/device differences; complete page/component validation with Web Design |

## Primary ownership

This specialist is the canonical owner for color perception, colorimetry, luminance/contrast, adaptation, gamut, color management, palette/ramp construction, semantic color systems, brand-color behavior, color-specific accessibility, environmental viewing conditions, and display/device color validation.

This is **primary ownership, not a research prohibition**.

The Color specialist may study Type, Layout, Interaction, Web Design, Accessibility, Human Factors or other adjacent subjects when needed to:

- validate color in realistic UI and interaction conditions;
- reproduce or challenge an important peer-domain result;
- understand a prerequisite deeply enough to apply it correctly;
- compare methods or standards;
- test transfer into color systems or a live project;
- answer a cross-domain research question.

When doing so, link to peer canonical evidence and state whether the work is reuse, replication, independent validation, contradiction review, transfer validation, or project-specific research.

Color may visually encode a state while also studying the surrounding interaction model deeply enough to validate that encoding. Layout/Interaction remains the canonical owner of the state semantics unless governance changes. Web Design remains the canonical owner of complete web page/system application and actual browser-context integration.

## Incoming dependencies

Current recurring collaboration needs:

- Type may require Color's measured contrast/luminance evidence for specific text roles and viewing contexts.
- Layout & Interaction may require Color's state/focus contrast, luminance hierarchy, color-vision independence, gamut and environmental evidence.
- Web Design may require Color's palette/ramp logic, semantic-color constraints, contrast, system-color/forced-colors guidance, gamut/fallback expectations, and device/viewing-condition evidence.

Respond with canonical Color evidence, a Color-owned study, or an explicitly labeled cross-domain validation when useful. Do not edit the requesting specialist's files during ordinary work.

## Useful external findings

### From Type

Use Type's canonical text-role, font-size/weight, numeral and scaling evidence when constructing realistic text/background contrast tests. Independently reproduce typographic conditions when necessary to validate the color result.

### From Layout & Interaction

Use Layout/Interaction's canonical surface hierarchy, grouping, control/state semantics, focus contexts and real interaction flows when validating semantic color. Color may independently reproduce or stress-test these contexts when the purpose is to validate the color system, but canonical ownership remains explicit.

### From Web Design

The Web Design role is now formally responsible for real website/web-app structure, component/state application, browser/device validation, native control behavior, responsive page systems, and design-to-code fidelity. No `W###` study existed at the time C001 was opened, so there is not yet a Web research conclusion to inherit. However, Web is now the primary implementation-validation partner for Color findings that depend on CSS/browser/device behavior.

Color should actively consume future Web findings on:

- actual CSS wide-gamut/OkLCh rendering and fallback;
- forced-colors and system-color behavior;
- light/dark theme integration with native controls;
- browser differences in focus/state rendering;
- content/page conditions that expose semantic-color collapse;
- implementation details that change a Color recommendation.

This section must be revisited at the start of each work block after reading the other specialist status files.

## Dependencies and cross-domain opportunities

### Type

Text-contrast and legibility tests require realistic font size, weight, glyph density, numeral use and text-role contexts. Reuse Type evidence where sufficient; independently validate when a second check materially improves confidence.

### Layout & Interaction

Color hierarchy must be validated on real surfaces, spatial structures and real state models. A luminance hierarchy should not compensate for weak grouping, and semantic color should be tested against actual behavior and feedback contexts.

### Web Design

Web is the strongest current partner for Color transfer validation. Prior Color studies that should be tested in real browser contexts include:

- Study 008: text/non-text contrast, focus, luminance hierarchy, color-only meaning;
- Study 016: Display P3 / OkLCh out-of-gamut handling and fallback;
- Study 017: ramp behavior after CSS mapping and real rendering;
- C001: `color-scheme`, forced colors, system colors, semantic-state resilience, native-control integration.

Color should not infer browser parity from specifications alone. Web should return implementation confirmations, limitations, contradictions, and page-context failures.

### Shared Accessibility / Human Factors

Color-vision independence, environmental conditions, visual salience, glare and non-color redundancy are legitimate Color research inputs even when they cross specialist boundaries.

## Active next queue

Research may resume now. Priorities are guidance, not hard constraints:

1. Execute spectral colorimetry practice with official CIE data: spectral integration → CIE 1931 XYZ/xy → spectrum scaling → same-spectrum observer comparison → metamerism evidence.
2. Render HSL vs CIELCh vs OkLCh equal-step ramps and test actual browser/device gamut behavior, including P3→sRGB fallback where applicable.
3. Transfer C001 into a real browser validation matrix with Web Design: light/dark, forced colors, system colors, native controls, focus, semantic states, and P3/OkLCh CSS behavior.
4. Validate the D65↔D50 adaptation exercise through an actual ICC CMM/profile round trip and compare managed conversion with hand calculation.
5. Compare Bradford/CAT02/CAT16 on explicitly bounded research datasets and document where the conclusions do and do not transfer.
6. Validate existing non-text/focus and ramp work on physical displays under controlled bright and low-light conditions, using realistic Layout/Interaction contexts and Type roles.
7. Begin a dedicated data-visualization color study when it becomes the highest-value project/readiness gap.
8. Pursue useful cross-domain replication, transfer validation, or adjacent learning when it materially strengthens professional judgment.
9. Open `C002` for the next substantial Color or Color-led cross-domain study when justified.

Do not limit growth merely to avoid overlap. Also do not repeat existing work without a reason that adds analytical value.

## Open research-quality gaps

- official spectral-data integration and observer-model comparison;
- browser implementation details for modern CSS color and gamut mapping;
- real forced-colors/system-color/theme validation on complete web components/pages;
- ICC/CMM and profile-based production validation;
- physical-display/environmental testing with controlled documentation;
- categorical/sequential/diverging data-visualization color systems;
- stronger empirical evidence for visual salience/hierarchy claims where model-space regularity is insufficient;
- stronger integration with Type, Layout/Interaction, and Web Design evidence in realistic project conditions.

## Handoffs to other specialists

### Typography / Type

Current useful Color handoffs:

- role-dependent foreground/background contrast constraints;
- environmental viewing implications for text hierarchy;
- C001 warning that browser/user palette replacement can alter final text/background colors and therefore browser-rendered typography needs transfer validation.

### Layout & Interaction

Current useful Color handoffs:

- luminance hierarchy and state/focus contrast evidence;
- color-independent semantic-state requirements;
- C001 evidence that forced-colors can remove/rewrite fill, shadow, outline, border, and SVG color channels, so state semantics must survive those transformations.

### Web Design

Current useful Color handoffs:

- Study 016 and 017 require real browser/device verification for CSS wide-gamut/gamut mapping and ramp behavior;
- C001 provides a concrete test matrix for `color-scheme`, forced colors, system colors, native controls, focus, semantic states, and P3/OkLCh behavior;
- Web should report browser/device confirmations, limitations, contradictions, and fallback failures back to Color rather than silently adapting the color system.

When repeat research confirms, contradicts, or limits peer work, hand that result back explicitly.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim canonical ownership of the peer domain and do not edit their files without authorization.
