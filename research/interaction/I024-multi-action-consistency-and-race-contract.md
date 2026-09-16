# I024 — Multi-action consistency and race contract

Date: 2026-09-16
Purpose: **SYSTEMS PRACTICE / ADVERSARIAL VALIDATION**

## RELATED DOMAIN CHECK
L028 owns spatial grouping/order; C037 visual precedence; W037 runtime race provenance; CD043 wording under changing authority; Type only rendering. I024 owns temporal/action truth.

## Extension of I023
I023 evaluates one action against required facts. I024 evaluates multiple actions on the same object while authority changes over time.

## Invariants
- Two actions may legitimately have different availability when their required facts differ.
- A newly arrived authority revision invalidates any decision derived from an older incompatible revision before dispatch.
- Pending mutation A must not silently authorize mutation B merely because the UI optimistically updated presentation.
- If action availability changes while keyboard/pointer focus remains on a control, the resulting state and safe next action must remain explicit.
- Reconciliation is correlated to operation/object IDs; late responses cannot overwrite a newer authoritative revision without conflict handling.

## Adversarial sequence
`rev1 → Action A enabled → dispatch A → optimistic presentation → rev2/conflict arrives → Action B evaluated → late A response → reconciliation`.
Record required-fact revisions, dispatch revision, current authoritative revision, enabled/blocked transitions, focused control, operation IDs and final stable state.

## Verdict
A PASS requires every dispatched action to have been authorized by the evidence revision current at dispatch, late responses to be ordered/correlated safely, and contradictory actions not to become enabled through presentation-only optimism.

## Evidence boundary
This is deterministic state-machine evidence, not human comprehension/workload evidence. Production retry/idempotency claims still require actual backend contracts.