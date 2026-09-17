# W048 Recovery Authorization Revocation Runtime Contract

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / PRODUCT TRANSFER TARGET**.

## Goal
Transfer W047 retention/recovery into request-time authorization change. A cached UI capability must never become the authorization oracle.

## SOURCE
OWASP Authorization Cheat Sheet guidance requires deny-by-default and permission validation on every request, and explicitly warns against relying on client-side access control. WCAG 2.2 remains the accessibility baseline; focus order must preserve meaning/operability and status changes must be programmatically available where applicable.

## RELATED DOMAIN CHECK
I035 supplies the action oracle. L039 supplies focus/spatial continuity. C048 supplies visual-truth assertions. CD054 supplies semantic resources. T021 custom font remains provisional; mature fallback is required for closure evidence.

## Runtime chain
1. Load authoritative deleted/recoverable object under subject permission set a1.
2. Render recovery capability only after object/recovery authority is known; record current authorization evidence separately.
3. Go offline or hold a stale client with Restore previously available.
4. Revoke recovery mutation permission server-side to a2 while optionally retaining read/history access.
5. Reconnect and attempt/recheck. Server/request-time authorization must decide; cached client state cannot grant.
6. Capture `notAuthorized`, `authorizationUnknown`, or `authorized` separately from object recoverability.
7. Variant: recovery request accepted, response lost, then permission revoked. Reconcile the prior operation without automatic retry.
8. Variant: permission restored later while object state changed. Recheck both authorization and object recoverability before enabling mutation.
9. Reload/deep-link/history/export and verify stale permission evidence does not become current authority.

## Provenance
One run binds `runId`, `subjectId` or non-sensitive test principal ID, `authorizationPolicyRevision`, `authorizationVerdictId`, `objectId`, `deletionEventId`, `recoveryOperationId`, `retentionPolicyRevision`, `authorityRevision`, browser/engine/version, commit SHA, network ordering, resource revision/locale, computed visual state, focus/geometry and artifact hashes. Do not store real credentials/tokens in artifacts.

## Security boundary
Client-side hidden/disabled controls are UX affordances, not enforcement. Production claims require backend authorization enforcement on the requested resource/action. If authorization authority is unavailable, exercise deny/safe-block behavior appropriate to the product contract rather than inventing permission.

## Accessibility transfer
Capture focus destination when an authorized control becomes unavailable; verify logical focus order and non-obscuration. Capture programmatic status semantics for permission changes where applicable. These are deterministic checks, not human comprehension evidence.

## Browser closure
Chromium plus an independent engine are required before cross-browser claims. Safari claims require Safari execution. Forced-colors, 200% text, localization, offline/reconnect and export are required transfer stresses.

## Performance boundary
Authorization/reconnect timings are lab/functional diagnostics. LCP/INP/CLS are field evidence only with actual field/RUM population context.

## Evidence boundary
No W048 execution, production authorization enforcement, cross-browser, Safari, screen-reader, physical-device, field Core Web Vitals or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Return actual permission cue survival to C048, focus/geometry to L039, action discrepancies to I035 and resource/fallback findings to CD054.