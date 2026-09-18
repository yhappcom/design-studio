# C090 — Pointer reorder action-state separation

Status: Stage 3 PRACTICE / RUNTIME EVIDENCE OPEN

## Semantic axes
Keep these independent: current focus, selected object, drag-active state, single-pointer move availability, destination availability, no-op boundary, recovery eligibility, success/failure/superseded state, hidden/disabled state.

## Failure patterns
- drag-active color reused as keyboard focus;
- disabled Move Up/Down communicated only by reduced opacity;
- destination eligibility encoded only by hue;
- selected row appears to own focus when focus is on a move action;
- success/recovery paint remains after the transaction is superseded;
- forced-colors removes the only cue that distinguishes available and unavailable movement.

## Validation
For each I077 scenario record semantic state → token → paint owner → rendered surface → non-color cue → accessible meaning. Repeat light/dark if supported, 200%, forced-colors and an independent browser engine before transfer closure.

Color does not define transaction semantics or target geometry; it renders states supplied by Interaction/Layout/Content contracts.
