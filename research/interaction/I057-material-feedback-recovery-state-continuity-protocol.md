# I057 — Material feedback and recovery-state continuity protocol

## Purpose
Repair the Material ownership assertion without sacrificing observable interaction feedback, then extend validation through consequential recovery states.

## Stage
Stage 3 PRACTICE / NOT PASSED. TRANSFER VALIDATION.

## PRACTICE A — interaction layer ownership
For each tappable ListTile/surface implicated by the runtime assertion, trace:
`pointer/keyboard focus → Material ancestor → Ink response → painted decoration → visible feedback → activation`.

The repair must make the Ink/state surface visible. Removing `onTap`, splash/highlight/focus feedback, or covering the feedback with another opaque layer is not an acceptable repair.

## PRACTICE B — state continuity
After basic activation is stable, exercise two distinct recovery families:

1. `idle → action → pending → known failure → correction → retry → success`
2. `idle → action → pending → ambiguous outcome → verify/reconcile → safe retry or resolved state`

Known failure and ambiguous outcome must not share the same instruction when retry could duplicate a consequential action.

## CRITIQUE dimensions
- feedback visibility;
- keyboard/focus continuity;
- target geometry;
- state/action adjacency;
- progress honesty;
- error specificity;
- recovery discoverability;
- duplicate-action prevention;
- history/reconciliation continuity.

## Reproducible validation
Record build SHA, route, initial state, input method, state transition, visible feedback, focus destination, resulting state and recovery action. Automated widget tests may establish deterministic transitions and assertions; they do not establish representative-human discoverability or workload.

## Failure classes
- FEEDBACK_OCCLUDED
- TARGET_REGRESSION
- FOCUS_LOSS
- FALSE_SUCCESS
- FALSE_FAILURE
- BLIND_RETRY
- AMBIGUOUS_AS_FAILURE
- RECOVERY_DEAD_END
- HISTORY_DISCONTINUITY

## RELATED DOMAIN CHECK
Color owns semantic state differentiation; Layout owns geometry/layer structure; Content owns consequence/recovery language; Type owns rendering integrity; Web owns browser/runtime transfer.

## Next evidence
First rerun the repaired ListTile path through idle/focus/pressed/activation. Once green, add pending/known-failure and ambiguous/reconcile fixtures to the same build identity rather than creating isolated micro-tests.