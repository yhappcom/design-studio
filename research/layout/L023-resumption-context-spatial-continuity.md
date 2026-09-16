# L023 — Resumption-Context Spatial Continuity

Date: 2026-09-16
Evidence: **SYSTEMS PRACTICE / TRANSFER CONTRACT / EXECUTION OPEN**

## RELATED DOMAIN CHECK
- **Interaction:** I019 owns what cognitive/task state must survive interruption.
- **Content:** CD037/CD038 owns labels and information sequence.
- **Color:** C032 audits semantic redundancy, not geometry.
- **Web:** W031/W032 executes route/history/reflow/browser behavior.
- **Type:** T021 custom metrics remain blocked; mature font metrics are required for current geometry transfer.

## Spatial question
When a user resumes a consequential professional task, which context must remain spatially associated so that object, state, consequence and recovery action are not mistaken for neighboring records or stale UI?

## Required association groups
1. record/object identity + key operational attributes;
2. current authoritative/uncertain state + timestamp/source when material;
3. consequence/recovery explanation + the action it governs;
4. conflict pair + comparison/resolution controls;
5. retrieval filters + visible result scope when returning from detail.

## Reflow invariants
At baseline, narrow reflow, actual 200% zoom and localized expansion:
- association order remains object → state → consequence/recovery → action;
- sticky content cannot fully obscure focused recovery controls;
- a control must not migrate visually into a neighboring record's group;
- persistent chrome must not consume the only visible state explanation;
- filter/scope context remains discoverable when returning to a result list;
- horizontal overflow is not accepted for primary recovery content unless the component's semantics genuinely require two-dimensional scrolling.

## Cognitive-load boundary
Reducing simultaneous choices and preserving association are design hypotheses supported by structural analysis, not measured cognitive-load evidence. No workload reduction is claimed without human study.

## Capture requirements
Shared capture ID must include viewport and visual-viewport dimensions, focused element ID/rect, relevant overlay rects, object ID, semantic state ID, action ID, route, locale, font identity and whether the condition is narrow reflow vs actual zoom. Do not collapse these into one “mobile” label.

## HANDOFFS TO OTHER SPECIALISTS
- **Web:** bind capture fields to W031/W032 runtime fixture.
- **Color:** attach C032 cue-independence verdict to the same semantic state ID.
- **Content:** verify long/localized consequence text remains associated with its action.
