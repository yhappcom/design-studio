# C028 — Focus Occlusion Conformance Ledger

Evidence type: SOURCE / SYNTHESIS / TRANSFER VALIDATION / OPEN

## RELATED DOMAIN CHECK
T022 custom drawing remains excluded. L018 supplies overlap geometry; I013 supplies state/action truth; W025 supplies runtime; CD032 supplies non-color semantics. This study does not claim UX comprehension.

## Source correction and baseline
WCAG 2.2 is the studio baseline. SC 2.4.11 Focus Not Obscured (Minimum) is AA and requires a focused component not be entirely hidden by author-created content. SC 2.4.12 is the stronger AAA condition. SC 2.4.13 Focus Appearance is AAA. Therefore C027 must not treat 2.4.13 as an AA gate.

Primary source: W3C WAI, What's New in WCAG 2.2 and WCAG 2 Overview.

## Executable ledger design
For every semantic state in W024/W025, record: theme, forced-colors mode, focused control, authored overlay/sticky layer, overlap classification (none/partial/entire), focus indicator survival, text/state survival without hue, and recovery action visibility. AA failure is triggered when author-created content entirely hides the focused component; stricter full-visibility and indicator-area checks remain separately labelled AAA/studio-quality targets.

## Risk model
A contrast calculation cannot prove non-occlusion. Forced-colors survival cannot prove focus visibility. Geometry and color evidence must be joined by the same runtime capture ID. Any result without both is incomplete.

## Current result
**C028 LEDGER CONTRACT COMPLETE / RUNTIME EXECUTION OPEN.** This corrects criterion-level classification and creates a reproducible evidence join for C027/L018/W025.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web must emit overlap classification and capture ID. Content supplies state/action identifiers. UX integration should treat AA conformance, AAA enhancement and human salience as different evidence classes.