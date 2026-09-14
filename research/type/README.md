# Typography & Type Design Research

This directory is the canonical research home for the **Typography / Type Design Specialist**.

## Primary scope

Research belongs here when its primary question concerns type anatomy/construction, curves and optical correction; metrics/spacing/kerning/rhythm/raster behavior; numerals/punctuation; family planning, variable fonts, OpenType and multiscript/fallback behavior; typography as information architecture; and type production, rendering, packaging, licensing and font engineering.

## Relationship with other disciplines

- **Layout, Spatial & Interaction** owns screen geometry, grouping, responsive recomposition, navigation, state, feedback and interaction behavior.
- **Color** owns colorimetry, color perception, gamut, contrast/color systems and color management.
- **Web Design** owns real website/web-app page systems, responsive composition, web-specific interaction, frontend-aware application and browser/device validation.

Canonical ownership is not a learning restriction. Type may reproduce, challenge or transfer-test adjacent-domain findings when that improves typography judgment. For web typography, Type owns font/type intent, metrics, OpenType behavior, fallback criteria, rendering questions, packaged-font semantics and typographic failure conditions; Web Design applies and stress-tests those findings in actual browsers/pages/devices.

## Mandatory cross-domain scan

Before substantial Type work: read `AGENTS.md`, `progress/STATUS.md`, all four specialist statuses, this README and related Type work; inspect materially related peer research; choose reuse/replication/challenge/transfer/extension deliberately; record `RELATED DOMAIN CHECK`; add handoffs when useful; and update `progress/TYPE_STATUS.md` before moving to materially different work.

## Current studies

Legacy: `001-type-as-system.md`, `002-metrics-spacing-optical-rhythm.md`, `003-stroke-contrast-bezier-optics.md`, `005-numerals-punctuation-systems.md`, `009-typography-as-information-architecture.md`.

T-series:

- `T001-web-typography-fallback-metrics-reflow-transfer.md` — web loading/failure/script fallback and metrics/reflow transfer baseline.
- `T002-raster-proof-redraw-cycle.md` — controlled failure→redraw→re-proof.
- `T003-minimal-font-renderer-matrix.md` — compiled TrueType / FreeType renderer dependence.
- `T004-native-numeral-punctuation-renderer-proof.md` — original numeral/punctuation system and `tnum`/raster practice.
- `T005-latin-korean-mixed-script-fallback.md` — Latin/Korean fallback metrics, apparent size and reflow.
- `T006-production-outline-audit.md` — production-style source topology, CFF/TTF conversion and raster transfer.
- `T007-variable-interpolation-source-compatibility.md` — two-master compatibility and adversarial correspondence proof.
- `T008-production-build-release-qa.md` — generated-VF binary/reproducible-build release QA.
- `T009-webfont-subset-feature-contract.md` — WOFF2/subset `tnum` semantic contract and feature-drop failure.
- `T010-variable-webfont-axis-contract.md` — WOFF2/subset variable-axis semantic contract; deliberate `avar` loss changes the same `wght=500` meaning.
- `T011-layout-multiscript-release-contract.md` — static WOFF2/subset contract for GPOS `kern`, language-bound GSUB `locl`, Latin+Hangul cmap closure and exact `hhea`/`OS/2` metrics; proves cmap can survive while layout semantics fail, and metrics can drift while layout features survive.

T-series reproducibility scripts and measured JSON live beside the studies. Generated experimental font binaries remain local outputs and are not product assets or canonical source authority.

## Current research direction

T006–T011 establish a progressively stricter production chain:

1. **source/design validity** — contours, correspondence, spacing/metric intent;
2. **build/interpolation compatibility** — topology, variation coverage, intermediate behavior;
3. **binary/spec sanity** — required tables, axis/name/STAT/head/metric integrity;
4. **distribution transformation contract** — exact packaged/subset artifact preserves required Unicode/script coverage, GSUB/GPOS behavior, language-system binding, non-cmap glyph closure, line metrics and variable-axis semantics;
5. **target shaping/rendering/layout integration** — exact shipped artifact in browser/OS/app, including language selection, fallback, CSS/app axis application, line boxes, zoom/DPR and layout regression;
6. **human/product validation**.

T011 materially sharpens layer 4: `character closure ≠ layout-feature closure ≠ language binding ≠ metric identity`. A parseable font containing every requested character can still be wrong for the product.

Highest-value next directions:

1. **T012 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; classify universal/spec/vendor-policy checks separately from product-semantic assertions.
2. Expand layout-feature release QA into `mark`/`mkmk`, anchors/combining marks, `locl`/script closure, vertical-writing metrics/features and real shaping.
3. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, overlap strategy and CFF2.
4. Browser/platform transfer of T001–T011 when substantive Web or a live target stack exists.
5. Type→Layout regression using exact shipped artifacts near known wrap/column/density thresholds.
6. Type→Color transfer with exact packaged artifact/axis/render condition pinned.
7. Broader family/design proof and target-platform Korean/Latin work for Flutter/CoreText/Skia/DirectWrite when project value justifies it.

External FontBakery/Fontspector/OTS and HarfBuzz execution remain **OPEN** in the current environment; no simulated PASS is claimed.

Foundation remains **NOT PASSED**.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.
