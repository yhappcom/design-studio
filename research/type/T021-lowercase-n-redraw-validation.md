# T021 — Lowercase `n` Redraw Validation

Status: **PRACTICE + CRITIQUE / DRAWING DEFECT REWORK EXECUTED**

This companion continues `T021-coherent-mini-family-spacing-comparison.md`; it does not open T022.

## Purpose
T021's first actual raster exposed the B-direction lowercase `n` shoulder as rectangular/schematic beside `o`. The next highest-value Type task was therefore to correct the drawing before any kerning work.

Reason for repetition: **REPLICATION + CONTRADICTION REVIEW**. The same `nono/noon/onno` controls are intentionally reused so the manipulated variable is the `n` contour rather than spacing, kerning, size, or color.

## RELATED DOMAIN CHECK
- **Type:** T002/T020/T021 checked. Spacing-before-kerning and intended-size proof remain binding.
- **Color:** held constant; no Color conclusion is claimed.
- **Layout / Interaction:** L003 width/reflow dependency checked. Advance widths are intentionally frozen during this contour-only test.
- **Web:** W012/W013 runtime evidence checked. This FreeType/Pillow proof is not browser proof; later Web transfer remains required.

## Method
A bounded independent redraw harness rebuilt two B-direction research fonts:

1. `old` — rectangular shoulder control;
2. `curved` — same 1000 UPM, 540u `n` advance, 58u `n` LSB, 85u nominal stem, but with a cubic shoulder converted to quadratic TrueType outlines through `Cu2QuPen`.

Kerning remained OFF. `o` geometry and all advances remained fixed. Controls were rendered with Pillow/FreeType at 14/17/24px.

Strings: `nono`, `noon`, `onno`.

## Executed results
All old/curved strings retained exactly the same advances because spacing metrics were frozen:

| size | advance for each four-glyph control |
|---|---:|
| 14px | 30.25px |
| 17px | 36.75px |
| 24px | 51.8125px |

Yet raster comparison confirms that the contour manipulation materially changed rendered pixels:

| size | changed pixels | absolute grayscale difference sum |
|---|---:|---:|
| 14px | 168 | 16,650 |
| 17px | 312 | 24,612 |
| 24px | 414 | 56,310 |

This is useful because it separates **drawing change** from **spacing change**: the redesign alters the raster while preserving nominal string width.

## CRITIQUE
### KEEP
- Curved shoulder direction is structurally more appropriate than the rectangular control for the next B-family iteration.
- Frozen advances make this a cleaner contour comparison than changing outline and sidebearings simultaneously.

### REWORK
- This run proves contour/raster change, not final optical quality. The shoulder joins and interior counter still need inspection alongside `H/O/n/o` and then A/V/T/L/I.
- Sidebearings must be reassessed only after the contour is accepted; identical advances are an experimental control, not evidence that current spacing is final.

### REJECT
- Do not use kerning to repair the old rectangular shoulder.
- Do not declare coherent-family PASS from pixel-difference counts; those counts establish that a rendering change occurred, not that humans prefer or read it better.

## SYNTHESIS
A useful Type practice order is reinforced:

`drawing defect → contour-only redraw with metrics frozen → intended-size raster confirmation → optical critique → spacing revision → broader family extension → kerning eligibility`.

This prevents pair adjustments from concealing glyph-construction defects.

## Evidence boundary
**SOURCE/EXECUTED:** fontTools + Pillow/FreeType built and rendered both controls successfully in the available environment.

**STUDIO JUDGMENT:** curved shoulder survives as the next working construction.

**OPEN:** human optical judgment, browser/native rendering, final sidebearings, broader family coherence, kerning.

## HANDOFFS TO OTHER SPECIALISTS
### Layout / Interaction
The contour changed without changing advance width. Therefore a visual Type revision does not automatically imply layout geometry change; later spacing revision may.

### Web
When the selected binary stabilizes, browser transfer should test the exact artifact rather than infer behavior from this FreeType proof.

## Checkpoint
- T021 lowercase drawing defect: **REWORK EXECUTED**.
- Curved `n`: **WORKING CONSTRUCTION, NOT FINAL**.
- Width control: **PRESERVED**.
- T022 kerning: **STILL BLOCKED** until broader B family/spacing evidence is stable.
