# C084 — Restored Versus Focused State Separation

## Purpose
Extend C083 across I071 Undo restoration. A semantic object can become visible/restored without becoming the current focus owner.

## RELATED DOMAIN CHECK
I071 supplies state truth; L075 supplies geometry; W083 supplies runtime proof; CD089 supplies wording; T052 supplies rendering constraints. This is cross-domain TRANSFER VALIDATION, not a new interaction policy.

## State matrix
Keep these axes independent: restored visibility, current focus owner, recovery-control availability, selection/insertion, enabled/disabled, hidden/visible, failure/superseded. Required cases include `O restored + F focused`, `O restored + Undo control focused`, and only when explicitly declared `O restored + O focused`.

## Practice / critique
FAIL if restoration highlight is visually indistinguishable from keyboard focus; if both old fallback and restored object appear focused; if a transient success accent masks the actual focus indicator; or if forced-colors collapses focus and restoration into one color-only signal.

Focus Visible and Focus Not Obscured remain AA floors. Focus Appearance in WCAG 2.2 is AAA; its size/contrast model is useful as a stronger critique target but must not be mislabeled as an AA requirement.

## Reproducible validation
For I071 scenarios capture semantic owner, paint owner, focused/unfocused pixel/state change, non-color cue, forced-colors result and accessible identity at baseline and 200%. Repeat after Undo, after status expiry and after a second action.

## Evidence boundary / OPEN
No rendered C084, forced-colors independent-engine, calibrated-display, observer or human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives any state-collapse finding; Layout receives focus-indicator geometry conflicts; Web proves actual browser paint/semantics; Content avoids wording that equates restoration with focus; Type protects text legibility under state decoration.