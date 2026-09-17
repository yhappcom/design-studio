# L042 — Batch Partial-Outcome Recovery Hierarchy Contract

Evidence purpose: **STAGE 3 PRACTICE / SPATIAL TRANSFER VALIDATION**. Pairs with I038.

## RELATED DOMAIN CHECK
- Type T021 is provisional; do not freeze layout around provisional custom metrics.
- C051 supplies cue precedence for mixed outcomes.
- I038 supplies member-level action/retry truth.
- W051 supplies runtime/reflow artifacts.
- CD057 supplies complete member and aggregate messages.

## Spatial problem
Dense batch UIs tend to privilege the aggregate banner and compress member exceptions. That can make a mixed consequential result look globally successful or globally failed.

## Required information spine
Preserve, through wide/narrow/reflow/200% text:
1. batch identity and aggregate summary;
2. explicit mixed/unknown certainty when applicable;
3. member identity;
4. member authoritative outcome;
5. member recovery/recheck action;
6. provenance/history.

Aggregate summary may collapse visually only if consequential exceptions remain reachable without relying on color or row position.

## Reflow and focus
- Reflow may stack members but may not move unknown/denied members into a visually subordinate region that implies completion.
- Filtering to failures must disclose that confirmed/unknown members are omitted from the current view.
- When a member becomes non-retryable during reconciliation, focus moves to a logical nearby status/recheck target rather than silently jumping to another member's Retry.
- Selection is view state, not authority or retry eligibility.

## Static transfer
Print/export must preserve batch identity, member identity, mixed outcome, omitted-member indication and generation provenance. Page breaks may not detach a member's status from its identity/recovery explanation.

## Evidence boundary
No rendered geometry, assistive-technology, physical-device/print, human scanning/workload or Layout Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W051 should capture viewport/focus geometry; C051 stress-tests cue loss; CD057 must provide labels that survive reflow; Type remains mature-fallback-only.