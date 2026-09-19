# T065 — Scroll / Focus Transfer Corpus

Date: 2026-09-19
Stage: Stage 2 PRACTICE / NOT PASSED
Upstream gate: T021 bounded R1 drawing

## Purpose
Extend the downstream transfer corpus for I083/CD102 without bypassing Type gates.

Corpus includes Move, Cancel, Undo, Reset/Restore, position numerals 1/35…35/35, focus/recovery status candidates, EN/KO field-label candidates and existing aviation abbreviations.

## Gate discipline
Widths/sidebearings remain frozen and kerning OFF while T021 drawing is immature. 200% wrapping, moving rows, sticky surfaces or scroll-restoration pressure are not reasons to compensate drawing with spacing/kerning.

After drawing and general-spacing gates permit, rerun T044–T065 against repaired candidate and mature fallback, checking clipping, line breaks, numeral differentiation, punctuation/key legends and Korean/Latin fallback.

## RELATED DOMAIN CHECK
I083/L087 define behavior/geometry; C096 defines focus-state visibility; W096 owns browser transfer; CD102 supplies semantic strings. Type owns only glyph/metric/fallback/rendering attribution.

## Evidence boundary
No T021 closure, kerning entry, custom-font production, cross-browser/native, AT or human PASS is claimed.