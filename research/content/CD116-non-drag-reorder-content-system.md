# CD116 — Non-drag reorder content system

## PURPOSE
Define the semantic/content contract for I097's non-drag reorder paths without turning wording into product logic.

## RELATED DOMAIN CHECK
T079 rendering, C110 state salience, I097 authority, L101 geometry and W109 runtime truth checked.

## CONTENT MODEL
Canonical jobs:
- object: field/item being moved;
- current position when useful;
- action: Move up / Move down / Move to position;
- destination/position;
- result: moved to position N;
- persistence state only when implementation supports it;
- recovery: Undo where a reliable inverse exists;
- boundary state: unavailable action should be structurally unavailable, not explained as an error.

`moved visually ≠ saved ≠ synced`.

## PRACTICE
Fixture strings:
- Move up
- Move down
- Move to position…
- Position 3 of 7
- Moved “Block time” to position 3 of 7.
- Order not saved. Retry.
- Order restored.

The exact production strings remain candidates until implemented context exists. Routine move results should be available as status information without demanding acknowledgement solely to be noticed.

## CRITIQUE
Reject:
- generic `Move` when direction/destination is hidden;
- `Saved` after only local visual reorder;
- instructions that mention drag as the only method;
- color/directional-location-only wording such as `move to the green area`;
- abbreviating necessary action/consequence semantics solely to preserve geometry;
- announcing every intermediate animation rather than meaningful result/state.

## LOCALIZATION / SOURCE BOUNDARY
LogMate product-authored UI remains English-only in current project scope. Architecture remains localization-ready; field/source/user text may contain Unicode and must not be rewritten to fit controls.

## HUMAN-EVIDENCE BOUNDARY
No claim is made that users discover or prefer stepwise versus destination controls, or that these strings optimize comprehension/workload. Those require observed human evidence.

## HANDOFFS
T079 stress-tests actual strings; L101 must allocate geometry without semantic shortening; C110 reinforces but does not replace language; W110 compares visible and accessibility payload; I097 owns actual state/action/recovery.