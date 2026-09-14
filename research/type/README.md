# Typography & Type Design Research

This directory is the canonical research home for the **Typography / Type Design Specialist**.

## Primary scope

Type owns font/glyph construction, metrics, spacing/kerning, numerals/punctuation, family/variable-font planning, OpenType behavior, multiscript/fallback, typography systems, rendering, packaging/release integrity and font engineering. Canonical ownership does not prohibit cross-domain replication or transfer validation.

## Mandatory cross-domain scan

Before substantial Type work: read `AGENTS.md`, `progress/STATUS.md`, all four specialist statuses, this README and relevant Type studies; inspect materially related peer research; choose reuse/replication/challenge/transfer/extension deliberately; record `RELATED DOMAIN CHECK`; add handoffs when useful; update `progress/TYPE_STATUS.md` after substantial work.

## Current studies

Legacy:

- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `003-stroke-contrast-bezier-optics.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`

T-series:

- `T001-web-typography-fallback-metrics-reflow-transfer.md` — web loading/failure/script fallback and metrics/reflow transfer baseline.
- `T002-raster-proof-redraw-cycle.md` — controlled failure→redraw→re-proof.
- `T003-minimal-font-renderer-matrix.md` — compiled TrueType / FreeType renderer dependence.
- `T004-native-numeral-punctuation-renderer-proof.md` — original numeral/punctuation system and `tnum`/raster practice.
- `T005-latin-korean-mixed-script-fallback.md` — Latin/Korean fallback metrics, apparent size and reflow.
- `T006-production-outline-audit.md` — production-style source topology, CFF/TTF conversion and raster transfer.
- `T007-variable-interpolation-source-compatibility.md` — two-master compatibility and adversarial correspondence proof.
- `T008-production-build-release-qa.md` — generated-variable-font binary/reproducible-build release QA.
- `T009-webfont-subset-feature-contract.md` — WOFF2/subset `tnum` semantic contract and feature-drop failure.
- `T010-variable-webfont-axis-contract.md` — WOFF2/subset variable-axis semantic contract; deliberate `avar` loss changes the same user-axis value.
- `T011-layout-multiscript-release-contract.md` — GPOS `kern`, language-bound GSUB `locl`, multi-script cmap and line-metric package contract.
- `T012-mark-mkmk-anchor-release-contract.md` — GPOS `mark`/`mkmk`, combining-mark advances, exact anchor-chain preservation, adversarial partial feature loss, and post-subset glyph-identity checker revision.
- `T013-normalization-sensitive-subset-contract.md` — Unicode NFC/NFD release contract; canonically equivalent strings can require different cmap/subset closure and different valid attachment paths.

T-series reproducibility scripts and measured JSON live beside the studies. Generated experimental font binaries remain local outputs and are not product assets or canonical source authority.

## Current production model

T006–T013 establish a progressively stricter chain:

1. **source/design validity** — contours, correspondence, spacing/metric intent;
2. **build/interpolation compatibility** — topology, variation coverage, intermediate behavior;
3. **binary/spec sanity** — required tables, axis/name/STAT/head/metric integrity;
4. **distribution transformation contract** — exact package/subset preserves required characters, GSUB/GPOS behavior, script/langsys bindings, non-cmap closure, metrics, variable-axis semantics and required attachment anchors;
5. **normalization-form closure** — the codepoint representation that can actually reach shaping must be covered; canonical equivalence does not imply identical subset closure;
6. **attachment-chain completeness** — for combining marks, retaining one stage (`mark` or `mkmk`) does not certify the entire `base → mark → mark` path;
7. **target shaping/rendering/layout integration** — exact shipped artifact in browser/OS/app;
8. **human/product validation**.

T013 extends the release model to:

`character closure ≠ normalization-form closure ≠ metric identity ≠ feature binding ≠ anchor identity ≠ complete attachment chain ≠ shaping/rendering integration`.

A parseable subset can be correct for one Unicode normalization form and fail the canonically equivalent form. The correct release contract therefore depends on the product's explicit text-normalization boundary.

## Highest-value next directions

1. **T014 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables become available; classify universal/spec/vendor-policy checks separately from studio semantic assertions.
2. HarfBuzz/browser shaping of T011–T013 exact artifacts, including normalization-sensitive combining-mark sequences and fallback behavior.
3. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and production complex scripts.
4. Test normalization/subset transfer on production-relevant Hangul and additional scripts rather than assuming the Latin specimen generalizes.
5. Vertical-writing release semantics: `vhea`, `vmtx`, `vert`, `vrt2` where project relevance justifies it.
6. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, variable anchors, overlap strategy and CFF2.
7. Browser/platform transfer of T001–T013 with substantive Web/live target stack.
8. Type→Layout regression using exact shipped artifacts near known thresholds.
9. Type→Color transfer with exact packaged artifact/axis/render condition pinned.
10. Broader family/design proof and human reading/recognition evidence after target rendering/layout stabilizes.

## Tool availability checkpoint

At the T013 checkpoint, `fontbakery`, `fontspector`, `ots-sanitize`, and `hb-shape` were unavailable. No external QA, sanitizer or shaping PASS is claimed.

Foundation remains **NOT PASSED**.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.
