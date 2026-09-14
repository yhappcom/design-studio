# Color Research

This directory is the canonical research home for the **Color Specialist**.

## Primary scope

Research belongs here when its primary question concerns:

- color perception, luminance, contrast, adaptation and viewing conditions;
- CIE colorimetry, observer models, illuminants, XYZ, Lab/LCh, Oklab/OkLCh;
- color difference, gamut, gamut mapping, wide-gamut and HDR-related color questions;
- ICC/color management, white points, chromatic adaptation and device reproduction;
- semantic color systems, brand-color behavior, environmental validation and color accessibility evidence.

## Boundary with other disciplines

- **Layout, Spatial & Interaction** owns spatial grouping, grid, responsive geometry, navigation, state semantics, feedback and interaction behavior. Color may encode a defined state but does not invent the state model.
- **Typography / Type Design** owns glyph/font systems, text metrics and typographic structure. Color may affect legibility and hierarchy but does not define the type system.

When a study crosses boundaries, keep one canonical owner and link to related research rather than duplicating conclusions.

## Mandatory cross-domain scan

Before new Color work:

1. read `progress/STATUS.md` and all specialist status files;
2. read this README and relevant Color studies;
3. search Type and Layout/Interaction research for related evidence;
4. identify what can be reused and what dependency remains;
5. verify the question is not already being studied elsewhere;
6. record the result under `RELATED DOMAIN CHECK` in the new study.

After completion, add `HANDOFFS TO OTHER SPECIALISTS` when the Color result can materially help Type or Layout/Interaction.

## Current studies

- `008-color-luminance-contrast-hierarchy.md`
- `010-color-science-colorimetry-foundations.md`
- `011-lms-cone-fundamentals-observer-models.md`
- `012-chromatic-adaptation-white-points.md`
- `013-perceptual-color-spaces-difference.md`
- `016-color-gamut-wide-gamut-mapping.md`
- `017-perceptual-ramp-authoring.md`

Existing study numbers remain stable. New Color studies use `C###` IDs.

## Status authority

Color progress is tracked in `progress/COLOR_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.