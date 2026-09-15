# T021 — Pair-Gap Geometry Diagnostics

Status: **EXECUTED — CONTRADICTION REVIEW + REPLICATION**  
Scope: current simplified T021 A/V/T/L/I constructions; kerning OFF; 1000 UPM.  
Companion result: `T021-pair-gap-geometry-diagnostics.json`.

## QUESTION

After replacing the falsified shared-cap metric model with per-glyph advances/LSBs, do the current A/B/C hypotheses have sufficiently credible base geometry to proceed to kerning?

## RELATED DOMAIN CHECK

### Type
Checked `T021-shape-sensitive-prekerning-spacing-revision.py` and current Type status. The prior run proved only that pathological forced equality of whole-string advances was removed; it explicitly left pair-gap diagnosis next.

### Color
Checked current Color status. Color Stage 2 is PASS; no color variable materially changes this geometry-only test. Color remains fixed.

### Layout / Interaction
Checked current Layout/Interaction status. L003/L009 make width and dense operational geometry relevant downstream, but they do not determine glyph sidebearings or authorize kerning.

### Web Design
Checked current Web status through W016. Browser transfer is important after a stable font binary exists; Chromium control evidence does not resolve primitive glyph geometry.

### Why repeat
This is **CONTRADICTION REVIEW + REPLICATION** of the current T021 working assumption. The preceding whole-string advance test could falsely suggest that per-glyph metrics solved the spacing problem. This test asks a narrower question at pair/scanline level before kerning is allowed.

## METHOD

For the exact simplified construction equations used by the current T021 harness, compute left/right ink-boundary intersections at y = 0, 85, 350, 615 and 700 font units. For a pair XY with kerning OFF:

`gap(X,Y,y) = advance(X) + leftBoundary(Y,y) - rightBoundary(X,y)`.

Pairs: `AV`, `VA`, `TA`, `AT`, `LI`, `IL`. This is deterministic analytic geometry on the research outlines, not a perceptual score.

## RESULTS

At the central B hypothesis:

| Pair | y=0 | y=85 | y=350 | y=615 | y=700 |
|---|---:|---:|---:|---:|---:|
| AV | 300.0 | 296.4 | 285.0 | 273.6 | 270.0 |
| VA | 300.0 | 296.4 | 285.0 | 273.6 | 270.0 |
| TA | 300.0 | 320.6 | 385.0 | 239.4 | 260.0 |
| AT | 300.0 | 320.6 | 385.0 | 239.4 | 260.0 |
| LI | 114.0 | 114.0 | 543.0 | 455.0 | 455.0 |
| IL | 114.0 | 114.0 | 202.0 | 114.0 | 114.0 |

A→B→C generally increases the measured whitespace, but that ordering is not a quality ranking. Full values are in the JSON companion.

## CRITIQUE

### CONTRADICTION
The previous correction removed forced equal whole-string advances, but it did **not** establish credible base spacing. The current primitive A/V constructions leave 270–300u of whitespace in B across the sampled scanlines. That magnitude is large enough that opening kerning now would risk using pair adjustments to conceal a primitive construction/base-spacing problem.

`LI` versus `IL` also exposes strong directional geometry asymmetry away from the baseline. The simplified L keeps only its stem at middle/high scanlines while I remains centered, so the pair gap changes dramatically by order and height. This is useful diagnostic evidence that whole-string advance alone was too coarse.

### KEEP
- per-glyph metrics rather than the falsified shared-cap metric;
- kerning OFF while primitive geometry is being diagnosed;
- A/B/C alternatives as controlled research hypotheses;
- explicit separation of deterministic geometry from human optical judgment.

### REWORK
- A/V primitive width/diagonal construction and their sidebearing relationship;
- T interaction with diagonal forms before pair-specific correction;
- L/I construction/sidebearing logic so directional whitespace can be classified cleanly.

### REJECT
- treating A<B<C advance ordering as evidence that B is optically balanced;
- opening T022 kerning on the current primitive A/V/T/L/I drawings;
- deriving kerning values directly from these scanline numbers;
- claiming human readability or production-font quality.

## STUDIO JUDGMENT

T021 remains pre-kerning. The next Type step should revise primitive A/V/T/L/I geometry/sidebearing hypotheses, then rerun both whole-string and pair-gap controls. Kerning becomes eligible only after residual pair problems can be distinguished from glyph-construction/base-spacing defects.

This is a useful failure: the diagnostic prevents a common type-design error—using kerning as a repair layer for unresolved spacing or drawing structure.

## EVIDENCE BOUNDARY

This study is deterministic analytic geometry on simplified research glyphs. It is not raster evidence, browser evidence, production-outline QA, or human optical evaluation. Human/app-stage validation remains deferred and is not simulated.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Do not freeze exact text-column geometry from the current T021 B metrics. Pair-level analysis has reopened primitive capital geometry even though whole-string advances were differentiated successfully.

### Web Design
Delay exact selected-font browser width/fallback transfer until T021 primitive capital geometry stabilizes. W016 remains independently valid; this finding only limits Type geometry readiness.

### Color
No contradiction. Keep color fixed during the next geometry revision so salience changes do not confound Type comparison.

## NEXT

1. revise A/V/T/L/I primitive geometry and sidebearing hypotheses with kerning still OFF;
2. rerun `HAVAL/AVAVA/TAVAT/LITIL` plus pair scanline diagnostics;
3. add numerals, core punctuation and one accented construction path;
4. open T022 kerning only after residual pair-specific problems are separable from base construction.