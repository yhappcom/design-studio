# I036 Tenant Context Switch Authority Contract

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / TRANSFER VALIDATION**.

## Goal
Prevent stale identity/tenant/workspace context from authorizing consequential actions after a context switch.

## SOURCE
OWASP recommends deny-by-default, authorization on every request, object-level authorization, and verified tenant context for tenant-scoped access. Multi-tenant cache/session state must be scoped to the relevant tenant/user attributes.

## RELATED DOMAIN CHECK
C049 owns visual truth; L040 owns spatial/focus continuity; W049 owns runtime/cache/route provenance; CD055 owns semantic state; Type remains on mature fallback until T021 closes.

## State contract
`contextConfirmed(A) → switchRequested(B) → contextSwitchPending → contextConfirmed(B) | contextAuthorityUnknown | switchRejected`.

Object state and context state are independent. An object visible under A may be `notAuthorized`, `unavailable`, or a distinct object under B even if the route/object identifier text is identical.

## Action oracle
A consequential action is enabled only when current subject, tenant/context, exact object, operation and relevant policy are jointly authoritative. Cached A authorization, prior enabled state, route persistence, browser history, optimistic selection or local storage cannot grant B authority.

During unknown context, default to safe blocking for protected mutation. Read-only retained content must be explicitly marked stale/prior-context when product policy permits its display.

## Transition/recovery scenarios
1. A object open + focused mutation control → switch to B.
2. B has same route/object ID but different object.
3. B lacks read permission while A data remains cached.
4. switch response lost; current context uncertain.
5. rapid A→B→A switch with out-of-order responses.
6. reload/deep-link/history/export after switch.
7. permission changes during switch.

## Accessibility
When controls disappear or content is replaced, focus moves to a logical surviving context/object anchor; status changes are exposed programmatically where applicable. Deterministic checks do not equal human comprehension evidence.

## Evidence boundary
No production tenant enforcement, runtime, AT, physical-device or human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
L040 should preserve context→object→authority→action hierarchy; W049 must prove request/cache isolation; C049 checks stale cue precedence; CD055 names uncertainty without implying logout/deletion.