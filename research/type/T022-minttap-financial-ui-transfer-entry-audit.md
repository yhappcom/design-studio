# T022 — MintTap financial UI transfer entry audit

Evidence purpose: **TRANSFER VALIDATION / PROJECT ENTRY AUDIT**

## RELATED DOMAIN CHECK
- Type: T021 remains drawing-gated; no provisional custom glyph may enter product UI.
- Color: C053 requires state truth to survive without color-only encoding.
- Layout/Interaction: L044/I040 require hierarchy and action/state truth to survive density/reflow.
- Web: W053 runtime closure is still open; browser claims are excluded.
- Content: CD059 requires materially different financial/system states to remain linguistically distinct.

## Product transfer finding
MintTap exposes a materially different typography stress corpus from LogMate: long localized labels, ticker symbols, currency marks, signed percentages, large monetary values, decimals, dates, tax/ROC terminology and dense list rows. The product therefore tests numeral alignment, sign visibility, decimal/currency parsing, hierarchy under 200% text, and fallback behavior more strongly than custom-brand glyph authorship.

## STUDIO JUDGMENT
For financial dashboards, mature system/fallback fonts remain the production default until a custom face has passed drawing → spacing → residual kerning gates. Monetary outcome and total-return strings must not inherit provisional T021 metrics. A useful product test corpus must include KRW/USD, positive/negative/zero, large values, long locale strings and ticker rows.

## OPEN
- No MintTap native raster capture or 200% text artifact is recorded here.
- No tabular-figure recommendation is made until actual list alignment is measured.
- T021 R1 mutation/raster remains the Type bottleneck; T022 does not bypass it.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web should preserve enough width/reflow freedom for full financial strings; Content should not shorten state truth solely to protect geometry; Color must keep sign/state legible without hue dependence.