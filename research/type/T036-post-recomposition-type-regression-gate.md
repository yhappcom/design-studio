# T036 — Post-Recomposition Type Regression Gate

Evidence class: **TRANSFER VALIDATION PLAN / GATE PROTECTION**

## PURPOSE
Define Type's next executable work after L058 repairs compact composition, without allowing Layout pressure to bypass T021 drawing→spacing→kerning order.

## PRACTICE
For the repaired 390×844 baseline and 2.0-scale scenario, record: actual font/fallback used, line count and break positions, clipping/ellipsis, baseline/vertical-metric anomalies, numeral/punctuation integrity, and raster evidence where available. Compare against the pre-repair scenario identity.

## CLASSIFICATION ORDER
1. glyph/drawing defect;
2. general metrics/spacing defect;
3. pair-specific residual only after 1–2 are defensible;
4. composition/reflow pressure when the font is not causal.

No tracking/kerning compression is permitted as a fix for L057. T021 R1 drawing remains open and product transfer should continue using mature fallback where required.

## CRITIQUE
A successful Layout recomposition can still create Type regressions: orphaned qualifiers, pathological numeral wrapping, fallback changes, clipped ascenders/descenders, or density loss. Conversely, a changed line break alone is not a Type failure if it is the intended reflow response.

## RELATED DOMAIN CHECK
L057/L058 supply the spatial failure and repair contract. CD072/CD073 preserve truth-bearing strings. C066 requires state meaning independent of hue. I054 may change surface containment but not text metrics. W066/W067 owns the shared runtime identity.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives any post-repair line-break pressure that is compositional rather than typographic. Content receives only genuine semantic/read-order breakage; wording is not a geometry escape hatch.

## OPEN
No post-repair runtime exists. T021 R1 mutation/raster closure, general spacing, kerning entry, browser/native breadth and human recognition remain OPEN.