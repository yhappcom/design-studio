# I060 — Material Feedback Repair Verification

Date: 2026-09-18
Stage: 3 PRACTICE
Purpose: TRANSFER VALIDATION after the MintTap ListTile/DecoratedBox assertion

## SOURCE
Flutter documents that InkWell reactions are painted on the ancestor Material. An opaque Container/Image/DecoratedBox between Material and InkWell can hide the reaction. Flutter recommends painting the decoration with `Ink`, or introducing an appropriate Material layer (including transparent Material where appropriate), rather than deleting interaction feedback.

Official sources:
- https://api.flutter.dev/flutter/material/InkWell-class.html
- https://api.flutter.dev/flutter/material/Ink-class.html

## PRACTICE
Repair acceptance requires all of the following under one build identity:
1. tappable ListTile still activates the intended destination/action;
2. pressed/ink feedback is visibly rendered on the intended surface;
3. keyboard focus remains reachable and visible;
4. selected state remains distinguishable from idle;
5. target geometry is not reduced to suppress the assertion;
6. decoration, clipping and Material ownership are structurally coherent;
7. no new duplicate Material surface changes elevation/shape semantics unintentionally.

Candidate implementation families are `Ink`-owned decoration or a deliberate Material layer. Selection is product-specific and must be validated against clipping, shape and surface semantics.

## CRITIQUE
An assertion-free run is necessary but not sufficient. Removing `onTap`, splash, focusability or selected styling can make the assertion disappear while degrading the interaction contract. Likewise, inserting a transparent Material mechanically can change clipping/paint order. The repair must preserve action, feedback and surface ownership together.

## REPRODUCIBLE VALIDATION
Capture idle, focused, pressed and selected states before/after repair. Repeat pointer/tap activation and keyboard traversal. Record visible-surface evidence and framework exceptions. Then execute I058 recovery families separately; a green Material smoke test does not prove pending/failure/ambiguous recovery.

## WCAG 2.2 TRANSFER
For Web transfer, keyboard focus must not be entirely obscured by author-created content (2.4.11 AA), and pointer target size/spacing must satisfy 2.5.8 AA where applicable. Automated geometry/state checks are not human usability evidence.

## RELATED DOMAIN CHECK
- Type: not causal to Material paint ownership.
- Color: C072 consumes visible state-surface evidence; token declarations alone are insufficient.
- Layout: L064 separately localizes RenderFlex overflow; do not conflate spatial overflow with ink ownership.
- Web: W072/W073 must verify served-browser focus/feedback after widget smoke passes.
- Content: state labels/consequences remain unchanged during this structural repair.

## HANDOFFS TO OTHER SPECIALISTS
Color receives rendered idle/focus/pressed/selected surfaces. Web receives keyboard/pointer evidence. Layout receives any target/clipping geometry change. Content is notified only if the repair changes visible state/consequence semantics.

## Evidence boundary
This is a repair-verification protocol; it does not claim the MintTap Material repair has been implemented or passed. Human/AT evidence remains OPEN.
