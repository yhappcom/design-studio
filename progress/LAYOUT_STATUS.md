# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / L081 POINTER TARGET GEOMETRY + I077 POINTER REORDER EQUIVALENCE**
Governance sync: 2026-09-19
Canonical paths: `research/layout/`, `research/interaction/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
I077 turns the previously listed non-drag reorder blocker into an explicit equivalence contract under WCAG 2.2 SC 2.5.7: drag and single-pointer alternatives may differ mechanically but must resolve the same semantic object/destination transaction. L081 adds SC 2.5.8 clause-aware target geometry plus baseline/200% reflow, obscuration and displacement validation.

## Active queue
1. Implement/execute a non-drag single-pointer reorder path and compare it with drag using I077; keyboard does not substitute for SC 2.5.7.
2. Execute adjacent/multi-position/boundary/system-group/repeated move/Undo/Reset families twice per path.
3. Execute L081 at baseline/200% with semantic IDs, target/focus boxes, scroll offsets, sticky/safe-area intersections and explicit SC 2.5.8 PASS clause.
4. Preserve I063–I076 transaction/focus/Undo/IME invariants while adding pointer equivalence; persistence/sync remain dormant until implemented.
5. Extend to forced colors and independent engine; keep AT, physical-device, discoverability, workload and representative-pilot evidence OPEN.

## Evidence boundary
No Stage 3 PASS, persisted/synced configuration, non-drag reorder runtime PASS, independent-browser/native transfer, AT, physical-device or representative-human usability PASS is claimed.