# Typography & Type Design Research

This directory is the canonical research home for the **Typography / Type Design Specialist**.

## Primary scope

Research belongs here when its primary question concerns:

- type anatomy, construction, stroke logic, curves and optical correction;
- metrics, spacing, kerning, rhythm and raster behavior;
- numeral and punctuation systems;
- family planning, variable fonts, OpenType, multiscript/fallback behavior;
- typography as information architecture and semantic text-role systems;
- type production, rendering, packaging, licensing and font engineering.

## Relationship with other disciplines

- **Layout, Spatial & Interaction** owns screen geometry, grouping, responsive recomposition, navigation, state, feedback and interaction behavior.
- **Color** owns colorimetry, color perception, gamut, contrast/color systems and color management.
- **Web Design** owns real website/web-app page systems, responsive composition, web-specific interaction, frontend-aware application, and browser/device validation.

These boundaries define canonical ownership, not limits on learning. Type may investigate adjacent domains for realistic typography validation, replication, method comparison, contradiction review, transfer testing, prerequisite learning or project-specific work. Ordinary cross-domain verification remains in the Type writable area and links back to peer canonical evidence.

For web typography, Type owns font/type intent, metrics, numeral/punctuation behavior, fallback criteria, rendering questions, packaged-font behavior and typographic failure conditions. Web Design applies and stress-tests those findings under actual loading, fallback, wrapping, zoom, localization, responsive layout, browser and device conditions.

## Mandatory cross-domain scan

Before substantial Type work:

1. read `AGENTS.md`, `progress/STATUS.md` and all four specialist status files;
2. read this README and relevant Type studies;
3. inspect materially related Color, Layout/Interaction and Web evidence;
4. identify reusable, uncertain, disputed or test-worthy findings;
5. choose reuse, replication, challenge, transfer or extension deliberately;
6. record the result under `RELATED DOMAIN CHECK`;
7. add `HANDOFFS TO OTHER SPECIALISTS` when useful;
8. update `progress/TYPE_STATUS.md` before moving to materially different work.

## Current studies

Legacy studies:

- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `003-stroke-contrast-bezier-optics.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`

New Type studies:

- `T001-web-typography-fallback-metrics-reflow-transfer.md` — loading/failure/script fallback, font metrics, zoom/reflow and data-stability transfer baseline.
- `T002-raster-proof-redraw-cycle.md` + SVG — controlled failure→redraw→re-proof for join darkness and compact survival.
- `T003-minimal-font-renderer-matrix.md` + Python/SVG — compiled TrueType and FreeType no-hint/autohint comparison; renderer/size/positioning dependence.
- `T004-native-numeral-punctuation-renderer-proof.md` + Python/JSON/SVG — original `0–9`/punctuation system, proportional/tabular metrics, ambiguity alternatives, compact colon redraw and renderer-aware tabular proof.
- `T005-latin-korean-mixed-script-fallback.md` + Python/JSON/SVG — Latin/Korean fallback, vertical metrics, apparent size and long-label transfer; rejects blind Latin x-height matching as a generic Hangul normalization method.
- `T006-production-outline-audit.md` + Python/JSON/SVG — production-style `H O n o` source-topology audit, overlap/extrema/winding failure→revision, cubic CFF vs quadratic TrueType export and raster-transfer evidence.
- `T007-variable-interpolation-source-compatibility.md` + Python/JSON/SVG — two-master `wght` interpolation compatibility, independent-conversion failure, shared conversion revision, and adversarial same-point-count/wrong-correspondence failure.
- `T008-production-build-release-qa.md` + Python/JSON/SVG — generated variable-font release QA: real LSB/xMin/head-flags failure→revision, required-table/axis/name/gvar/checksum audit, deliberate `STAT` removal rejection, and bounded reproducible-build proof.
- `T009-webfont-subset-feature-contract.md` + Python/JSON — TTF→WOFF2 and feature-aware subsetting release proof using `tnum`; includes a deliberate feature-dropping artifact that remains parseable but violates the numeric contract, plus a QA-checker failure→revision when subset glyph names change.
- `T010-variable-webfont-axis-contract.md` + Python/JSON — variable TTF→WOFF2/subset axis-semantics proof using `fvar`/`gvar`/`STAT`/`avar`; a deliberate `avar` removal remains parseable and keeps the visible `wght` axis/named instances yet changes the H advance at user-space `wght=500` from `641u` to `650u`.

Generated experimental font binaries remain local outputs; they are not product assets and are not canonical source authority.

## Current research direction

T006 moved the studio from procedural outline geometry into explicit source/build QA. T007 extended that discipline into variable-family correspondence. T008 extended the chain into generated-binary release QA. T009 established a **distribution transformation contract** for required OpenType features/glyph closure/metrics. T010 now extends that contract to **variable-font axis semantics**: preserving `fvar`/`gvar`/`STAT` and parseability does not by itself prove that the same user-space axis coordinate still resolves to the intended intermediate instance when an authored `avar` mapping is lost.

Current production model:

1. **source/design validity** — contours, master correspondence, spacing/metric intent;
2. **build/interpolation compatibility** — generated topology, variation coverage, intermediate behavior, warnings;
3. **binary/spec sanity** — required tables, variable-font metric/head requirements, axis/name/STAT consistency, checksum/integrity;
4. **distribution transformation contract** — WOFF2/app packaging, subsetting, required feature/glyph/metric retention, variation-table retention and authored user-space→variation-space semantics;
5. **target shaping/rendering/layout integration** — exact shipped artifact in browser/OS/app, fallback/script, CSS/app axis application, zoom/DPR and layout regression;
6. **human/product validation**.

No layer substitutes for the next one.

Highest-value next directions are now:

1. **T011 external broad QA + sanitizer integration** — execute FontBakery/Fontspector/OTS or equivalent when tooling is available, classify OpenType/universal/vendor-policy findings, and integrate them with studio-specific semantic assertions rather than treating one profile as universal truth;
2. **broader feature/metric release QA** — GPOS/kerning, marks/anchors, `locl`, vertical metrics and multi-script closure through packaging/subsetting;
3. **broader variable-family compatibility** — three masters, multiple axes, richer `avar`, components/diacritics, overlap strategy and CFF2;
4. browser/platform transfer of T001–T010 when substantive Web or a live target stack exists;
5. Type→Layout regression using exact shipped artifacts and actual axis mappings near known wrap/column/density thresholds;
6. Type→Color transfer with exact packaged artifact/axis/render condition pinned;
7. broader production-outline/family audit of diagonals, `S`, bowl+stem forms, figures, punctuation, components, marks and anchors;
8. target-platform Korean/Latin proof for Flutter/CoreText/Skia/DirectWrite when project value justifies it.

External FontBakery/Fontspector/OTS execution remains **OPEN** because those executables were unavailable in the latest T010 environment and network installation failed. This is not treated as a simulated PASS.

Foundation remains **NOT PASSED**.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.
