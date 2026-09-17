# C057 — Semantic State Acceptance Matrix

Status: STAGE 3 PRACTICE / TRANSFER VALIDATION SPEC

## PURPOSE
Turn C055/C056 into an executable state matrix rather than another palette study.

## SOURCE
WCAG 2.2/WAI guidance requires information not depend on color alone and applicable text/non-text contrast to survive alternate presentation. Flutter release guidance likewise calls for contrast, grayscale/color-vision checks and large-scale usability.

## PRACTICE MATRIX
Shared W056 scenarios cross four independent axes: identity/brand; outcome polarity; certainty/finality; availability/integrity. Exercise high-income + negative-return, zero, estimated/final ROC, partial/unavailable, KRW/USD, light/dark, grayscale and high/forced-contrast where supported.

Acceptance requires a non-color carrier for every material state; brand mint never means gain/success/final/complete by itself; polarity remains explicit in text/sign; estimated/final and partial/unavailable remain distinguishable without hue; contrast is measured on rendered foreground/background pairs rather than token names.

## CRITIQUE
A palette can pass contrast while failing semantics. Conversely, loss of brand hue in forced colors is not a failure if identity and state remain operable and understandable.

## RELATED DOMAIN CHECK
T026 supplies string/render pressure. L047/I043 preserve adjacency and focus/target behavior. W056 owns runtime capture. CD062 supplies explicit state language.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture rendered colors/modes with exact scenario identity. Content should reject color-referential instructions. Layout should preserve state carrier adjacency after reflow.

## OPEN
No calibrated-display, cross-browser/device, observer or representative-human evidence is claimed.