# CD057 — Batch Partial-Outcome Recovery Language System

Evidence purpose: **STAGE 3 PRACTICE / CONTENT SYSTEM / TRANSFER VALIDATION**. Extends CD056 from one queued operation to mixed outcomes inside one batch.

## RELATED DOMAIN CHECK
- Type T021 remains provisional; preserve necessary strings and use mature fallback.
- C051 owns visual state encoding.
- I038 owns actual member outcome/retry truth; L042 owns hierarchy.
- W051 owns runtime/reconciliation evidence.

## Semantic model
Do not force a batch into binary success/failure when member outcomes differ or remain unknown.

Separate resources for concepts such as:
- `batchPending`
- `batchCompletedAllConfirmed`
- `batchMixedOutcome`
- `batchOutcomeUnknown`
- `memberConfirmed`
- `memberDenied`
- `memberFailedKnown`
- `memberOutcomeUnknown`
- `memberRetryAvailable`
- `memberRetryBlockedPendingRecheck`
- `batchRetryUnavailableMixedSafety`

## Language invariants
- Mixed outcome ≠ failure.
- Unknown outcome ≠ not applied.
- Known failure ≠ denied unless authorization is the cause.
- Retry available ≠ safe to replay the whole batch.
- Local cancellation ≠ backend rollback.
- `3 of 5 completed` must not imply the remaining two failed unless that is authoritative.

Prefer complete localized messages over fragment concatenation such as `{count} + succeeded + {count} + failed`; grammar, pluralization and semantic ordering vary by locale. Batch and member identifiers remain data parameters.

## Recovery wording
A recovery CTA names its actual scope: retry this item, recheck status, review denied item, or retry eligible items. Avoid generic `Retry all` unless I038/W051 establish whole-batch replay safety.

## Stress cases
Pseudo-expansion, plural/select forms, zero/one/many members, same object label repeated, long context names, locale change after dispatch, missing-resource fallback, narrow layout, history/export.

## Evidence boundary
No Flutter/TMS/ARB round trip, linguistic review, human comprehension/task evidence or Content Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W051 must provide actual member outcomes; I038 determines action truth; L042 tests hierarchy/wrapping; C051 tests non-color equivalence; Type receives unchanged strings only after T021 repair.