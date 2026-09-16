# I033 — Delete/Update Tombstone Authority Contract

## PURPOSE
Stage-3 systems practice extending I032 partial-order merge to destructive concurrency. Deletion is not merely another field value: products may represent it as absence, a tombstone, retention state, or a reversible operation. The UI must not invent those backend semantics.

## AUTHORITY MODEL
For each object preserve `objectId`, branch/event IDs, authoritative revision/sequence or comparison token, delete operation ID, optional tombstone identity/retention evidence, restore operation ID, certainty and current existence verdict.

Comparison outcomes remain `A-before-B`, `B-before-A`, `same`, `concurrent-incomparable`, `ordering-unknown`. A delete/update pair that is concurrent must not be resolved by client clock, receive order, DOM/list position, or optimistic UI. Production deletion-wins/update-wins/merge/restore policy is a DEPENDENCY on the product/backend authority.

## ACTION ORACLE
Consequential actions require action-specific evidence. When existence or delete outcome is unknown, mutation that assumes existence or absence is blocked unless the product authority explicitly defines an idempotent/replay-safe operation. Restore is a new consequential operation, not a visual undo, unless the backend contract proves equivalence.

## DETERMINISTIC SCENARIOS
1. A edits offline while B deletes from same base; branches become incomparable.
2. Delete response is lost; recheck proves deleted.
3. Delete response is lost; recheck proves still live.
4. Late update arrives after authoritative tombstone; UI must follow declared authority policy, not arrival time.
5. Restore is requested, response lost, and authority changes again before reconciliation.
6. Retention/tombstone metadata is unavailable; UI must not promise recoverability.
7. Reload/deep-link/history reconstructs deleted object provenance without silently recreating it.

## FAILURE CONDITIONS
- visually removing an object is treated as proof of authoritative deletion;
- a late update resurrects an object without authority evidence;
- `undo` is offered when only a new restore mutation is possible;
- deletion conflict is collapsed into generic failure;
- destructive action remains enabled after evidence revision invalidates its prerequisites.

## RELATED DOMAIN CHECK
Type T021 remains provisional. C046 owns visual truth. L037 owns disappearance/recovery locality. W046 owns runtime provenance. CD052 owns existence/deletion/recovery language. Human comprehension and professional error rate remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Web must obtain actual persistence/tombstone/idempotency/retention semantics from engineering/product authority. Content must not promise restoration unless that contract exists. Color/Layout must not use disappearance or salience as authority evidence.

## EVIDENCE BOUNDARY
Deterministic interaction contract only; no production backend, native, AT, physical-device or human PASS.