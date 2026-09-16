# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / LOGMATE TYPE IDENTITY PRIORITY / T021 TOKEN SENSITIVITY MEASURED, OPERATIONALITY REWORK**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 drawing and spacing stabilize

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 Stage 1; T020 Stage 2 entry; T021 ongoing operational-family authorship.

## Latest evidence
`T021-executable-token-sensitivity-review.md` records an exact GitHub Actions perturbation audit of the current architecture constructors. Run `35048091113` / job `104642269401` succeeded and fingerprinted compiled `glyf+hmtx` after one-token perturbations.

Against the current consumer matrix: FULL = `stem`, `round_stem`, `x_overshoot`, `figure_width`, `zero`; PARTIAL = `cap_overshoot`, `aperture`; NONE = `corner`, `join`, `diag_comp`, `terminal`. Thus only 5/11 declared token groups are fully operational; 2/11 are partial and 4/11 have zero executable effect. The audit source was tightened so FULL requires every required consumer, not merely one changed glyph.

This converts the previous qualitative source finding into executable evidence and narrows implementation targets. It does not change the drawing verdict: both current A/B rasters remain FAIL.

## Evidence chain
`repertoire → architecture contract → construction provenance → token consumer assertions → executable sensitivity → operational completeness → 36/36 build → 14/17/24 raster → drawing validity → general spacing → pair residual → kerning`

## Decision boundary
Do not reraster yet. Resolve the four NONE groups and two PARTIAL groups first. Consumer expectations themselves may be revised only with explicit design rationale; do not force meaningless deltas to satisfy a matrix. Once the architecture is defensibly FULL, rebuild/raster A/B. If both still fail drawing, execute bespoke-vs-current-Roboto comparison rather than another serial patch cycle.

## Stage 2 snapshot
- coherent glyph family: **FAIL / PRACTICE**
- bounded repertoire: **36/36 prior exact proof**
- construction provenance: **PASS**
- token consumer specification: **PASS as specification / subject to justified refinement**
- executable token sensitivity: **MEASURED — 5 FULL / 2 PARTIAL / 4 NONE**
- executable architecture operationality: **FAIL / REWORK**
- spacing: **BLOCKED by drawing**
- kerning/T022: **BLOCKED**
- target-size raster: prior exact evidence retained; new operational A/B reraster intentionally blocked

## Active queue — large block only
1. implement `corner` consumers in open/straight terminal classes;
2. implement `join` across B/D/P/R/8;
3. implement `diag_comp` across diagonal capitals and relevant figures;
4. implement `terminal` across C/G/S/5/E/F;
5. reconcile PARTIAL `cap_overshoot` and `aperture` contracts with defensible consumers;
6. rerun strict token-sensitivity audit until the operational contract is FULL;
7. only then rebuild 36/36 A/B, reraster 14/17/24 and critique drawing;
8. if both fail, compare bespoke route against current proportional Roboto;
9. open spacing only after drawing PASS; T022 only after spacing stabilizes.

## HANDOFFS
- Layout/Web continue using flexible/current product geometry, not A/B metrics.
- Content preserves literal identifiers/numerics.
- Color does not compensate ambiguity.

## Evidence boundary
No custom-family drawing PASS, executable operationality PASS, human readability/recognition, product preference, native/browser or physical-device PASS is claimed.
