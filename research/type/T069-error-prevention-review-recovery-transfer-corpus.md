# T069 — Error-Prevention Review/Recovery Transfer Corpus

Date: 2026-09-19
Stage: Stage 2 PRACTICE
Evidence purpose: DOWNSTREAM TRANSFER SPECIFICATION; T021 remains upstream gate

## RELATED DOMAIN CHECK
I087/CD106 create material object→consequence→recovery strings; L091 creates review/confirmation geometry; C100 separates state emphasis; W100 will supply served rendering evidence. Type does not redefine these semantics.

## GATE DISCIPLINE
T021 bounded R1 drawing remains unresolved. Keep widths/sidebearings frozen, kerning OFF and unrelated glyphs frozen. Do not use spacing, tracking or kerning to compensate for unfinished `I/l/1/0` drawing. Mature fallback remains the product-transfer control until drawing then general spacing are defensible.

## TRANSFER CORPUS
Queue after T021 permits: `Delete flight`, `Delete 1 flight`, `Replace import`, `Reset fields`, `Review changes`, `Confirm`, `Cancel`, `Undo`, `Undo unavailable`, `Restore failed`, position numerals such as `1/35`, operational identifiers, dates/times, DEP/ARR, PIC, SIC/FO, PICUS, SPIC, PF/PM, T/O, L/D, plus semantically equivalent Korean stress strings. Include long object names and mixed Latin/numeral/punctuation cases at baseline and 200%.

## CRITIQUE / FAILURE CONDITIONS
Attribute a failure to Type only when glyph shape, metrics, fallback, rasterization or font loading reproduces it. Do not shorten CD106 consequence wording solely to preserve provisional geometry. Reject ambiguity regressions in `I/l/1/0`, clipping, punctuation/key-legend defects and fallback discontinuity before later spacing/kerning work.

## REPRODUCIBLE VALIDATION
When T021 closes, rerun the corpus against repaired candidate and mature fallback at the established raster sizes and product conditions, then browser/native transfer. Human recognition/readability, AT and production custom-font PASS remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web must continue using mature fallback for closure evidence while T021 is open. Content should preserve semantic completeness rather than optimize around provisional custom metrics.