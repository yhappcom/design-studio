# T044 — LogMate Ledger Compact-Header Transfer

Date: 2026-09-18
Mode: **TRANSFER VALIDATION / TYPE NON-INTERVENTION**
Stage: 2 PRACTICE / NOT PASSED

## Question
What Type evidence is required when a professional ledger exposes many compact aviation headers and extreme duration values?

## SOURCE
LogMate's confirmed Standard projection uses compact headers such as Date, Type, Reg, Flight, DEP, ARR, Block, Night, Inst and Remark. The wider 35-item catalog adds labels including R/O, T/O Time, L/D Time, R/I, Actual Inst, Sim Inst, PIC, SIC/FO, PICUS, SPIC, PF/PM and Exam/Check. The product contract also preserves cumulative duration display capacity of at least `99,999+59` where applicable.

T021 remains authoritative: unfinished drawing is repaired before general spacing, and kerning is only for residual pair-specific defects. Current product-transfer work therefore uses mature fallback rather than changing provisional custom-font metrics.

## PRACTICE CORPUS
After T021 drawing/spacing gates permit product transfer, validate at minimum:
- `DEP ARR R/O R/I T/O L/D`;
- `PIC SIC/FO PICUS SPIC PF/PM`;
- `Inst IFR Actual Inst Sim Inst Inst Ground`;
- `99,999+59`, `0+00`, `12+30`, `5+15`;
- registrations and 7-character Flight identifiers;
- mixed compact headers adjacent in dense ledger columns.

Capture resolved font/fallback, glyph coverage, advance widths, vertical metrics, clipping, raster at production sizes, and punctuation/numeral alignment.

## CRITIQUE
The catalog creates legitimate abbreviation density. That is not permission to repair layout by negative tracking, font-size reduction, width squeezing or pair kerning. If a protected semantic label does not fit, first classify whether the failure is glyph drawing, general spacing, pair residual, fallback, line-break policy or composition pressure.

`I/l/1/0` ambiguity remains particularly relevant to registrations, identifiers and time/numeric reading; T021's bounded R1 drawing work therefore has direct professional-product value. But product layout must not wait on or freeze around provisional metrics.

## REPRODUCIBLE VALIDATION
Same-build comparison across Standard, totals-heavy and operational-wide projections; baseline and enlarged text; mature fallback versus repaired custom candidate only after gate entry. A Type defect requires reproduced glyph/metric/fallback/raster evidence. Geometry pressure alone is Layout-owned.

## RELATED DOMAIN CHECK
- **Color:** compact state labels must retain contrast under actual raster conditions.
- **Layout:** ledger density supplies composition pressure and width budgets.
- **Interaction:** reorder must not change semantic string identity.
- **Web:** browser font loading/fallback and zoom provide transfer evidence.
- **Content:** semantic IDs and compact headers are protected strings, not ad-hoc truncation targets.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives measured string widths only after Type gate permits them; Content receives any ambiguity/fallback findings; Web validates browser loading; Color validates rendered contrast with actual font/raster.

## OPEN
T021 R1 mutation/raster closure, general spacing, kerning entry, shipped Flutter/native/browser custom-font transfer, human recognition evidence.

## Conclusion
T044 connects the current Type drawing gate to a concrete professional ledger corpus without violating gate order. No new Type PASS is claimed.