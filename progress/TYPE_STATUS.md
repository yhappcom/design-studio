# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 BROADER FAMILY EXECUTED, BASE-SPACING MODEL REWORK NEXT**  
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
- `T021-broader-mini-family-prekerning-transfer.py`
- `T021-broader-mini-family-prekerning-results.json`
- `T021-broader-mini-family-prekerning-transfer.md`

Three pre-kerning hypotheses remain A Compact, B Balanced, C Open. B remains the working direction.

### Executed evidence
The first custom-outline run exposed a cubic→TrueType build defect, corrected through `Cu2QuPen`, then rendered A/B/C at 14/17/24px. That proof exposed B's lowercase `n` shoulder as too rectangular/schematic beside `o`.

The contour-only redraw then rebuilt old/curved B `n` controls with metrics frozen. `nono/noon/onno` retained identical advances while raster pixels changed materially, classifying the original problem as a DRAWING defect rather than a kerning problem.

The latest broader-family TRANSFER VALIDATION extends all A/B/C controls to A/V/T/L/I with kerning OFF and executes the same 14/17/24px measurement regime. It succeeds as a build/raster breadth extension but exposes a new model-level failure: A/V/T/L/I currently share one `cap_aw` and one `cap_lsb`, so shape-different control strings such as `HAVAL`, `AVAVA`, `TAVAT`, and `LITIL` receive identical advances inside each hypothesis. That equality is mechanically expected but cannot support an optical-spacing claim.

Current chain:
`metric alternatives → actual outlines → build failure → source correction → raster proof → drawing defect → contour-only redraw → broader family transfer → shared-cap base-spacing model failure → shape-specific spacing revision → kerning eligibility`.

## Stage 2 matrix
| Requirement | Current state |
|---|---|
| coherent glyph family | **PRACTICE — H/O/n/o + A/V/T/L/I executed; broader spacing rework required** |
| spacing/control strings | **PRACTICE — 14/17/24px proof executed; shared cap metric model falsified as sufficient evidence** |
| kerning classes/exceptions | **OPEN; deliberately deferred** |
| figure styles | **PARTIAL / STRONG BRIDGE** |
| diacritics/punctuation coherence | **PARTIAL** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — intended-size raster, redraw and broader-family transfer executed** |
| typography across product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PRACTICE — B survives as working direction; final selection OPEN** |

## Four-specialist balance
- **Type:** Stage 1 PASS; Stage 2 PRACTICE; active family/drawing/spacing chain.
- **Color:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Web:** Stage 1 PASS; Stage 2 PRACTICE through W014; browser-runtime breadth remains active.

Type and Web remain the two Stage 2 incomplete specialists. This cycle selected Type because W014 had just received the latest Web treatment while T021 still had an explicit broader-family prerequisite before kerning. Future cycles must re-evaluate all four again.

## Active next queue
1. Replace the shared A/V/T/L/I `cap_aw/cap_lsb` control with shape-sensitive base-spacing groups; keep kerning OFF.
2. Re-run `HAVAL/AVAVA/TAVAT/LITIL` at 14/17/24px and classify whether remaining problems are drawing or spacing.
3. Add numerals, core punctuation and one accented construction path.
4. Only then open T022: kerning classes/exceptions + proportional/tabular figures.
5. T023 weight/interpolation + diacritic/punctuation coherence; T024 multi-role typography alternatives.
6. Exact LogMate Flutter need pre-empts nonessential curriculum expansion.

## OPEN / dependencies
Stage 2: shape-specific broader-family spacing revision, kerning model, integrated figures, punctuation/diacritics, design-level weight proof, final defended family selection.

Later: FontBakery/Fontspector/OTS, direct HarfBuzz, naming/style linking, hinting, multi-axis/CFF2/components, native/browser matrix, production PWA, larger complex scripts.

Human/app-stage validation remains deferred; no simulated human PASS.

## RELATED DOMAIN / HANDOFF state
Color remains fixed during geometry comparison. Layout L003 remains width/reflow constraint. Web later validates exact selected binaries under loading/fallback/zoom/localization; FreeType evidence is not browser proof. The latest broader-family transfer specifically warns Layout/Web not to freeze geometry against the intermediate shared-cap metrics.

## Latest checkpoint
- Stage 1: **PASS**.
- T020: **COMPLETE**.
- T021 initial custom-outline raster: **EXECUTED**.
- T021 lowercase `n` contour-only redraw/re-proof: **EXECUTED**.
- T021 A/V/T/L/I broader pre-kerning transfer: **EXECUTED**.
- Shared-cap spacing parameterization: **REWORK REQUIRED**.
- B direction: **WORKING, NOT FINAL**.
- T022: **NOT OPEN**.
- Stage 2: **NOT PASSED**.