# C096 — Scroll Motion / Focus State Separation

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Related: I083/L087

## State contract
Keep keyboard focus, selection, candidate, commit, cancel/no-op, recovery and disabled/unavailable independent from viewport/scroll motion. Browser scroll anchoring has no user-facing semantic color of its own.

## Practice
Transfer C095 through I083/L087 at baseline/200%, light/night and forced-colors. Verify the same semantic object retains a recognizable focus cue before/after viewport correction, and that rebuilt/repositioned rows do not inherit stale focus or success paint.

WCAG 2.2 SC 2.4.7 and 1.4.11 remain AA concerns for visible/non-text focus indication; SC 2.4.13 is AAA and may be used as a stronger Studio target, but must not be mislabeled as the AA requirement.

## Failure conditions
- viewport movement is styled as success/recovery;
- focus cue disappears or becomes indistinguishable after scroll correction;
- candidate/commit paint follows ordinal slot instead of semantic object;
- forced-colors collapses focus with selection/candidate state.

## RELATED DOMAIN CHECK
Type T064, Interaction I083, Layout L087, Web W095/W096, Content CD101/CD102 checked. This is transfer validation of existing state architecture under moving geometry.

## Evidence boundary
No rendered forced-colors, independent-engine, calibrated-display, observer or human PASS is claimed.