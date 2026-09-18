# T050 — Reset Focus/Status Transfer Corpus

## Purpose
Add I068/CD087 post-Reset status strings to product-transfer coverage without changing the T021 drawing→spacing→kerning gate.

## RELATED DOMAIN CHECK
Color C080/C081, Layout L071/L072, Interaction I067/I068, Web W080, Content CD086/CD087 checked. This is TRANSFER VALIDATION only.

## Corpus
Exercise mature fallback now, repaired custom candidate only after T021 permits: `Reset display`, `Reset to default`, `Already using default layout`, `Undo reset`, `Display restored`, plus DEP/ARR, PIC, SIC/FO, PICUS, SPIC, T/O, L/D and positions 1/35, 9/35, 10/35, 19/35, 20/35, 34/35, 35/35. Include long/localized placeholders and mixed-script fallback.

## Gate discipline
T021 remains authoritative: bounded R1 drawing with widths/sidebearings frozen and kerning OFF → general spacing → only then residual pair-specific kerning. Reset/status density is not evidence to narrow glyphs, tracking or kerning.

## Validation
After T021 drawing/spacing permits, compare repaired candidate with mature fallback at 14/17/24px and 200% product transfer; record fallback, clipping, line breaks, ambiguity-critical glyphs and raster evidence. Composition-only pressure returns to Layout.

## OPEN
No T021 closure, custom-font production PASS, browser/native breadth, AT or human recognition evidence.

## HANDOFFS TO OTHER SPECIALISTS
Content strings remain semantically protected; Layout owns wrapping/recomposition; Web owns runtime font loading/fallback; Color must not rely on typographic compression for state differentiation.