# I032 — Concurrent Branch / Merge Authority Contract

## PURPOSE
`TRANSFER VALIDATION` of I031 where authoritative events form a partial order rather than a total sequence.

## ORDERING MODEL
For two events A and B, the system must distinguish `A-before-B`, `B-before-A`, `equal/same-revision`, `concurrent-incomparable`, and `ordering-unknown`. Wall-clock time, receive time, row position and locale-formatted strings are not sufficient to convert `concurrent-incomparable` into an order.

## ACTION ORACLE
Consequential actions require the facts relevant to that action to be authoritative after reconciliation. When branches are concurrent:
- branch-local read/inspection may remain available;
- mutation that assumes a global winner is blocked;
- explicit merge/reconciliation may be available only when backend/product rules authorize it;
- destructive conflict resolution requires branch identity, consequence and reversibility to be known;
- if merge outcome is unknown, do not auto-chain another corrective mutation.

Required scenarios: concurrent offline edits; one branch arrives later; duplicate/replay; merge succeeds; merge rejected; merge response lost; authority changes during merge; reload/deep-link after merge.

## RELATED DOMAIN CHECK
- Color: C045 owns visual truth, not merge semantics.
- Layout: L036 owns spatial branch/consequence continuity.
- Web: W045 must execute the runtime ordering oracle.
- Content: CD051 verbalizes comparability and merge consequence.
- Type: branch IDs must remain discriminable without provisional metrics becoming layout authority.

## HANDOFFS TO OTHER SPECIALISTS
Expose `comparisonVerdict`, `branchIds`, `mergeOperationId`, `authorityRevision`, `mergeOutcomeCertainty`, and allowed actions to W045/CD051/C045/L036.

## EVIDENCE BOUNDARY
Deterministic interaction contract only; no production persistence/idempotency/deduplication, native, AT, or human workflow PASS.