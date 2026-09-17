# W049 Tenant Context Cache Isolation Runtime Contract

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / PRODUCT TRANSFER TARGET**.

## Goal
Extend W048 from permission revocation to subject/tenant/workspace context switching, including route, cache, service-worker/local persistence and out-of-order network responses. UI context is not the authorization oracle.

## SOURCE
OWASP Authorization guidance requires authorization on every request and exact-object checks. OWASP Multi-Tenant Security guidance requires verified tenant context, tenant-scoped resource checks, and cache/session isolation; tenant/user/locale/permission-version attributes that change results belong in cache decisions. OWASP IDOR guidance requires authorization for each referenced object across read/update/delete/export operations. WCAG 2.2 remains baseline.

## RELATED DOMAIN CHECK
I036 supplies context/action oracle; L040 supplies spatial/focus contract; C049 supplies visual truth; CD055 supplies semantic resources; Type custom font remains provisional.

## Runtime chain
1. Authenticate test principal with access to tenant A and B; load A/object-17.
2. Record A tenant/policy/object authority and cache provenance.
3. Initiate switch to B while retaining delayed A fetch/mutation responses.
4. Verify each B request derives/validates B context server-side; client tenant ID is selector, not proof.
5. Deliver delayed A response after B confirmation. It must not populate B-authoritative protected state.
6. Variant: B also has object-17 but it is a distinct tenant-scoped object.
7. Variant: B lacks read/mutate permission; stale A cache exists.
8. Variant: switch response lost, yielding context authority unknown.
9. Rapid A→B→A with reordered responses and cache reuse.
10. Reload, deep-link, browser history, offline/reconnect, locale change and export; prove current context and artifact provenance remain scoped.

## Provenance
Bind `runId`, non-sensitive `principalId`, `contextId`, `contextRevision`, `authorizationPolicyRevision`, `authorizationVerdictId`, `objectId`, `objectAuthorityRevision`, request/response context, cache key namespace, route, resource revision/locale, browser/engine/version, commit SHA, focus/geometry, computed state and artifact hashes. Never record real credentials/tokens.

## Security boundary
Hidden controls, context selector state, route parameters and opaque object IDs are not enforcement. Protected data must be authorized before delivery/use. Production claims require actual server/data-layer isolation evidence; otherwise test safe blocking only.

## Browser/accessibility closure
Require Chromium plus an independent engine before cross-browser claims; Safari separately for Safari. Stress forced colors, 200% text, keyboard focus, offline/cache, localization and export. Programmatic status/focus checks are deterministic accessibility evidence, not human UX evidence.

## Performance boundary
Cache/context-switch timings are lab/functional diagnostics. Field LCP/INP/CLS require actual RUM population context.

## Evidence boundary
No W049 execution, production tenant isolation, cross-browser, Safari, screen-reader, physical-device, field Core Web Vitals or human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Return stale cue survival to C049, focus/geometry to L040, action discrepancies to I036, and resource/fallback/context-string findings to CD055.