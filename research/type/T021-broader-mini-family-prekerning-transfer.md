# T021 — Broader Mini-Family Pre-Kerning Transfer

Status: **PRACTICE + CRITIQUE / FAMILY EXTENSION EXECUTED, SHAPE-SPECIFIC SPACING REWORK REQUIRED**

This companion continues T021. It does not open T022.

## Purpose
The prior T021 redraw corrected a diagnosed lowercase `n` drawing defect while freezing metrics. The next queue required broader family evidence before kerning. This run extends all A/B/C controls from H/O/n/o to A/V/T/L/I, keeps kerning OFF, builds real research TTFs, and measures target-size strings at 14/17/24px.

Reason for repetition: **TRANSFER VALIDATION + CONTRADICTION REVIEW**. The existing A/B/C spacing hypotheses are transferred from straight/round controls into diagonal and terminal-sensitive capitals to test whether the same parameter model remains adequate.

## RELATED DOMAIN CHECK
- **Type:** Study 002, T020, T021 main study and lowercase redraw checked. Spacing-before-kerning remains binding.
- **Color:** held constant / not materially manipulated.
- **Layout / Interaction:** L003 width/reflow dependency remains relevant; this run records exact advances rather than claiming layout safety.
- **Web:** W012–W014 checked. FreeType execution is not browser/native evidence; exact binary transfer remains a later Web dependency.
- **Overlap decision:** deliberate Type-internal transfer. The goal is not to repeat H/O/n/o evidence but to challenge its spacing model with new glyph geometries.

## Method
Reproducible harness: `T021-broader-mini-family-prekerning-transfer.py`.

Fixed conditions:
- 1000 UPM;
- A/B/C stem and spacing directions retained;
- curved `n` working construction retained;
- A/V/T/L/I added to every direction;
- kerning OFF;
- Pillow/FreeType target sizes 14/17/24px;
- controls: `HAVAL`, `AVAVA`, `TAVAT`, `LITIL`, `HOnonO`, `nono`, `noon`, `onno`.

## Executed evidence
All three research fonts built and all controls rendered/measured successfully.

Representative advances:

| size | string | A | B | C |
|---|---|---:|---:|---:|
| 14px | `AVAVA` | 42.0312 | 43.4375 | 45.4688 |
| 17px | `AVAVA` | 51.0156 | 52.7344 | 55.2344 |
| 24px | `AVAVA` | 72.0312 | 74.3750 | 77.9688 |
| 14px | `HOnonO` | 47.4844 | 48.7500 | 51.0781 |
| 24px | `HOnonO` | 81.3750 | 83.4844 | 87.5938 |

A remains the narrow boundary, C the wide boundary, and B remains intermediate in nominal width.

## CONTRADICTION / failure exposed
The broader extension revealed a weakness in the current family parameterization: A/V/T/L/I all inherit one `cap_aw` and one `cap_lsb` inside each hypothesis. Consequently `HAVAL`, `AVAVA`, `TAVAT`, and `LITIL` have identical total advances within a given direction despite materially different edge shapes.

This equality is mechanically correct for the harness, but it is **not** evidence of coherent optical spacing. It exposes that the original hypothesis model is too coarse for diagonal/open/terminal-sensitive capitals.

Bounds confirm the same limitation. In B, A/V/T/L/I each occupy x=60..560 inside a 620u advance, while H occupies x=65..555. The test therefore succeeded as a family-build/raster transfer and simultaneously falsified the idea that one shared cap sidebearing is sufficient evidence for final pre-kerning spacing.

## CRITIQUE
### KEEP
- B remains the working overall width/stem direction; nothing in this execution reverses its role as the middle hypothesis.
- Curved `n` remains the working lowercase construction.
- Kerning remains OFF: the newly exposed issue is base spacing/model resolution, not pair adjustment.

### REWORK
- Split A/V/T/L/I from the shared `cap_lsb/cap_aw` control into shape-sensitive base-spacing groups.
- Re-measure the same strings after sidebearing differentiation so pair behavior can be judged before kerning.
- Inspect diagonal-to-diagonal (`AV/VA`), top-bar-to-diagonal (`TA/AT`), and open-right/vertical (`LI/IL`) classes separately.

### REJECT
- Do not open T022 kerning while all five new capitals share one spacing parameter.
- Do not interpret equal advances as optical consistency.
- Do not use kerning exceptions to conceal an under-resolved base-spacing model.

## SYNTHESIS
The evidence chain advances to:

`H/O/n/o family → raster drawing defect → contour redraw → broader A/V/T/L/I transfer → shared-metric model failure exposed → shape-specific base spacing next → only then kerning eligibility`.

This is useful Stage 2 evidence because execution produced a concrete model-level failure rather than a paper-only family extension.

## Evidence boundary
**SOURCE / EXECUTED:** fontTools built all A/B/C research fonts; Pillow/FreeType measured all specified strings at 14/17/24px.

**STUDIO JUDGMENT:** B remains the working direction, but broader-family spacing is REWORK.

**OPEN:** optical/human judgment, shape-specific sidebearings, kerning, numerals/punctuation/accented construction, browser/native transfer.

## HANDOFFS TO OTHER SPECIALISTS
### Layout / Interaction
The broader family preserves the A<B<C width ordering, but the next shape-specific spacing revision can change exact widths. Do not freeze product geometry against this intermediate artifact.

### Web
Do not browser-transfer this broader research font as if it were selected production typography. The useful later transfer point is after shape-specific spacing and T022 eligibility are established.

## Checkpoint
- A/V/T/L/I broader outline extension: **EXECUTED**.
- 14/17/24px pre-kerning measurement: **EXECUTED**.
- Shared-cap spacing model: **REWORK REQUIRED**.
- B direction: **WORKING, NOT FINAL**.
- T022: **STILL BLOCKED**.
- Stage 2: **NOT PASSED**.