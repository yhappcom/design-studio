# Color Specialist Status

Operating state: **PAUSED BY OWNER**
Governance sync: 2026-09-14
Primary path: `research/color/`
Next new-study ID: `C001`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

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

## Ownership boundary

This specialist owns color perception, colorimetry, luminance/contrast, adaptation, gamut, color management, palette/ramp construction, semantic color systems, brand-color behavior, and color-specific accessibility.

Do not launch research whose primary question is:

- font/glyph/type metrics or type hierarchy mechanics → Type;
- screen geometry, grouping, grid, responsive recomposition, state semantics or interaction flow → Layout & Interaction.

Color may visually encode a state only after Layout & Interaction has established what the state means and how it behaves.

## Incoming dependencies

Record active requests from other specialists here. Current recurring collaboration needs:

- Type may require Color's measured contrast/luminance evidence for specific text roles and viewing contexts.
- Layout & Interaction may require Color's state/focus contrast, luminance hierarchy, color-vision independence, gamut and environmental evidence.

Respond with canonical Color evidence or a Color-owned study; do not edit the requesting specialist's files.

## Useful external findings

### From Type

Use Type's canonical text-role, font-size/weight, numeral and scaling evidence when constructing realistic text/background contrast tests. Do not treat arbitrary font settings as universal test conditions.

### From Layout & Interaction

Use Layout/Interaction's canonical surface hierarchy, grouping, control/state semantics, focus contexts and real interaction flows when validating semantic color. Do not create state semantics inside Color research.

This section must be revisited at the start of each work block after reading the other specialist status files.

## Dependencies to other domains

### DEPENDENCY — Type

Text-contrast and legibility tests require realistic font size, weight, glyph density, numeral use and text-role contexts. Color owns color/luminance behavior; Type owns the typographic system.

### DEPENDENCY — Layout & Interaction

Color hierarchy must be validated on real surfaces, spatial structures and real state models. A luminance hierarchy must not compensate for weak grouping, and a semantic state color must not invent the state it is encoding.

### DEPENDENCY — Shared Accessibility / Human Factors

Color-vision independence, environmental conditions and non-color redundancy may require shared evidence. Record unowned gaps and request coordinator triage rather than creating a competing specialty.

## Next queue after explicit restart

1. Execute spectral colorimetry practice with official CIE data: spectral integration → CIE 1931 XYZ/xy → spectrum scaling → same-spectrum observer comparison → metamerism evidence.
2. Render HSL vs CIELCh vs OkLCh equal-step ramps and test actual browser/device gamut behavior, including P3→sRGB fallback where applicable.
3. Validate the D65↔D50 adaptation exercise through an actual ICC CMM/profile round trip and compare managed conversion with hand calculation.
4. Compare Bradford/CAT02/CAT16 only on an explicitly bounded research dataset; do not convert that exercise into an unconditional production rule.
5. Validate existing non-text/focus and ramp work on physical displays under controlled bright and low-light conditions, using Layout/Interaction-owned state/focus contexts where relevant.
6. Only after those evidence gaps are addressed, open `C001` for a genuinely new missing topic.

Prefer validation of existing conceptual work over additional breadth until the current Foundation gate becomes defensible.

## Open research-quality gaps

- official spectral-data integration and observer-model comparison;
- browser implementation details for modern CSS color and gamut mapping;
- ICC/CMM and profile-based production validation;
- physical-display/environmental testing with controlled documentation;
- categorical/sequential/diverging data-visualization color systems as a separate later study;
- stronger empirical evidence for visual salience/hierarchy claims where model-space regularity is insufficient.

## Handoffs to other specialists

After substantial Color work, state explicitly whether the result can help:

- Type: text contrast, role-dependent foreground/background constraints, viewing-condition implications;
- Layout & Interaction: surface hierarchy, state/focus feedback, environment/device constraints, color-independent interaction design.

Reference the canonical Color file rather than copying source summaries elsewhere.

## Handoff rule

If another specialist requests Color evidence, answer with a canonical Color study or a new Color-only study. Do not edit their files. Split Type- or Layout/Interaction-owned portions into dependencies.