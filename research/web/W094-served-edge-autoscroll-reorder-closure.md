# W094 — Served edge-autoscroll reorder closure

Status: STAGE 3 PRACTICE / RUNTIME TRANSFER SPEC
Date: 2026-09-19

## Closure target
Extend W093 beyond scroll-versus-reorder arbitration into authored edge-autoscroll after reorder has won, without adding another isolated Chromium micro-test.

## SOURCE
Flutter reorderable lists expose `autoScrollerVelocityScalar` and `dragBoundaryProvider`; this is framework capability only. WCAG 2.2 SC 2.5.7 still requires equivalent single-pointer non-drag operation for authored dragging.

## Promotion ladder
Actual LogMate implementation → production Web build → served primary engine → independent engine → 200% → forced-colors. Execute each available family twice before REPLICATION is claimed.

## Required manifest
Build SHA; route; browser/engine/OS; viewport/zoom; pointer type/id/coordinates; event order; scrollOffset(t); scroll-container/edge-zone/drag-boundary rectangles; effective reorder/autoscroll configuration where instrumentable; semantic object/candidate/committed destination IDs; transaction/branch/inverse; projection hash; focus owner; visible/a11y status; recovery eligibility; runtime exceptions.

## Families
Bottom/top edge autoscroll→exit→valid drop; autoscroll→cancel; stationary pointer with moving rows; list-end saturation; 200% active-drag reflow; sticky/safe-area collision; same semantic move via non-drag single-pointer path; Undo/Reset after committed move only.

## Acceptance
Viewport motion alone cannot establish commit. Cancellation cannot create mutation/recovery. Boundary saturation is not failure. Non-drag alternative remains independently operable and testable. Preserve I063–I080 transaction/focus/Undo/IME/gesture invariants.

## Performance evidence
Lighthouse/DevTools/CI synthetic remain LAB. LCP/INP/CLS become FIELD evidence only with provenance-bearing aggregate/RUM; no field claim is made here.

## RELATED DOMAIN CHECK
T063 receives string pressure without gate changes. C094 supplies state-separation acceptance. I081 supplies authority. L085 supplies geometry. CD100 supplies semantic messaging. W094 is the browser/product TRANSFER VALIDATION layer.

## OPEN
Actual product implementation, independent-engine result, physical touch/pen, screen reader, field CWV and representative-human evidence.