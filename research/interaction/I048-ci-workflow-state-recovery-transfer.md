# I048 — CI Workflow State and Recovery Transfer

Evidence purpose: **TRANSFER VALIDATION**

## RELATED DOMAIN CHECK
W061 defines the shared CI identity; L052 owns geometry; CD067 names product truth; C061 reinforces state without color-only dependence; T030 preserves rendering truth.

## Objective
Use deterministic CI to validate state/action/recovery continuity across the whole MintTap workflow while keeping human discoverability/comprehension claims open.

## Required transitions
Exercise, where supported by the isolated lab/fixture:
- initial/empty → first value;
- valid add → pending → success;
- invalid add → error → correction;
- pending → known failure → retry;
- ambiguous outcome → verify/reconcile before retry;
- partial/unavailable data → explicit bounded action;
- estimated ROC → final ROC;
- tax adjustment positive/negative;
- locale/currency change without state corruption;
- destructive action → confirmation/recovery path.

## Pass conditions
The artifact history must show actual state, available action, consequence and recovery without silent transitions or fabricated certainty. Focus/order and status evidence are captured when automation can observe them.

## Failure classes
`SILENT_STATE_CHANGE`, `FALSE_SUCCESS`, `FALSE_FAILURE`, `BLIND_RETRY`, `LOST_RECOVERY`, `FOCUS_DISCONTINUITY`, `ACTION_STATE_MISMATCH`, `AMBIGUOUS_OUTCOME_COLLAPSE`.

## Evidence boundary
Automation can establish deterministic behavior for the exact fixture. It cannot establish discoverability, trust, workload, comprehension, screen-reader quality or representative-user success.

## Next block
Execute these transitions under one W061 manifest and cross-critique failures with L052/CD067/C061/T030.

## HANDOFFS
Content verbalizes the exact state; Layout protects state/action/recovery adjacency; Web reproduces browser/runtime behavior; Color and Type preserve redundant readable cues.