# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 LOWERCASE REDRAW EXECUTED, FAMILY EXTENSION NEXT**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/spacing evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## T021 current state
Canonical evidence now includes:
- `T021-coherent-mini-family-spacing-comparison.md`
- `T021-mini-family-comparison-metrics.json`
- `T021-mini-family-comparison-specimen.svg`
- `T021-outline-render-proof.py`
- `T021-outline-render-measured-summary.json`
- `T021-lowercase-n-redraw-validation.md`
- `T021-lowercase-n-redraw-results.json`

Three pre-kerning hypotheses remain A Compact, B Balanced, C Open. B remains the working direction.

### Executed evidence
The first custom-outline run exposed a cubic→TrueType build defect, corrected through `Cu2QuPen`, then rendered A/B/C at 14/17/24px. That proof exposed B's lowercase `n` shoulder as too rectangular/schematic beside `o`.

The follow-up redraw validation has now been executed. Old and curved B `n` controls were rebuilt with the same 1000 UPM, 540u advance, 58u LSB and 85u nominal stem; kerning stayed OFF. `nono/noon/onno` retained identical advances at each tested size while the raster changed materially: 168 changed pixels at 14px, 312 at 17px, and 414 at 24px.

Classification: the original problem was a **DRAWING defect**. The curved shoulder survives as the next working construction. Pixel-difference counts prove contour/rendering change, not human preference or final optical quality.

Current chain:
`metric alternatives → actual outlines → build failure → source correction → raster proof → drawing defect → contour-only redraw with metrics frozen → raster confirmation → broader family/spacing critique → kerning eligibility`.

## Stage 2 matrix
| Requirement | Current state |
|---|---|
| coherent glyph family | **PRACTICE — H/O/n/o executed; n redraw completed; broader family required** |
| spacing/control strings | **PRACTICE — 14/17/24px proof + contour-only control executed; sidebearing reassessment next** |
| kerning classes/exceptions | **OPEN; deliberately deferred** |
| figure styles | **PARTIAL / STRONG BRIDGE** |
| diacritics/punctuation coherence | **PARTIAL** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — intended-size raster and redraw re-proof executed** |
| typography across product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PRACTICE — B survives raster + redraw challenge; final selection OPEN** |

## Four-specialist balance
- **Type:** Stage 1 PASS; Stage 2 PRACTICE; active family/drawing/spacing chain.
- **Color:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Web:** Stage 1 PASS; Stage 2 PRACTICE through W013; browser-runtime breadth remains active.

Type and Web remain the two Stage 2 incomplete specialists. This cycle selected Type because T021 had a concrete diagnosed drawing defect with an executable correction path; the cycle must re-evaluate all four specialists again before continuing Type.

## Active next queue
1. Reassess B `n/o` side space after the curved-shoulder contour change; keep kerning OFF.
2. Extend B/relevant controls to A/V/T/L/I with kerning OFF and render at 14/17/24px.
3. Add numerals, core punctuation and one accented construction path.
4. Only then open T022: kerning classes/exceptions + proportional/tabular figures.
5. T023 weight/interpolation + diacritic/punctuation coherence; T024 multi-role typography alternatives.
6. Exact LogMate Flutter need pre-empts nonessential curriculum expansion.

## OPEN / dependencies
Stage 2: broader mini-family, spacing revision, kerning model, integrated figures, punctuation/diacritics, design-level weight proof, final defended family selection.

Later: FontBakery/Fontspector/OTS, direct HarfBuzz, naming/style linking, hinting, multi-axis/CFF2/components, native/browser matrix, production PWA, larger complex scripts.

Human/app-stage validation remains deferred; no simulated human PASS.

## RELATED DOMAIN / HANDOFF state
Color remains fixed during geometry comparison. Layout L003 remains width/reflow constraint. Web later validates exact selected binaries under loading/fallback/zoom/localization; FreeType evidence is not browser proof.

## Latest checkpoint
- Stage 1: **PASS**.
- T020: **COMPLETE**.
- T021 initial custom-outline raster: **EXECUTED**.
- T021 lowercase `n` contour-only redraw/re-proof: **EXECUTED**.
- B curved `n`: **WORKING CONSTRUCTION, NOT FINAL**.
- T022: **NOT OPEN**.
- Stage 2: **NOT PASSED**.
