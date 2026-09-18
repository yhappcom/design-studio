# C085 — Restoration, Recency, and Agency State Separation

Date: 2026-09-18
Stage: Stage 3 PRACTICE
Purpose: TRANSFER VALIDATION from I072/L076.

## RELATED DOMAIN CHECK
I072 separates transaction restoration from newer user agency; L076 measures the chosen locus; W084/W085 must verify actual browser paint; CD090/CD091 verbalize restoration without inventing focus; T053/T054 owns rendering, not semantic-state compression.

## SOURCE
WCAG 2.2 remains baseline. Focus Visible and Focus Not Obscured are accessibility floors; Focus Appearance is AAA. Color must not be the sole carrier of state meaning.

## STATE MODEL
Keep these axes independent:
- restored/not-restored;
- current focus owner;
- selection;
- recovery available/unavailable/superseded;
- changed object;
- newer-agency object;
- visible/hidden/disabled;
- success/failure/no-op.

A restored object may be visible and recently changed while another object or Undo control owns focus. A short-lived restoration cue must never masquerade as focus.

## PRACTICE / CRITIQUE
Construct state tuples for immediate Undo, intervening focus, intervening operation, superseding Reset and stale Undo rejection. For each tuple map semantic token → paint owner → visible surface → non-color cue → accessible meaning.

FAIL patterns:
- restored highlight visually indistinguishable from focus;
- old and new focus owners simultaneously appear focused;
- unavailable/superseded recovery encoded only by reduced opacity;
- success color applied to stale/no-op recovery;
- forced-colors removes the only distinction between restored and focused.

## REPRODUCIBLE VALIDATION
When runtime exists, execute light/night/forced-colors in primary and independent engines using the same I072 scenario IDs. Capture computed/visible state and focus owner; do not infer PASS from token definitions.

## EVIDENCE BOUNDARY
No rendered C085, forced-colors, independent-engine, calibrated-display, observer or human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Layout supplies geometry; Interaction supplies state truth; Content supplies non-color semantics; Web supplies runtime; Type must not compensate state ambiguity typographically.