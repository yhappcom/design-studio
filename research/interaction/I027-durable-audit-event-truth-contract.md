# I027 — Durable Audit Event Truth Contract

Evidence purpose: **SYSTEMS PRACTICE**.

## RELATED DOMAIN CHECK
C040 visualizes but does not define audit truth; L030 currently owns terminal escalation locality; W039 provides runtime provenance; CD045 owns terminal language; Type remains provisional.

## Problem
I026 safely terminates automatic correction. A professional workflow still fails if later retrieval cannot reconstruct what happened. Transient UI state is not an audit model.

## Event contract
Each durable event must retain: `objectId`, `correctionChainId`, `operationId`, event type, observed/authoritative revision when known, certainty at event time, consequence, actor/source where product truth supports it, timestamp semantics, and relationship to superseding/reconciling events.

Events are append-oriented evidence. Later reconciliation may supersede interpretation but must not silently rewrite an earlier `outcomeUnknown` observation into a fictional historical `failed` or `confirmed` event.

Minimum sequence test: original mutation → conflict → compensation dispatch → response loss/outcome unknown → reconciliation → authority change → automatic termination → intervention required → later manual resolution. Reload/deep-link/history retrieval must reconstruct the chain without depending on transient component state.

## Safety rules
- UI dismissal does not delete product history.
- Retry/compensation creates a new operation identity; it does not overwrite the prior event.
- Unknown actor/source remains unknown.
- Client timestamps do not become server commit timestamps.
- History availability failure is distinct from no-history.

## Gate
Deterministic contract ready; production persistence/backend provenance and human comprehension remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
L031 must keep current consequence distinct from chronology; CD046 should label event certainty without rewriting history; C040 tests visual survival; W040 should execute reload/deep-link reconstruction.