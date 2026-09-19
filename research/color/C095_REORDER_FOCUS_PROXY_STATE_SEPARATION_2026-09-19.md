# C095 — Reorder Focus / Proxy State Separation

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Related: I082/L086

## State axes
Keep these visually and semantically independent: keyboard focus, selection, pressed/drag preview, proxy representation, candidate destination, autoscroll-active, committed move, cancellation/no-op, recovery eligibility, disabled/unavailable.

A drag proxy is not a focus state. Candidate styling is not success styling. Recycled/rebuilt rows must not inherit state merely from ordinal/index reuse.

## Practice matrix
Evaluate light, night and forced-colors for I082 scenarios at baseline and 200%. Record non-color cues for focus, candidate, commit/cancel and disabled/unavailable states. Check contrast of focus treatment when affected by author overlays; WCAG 2.2 Understanding 2.4.11 notes that overlays can also create non-text contrast problems.

## Failure conditions
- proxy elevation/accent impersonates keyboard focus;
- candidate and committed states are distinguishable only by hue;
- rebuilt row at reused index inherits stale focus/selection/recovery paint;
- forced-colors collapses focus and drag/candidate state into an ambiguous cue;
- obscuring overlay leaves the focused interaction locus visually indeterminate.

## Evidence boundary
No rendered forced-colors, independent-engine, calibrated-display, observer or human PASS is claimed.