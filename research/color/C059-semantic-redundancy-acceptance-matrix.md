# C059 — Semantic Redundancy Acceptance Matrix

Status: STAGE 3 PRACTICE / EXECUTION PREPARATION  
Date: 2026-09-17

## PURPOSE
Turn C058's runtime oracle into a bounded acceptance matrix for real financial-product transfer without adding another isolated palette study.

## RELATED DOMAIN CHECK
Type T028 supplies the exact string/rendering pressure. L049/I045 own adjacency and behavioral truth. W058 owns runtime evidence identity. CD064 owns the semantic distinction between outcome, certainty, availability and basis.

Analytical purpose: TRANSFER VALIDATION preparation.

## SOURCE
WCAG 2.2 remains the current W3C baseline used by the studio. Relevant checks include Use of Color, text/non-text contrast, focus visibility/obscuration and target-related presentation. Color evidence must therefore preserve meaning without color-only dependence and must distinguish normative contrast checks from studio diagnostic transforms such as grayscale.

## PRACTICE MATRIX
Execute the Cartesian-risk cases below, not every possible combination:

| Case | Outcome | Certainty | Availability | Basis | Required non-color cue |
| --- | --- | --- | --- | --- | --- |
| A | positive | final | complete | after-tax | signed value + explicit label |
| B | negative | final | complete | after-tax | minus sign + explicit label |
| C | zero | final | complete | after-tax | numeric zero + explicit label |
| D | positive income + negative total return | mixed | complete | after-tax | separate metric labels; no shared success badge |
| E | unknown | estimated | complete | gross | `Estimated` text/state cue |
| F | unknown | final | partial | net | `Partial data` cue independent of polarity |
| G | unknown | unknown | unavailable | n/a | `Unavailable`; never numeric zero |
| H | positive/negative | final | complete | tax adjustment | explicit refund/additional-tax consequence |

Brand mint is permitted as brand/action emphasis only when it does not imply economic success or finality.

## CRITIQUE / FAILURE CLASSES
Retain C058 classes: COLOR_ONLY, AXIS_COLLISION, BRAND_AS_SUCCESS, POLARITY_AS_CERTAINTY, AVAILABILITY_AS_ZERO, CONTRAST, FORCED/HIGH-CONTRAST LOSS, ADJACENCY_BREAK.

New acceptance condition: every semantic distinction above must remain recoverable from text/sign/shape/structure when hue is removed. Grayscale is a diagnostic, not a WCAG conformance test.

## VALIDATION CONTRACT
Use the same W058 runtime identity as T028/L049/I045/CD064. Capture declared token pair, rendered context, applicable WCAG contrast calculation, non-color cue, high/forced-contrast behavior where supported, and screenshot/semantics evidence. Do not infer calibrated-display, observer or human discrimination results.

## HANDOFFS
Layout/Interaction receives any adjacency/focus loss; Type receives raster/text contrast context only when typography is causal; Content receives semantic cue omissions; Web packages runtime artifacts.

## EVIDENCE BOUNDARY
No Stage 3 PASS, rendered product PASS, cross-browser/device, calibrated-display, observer or representative-human PASS is claimed.