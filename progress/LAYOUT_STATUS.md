# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / L085 EDGE-AUTOSCROLL GEOMETRY + I081 AUTHORITY**
Governance sync: 2026-09-19
Canonical paths: `research/layout/`, `research/interaction/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
I081 separates edge-zone membership, authored autoscroll, viewport displacement, semantic candidate and committed reorder transaction. L085 transfers this into baseline/200% edge-zone, sticky/safe-area, target/focus and reflow geometry. Viewport motion is not evidence of commit.

## Active queue
1. Implement/execute the non-drag single-pointer reorder path and compare with drag; keyboard does not substitute for WCAG 2.2 SC 2.5.7.
2. Execute top/bottom edge autoscroll→exit/drop, autoscroll→cancel, stationary-pointer moving rows, list-end saturation, active-drag 200% reflow, sticky/safe-area collision and non-drag equivalent twice.
3. Record semantic IDs, pointer coordinates, scrollOffset(t), edge/drag-boundary/target/focus boxes and explicit SC 2.5.8 PASS clause.
4. Preserve I063–I080 transaction/focus/Undo/IME/gesture invariants; persistence/sync remain dormant until implemented.
5. Extend to forced colors and independent engine; keep AT, physical-device, discoverability, overshoot, workload and representative-pilot evidence OPEN.

## Evidence boundary
No Stage 3 PASS, persisted/synced configuration, non-drag reorder, edge-autoscroll runtime PASS, independent-browser/native transfer, AT, physical-device or representative-human usability PASS is claimed.