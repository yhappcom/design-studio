# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / L084 SCROLL-REORDER GEOMETRY + I080 GESTURE ARBITRATION**
Governance sync: 2026-09-19
Canonical paths: `research/layout/`, `research/interaction/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
I080 extends I079 from pointer-stream ownership into scroll-versus-reorder arbitration: pointer stream, UA pan owner, Flutter gesture-arena winner, reorder preview owner and transaction owner are separate. L084 measures scroll displacement, target/focus geometry and 200% reflow without inferring semantic ownership from motion.

## Active queue
1. Implement/execute the non-drag single-pointer reorder path and compare it with drag using I077–I080; keyboard does not substitute for SC 2.5.7.
2. Execute row-body scroll, affordance-start→scroll/arena-loss, valid reorder, pointercancel/UA suppression, stationary-pointer 200% reflow, boundary no-op and non-drag equivalent twice.
3. Execute L081–L084 at baseline/200% with semantic IDs, pointer coordinates, scroll offsets, gesture owner, preview/target/focus boxes, sticky/safe-area intersections and explicit SC 2.5.8 PASS clause.
4. Preserve I063–I076 transaction/focus/Undo/IME invariants; persistence/sync remain dormant until implemented.
5. Extend to forced colors and independent engine; keep AT, physical-device, discoverability, motor-error, workload and representative-pilot evidence OPEN.

## Evidence boundary
No Stage 3 PASS, persisted/synced configuration, non-drag reorder, scroll/reorder arbitration runtime PASS, independent-browser/native transfer, AT, physical-device or representative-human usability PASS is claimed.