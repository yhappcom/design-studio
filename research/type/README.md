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

- **Layout, Spatial & Interaction** is the canonical owner for screen geometry, grouping, responsive recomposition, navigation, state, feedback and interaction behavior.
- **Color** is the canonical owner for colorimetry, color perception, gamut, contrast/color systems and color management.
- **Web Design** is the canonical owner for real website/web-app page systems, browser-responsive composition, web-specific interaction, frontend-aware application, and browser/device validation.

These boundaries define canonical ownership, not limits on what Type may study. Type may directly investigate Color, Layout/Interaction, or Web material for realistic typography validation, replication, method comparison, contradiction review, transfer testing, prerequisite learning or project-specific work.

When doing overlapping research, cite the peer canonical study and state why the overlap is useful. Store ordinary cross-domain verification in the Type specialist's writable area rather than editing peer files.

For web typography specifically, Type owns font/type intent, metrics, numeral/punctuation behavior, fallback criteria, rendering questions, and typographic failure conditions. Web Design applies and stress-tests those findings under actual loading, fallback, wrapping, zoom, localization, responsive layout, browser, and device conditions, then returns confirmations, limitations, or contradictions.

## Mandatory cross-domain scan

Before new Type work:

1. read `progress/STATUS.md` and all four specialist status files;
2. read this README and relevant Type studies;
3. search Color, Layout/Interaction, and Web research for related evidence;
4. identify what can be reused, independently verified, challenged or extended;
5. identify dependencies and collaboration opportunities;
6. record the result under `RELATED DOMAIN CHECK` in the new study.

Existing work elsewhere is not an automatic reason to stop. Decide whether to reuse it or intentionally repeat/extend it, and document why.

After completion, add `HANDOFFS TO OTHER SPECIALISTS` when the Type result can materially help Color, Layout/Interaction, or Web Design.

## Current studies

- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `003-stroke-contrast-bezier-optics.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`
- `T001-web-typography-fallback-metrics-reflow-transfer.md` — Type→Web transfer baseline for font loading, fallback metrics, zoom/reflow, and data stability; real browser proof remains open.
- `T002-raster-proof-redraw-cycle.md` — controlled surrogate-raster failure → redraw → re-proof study for join darkness and compact survival.
- `T002-raster-proof-redraw-cycle.svg` — embedded surrogate-raster evidence for the T002 R0/R1 comparison.
- `T003-minimal-font-renderer-matrix.md` — compiled minimal TrueType + FreeType no-hint/autohint method comparison; demonstrates that compact form and hinted metrics are renderer/size dependent.
- `T003-minimal-research-font-renderer-matrix.py` — reproducible T003 research-font build and renderer-measurement source.
- `T003-minimal-font-renderer-matrix.svg` — embedded FreeType bitmap evidence at 14/16/24/48 ppem.
- `T004-native-numeral-punctuation-renderer-proof.md` — complete original research `0–9`/punctuation system, proportional/tabular metrics, ambiguity alternatives, colon failure→redraw and renderer-aware tabular proof.
- `T004-numeral-punctuation-research-font.py` — reproducible T004 TrueType build and FreeType measurement source.
- `T004-numeral-punctuation-results.json` — measured source metrics, raw hinted advances, colon redraw and zero-mark raster data.
- `T004-numeral-punctuation-evidence.svg` — compact measurement summary for T004.

Existing study numbers remain stable. New Type studies use `T###` IDs. The next available Type study ID is tracked in `progress/TYPE_STATUS.md`.

## Current research direction

T004 closes the largest missing numeral/punctuation **practice** gap, but not the Foundation gate. The highest-value next Type direction is mixed-script/fallback work, especially Latin/Korean apparent-size, vertical metrics, line-box behavior, long localized labels and dense rows, while browser transfer of T001/T003/T004 remains a major dependency once substantive Web evidence is available.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.
