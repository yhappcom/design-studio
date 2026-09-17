# C049 Tenant Context Switch Visual Truth Contract

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / TRANSFER VALIDATION**.

## Goal
Extend C048 from permission revocation within one context to identity/tenant/workspace switching. Cached visual state from context A must not masquerade as authority in context B.

## SOURCE
OWASP Authorization guidance requires permission validation on every request and object-specific access checks. OWASP Multi-Tenant Security guidance requires verified tenant context and tenant-aware cache/session isolation. WCAG 2.2 remains the accessibility baseline.

## RELATED DOMAIN CHECK
Type: custom font remains provisional; context names and identifiers must use mature fallback. Layout/Interaction: I036/L040 own context transition, action truth, focus and spatial continuity. Web: W049 owns runtime/cache/route evidence. Content: CD055 owns context and stale-state semantics. UX remains cross-cutting.

## Visual truth states
Keep visually distinct without relying on hue alone:
- `contextConfirmed`
- `contextSwitchPending`
- `contextAuthorityUnknown`
- `stalePriorContext`
- `objectNotAuthorizedInContext`
- `objectUnavailableInContext`
- `contextSwitchConfirmed`

A selected row, cached success badge, prior tenant brand/accent, optimistic route title or focused destructive action cannot prove current context.

## Adversarial matrix
Test context A→B with stale A content retained during transition, identical object IDs across tenants, long/localized tenant names, forced colors, grayscale, background-image loss, 200% text, print/export and focus/selection removal. Current context must remain perceivable through text/structure and must not be inferred from brand color alone.

## Acceptance
PASS requires current-context consequence to outrank stale object success and prior-context decoration. If context authority is unknown, consequential controls must not look currently authorized. Static export must state its context/snapshot provenance rather than inherit the viewer's current context.

## Evidence boundary
No runtime, cross-browser, observer, calibrated-display or human context-switch comprehension PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W049 should return computed cue survival and cache-transition artifacts; I036/L040 return action/focus geometry; CD055 preserves non-color context semantics. Type must not shorten tenant/context strings to protect provisional metrics.