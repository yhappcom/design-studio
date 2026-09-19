# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / I083 SCROLL-FOCUS AUTHORITY + L087 GEOMETRY**
Governance sync: 2026-09-19
Canonical paths: `research/layout/`, `research/interaction/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
I083 separates semantic focus identity, browser visual anchor, application scroll restoration and reorder transaction. L087 transfers this into baseline/200% viewport, focus, sticky/overlay and layout-delta geometry while preserving I082 focus ownership and I081 autoscroll authority.

## Active queue
1. Implement/execute the non-drag single-pointer reorder path and compare with drag; keyboard does not substitute for WCAG 2.2 SC 2.5.7.
2. Execute I083 families across commit/cancel, status insertion, source-offscreen rebuild, Undo/Reset and 200% twice.
3. Record semantic focus ID, scrollOffset deltas, focus/source/sticky boxes, projection/transaction and distinguish browser/app/layout movement.
4. Preserve I063–I082 transaction/focus/Undo/IME/gesture/autoscroll invariants; persistence/sync remain dormant until implemented.
5. Extend to forced colors and independent engine; keep AT, physical-device, discoverability, context-loss, workload and representative-pilot evidence OPEN.

## Evidence boundary
No Stage 3 PASS, persisted/synced configuration, non-drag reorder, scroll-focus runtime PASS, independent-browser/native transfer, AT, physical-device or representative-human usability PASS is claimed.