# L019 — Geometry Evidence Join Protocol

Evidence type: SYNTHESIS / TRANSFER VALIDATION / OPEN

## RELATED DOMAIN CHECK
T022 metrics are not frozen. C028 needs actual overlap classification. I013 supplies state/action identity. W025 is the browser executor. CD032 supplies long/localized strings. Human workload remains OPEN.

## Purpose
L018 defined the stress matrix; L019 makes its evidence reproducible across domains rather than producing disconnected screenshots.

## Capture contract
Each geometry run receives one capture ID containing route, semantic state, viewport CSS size, zoom, visual viewport if available, keyboard state, safe-area assumption/device, focused control, sticky/overlay rectangles, focused-control rectangle, horizontal overflow, reading/focus order, localized string fixture and expected safe action.

Derived classifications are: `clear`, `partial overlap`, `entirely obscured`, `off-viewport`, and `reflow failure`. Do not infer keyboard geometry from desktop viewport resizing; label simulation separately.

## Acceptance boundaries
At 200% zoom the workflow must remain operable without hiding required information/actions through authored layout. C028 consumes exact overlap data for WCAG 2.2 focus analysis. I013 recovery action must remain reachable after reflow. Numeric component widths remain unfrozen until Type/product metrics justify them.

## Current result
**PROTOCOL PASS / ENVIRONMENT TRANSFER OPEN.** This is a reproducibility advance, not physical-device or browser evidence.

## HANDOFFS TO OTHER SPECIALISTS
C028 joins by capture ID. W025 implements the record. CD032 attaches message ID/revision. UX integration can trace a failure from semantic state through geometry without converting it into human-usability evidence.