# Typography & Type Design Research

This directory is the canonical research home for the **Typography / Type Design Specialist**.

## Primary scope
Type owns font/glyph construction, metrics, spacing/kerning, numerals/punctuation, family/variable-font planning, OpenType behavior, multiscript/fallback, typography systems, rendering, packaging/release integrity and font engineering.

## Mandatory cross-domain scan
Before substantial Type work: read studio governance, global and specialist statuses, research indexes, relevant Type studies and materially related peer evidence. Record `RELATED DOMAIN CHECK`, handoffs, evidence boundaries and status updates. The studio now includes Content Design as an active peer domain.

## Curriculum state

### Stage 1 — Foundations: PASS
Authority: `T019-stage1-foundation-closure-audit.md`.

### Stage 2 — Intermediate Professional Practice: PRACTICE / NOT PASSED
Authority for entry: `T020-stage2-entry-audit.md`.

The active live-project priority is LogMate Type identity. T017–T020 remain useful conservative product evidence, but the current T021–T024 chain must test whether a more distinctive system can preserve or improve operational behavior rather than treating generic mono or proportional Roboto as the final identity answer.

## T021 current evidence chain

T021 now includes:
- A/B/C pre-kerning family/spacing hypotheses;
- custom H/O/n/o outline and 14/17/24px raster proof;
- lowercase `n` contour redraw after raster failure;
- A/V/T/L/I family expansion;
- shared-cap metric-model falsification and shape-sensitive spacing revision;
- pair/scanline geometry diagnostics;
- mature-font method validation that withdrew an unsupported absolute AV-gap defect threshold;
- bounded LogMate operational glyph-coverage audit;
- `T021-logmate-operational-family-expansion-contract.md` — one coherent construction/spacing/validation contract for the next product-relevant breadth block.

Latest measured coverage of the built candidate remains only **6/33 = 18.18%** of distinct non-space characters in the bounded LogMate corpus. Therefore the present blocker is operational family breadth, not an arbitrary AV gap target.

## T021 next large block

Build, with kerning OFF, enough coherent repertoire to render the bounded LogMate corpus itself:
- uppercase `A B C D E F G H I J K L N O R S T U V X`;
- lowercase controls `n o l`;
- digits `0–9`;
- punctuation `- : ,`;
- one accented path (`É` recommended for the bounded curriculum proof);
- space/notdef.

Then in the same work block where technically possible:
1. render airports, identifiers, time/totals and ambiguity controls at 14/17/24px;
2. repair drawing/general-spacing defects and rerun;
3. verify no fallback/notdef across the bounded corpus;
4. compare against proportional Roboto and the exact product mono control only when that exact artifact is available;
5. enumerate residual pair-specific candidates;
6. decide whether T021 can close.

T022 remains blocked until this evidence exists.

## Kerning boundary

OpenType GPOS supports individual-pair and class-pair positioning, but T021 deliberately does not use kerning to repair unfinished base drawings or sidebearings. Observed failures are classified as drawing → general spacing → pair-specific residual. Only the last category becomes T022 evidence.

## Later sequence
- **T022:** kerning classes/exceptions + proportional/tabular figure alternatives after T021 closure evidence.
- **T023:** weight/interpolation + diacritic/punctuation coherence.
- **T024:** multi-role typography alternatives / LogMate identity integration if evidence is mature enough.

## Production/transfer constraints retained
T006–T018 remain useful constraints covering source validity, interpolation/build compatibility, binary/spec sanity, distribution transforms, normalization/script closure, shaping, loading/fallback, target rendering/layout and human/product validation. These later mechanisms constrain Stage 2 practice; they do not substitute for the Stage 2 family-system gate.

## Tool / platform OPEN
- broad external font QA;
- direct HarfBuzz tracing;
- exact shipped LogMate Flutter/native renderer transfer for a custom candidate;
- Android/iOS/Firefox/Safari matrix;
- production PWA loading/cache/failure;
- larger Korean/complex-script production transfer;
- human recognition/scan/readability evidence at app-validation stage.

## Status authority
Type progress is tracked in `progress/TYPE_STATUS.md`; the specialist does not edit global `progress/STATUS.md` during ordinary research.

Current operating state: **ACTIVE — STAGE 2 PRACTICE / LOGMATE TYPE IDENTITY PRIORITY / T021 OPERATIONAL EXPANSION CONTRACT READY**.