# T085 — LogMate Candidate 03 Flutter Text-Scaling Transfer — 2026-09-20

Status: **TRANSFER VALIDATION PLAN / T021 GATE UNCHANGED**

## Purpose
Candidate 03 is now owner-review eligible as a static concept, but production Type evidence is still open. This study converts its actual Flutter surface into a falsifiable Type transfer plan without using kerning or compressed drawing to preserve the 390×844 composition.

## SOURCE
Flutter documents Android 14 nonlinear font scaling up to 200% and recommends migration from scalar `textScaleFactor` assumptions to `TextScaler`; custom layout dimensions must not assume a single linear multiplier. Flutter also recommends that UI remain usable at very large text/display scaling.

Sources:
- https://docs.flutter.dev/release/breaking-changes/android-14-nonlinear-text-scaling-migration
- https://docs.flutter.dev/release/breaking-changes/deprecate-textscalefactor
- https://docs.flutter.dev/ui/accessibility

## PRACTICE — Candidate 03 corpus
Test the actual visible roles, not synthetic lorem ipsum:
- proportional: Current Period, Search, Recent Flights, Activity, Totals, Add Flight, View Logbook;
- operational mono candidates: Recent Date / Flight / Route / Block only;
- proportional tabular numerics: Current Period / Activity / Totals values;
- canonical date fixture: `09/2026`.

For each role capture: requested family, resolved family/fallback, unscaled size, `TextScaler` result, line count, intrinsic width, clipping/ellipsis, baseline/row growth and adjacent protected relationship.

## CRITIQUE / failure conditions
FAIL if any Candidate 03 geometry is preserved by:
- disabling or arbitrarily clamping user text scaling for ordinary text;
- negative tracking or glyph narrowing;
- shortening canonical wording solely for fit;
- extending mono into summary numerics merely to reduce width;
- opening kerning before T021 drawing and general-spacing gates pass.

A layout recompose or taller row is preferable to falsifying Type semantics.

## Reproducible validation
Run the same coded fixture at default scaling and platform maximum accessibility text scaling, including Android nonlinear scaling. Repeat with forced fallback. Compare resolved glyph/family evidence and geometry; do not infer the font from CSS/Flutter style declarations alone.

## T021 gate
Unchanged: bounded drawing repair → critique/PASS → general spacing → residual kerning. Candidate 03 does not justify bypassing this sequence.

## RELATED DOMAIN CHECK
- Type: T021/T084 retained; this is TRANSFER VALIDATION, not a new drawing gate.
- Color: C115 state salience must survive row/label growth.
- Layout/Interaction: I102/L106 own semantic relationship preservation when text grows.
- Web: W115 owns runtime provenance; Flutter Web semantics/runtime evidence is distinct from native Flutter evidence.
- Content: CD121 canonical strings remain immutable-first stress inputs.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web should record actual `TextScaler`/resolved-font conditions in the shared packet. Content should not abbreviate labels until Type/Layout evidence proves semantic wording itself is the blocker. Color should recheck focus/state boundaries after geometry changes.

## OPEN
No production family/fallback, scaled Candidate 03 render, AT readability or human readability PASS is claimed.