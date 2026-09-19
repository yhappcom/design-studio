# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / I082 FOCUS OWNERSHIP + L086 OBSCURATION GEOMETRY**
Governance sync: 2026-09-19
Canonical paths: `research/layout/`, `research/interaction/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
I082 separates semantic object, rendered row, drag proxy, focused node, candidate and committed destination. L086 transfers that contract into baseline/200% focus, sticky/overlay, proxy, target and recovery geometry under WCAG 2.2 SC 2.4.11 while preserving I081 edge-autoscroll authority.

## Active queue
1. Implement/execute the non-drag single-pointer reorder path and compare with drag; keyboard does not substitute for WCAG 2.2 SC 2.5.7.
2. Execute I082 focus families across commit/cancel, source-offscreen rebuild, autoscroll, sticky content and 200% twice.
3. Record semantic IDs, focused semantic ID, source/proxy/focus/sticky boxes, scrollOffset(t), transaction/projection and explicit SC 2.5.8 PASS clause.
4. Preserve I063–I081 transaction/focus/Undo/IME/gesture/autoscroll invariants; persistence/sync remain dormant until implemented.
5. Extend to forced colors and independent engine; keep AT, physical-device, discoverability, context-loss, workload and representative-pilot evidence OPEN.

## Evidence boundary
No Stage 3 PASS, persisted/synced configuration, non-drag reorder, reorder-focus runtime PASS, independent-browser/native transfer, AT, physical-device or representative-human usability PASS is claimed.