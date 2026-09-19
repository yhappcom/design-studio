# C110 — Non-drag reorder state salience

## PURPOSE
Transfer I097/L101 into Color without using color to carry reorder meaning.

## RELATED DOMAIN CHECK
T079, I097/L101, W109 and CD115 checked. This is TRANSFER VALIDATION of reorder states under the existing C109 semantic-state discipline.

## STATE AXES
Keep distinct:
- item selected/action context open;
- move action available/unavailable;
- proposed destination;
- moved/locally committed;
- persistence pending/failure;
- saved/synced only when evidenced;
- Undo available/restored;
- keyboard/pointer focus.

Brand accent is subordinate to these functional distinctions.

## PRACTICE / CRITIQUE
Test light, night and forced-colors with first/middle/last moves, boundary-disabled actions, pending save, failure, retry and Undo. Meaning must remain available through text/structure/state, not hue alone.

Reject:
- green immediately after a visual move when persistence is unresolved;
- red for a normal boundary-disabled action;
- selection and focus sharing an indistinguishable treatment;
- proposed destination and committed order using the same state treatment when both can coexist;
- quiet-brand styling that suppresses recovery/error visibility.

## SYNTHESIS
Reorder is a useful adversarial test of SC-C Quiet Functional Boundary: low decorative chroma is compatible with strong functional state clarity. Color should reinforce transaction truth, never invent it.

## HANDOFFS
L101 provides boundaries/target geometry; I097 provides state truth; CD116 verbalizes state; W110 validates used rendering and stale-state cleanup; T079 supplies realistic text/fallback conditions.

## OPEN
No rendered production, forced-colors cross-engine/device, calibrated-display, glare/night observer or human evidence is claimed.