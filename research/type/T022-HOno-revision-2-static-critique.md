# T022 — H/O/n/o Revision 2 Static Geometry Critique

Evidence type: PRACTICE / CRITIQUE / PARTIAL

## RELATED DOMAIN CHECK
Type owns contour construction. W025/L018/CD032/C027 remain transfer constraints only and do not determine glyph geometry. Human recognition evidence remains unavailable.

## What was executed
`T022-HOno-control-drawing-revision-2.svg` implements the previously specified second construction cycle while preserving A compact and B open hypotheses. This is an authored vector artifact, not a font binary and not a product recommendation.

## Static contour audit
The previous `n` construction used a rectangular stem plus a separate overlapping shoulder path. Revision 2 replaces that with one filled outer path per candidate. This removes the prior doubled overlap/wedge mechanism at the construction level. The shoulder still changes direction aggressively near the stem-to-arch transition, so optical smoothness requires raster/outline inspection before PASS.

The `o` counters are no longer simple-looking uniform insets relative to the outside widths: A uses a narrower/taller counter relationship than the outside mass; B preserves a wider open hypothesis. This is a construction improvement, not proof of mature curve tension.

Round/stem mass was deliberately adjusted rather than numerically equalized: H verticals were reduced from the first proof while O/o counters were reopened. Whether apparent darkness is actually balanced at 14/17/24 px remains visually unverified.

## Candidate distinction
A remains materially more compact; B remains materially wider/open in H/O/n/o. Revision therefore did not collapse the hypotheses merely to repair defects.

## Gate result
**PARTIAL CONSTRUCTION PASS; DRAWING PASS STILL OPEN.** The specific overlapping-path cause of the n wedge has been removed and the o counter construction has been revised, but trustworthy rendered visual inspection is still required for shoulder continuity, curve acceleration, overshoot and apparent weight. Spacing, kerning, S/5 and font-binary work remain blocked.

## HANDOFFS TO OTHER SPECIALISTS
Web/Layout continue mature product fonts. Content preserves literals. Color does not compensate for glyph ambiguity. No downstream specialist should consume Revision 2 as a production font asset.