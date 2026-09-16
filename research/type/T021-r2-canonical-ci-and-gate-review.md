# T021 — R2 Canonical CI and Gate Review

Status: **CANONICAL CI EXECUTED / BUILD + BOUNDED COVERAGE PASS / DRAWING + SPACING GATES STILL OPEN**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Scope

This review closes the reproducibility defect found after the first equivalent local execution. Commit `340705130357eed2d715439bec1577ed94d40561` repaired the exact repository generator and triggered `Type T021 Proof` run `35041460583`. The GitHub-hosted Ubuntu runner checked out that exact commit and executed `research/type/T021-logmate-operational-family-expansion-harness.py` with Python 3.13.15, FontTools 4.65.0 and Pillow 12.3.0.

## SOURCE → EXECUTION evidence

The canonical CI job completed successfully. All workflow steps, including dependency installation, T021 proof execution and artifact upload, completed with `success`.

The exact source reported:
- revision `R2-structural`;
- kerning `false`;
- artifact `T021-LogMate-Balanced-Expanded-R2.ttf`;
- declared uppercase `ABCDEFGHIJKLMNOPRSTUVX`;
- required distinct non-space corpus characters: 36;
- covered: 36;
- missing: `[]`;
- intended-size measurement at 14/17/24px.

This supersedes the prior exact-source reproducibility FAIL. It does not supersede the drawing-quality failure from the first raster review.

## Measured R2 evidence

Representative exact-CI advances at 17px:
- `ICN` 28.1406px
- `NRT` 31.2031px
- `JFK` 28.7344px
- `B737-900` 74.3438px
- `1,284:35` 67.2812px
- `0O` 20.0625px
- `1Il` 25.8438px
- `5S` 19.5469px
- `8B` 19.9688px
- `AVAVA` 51.8750px

All four equal-length time strings `00:45`, `02:18`, `09:55`, `12:40` measured 43.1562px at 17px. `1`, `11`, `111` and `8`, `88`, `888` also scale by an equal 9.5156px per figure. This demonstrates the current R2 default figures behave as equal-advance figures in this bounded generator. It does **not** establish that tabular figures should be the default product style; that choice belongs to T022's proportional-vs-tabular comparison.

## Reproducibility defect resolution

The previous blocker was valid for the prior source: declared repertoire, metrics and construction dispatch were inconsistent around M. R2 repairs this by requiring explicit metric coverage and explicit uppercase construction. Unsupported uppercase construction now fails rather than silently becoming a generic filled box.

Therefore the evidence chain now passes through:

`declared repertoire → metric completeness → explicit construction dispatch → canonical CI executable build → bounded cmap coverage`

The next gate remains raster drawing validity.

## Artifact-path defect found in workflow

The proof script wrote the JSON result under `/tmp/t021-logmate-expanded-r2/`, while the workflow's `cat` command still looked under `/tmp/t021-logmate-expanded/`. The log therefore printed `No such file or directory` for that display step even though the proof command itself succeeded. Artifact upload targeted the parent `/tmp/t021-logmate-expanded/` tree and uploaded two files, so the run remained successful.

**STUDIO JUDGMENT:** this is a proof-workflow observability defect, not a font-build failure. The workflow should be aligned to the R2 output directory before treating its human-readable result-display step as reliable.

## Gate review

### PASS — exact-source reproducibility

The exact repository generator builds on a clean GitHub-hosted runner and produces the expected bounded measurements.

### PASS — bounded encoded coverage

36/36 distinct non-space characters required by the current operational corpus are encoded with no missing characters.

### OPEN — drawing validity

R2 removed known placeholder/fallback mechanisms and replaced several structural primitives, but CI success cannot judge visual coherence. No claim is made that S, figures, n, bowls, terminals, joins or ambiguity forms are visually mature. The earlier raster critique remains a reason to require a fresh R2 raster inspection rather than infer PASS from source structure.

### OPEN — general spacing

Advance equality and string widths are measurements, not proof of optical spacing. Base sidebearings must be judged only after R2 drawings are inspected.

### OPEN — pair-specific residual / kerning

No pair is promoted to T022 while drawing and general-spacing gates remain open.

### OPEN — product control comparison

Proportional Roboto has bounded prior geometry evidence. Exact `LogMateRobotoMono` binary comparison remains unavailable in the current evidence chain and must not be substituted with a generic mono.

## T021 closure decision

**DO NOT CLOSE T021 YET.**

The exact-source reproducibility blocker is resolved, which is a major gate advance. However, the T021 contract also requires credible drawing/base-spacing evidence and rendered intended-size critique. R2 still needs an actual raster artifact suitable for inspection and any resulting redraw/spacing iteration.

## Next large block

1. Repair the workflow output-directory mismatch.
2. Make the canonical proof emit deterministic 14/17/24 specimen PNG(s), not only a TTF and JSON measurements.
3. Run canonical CI again and inspect the emitted R2 raster artifact.
4. Redraw any remaining structural defects and rerun in the same block.
5. Only after drawing validity, revise general spacing and enumerate residual pairs.
6. Decide T021 closure and, if it passes, open T022 immediately.

## RELATED DOMAIN CHECK

- Layout/Interaction: equal figure advances are useful evidence for comparison columns, but whole-family geometry must not be frozen around a research candidate.
- Web: canonical CI reproducibility improves transfer readiness; browser rendering remains untested for R2.
- Content Design: literal LogMate operational strings remain unchanged.
- Color: held constant; no Type conclusion depends on color.

## Verdict

**R2 resolves the exact-source build/repertoire blocker and establishes canonical CI reproducibility with 36/36 bounded coverage. T021 remains OPEN because visual drawing and optical spacing are independent gates that CI build success does not satisfy.**
