# T042 — Diagnostic Context Capture Without Type Compensation

Date: 2026-09-18
Stage: 2 PRACTICE
Purpose: INDEPENDENT VALIDATION / causal isolation

## Problem
L064 can now preserve the full Flutter layout diagnostic. Type must contribute enough context to identify a genuine typography defect without altering typography to make a spatial failure disappear.

## PRACTICE
For every L064 baseline/enlarged-text scenario record, without changing geometry:
- exact visible string and script;
- resolved family/style/weight/size/height/letter spacing;
- text scaler and locale;
- fallback evidence where observable;
- line count, wrapping/ellipsis/clipping behavior;
- numeric/currency punctuation class;
- whether the failure persists with identical typography but different available width.

Causal classification:
- `TYPE_OWNED`: reproduced glyph drawing, font metric, fallback, raster or spacing defect;
- `COMPOSITION_OWNED`: valid text exceeds an inadequate spatial allocation;
- `CONTENT_DEPENDENCY`: required semantic string is truncated/collapsed;
- `UNRESOLVED`: diagnostic insufficient.

## Gate discipline
T021 remains authoritative: drawing first, general spacing second, residual kerning last. A RenderFlex overflow is not evidence for kerning. Do not reduce font size, tracking, glyph width or sidebearings during owner localization. Kerning entry requires the existing T021 drawing/spacing gate, not a desire to recover pixels.

## CRITIQUE
Large-text failure can expose a real metric/fallback issue, but the mere correlation `more scaling → more overflow` is not sufficient. The same run must show a typography-specific defect rather than normal text expansion under a fixed constraint.

## REPRODUCIBLE VALIDATION
Repeat the localized scenario under identical typography and at least two width allocations. If the defect follows the font/rendering system rather than the container budget, open a Type repair. Otherwise hand off to Layout. After structural repair, rerun the Type context to detect fallback, clipping, line-break or raster regressions.

## RELATED DOMAIN CHECK
- Layout L064 owns RenderFlex localization and claimant budget.
- Interaction I060 owns Material feedback, unrelated unless typography changes target geometry.
- Color C072 is not causal to text width.
- Web W072/W073 later tests real browser font loading/fallback.
- Content CD078 preserves exact semantic strings during localization.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives composition-owned results. Content receives semantic truncation. Web receives font/fallback context for browser transfer. No kerning request is accepted from another domain without T021 gate evidence.

## Evidence boundary
No new Type defect or Stage 2 PASS is claimed. Browser/native breadth, AT and human evidence remain OPEN.
