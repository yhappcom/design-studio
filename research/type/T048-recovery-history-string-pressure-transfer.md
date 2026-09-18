# T048 — Recovery-History String Pressure Transfer

Status: **STAGE 2 PRACTICE / T021 GATE UNCHANGED**  
Purpose: **TRANSFER VALIDATION PREPARATION** for CD085/I066 recovery strings.

## RELATED DOMAIN CHECK
CD085 introduces object/scope/position/Undo strings. I066 defines transaction truth. L070 owns density/reflow. C079 owns state visibility. W078 owns browser rendering. Type must not use unfinished drawing/spacing/kerning to absorb their pressure.

## Transfer corpus
When semantics are fixed, test mature fallback first with: aviation labels `DEP`, `ARR`, `PIC`, `SIC/FO`, `PICUS`, `SPIC`; positions `1/35`, `9/35`, `10/35`, `34/35`, `35/35`; object+position+Undo; relational feedback; unavailable/superseded recovery; long localized labels and punctuation.

Capture resolved family/fallback, glyph coverage, line breaks, clipping, numeral alignment and raster at baseline/200% text. Attribute a defect to Type only with reproduced glyph/metric/fallback/raster evidence.

## Gate
T021 remains drawing → general spacing → residual pair-specific kerning. R1 drawing is still open, widths/sidebearings frozen and kerning OFF. Recovery density cannot justify font-size, tracking, width or kerning compensation. Product evidence continues with mature fallback until T021 permits transfer.

## CRITIQUE
Transaction-history strings increase numeral/punctuation repetition and wrap pressure, but those are not themselves Type defects. Prematurely narrowing glyphs would freeze Layout around provisional metrics and corrupt the causal diagnosis.

## OPEN
No T021 closure, repaired-raster PASS, custom-font product/browser/native, multilingual or human recognition PASS.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives composition-pressure failures; Content receives rendering evidence without semantic shortening authority; Web receives fallback/font-loading fields; Interaction receives no change to transaction semantics.
