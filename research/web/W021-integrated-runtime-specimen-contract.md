# W021 — Integrated professional-record runtime specimen contract

Classification: **INTEGRATION + TRANSFER VALIDATION DESIGN**

## Purpose
Replace isolated browser micro-tests with one coherent executable target that consumes L013, I008, C021 and CD021 simultaneously.

## RELATED DOMAIN CHECK
- Type: T021 custom family is not drawing-valid; specimen uses current product/fallback typography and treats custom-font transfer as blocked.
- Color: C021 provides candidate light/dark semantic pairs; browser contrast/forced-color behavior must be returned to Color.
- Layout/Interaction: L013/I008 define recomposition and state/action invariants.
- Content: CD021 provides structured message IDs, typed literals and localization stress.

## Specimen surfaces
One semantic DOM/task model must support:
- narrow phone composition;
- tablet/EFB split composition;
- desktop/web navigation + list + detail composition.

CSS may recompose regions, but source/DOM order must remain meaningful without relying on visual placement.

## Integrated executable assertions
1. Keyboard traversal reaches all currently available task actions in meaningful order.
2. Sticky/transient regions do not fully obscure focused controls/status; focus remains visually detectable.
3. Pending, confirmed, known-failure and outcome-unknown expose distinct semantic status text; outcome-unknown has no blind retry action.
4. 30–40% pseudo-expanded strings and long action labels reflow without semantic truncation.
5. RTL wrapper text preserves LTR operational identifiers as distinct literals using bidi isolation.
6. 200% text/zoom or the closest environment-supported browser mechanism triggers recomposition rather than ordinary two-dimensional task scrolling.
7. Light/dark theme preserves semantic role mapping; forced-colors acceptance is based on state/focus/control survival rather than authored hue retention.
8. Reduced-motion mode preserves state/focus meaning without animation dependency.
9. Viewport recomposition does not mutate commit/certainty state.
10. Local/lab timing may diagnose readiness/layout instability but cannot be labeled production LCP/INP/CLS field evidence.

## Route/network boundary
True direct-entry/reload/404/auth and request-dispatch ambiguity require an HTTP/network-capable environment. If blocked, W021 records the blocker and retains deterministic I008 state simulation rather than presenting simulation as network evidence.

## WCAG 2.2 baseline
Conformance checks use published WCAG 2.2 normative criteria as the studio baseline. Focus Not Obscured (Minimum), Target Size (Minimum), reflow/text resizing and related criteria are treated with their normative scope/exceptions. Technique examples are not substituted for success criteria.

## Performance evidence boundary
- **Lab/local:** useful for rendering order, layout movement, interaction instrumentation and regression diagnostics.
- **Field:** required before product LCP/INP/CLS claims. No local/headless result is promoted to field Core Web Vitals evidence.

## Gate result
**INTEGRATED EXECUTION CONTRACT READY; BROWSER EXECUTION OPEN.**
This advances W021 from an unspecified next task to a falsifiable integrated specimen, but Stage 3 does not pass until actual browser evidence exists.

## HANDOFFS TO OTHER SPECIALISTS
- Layout/Interaction: return any recomposition/focus/state contradictions.
- Color: return computed pair/forced-colors behavior.
- Content: return string-fit, bidi and semantic-status failures.
- Type: custom-font browser transfer remains blocked until drawing validity.