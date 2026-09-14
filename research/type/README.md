# Typography & Type Design Research

This directory is the canonical research home for the **Typography / Type Design Specialist**.

## Primary scope

Research belongs here when its primary question concerns:

- type anatomy, construction, stroke logic, curves and optical correction;
- metrics, spacing, kerning, rhythm and raster behavior;
- numeral and punctuation systems;
- family planning, variable fonts, OpenType, multiscript/fallback behavior;
- typography as information architecture and semantic text-role systems;
- type production, rendering, licensing and font engineering.

## Boundary with other disciplines

- **Layout, Spatial & Interaction** owns screen-level geometry, grouping, responsive recomposition, navigation, state, feedback and interaction behavior. Type may study how text behaves inside those contexts but does not own them.
- **Color** owns colorimetry, color perception, gamut, contrast/color systems and color-management questions. Type may use measured Color evidence when legibility depends on foreground/background behavior.

When a study crosses boundaries, keep one canonical owner and link to related research rather than duplicating the same knowledge.

## Mandatory cross-domain scan

Before new Type work:

1. read `progress/STATUS.md` and all specialist status files;
2. read this README and relevant Type studies;
3. search Color and Layout/Interaction research for related evidence;
4. identify what can be reused and what dependency remains;
5. verify the question is not already being studied elsewhere;
6. record the result under `RELATED DOMAIN CHECK` in the new study.

After completion, add `HANDOFFS TO OTHER SPECIALISTS` when the Type result can materially help Color or Layout/Interaction.

## Current studies

- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `003-stroke-contrast-bezier-optics.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`

Existing study numbers remain stable. New Type studies use `T###` IDs.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.