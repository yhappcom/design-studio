# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / L082 POINTER-CANCELLATION GEOMETRY + I078 COMMIT BOUNDARY**
Governance sync: 2026-09-19
Canonical paths: `research/layout/`, `research/interaction/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
I078 adds WCAG 2.2 SC 2.5.2 pointer-cancellation/commit semantics to I077: press/preview must not silently become a committed reorder, ordinary controls prefer up-event/platform activation, and drag requires an abort/undo path. L082 adds baseline/200% preview-abort-commit geometry without allowing animation to redefine semantic truth.

## Active queue
1. Implement/execute the non-drag single-pointer reorder path and compare it with drag using I077–I078; keyboard does not substitute for SC 2.5.7.
2. Execute down-inside→up-outside, normal activation, drag-abort, valid-drop, pointer-cancel/gesture-loss, boundary no-op, Undo/Reset families twice.
3. Execute L081–L082 at baseline/200% with semantic IDs, preview/target/focus boxes, scroll offsets, sticky/safe-area intersections and explicit SC 2.5.8 PASS clause.
4. Preserve I063–I076 transaction/focus/Undo/IME invariants; persistence/sync remain dormant until implemented.
5. Extend to forced colors and independent engine; keep AT, physical-device, discoverability, motor-error, workload and representative-pilot evidence OPEN.

## Evidence boundary
No Stage 3 PASS, persisted/synced configuration, non-drag reorder or pointer-cancellation runtime PASS, independent-browser/native transfer, AT, physical-device or representative-human usability PASS is claimed.