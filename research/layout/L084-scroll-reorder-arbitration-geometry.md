# L084 — Scroll/reorder arbitration geometry

Status: STAGE 3 PRACTICE / TRANSFER SPEC
Date: 2026-09-19

## Purpose
Geometry evidence for I080. Semantic gesture ownership is determined by Interaction/Web runtime evidence first; layout may not infer ownership from motion.

## Measurement protocol
At baseline and 200%, capture row, reorder affordance, scroll container, candidate destination, focus target and sticky/safe-area rectangles plus scroll offset before/down/move/cancel-or-commit/after. Repeat each family twice.

Families: scroll from row body; affordance start then scroll/arena loss; valid reorder; pointercancel; stationary touch during 200% recomposition; boundary no-op; non-drag Move alternative.

## Acceptance
- Scroll-only path changes scroll offset but not projection hash or recovery eligibility.
- Cancel/arena-loss clears preview without unexplained layout residue.
- Valid reorder preserves semantic destination even when row heights differ.
- 200% wrapping/reflow cannot convert layout motion into destination intent.
- Sticky headers/bottom bars must not obscure the active focus/target or hide the non-drag alternative.
- Record the exact WCAG 2.2 SC 2.5.8 clause used for target-size PASS; do not infer PASS from visual comfort.

## Critique axes
Context displacement, accidental gesture capture, target overlap, scroll trapping, clipped controls, sticky obstruction, safe-area collision, excessive auto-scroll, and mismatch between semantic neighbor and geometric neighbor.

## Evidence boundary
No runtime, physical-device or human usability PASS is claimed. L084 is downstream of I080 semantic ownership and upstream of Color/Web transfer evidence.