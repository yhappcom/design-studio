# Typography & Type Design Research

This directory is the canonical research home for the **Typography / Type Design Specialist**.

## Primary scope

Type owns font/glyph construction, metrics, spacing/kerning, numerals/punctuation, family/variable-font planning, OpenType behavior, multiscript/fallback, typography systems, rendering, packaging/release integrity and font engineering. Canonical ownership does not prohibit cross-domain replication or transfer validation.

## Mandatory cross-domain scan

Before substantial Type work: read `AGENTS.md`, `progress/STATUS.md`, all four specialist statuses, `research/README.md`, this README and relevant Type studies; inspect materially related peer research; choose reuse/replication/challenge/transfer/extension deliberately; record `RELATED DOMAIN CHECK`; add handoffs when useful; update `progress/TYPE_STATUS.md` after substantial work.

## Current studies

Legacy:

- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `003-stroke-contrast-bezier-optics.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`

T-series:

- `T001-web-typography-fallback-metrics-reflow-transfer.md`
- `T002-raster-proof-redraw-cycle.md`
- `T003-minimal-font-renderer-matrix.md`
- `T004-native-numeral-punctuation-renderer-proof.md`
- `T005-latin-korean-mixed-script-fallback.md`
- `T006-production-outline-audit.md`
- `T007-variable-interpolation-source-compatibility.md`
- `T008-production-build-release-qa.md`
- `T009-webfont-subset-feature-contract.md`
- `T010-variable-webfont-axis-contract.md`
- `T011-layout-multiscript-release-contract.md`
- `T012-mark-mkmk-anchor-release-contract.md`
- `T013-normalization-sensitive-subset-contract.md`
- `T014-hangul-normalization-subset-contract.md` — Hangul NFC/NFD structural package transfer; precomposed-only and Jamo-only WOFF2 packages have different `cmap` closure; deterministic rebuild proof included.
- `T015-hangul-browser-canonical-cluster-transfer.md` — Chromium transfer of T014: deliberately asymmetric NFC-only/NFD-only/dual WOFF2 fonts render canonically equivalent Hangul identically in the bounded browser matrix, showing structural closure and target rendering are separate gates.

T-series reproducibility scripts and measured JSON live beside the studies. Generated experimental font binaries and screenshots remain runtime outputs and are not product assets or canonical source authority.

## Current production model

T006–T015 establish a progressively stricter chain:

1. **source/design validity** — contours, correspondence, spacing/metric intent;
2. **build/interpolation compatibility** — topology, variation coverage, intermediate behavior;
3. **binary/spec sanity** — required tables, axis/name/STAT/head/metric integrity;
4. **distribution transformation contract** — exact package/subset preserves required characters, GSUB/GPOS behavior, script/langsys bindings, non-cmap closure, metrics, variable-axis semantics and attachment anchors;
5. **normalization-form / script-specific structural closure** — canonically equivalent text can have different codepoint and `cmap` closure;
6. **target cluster matching/shaping** — T015 proves that different structural closure does not automatically produce different browser output: Chromium resolved canonically equivalent Hangul across deliberately asymmetric packages in the bounded test;
7. **fallback/glyph selection and attachment-chain completeness** — retained codepoints/features do not by themselves certify the complete shaping path;
8. **target rendering/layout integration** — exact shipped artifact in browser/OS/app;
9. **human/product validation**.

Current synthesis:

`content representation → binary cmap/feature closure → target cluster matching/shaping → fallback/glyph selection → rendered geometry/raster → layout/color consequence → human/product result`.

T014 remains valid as a structural package audit. T015 limits its runtime interpretation: **different `cmap` closure is not automatically a browser rendering failure** when canonical-equivalent matching/shaping can bridge the representations. Conversely, one Chromium result is not a cross-platform package-minimization PASS.

## Highest-value next directions

1. **T016 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables become available; separate universal/spec/vendor-policy checks from studio semantic assertions.
2. Direct HarfBuzz CLI/`uharfbuzz` glyph/cluster tracing of T011–T015 artifacts when available, then Firefox/Safari/Windows/macOS/Android/Flutter replication of T015.
3. Production Korean transfer: real conjoining-Jamo design/shaping, larger Hangul coverage, Korean line breaking and mixed-script line boxes using an exact production-relevant font.
4. Real `@font-face` network loading/failure/`font-display` and browser zoom transfer, preferably through substantive Web/live-product work.
5. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and production complex scripts.
6. Study vertical-writing release semantics: `vhea`, `vmtx`, `vert`, `vrt2` where project relevance justifies it.
7. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, variable anchors, overlap strategy and CFF2.
8. Type→Layout regression using exact shipped artifacts near known thresholds.
9. Type→Color transfer with exact package/build/axis/render condition pinned.
10. Broader family/design proof and human reading/recognition evidence after target rendering/layout stabilizes.

## Tool availability checkpoint

At T015, `fontbakery`, `fontspector`, `ots-sanitize`, `hb-shape`, and Python `uharfbuzz` were unavailable. Chromium `144.0.7559.96`, Playwright, `fontTools 4.63.0`, Python Unicode data `15.1.0`, and local `NanumGothic` were available. T015 therefore adds bounded Chromium shaping/rendering transfer, **not** external sanitizer or direct HarfBuzz PASS.

Foundation remains **NOT PASSED**.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.