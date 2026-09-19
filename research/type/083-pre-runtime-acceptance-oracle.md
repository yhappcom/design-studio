# T083 — Pre-runtime Type acceptance oracle

Date: 2026-09-20
Purpose: PRACTICE / CONTRADICTION REVIEW. Convert accumulated product constraints into falsifiable implementation checks without bypassing T021.

## RELATED DOMAIN CHECK
Type T082, Color C113, Interaction I100, Layout L104, Web W113 and Content CD119 checked. Reuse: shared workflow corpus and runtime provenance. Dependency: Content owns strings; Layout owns protected geometry; Web owns resolved-font capture.

## Acceptance oracle
A product surface fails Type transfer if any of these are true:
1. intended family is reported without the actually resolved family/fallback;
2. required wording is shortened only to preserve preferred geometry;
3. negative tracking, glyph narrowing or kerning compensates for unresolved T021 drawing/general spacing;
4. fallback changes record identity, comparison order, action meaning or recoverability;
5. enlarged text or WCAG text-spacing causes unrecoverable clipping/truncation;
6. a provisional custom font is treated as production evidence.

For each shared closure scenario capture canonical string, rendered string, requested/resolved family, font features, wrap/truncation, line/box geometry and the protected semantic relationship affected.

## Gate discipline
T021 remains upstream: bounded drawing repair with widths/sidebearings frozen and kerning OFF → drawing critique → general-spacing validation → only then residual kerning. T083 does not promote Stage 2.

## HANDOFFS TO OTHER SPECIALISTS
Web can embed this oracle in the W113 provenance packet; Layout receives actual metric/fallback changes; Content receives any fit failure without pressure to delete semantic jobs; Color/Interaction should verify that fallback does not remove state/action cues.

## Evidence boundary
No drawing, spacing, kerning, production-font, runtime, AT or human PASS is claimed.