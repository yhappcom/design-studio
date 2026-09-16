# I014 — Recovery, Idempotency and Reconciliation Matrix

Evidence type: SYNTHESIS / CRITIQUE / TRANSFER VALIDATION / OPEN

## RELATED DOMAIN CHECK
L019 owns geometry; C028 owns visual/focus encoding; W025 owns request-boundary execution; CD032 owns wording. Type is not behavior authority. UX human trust evidence remains OPEN.

## Problem
I013 established that transport interruption is not equivalent to known failure. I014 extends that into a recovery decision matrix so UI actions cannot accidentally duplicate a professional record operation.

## Matrix
- Confirmed success: do not retry; expose resulting record/action.
- Confirmed failure before commit: retry may be offered if operation semantics permit it.
- Client abort/timeout with server outcome unknown: do not label failure; reconcile status before destructive/repeating action.
- Offline before request dispatch: preserve local intent/draft and explain unsent state; sending later is a new controlled transition.
- Reconnect after unknown outcome: query/reconcile first; retry only after absence/non-commit is established or the operation is explicitly idempotent.
- Conflict: compare/resolve authoritative and local versions; generic retry is not recovery.

## Implementation contract
Runtime evidence must record request ID/operation ID where available, dispatch status, response/abort event, server-observable outcome when available, semantic state chosen, and safe action exposed. The UI must not derive semantic truth from a browser exception string alone.

## Current result
**DECISION MATRIX PASS / BACKEND TRANSFER OPEN.** No actual backend idempotency guarantee is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W025 maps real Fetch outcomes to this matrix. CD032 may finalize conditional recovery wording only after classification. UX integration should audit duplicate-action risk separately from perceived trust.