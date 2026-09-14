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

These boundaries define canonical ownership, not limits on learning. Type may investigate adjacent domains for realistic typography validation, replication, method comparison, contradiction review, transfer testing, prerequisite learning or project-specific work. Ordinary cross-domain verification remains in the Type writable area and links back to peer canonical evidence.

For web typography, Type owns font/type intent, metrics, numeral/punctuation behavior, fallback criteria, rendering questions and typographic failure conditions. Web Design applies and stress-tests those findings under actual loading, fallback, wrapping, zoom, localization, responsive layout, browser and device conditions.

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
- `T008-production-build-release-qa.md` + `T008-production-build-qa.py` / JSON / SVG — generated variable-font release QA: real LSB/xMin/head-flags failure discovered in the previous research builder, corrected metrics/head state, required-table/axis/name/gvar/checksum audit, deliberate `STAT` removal rejection, and corrected bounded reproducible-build proof.

Generated experimental font binaries remain local outputs; they are not product assets and are not canonical source authority.

## Current research direction

T006 moved the studio from procedural outline geometry into explicit source/build QA. T007 extended that discipline into variable-family correspondence and proved that build success/equal point counts are weak acceptance criteria. T008 now extends the chain into **generated-binary release QA** and provides a concrete example where a valid interpolation experiment still emitted a non-release-compliant TrueType VF metric/head configuration.

Current production model:

1. **source/design validity** — contours, master correspondence, spacing/metric intent;
2. **build/interpolation compatibility** — generated topology, variation coverage, intermediate behavior, warnings;
3. **binary/spec sanity** — required tables, TrueType VF metric/head requirements, axis/name/STAT consistency, checksum/integrity;
4. **design regression** — endpoint/intermediate visual and metric behavior, compact raster, fallback/script transfer;
5. **target integration** — broad QA/sanitizer, WOFF2/app packaging, browser/OS/device, accessibility/localization and human/product evidence.

No layer substitutes for the next one.

Highest-value next directions are now:

1. **T009 external broad QA + sanitizer integration** — execute FontBakery/Fontspector/OTS or equivalent when tooling is available, classify OpenType/universal/vendor-policy findings, and integrate them with studio-specific assertions rather than treating a single profile as universal truth;
2. broader variable-family compatibility: three masters, `avar`, multiple axes, components/diacritics, overlap strategy and CFF2;
3. feature/metric release QA: GSUB/GPOS/kerning, vertical metrics, named instances/STAT AxisValues, numerals, WOFF2 and subsetting;
4. browser/platform transfer of T001–T008 when substantive Web or a live target stack exists;
5. Type→Layout regression using release-identified artifacts near known wrap/column/density thresholds;
6. Type→Color transfer with exact build/axis/render condition pinned;
7. broader production-outline/family audit of diagonals, `S`, bowl+stem forms, figures, punctuation, components, marks and anchors;
8. target-platform Korean/Latin proof for Flutter/CoreText/Skia/DirectWrite when project value justifies it.

Foundation remains **NOT PASSED**.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.
