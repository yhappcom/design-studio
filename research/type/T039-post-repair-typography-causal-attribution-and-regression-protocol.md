# T039 — Post-repair typography causal attribution and regression protocol

## Purpose
Prevent a spatial repair from being accepted by silently degrading typography, and prevent Type from being used to compensate for an unresolved composition defect.

## Gate position
Stage 2 PRACTICE. T021 ordering remains normative: drawing → general spacing → residual kerning. No advancement is claimed.

## SOURCE
Current MintTap transfer evidence has already shown compact-width overflow at baseline and larger overflow under 2× text scaling. That pattern is treated as composition pressure unless a controlled typography comparison isolates a glyph, metric, fallback, spacing, or pair-specific cause. WCAG 2.2 remains the accessibility reference point for downstream reflow/zoom checks; Type does not reinterpret layout acceptance.

## PRACTICE — controlled repair matrix
Run the same build/scenario identity before and after the spatial repair and record:

1. font family and resolved fallback per stressed string;
2. font size, weight, line height and letter spacing;
3. measured line count and break positions;
4. clipping/ellipsis/wrap behavior;
5. signed/large KRW and USD numerals, punctuation and minus sign;
6. long localized labels and qualifiers;
7. baseline and 2× text-scale screenshots/raster evidence.

No typography property may be changed merely to make the failing Row fit. If a typography change is independently justified, it must be evaluated as a separate intervention.

## CRITIQUE / attribution vocabulary
Classify every regression as one primary cause before changing Type:

- GLYPH_DRAWING
- FONT_METRICS
- FALLBACK_SUBSTITUTION
- GENERAL_SPACING
- PAIR_RESIDUAL
- LINE_BREAK
- RASTERIZATION
- COMPOSITION_PRESSURE
- SEMANTIC_TRUNCATION

A COMPOSITION_PRESSURE or SEMANTIC_TRUNCATION result is handed back to Layout/Content. It is not a kerning task.

## Reproducible validation
A post-repair Type PASS requires all of the following under the same build identity:

- no new fallback substitution;
- no unexplained font-size/weight/leading/tracking change;
- no new clipping or semantic ellipsis;
- stable signed-number and currency punctuation rendering;
- any changed line break is attributable to the intended responsive recomposition rather than glyph compression;
- no pair-specific adjustment is introduced before drawing and general spacing are mature.

## Product-transfer boundary
Automated screenshots and widget measurements can establish rendering consistency, not human reading comfort or preference. Representative-human readability and AT comprehension remain OPEN.

## RELATED DOMAIN CHECK
- Layout owns spatial recomposition and overflow elimination.
- Content owns semantic shortening/abbreviation decisions.
- Color owns state/polarity meaning, not typographic fit.
- Web owns browser/runtime provenance.
- Interaction owns focus/action continuity.

## Next evidence
Consume the first repaired MintTap runtime artifact. If it is not available, do not invent a PASS; preserve this protocol as the attribution gate and move effort to executable non-human validation elsewhere.