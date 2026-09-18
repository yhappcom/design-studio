# W093 — Served scroll/reorder arbitration runtime closure

Status: STAGE 3 PRACTICE / RUNTIME TRANSFER SPEC
Date: 2026-09-19

## Closure target
Replace isolated gesture micro-tests with one product-transfer manifest for I077–I080 and L081–L084.

## Promotion ladder
Actual LogMate implementation → production Web build → served primary engine → independent engine → 200% → forced-colors. Each scenario family requires two executions before REPLICATION is claimed.

## Required provenance
Build SHA; route; browser/engine/OS; viewport/zoom; pointer type/id; pointer event order; scroll offsets; effective `touch-action`/direct-manipulation policy where observable; Flutter recognizer/gesture-arena outcome where instrumented; semantic object/action/destination IDs; transaction/branch/inverse; projection hash; focus owner; visible/a11y status; recovery eligibility; target/focus/scroll-container rectangles; runtime exceptions.

## Families
Row-body native/Flutter scroll; reorder-affordance start then scroll/arena loss; valid drag reorder; pointercancel/UA suppression; stationary pointer + 200% reflow; boundary no-op; non-drag single-pointer equivalent; Undo/Reset after committed move.

## Acceptance
Browser scrolling and authored reorder must not both commit from one ambiguous stream. `pointercancel`/arena loss cannot create transaction or recovery. Non-drag single-pointer operation remains independently testable for WCAG 2.2 SC 2.5.7. Record SC 2.5.8 target-size PASS clause explicitly.

## Performance evidence
Lighthouse, DevTools and CI synthetic measurements remain LAB evidence. LCP/INP/CLS are FIELD evidence only when provenance-bearing field/RUM aggregate data exists; no such field claim is made here.

## Evidence boundary
Framework/source feasibility is not browser/product PASS. Independent-engine, physical touch/pen, AT, human discoverability/workload and representative-pilot evidence remain OPEN until executed.