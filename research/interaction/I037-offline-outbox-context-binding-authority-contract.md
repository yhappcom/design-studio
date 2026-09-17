# I037 — Offline Outbox Context-Binding Authority Contract

Evidence purpose: **PRACTICE / TRANSFER VALIDATION**. Extends I036 from context switching of visible state to deferred consequential operations created offline or during transport interruption.

## RELATED DOMAIN CHECK
- **Type:** mature fallback remains required while T021 drawing is open.
- **Color:** C050 must not visually imply dispatch authority from queue status or current-context color.
- **Layout:** L041 preserves origin/current context and safe actions under reflow.
- **Web:** W050 owns queue persistence, reconnect, request and response provenance.
- **Content:** CD056 names suspension, recheck, denial and ambiguous outcome without collapsing them.
- **UX:** human queue comprehension/error-rate evidence remains OPEN.

## Authority invariant
A queued consequential operation is bound to the authority context under which it was authored. `principal + originContext + objectIdentity + operation + policy/precondition + operationId` travel as one evidence bundle. A later UI context switch does not rewrite that bundle.

Before dispatch, the system must re-establish authoritative current eligibility for the **origin context** or require explicit, product-authorized rebinding semantics. Merely being authenticated in another context, having the same object ID, or having a current permission grant is insufficient.

## Deterministic state model
- `queuedOriginConfirmed`
- `queuedOriginStale`
- `contextMismatchSuspended`
- `dispatchAuthorityUnknown`
- `dispatchRecheckRequired`
- `dispatchDenied`
- `dispatchInFlight`
- `dispatchOutcomeUnknown`
- `dispatchConfirmed`
- `cancelledBeforeDispatch`

`contextMismatchSuspended` is not failure. `dispatchOutcomeUnknown` is not safe to retry unless idempotency/reconciliation evidence permits it.

## Adversarial scenarios
1. Enqueue A/object-17 offline → switch B → reconnect. Must not dispatch as B.
2. Same object-17 exists in B. Identity collision must not rebind the operation.
3. A permission revoked while offline. Recheck must deny/suspend before dispatch.
4. Rapid A→B→A with delayed switch responses. Queue origin remains A independent of UI ordering.
5. Dispatch request sent under A, response lost, user switches B. B UI must preserve ambiguous A outcome and safe reconciliation path.
6. User cancels queued A work while B current. Cancellation semantics affect the local queue item only unless backend cancellation is separately authoritative.

## Action enablement
Consequential dispatch is enabled only when origin context identity, object identity, operation preconditions and current authorization are authoritative. Unknown evidence blocks dispatch safely.

## Evidence boundary
This contract does not define backend queue technology, tenant policy, idempotency mechanism or cross-context transfer policy. Those are production dependencies.

## HANDOFFS TO OTHER SPECIALISTS
W050 must preserve origin/current context IDs and operationId across persistence/reload. C050 and CD056 consume the exact states. L041 keeps origin evidence adjacent to queue action under narrow/reflow conditions.