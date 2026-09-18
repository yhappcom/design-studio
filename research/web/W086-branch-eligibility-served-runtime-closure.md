# W086 — Branch eligibility served-runtime closure

## Purpose
Extend W085 from causal Undo to I073 branching-history evidence. Correct final projection is insufficient if the browser exposes a stale recovery target or loses current focus/agency.

## RELATED DOMAIN CHECK
Type T055, Color C086, Layout L077, Interaction I073 and Content CD092 checked. This is `TRANSFER VALIDATION` into real browser/runtime closure.

## Closure manifest
For each scenario capture: product commit/build, served route, engine/version, viewport, zoom, theme/forced-colors, `scenario_id`, `step`, `tx_id`, `parent_tx_id`, `branch_id`, `inverse_of`, eligibility before/after, semantic order/visibility, projection hash, current focus semantic/action identity, recovery-control identity/state, visible status, accessibility status payload, focus/recovery/target rectangles, scroll/obscuration, console/runtime exceptions.

## Required scenarios
Run twice where executable:
1. A → B → Undo B;
2. A → B → Undo B → C;
3. previous Undo consumed → focus-only move;
4. previous Undo consumed → Reset;
5. stale recovery invocation guard;
6. branch replacement at 200% reflow.

Then transfer identical scenario IDs from production Web build → served primary engine → independent engine → forced colors. A Chromium-only widget micro-test does not close the stage.

## Browser/Flutter considerations
Flutter focus state is its own tree/history and can change after build; record semantic/focus identity rather than relying on visual ordinal. A focus-only framework history change must not be mistaken for a configuration transaction. Browser accessibility output and visible Flutter state are separate evidence rungs.

## Accessibility
WCAG 2.2 remains the baseline. Focus visibility/obscuration and status-message behavior are checked in actual runtime, while branch-stack semantics remain a Studio/product contract rather than a WCAG-prescribed algorithm.

## Performance evidence boundary
Lighthouse, DevTools and CI traces remain LAB/synthetic. Only provenance-bearing aggregate/RUM can support FIELD LCP/INP/CLS claims. This study creates no field performance evidence.

## Failure conditions
FAIL if stale recovery remains actionable, branch identity differs across visible/accessibility state, current focus is replaced by stale restoration, 200% hides the current locus, forced colors erases the only eligibility cue, or runtime errors occur despite correct final order.

## OPEN
Actual LogMate non-drag reorder/recovery implementation, independent browser, forced-colors, screen-reader, physical-device, field CWV and representative-human UX remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Return any browser contradiction to I073/CD092/C086/L077/T055 with the same scenario ID; do not patch semantic failures only in Web presentation.
