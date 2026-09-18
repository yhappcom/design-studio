# T047 — Recovery/Status Rendering Transfer Corpus

Status: **STAGE 2 PRACTICE / T021 GATE PROTECTED**  
Purpose: **TRANSFER VALIDATION PREPARATION**, not permission to advance kerning.

## RELATED DOMAIN CHECK
I065 adds move/undo/reset transaction truth. CD084 supplies required recovery/persistence strings. L069 owns geometry/reflow. C078 owns state color. W078 will test browser realization.

## Gate protection
T021 remains authoritative: bounded R1 drawing repair → general spacing → only then residual pair-specific kerning. Recovery density must not be solved by narrowing glyphs, reducing font size/tracking, changing frozen sidebearings or opening kerning early.

## Transfer corpus
Add to T044–T046 after T021 gates permit:
- `Undo`, `Reset layout`, `Moved`, `Move undone`;
- positions `1 of 35`, `9 of 35`, `10 of 35`, `19 of 35`, `34 of 35`, `35 of 35`;
- punctuation/slash stress with `SIC/FO`, `T/O`, `L/D`, `R/O/R/I`;
- adjacency with `DEP`, `ARR`, `PIC`, `PICUS`, `SPIC`;
- localized expansion supplied by Content, using mature fallback until custom-font multiscript scope is defensible.

## Reproducible checks
At 14/17/24px and 200% product text conditions capture resolved font/fallback, line count, clipping, numeral/punctuation ambiguity and raster. Attribute failure to Type only with reproduced glyph/metric/fallback/raster evidence; composition pressure returns to Layout.

## CRITIQUE
Repeated position numerals can expose `1/I/l/0` ambiguity and punctuation weakness, but a crowded recovery surface is not itself a Type defect. No kerning change is justified from string fit alone.

## OPEN
R1 mutation/rerender, general spacing closure, kerning entry, shipped Flutter/browser/native transfer, AT/human recognition.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives any reproduced metric evidence after Type gates permit. Content keeps semantic strings intact. Web captures actual resolved font/fallback. Interaction/Color receive no authority changes.