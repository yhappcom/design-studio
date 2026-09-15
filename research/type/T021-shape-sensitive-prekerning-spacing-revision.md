# T021 — Shape-Sensitive Pre-Kerning Spacing Revision

Status: **PRACTICE + CRITIQUE / SHARED-CAP MODEL REPLACED, PRE-KERNING FAMILY STILL OPEN**

This companion continues T021 and does not open T022.

## Purpose
The prior broader-family transfer deliberately challenged the H/O/n/o spacing model with A/V/T/L/I and exposed a concrete failure: all five capitals inherited one `cap_aw/cap_lsb`, making shape-different control strings mechanically equal in total advance. This run replaces that under-resolved parameterization with per-glyph base metrics while keeping kerning OFF.

Reason for repetition: **CONTRADICTION REVIEW + REPLICATION + TRANSFER VALIDATION**. The same control strings and target sizes are retained so the prior failure can be tested under one changed variable: shape-sensitive base spacing.

## RELATED DOMAIN CHECK
- **Type:** Study 002, T020, T021 main study, lowercase redraw, and broader-family transfer checked. Spacing-before-kerning remains binding.
- **Color:** no color variable is manipulated; contrast/color evidence cannot resolve glyph spacing.
- **Layout / Interaction:** L003 remains the width/reflow dependency. Exact advances are evidence inputs, not a claim that product geometry is safe.
- **Web:** W012–W015 checked through current specialist status. This FreeType/Pillow execution is not browser/native font proof; Web transfer remains downstream of a stable family.
- **Overlap decision:** deliberate replication of the prior controls to test whether the diagnosed parameter-model failure disappears after base-spacing resolution increases.

## Method
Reproducible harness: `T021-shape-sensitive-prekerning-spacing-revision.py`.

Fixed:
- 1000 UPM;
- A/B/C overall compact/balanced/open directions;
- curved lowercase `n` working construction;
- same glyph set H/O/n/o/A/V/T/L/I;
- kerning OFF;
- Pillow/FreeType at 14/17/24px;
- same strings `HAVAL`, `AVAVA`, `TAVAT`, `LITIL`, `HOnonO`, `nono`, `noon`, `onno`.

Changed:
- A/V/T/L/I no longer share `cap_aw/cap_lsb`;
- each receives an explicit advance/LSB pair within each A/B/C direction.

These per-glyph values are research hypotheses, not optically validated production metrics.

## Executed evidence
All A/B/C research TTFs built and all controls measured.

Representative 17px results:

| string | A | B | C |
|---|---:|---:|---:|
| `HAVAL` | 49.3906 | 51.0156 | 53.2188 |
| `AVAVA` | 50.1562 | 51.8750 | 53.9844 |
| `TAVAT` | 49.4688 | 51.0000 | 53.1406 |
| `LITIL` | 39.7812 | 41.0312 | 43.0312 |
| `HOnonO` | 57.6562 | 59.2031 | 62.0469 |

The prior pathological equality among `HAVAL/AVAVA/TAVAT/LITIL` is gone at every tested size. B remains intermediate between A and C for every control.

The lowercase permutation controls `nono/noon/onno` remain equal in advance. That is expected with identical glyph counts and kerning OFF; it is now correctly classified as a limitation of advance-only pre-kerning measurement, not evidence of equal optical pair quality.

## CONTRADICTION REVIEW
Prior conclusion: the shared-cap parameterization was insufficient. **CONFIRMED.** Increasing model resolution to per-glyph metrics removes the mechanically forced equality without introducing kerning.

A stronger claim — that these new metrics are optically correct — is **NOT ESTABLISHED**. Total advances prove that the model can represent shape-sensitive widths; they do not prove pair rhythm, sidebearing quality, or human readability.

## CRITIQUE
### KEEP
- B remains the working middle direction.
- Curved `n` remains the working lowercase construction.
- Separate base metrics for diagonal/top-bar/open-right/narrow capitals.
- Kerning OFF while base-spacing evidence is still being stabilized.

### REWORK
- Add raster/pixel-bound or outline-gap diagnostics for AV/VA, TA/AT, LI/IL rather than relying on string advance alone.
- Add numerals, core punctuation, and one accented construction before declaring the mini-family broad enough for T022.
- Revisit exact A/V/T/L/I LSB/RSB values if gap diagnostics expose systematic collisions or holes.

### REJECT
- Shared `cap_aw/cap_lsb` as the final base-spacing model.
- Interpreting distinct total advances as proof of optical correctness.
- Opening kerning solely because the equality defect disappeared.

## SYNTHESIS
The chain is now:

`family hypotheses → real outlines → drawing defect → contour redraw → broader transfer → shared-cap model falsified → shape-sensitive base metrics executed → pair-gap diagnostics + numerals/punctuation/accent next → kerning eligibility`.

The important advance is methodological: base spacing must have enough degrees of freedom to represent materially different glyph geometry before pair-specific kerning is allowed to compensate residual relationships.

## Evidence boundary
**EXECUTED:** fontTools build plus Pillow/FreeType advances for all A/B/C controls at 14/17/24px.

**STUDIO JUDGMENT:** B remains working, not final; per-glyph metric resolution is retained.

**OPEN:** optical gap diagnostics, numerals/punctuation/accent, kerning, human judgment, browser/native transfer.

Human validation remains deferred to app-development validation; no human PASS is simulated.

## HANDOFFS TO OTHER SPECIALISTS
### Layout / Interaction
Exact capital widths changed after the base-spacing correction. Intermediate Type metrics remain unsuitable as frozen layout geometry; L003-style reflow validation should use a later stable binary.

### Web
Do not treat this research font as production-ready. Browser transfer becomes materially useful after pair-gap diagnostics and basic family breadth establish T022 eligibility.

## Checkpoint
- Shared-cap model failure: **CONFIRMED AND REMOVED FROM CURRENT HARNESS**.
- Shape-sensitive A/V/T/L/I metrics: **EXECUTED**.
- 14/17/24px replication: **EXECUTED**.
- B: **WORKING, NOT FINAL**.
- T022: **STILL BLOCKED** pending pair-gap diagnostics and numerals/punctuation/accent breadth.
- Stage 2: **NOT PASSED**.