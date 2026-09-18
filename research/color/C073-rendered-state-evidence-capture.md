# C073 — Rendered State Evidence Capture

Date: 2026-09-18
Stage: 3 PRACTICE
Purpose: TRANSFER VALIDATION after I060 Material repair

## Problem
MintTap has direct evidence that configured interaction-state paint can be hidden by layer ownership. Color therefore needs an evidence packet based on rendered surfaces, not theme/token declarations.

## PRACTICE
For each repaired component capture the same geometry in idle, focus, pressed and selected states and record:
- semantic token/value used;
- actual paint owner/surface;
- visible foreground/background/border/focus treatment;
- non-color cue carrying the state;
- financial polarity, certainty/finality and availability flags present simultaneously;
- contrast calculation input from the rendered/implemented colors where technically available;
- whether state layering masks another semantic axis.

Contradiction matrix must include selected+negative, focus+unavailable, positive-income+negative-return, zero+unavailable, estimated/final, partial/complete and gross/net.

## CRITIQUE
A screenshot alone cannot establish accessible meaning, and source token inspection cannot establish visibility. Acceptance therefore needs both implementation provenance and rendered-state evidence. Anti-aliasing/device reproduction and human perception remain separate evidence layers.

## REPRODUCIBLE VALIDATION
Repeat the state capture after I060 repair under baseline and enlarged-text layouts. A layout recomposition must not move state indication onto a clipped/occluded surface. Run non-color inspection by checking that labels/icons/shape/border/position semantics preserve critical meaning without relying solely on hue.

## WCAG 2.2
Use WCAG 2.2 as the current W3C baseline. Apply relevant contrast/focus/non-color criteria to the visible component, not merely declarations. Human perception and calibrated-display claims remain OPEN until measured appropriately.

## RELATED DOMAIN CHECK
- Type: no Type compensation is allowed for spatial fit.
- Layout: L064/L063 determine repaired geometry and possible occlusion.
- Interaction: I060 supplies paint-owner and focus/pressed/selected behavior.
- Web: W073 must re-check the state surfaces in served browser runtime.
- Content: CD078 supplies explicit semantic labels so color is never the sole carrier.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives any missing/hidden feedback state. Layout receives occlusion/clipping. Content receives any color-only semantic dependency. Web receives the exact contradiction matrix for browser transfer.

## Evidence boundary
No repaired Color PASS, calibrated-display, observer or human PASS is claimed.
