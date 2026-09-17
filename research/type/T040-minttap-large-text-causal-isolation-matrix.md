# T040 — MintTap Large-Text Causal Isolation Matrix

Date: 2026-09-18
Purpose: **TRANSFER VALIDATION / CONTRADICTION REVIEW**
Stage: Stage 2 PRACTICE; does not advance T021 drawing gate.

## QUESTION
When MintTap compact UI is repaired, how can Type determine whether remaining failures are genuinely font/type defects rather than composition or semantic pressure?

## SOURCE
Flutter `Text.textScaler` normally inherits the platform/user scaling strategy through `MediaQuery.textScalerOf`; Flutter accessibility guidance explicitly says layouts must have enough room when fonts increase and recommends testing small screens at the largest font setting.

- https://api.flutter.dev/flutter/widgets/Text/textScaler.html
- https://docs.flutter.dev/ui/accessibility/ui-design-and-styling

WCAG 2.2 remains the studio web accessibility baseline. Reflow and text-resize evidence is treated as a Web/Layout acceptance condition, not as permission to alter unfinished glyphs.

- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/#1410-reflow-aa

## PRACTICE — finite causal matrix
For the same build/scenario identity, capture at baseline and enlarged text:

| Variable | Evidence | Type-owned failure only when… |
| --- | --- | --- |
| resolved font | family + fallback chain | unintended fallback or wrong face is reproduced |
| glyph drawing | raster/vector comparison | contour/ambiguity defect survives stable geometry |
| metrics | advance/vertical metrics | metric defect is reproduced independent of container pressure |
| general spacing | sidebearing/advance behavior | repeated class-wide spacing defect remains after drawing gate |
| pair residual | exact pair | only pair-specific defect remains after drawing + general spacing |
| line break | break positions | font metrics/fallback, not required content or container width, causes the change |
| clipping | glyph bounds vs box | glyph/vertical metric is clipped despite adequate container geometry |
| raster | same size/DPR comparison | rendering defect is repeatable without layout overflow |

Negative controls: do not reduce font size, tracking, glyph width, sidebearings or kerning merely to make the compact AppBar fit.

## CRITIQUE
The existing 9.3 px baseline and 47 px enlarged-text overflows scale with available-width pressure. Without a reproduced font-specific cause, this is insufficient evidence for Type intervention. Treating the larger number as proof of bad spacing would violate T021's drawing → general spacing → residual kerning order.

## REPRODUCIBLE VALIDATION
A repaired run may produce one of four outcomes:

1. `TYPE_NOT_CAUSAL`: layout passes and resolved font/raster remain stable.
2. `TYPE_TRANSFER_DEFECT`: fallback/metric/raster defect reproduces independently.
3. `COMPOSITION_PRESSURE`: width/reflow fails while Type evidence is stable.
4. `SEMANTIC_TRUNCATION`: geometry is recovered only by losing required meaning; hand to Content/Layout.

Record build SHA, scenario, viewport, text scaler, locale, resolved fonts, break/clipping result and failure class. Do not claim human readability from automated evidence.

## RELATED DOMAIN CHECK
- Type: T021 gate remains authoritative; T039 attribution model reused.
- Color: state color does not alter Type causality except contrast/raster legibility handoff.
- Layout/Interaction: consumes `COMPOSITION_PRESSURE`; must preserve target/action geometry.
- Web: supplies actual browser font loading/fallback and zoom/reflow transfer evidence after widget smoke.
- Content: owns whether shortening is meaning-equivalent or semantic loss.
- UX: automated fit is not human recognition, comprehension or workload evidence.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives a hard prohibition on Type-as-width-compensation. Web must capture resolved browser fonts before cross-browser Type claims. Content must classify any abbreviation before it is accepted as a geometry repair.

## EVIDENCE BOUNDARY
No repaired MintTap run exists in this study. No T021 drawing PASS, spacing PASS, kerning entry, browser/native transfer or human readability PASS is claimed.
