# T056 — Undo-scope string transfer boundary

## PURPOSE
Carry I074/CD093 multi-scope recovery strings into later Type transfer without violating the active T021 drawing gate.

## RELATED DOMAIN CHECK
I074 may require scope-qualified recovery; CD093 owns wording; L078 owns fit/placement; C087 owns state paint; Web runtime transfer is pending.

## PRACTICE CORPUS
Later repaired-candidate comparison must include short and qualified recovery strings, repeated position numerals `1/35 … 35/35`, and aviation tokens DEP/ARR, PIC, SIC/FO, PICUS, SPIC, PF/PM, T/O/L/D alongside mature fallback and mixed EN/KO fallback.

## GATE DISCIPLINE
Current order remains:
1. bounded T021 R1 drawing repair;
2. normalized rerender with widths/sidebearings frozen and kerning OFF;
3. direct raster critique;
4. general spacing;
5. only then residual pair-specific kerning.

Longer recovery labels, 200% wrapping or scope qualification are not evidence to narrow provisional glyphs, alter sidebearings or open kerning early. Product systems strings use mature fallback while R1 is open.

## VALIDATION LATER
At 14/17/24px and product sizes: ambiguity-critical glyphs, clipping, repeated numerals, punctuation, mixed-script fallback, 200% line breaks and scope-qualified labels. Attribute a failure to Type only when glyph/metric/fallback/raster evidence reproduces it.

## OPEN
R1 source mutation, repaired raster, spacing closure, kerning entry, shipped Flutter/native/browser transfer, EN/KO human recognition.

## HANDOFFS
Content should not shorten semantic truth to accommodate provisional metrics; Layout/Web should use mature fallback for current scope-routing evidence.
