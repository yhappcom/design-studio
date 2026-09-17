# C066 — Material Feedback-Layer Color Transfer

Evidence class: **TRANSFER VALIDATION / EXECUTED-FAIL CLASSIFICATION**

Run `35255971379` exposed repeated ListTile assertions that ink/background feedback may be hidden by an intervening DecoratedBox. This is directly relevant to semantic color because selected/pressed feedback can be correctly specified yet not visibly rendered on the intended surface.

## SYNTHESIS
Semantic-color validation requires paint/layer ownership as well as token correctness. A state color that cannot reach the visible interaction surface is functionally absent.

## RELATED DOMAIN CHECK
Interaction owns feedback behavior; Layout owns surface containment; Web supplies runtime evidence; Content must provide non-color state meaning; Type is not causal.

## OPEN
After Material-layer repair, rerun selected/pressed states and then continue contradiction, grayscale/color-loss and applicable WCAG 2.2 rendered contrast checks.