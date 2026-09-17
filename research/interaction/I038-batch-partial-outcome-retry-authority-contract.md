# I038 — Batch Partial-Outcome Retry Authority Contract

Evidence purpose: **STAGE 3 PRACTICE / SYSTEMS CONTRACT / TRANSFER VALIDATION**. Extends I037 from one context-bound operation to multi-operation batches with partial acknowledgement.

## RELATED DOMAIN CHECK
- **Type:** mature fallback required for member IDs/counts while T021 R1 is open.
- **Color:** C051 prevents aggregate styling from replacing member truth.
- **Layout:** L042 preserves batch/member hierarchy and recovery path.
- **Web:** W051 executes acknowledgement loss, partial completion and replay hazards.
- **Content:** CD057 names aggregate versus member outcomes without semantic collapse.

## Authority model
A batch is a transport/workflow grouping, not proof of atomicity. Unless the production contract explicitly guarantees atomic commit, every consequential member retains its own:
`operationId | originContext | object | precondition | authorization | dispatch state | authoritative outcome | retry eligibility`.

## Interaction invariants
1. Never infer all-member success from one batch-level 2xx/progress completion without an authoritative member result contract.
2. `outcomeUnknown` is not failure and must not be blindly replayed.
3. Retry targets only members whose retry safety is established by production idempotency/reconciliation semantics.
4. A denied member must not be retried merely because sibling members are retryable.
5. Batch cancellation after dispatch is not backend rollback unless reversal is authoritative.
6. A second attempt must preserve original member identity or explicit supersession linkage.

## Deterministic scenarios
- members A/B/C: A confirmed, B denied, C response lost;
- batch response lost after A/B committed;
- reconnect reconstructs mixed state from authority;
- user selects Retry failed: C remains blocked until reconciled;
- locale/context switch occurs while mixed outcome persists;
- reload/deep-link/history/export retains per-member provenance.

## Action oracle
`retryMember` requires known member identity + current authority + retry eligibility + relevant authorization/precondition. `retryBatch` is disabled unless the production contract proves replay safety for every included member.

## Evidence boundary
No production atomicity/idempotency guarantee, executed runtime PASS, human error-rate reduction or Interaction Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
C051 consumes member certainty; L042 must expose exceptions without destructive reorder; W051 must test response-loss/reconciliation; CD057 must not call mixed outcome simply success or failure.