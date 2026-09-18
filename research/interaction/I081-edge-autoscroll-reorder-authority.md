# I081 — Edge-autoscroll reorder authority

Status: STAGE 3 PRACTICE / TRANSFER SPEC
Date: 2026-09-19

## Question
When a dragged item enters a scrollable list edge and the viewport begins moving, which motion is evidence of user intent and which motion is merely transport of the viewport?

## SOURCE
WCAG 2.2 SC 2.5.7 requires dragging functionality to have an equivalent single-pointer alternative that does not require dragging. W3C Understanding 2.5.7 distinguishes user-agent scrolling from author-interpreted dragging; keyboard equivalence alone does not satisfy the single-pointer requirement. Flutter `ReorderableListView`/`SliverReorderableList` expose `autoScrollerVelocityScalar` and `dragBoundaryProvider`; this establishes implementation capability, not LogMate behavior or accessibility PASS.

## SYNTHESIS
Treat these as independent state dimensions: pointer/gesture owner; edge-zone membership; autoscroll active state; scroll offset; semantic candidate destination; committed destination; reorder transaction. `edge zone entered != destination chosen`; `autoscrolled != reordered`; `row moved beneath a stationary pointer != pointer moved`; `candidate changed during autoscroll != commit`.

## PRACTICE / REPRODUCIBLE MATRIX
Use a 35-item LogMate Customize list with stable semantic IDs. Run each family twice: bottom-edge enter→autoscroll→edge exit→valid drop; top-edge equivalent; autoscroll→cancel; stationary pointer while rows move; list-end saturation; active drag during 200% reflow; sticky/safe-area intersection; same final move through the non-drag single-pointer path; Undo/Reset only after committed mutation.

Record pointer coordinates over time, viewport/scroll-container bounds, scrollOffset(t), edge-zone and drag-boundary bounds, candidate semantic ID over time, committed ID/index, transaction/branch/inverse, projection hash, focus owner and visible/a11y result.

## CRITIQUE / FAILURE CONDITIONS
FAIL if viewport motion alone commits a different destination; cancellation after autoscroll creates a transaction/recovery entry; reaching a scroll boundary is reported as failure; edge-autoscroll blocks the required non-drag alternative; or reflow changes the semantic target without a defensible commit rule. Velocity preference and overshoot are not inferred from model inspection.

## RELATED DOMAIN CHECK
Type: T062 transfer strings are downstream; no spacing/kerning compensation. Color: C093 separates preview/scroll/commit states. Layout: L084 already separates displacement from semantic ownership. Web: W093 requires served event/scroll provenance. Content: CD099 resolves messaging from semantic result, not gesture mechanics. This study extends rather than repeats I080 by testing authored autoscroll after arbitration has already selected reorder.

## HANDOFFS TO OTHER SPECIALISTS
Layout should measure edge-zone/reflow/sticky geometry without inferring intent from motion. Color should keep autoscroll-active distinct from candidate/commit. Content should not narrate autoscroll mechanics unless action/recovery changes. Web should capture scrollOffset(t), boundary configuration and semantic candidate/commit under served runtime.

## OPEN
Actual LogMate implementation; independent engine; forced colors; physical touch/pen; AT; human discoverability, overshoot, workload and representative-pilot evidence.