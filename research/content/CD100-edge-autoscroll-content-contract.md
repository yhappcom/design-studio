# CD100 — Edge-autoscroll content contract

Status: STAGE 3 PRACTICE / COMPLETE-SYSTEM TRANSFER
Date: 2026-09-19

## Semantic contract
User-facing content resolves from semantic action/result, not viewport mechanics. Protect: `autoscrolled != moved`; `candidate changed during scroll != committed`; `scroll boundary reached != failure`; `cancel after autoscroll != failed reorder`; `committed reorder != Saved/Synced`; `moved object != focused object`.

## PRACTICE
Extend the complete content system across reorder alternative, drag preview, autoscroll, cancellation, boundary no-op, commit, Undo and Reset. Source payload: semantic object ID/name, requested action, candidate only when user-relevant, committed destination/result, transaction/recovery eligibility, current focus and persistence truth. Do not source success from edge-zone entry or scroll displacement.

For EN/KO transfer, preserve meaning before brevity. Compare concise visible feedback with richer accessibility payload under baseline/200% layouts; do not freeze literal Korean until runtime fit and linguistic review exist.

## CRITIQUE
FAIL if clean autoscroll cancellation produces an error; reaching the list end sounds like system failure; movement is announced before commit; wording implies persistence; or strings are shortened solely to preserve preferred geometry.

## RELATED DOMAIN CHECK
Type T062 owns rendering. Color C093/C094 owns visual semantic separation. Interaction I081 owns action/result truth. Layout L085 owns spatial fit. Web W093/W094 owns served integration. This extends CD099 from arbitration into post-arbitration authored autoscroll.

## OPEN
Actual EN/KO runtime, linguistic review, screen-reader comprehension and representative-pilot task evidence.