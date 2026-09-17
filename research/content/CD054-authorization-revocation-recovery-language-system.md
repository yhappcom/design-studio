# CD054 Authorization Revocation Recovery Language System

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / TRANSFER VALIDATION**.

## Goal
Keep recovery capability, current authorization and authorization uncertainty semantically distinct when permissions change during a professional workflow.

## SOURCE
OWASP authorization guidance distinguishes authentication from authorization, recommends deny-by-default and permission validation on every request. Content therefore must not translate a cached signed-in state or previously available action into a current permission claim.

## RELATED DOMAIN CHECK
I035 owns actual authorization/action truth. L039 owns placement and continuity. C048 owns visual distinction. W048 owns request-time runtime evidence. Type consumes exact strings only after its drawing gates.

## Canonical semantic resources
- `recoveryAvailableButNotAuthorized`
- `authorizationCheckPending`
- `authorizationUnavailable`
- `recoveryPermissionChanged`
- `recoveryNotAuthorizedConfirmed`
- `recheckAuthorization`
- `priorRecoveryOutcomeUnknown`
- `readOnlyAccessRetained` when product authority explicitly supports it

Do not collapse `not authorized`, `authorization unavailable`, `not signed in`, `object unavailable`, `recovery unavailable`, and `recovery period ended`. They imply different causes and safe next steps.

## Wording rules
1. Do not say “You can restore this” from retention capability alone.
2. Do not say “Permission denied” when the authorization service is unreachable.
3. Do not say “Sign in again” unless authentication, rather than authorization, is the established dependency.
4. Do not promise “Ask an admin” unless the product actually exposes that escalation route.
5. If permission changes after a response-loss event, explain that the prior operation still requires reconciliation; do not imply revocation cancelled it.
6. Historical/export text must timestamp or otherwise qualify past permission evidence so it cannot read as current authority.

## Localization invariants
Translation may adapt grammar and politeness but must preserve the distinction between capability, permission, uncertainty and authentication. Missing-resource fallback must not strengthen uncertainty into denial or denial into recoverability failure.

## Accessibility
State changes that do not move focus still require programmatically available status semantics where applicable. Action labels must remain input-neutral and must not rely on color or position references.

## Evidence boundary
No Flutter/TMS/ARB round trip, linguistic review, AT, human comprehension or Content Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W048 must bind resource revision to request-time authorization verdict; C048/L039 must preserve these distinctions visually/spatially; I035 remains the authority for available action.