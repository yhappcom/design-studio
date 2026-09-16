# L020 — W027 Adaptive Geometry Transfer

Evidence type: SYSTEMS PRACTICE / TRANSFER VALIDATION / OPEN

## RELATED DOMAIN CHECK
W027 provides the concrete surface. C029 consumes focus/occlusion geometry. I014 owns recovery behavior. CD033 supplies expansion strings. T023 supplies measured mature-font metrics later. Layout owns spatial survival, not semantic state truth.

## Geometry contract
For each W027 capture ID collect layout viewport, visual viewport where exposed, zoom, focused element rect, sticky-layer rect, viewport intersection, horizontal overflow, primary action visibility, reading/order continuity, and long-string wrapping. Required stress cases are baseline desktop, narrow viewport, 200% zoom, narrow+200%, keyboard-reduced visual viewport where executable, and localization expansion.

The key failure is not merely horizontal overflow. A layout fails the transfer if the recovery action becomes unreachable, focus is entirely obscured by authored content, semantic order is broken, or long content forces a destructive fixed-width assumption.

## Adaptive rule
Do not freeze numeric widths before T023 product-font evidence. Prefer content-driven/min-max geometry and allow state/recovery copy to wrap. Layout must absorb required semantics rather than pressure Content to shorten truthful wording.

## Current result
**TRANSFER PROTOCOL BOUND TO A CONCRETE SURFACE / EXECUTION OPEN.** W027 makes L019 measurable, but no browser/device rectangles are claimed until the harness is actually served and exercised.

## HANDOFFS TO OTHER SPECIALISTS
C029 consumes focus/overlay rectangles; W027 records them by capture ID; Content gets any wrap-induced comprehension risks; Type receives strings that expose metric/fallback stress; UX receives action reachability and order evidence.