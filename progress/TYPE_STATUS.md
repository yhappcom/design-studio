# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 RASTER EXECUTED, LOWERCASE REWORK NEXT**  
Governance sync: 2026-09-15  
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

Three pre-kerning hypotheses: A Compact, B Balanced, C Open.

### Executed evidence
The custom-outline harness was actually run in a Python/fontTools/Pillow environment. Initial execution exposed a real build defect: cubic curves were written directly to TrueType glyf format 0. The harness was corrected to convert construction cubics through `Cu2QuPen`, after which all A/B/C research TTFs built and rendered at 14/17/24px.

B survives as the working direction; A remains compact/dark control; C remains open/light stress control. This is not a final family PASS.

### Critical critique
Actual raster inspection exposed the current lowercase `n` shoulder as too rectangular/schematic beside `o`. Classification: **DRAWING defect**, not spacing/kerning. Therefore T022 remains intentionally blocked.

Current chain:
`metric alternatives → actual outlines → build failure → source correction → raster proof → drawing defect → redraw/re-proof → extension → kerning eligibility`.

## Stage 2 matrix
| Requirement | Current state |
|---|---|
| coherent glyph family | **PRACTICE — H/O/n/o executed; lowercase rework required** |
| spacing/control strings | **PRACTICE — actual 14/17/24px proof established; revision next** |
| kerning classes/exceptions | **OPEN; deliberately deferred** |
| figure styles | **PARTIAL / STRONG BRIDGE** |
| diacritics/punctuation coherence | **PARTIAL** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — T021 intended-size raster now executed** |
| typography across product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PRACTICE — B survives first raster challenge; final selection OPEN** |

## Active next queue
1. Redraw B lowercase `n` shoulder as a coherent curved form and re-render `nono/noon/onno/HOnonO` at 14/17/24px.
2. Reassess B sidebearings after contour change; classify remaining defects without kerning.
3. Extend B/relevant controls to A/V/T/L/I with kerning OFF.
4. Add numerals, core punctuation and one accented construction path.
5. Only then open T022: kerning classes/exceptions + proportional/tabular figures.
6. T023 weight/interpolation + diacritic/punctuation coherence; T024 multi-role typography alternatives.
7. Exact LogMate Flutter need pre-empts nonessential curriculum expansion.

## OPEN / dependencies
Stage 2: lowercase redraw, broader mini-family, spacing revision, kerning model, integrated figures, punctuation/diacritics, design-level weight proof, final defended family selection.

Later: FontBakery/Fontspector/OTS, direct HarfBuzz, naming/style linking, hinting, multi-axis/CFF2/components, native/browser matrix, production PWA, larger complex scripts.

Human/app-stage validation remains deferred; no simulated human PASS.

## RELATED DOMAIN / HANDOFF state
Color remains fixed during geometry comparison. Layout L003 remains width/reflow constraint. Web later validates exact selected binaries under loading/fallback/zoom/localization; FreeType evidence is not browser proof.

## Latest checkpoint
- Stage 1: **PASS**.
- T020: **COMPLETE**.
- T021 actual raster: **EXECUTED after fixing a real source/build defect**.
- B: **working direction survives, not final**.
- Lowercase `n`: **REWORK REQUIRED**.
- T022: **NOT OPEN**.
- Stage 2: **NOT PASSED**.