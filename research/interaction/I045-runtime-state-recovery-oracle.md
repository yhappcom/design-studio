# I045 — Runtime state/recovery oracle

Status: PRACTICE / TRANSFER VALIDATION PREPARATION

## PURPOSE
Make I044 executable by defining observable state/action/recovery continuity for the integrated product workflow.

## RELATED DOMAIN CHECK
T027 preserves rendered action/state language; C058 requires redundant state encoding; L049 protects spatial association; W057 captures runtime/focus/history artifacts; CD063 names state/action/consequence/recovery.

## ORACLE
For each Start → Portfolio → Holding → Add Transaction → Insights/ROC/Tax → Settings scenario record:
- entry state and user goal;
- available action and its visible/accessibility name;
- immediate feedback;
- pending/ambiguous/success/failure state when applicable;
- retry/cancel/back/undo path where applicable;
- focus destination and restoration;
- navigation/history/deep-link continuity;
- resulting data/history visibility.

Failures include silent state change, focus loss/obscuration, action without consequence feedback, ambiguous outcome presented as known failure/success, destructive dead end, retry that duplicates state, and promotional/ad interruption before first-value completion.

For web markup, consequential status updates should be programmatically determinable without requiring focus where WCAG 4.1.3 applies.

## EVIDENCE BOUNDARY
No AT announcement quality, physical-device, discoverability or representative-user task PASS is claimed until executed with appropriate evidence.

## HANDOFFS
CD063 owns wording; L049 owns spatial visibility; C058 owns visual redundancy; W057 owns executable evidence packaging.