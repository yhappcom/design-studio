# C114 — Pre-runtime semantic-salience oracle

Date: 2026-09-20
Purpose: PRACTICE / TRANSFER VALIDATION planning after C113.

## RELATED DOMAIN CHECK
T082/T083, I100/L104, W113 and CD119 checked. Reuse the five shared workflows; do not open another palette exercise.

## State-separation matrix
The implementation must keep these meanings distinguishable without requiring hue alone: focus, current destination, selection, invalidity, ambiguity/unknown outcome, offline/degraded capability, pending persistence, persistence failure, evidenced local success, evidenced sync success, stale/superseded data, recovery/Undo.

## Falsification rules
FAIL if: current=focus; active search result=committed selection; zero results=error; offline=save failure; retry-start=success; local commit=synced; decorative/brand accent outranks consequence-bearing state; forced colors removes the only state boundary; night treatment reduces a required state below its functional hierarchy.

Test the same semantic IDs through baseline, enlarged/text-spacing, light/night and forced-colors. Color values may change; semantic rank and non-color boundary must survive.

## WCAG boundary
WCAG 2.2 remains the current W3C baseline. Passing isolated contrast calculations is not a WCAG conformance claim; conformance is broader than techniques or individual checks.

## HANDOFFS TO OTHER SPECIALISTS
Interaction supplies authoritative states; Content supplies verbal state truth; Layout supplies boundary/occlusion geometry; Web captures rendered state and forced-colors provenance; Type fallback must not erase non-color cues.

## Evidence boundary
No Stage 3, production palette, forced-colors/browser/device, calibrated-display, glare/night, AT or human PASS is claimed.