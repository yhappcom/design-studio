# T055 — Recovery branch string transfer boundary

## Purpose
Carry I073/CD092 branch-eligibility semantics into Type transfer planning without allowing new content density to bypass the T021 drawing → spacing → kerning gate.

## RELATED DOMAIN CHECK
Color C086, Layout L077, Interaction I073, Web W085 and Content CD092 checked. This is `TRANSFER VALIDATION`, not a new Type gate.

## Transfer corpus
Future repaired-candidate comparison should include, in mature-fallback and candidate conditions where permitted:
- `Undo`, `Reset`, `Moved`, `Hidden`, `Shown`;
- eligibility/supersession/no-op/failure strings supplied by final Content realization;
- positions `1/35`, `9/35`, `10/35`, `19/35`, `20/35`, `34/35`, `35/35`;
- DEP/ARR, PIC, SIC/FO, PICUS, SPIC, PF/PM, T/O, L/D;
- English/Korean mixed-script fallback and punctuation.

## Gate protection
Current T021 invariants remain: only bounded R1 drawing loci mutable; widths/sidebearings frozen; kerning OFF; unrelated glyphs frozen. New recovery strings do not justify tracking, width, sidebearing or kerning compensation for unfinished drawing.

After R1 drawing and general-spacing gates permit, compare the corpus at operational sizes and 200% for ambiguity, clipping, repeated numerals, punctuation, line breaking and fallback. Attribute a failure to Type only when glyph/metric/fallback/raster evidence reproduces it; composition pressure returns to Layout/Content.

## OPEN
T021 R1 mutation/rerender, spacing closure, kerning entry, custom-font browser/native transfer, multilingual production and human recognition remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Content should preserve semantic truth rather than shorten for provisional metrics; Layout/Web should use mature fallback until T021 permits custom-font transfer; Color focus/recovery paint must not depend on provisional glyph geometry.
