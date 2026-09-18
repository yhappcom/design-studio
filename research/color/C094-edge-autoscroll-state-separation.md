# C094 — Edge-autoscroll state separation

Status: STAGE 3 PRACTICE / SYSTEMS TRANSFER
Date: 2026-09-19

## Problem
Autoscroll adds visible motion without necessarily adding a new semantic result. Color must not convert motion into false transaction truth.

## STATE MODEL
Keep focus, selection, drag preview, edge-autoscroll active, candidate destination, valid/invalid destination, committed move, cancellation, boundary saturation, recovery and failure/superseded independent. Autoscroll-active is not success and does not inherit committed/recovery paint.

## PRACTICE
Apply the model to I081/L085 families in light, night and forced-colors. Check non-color cues for candidate, commit, cancellation and disabled/non-drag controls. At 200%, verify state cues remain attached to the correct semantic object after rows move beneath the pointer.

## CRITIQUE
FAIL if autoscroll motion gains success color before commit; boundary saturation looks like error; preview impersonates keyboard focus/selection; forced-colors removes the only distinction between eligible action and committed result; or stale paint remains after cancel.

## RELATED DOMAIN CHECK
Type T062: no metric compensation. Interaction I081 supplies lifecycle truth. Layout L085 supplies moving geometry. Web W093 supplies runtime/forced-colors evidence. Content CD099 supplies verbal meaning. This is TRANSFER VALIDATION, not a new interaction state machine.

## OPEN
Rendered LogMate evidence, independent engine, calibrated display, observer and human recognition evidence.