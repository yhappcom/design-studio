# I083 — Scroll Anchoring vs Focus Continuity

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Evidence intent: SOURCE → PRACTICE → CRITIQUE → reproducible runtime validation → browser/product transfer

## Question
When reorder, row rebuild, status insertion, zoom/reflow or focus restoration changes geometry, can browser/framework scroll stabilization move the viewport without changing semantic focus or transaction truth?

## SOURCE
- CSS Scroll Anchoring adjusts scroll position to reduce visible content jumps; anchoring has suppression triggers/windows and `overflow-anchor` control.
- A 2026 CSSWG issue reports suppression-window behavior differing from the current draft across implementations; therefore spec reading is not browser-parity evidence.
- Flutter Scrollable may persist scroll position via PageStorage/ScrollController; framework persistence capability is not semantic focus or reorder correctness.
- WCAG 2.2 SC 2.4.11 remains the AA floor for author-created focus obscuration.

Sources:
- https://drafts.csswg.org/css-scroll-anchoring/
- https://lists.w3.org/Archives/Public/public-css-archive/2026Jul/0346.html
- https://api.flutter.dev/flutter/widgets/Scrollable-class.html
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum

## Contract
`semantic focus identity ≠ visual anchor node ≠ scroll anchor adjustment ≠ application scroll restoration ≠ reorder transaction`.

A viewport correction may preserve visual position without changing focus. Conversely, focus restoration may legitimately scroll. Neither event proves a reorder commit, cancellation, recovery, or persistence result.

## Reproducible scenario family
Use stable semantic IDs and the 35-item Customize model; run each twice:
1. focused source + reorder commit + row-height change above viewport;
2. focused source + cancel + status insertion/removal above viewport;
3. source off-screen rebuild + focus restoration;
4. 200% reflow while focus remains on the same semantic object;
5. Undo/Reset causing projection and height changes;
6. same scenarios with browser scroll anchoring enabled and controlled/disabled only where implementation permits;
7. served primary engine then independent engine.

Record semantic focus ID, DOM/Flutter focus identity where observable, scrollOffset before/after, bounding boxes, anchor-related CSS/configuration, projection hash, transaction result and visible/a11y status.

## CRITIQUE / failure conditions
FAIL if viewport motion changes semantic focus ownership, if index/recycled-row identity is used as focus restoration truth, if scroll adjustment is announced as mutation success, or if author scroll correction causes the focused component to become entirely obscured.

## RELATED DOMAIN CHECK
Type: T064 focus strings; Color: C095 focus/proxy separation; Layout: L086 obscuration geometry; Web: W095 served focus closure; Content: CD101 semantic-result truth. This is TRANSFER VALIDATION across browser scroll mechanics rather than a new ownership structure.

## HANDOFFS TO OTHER SPECIALISTS
Web must capture actual engine behavior because current CSSWG evidence shows implementation/spec divergence. Layout should measure viewport/focus geometry; Content/Color must not encode scroll movement as transaction state; Type remains downstream.

## Evidence boundary
No served runtime, independent-engine, AT, physical-device or human PASS is claimed.