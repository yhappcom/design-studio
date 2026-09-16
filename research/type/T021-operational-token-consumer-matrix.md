# T021 — Operational Token Consumer Matrix

Classification: **METHOD CONTROL + ARCHITECTURE IMPLEMENTATION SPECIFICATION**

## RELATED DOMAIN CHECK
- C020 explicitly forbids color compensation for glyph ambiguity.
- L012 does not freeze geometry around a custom candidate and requires metric-change tolerance.
- I007/CD020 preserve operational identifiers and consequential strings as proof inputs.
- W020 keeps the current product typography control until T021 drawing passes.

## Purpose
The prior operational-architecture gate found that an architecture dictionary can differ while outlines remain insufficiently different. This matrix turns each architecture token into an explicit implementation obligation before another A/B raster comparison.

## Consumer matrix
| Token | Required consumers | Observable effect | Invalid shortcut |
| --- | --- | --- | --- |
| stem | H/I/E/F/L/T + straight segments | stem/crossbar thickness | metadata only |
| round_stem | O/o/0 + B/D/P/R/8 bowls | counter/curve compensation | aliasing stem everywhere |
| aperture | C/G/S/5 where structurally relevant | opening geometry | unrelated width tweak |
| cap/lower overshoot | O/C/G/S/U/o/0 as justified | vertical extrema | metric-only declaration |
| diag_comp | A/V/X/K/R leg + diagonal figures where present | diagonal thickness/placement | consuming token without outline delta |
| terminal_policy | C/G/S/5 + open straight endings | terminal cut/shape/position | label only |
| bowl_join | B/D/P/R/8 | join inset/tension/counter relationship | independent ad-hoc bowls |
| shoulder_tension | n/S transition groups | shoulder/spine control points | same geometry under different token |
| figure_width_mode | 0–9 metrics | coordinated numeric rhythm | applying only to selected figures |
| zero_treatment | 0 only | slash/plain treatment while O stays independent | changing O to exaggerate comparison |

## Pre-export assertions
A/B rebuild MUST fail before export if:
1. any declared token has no named consumers;
2. A/B values differ but no intended outline/metric delta exists;
3. any bounded operational glyph delegates predecessor geometry;
4. any digit escapes the figure-width policy;
5. zero comparison changes O or unrelated glyphs;
6. kerning exists;
7. source provenance cannot identify which constructor consumed which token.

## Drawing gate sequence
`token operationality → full 36/36 build → 14/17/24 identical corpus → exact artifact critique → drawing PASS/FAIL → only then general spacing`.

If both fully operational architectures still fail drawing, the next method is bespoke-vs-current-Roboto comparison, not R4-style serial patching.

## Current verdict
**Specification complete; executable operationality proof remains OPEN. T021 drawing remains FAIL/PRACTICE. Spacing and T022 remain BLOCKED.**

## HANDOFFS TO OTHER SPECIALISTS
No peer should consume A/B metrics as stable. Preserve original strings and layout flexibility until executable drawing evidence passes.