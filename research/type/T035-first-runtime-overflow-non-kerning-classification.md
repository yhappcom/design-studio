# T035 — First Runtime Overflow: Non-Kerning Classification

Evidence class: **TRANSFER VALIDATION / EXECUTED-FAIL CLASSIFICATION**

Run `35255971379` produced 9.3 px baseline and 47 px enlarged-text horizontal RenderFlex overflows. No evidence identifies a glyph drawing, font metric, pair-spacing or residual kerning defect.

## STUDIO JUDGMENT
Classify these as composition pressure until a Type-specific defect is demonstrated. Do not use tracking/kerning reduction, smaller text or glyph distortion to recover space. T021 drawing→spacing→kerning gate remains unchanged.

## RELATED DOMAIN CHECK
Layout owns recomposition; Content owns truth-bearing strings; Web supplies runtime identity; Color/Interaction must survive the repair.

## OPEN
After spatial repair, rerun to inspect actual line breaks, fallback and raster behavior. Native/browser/AT/human Type evidence remains open.