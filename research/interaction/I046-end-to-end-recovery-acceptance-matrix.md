# I046 — End-to-end Recovery Acceptance Matrix

Status: STAGE 3 PRACTICE / TRANSFER VALIDATION PREPARATION  
Date: 2026-09-17

## PURPOSE
Convert I045 into a finite behavioral matrix for the complete workflow rather than accumulating another isolated interaction specimen.

## RELATED DOMAIN CHECK
L050 owns spatial grouping; C059 visual state redundancy; T028 rendering pressure; W058/W059 runtime identity; CD064/CD065 user-facing state truth. Human task evidence remains OPEN.

## PRACTICE — state/action/recovery matrix
Across Start → Portfolio → Holding → Add Transaction → Insights/ROC/Tax → Settings, exercise:
1. empty → create/add → populated;
2. editing valid data → submit → known success;
3. editing invalid data → validation error → correction → success;
4. submit → pending → known failure → retry;
5. submit → ambiguous outcome/network interruption → verify/reconcile before destructive retry;
6. partial/unavailable data → explanation → refresh/recovery where actually available;
7. destructive action → confirmation/undo or documented recovery;
8. navigation away/back → preserve or intentionally discard draft with explicit consequence;
9. locale/text-scale change → focus and task continuity;
10. history/export → state meaning preserved outside the originating screen.

## CRITIQUE / FAILURE CONDITIONS
- false success/failure when outcome is ambiguous;
- duplicate-creating blind retry;
- focus lost or moved behind authored overlay;
- keyboard path differs materially from pointer/touch consequence without reason;
- state change communicated only by color;
- destructive action lacks proportionate confirmation/recovery;
- back/deep-link/history produces stale or semantically different state without notice;
- promotional interruption occurs before first value or blocks recovery.

## VALIDATION CONTRACT
For every scenario record initial state, action, transition, feedback, available next action, recovery, focus before/after, navigation/history effect and final state. Bind all observations to W058 identity and raw evidence. Automated/model critique is non-human evidence.

## HANDOFFS
Content owns wording for each true state; Color reinforces but cannot replace state semantics; Layout protects adjacency/focus visibility; Web executes browser-specific history/focus/network cases; Type handles rendering pressure.

## EVIDENCE BOUNDARY
No Stage 3 PASS, screen-reader/AT, physical-device, discoverability, workload or representative-human task-performance PASS is claimed.