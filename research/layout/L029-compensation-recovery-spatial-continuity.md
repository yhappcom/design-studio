# L029 — Compensation/recovery spatial continuity

Date: 2026-09-16
Evidence purpose: **SYSTEMS PRACTICE / TRANSFER CONTRACT**

## RELATED DOMAIN CHECK
I025 owns rollback/compensation semantics; C038 owns visual state; W038 owns browser execution; CD044 owns wording; Type metrics remain provisional until T021.

## Spatial problem
A reversal flow can be behaviorally correct yet spatially misleading if the explanation, affected object and safe recovery action separate during optimistic change, conflict, rollback, reflow or localization.

## Priority model
For a rollback/compensation state preserve the association:
`affected object → authoritative/current consequence → reversal/compensation status → safe next action → history/detail`.

The prior success message may remain in history but must not occupy stronger current-state hierarchy than the correction.

## Required geometry cases
- baseline desktop;
- 320 CSS px reflow;
- actual 200% zoom when executable;
- long/pseudo-localized explanation;
- sticky header/footer overlap;
- focused safe action;
- disabled unsafe retry adjacent to explanation;
- reduced visual viewport where executable.

Record rectangles for object identity, current state, correction explanation, safe action, unsafe action and sticky layers. Test reading/focus order separately from visual proximity.

## Failure conditions
- rollback message detaches from the object it corrects;
- stale success remains visually/spatially dominant;
- safe recovery moves outside the local correction region while unsafe retry remains prominent;
- focus moves to a control whose authority changed;
- reflow changes semantic reading order;
- sticky layers fully obscure the focused control.

## Evidence boundary
Geometry contract is not browser evidence. Actual 200% zoom is not inferred from a 320px viewport. Human noticeability/workload remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W038 records rectangles/run IDs; C038 evaluates cue precedence; CD044 preserves correction/consequence language; I025 supplies enabled/blocked truth; Type later supplies accepted metrics.