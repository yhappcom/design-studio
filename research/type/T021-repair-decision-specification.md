# T021 — Drawing Repair Decision Specification

Evidence purpose: **PRACTICE + CRITIQUE PREPARATION**. This converts the direct normalized A/B critique into bounded drawing decisions without opening spacing or kerning.

## RELATED DOMAIN CHECK
- **Color:** C040 cannot compensate for character ambiguity.
- **Layout/Interaction:** L031/I027 require stable identifiers but must not freeze provisional metrics.
- **Web:** W040 remains on mature fallback until Type gates pass.
- **Content:** CD046 preserves operational identifiers and audit strings; they remain stress strings rather than being shortened for fit.
- **UX:** human recognition/error-rate evidence remains OPEN.

## Repair hypotheses
### I / l / 1
The three glyphs require different primary silhouettes, not merely tiny terminal differences that disappear at 14–17 px.
- `I`: preserve an unmistakable capital construction with bilateral horizontal terminals sufficiently substantial to survive target raster sizes.
- `l`: preserve a lowercase silhouette whose terminal/direction differs structurally from both I and 1; do not rely on a one-pixel cosmetic hook.
- `1`: retain numeral identity through a distinct top entry and/or base construction; avoid converging on lowercase l.

The repair must be evaluated as a **three-glyph system** in repeated mixed strings, not one glyph at a time.

### B zero
Retain explicit O/0 differentiation, but reduce slash dominance. The slash is a discrimination cue, not the visual center of every numeric string. Candidate repair variables are slash weight, inset/overshoot and intersection treatment. Any reduction that causes O/0 convergence is rejected.

## Required rerender matrix
Kerning remains OFF. Rerender at 14/17/24 px using at minimum:
- `Il1 I1l lI1 111 lll III`;
- `O0 00 OO 00:45 B737-900`;
- bounded airport, identifier, numeric and spacing rows from the normalized proof.

For each repair record source/build hash, size, raster capture, defect class and before/after verdict. A repair is rejected if it improves one synthetic ambiguity row but degrades operational strings materially.

## Gate order
1. drawing repair;
2. rerender/direct critique;
3. only then general spacing;
4. only residual pair-specific defects may reach T022.

No sidebearing or kerning change is authorized merely to make the repaired silhouettes appear less awkward.

## Verdict
This specification makes the next drawing iteration executable, but it is **not drawing evidence**. T021 remains OPEN; general spacing and T022 remain BLOCKED.

## HANDOFFS TO OTHER SPECIALISTS
Web should continue mature fallback. Content should preserve the exact stress strings. Layout should avoid locking widths. Color should treat the repaired glyph system as an independent discrimination channel, not a semantic-color substitute.