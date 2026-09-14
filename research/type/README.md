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
- `T014-hangul-normalization-subset-contract.md` — Hangul NFC/NFD package transfer; precomposed-only and Jamo-only WOFF2 packages each fail the canonically equivalent opposite form, while a dual package covers both; deterministic rebuild proof included.

T-series reproducibility scripts and measured JSON live beside the studies. Generated experimental font binaries remain local outputs and are not product assets or canonical source authority.

## Current production model

T006–T014 establish a progressively stricter chain:

1. **source/design validity** — contours, correspondence, spacing/metric intent;
2. **build/interpolation compatibility** — topology, variation coverage, intermediate behavior;
3. **binary/spec sanity** — required tables, axis/name/STAT/head/metric integrity;
4. **distribution transformation contract** — exact package/subset preserves required characters, GSUB/GPOS behavior, script/langsys bindings, non-cmap closure, metrics, variable-axis semantics and attachment anchors;
5. **normalization-form closure** — the codepoint representation that can actually reach shaping must be covered; canonical equivalence does not imply identical subset closure;
6. **script-specific normalization transfer** — T014 confirms the normalization problem on Hangul's algorithmic syllable↔conjoining-Jamo decomposition rather than only Latin combining marks;
7. **attachment-chain completeness** — retaining one stage does not certify an entire attachment path;
8. **target shaping/rendering/layout integration** — exact shipped artifact in browser/OS/app;
9. **human/product validation**.

Current synthesis:

`content normalization boundary → required codepoint representation → subset closure → shaping/fallback → layout/rendering → human/product result`.

A parseable package can be correct for one Unicode representation and fail a canonically equivalent representation. The required closure depends on the real product text-normalization contract.

## Highest-value next directions

1. **T015 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables become available; separate universal/spec/vendor-policy checks from studio semantic assertions.
2. HarfBuzz/browser shaping of T011–T014 exact artifacts, especially Hangul NFC/NFD, combining marks and fallback behavior.
3. Production Korean transfer: real conjoining-Jamo coverage/shaping, full Hangul subset strategy, Korean line breaking and mixed-script layout.
4. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and complex scripts.
5. Vertical-writing release semantics: `vhea`, `vmtx`, `vert`, `vrt2` where project relevance justifies it.
6. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, variable anchors, overlap strategy and CFF2.
7. Browser/platform transfer of T001–T014 with substantive Web/live target stack.
8. Type→Layout regression using exact shipped artifacts near known thresholds.
9. Type→Color transfer with exact packaged artifact/axis/render condition pinned.
10. Broader family/design proof and human reading/recognition evidence after target rendering/layout stabilizes.

## Tool availability checkpoint

At T014, `fontbakery`, `fontspector`, `ots-sanitize`, and `hb-shape` were unavailable. No external QA, sanitizer or shaping PASS is claimed. `fontTools 4.63.0` and Python Unicode data `15.1.0` were used for the bounded experiment.

Foundation remains **NOT PASSED**.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.
