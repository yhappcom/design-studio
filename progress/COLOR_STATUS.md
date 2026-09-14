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
- screen geometry, grouping, grid, responsive recomposition → Layout;
- action/state/task-flow semantics → Coordinator-managed cross-cutting Interaction/UX.

Color may visually encode a state only after the state semantics are established elsewhere.

## Dependencies to other domains

### DEPENDENCY — Type

Text-contrast and legibility tests require realistic font size, weight, glyph density, numeral use, and text-role contexts. Color may measure color/luminance behavior but must not invent typographic thresholds beyond supported evidence.

### DEPENDENCY — Layout

Color hierarchy must be validated on real surfaces and spatial structures. A luminance hierarchy should not be used to compensate for weak grouping or geometry. Use Layout-owned compositions for cross-context tests.

### DEPENDENCY — Cross-cutting Accessibility / Interaction

State meaning, focus semantics, status communication, and non-color redundancy are shared constraints. Color owns only the visual color channel. Record semantic gaps as dependencies rather than redefining the interaction model.

## Next queue after explicit restart

1. Execute spectral colorimetry practice with official CIE data: spectral integration → CIE 1931 XYZ/xy → spectrum scaling → same-spectrum observer comparison → metamerism evidence.
2. Render HSL vs CIELCh vs OkLCh equal-step ramps and test actual browser/device gamut behavior, including P3→sRGB fallback where applicable.
3. Validate the D65↔D50 adaptation exercise through an actual ICC CMM/profile round trip and compare managed conversion with hand calculation.
4. Compare Bradford/CAT02/CAT16 only on an explicitly bounded research dataset; do not convert that exercise into an unconditional production rule.
5. Validate existing non-text/focus and ramp work on physical displays under controlled bright and low-light conditions.
6. Only after those evidence gaps are addressed, open `C001` for a genuinely new missing topic.

Prefer validation of existing conceptual work over additional breadth until the current Foundation gate becomes defensible.

## Open research-quality gaps

- official spectral-data integration and observer-model comparison;
- browser implementation details for modern CSS color and gamut mapping;
- ICC/CMM and profile-based production validation;
- physical-display/environmental testing with controlled documentation;
- categorical/sequential/diverging data-visualization color systems as a separate later study;
- stronger empirical evidence for visual salience/hierarchy claims where model-space regularity is insufficient.

## Handoff rule

If another specialist requests Color evidence, answer with a canonical Color study or a new Color-only study. Do not edit their files. If the request contains Type, Layout, or interaction-semantic questions, split them and return those portions as dependencies.