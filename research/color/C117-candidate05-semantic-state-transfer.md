# C117 — Candidate 05 semantic-state transfer

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION / RUNTIME OPEN**

## Question
Does Candidate 05's warm-ivory / continuous-sheet / scarce-mint language remain semantically reliable when real focus, selection, error, pending, offline, recovery and evidenced-success states are introduced?

## RELATED DOMAIN CHECK
Type T086, I103/L107, W116 and CD122 checked. Candidate 05's static owner-review PASS does not contain consequence-bearing runtime states, native high-contrast, Web forced-colors or human evidence.

## SOURCE / boundary
WCAG 2.2 remains the accessibility baseline. WCAG target-size and focus requirements are separate from Flutter's platform recommendations; Color does not infer WCAG conformance from Flutter guideline tests. Native high-contrast and Flutter Web forced-colors remain different evidence classes.

## PRACTICE matrix
On the same coded Candidate 05 build, inject only states authorized by Interaction:
- focus;
- current destination;
- selected period/result;
- validation/error;
- pending;
- offline/degraded;
- recovery/Retry/Undo;
- evidenced local save / evidenced sync.

Run light and dark first, then supported native high-contrast, then Flutter Web forced-colors where Web scope applies. At each state capture semantic ID, foreground/background/boundary role, non-color cue, focus geometry and any reflow from T086/L108.

## CRITIQUE / failure conditions
- FAIL if mint simultaneously means brand, focus, selection and success with no independent boundary.
- FAIL if `pending` or visual movement is painted as success before authoritative evidence.
- FAIL if error/offline/recovery is reduced below brand salience to keep the surface quiet.
- FAIL if state identity disappears in high-contrast/forced-colors or after text reflow.
- FAIL if the warm ivory canvas is treated as a semantic state rather than a surface role.

## Evidence boundary
This is not a calibrated-display, glare/night, observer, physical-device or human-perception PASS. It defines the next reproducible runtime test.

## HANDOFFS TO OTHER SPECIALISTS
Interaction supplies state truth; Content supplies state language; Layout protects state ownership under reflow; Web records platform/browser provenance. Type changes may trigger Color revalidation when boundaries move.