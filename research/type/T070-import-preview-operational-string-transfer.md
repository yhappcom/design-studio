# T070 — Import-preview operational string transfer corpus

Date: 2026-09-19
State: STAGE 2 PRACTICE — DOWNSTREAM TRANSFER ONLY; T021 DRAWING GATE UNCHANGED

## RELATED DOMAIN CHECK
I088/CD107 introduce dense import strings and identifiers; L092 introduces 200% row geometry; C101 and W101 need rendered-state transfer. None changes Type's gate order.

## GATE DISCIPLINE
T021 bounded drawing remains upstream. Widths/sidebearings stay frozen and kerning stays OFF until drawing and then general spacing permit progression. No import-table fit problem may be “fixed” by premature kerning or narrowing immature glyphs.

## TRANSFER CORPUS
Operational identifiers: flight numbers, registrations, DEP/ARR airport codes, dates/times, PIC/SIC/FO/PICUS/SPIC/PF/PM, T/O, L/D.

Import/recovery strings: Import preview, Ready to import, Exact duplicate, Possible duplicate, Invalid row, Keep, Skip, Replace, Review, Fix, Exclude, Cancel import, Import records, Undo import, Undo unavailable, Restore, 1/28…28/28, long filenames and EN/KO equivalents supplied by Content.

Ambiguity stress remains concentrated on I/l/1/0/O plus punctuation, slash, hyphen, colon, parentheses and numerals.

## FUTURE VALIDATION AFTER T021
Render the corpus against repaired candidate and mature fallback at production sizes, baseline and 200%; inspect clipping, fallback, line breaks, identifier ambiguity and numeral/punctuation rhythm. Attribute failures to Type only when glyph/metric/fallback/raster evidence reproduces them.

## OPEN
T021 closure, general-spacing entry, kerning, production font, browser/native breadth, Korean fallback, AT and human recognition remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Content should not shorten required semantic distinctions solely for fit. Layout/Web should return reproduced clipping/wrapping evidence rather than inferred Type blame.
