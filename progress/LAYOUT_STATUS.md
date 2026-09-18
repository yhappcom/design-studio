# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / L083 RECOMPOSITION GEOMETRY + I079 POINTER-STREAM OWNERSHIP**
Governance sync: 2026-09-19
Canonical paths: `research/layout/`, `research/interaction/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
I079 extends I078 from cancel/commit into pointer-stream ownership: capture/hit target/semantic drag owner/candidate/committed destination are separate, and capture never authorizes mutation. L083 adds stationary-pointer baseline/200% recomposition evidence so layout motion cannot be misread as user pointer intent.

## Active queue
1. Implement/execute the non-drag single-pointer reorder path and compare it with drag using I077–I079; keyboard does not substitute for SC 2.5.7.
2. Execute normal activation, drag abort/drop, pointercancel/stream suppression, capture/gesture release, stationary-pointer recomposition, row rebuild, boundary no-op and stale-owner families twice.
3. Execute L081–L083 at baseline/200% with semantic IDs, pointer coordinates, capture/gesture owner, preview/target/focus boxes, scroll, sticky/safe-area intersections and explicit SC 2.5.8 PASS clause.
4. Preserve I063–I076 transaction/focus/Undo/IME invariants; persistence/sync remain dormant until implemented.
5. Extend to forced colors and independent engine; keep AT, physical-device, discoverability, motor-error, workload and representative-pilot evidence OPEN.

## Evidence boundary
No Stage 3 PASS, persisted/synced configuration, non-drag reorder, pointer-capture/cancellation runtime PASS, independent-browser/native transfer, AT, physical-device or representative-human usability PASS is claimed.