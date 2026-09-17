# C067 — Visible State-Surface Acceptance Gate

Evidence class: **SOURCE + TRANSFER VALIDATION PLAN**

## PURPOSE
Convert C066's paint/layer failure into a rendered Color acceptance gate after I054 repair.

## SOURCE
Flutter's InkWell/Ink documentation establishes that ink is painted on Material and may be obscured by an intervening opaque decoration. Therefore a semantic state color is not operationally present merely because a token/value exists; the intended state must reach the visible surface.

## PRACTICE
For default, hover/focus where applicable, pressed, selected, disabled, positive, negative, zero, estimated/final and partial/unavailable states: capture declared semantic role, resolved color, actual visible surface, non-color cue, and rendered contrast where WCAG 2.2 applies. Run the existing high-income + negative-total-return + partial + KRW contradiction fixture after spatial/Material repair.

## CRITIQUE
Reject `TOKEN_PASS / RENDER_FAIL`: a correct token hidden below an opaque layer is a functional failure. Also reject color-only state meaning. Brand, financial polarity, certainty/finality and availability remain independent axes.

## REPRODUCIBLE VALIDATION
Acceptance requires: no hidden feedback layer; polarity and availability recoverable without hue; selected/pressed state visibly distinct on the intended surface; applicable text/non-text contrast checked against WCAG 2.2; and no semantic-axis collision introduced by repair.

## RELATED DOMAIN CHECK
I053/I054 owns action/paint-layer behavior. L058 owns containment/recomposition. T036 checks rendering after repair. CD072/CD073 supplies explicit semantic language. W067 will bind all evidence to one runtime identity.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives any state that is technically painted but behaviorally ambiguous. Layout receives any surface/containment rule that changes layer ownership. Content receives cases where non-color redundancy is missing.

## OPEN
No repaired rendered evidence yet. Forced/high-contrast, independent browser/device, calibrated display and representative observer evidence remain OPEN.