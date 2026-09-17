# W050 — Offline Outbox Tenant-Binding Runtime Contract

Evidence purpose: **STAGE 3 PRACTICE / RUNTIME CLOSURE TARGET / TRANSFER VALIDATION**. Extends W049 from stale cache/response isolation into persisted deferred mutations.

## RELATED DOMAIN CHECK
- **Type:** T021 remains provisional; mature fallback is mandatory.
- **Color:** C050 defines visual truth under cue degradation.
- **Layout/Interaction:** I037 defines dispatch authority; L041 defines queue/context geometry and focus continuity.
- **Content:** CD056 defines queue/context language and localization invariants.
- **UX:** deterministic workflow evidence is distinct from human comprehension/task evidence.

## Current source basis
OWASP Multi-Tenant Security guidance identifies queue injection/shared-resource pollution as cross-tenant risks, requires verified tenant context for tenant-scoped requests, and treats client tenant identifiers as selectors rather than authorization. OWASP Authorization guidance requires deny-by-default and permission validation on every request. These sources support the boundary below; they do not prescribe a specific offline queue implementation.

## Runtime invariant
Persist each consequential queued operation with immutable or explicitly versioned provenance:
`operationId | principalId | originContextId | objectId | operationKind | authoredAt | policy/precondition revision | payload digest | idempotency/reconciliation key where supported`.

Current UI context is separate runtime state. Queue dispatch must never substitute `currentContextId` for `originContextId` merely because the user switched workspaces.

## Closure scenario
Execute as one trace where possible:
1. Confirm A and object-17.
2. Go offline; enqueue consequential operation q1 under A.
3. Switch UI to B while q1 remains persisted.
4. B also contains object-17 variant.
5. Reconnect; verify q1 remains A-bound and suspended/rechecked rather than dispatched as B.
6. Exercise A authorization revoked variant.
7. Exercise rapid A→B→A plus delayed context responses.
8. Dispatch q1 under verified A; inject response loss.
9. Switch to B; preserve q1 `outcomeUnknown` and reconcile against A authority without exposing protected A payload to B.
10. Reload/deep-link/history/export and prove origin context survives reconstruction.

## Required evidence
Capture browser/engine/version, commit SHA, runId, operationId, principalId, origin/current context IDs, policy revision, object identity, request target/context, response/reconciliation result, persistence record schema, DOM/AX-relevant state, focus, computed styles, viewport/reflow geometry, locale/resource revision and artifact hashes.

## Security boundary
Client-side queue labels, hidden controls, cache partitioning and context selectors improve UX but do not enforce authorization. Protected dispatch requires server/data-layer authorization at execution. Unknown production policy means safe blocking, not invented transfer semantics.

## Browser and performance boundary
Chromium plus an independent engine are required before cross-browser claims; Safari requires Safari execution. Queue/reconnect timing is lab/functional diagnostic. LCP/INP/CLS become field evidence only with actual RUM population/context.

## Evidence boundary
No W050 runtime PASS, Web Stage 3 PASS, production tenant isolation, cross-browser, AT, physical-device, field Core Web Vitals or human UX PASS is claimed by this contract.

## HANDOFFS TO OTHER SPECIALISTS
Use shared `runId/principalId/originContextId/currentContextId/objectId/operationId/artifactId` across C050, I037/L041 and CD056.