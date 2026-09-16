# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / LOGMATE TYPE IDENTITY PRIORITY / T021 R2 CANONICAL CI PASS, RASTER-DRAWING GATE OPEN**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/spacing/operational evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## T021 evidence state

Canonical R2 review: `research/type/T021-r2-canonical-ci-and-gate-review.md`.

The prior exact-source M metrics/construction blocker has been repaired in commit `340705130357eed2d715439bec1577ed94d40561`. GitHub Actions `Type T021 Proof` run `35041460583` checked out that exact commit and completed successfully on Ubuntu with Python 3.13.15, FontTools 4.65.0 and Pillow 12.3.0.

Exact-CI R2 output:
- revision `R2-structural`;
- kerning OFF;
- bounded distinct non-space corpus characters: **36**;
- covered: **36/36**;
- missing: `[]`;
- intended-size measurements executed at 14/17/24px.

Representative 17px exact-CI advances: `ICN` 28.1406px; `NRT` 31.2031px; `JFK` 28.7344px; `B737-900` 74.3438px; `1,284:35` 67.2812px; `0O` 20.0625px; `1Il` 25.8438px; `5S` 19.5469px; `8B` 19.9688px; `AVAVA` 51.8750px.

The four equal-length time strings `00:45`, `02:18`, `09:55`, `12:40` all measured 43.1562px at 17px, and the default R2 figures use equal advances in this bounded generator. This is geometry evidence, not a product decision that all figures should remain tabular/default-equal-width.

## Reproducibility correction resolved

Evidence chain now has direct canonical evidence through:
`declared repertoire → metric completeness → explicit construction dispatch → exact repository CI build → bounded cmap coverage`.

Unsupported uppercase construction fails rather than silently becoming a generic filled box.

The previous exact-source reproducibility FAIL is therefore **RESOLVED**.

## Workflow observability repair

The successful R2 run exposed a workflow path mismatch: the script writes under `/tmp/t021-logmate-expanded-r2/` while the workflow display/upload paths still referenced `/tmp/t021-logmate-expanded/`. This did not invalidate the proof execution, but it made the display step misleading. The workflow has now been aligned to the R2 directory for the next run.

## Stage 2 matrix

| Requirement | Current state |
| --- | --- |
| coherent glyph family | **PRACTICE — explicit R2 construction + canonical CI PASS; fresh raster drawing-quality gate OPEN** |
| spacing/control strings | **PRACTICE — exact-CI widths measured; optical sidebearing revision waits on raster drawing validity** |
| kerning classes/exceptions | **OPEN / BLOCKED until drawing + general spacing stabilize** |
| figure styles | **PRACTICE — equal-advance R2 default figures measured; proportional-vs-tabular alternative study belongs to T022** |
| diacritics/punctuation coherence | **PRACTICE — encoded/executable; optical/component quality still OPEN** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — exact 14/17/24 measurement exists; deterministic raster artifact/critique still OPEN** |
| typography across product roles | **PARTIAL / STRONG BRIDGE; proportional Roboto bounded comparison exists; exact product mono OPEN** |
| multiple solutions + defended selection | **PRACTICE — B metric direction remains provisional; final identity selection OPEN** |

## Active next queue — large block only

1. Extend the canonical harness to emit deterministic 14/17/24 specimen raster artifacts.
2. Execute canonical CI again and inspect the exact R2/R3 raster rather than infer visual quality from successful build.
3. Redraw any remaining S/figure/n/bowl/terminal/join defects and rerun within the same block.
4. Once drawing validity is credible, revise sidebearings/general spacing from repeated-context evidence.
5. Enumerate only true pair-specific residuals; these become T022 kerning candidates.
6. Compare accepted candidate against proportional Roboto and exact `LogMateRobotoMono` only if the exact artifact becomes available.
7. Close T021 only when its contract is satisfied; if closed, open T022 immediately and begin kerning-class/exception + proportional/tabular figure comparison.

## Evidence boundary

Canonical CI build/coverage is now proven. A fresh R2 raster drawing PASS is **not** claimed. No human recognition/error-rate, native Flutter, browser, or physical-device evidence is simulated. Exact LogMate mono comparison remains OPEN.

## Latest checkpoint

- Stage 1: **PASS**.
- T020: **COMPLETE as Stage 2 entry**.
- T021 first equivalent raster: **EXECUTED; drawing gate FAIL**.
- T021 exact-source M blocker: **RESOLVED**.
- T021 R2 exact repository CI build: **PASS**.
- bounded R2 cmap coverage: **36/36 PASS**.
- exact intended-size measurements: **14/17/24 EXECUTED**.
- R2 fresh raster drawing gate: **OPEN**.
- general spacing revision: **OPEN after raster**.
- T022: **BLOCKED**.
- Stage 2: **NOT PASSED**.
