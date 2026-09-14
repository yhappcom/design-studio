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

## Relationship with other disciplines

- **Layout, Spatial & Interaction** owns screen geometry, grouping, responsive recomposition, navigation, state, feedback and interaction behavior.
- **Color** owns colorimetry, color perception, gamut, contrast/color systems and color management.
- **Web Design** owns real website/web-app page systems, responsive composition, web-specific interaction, frontend-aware application, and browser/device validation.

These boundaries define canonical ownership, not limits on what Type may study. Type may investigate adjacent domains for realistic typography validation, replication, method comparison, contradiction review, transfer testing, prerequisite learning or project-specific work. Ordinary cross-domain verification remains in the Type writable area and links back to peer canonical evidence.

For web typography, Type owns font/type intent, metrics, numeral/punctuation behavior, fallback criteria, rendering questions and typographic failure conditions. Web Design applies and stress-tests those findings under actual loading, fallback, wrapping, zoom, localization, responsive layout, browser and device conditions, then returns confirmations, limitations or contradictions.

## Mandatory cross-domain scan

Before substantial Type work:

1. read `AGENTS.md`, `progress/STATUS.md` and all four specialist status files;
2. read this README and relevant Type studies;
3. inspect materially related Color, Layout/Interaction and Web evidence;
4. identify reusable, uncertain, disputed or test-worthy findings;
5. choose reuse, replication, challenge, transfer or extension deliberately;
6. record the result under `RELATED DOMAIN CHECK`;
7. after completion, add `HANDOFFS TO OTHER SPECIALISTS` when useful;
8. update `progress/TYPE_STATUS.md` before moving to materially different work.

## Current studies

Legacy studies:

- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `003-stroke-contrast-bezier-optics.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`

New Type studies:

- `T001-web-typography-fallback-metrics-reflow-transfer.md` — loading/failure/script fallback, font metrics, zoom/reflow and data stability transfer baseline.
- `T002-raster-proof-redraw-cycle.md` + SVG — controlled failure→redraw→re-proof for join darkness and compact survival.
- `T003-minimal-font-renderer-matrix.md` + Python/SVG — compiled TrueType and FreeType no-hint/autohint comparison; renderer/size/positioning dependence.
- `T004-native-numeral-punctuation-renderer-proof.md` + Python/JSON/SVG — original `0–9`/punctuation system, proportional/tabular metrics, ambiguity alternatives, compact colon redraw and renderer-aware tabular proof.
- `T005-latin-korean-mixed-script-fallback.md` + Python/JSON/SVG — Latin/Korean fallback, vertical metrics, apparent size and long-label transfer; rejects blind Latin x-height matching as a generic Hangul normalization method.
- `T006-production-outline-audit.md` + Python/JSON/SVG — production-style `H O n o` source-topology audit, overlap/extrema/winding failure→revision, cubic CFF vs quadratic TrueType export and raster-transfer evidence.
- `T007-variable-interpolation-source-compatibility.md` + Python/JSON/SVG — two-master `wght` interpolation compatibility, independent-conversion failure, shared cu2qu revision, and adversarial same-point-count/wrong-correspondence failure.

Generated experimental font binaries remain local outputs; they are not product assets and are not canonical source authority.

## Current research direction

T006 moved the studio from procedural outline geometry into explicit source/build QA. T007 extends that discipline from one clean master into a variable-family contract.

T007 materially changes the variable-font method:

- a variable font can build while a required glyph is skipped from `gvar` variation in the tested FontTools path;
- independent cubic→quadratic conversion can create incompatible generated topology even when the cubic masters were structurally related;
- joint conversion can restore compatible generated topology;
- **equal contour/point counts are still not sufficient**: corresponding point indices must represent corresponding structural locations;
- endpoint-only inspection is insufficient because malformed correspondence can produce an unacceptable intermediate while both masters look valid.

Highest-value next directions are now:

1. **T008 production build/release QA** — extend T006/T007 into binary sanity checks, expected variation coverage, naming/axis metadata and failure-catching automation without pretending a full release pipeline exists yet;
2. broader multi-master/axis compatibility: three masters, `avar`, multiple axes, components/diacritics and overlap strategy;
3. browser/platform transfer of T001/T003/T004/T005/T006/T007 when substantive Web or target-platform evidence is available;
4. Type→Layout regression transfer using known L003/L004 constraints when source/build/axis changes alter width or compact rendering;
5. Type→Color transfer using actual renderer output under current Color role/background evidence with font instance/build held fixed;
6. broader production-outline audit of diagonals, `S`, bowl+stem forms, figures, punctuation, components and diacritics;
7. target-platform Korean/Latin proof for Flutter/CoreText/Skia/DirectWrite when a live project requires it.

Foundation remains **NOT PASSED**.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.
