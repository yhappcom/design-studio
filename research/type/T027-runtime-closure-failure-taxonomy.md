# T027 — Runtime closure failure taxonomy

Status: PRACTICE / TRANSFER VALIDATION PREPARATION

## PURPOSE
T026 already defines the executable financial-string matrix. T027 prevents a future runtime run from collapsing distinct Type failures into a generic overflow result.

## RELATED DOMAIN CHECK
- Type: T021 drawing gate and T026 execution matrix remain authoritative.
- Color: C057 state encoding must not force semantic shortening.
- Layout/Interaction: L048/I044 may recompose geometry but may not delete label/value/qualifier relationships.
- Web: W057 owns runtime artifact identity.
- Content: CD063 owns truth-bearing strings.

## FAILURE TAXONOMY
Classify every observed failure before revision:
1. GLYPH — missing/wrong glyph, tofu, fallback mismatch, ambiguous numeral/punctuation.
2. DRAWING — custom-glyph construction defect. Route to T021; do not compensate with spacing/kerning.
3. METRICS — line/advance/vertical metrics produce clipping or unstable alignment.
4. GENERAL SPACING — sidebearing/spacing defect after drawing is defensible.
5. PAIR RESIDUAL — only after drawing and general spacing; eligible for later kerning evidence.
6. FALLBACK — script/font fallback changes hierarchy, weight, width or symbol association.
7. COMPOSITION PRESSURE — correct type/string cannot fit current geometry without reflow; route to Layout, not semantic deletion.
8. SEMANTIC TRUNCATION — currency, sign, unit, qualifier or state text removed/ellipsized; joint Type/Content failure.
9. RUNTIME RASTER — browser/native rendering changes legibility despite source correctness.

## ACCEPTANCE RECORD
For each W057 scenario preserve build/runtime identity, font/fallback identity, locale, scale/zoom, viewport, observed class, screenshot/raster reference, and disposition. A PASS requires no unresolved class 1–9 failure in the scoped scenario.

## STUDIO JUDGMENT
Runtime evidence must diagnose ownership before revision. A geometry problem is not automatically a font problem; a font problem is not automatically a kerning problem.

## OPEN
No runtime execution occurred in this study. T021 R1 drawing remains open. Human recognition and AT evidence remain open.

## HANDOFFS TO OTHER SPECIALISTS
- Layout: accept COMPOSITION PRESSURE without requesting semantic deletion.
- Content: preserve truth-bearing strings when Type reports pressure.
- Web: include this classification in W057 result manifests.