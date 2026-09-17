# W051 — Batch Partial-Acknowledgement Reconciliation Runtime Contract

Evidence purpose: **STAGE 3 PRACTICE / RUNTIME CLOSURE TARGET / TRANSFER VALIDATION**. Extends W050 from one persisted deferred mutation to a batch with member-level partial outcomes.

## RELATED DOMAIN CHECK
- **Type:** T021 remains provisional; mature fallback only.
- **Color:** C051 defines aggregate/member visual truth.
- **Layout/Interaction:** I038 defines retry authority; L042 defines mixed-outcome hierarchy/focus continuity.
- **Content:** CD057 defines aggregate/member language and localization invariants.
- **UX:** deterministic runtime evidence remains distinct from human comprehension/task evidence.

## Runtime invariant
Unless the production API explicitly guarantees atomicity, preserve member-level provenance and outcome. A transport batch identifier does not replace operation identity.

Recommended evidence shape:
`batchId | operationId | principalId | originContextId | objectId | precondition/policy revision | dispatchAttemptId | request digest | authoritative result/revision | reconciliation result | retry eligibility`.

## Closure scenario
Execute one trace where possible:
1. Create batch B with q1/q2/q3 under a verified context.
2. Dispatch while instrumenting member identities.
3. Force q1 confirmed, q2 denied/known failure, q3 acknowledgement lost or response ambiguous.
4. Render `batchMixedOutcome`; do not map q3 to failure.
5. Attempt `Retry failed`; prove q3 is reconciled/blocked until retry safety is known.
6. Inject whole-batch response loss after at least one member commits.
7. Reload and reconstruct member outcomes from authority rather than local progress.
8. Exercise context switch, locale change, 200% text, forced colors and narrow reflow.
9. Deep-link/history/export and prove batch/member provenance survives.
10. If production supports atomic batches, run a separate atomic-contract variant rather than generalizing non-atomic assumptions.

## Required artifacts
Browser/engine/version, commit SHA, runId, batchId, operation IDs, context/object IDs, request/response/reconciliation trace, persistence records, DOM/AX-relevant state, focus, computed styles, viewport geometry, locale/resource revision and artifact hashes.

## Retry and security boundary
Client replay convenience is not idempotency. Authorization and preconditions are revalidated for each consequential retry according to production policy. Unknown idempotency/atomicity means safe reconciliation/blocking, not invented replay semantics.

## Browser/performance boundary
Chromium plus an independent engine are required for cross-browser claims; Safari requires Safari execution. Batch/retry timings are lab/functional diagnostics. Field LCP/INP/CLS require actual RUM population/context.

## Evidence boundary
No W051 runtime PASS, production batch atomicity/idempotency, Web Stage 3 PASS, cross-browser, AT, physical-device, field Core Web Vitals or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Use shared `runId/batchId/operationId/contextId/objectId/artifactId` across C051, I038/L042 and CD057.