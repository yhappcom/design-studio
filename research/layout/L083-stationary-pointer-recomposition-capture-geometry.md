# L083 — Stationary-pointer recomposition and capture geometry

Status: PRACTICE / TRANSFER VALIDATION OPEN

## Question
When 200% zoom/recomposition, wrapping, sticky surfaces, or row replacement moves targets under an active pointer, can geometry remain truthful without converting layout motion into user pointer intent?

## SOURCE / SYNTHESIS
Current Pointer Events defines boundary events caused by layout changes for a stationary pointer. This makes a critical distinction for reorder UI: `target geometry moved` is not `pointer moved`. WCAG 2.2 remains the accessibility baseline; SC 2.5.8 target-size acceptance and SC 2.4.11 Focus Not Obscured remain separate from the stronger Studio requirement that recomposition not fabricate a destination.

## PRACTICE
For each I079 scenario capture before/after:
- viewport and effective text/zoom condition;
- pointer coordinates and whether they changed;
- semantic object/candidate IDs;
- capture/gesture owner;
- source, candidate, focus and recovery rectangles;
- scroll offsets;
- sticky/safe-area intersections;
- wrapping/row-height changes;
- projection hash and commit result.

Run baseline and 200% twice. Include stationary pointer + row height growth, sticky header intrusion, candidate crossing due solely to reflow, row rebuild/removal, cancel, valid commit and non-drag alternative.

## CRITIQUE
FAIL if layout motion alone changes committed destination, if preview geometry implies a new candidate without semantic resolution, if cancellation leaves a ghost target, if the correct semantic owner becomes obscured, or if target-size acceptance is claimed without identifying the applicable SC 2.5.8 clause.

## RELATED DOMAIN CHECK
Type T060: necessary strings may wrap; provisional Type metrics must not be frozen into geometry. Color C091: preview/cancel state must survive recomposition. Interaction I079 owns semantic pointer-stream truth. Web W091/W092 owns served event provenance. Content CD097/CD098 owns semantic feedback, not spatial inference.

## HANDOFFS TO OTHER SPECIALISTS
Web should correlate boundary-event/event-target evidence with these rectangles. Interaction should reject any destination inferred only from reflow. Color/Content should clear stale preview semantics after cancellation/rebuild.

## OPEN
No actual LogMate runtime, independent engine, physical touch/pen, AT or human usability PASS is claimed.