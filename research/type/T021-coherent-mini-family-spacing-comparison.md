# T021 — Coherent Mini-Family + Spacing Comparison Practice

Status: **STAGE 2 PRACTICE + CRITIQUE — custom-outline raster proof executed; B survives as working direction; lowercase drawing revision OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`

Companion evidence:
- `T021-mini-family-comparison-metrics.json`
- `T021-mini-family-comparison-specimen.svg`
- `T021-outline-render-proof.py`
- `T021-outline-render-measured-summary.json`

## Purpose
T020 identified the largest Stage 2 gap as integrated family/system practice. T021 compares three pre-kerning construction/spacing hypotheses and subjects them to actual custom-outline rendering before kerning.

## RELATED DOMAIN CHECK
### Typography / Type
Study 002, T002, T006 and T020 reused: H/O and n/o controls; spacing before kerning; intended-size proof; source/metric audit.
### Color
Color held constant so geometry/stem/spacing remain the manipulated variables.
### Layout / Interaction
L003 reused: width differences can become wrap/layout differences near thresholds.
### Web Design
FreeType/Pillow is not browser delivery. T016 remains browser loading/fallback baseline.
### Overlap decision
**PRACTICE + COMPARISON + FAILURE/REVISION.** Foundation principles are deliberately repeated at a higher evidence level because Stage 2 requires alternatives, critique and defended selection.

## Exercise contract
1000 UPM; baseline 0; x-height 500; cap 700; round overshoot about 10–12u; kerning OFF; target raster 14/17/24px.

- **A Compact geometric:** 90u stem, tight bearings.
- **B Balanced text:** 85u stem, moderate differentiated bearings.
- **C Open screen:** 82u stem, generous bearings.

## PRACTICE — actual execution
`T021-outline-render-proof.py` builds H/O/n/o research TTFs and renders repeated strings through Pillow/FreeType.

### Failure discovered
The first real execution failed before rendering: the ellipse helper emitted cubic Béziers directly into TrueType `glyf` format 0. FontTools rejected glyph O.

### Revision
The harness now routes cubic construction curves through `Cu2QuPen` before `glyf` serialization. All three TTFs then built and rendered.

**SYNTHESIS:** executable practice exposed a source/build incompatibility that source inspection alone had missed.

## Measured evidence
Representative FreeType advances:

| size | string | A | B |
|---|---|---:|---:|
|14px|`HHOO`|33.9062px|34.7500px|
|14px|`HOHOHO`|50.8594px|52.1250px|
|14px|`nono`|29.4062px|30.2500px|
|17px|`HHOO`|41.1562px|42.1875px|
|17px|`HOHOHO`|61.7344px|63.2812px|
|24px|`HHOO`|58.0938px|59.5312px|
|24px|`HOHOHO`|87.1406px|89.2969px|

A remains the compact/dark boundary. C remains the visibly lighter/open boundary. B remains intermediate at all three tested sizes.

## CRITIQUE
### A — REWORK / compact control
Strongest apparent black mass and smallest footprint. Useful adversarial boundary, but later diagonal/round additions may create exception pressure if spacing remains this tight.

### B — KEEP AS WORKING DIRECTION
The raster does not falsify the original middle hypothesis. B preserves moderate footprint and mass and therefore survives the first intended-size challenge. This is not a final family selection.

### C — REJECT AS DEFAULT / retain stress control
Most open/light but with the largest horizontal cost. No evidence yet establishes a task benefit sufficient to justify default selection.

### Critical defect — lowercase `n`
Actual rendering exposed a more important family problem: the current `n` shoulder is too rectangular/schematic beside round `o`. This is a **DRAWING defect**, not a kerning defect. Pair-specific spacing must not hide it.

## SYNTHESIS
The evidence chain is now:

`metric hypothesis → actual outline → build failure → source correction → 14/17/24px raster → drawing/spacing classification → revision before kerning`.

B survives, but T021 cannot close while lowercase construction remains incoherent.

## STUDIO JUDGMENT
Do not open T022. Redraw B `n` with a coherent curved shoulder, re-render `nono/noon/onno/HOnonO`, and reassess sidebearings. A/C remain controls. Once B lowercase stabilizes, extend A/V/T/L/I with kerning OFF, then numerals/core punctuation/accented construction.

## OPEN
- B `n` curved-shoulder redraw/re-proof;
- spacing revision if contour change alters perceived side space;
- A/V/T/L/I extension, kerning OFF;
- numerals/core punctuation;
- one accented construction path;
- browser/native transfer;
- human evidence.

Stage 2 remains **NOT PASSED**.

## HANDOFFS TO OTHER SPECIALISTS
### Color
Keep Color fixed during redraw comparison; no Color conclusion claimed.
### Layout / Interaction
Later transfer should stress exact selected artifact widths; do not infer fixed-cell safety from nominal metrics.
### Web Design
Corrected TTFs are FreeType evidence only; exact binaries need browser loading/fallback/zoom/localization transfer later.

## Checkpoint
- Three alternatives: **ESTABLISHED**.
- Actual custom-outline build: **EXECUTED after source correction**.
- 14/17/24px raster proof: **EXECUTED**.
- B working direction: **SURVIVES FIRST RASTER CHALLENGE**.
- Lowercase coherent-family proof: **REWORK REQUIRED**.
- Kerning: **NOT STARTED intentionally**.
- Stage 2: **NOT PASSED**.