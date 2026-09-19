# T071 — Import mapping source/target string transfer

Status: **DOWNSTREAM TRANSFER CORPUS / T021 DRAWING GATE UNCHANGED**

## RELATED DOMAIN CHECK
I089/CD108 introduce source-vs-target mapping strings; L093 supplies narrow/200% geometry; C102 supplies simultaneous states; W102 will provide browser rendering. This is downstream corpus extension only, not permission to bypass T021.

## Gate discipline
T021 remains the upstream bounded drawing repair. Widths/sidebearings remain frozen and kerning remains OFF. Order remains:
`drawing → general spacing → residual pair-specific kerning`.

No mapping layout failure may be repaired by premature kerning or by narrowing immature glyphs.

## Transfer corpus
After T021 drawing/spacing gates permit, render mature fallback and repaired candidate against:
- `Block Time → Flight Time`;
- `PIC`, `SIC`, `PICUS`, `SPIC`, `PF`, `PM`;
- `DEP`, `ARR`, flight number, registration;
- `Needs review`, `Unmapped`, `Excluded`, `Change mapping`;
- Korean interface equivalents from CD108 while preserving literal source headers;
- long filenames/source-system names;
- `1:30`, `1.5`, `90 min`, `12/12`;
- arrows, colon, slash, hyphen, parentheses and key/focus legends if present.

## Reproducible checks
At 14/17/24 px and later real runtime/200%: ambiguity-critical `I/l/1/0`, numeral/punctuation clarity, clipping, fallback transitions, line breaks, source/target distinguishability. Attribute failure to Type only when reproduced as glyph/metric/fallback/raster evidence.

## HANDOFFS TO OTHER SPECIALISTS
CD108 should not shorten semantic strings solely to fit provisional metrics. L093/W102 should use mature fallback until T021 allows custom-font transfer.

## Evidence boundary
No T021 closure, spacing/kerning entry, custom-font production recommendation, browser/native or human recognition PASS is claimed.