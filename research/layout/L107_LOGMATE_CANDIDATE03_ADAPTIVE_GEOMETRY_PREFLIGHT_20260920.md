# L107 — LogMate Candidate 03 Adaptive Geometry Preflight — 2026-09-20

Status: **TRANSFER VALIDATION PLAN / STAGE 3 NOT PASSED**

## Purpose
The 390×844 Candidate 03 render is static review evidence, not a geometry contract. Define what must survive real Flutter text/display scaling, safe areas and narrow/adaptive conditions.

## SOURCE
Flutter SafeArea/MediaQuery exposes window size, accessibility text scaling, high contrast, assistive-service state and display features such as hinges/folds. Flutter's nonlinear TextScaler means layout must not assume one global linear scale factor.

Sources:
- https://docs.flutter.dev/ui/adaptive-responsive/safearea-mediaquery
- https://docs.flutter.dev/release/breaking-changes/android-14-nonlinear-text-scaling-migration

## PRACTICE — protected relationships
Preserve, rather than fixed coordinates:
- identity ↔ Current Period;
- Search control ↔ search purpose;
- Recent row identity ↔ Date/Flight/Route/Block values;
- Activity period control ↔ corresponding values;
- Totals label ↔ total;
- command action ↔ its target and consequence.

Adaptation order: intrinsic growth → local redistribution → row growth/wrap → secondary-detail transfer → justified local scrolling → recoverable truncation last.

## CRITIQUE / failure conditions
FAIL if text/targets shrink to preserve the screenshot; if SafeArea/display-feature changes obscure controls; if scaled rows detach labels from values; if Recent comparison axes become ambiguous; if focus/recovery targets are obscured; or if command rail order changes without semantic reason.

## Reproducible validation
Capture geometry at baseline, narrow window, maximum platform text scaling, text-spacing stress where applicable, forced font fallback, and representative safe-area/display-feature conditions. Record target rectangles and semantic ownership, not screenshots alone.

## RELATED DOMAIN CHECK
- Type: T085 supplies actual scaling/fallback measurements.
- Color: C116 state boundaries must remain attached after reflow.
- Interaction: I103 supplies focus/route/action ownership.
- Web: W116 captures Flutter Web viewport/browser transfer separately.
- Content: CD122 keeps canonical strings immutable-first.

## HANDOFFS TO OTHER SPECIALISTS
Type should report line/intrinsic growth rather than compensate typographically. Interaction/Web should capture focus and target rectangles after every recompose. Content should treat geometry-driven shortening as a last resort requiring semantic review.

## OPEN
No narrow/scaled/device/foldable/physical-device or human scanning PASS is claimed.