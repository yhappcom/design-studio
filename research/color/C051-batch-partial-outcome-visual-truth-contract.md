# C051 — Batch Partial-Outcome Visual Truth Contract

Evidence purpose: **STAGE 3 PRACTICE / TRANSFER VALIDATION**. Extends C050 from one deferred operation to a batch whose members can resolve differently.

## RELATED DOMAIN CHECK
- **Type:** T021 remains provisional; batch identifiers/counts use mature fallback until drawing repair passes.
- **Layout/Interaction:** I038 owns member-level outcome truth; L042 owns batch/member hierarchy and recovery geometry.
- **Web:** W051 owns runtime evidence for partial acknowledgement, retry and reconstruction.
- **Content:** CD057 owns batch/member semantic wording.
- **UX:** deterministic state discrimination is not human comprehension evidence.

## Problem
A batch-level green success, red failure, progress completion or disabled Retry can falsely imply that every member has the same authoritative outcome. Batch chrome must not overwrite member truth.

## Visual state contract
Distinguish without hue alone:
- `batchPending`
- `batchMixedOutcome`
- `batchOutcomeUnknown`
- member `confirmed`
- member `denied`
- member `failedKnown`
- member `outcomeUnknown`
- member `retryEligible`
- member `retryBlocked`

A batch may display aggregate progress only when member-level exceptions remain discoverable and consequential action is bound to the relevant member state.

## Cue precedence
1. member authoritative consequence;
2. member certainty/recovery eligibility;
3. batch aggregate summary;
4. selection/focus/hover;
5. decorative/brand treatment.

Selection, focus, brand accent, progress fill or success color may not visually promote an unknown/failed member into confirmed state.

## Transfer stress
Evaluate normal theme, grayscale, forced colors, print/export, selected-row overlay, dense list, 200% text and localized labels. A mixed batch must survive loss of background fill and hue.

## Failure conditions
- one success color implies whole-batch success despite unknown members;
- red batch chrome implies every member failed;
- retry styling does not distinguish safe member retry from batch replay;
- aggregate percentage hides denied/unknown consequential members;
- print/export loses member-level outcome distinctions.

## Evidence boundary
No rendered C051 artifact, observer study, CVD/low-vision validation, physical print/display or Color Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
I038/L042 define the state/action and hierarchy consumed here; W051 must capture rendered cue state; CD057 must preserve equivalent non-color semantics.