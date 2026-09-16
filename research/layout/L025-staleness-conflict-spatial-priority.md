# L025 — Staleness / conflict spatial priority

Evidence: **SYSTEMS PRACTICE / TRANSFER VALIDATION OPEN**

## RELATED DOMAIN CHECK
I021 defines authority/freshness truth; C034 owns cue survival under forced colors; W033 owns actual restoration/runtime evidence; CD039 owns state wording; T021 blocks custom metric freezing.

## Spatial problem
A resumed screen can be internally tidy yet unsafe if restored/stale state is visually indistinguishable from authoritative current state. L024's resumption context budget is therefore extended with authority/freshness priority.

## Priority stack
When freshness is not established, the visible reading/action order should preserve:
1. object identity;
2. current certainty / freshness status;
3. consequence or conflict;
4. safe primary action;
5. history/detail/reconciliation path;
6. secondary metadata.

The exact visual layout may vary, but a stale/conflict indicator must not be spatially detached from the object/state it qualifies.

## Stress matrix
Evaluate at baseline, 320 CSS px reflow, actual 200% zoom, long localization and reduced visual viewport where executable. Record:
- identity-to-status distance/association;
- status-to-action association;
- action reachability;
- sticky/fixed overlap rectangles;
- whether secondary metadata displaces certainty/consequence;
- whether conflict comparison remains reachable without horizontal two-column dependence.

## Critique rules
- Do not solve density by hiding certainty or consequence behind optional disclosure while leaving risky action prominent.
- Do not infer 200% zoom behavior from a 320px viewport.
- Do not infer cognitive salience from DOM order or geometry alone.
- A visible focus ring can still fail if author-created content entirely obscures the focused component; geometry and Color remain separate evidence.

## Evidence boundary
No browser geometry, actual zoom, keyboard viewport, AT, physical-device, discoverability, workload or human task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Web captures actual rectangles and restoration provenance. Interaction supplies authority state and enabled actions. Content supplies last-known/current/conflict semantics. Color tests redundant state cues. Type supplies final metrics only after T021.