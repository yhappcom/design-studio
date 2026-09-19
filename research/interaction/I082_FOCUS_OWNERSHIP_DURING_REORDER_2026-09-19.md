# I082 — Focus Ownership During Reorder

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Evidence intent: SOURCE → PRACTICE → CRITIQUE → reproducible runtime validation → product/browser transfer

## Question
When a long Customize list reorders, autoscrolls, rebuilds rows, or shows a drag proxy, what owns keyboard focus, and can the user still identify and operate the focused semantic object?

## Source findings
- WCAG 2.2 SC 2.4.11 (AA) requires a component receiving keyboard focus not to be entirely hidden by author-created content. W3C specifically calls out sticky headers/footers and overlays as common obscurers and recommends reducing partial obscuration even when AA still passes.
- WCAG 2.2 SC 2.5.7 (AA) independently requires a non-drag single-pointer path for authored dragging functionality.
- Flutter `ReorderableListView` supports a `proxyDecorator`; the proxy is a decorated representation of the dragged child. Framework support does not establish product focus behavior or accessibility equivalence.
- Flutter reorder callbacks distinguish drag end from actual reorder: `onReorderEnd` can fire when dropped in the same location, while `onReorderItem` is the application mutation callback. Focus/recovery must therefore resolve from semantic result, not merely drag termination.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://api.flutter.dev/flutter/material/ReorderableListView-class.html
- https://api.flutter.dev/flutter/material/ReorderableListView/proxyDecorator.html
- https://api.flutter.dev/flutter/material/ReorderableListView/onReorderEnd.html
- https://api.flutter.dev/flutter/material/ReorderableListView/onReorderItem.html

## Contract
`semantic object identity ≠ rendered row instance ≠ drag proxy ≠ focused node ≠ candidate destination ≠ committed destination`.

A drag proxy may represent an object visually but does not automatically become focus owner. Rebuild/virtualization must not silently transfer focus to a recycled row. Drag end is not mutation success. A committed move may require a deliberate focus-restoration policy, but that policy must be verified in product runtime rather than inferred from framework behavior.

## Reproducible scenario family
Use the 35-item Customize model and stable semantic IDs. Run each family twice:
1. Keyboard focus on source → pointer drag → autoscroll → valid commit.
2. Keyboard focus on source → drag proxy → cancel.
3. Source leaves viewport during autoscroll/rebuild → commit.
4. Source leaves viewport → cancel and restore.
5. Focused non-drag Move control → adjacent and multi-position move.
6. Commit/no-op/cancel while sticky header/footer is present.
7. Repeat at 200% zoom/reflow.
8. Repeat in forced-colors and an independent engine.

Record: scenario ID, semantic source/destination IDs, focused semantic ID before/during/after, active DOM/Flutter semantics identity where observable, source/proxy/focus rectangles, viewport and sticky rectangles, scrollOffset(t), transaction/branch/inverse, projection hash, visible status and accessibility payload.

## Critique / failure conditions
FAIL if any of the following occurs:
- focus lands on a recycled row solely because its index reused the old position;
- proxy styling visually impersonates focus while keyboard focus remains elsewhere;
- sticky/overlay content entirely obscures the focused component;
- cancellation mutates projection or announces a successful move;
- drag end is treated as reorder success without a committed semantic mutation;
- focus restoration targets ordinal position rather than stable semantic identity;
- non-drag alternative produces a different semantic result from drag.

## Evidence boundary
No product runtime, screen-reader, physical-device, independent-engine, human discoverability or representative-pilot PASS is claimed. SC 2.4.11 conformance must be measured in the actual rendered product. Human usability remains OPEN.