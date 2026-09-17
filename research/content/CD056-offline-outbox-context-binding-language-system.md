# CD056 — Offline Outbox Context-Binding Language System

Evidence purpose: **STAGE 3 PRACTICE / SEMANTIC TRANSFER VALIDATION**. Extends CD055 from context switching of visible data into deferred operations authored in another context.

## RELATED DOMAIN CHECK
- **Type:** complete queue/context strings remain unchanged; mature fallback until T021 gates pass.
- **Color:** C050 cannot carry queue ownership by color alone.
- **Layout/Interaction:** I037 owns dispatch truth; L041 owns origin/current-context hierarchy.
- **Web:** W050 owns persistence/request/reconciliation evidence.
- **UX:** human comprehension and trust remain OPEN.

## Semantic state inventory
Do not collapse these resources:
- `operationQueuedForContext`
- `operationQueuedOffline`
- `operationFromPriorContext`
- `dispatchSuspendedContextMismatch`
- `dispatchRecheckRequired`
- `dispatchAuthorityUnavailable`
- `dispatchNotAuthorized`
- `dispatchInProgress`
- `dispatchOutcomeUnknown`
- `dispatchConfirmed`
- `queuedOperationCancelledLocally`

`Suspended` is not `Failed`; `authority unavailable` is not `not authorized`; `outcome unknown` is not `not applied`; local queue cancellation is not backend reversal.

## Message model
Parameterized messages must bind the operation to its origin context without fragment concatenation. Context names are data parameters, not translatable nouns. The current workspace may be named separately when mismatch is relevant.

Examples of semantic intent, not production copy:
- operation belongs to `{originContextName}`;
- current workspace is `{currentContextName}`;
- reconnect/recheck is required before sending;
- sending result is unknown; verify the original workspace before retrying.

## Localization invariants
Across pseudo-expansion, Korean/English order changes, missing-resource fallback and locale change:
1. origin vs current context roles remain explicit;
2. no translation upgrades unknown/suspended into failed/denied;
3. no translation implies cross-context transfer unless product authority explicitly supports it;
4. object ID and operation ID remain data parameters with stable semantics;
5. history/export wording retains which context authored and which context was current at observation.

## Retrieval and tone
Queue/history surfaces should prioritize consequence and safe next action over implementation jargon such as “outbox”. Technical identifiers may appear as secondary audit detail. Tone remains neutral and operational; context mismatch is not blamed on the user.

## Evidence boundary
Static semantic contracts are not Flutter/TMS/ARB round-trip evidence, linguistic review, AT evidence or human comprehension evidence.

## HANDOFFS TO OTHER SPECIALISTS
W050 should materialize these states through the production localization path. L041 must allow complete parameterized wording. C050 verifies non-color survival. I037 remains the source of action truth.