# T057 — Korean IME composition and recovery-string Type transfer

## Purpose
Add Korean IME/composition and contextual Undo strings to the later LogMate transfer corpus while explicitly preserving the T021 drawing gate.

## RELATED DOMAIN CHECK
Checked C087/C088, I074/I075, L078/L079, W087 and CD093. The new pressure is multilingual/provisional rendering; it is not evidence that current glyph drawing, spacing or kerning should be changed.

## PRACTICE CORPUS
Later, after T021 permits transfer testing, compare repaired candidate/fallback behavior for:
- `Undo`, `Undo display change`, `Undo text edit`, `Undo reset`;
- Korean equivalents selected by Content after linguistic/runtime validation;
- mixed strings containing DEP/ARR, PIC, SIC/FO, PICUS, SPIC, PF/PM, T/O/L/D and `1/35…35/35`;
- active Korean composition adjacent to Latin aviation abbreviations and numerals;
- punctuation, caret/selection/composition decoration alignment and 200% wrapping.

## GATE DISCIPLINE
Current order remains: **bounded R1 drawing → normalized raster critique → general spacing → residual kerning**. Widths/sidebearings remain frozen and kerning remains OFF during the drawing gate. Composition/recovery density is not permission to compress provisional glyphs or hide immature drawing with tracking/kerning.

## CRITIQUE
Attribute a failure to Type only after reproducing a glyph/metric/fallback/raster cause. Scope ambiguity belongs to Interaction/Content; wrapping/placement belongs to Layout/Web; state paint belongs to Color.

## VALIDATION
When the gate opens, run the same corpus against the repaired candidate and mature fallback at matched rendered sizes, then browser/native transfer. Preserve composing text as provisional input state; do not treat a platform IME candidate window as font evidence.

## OPEN
T021 remains open. Therefore T057 has no custom-font production PASS, no spacing/kerning entry, no cross-browser/native/AT/human recognition claim.

## HANDOFFS TO OTHER SPECIALISTS
Content supplies validated EN/KO strings; Web supplies actual font/fallback/composition runtime; Layout supplies wrapping constraints; Color supplies composition/focus decoration distinctions.