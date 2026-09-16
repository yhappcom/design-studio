# L022 — Workflow Reflow & Reachability Contract

Date: 2026-09-16
Evidence: SYSTEMS PRACTICE / TRANSFER VALIDATION CONTRACT / OPEN

## RELATED DOMAIN CHECK
- **Type:** T021 metrics are not yet production-valid; use mature fonts for geometry transfer.
- **Color:** C031 requires same-capture focus/overlay evidence but does not own geometry.
- **Interaction:** I018 supplies the end-to-end safe-action oracle.
- **Web:** W029/W030 owns actual browser execution provenance.
- **Content:** CD036 and later complete-system strings are not shortened to preserve geometry.

## Spatial question
Can the next safe action and the information needed to choose it remain reachable and correctly prioritized as the workflow moves through long content, narrow reflow, actual zoom, sticky layers, keyboard-reduced viewport and localization expansion?

## Geometry record per capture
Record layout viewport, visual viewport where available, document scroll dimensions, focused-control rectangle, sticky/fixed overlay rectangles, primary safe-action rectangle, message/heading rectangle, scroll position, horizontal overflow, and whether reading/action order matches DOM/focus order.

## Distinct transfer classes
- 320 CSS px narrow viewport: responsive reflow stress only.
- Actual browser 200% zoom: zoom evidence; do not substitute narrow viewport.
- Text-only enlargement where applicable: separate text-resize evidence.
- Software-keyboard reduced visual viewport: separate mobile geometry evidence.
- Headless browser: browser automation evidence, not physical-device evidence.
- Physical phone/tablet: device transfer; not implied by emulation.

## Failure conditions
- safe reconciliation action entirely obscured by author-created sticky content;
- action reachable only through horizontal scrolling in a one-dimensional workflow where reflow should avoid it;
- visual reorder contradicts DOM/focus/task order;
- localization moves consequence text away from the action such that association is lost;
- persistent controls consume enough viewport that record context or recovery status cannot be inspected;
- back/forward transition restores scroll/focus to a misleading prior state.

## Critique rule
A geometry PASS cannot establish semantic correctness or comprehension. Conversely, a semantically correct action that is obscured or unreachable is a product failure. I018 + Content truth and L022 geometry must both hold.

## Accessibility baseline
WCAG 2.2 is the studio baseline. Focus Not Obscured (Minimum) is evaluated against author-created content separately from stronger full-visibility goals. Reflow/zoom evidence must use the actual test mode being claimed.

## UX integration
The intended outcome is lower interaction friction and safer recovery, but perceived effort/workload remains HUMAN EVIDENCE OPEN. This contract establishes observable geometry and reachability only.

## HANDOFFS TO OTHER SPECIALISTS
- **Web:** capture these fields in actual browser runs.
- **Color:** consume identical focus/overlay captures for C031.
- **Content:** preserve complete semantic strings and flag expansion cases.
- **Type:** later rerun with valid custom metrics after T021.
