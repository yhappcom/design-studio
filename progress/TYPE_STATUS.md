# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 SHAPE-SENSITIVE BASE SPACING EXECUTED, PAIR-GAP + FAMILY BREADTH NEXT**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/spacing evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## T021 current state
Canonical evidence now includes the original mini-family comparison, real outline/raster proof, lowercase `n` redraw, broader A/V/T/L/I transfer, and the latest shape-sensitive pre-kerning spacing revision with executable harness/results.

Three pre-kerning hypotheses remain A Compact, B Balanced, C Open. B remains the working direction, not a final selection.

### Executed evidence chain
The first custom-outline run exposed and corrected a cubic→TrueType build defect, then target-size rendering exposed B's lowercase `n` drawing defect. A contour-only redraw changed raster output while preserving advances, correctly classifying that defect as drawing rather than kerning.

The broader A/V/T/L/I transfer then exposed a second model-level defect: all new capitals shared one `cap_aw/cap_lsb`, forcing shape-different `HAVAL/AVAVA/TAVAT/LITIL` to identical advances.

The latest **CONTRADICTION REVIEW + REPLICATION + TRANSFER VALIDATION** replaces that shared-cap control with per-glyph A/V/T/L/I advance/LSB hypotheses while keeping kerning OFF. All A/B/C research fonts built and all controls executed at 14/17/24px. At 17px B now measures `HAVAL` 51.0156, `AVAVA` 51.8750, `TAVAT` 51.0000, `LITIL` 41.0312 px: the pathological forced equality is removed. A<B<C remains true for every tested control.

This does **not** prove optical spacing quality. `nono/noon/onno` remain equal in total advance as expected for equal glyph counts with kerning OFF, demonstrating why pair-gap/raster diagnostics are the next evidence layer.

Current chain:
`metric alternatives → actual outlines → build correction → raster proof → drawing defect → contour redraw → broader transfer → shared-cap model failure → shape-sensitive base metrics → pair-gap diagnostics + family breadth → kerning eligibility`.

## Stage 2 matrix
| Requirement | Current state |
|---|---|
| coherent glyph family | **PRACTICE — H/O/n/o + A/V/T/L/I executed; shape-sensitive base metrics now present** |
| spacing/control strings | **PRACTICE — 14/17/24px replication executed; forced-equality defect removed; pair-gap diagnostics next** |
| kerning classes/exceptions | **OPEN; deliberately deferred** |
| figure styles | **PARTIAL / STRONG BRIDGE** |
| diacritics/punctuation coherence | **PARTIAL** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — intended-size raster/redraw/broader transfer executed** |
| typography across product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PRACTICE — B survives as working direction; final selection OPEN** |

## Four-specialist balance
- **Type:** Stage 1 PASS; Stage 2 PRACTICE; active family/drawing/spacing chain.
- **Color:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Web:** Stage 1 PASS; Stage 2 PRACTICE through W015; integrated state-model execution exists, browser-runtime breadth remains incomplete.

Type and Web remain the two Stage 2 incomplete specialists. This cycle selected Type because Web had just received W015 while Type had a falsified base-spacing model with a directly executable correction. Future cycles must re-evaluate all four again.

## Active next queue
1. Add objective raster/outline gap diagnostics for `AV/VA`, `TA/AT`, `LI/IL` with kerning OFF; distinguish base-spacing defects from pair-specific residuals.
2. Add numerals, core punctuation and one accented construction path to T021.
3. Only after that evidence is stable, open T022: kerning classes/exceptions + proportional/tabular figures.
4. T023 weight/interpolation + diacritic/punctuation coherence; T024 multi-role typography alternatives.
5. Exact LogMate Flutter need pre-empts nonessential curriculum expansion.

## OPEN / dependencies
Stage 2: pair-gap validation of shape-specific spacing, integrated numerals/punctuation/accent breadth, kerning model, integrated figures, design-level weight proof, final defended family selection.

Later: FontBakery/Fontspector/OTS, direct HarfBuzz, naming/style linking, hinting, multi-axis/CFF2/components, native/browser matrix, production PWA, larger complex scripts.

Human/app-stage validation remains deferred; no simulated human PASS.

## RELATED DOMAIN / HANDOFF state
Color remains fixed during geometry comparison. Layout L003 remains a width/reflow constraint. Web later validates exact selected binaries under loading/fallback/zoom/localization; FreeType evidence is not browser proof. Latest handoff warns Layout/Web that exact widths changed after shape-sensitive spacing correction and should not yet be frozen as product geometry.

## Latest checkpoint
- Stage 1: **PASS**.
- T020: **COMPLETE**.
- T021 actual outline/raster: **EXECUTED**.
- T021 lowercase `n` contour redraw: **EXECUTED**.
- T021 broader A/V/T/L/I transfer: **EXECUTED**.
- Shared-cap spacing parameterization: **FALSIFIED / REPLACED IN CURRENT HARNESS**.
- Shape-sensitive A/V/T/L/I base metrics: **EXECUTED**.
- Pair-gap diagnostics + numerals/punctuation/accent: **NEXT**.
- B direction: **WORKING, NOT FINAL**.
- T022: **NOT OPEN**.
- Stage 2: **NOT PASSED**.