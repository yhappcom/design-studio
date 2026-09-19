# I096 — Runtime authority under offline, retry and update

Date: 2026-09-20
Status: Stage 3 PRACTICE / H5 RUNTIME AUTHORITY

## Purpose
Prevent runtime/network transitions from collapsing product truth in professional record workflows.

## RELATED DOMAIN CHECK
Checked T078, C109, L099, W108 and CD114. Extends I095 from cross-surface transfer to degraded-runtime authority. CONTRADICTION REVIEW + TRANSFER VALIDATION.

## Authority chain
`visible draft ≠ validated draft ≠ local commit ≠ persistence attempt ≠ persisted local state ≠ remote/sync acknowledgement ≠ refreshed projection`.

Offline availability is a capability state, not proof of persistence or sync. Retry initiation is not success. Reload/update must not silently promote uncertain state.

## Scenario family
1. Add Flight edit → local commit → persistence failure → retry → recovery.
2. Offline launch → create/edit → route return → reconnect → reconciliation.
3. Import preview → commit attempt interrupted → reload → determine committed/unknown/not committed before offering retry.
4. Update/reload while dirty draft or Undo is available.

## Failure conditions
FAIL on duplicate mutation from blind retry; lost dirty draft without explicit contract; Saved/Synced before evidence; stale projection presented as current without state; focus moved merely to announce routine status; or recovery offered when inverse/transaction identity is absent.

## Accessibility boundary
Routine result/wait/error status that does not take focus must be programmatically determinable; focus remains reserved for actual context changes/recovery needs. Non-drag reorder remains independently OPEN under WCAG 2.2 SC 2.5.7.

## Human boundary
Trust, workload, comprehension and pilot recovery performance remain HUMAN evidence and are not simulated.

## HANDOFFS TO OTHER SPECIALISTS
Content names only states this authority model can prove. Color encodes them without merging. Layout preserves ownership/focus. Web records transaction, route, network and persistence provenance.