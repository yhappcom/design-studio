# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/color/`
Next new-study ID: `C001`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist is not studying color for academic self-satisfaction or file accumulation. The purpose of the Color program is to improve real app/product decisions.

When a project arrives, the specialist must be able to convert accumulated knowledge into project-specific guidance on palette systems, semantic color, luminance/contrast, viewing conditions, gamut, device behavior, accessibility, brand behavior, and implementation trade-offs.

Self-directed research may resume immediately. Research breadth is not artificially limited to Color-only material: adjacent Type or Layout/Interaction knowledge may be studied directly when it improves understanding, independent verification, transfer testing, or project quality.

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

## Primary ownership

This specialist is the canonical owner for color perception, colorimetry, luminance/contrast, adaptation, gamut, color management, palette/ramp construction, semantic color systems, brand-color behavior, and color-specific accessibility.

This is **primary ownership, not a research prohibition**.

The Color specialist may study Type, Layout, Interaction, Accessibility, Human Factors or other adjacent subjects when needed to:

- validate color in realistic UI and interaction conditions;
- reproduce or challenge an important peer-domain result;
- understand a prerequisite deeply enough to apply it correctly;
- compare methods or standards;
- test transfer into color systems or a live project;
- answer a cross-domain research question.

When doing so, link to peer canonical evidence and state whether the work is reuse, replication, independent validation, contradiction review, transfer validation, or project-specific research.

Color may visually encode a state while also studying the surrounding interaction model deeply enough to validate that encoding. Layout/Interaction remains the canonical owner of the state semantics unless governance changes.

## Incoming dependencies

Current recurring collaboration needs:

- Type may require Color's measured contrast/luminance evidence for specific text roles and viewing contexts.
- Layout & Interaction may require Color's state/focus contrast, luminance hierarchy, color-vision independence, gamut and environmental evidence.

Respond with canonical Color evidence, a Color-owned study, or an explicitly labeled cross-domain validation when useful. Do not edit the requesting specialist's files during ordinary work.

## Useful external findings

### From Type

Use Type's canonical text-role, font-size/weight, numeral and scaling evidence when constructing realistic text/background contrast tests. Independently reproduce typographic conditions when necessary to validate the color result.

### From Layout & Interaction

Use Layout/Interaction's canonical surface hierarchy, grouping, control/state semantics, focus contexts and real interaction flows when validating semantic color. Color may independently reproduce or stress-test these contexts when the purpose is to validate the color system, but canonical ownership remains explicit.

This section must be revisited at the start of each work block after reading the other specialist status files.

## Dependencies and cross-domain opportunities

### Type

Text-contrast and legibility tests require realistic font size, weight, glyph density, numeral use and text-role contexts. Reuse Type evidence where sufficient; independently validate when a second check materially improves confidence.

### Layout & Interaction

Color hierarchy must be validated on real surfaces, spatial structures and real state models. A luminance hierarchy should not compensate for weak grouping, and semantic color should be tested against actual behavior and feedback contexts.

### Shared Accessibility / Human Factors

Color-vision independence, environmental conditions, visual salience, glare and non-color redundancy are legitimate Color research inputs even when they cross specialist boundaries.

## Active next queue

Research may resume now. Priorities are guidance, not hard constraints:

1. Execute spectral colorimetry practice with official CIE data: spectral integration → CIE 1931 XYZ/xy → spectrum scaling → same-spectrum observer comparison → metamerism evidence.
2. Render HSL vs CIELCh vs OkLCh equal-step ramps and test actual browser/device gamut behavior, including P3→sRGB fallback where applicable.
3. Validate the D65↔D50 adaptation exercise through an actual ICC CMM/profile round trip and compare managed conversion with hand calculation.
4. Compare Bradford/CAT02/CAT16 on explicitly bounded research datasets and document where the conclusions do and do not transfer.
5. Validate existing non-text/focus and ramp work on physical displays under controlled bright and low-light conditions, using realistic Layout/Interaction contexts and Type roles.
6. Pursue useful cross-domain replication, transfer validation, or adjacent learning when it materially strengthens professional judgment.
7. Open `C001` for the next substantial Color or Color-led cross-domain study when justified.

Do not limit growth merely to avoid overlap. Also do not repeat existing work without a reason that adds analytical value.

## Open research-quality gaps

- official spectral-data integration and observer-model comparison;
- browser implementation details for modern CSS color and gamut mapping;
- ICC/CMM and profile-based production validation;
- physical-display/environmental testing with controlled documentation;
- categorical/sequential/diverging data-visualization color systems;
- stronger empirical evidence for visual salience/hierarchy claims where model-space regularity is insufficient;
- stronger integration with Type and Layout/Interaction evidence in realistic project conditions.

## Handoffs to other specialists

After substantial Color or Color-led cross-domain work, state explicitly whether the result can help:

- Type: text contrast, role-dependent foreground/background constraints, viewing-condition implications;
- Layout & Interaction: surface hierarchy, state/focus feedback, environment/device constraints, color-independent interaction design.

When repeat research confirms, contradicts, or limits peer work, hand that result back explicitly.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim canonical ownership of the peer domain and do not edit their files without authorization.