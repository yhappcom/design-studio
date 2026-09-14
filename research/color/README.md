# Color Research

This directory is the canonical research home for the **Color Specialist**.

## Primary scope

Research belongs here when its primary question concerns:

- color perception, luminance, contrast, adaptation and viewing conditions;
- CIE colorimetry, observer models, illuminants, XYZ, Lab/LCh, Oklab/OkLCh;
- color difference, gamut, gamut mapping, wide-gamut and HDR-related color questions;
- ICC/color management, white points, chromatic adaptation and device reproduction;
- palette/ramp systems, semantic color architecture, brand-color behavior, data-visualization color, environmental validation and color accessibility evidence.

## Relationship with other disciplines

- **Layout, Spatial & Interaction** owns spatial grouping, responsive geometry, navigation, state/action semantics, feedback and interaction behavior. Color may encode those states but does not redefine their meaning silently.
- **Typography / Type Design** owns glyph/font systems, text metrics, hierarchy and rendering. Color foreground roles and chart labels must be validated with realistic Type conditions.
- **Web Design** owns complete website/web-app integration and real browser/device validation. Color supplies canonical palette, token, contrast, gamut, data-color and viewing-condition evidence and consumes Web implementation findings that confirm, limit or contradict it.

These boundaries define canonical ownership, not limits on what Color may study. Cross-domain replication, method comparison, contradiction review, transfer testing, prerequisite learning and project-specific research are allowed when analytically useful.

## Mandatory cross-domain scan

Before new Color work:

1. read `AGENTS.md`, `progress/STATUS.md`, and all four specialist status files;
2. read `research/README.md`, this README, and relevant Color studies;
3. inspect related Type, Layout/Interaction and Web evidence;
4. identify reusable, uncertain, disputed or test-worthy findings;
5. decide whether the new work is reuse, extension, replication, contradiction review, transfer validation, implementation validation or project-specific study;
6. record the result under `RELATED DOMAIN CHECK`;
7. after completion, add `HANDOFFS TO OTHER SPECIALISTS` when useful;
8. update `progress/COLOR_STATUS.md` before moving to a materially different block.

## Current canonical studies

Legacy IDs remain stable:

- `008-color-luminance-contrast-hierarchy.md`
- `010-color-science-colorimetry-foundations.md`
- `011-lms-cone-fundamentals-observer-models.md`
- `012-chromatic-adaptation-white-points.md`
- `013-perceptual-color-spaces-difference.md`
- `016-color-gamut-wide-gamut-mapping.md`
- `017-perceptual-ramp-authoring.md`

New Color studies use `C###` IDs:

- `C001-web-color-user-override-resilience.md` — forced/user colors, semantic resilience, browser-transfer contract.
- `C002-semantic-color-role-token-architecture.md` — base/semantic/component/context architecture, pair contracts, state/status separation, project-readiness method.
- `C003-data-visualization-color-systems.md` — categorical/sequential/diverging scale semantics, numerical monotonicity practice, CVD/redundant coding, interaction/theme transfer and chart failure modes.

Next new Color study ID is tracked in `progress/COLOR_STATUS.md`.

## Evidence and project-use rule

Research should distinguish as appropriate:

- `SOURCE`
- `SYNTHESIS`
- `STUDIO JUDGMENT`
- `OPEN`
- `DEPENDENCY`
- `REPLICATION`
- `CONTRADICTION`
- `TRANSFER VALIDATION`

A color topic is not considered project-ready merely because a palette, formula, chart, or token file exists. It must be possible to state when the knowledge applies, what decision it changes, what trade-offs/failure modes exist, which peer evidence is required, and how the result will be validated.

## Status authority

Color progress is tracked in `progress/COLOR_STATUS.md`. The Color Specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.