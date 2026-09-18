# L076 — Intervening-Action Undo Locus and Displacement

Date: 2026-09-18
Stage: Stage 3 PRACTICE
Purpose: TRANSFER VALIDATION of I072 into spatial evidence.

## RELATED DOMAIN CHECK
I072 owns causal focus destination. C084 separates restoration/focus paint. T053 prevents typographic compensation for density. W084 owns browser evidence. CD090 separates restoration truth from focus language.

## SOURCE
WCAG 2.2 SC 2.4.11 Focus Not Obscured (Minimum) is the AA floor: a focused component must not be entirely hidden by author-created content. Focus Appearance is AAA, not the AA gate. These criteria do not decide the product's semantic focus destination.

Sources:
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://www.w3.org/TR/WCAG22/

## PRACTICE
After I072 declares the post-Undo semantic owner, capture baseline and 200% evidence for:
- focus-owner rectangle;
- restored-object rectangle if visible;
- Undo/recovery-control rectangle;
- viewport and safe-area rectangle;
- sticky/header/footer overlap;
- scroll offset before mutation, after fallback/intervening action, and after Undo;
- author-triggered scroll delta;
- wrapping/reflow and target geometry.

Compare immediate Undo, focus-only intervening action, operated intervening object, Reset supersession and navigation-return families.

## CRITIQUE
A geometrically attractive return to restored O is a failure if I072 says newer agency owns focus. Conversely, preserving the correct semantic owner can still fail spatially if it is obscured or requires unexplained large displacement. Geometry therefore follows, rather than chooses, semantic focus ownership.

## REPRODUCIBLE VALIDATION
Run each available family twice at baseline and 200%. Classify:
- correct owner / stable locus;
- correct owner / minimal reveal;
- correct owner / excessive displacement;
- correct owner / obscured;
- wrong semantic owner regardless of geometry.

Record actual rectangles and scroll deltas; screenshots alone are insufficient.

## PRODUCT TRANSFER / BLOCKERS
Executable LogMate hide/Undo/recovery and non-drag reorder are required for product evidence. forced-colors and independent-engine transfer remain downstream. Human workload and perceived continuity remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Color receives overlap/owner geometry; Web reproduces the same scenario manifest; Content receives available surface/line pressure; Type receives corpus pressure only after T021 gates.