# W092 — Served pointer capture, suppression, and layout-boundary manifest

Status: PRACTICE / PRODUCT RUNTIME OPEN

## Goal
Close a browser-specific gap exposed by I079: framework gesture cancellation alone does not prove how the served Web build behaves when pointer capture, UA stream suppression, hit testing and layout-driven boundary events interact.

## SOURCE
Pointer Events Level 3 became a W3C Recommendation on 30 June 2026. The current Level 4 Working Draft dated 26 August 2026 retains the capture/suppression model: capture overrides normal hit testing for subsequent pointer events; `pointerup` implicitly releases capture; stream suppression fires `pointercancel` and releases capture; layout changes can cause boundary events for a stationary pointer. Flutter `Listener` exposes raw pointer callbacks including `onPointerCancel`, but framework API availability is SOURCE/feasibility evidence, not proof of DOM/browser event order or product semantics.

## SERVED EVIDENCE MANIFEST
For each scenario preserve one `scenario_id` across production build → served primary engine → independent engine → 200% → forced-colors. Record:
- build SHA/browser+version/OS/input modality;
- pointer ID/type and coordinates;
- DOM/browser event order where observable (`pointerdown/move/up/cancel`, capture/boundary events);
- Flutter pointer/gesture/action result where observable;
- semantic object/action/candidate/committed destination;
- capture/gesture owner and hit target separately;
- transaction/branch/inverse and projection hashes;
- focus and visible/a11y status;
- source/candidate/focus/recovery rectangles, scroll and obscuration;
- runtime exception/log.

## SCENARIOS
1. Captured/owned drag leaves source bounds and resolves validly.
2. Stationary active pointer while 200% recomposition moves row/candidate boundaries.
3. UA suppression/pointercancel path where reproducible, including viewport-manipulation conflict on touch-capable hardware when available.
4. Visual row rebuild/removal during preview.
5. Capture/gesture release followed by later pointer sequence: stale owner must not mutate.
6. Compare the same semantic move through the non-drag single-pointer alternative; replicate each executable family twice.

## CRITIQUE / PROMOTION
Do not infer browser PASS from Pointer Events conformance text or Flutter API docs. FAIL if a browser event artifact becomes transaction authority, cancellation commits, layout movement fabricates a destination, stale capture state leaks into the next sequence, or primary/independent engines produce materially different semantic results without an explicit blocker/contradiction record.

WCAG 2.2 SC 2.5.2, 2.5.7 and 2.5.8 remain separate acceptance axes. Full WCAG conformance is not claimed from these scenarios.

Performance: Lighthouse/DevTools/CI remain LAB. Only provenance-bearing aggregate/RUM may be called FIELD LCP/INP/CLS evidence.

## RELATED DOMAIN CHECK
Type T061 remains downstream behind T021. Color C092 needs rendered interruption states. I079 owns semantic lifecycle; L083 owns recomposition geometry; CD098 owns semantic feedback. W092 is TRANSFER VALIDATION of those contracts in actual browser runtime.

## HANDOFFS TO OTHER SPECIALISTS
Return browser ordering/capture contradictions to Interaction; geometry failures to Layout; forced-colors state loss to Color; wording/a11y payload mismatch to Content; reproduced font/fallback failures only to Type.

## OPEN
Actual LogMate reorder implementation, served runtime execution, Safari/Firefox breadth, physical touch/pen, screen reader, field Core Web Vitals and representative-human evidence remain OPEN.