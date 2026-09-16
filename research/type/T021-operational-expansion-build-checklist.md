# T021 — Operational expansion build checklist

Date: 2026-09-16
Evidence class: **PRACTICE specification / drawing gate remains open**

## RELATED DOMAIN CHECK
- **Color:** C029 cannot compensate for ambiguous glyph construction.
- **Layout/Interaction:** L020 must not freeze numeric widths from an incomplete candidate.
- **Web:** W029 continues with a mature system font; replacing it with the custom candidate is blocked.
- **Content:** CD034/CD035 provide operational strings and state language; wording must not be shortened merely to accommodate unfinished metrics.

## Purpose
Convert the broad T021 expansion contract into a build-order checklist that preserves drawing → general spacing → pair-specific residual discipline. This file does not claim newly drawn glyphs.

## Build order
1. **Control skeleton:** H O n o l I 1 0. Repair any contour or apparent-weight inconsistency first.
2. **Straight/diagonal capitals:** A V X N K M-like construction logic where corpus requires it; do not derive sidebearings from one universal cap width.
3. **Round/mixed capitals:** C D G? O U where corpus requires; preserve overshoot/round-stem optical relation.
4. **Remaining operational capitals:** B E F J L R S T and corpus-specific set.
5. **Digits 0–9:** establish zero distinction before family completion; keep proportional/tabular decision out of this gate unless base drawing/spacing passes.
6. **Punctuation:** `- : ,` and space with role-appropriate vertical placement and sidebearings.
7. **Accent path:** É from a coherent E + acute construction; validate vertical metrics/clipping rather than treating it as decorative add-on.
8. **notdef/fallback audit:** bounded corpus must render without unintended fallback/notdef.

## Proof strings
At 14/17/24px with kerning OFF, proof at minimum:
- airport/identifier clusters containing I/l/1, O/0 and dense capitals;
- times/durations using digits and colon;
- totals with repeated figures;
- hyphenated identifiers;
- É path;
- CD034/CD035 long operational state strings using mature fallback for unsupported characters until candidate coverage is complete.

## Failure classification
For every failure record exactly one primary class before repair:
1. drawing/contour;
2. general sidebearing/spacing;
3. raster/size-specific rendering;
4. fallback/notdef;
5. pair-specific residual — record only after 1–4 are cleared.

Only class 5 becomes evidence for opening T022. Kerning remains OFF throughout T021.

## Closure threshold
T021 cannot close on glyph count alone. The bounded repertoire must be complete enough to render the declared operational corpus, show no unintended fallback/notdef, survive 14/17/24px critique, and leave only explicitly enumerated pair-specific residuals. Human recognition and native-platform breadth remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- **Web/Layout:** continue using mature product/system fonts until T021 closure supplies valid metrics.
- **Content:** retain semantic wording; report overflow stress rather than editing truth to fit unfinished Type.
- **Color:** treat glyph ambiguity as Type failure, not a color-state problem.
