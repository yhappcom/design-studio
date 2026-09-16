# T021 — Normalized A/B Direct Drawing Critique

Evidence purpose: **CRITIQUE + CONTRADICTION REVIEW**. This study directly inspects the executed `t021-normalized-proof` artifact from workflow run `35048673549` (head `21f9bc8470403716cbf2b45ab3f8338db18c3323`), rather than inferring drawing quality from CI metadata.

## RELATED DOMAIN CHECK

- **Content:** CD045 terminal/recovery strings increase the importance of reliable digits, identifiers and compact operational strings; wording is not shortened to hide Type defects.
- **Color:** C039 cannot repair glyph ambiguity; color/state salience remains independent.
- **Layout/Interaction:** L030 must not freeze provisional custom-font metrics; I026 owns behavioral truth.
- **Web:** W039 continues to use mature fallback until T021 drawing/general-spacing gates pass.
- **UX integration:** this is non-human expert critique. It does not establish recognition speed, error rate or pilot task performance.

## Executed evidence inspected

Direct raster inspection covered normalized A and B at **14, 17 and 24 px**, kerning OFF, using the artifact's AMBIGUITY, AIRPORTS, IDENTIFIERS, NUMERIC and SPACING rows. The artifact already establishes 36/36 bounded coverage; this study evaluates drawing, not coverage.

## Findings

### 1. `O/0` differentiation

**A:** zero remains visually close to O in dense `00 / 000` and time/identifier contexts. The distinction is insufficiently explicit for an operational identity candidate. **Drawing defect — HIGH.**

**B:** slashed zero materially differentiates 0 from O at all three inspected sizes. However the slash creates conspicuous internal texture in dense numeric strings (`00:45`, `B737-900`, repeated zero groups), especially at 14 px. **Directionally stronger ambiguity control, but drawing/raster refinement required — MEDIUM.**

Decision: B is provisionally stronger specifically for O/0 discrimination; this is not an overall A/B winner.

### 2. `I/l/1` family

Across both A and B, the repeated ambiguity rows show insufficiently stable differentiation among capital I, lowercase l and digit 1 at small sizes. Thin vertical constructions and small terminal differences lose authority at 14 px and remain fragile at 17 px. **Drawing-system defect — HIGH.**

This must be repaired in base construction. Kerning is prohibited as a remedy.

### 3. Raster consistency / construction texture

At 14 px several diagonals, joins and small terminals become uneven relative to the calmer vertical/horizontal stems. The issue is visible in identifiers and airport strings, not only synthetic controls. At 24 px the intended constructed personality is clearer, showing that the problem is partly size/raster sensitivity rather than only spacing. **Drawing/raster defect — MEDIUM.**

### 4. Operational string integrity

Airport and identifier rows remain readable as static expert inspection, but this does **not** justify a human-recognition claim. Dense numeric strings expose the strongest risk: ambiguity controls and stylistic texture compete for attention. The candidate therefore remains unsuitable for product transfer until the ambiguity family is repaired and rerendered.

### 5. General spacing gate

No general-spacing PASS is issued. Some strings suggest uneven apparent rhythm, but drawing defects in I/l/1 and zero architecture are sufficiently material that spacing critique would be contaminated. Per gate order, drawing repair precedes general-spacing judgment.

## Required repair block

1. Redraw the `I/l/1` family as a coherent ambiguity-control system.
2. Retain B's explicit zero differentiation as the stronger hypothesis, but reduce slash/raster intrusion at 14/17 px and rerender.
3. Recheck diagonals/joins/terminals in operational strings at 14/17/24 px.
4. Keep kerning OFF.
5. Only after these drawing defects are defensible, perform general-spacing critique.
6. Only residual pair-specific defects may enter T022.

## Gate verdict

- Direct drawing critique: **EXECUTED**.
- Drawing PASS: **NO**.
- A/B overall winner: **NO**.
- B zero architecture: **PROVISIONALLY PREFERRED FOR O/0 DISCRIMINATION**, pending repair.
- General-spacing gate: **BLOCKED BY DRAWING REPAIR**.
- T021 closure: **OPEN**.
- T022 kerning entry: **BLOCKED**.
- Human recognition/task-performance evidence: **OPEN**.

## HANDOFFS TO OTHER SPECIALISTS

- Web should continue mature fallback and must not treat the custom candidate as production-ready.
- Layout must avoid freezing widths from these provisional drawings.
- Content should preserve real operational strings for rerender stress rather than shortening them.
- Color must continue treating glyph discrimination as Type-owned and non-substitutable.
