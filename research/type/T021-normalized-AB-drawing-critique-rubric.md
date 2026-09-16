# T021 — Normalized A/B drawing critique rubric

Date: 2026-09-16
Purpose: **CRITIQUE GATE / executed-proof interpretation**

## RELATED DOMAIN CHECK
Color cannot compensate for ambiguous glyph construction. Layout/Web must continue using mature metrics until this gate and general spacing pass. Content supplies unchanged operational strings. Interaction owns action semantics; Type tests only their rendering/discrimination.

## Evidence entering this gate
Executed CI evidence already establishes procedural editable source, kerning OFF, 36/36 bounded coverage, 14/17/24px specimens, and architecture-token sensitivity for normalized A/B. It explicitly does not establish drawing quality.

## Critique dimensions
Evaluate A and B independently before preference comparison.
1. **Ambiguity controls:** I/l/1 and O/0 remain structurally discriminable without relying on color/context.
2. **Construction consistency:** stem/round-stem relationships, cap/x-height logic, overshoot and repeated construction families agree unless an optical exception is documented.
3. **Counters/apertures:** internal spaces remain open and proportionate at 14px; closure/dark spots at 17/24px are classified as drawing/raster defects, not spacing.
4. **Joins/shoulders:** bowls, diagonals and shoulders avoid local weight spikes, pinches and accidental pseudo-serifs.
5. **Terminals:** terminal policy is coherent across the bounded corpus and does not create identifier ambiguity.
6. **Apparent weight:** rounds, straights and diagonals appear balanced across proof sizes; numerical stroke equality is not sufficient evidence.
7. **Raster behavior:** defects that appear only at a proof size are logged separately from source-shape defects.

## Decision discipline
For each observed defect record candidate, glyph(s), proof size, defect class, severity, reproducible specimen location and proposed drawing repair. Do not adjust kerning. Do not open general-spacing critique until high-severity drawing defects are repaired or explicitly rejected with rationale.

A/B selection is not a beauty vote. Prefer the architecture that survives the operational corpus with fewer high-severity drawing defects and clearer ambiguity controls while retaining a coherent construction system.

## Gate result
**RUBRIC READY / DRAWING VERDICT OPEN.** The current repository evidence is sufficient to begin critique but the available text metadata does not substitute for inspecting the rendered specimens. No T021 closure or A/B winner is claimed here.

## HANDOFFS
After a defensible drawing verdict, Type performs general-spacing critique with kerning OFF. Only then may Layout/Web consume candidate metrics for transfer and only pair-specific residuals may feed T022.