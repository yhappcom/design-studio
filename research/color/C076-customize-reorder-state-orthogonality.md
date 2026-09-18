# C076 — Customize reorder state orthogonality

## Purpose
CONTRADICTION REVIEW + TRANSFER VALIDATION of C075 when non-drag reorder controls are added to LogMate Customize.

## RELATED DOMAIN CHECK
Type T044/T045 protects professional labels from density-driven compression. L066/I062 own spatial order and equivalent operation. W075 owns browser transfer. CD081 owns semantic field identity and action language.

## SOURCE
WCAG 2.2 SC 2.5.7 requires a non-drag single-pointer alternative for non-essential dragging. SC 2.5.8 requires pointer targets to meet the 24×24 CSS-pixel minimum or an enumerated exception. These criteria make the alternative controls real interactive states, not decorative affordances.

## PRACTICE — orthogonal state matrix
Validate these axes independently:
- visibility: SHOWN / HIDDEN;
- interaction: idle / focus / pressed / disabled;
- reorder: movable-earlier / movable-later / boundary-disabled / insertion destination;
- operation mode: drag / non-drag / keyboard;
- theme/environment: light / night / forced colors.

A field can be SHOWN + focused + boundary-disabled-for-earlier while still movable later. No single color token may collapse these meanings.

## CRITIQUE
Potential failure: using one accent hue both for SHOWN and the current reorder destination. Another failure: lowering opacity for a boundary-disabled arrow until it becomes indistinguishable from hidden/de-emphasized content. Color success requires semantic token → paint owner → visible surface → non-color cue → accessible meaning.

## REPRODUCIBLE VALIDATION CONTRACT
For each scenario ID capture computed/used state where available, rendered screenshot, focus indicator, text/icon/state redundancy, and target geometry. Repeat in forced-colors and an independent browser engine before claiming browser breadth. Token inspection alone is NOT PASS.

## OPEN
No forced-colors, independent-engine, calibrated-display, observer or representative-human PASS is claimed. Stage 3 remains PRACTICE.

## HANDOFFS TO OTHER SPECIALISTS
Interaction should expose boundary-disabled versus globally-disabled semantics. Content should not verbalize state through color references. Web should preserve scenario identity across theme/forced-color runs.