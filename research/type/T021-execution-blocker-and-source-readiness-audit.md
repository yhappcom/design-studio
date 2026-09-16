# T021 — Executable source readiness audit

Evidence: **CONTRADICTION REVIEW / DEPENDENCY / OPEN**

## RELATED DOMAIN CHECK
Color C032 needs unambiguous non-color cues; Layout L023 must not freeze widths from unfinished glyphs; Interaction I019 supplies interruption/resumption strings; Web W032 must retain mature fallback until candidate coverage is valid; Content CD038 supplies certainty-critical strings that may not be shortened to fit Type.

## Audit
The canonical Type README reports only 6/33 bounded operational characters built. Recent T021 notes correctly specify corpus and critique order, but a reproducible drawing block additionally requires an editable source artifact plus deterministic build/render command. No newly verified editable source/build artifact is established by the current canonical evidence reviewed for this cycle.

Therefore another spacing or kerning study would be premature. T021 remains a **drawing/source execution blocker**, not a kerning problem.

## Minimum executable package required before the next claimed drawing advance
1. canonical editable glyph source with version/hash;
2. explicit units-per-em, ascender/descender and baseline/cap/x-height references;
3. deterministic build command producing the candidate font;
4. deterministic proof command for 14/17/24px with kerning disabled;
5. bounded-corpus fallback/notdef audit;
6. before/after proof artifact for each repaired drawing/general-spacing defect.

## Critique rule
Until that package exists, mature system/product fonts remain the transfer baseline. No width token, kerning class, figure system or production identity recommendation may be frozen from the incomplete candidate.

## HANDOFFS TO OTHER SPECIALISTS
Web/Layout should continue with mature font metrics. Content should preserve semantic strings. Color should treat ambiguous glyph recognition as Type-owned failure. Interaction should not alter state labels to accommodate incomplete glyph coverage.
