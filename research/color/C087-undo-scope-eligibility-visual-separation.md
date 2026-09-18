# C087 — Undo-scope eligibility visual separation

## PURPOSE
TRANSFER VALIDATION of I074/L078 into semantic color systems.

## RELATED DOMAIN CHECK
I074 resolves scope before inverse eligibility; L078 tests spatial ownership; CD092 protects eligibility language; W086 requires runtime provenance; T055 prevents Type compensation.

## SYNTHESIS
`scope ownership`, `eligible recovery`, `current focus`, `restoration`, `selection`, `failure`, `no-op`, and `superseded` are independent state axes. Color may reinforce them only after semantic resolution.

## PRACTICE
Construct state matrix for: text editor owns Cmd/Ctrl+Z while Customize has visible button recovery; Customize owns shortcut; configuration recovery superseded; recovery disabled; recovery invoked successfully; focus in competing region. Test light/night and later forced-colors.

## CRITIQUE
FAIL when a non-owning/stale recovery retains actionable-success paint, when focus and recovery ownership collapse into one accent, or when color is the only cue distinguishing two simultaneously plausible Undo scopes.

## REPRODUCIBLE VALIDATION
For each rendered state capture `scope_id`, eligibility, token, paint owner, visible surface, non-color cue and accessibility meaning. Forced-colors and independent-engine evidence remain OPEN until executable runtime exists.

## HUMAN BOUNDARY
No claim that users perceive or understand scope from color is made without observer/task evidence.

## HANDOFFS TO OTHER SPECIALISTS
Layout supplies owning-region geometry; Content supplies semantic qualification; Web must verify computed/used browser behavior; Type must preserve required labels without premature metric changes.
