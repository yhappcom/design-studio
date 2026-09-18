# T045 — LogMate Customize reorder-control Type transfer

## Purpose
TRANSFER VALIDATION of T044 under the next accessibility-critical Customize state: adding a non-drag reorder path without allowing control density to distort the still-open T021 drawing/spacing/kerning sequence.

## RELATED DOMAIN CHECK
- Type: T021 remains authoritative: drawing → general spacing → residual kerning. T044 supplies the 35-field professional corpus.
- Color: C075 requires state visibility to survive without hue-only encoding.
- Layout/Interaction: L066/I062 establish dense projection and drag-equivalence requirements.
- Web: W075 requires real-browser pointer/keyboard/non-drag closure.
- Content: CD081 separates semantic IDs, full names and compact ledger headers.

## SOURCE
WCAG 2.2 SC 2.5.7 requires dragging functionality to be achievable with a single pointer without dragging unless dragging is essential. The W3C explanatory example uses up/down controls for list reordering. SC 2.5.8 separately constrains pointer target size/spacing. These are interaction/accessibility requirements, not permission to compress typography.

## PRACTICE
The non-drag path creates a new string/control corpus: field label + move-earlier/move-later action + position/state feedback. Type acceptance therefore checks:
1. operational glyph ambiguity (`I/l/1/0`) remains attributable to the mature fallback while T021 R1 is open;
2. action labels and field labels may wrap/recompose rather than forcing reduced font size/tracking;
3. numerals in position feedback remain distinct from ledger-time totals such as `99,999+59`;
4. compact ledger headers remain separate from accessible/full Customize labels.

## CRITIQUE
A dense row can appear cleaner if action labels are icon-only or type is reduced. That is not a Type success if it removes semantic/accessibility information or masks a Layout constraint. Likewise kerning cannot be opened merely because additional reorder controls increase width pressure.

## REPRODUCIBLE VALIDATION CONTRACT
For the same semantic field IDs, capture at default and 200% text scale: resolved font/fallback, full visible/accessibility label, line count/clipping, target geometry supplied by Layout/Web, and screenshot/runtime exception status. Classify failures as TYPE-owned only with reproduced glyph/metric/fallback/raster evidence; otherwise return composition pressure to Layout.

## TRANSFER / OPEN
No new Type gate passes. T021 R1 mutation/raster remains the primary Type blocker. Browser/native/AT/human recognition evidence remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web should not solve reorder-control density by shrinking Type. Content should supply stable semantic IDs and input-neutral action names; Type validates their rendering rather than rewriting them.