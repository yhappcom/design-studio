# I035 Recovery Authorization Revocation Contract

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / TRANSFER VALIDATION**.

## Goal
Extend I034 recoverability across a permission change. An object may remain technically recoverable while the current subject is no longer authorized to recover it. Capability, object state and subject authorization are separate authorities.

## SOURCE
Current OWASP Authorization Cheat Sheet guidance distinguishes authentication from authorization, recommends deny-by-default, and requires permission validation on every request. This study applies those security invariants to the UX/action oracle rather than treating a cached enabled control as authority.

## RELATED DOMAIN CHECK
C048 must not make prior permission visually persistent. L039 must preserve current permission consequence near the affected action. W048 owns runtime request/recheck evidence. CD054 owns permission/recovery language. Type remains provisional and cannot solve authorization ambiguity.

## Authority tuple
A consequential recovery action requires all of:
`objectRecoverable == confirmed` + `subjectAuthorizedForRecovery == confirmed` + `targetIdentityContinuity == confirmed` + action-specific preconditions/idempotency satisfied.

Any unknown member blocks automatic recovery. A cached role, previously enabled Restore control, successful prior request, local ownership label or possession of an object ID is not sufficient authorization evidence.

## Deterministic scenarios
1. Recovery confirmed under policy p1; subject permission is then revoked before request.
2. Client remains offline with cached `Restore` enabled; reconnect returns authorization denied.
3. Recovery request is accepted, response is lost, then permission is revoked before reconciliation. Do not infer that revocation rolled back the already-authorized effect.
4. Permission is restored later. Recheck object/recovery state before re-enabling action; do not replay the old request automatically.
5. Read access remains while recovery mutation access is revoked. Preserve history/read-only context without presenting mutation capability.
6. Authority service unavailable. Distinguish `authorizationUnknown` from `notAuthorized`.

## Action oracle
- `recoverable + authorized` → recovery may be offered subject to remaining evidence.
- `recoverable + notAuthorized` → no recovery mutation; preserve explanation/history and any legitimate escalation path supplied by product authority.
- `recoverable + authorizationUnknown` → block mutation and offer recheck when meaningful.
- `recoveryOutcomeUnknown + permissionRevoked` → reconcile prior operation by operation/object authority; do not retry.

## Accessibility / feedback
Permission-state changes that alter available actions are status changes. They must remain programmatically exposed where applicable and must not strand keyboard focus when a control disappears. Focus relocation must preserve meaning and operability; this is a deterministic accessibility requirement, not human comprehension evidence.

## Evidence boundary
No production authorization model, backend enforcement, AT, human comprehension or task-performance PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W048 must prove server-side/request-time authorization behavior; C048/L039/CD054 must represent the same verdict without inventing permissions or escalation routes.