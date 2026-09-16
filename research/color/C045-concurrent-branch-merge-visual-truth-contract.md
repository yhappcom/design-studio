# C045 — Concurrent Branch / Merge Visual Truth Contract

## PURPOSE
`TRANSFER VALIDATION` from C044 causal order into non-total-order systems. Two valid concurrent branches may be incomparable; visual hierarchy must not invent a winner before authoritative merge/reconciliation.

## SYSTEM CONTRACT
Visual precedence is: current authoritative consequence > action safety > merge/reconciliation state > branch provenance > wall-clock/display recency > focus/selection/brand emphasis.

Required semantic states: `single-authority`, `concurrent-incomparable`, `merge-pending`, `merge-conflict`, `merged-confirmed`, `branch-superseded`, `authority-unavailable`. `concurrent-incomparable` must not reuse success/current styling merely because one branch has a later displayed timestamp.

## ADVERSARIAL MATRIX
Test two concurrent branches under: later client clock on A; later receive time on B; equal formatted time; selected A row; focused B action; one branch color removed; grayscale; forced-colors; print/export; dark/light theme. PASS requires branch distinction and unresolved merge truth to survive without hue alone.

A merge-confirmed surface may inherit current-authority emphasis only after authoritative merge evidence exists. Selection/focus remains interaction state, never causal priority.

## RELATED DOMAIN CHECK
- Type: branch/event IDs remain operational strings; custom metrics provisional.
- Interaction/Layout: I032/L036 own comparability, safe actions and branch geometry.
- Web: W045 must expose actual branch/merge runtime provenance.
- Content: CD051 must say concurrent/merged/conflicted without fabricating chronological superiority.
- UX: perceived salience/comprehension remains human evidence OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W045 should capture computed styles for both branches and merged/current surfaces. L036 must keep branch provenance adjacent to consequence. CD051 supplies non-color semantics.

## EVIDENCE BOUNDARY
Deterministic visual contract only. No executed artifact, observer, CVD/low-vision, physical display/print, or human task PASS.