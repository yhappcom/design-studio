# T079 — Non-drag reorder string/rendering stress

## PURPOSE
Support I097/L101 without violating T021's drawing→spacing→kerning gate.

## RELATED DOMAIN CHECK
I097/L101 define action and geometry; C109 state salience; W109 runtime/fallback provenance; CD115 semantic truth. Type does not redefine reorder behavior.

## PRACTICE CORPUS
Render with mature production/fallback families while T021 remains open:
- Move up
- Move down
- Move to position
- Position 1 of 7 / 3 of 7 / 7 of 7
- Aircraft registration
- Flight number
- Departure / Arrival
- Block time
- Remarks
- Can't move further up/down
- Order not saved / Retry / Undo

Stress baseline, enlarged text, WCAG text spacing, narrow action regions, actual fallback, numerals 1/3/7 and ambiguity-critical `I/l/1/0` in surrounding operational strings.

## SYNTHESIS
Control fit is downstream of semantic wording and mature rendering. Do not shorten necessary labels, apply negative tracking, narrow glyphs, or introduce kerning to compensate for immature T021 drawings.

Position numerals need stable recognition, but this study does not promote tabular figures or mono globally. Use them only if actual comparison evidence requires them.

## CRITIQUE
FAIL if typography causes action truncation that changes meaning, boundary-state labels become ambiguous, fallback materially detaches position from item identity, or geometry is frozen around provisional custom metrics.

## GATE
T021 remains upstream: widths/sidebearings frozen, kerning OFF, bounded drawing repair first; then general spacing; only residual pair-specific defects may enter kerning.

## HANDOFFS
L101 consumes actual rendered widths; W110 records requested/actual families; CD116 must not shorten semantic jobs for fit.

## OPEN
No T021 closure, exact production mono, custom-font production recommendation, browser/native/human recognition PASS.