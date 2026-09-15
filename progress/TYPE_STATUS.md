# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 PAIR-GAP CONTRADICTION FOUND, PRIMITIVE CAPITAL GEOMETRY REWORK NEXT**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/spacing evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## T021 current state
Canonical evidence includes the original mini-family comparison, actual outline/raster proof, lowercase `n` redraw, broader A/V/T/L/I transfer, shape-sensitive pre-kerning metrics, and now pair/scanline geometry diagnostics.

Three pre-kerning hypotheses remain A Compact, B Balanced, C Open. B remains only a working direction; the latest diagnostic explicitly prevents final selection or kerning.

### Executed evidence chain
The first custom-outline run exposed and corrected a cubic→TrueType build defect, then target-size rendering exposed B's lowercase `n` drawing defect. A contour-only redraw changed raster output while preserving advances, correctly classifying that defect as drawing rather than kerning.

The broader A/V/T/L/I transfer exposed a second model-level defect: all new capitals shared one `cap_aw/cap_lsb`, forcing shape-different strings to identical advances. Per-glyph A/V/T/L/I advance/LSB hypotheses removed that pathological equality while keeping kerning OFF.

The latest **CONTRADICTION REVIEW + REPLICATION** then tested pair-level whitespace analytically on the exact simplified construction geometry at y=0/85/350/615/700. It found that differentiated whole-string advances still did not establish credible primitive spacing. In B, `AV` remains roughly 270–300u across sampled scanlines; `LI` versus `IL` shows strong height/order asymmetry. Therefore kerning is still blocked: current A/V/T/L/I drawing/base-spacing structure must be reworked before pair-specific residuals can be identified.

This is deterministic geometry, not a human optical score and not raster/browser proof.

Current chain:
`metric alternatives → actual outlines → build correction → raster proof → drawing defect → contour redraw → broader transfer → shared-cap model failure → shape-sensitive base metrics → pair-gap contradiction → primitive A/V/T/L/I geometry rework → family breadth → kerning eligibility`.

## Stage 2 matrix
| Requirement | Current state |
|---|---|
| coherent glyph family | **PRACTICE — H/O/n/o + A/V/T/L/I executed; primitive capital geometry reopened by pair-gap diagnostic** |
| spacing/control strings | **PRACTICE — whole-string forced equality removed, but pair/scanline diagnostic found unresolved base-geometry whitespace** |
| kerning classes/exceptions | **OPEN; deliberately blocked until primitive geometry stabilizes** |
| figure styles | **PARTIAL / STRONG BRIDGE** |
| diacritics/punctuation coherence | **PARTIAL** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — intended-size raster/redraw/broader transfer executed; new capital rework will require rerender** |
| typography across product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PRACTICE — B working direction only; pair-gap evidence prevents final selection** |

## Four-specialist balance
- **Type:** Stage 1 PASS; Stage 2 PRACTICE; active family/drawing/spacing chain with a newly isolated primitive-capital contradiction.
- **Color:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Web:** Stage 1 PASS; Stage 2 PRACTICE through W016; actual Chromium native/custom control transfer exists, network/runtime breadth remains incomplete.

Type and Web remain the two Stage 2 incomplete specialists. This cycle selected Type because Web had just received W016 actual Chromium transfer, while Type's next pair-gap diagnostic could directly test whether the recent base-spacing correction was genuinely sufficient. It was not. Future cycles must re-evaluate all four again.

## Active next queue
1. Rework primitive A/V/T/L/I geometry and sidebearing hypotheses with kerning OFF; rerun whole-string and scanline pair-gap controls.
2. Add numerals, core punctuation and one accented construction path to T021 after primitive capitals stabilize.
3. Only after that evidence is stable, open T022: kerning classes/exceptions + proportional/tabular figures.
4. T023 weight/interpolation + diacritic/punctuation coherence; T024 multi-role typography alternatives.
5. Exact LogMate Flutter need pre-empts nonessential curriculum expansion.

## OPEN / dependencies
Stage 2: credible primitive A/V/T/L/I geometry, rerendered pair-gap validation, integrated numerals/punctuation/accent breadth, kerning model, integrated figures, design-level weight proof, final defended family selection.

Later: FontBakery/Fontspector/OTS, direct HarfBuzz, naming/style linking, hinting, multi-axis/CFF2/components, native/browser matrix, production PWA, larger complex scripts.

Human/app-stage validation remains deferred; no simulated human PASS.

## RELATED DOMAIN / HANDOFF state
Color remains fixed during geometry comparison. Layout L003 remains a width/reflow constraint, but exact T021 B widths should not yet be frozen because pair-level evidence reopened capital construction. Web should delay exact selected-font width/fallback transfer until primitive geometry stabilizes; FreeType/analytic evidence is not browser proof.

## Latest checkpoint
- Stage 1: **PASS**.
- T020: **COMPLETE**.
- T021 actual outline/raster: **EXECUTED**.
- T021 lowercase `n` contour redraw: **EXECUTED**.
- T021 broader A/V/T/L/I transfer: **EXECUTED**.
- Shared-cap spacing parameterization: **FALSIFIED / REPLACED**.
- Shape-sensitive A/V/T/L/I base metrics: **EXECUTED, BUT INSUFFICIENT**.
- Pair-gap geometry diagnostic: **EXECUTED — CONTRADICTION FOUND**.
- Primitive A/V/T/L/I geometry/sidebearing rework: **NEXT**.
- Numerals/punctuation/accent breadth: **OPEN**.
- B direction: **WORKING, NOT FINAL**.
- T022: **NOT OPEN**.
- Stage 2: **NOT PASSED**.