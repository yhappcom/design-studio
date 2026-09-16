# T021 — R2 Canonical CI and Gate Review

Status: **CANONICAL CI EXECUTED / BUILD + BOUNDED COVERAGE PASS / DRAWING GATE SUBSEQUENTLY FAILED**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Scope

Commit `340705130357eed2d715439bec1577ed94d40561` repaired the exact repository generator and triggered `Type T021 Proof` run `35041460583`. The GitHub-hosted Ubuntu runner checked out that exact commit and executed `research/type/T021-logmate-operational-family-expansion-harness.py` with Python 3.13.15, FontTools 4.65.0 and Pillow 12.3.0.

## SOURCE → EXECUTION evidence

The canonical CI job completed successfully. The exact source reported revision `R2-structural`, kerning OFF, artifact `T021-LogMate-Balanced-Expanded-R2.ttf`, declared uppercase `ABCDEFGHIJKLMNOPRSTUVX`, 36 required distinct non-space corpus characters, 36 covered, no missing characters, and 14/17/24px measurements.

Representative exact-CI advances at 17px: `ICN` 28.1406px; `NRT` 31.2031px; `JFK` 28.7344px; `B737-900` 74.3438px; `1,284:35` 67.2812px; `0O` 20.0625px; `1Il` 25.8438px; `5S` 19.5469px; `8B` 19.9688px; `AVAVA` 51.8750px.

All four equal-length time strings `00:45`, `02:18`, `09:55`, `12:40` measured 43.1562px at 17px. The R2 figures are equal-advance in this bounded generator. This is geometry evidence, not a decision that the product should use tabular figures everywhere.

## Reproducibility defect resolution

The prior M blocker was valid for the older source. R2 requires explicit metric coverage and explicit uppercase construction. Unsupported uppercase construction now fails rather than silently becoming a generic filled box.

Evidence therefore passes through:
`declared repertoire → metric completeness → explicit construction dispatch → canonical CI executable build → bounded cmap coverage`.

## Correction to earlier artifact-path wording

The first version of this note incorrectly stated that the R2 script wrote under `/tmp/t021-logmate-expanded-r2/`. Re-reading the exact canonical source showed `OUT=Path('/tmp/t021-logmate-expanded')`. The workflow had been changed to the wrong `-r2` path after that mistaken audit. That change was subsequently corrected: the workflow now reads and uploads from `/tmp/t021-logmate-expanded/` and runs a deterministic raster-proof script.

This correction is intentionally explicit: repository source, not prior prose, is canonical.

## Subsequent raster evidence

Workflow run `35041942223` on commit `eeb618682ba56b8bb762669f1fb401806e3eecef` completed successfully with a new deterministic raster step. Its artifact contains the exact R2 TTF, measured JSON, and 14/17/24px specimen PNGs. The fresh raster inspection is recorded separately and **fails drawing validity**. Therefore the earlier OPEN drawing gate is no longer merely untested; it has direct negative evidence.

## Product-control correction

A fresh tree audit of current `yhappcom/logmate` `main` found `assets/fonts/NotoSansKR-wght.ttf`, `Roboto-Regular.ttf`, and `Roboto-Medium.ttf`, but no Roboto Mono binary. Current `pubspec.yaml` declares only `LogMateNotoSansKR` and `LogMateRoboto`. Therefore an exact `LogMateRobotoMono` product-control comparison is not a current-main requirement unless that asset is reintroduced or another branch is explicitly selected. A generic mono must not be mislabeled as a current product control.

## Gate review

- exact-source reproducibility: **PASS**
- bounded encoded coverage: **PASS — 36/36**
- deterministic 14/17/24 raster production: **PASS as evidence-generation mechanism**
- drawing validity: **FAIL — see fresh raster critique**
- general spacing: **BLOCKED by drawing failure**
- pair-specific residual / kerning: **BLOCKED**
- T021 closure: **NO**

## RELATED DOMAIN CHECK

- Layout/Interaction: do not freeze product columns around this research candidate.
- Web: browser rendering remains separate evidence.
- Content Design: operational corpus literals remain stable.
- Color: held constant.

## Verdict

**R2 is now reproducible and fully inspectable, but the new exact raster proves that executable coverage is not sufficient: the drawing system is still too primitive for T021 closure.**
