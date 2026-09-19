# C100 — Error-Prevention and Recovery State Separation

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION from I087/L091

## RELATED DOMAIN CHECK
I087 defines mutation/reversal semantics; L091 defines geometry; CD106 defines consequence/recovery language; T069 owns text rendering; W100 owns browser/runtime transfer. Color reinforces states without redefining them.

## STATE CONTRACT
Keep `dirty/editing`, `invalid`, `review-ready`, `destructive consequence`, `committed`, `undo available`, `undo pending`, `undo failed`, `restored`, and `Saved/Synced` distinct. A destructive action is not an error merely because it is destructive; a successful local inverse is not Saved/Synced; warning color does not substitute for consequence text.

## PRACTICE / CRITIQUE
Transfer the I087 families through light/night/forced-colors: reversible preference change, flight-record deletion, imported-data replacement, Reset, invalid edit, commit, Undo success/failure. FAIL if warning/error/success tokens collapse materially different states; disabled/destructive/cancel become indistinguishable; color alone identifies the destructive choice; stale success survives failed Undo; or forced colors erase focus/action identity.

## REPRODUCIBLE VALIDATION
Rendered product evidence must preserve semantic state under baseline/200%, forced colors and an independent engine with identical scenario IDs. Numerical contrast/token checks alone are not Stage 3 closure, human salience, comprehension, trust or error-rate evidence.

## HANDOFFS TO OTHER SPECIALISTS
CD106 must verbalize meaning without color references. L091 must preserve action/focus geometry when visual emphasis changes. W100 records computed/used rendering evidence. Type T069 must not alter provisional glyph metrics to rescue warning/recovery fit.