# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / LOGMATE TYPE IDENTITY PRIORITY / T021 A+B EXACT RESET RASTER FAIL, OPERATIONAL-ARCHITECTURE GATE OPEN**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/drawing/spacing/operational evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## T021 latest evidence

Latest exact review: `research/type/T021-architecture-reset-complete-ci-raster-review.md`.  
Construction-complete harness: `research/type/T021-family-architecture-reset-complete-harness.py`.  
Dedicated proof: `.github/workflows/type-t021-architecture-reset-proof.yml`.  
Architecture-reset predecessor: `research/type/T021-family-architecture-reset-harness.py`.

The inherited-figure defect from the first A/B reset is now closed. All figures 0–9 dispatch through the reset construction path and an explicit provenance assertion covers every digit.

GitHub Actions run `35045568141`, job `104634521908`, checked out exact commit `c6a43969863aa5716dcb21047ad536ecfbc2e04a` and completed successfully on Ubuntu 24.04 / Python 3.13.15 / FontTools 4.65.0 / Pillow 12.3.0. Artifact `10427275894` retained both A/B TTFs, 14/17/24 specimens and JSON evidence.

Both architectures cover the same bounded corpus **36/36**, missing `[]`, kerning OFF. Exact 17px artifacts were downloaded and inspected. Neither A nor B passes coherent-family drawing: S/5 and 8/B remain weak at target size, round/bowl rhythm remains mechanically compressed, lowercase texture is not mature, and figure transitions remain schematic. B's slashed zero improves explicit 0/O separation but does not rescue family coherence.

A new source audit also tightens the architecture gate: declared tokens `corner`, `join`, `diag_comp`, and `terminal` are currently metadata-only or insufficiently consumed by relevant glyph constructors. Therefore closing predecessor delegation is not enough to call the architecture implementation complete.

## Evidence chain

Current chain:

`declared repertoire → architecture contract → construction provenance → architecture-token operationality → complete metrics/construction → executable build → cmap coverage → deterministic intended-size raster → drawing validity → general spacing → pair residual → kerning`

Current evidence passes construction provenance and exact CI/raster production but fails at **architecture-token operationality + drawing validity**.

## Current LogMate control boundary

Current `yhappcom/logmate` main uses proportional Roboto plus Noto Sans KR fallback. Proportional Roboto remains the valid current product control. Historical mono experiments are not current product evidence.

## Stage 2 matrix

| Requirement | Current state |
| --- | --- |
| coherent glyph family | **PRACTICE / FAIL — exact A+B raster inspected; neither architecture drawing-valid** |
| spacing/control strings | **PRACTICE; blocked by architecture/drawing gate** |
| kerning classes/exceptions | **OPEN / BLOCKED** |
| figure styles | **PRACTICE — all 0–9 reset-owned; A proportional-width hypothesis vs B semi-mono/slashed-zero hypothesis executable; drawing still FAIL** |
| diacritics/punctuation coherence | **PRACTICE; optical quality downstream of architecture completion** |
| weight/width relationships | **PRACTICE — A/B differences measurable in exact CI** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — exact A/B 14/17/24 retained and 17px inspected** |
| typography across product roles | **PARTIAL / STRONG BRIDGE; proportional Roboto current-main control verified** |
| multiple solutions + defended selection | **PRACTICE — A and B are real executable alternatives; both REWORK, no false winner selected** |

## Exact A/B geometry snapshot at 17px

A/B respectively: `ICN` 27.3906/27.7188; `JFK` 27.7812/29.9219; `B737-900` 72.7344/74.9531; `1,284:35` 65.7500/68.0000; `0O` 19.7500/19.8906; `1Il` 24.8125/26.5156; `5S` 19.0781/19.8906; `8B` 19.5469/19.8906; `AVAVA` 51.0156/51.0156.

These establish real width-system differences, not drawing quality.

## Active next queue — large block only

Do not begin spacing or T022.

1. reduce A/B architecture contracts to parameters that actually alter outlines;
2. add explicit consumer maps/assertions for stem, round-stem, aperture, overshoot, diagonal compensation, terminal policy, bowl/join policy, shoulder tension, figure-width mode and zero treatment;
3. make diagonal/terminal/join parameters operational instead of metadata labels;
4. rebuild both complete 36-character architectures with no predecessor glyph delegation;
5. rerun exact 14/17/24 CI and adversarial raster critique;
6. if both remain drawing-invalid after a genuinely operational architecture pass, compare the bespoke-font route itself against proportional Roboto rather than continuing indefinite local repair;
7. only a drawing-valid surviving architecture may enter repeated-context sidebearing analysis;
8. only after base spacing stabilizes enumerate residual pairs and consider T021 closure/T022.

## Evidence boundary

No A/B drawing PASS or product recommendation is claimed. Exact CI proves reproducibility, coverage and artifact generation only. Raster critique is designer evidence, not human recognition/error-rate evidence. Human/native/browser/physical-device validation remains OPEN/deferred as appropriate.

## HANDOFFS

- Layout/Interaction: B's regularized widths are measurable but must not be used to justify layout changes before Type drawing stabilizes.
- Web: no transfer test for either failed architecture.
- Content: preserve literal identifiers/numerics.
- Color: character identity remains independent of color.

## Latest checkpoint

- Stage 1: **PASS**.
- T020: **COMPLETE as Stage 2 entry**.
- R3 exact full CI: **PASS through retained raster / drawing FAIL**.
- R4A: **REJECTED**.
- R4B/R4C bounded grammar: **EXECUTED**.
- R4D/R4E exact full family: **36/36 + raster PASS / drawing FAIL**.
- serial local repair method: **REJECTED as sufficient strategy**.
- A/B reset figure provenance: **PASS — all 0–9 reset-owned**.
- A/B exact reset CI: **PASS — 36/36 + 14/17/24 artifacts**.
- A/B exact 17px drawing critique: **FAIL for both**.
- architecture-token operationality: **REWORK**.
- general spacing: **BLOCKED**.
- T022: **BLOCKED**.
- Stage 2: **NOT PASSED**.
