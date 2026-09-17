# Typography & Type Design Research

This directory is the canonical research home for the **Typography / Type Design Specialist**.

## Primary scope
Type owns font/glyph construction, metrics, spacing/kerning, numerals/punctuation, family/variable-font planning, OpenType behavior, multiscript/fallback, typography systems, rendering, packaging/release integrity and font engineering.

## Mandatory cross-domain scan
Before substantial Type work: read studio governance, global and specialist statuses, research indexes, relevant Type studies and materially related peer evidence. Record `RELATED DOMAIN CHECK`, handoffs, evidence boundaries and status updates.

## Curriculum state
### Stage 1 — Foundations: PASS
Authority: `T019-stage1-foundation-closure-audit.md`.

### Stage 2 — Intermediate Professional Practice: PRACTICE / NOT PASSED
Authority for entry: `T020-stage2-entry-audit.md`.

## Current T021 gate — bounded R1 drawing repair
Later T021 evidence supersedes the older operational-breadth summary that previously appeared here. The current executable family has already been expanded and directly critiqued. The active blocker is now a bounded drawing repair, not additional repertoire breadth.

Current R1 mutable loci only:
- capital `I`;
- lowercase `l`;
- digit `1`;
- candidate-B `0` slash refinement.

Current invariants:
- kerning OFF;
- widths and sidebearings frozen;
- unrelated glyphs frozen;
- product/system strings remain unchanged;
- new systems terminology uses mature fallback rather than expanding provisional custom-font scope.

Canonical recent evidence includes:
- `T021-normalized-AB-direct-drawing-critique.md`;
- `T021-repair-decision-specification.md`;
- `T021-repair-rerender-regression-matrix.md`;
- `T021-r1-exact-geometry-patch-specification.md`;
- `T021-r1-mutation-blocker-and-ci-execution-plan.md`;
- `T021-r1-no-scope-creep-contradiction-review.md`.

## Next executable block
1. Apply only the bounded R1 geometry patch in a complete-source environment.
2. Run the normalized CI/toolchain with kerning OFF and frozen metrics.
3. Capture source/build/font/raster hashes.
4. Directly critique ambiguity and accepted operational corpora at 14/17/24px.
5. Reject material regressions before opening general spacing.
6. Only after drawing is defensible, perform general-spacing and fallback/notdef recheck.
7. Open kerning only for residual pair-specific defects after general spacing.

## Drawing → spacing → kerning boundary
T021 deliberately does not use kerning to repair unfinished drawings or sidebearings. Failures are classified as drawing → general spacing → pair-specific residual. Only the last category may become kerning evidence.

## Product-transfer boundary
While R1 remains open, peer domains use mature fallback for product evidence and must not freeze layout around provisional custom metrics. Browser/native transfer of the custom candidate occurs only after Type drawing and spacing gates are defensible.

## Tool / platform OPEN
- R1 source mutation + normalized rerender;
- direct repaired-raster critique;
- general-spacing closure;
- kerning entry;
- exact shipped LogMate Flutter/native custom-font transfer;
- Android/iOS/Firefox/Safari matrix;
- production PWA loading/cache/failure;
- larger Korean/complex-script production transfer;
- human recognition/scan/readability evidence at app-validation stage.

## Evidence boundary
No R1 mutation, repaired-raster PASS, T021 closure, kerning entry, custom-font production recommendation, native/browser transfer or human recognition PASS is claimed.

## Status authority
Type progress is tracked in `progress/TYPE_STATUS.md`; the specialist does not edit global `progress/STATUS.md` during ordinary research.

Current operating state: **ACTIVE — STAGE 2 PRACTICE / T021 R1 SCOPE FROZEN — MUTATION + RASTER EXECUTION OPEN**.