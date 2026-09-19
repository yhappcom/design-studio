# C112 — LogMate Search/Retrieval State Separation

Date: 2026-09-20

## RELATED DOMAIN CHECK
I099/L103/T081/W112/CD118 checked. Color communicates state but does not invent query, retrieval or persistence truth.

## State axes
Keep visually and semantically distinguishable where present:
- input focus;
- active/highlighted suggestion or result;
- committed selection/opened record;
- loading/progress;
- empty/no-match;
- retrieval error;
- offline/degraded;
- stale/superseded result;
- filter-active;
- recovery/Retry;
- page-local navigation/current state.

Color is never the sole carrier of these distinctions. `No results` is not an error color by default; offline is not equivalent to invalid query; active option is not selected/opened record; successful retrieval is not persistence success.

## TRANSFER VALIDATION PLAN
With L103/W112 capture semantic state IDs and rendered boundaries in light/night/forced-colors at baseline and enlarged/text-spacing states. Verify stale loading/error paint clears only when authority changes, and focus remains distinguishable from active/selected/current states.

## FAILURE CONDITIONS
Hue-only active result; generic red for zero results; brand accent collides with focus/selection; stale error survives successful newer request; forced-colors erases the only result-state distinction; status paint implies success before I099/W112 evidence.

## EVIDENCE BOUNDARY
No production palette, rendered search runtime, forced-colors/cross-browser/device, calibrated-display, glare/night or representative-human PASS is claimed.