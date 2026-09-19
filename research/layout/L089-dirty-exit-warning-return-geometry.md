# L089 — Dirty Exit, Warning, and Return Geometry

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION

## RELATED DOMAIN CHECK
Uses I085 lifecycle authority, C097 semantic-state separation, T066 downstream strings, W097 served restoration provenance, and CD103 draft truth. No ownership is moved.

## PURPOSE
Transfer I085 into measurable spatial/focus behavior without treating browser lifecycle as a visual state.

## GEOMETRY CONTRACT
Measure separately: focused semantic object, focus rectangle, dirty indicator if product-owned, in-app warning surface if implemented, sticky header/footer, viewport, recovery control, and post-return target. Browser-native `beforeunload` dialog geometry is user-agent owned and must not be specified as product geometry.

## PRACTICE MATRIX
At baseline and 200%, twice per executable family:
- dirty edit → in-app leave → stay;
- dirty edit → discard/leave;
- browser Back → return;
- reload/new-document return;
- bfcache return;
- Undo/Reset dirty→clean → leave;
- source unavailable on return;
- non-drag reorder dirty state once implemented.

Record viewport, scroll offset, focus/source/sticky/recovery rectangles, obscuration, displacement, route/draft identity and projection hash.

## ACCESSIBILITY BASELINE
WCAG 2.2 remains baseline. Focus must remain visible/not fully obscured under applicable AA criteria; a focus-taking warning is not misclassified as a 4.1.3 status message. Browser-native confirmation is not restyled or spatially controlled by the product.

## FAILURE CONDITIONS
- focus restored to ordinal slot rather than semantic object;
- warning/dirty banner fully obscures focused control;
- 200% reflow removes the leave/stay/recovery action;
- browser dialog dimensions are treated as deterministic product layout;
- viewport restoration is treated as focus/draft restoration;
- geometry success is claimed without served runtime.

## HUMAN EVIDENCE BOUNDARY
Interruption cost, warning noticeability, spatial orientation and pilot workload remain OPEN.