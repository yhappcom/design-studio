# T063 — Edge-autoscroll transfer corpus

Status: STAGE 2 PRACTICE / DOWNSTREAM TRANSFER CORPUS
Date: 2026-09-19

## Purpose
Capture the string/rendering pressure created by I081/L085/CD100 without changing the current Type gate order.

## Corpus extension
Later transfer set includes Move up/down, Move to…, Cancel, Undo move, first/previous/next/last, boundary/no-op/recovery candidates, `1/35`…`35/35`, EN/KO field labels, and operational abbreviations DEP/ARR, PIC, SIC/FO, PICUS, SPIC, PF/PM, T/O/L/D.

## Gate discipline
T021 bounded R1 drawing remains upstream. Widths/sidebearings stay frozen and kerning stays OFF until drawing and then general-spacing gates permit progression. Long Korean strings, compact controls, edge-autoscroll geometry or 200% wrapping are not evidence that immature drawing should be compressed or repaired with kerning.

## TRANSFER VALIDATION PLAN
After T021 closure, render this corpus against the repaired candidate and mature fallback under baseline/200%, actual browser fallback and EN/KO content. Attribute a failure to Type only when glyph, metric, fallback or raster evidence reproduces it.

## RELATED DOMAIN CHECK
I081 defines semantic behavior; L085 geometry; C094 state encoding; W094 runtime; CD100 wording. Type receives these as downstream constraints and does not redefine them.

## OPEN
No T021 closure, spacing/kerning entry, production custom-font, browser/native breadth, AT or human recognition PASS.