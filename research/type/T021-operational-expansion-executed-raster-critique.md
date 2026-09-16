# T021 — Operational Expansion Executed Raster Critique

Status: **EXECUTED LOCALLY / BUILD + COVERAGE PASS / DRAWING QUALITY FAIL / T021 REMAINS OPEN**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Scope

This block executed an equivalent of the canonical `T021-logmate-operational-family-expansion-harness.py` in the available Python environment with FontTools + Pillow, built the bounded TTF, measured the full encoded corpus at 14/17/24px, rendered specimens, inspected the 17px raster, and compared corpus widths against the locally available unhinted Roboto Regular control. It does **not** claim GitHub Actions execution, native Flutter rendering, browser rendering, human recognition evidence, or production-font quality.

A repository workflow was also added to make future proof execution reproducible in GitHub Actions, but the repository currently reported zero push workflow runs immediately after creation. That absence is not treated as execution evidence.

## SOURCE → EXECUTION

Canonical source repertoire:
- uppercase `A–P, R, S, T, U, V, X` as encoded by the bounded harness;
- lowercase `n/o/l`;
- figures `0–9`;
- punctuation `- : ,`;
- `É` construction;
- LogMate airport / identifier / numeric / ambiguity / spacing strings;
- kerning OFF.

Local execution successfully produced a TTF and Pillow could load and measure it at 14/17/24px.

## Measured coverage

The exact encoded corpus contained **36 distinct non-space characters** in this executed harness. The built font cmap covered **36/36; missing = []**.

This supersedes the earlier 6/33 = 18.18% result **for this bounded encoded corpus only**. It is not a production character-set coverage claim.

Representative 17px measured advances:
- `ICN`: 28.1406px
- `JFK`: 28.7344px
- `B737-900`: 74.3438px
- `1,284:35`: 67.2812px
- `0O`: 20.0625px
- `1Il`: 25.8438px
- `AVAVA`: 51.8750px

## Roboto geometry control

Using the locally installed unhinted `Roboto-Regular.ttf`, candidate-vs-Roboto advance deltas across the airport + identifier + numeric corpus ranged approximately **-9.7% to +4.2%**, with a mean near **-0.6%** at 14/17/24px. Because font advances scale linearly, the percentage range was effectively stable across these sizes.

### Interpretation

**SYNTHESIS:** the bounded candidate is not globally wider than Roboto. Width pressure is string-specific. This is useful layout evidence, but it does not rescue malformed glyph drawings.

The exact product `LogMateRobotoMono` artifact was not available in this execution environment, so no exact product-mono comparison is claimed.

## Raster critique

The 17px specimen exposed severe drawing defects that source-level coverage could not reveal.

### DRAWING defects

1. **C/G construction is invalid as an open-form strategy.** The harness starts from a closed O-like ring and adds rectangles. TrueType contours are additive/nonzero-fill geometry; an added rectangle is not an eraser. The resulting forms do not become coherent C/G shapes.
2. **S is not an S.** It is currently derived from the O-like ring plus a horizontal rectangle. The raster confirms that this primitive is structurally invalid.
3. **R is a placeholder H construction.** The source explicitly routes `R` to `boxglyph(..., 'H')`; therefore coverage-by-cmap overstates actual glyph-design completion.
4. **B/D family construction is too primitive.** Adding stems/bars to an ellipse does not establish coherent bowl joins and creates forms that are not acceptable family evidence.
5. **Several figures are skeletal box/polygon constructions.** They technically encode and render, but forms such as 2/3/5/6/8/9 require real contour design before ambiguity or identity conclusions are possible.
6. **lowercase n remains schematic.** The shoulder is still a rectangular construction rather than the curved shoulder required by the earlier T021 redraw finding.

### GENERAL SPACING

No base-spacing revision is justified yet for the defective glyphs. Their contour construction contaminates perceived whitespace. H/O/A/V/T/L/I controls remain useful, but new-form spacing must be deferred until the drawings are structurally credible.

### PAIR-SPECIFIC RESIDUAL

No new T022 kerning candidates are accepted from this specimen. Pair-specific residual diagnosis is blocked wherever one or both glyphs have unresolved drawing defects.

## Important methodological correction

**cmap coverage PASS != coherent family PASS.**

The executed block achieved full bounded character encoding and successful rasterization while simultaneously failing the family drawing gate. This is exactly why the Stage 2 evidence chain must remain:

`character coverage → executable font → raster inspection → drawing validity → general spacing → pair residual → kerning`.

Moving directly from 36/36 cmap coverage to T022 would be a false positive.

## KEEP / REWORK / REJECT

- **KEEP:** B's overall metric direction; H/O/A/V/T/L/I controls; bounded corpus; 14/17/24 measurement method; no-kerning discipline; cmap audit; Roboto width comparison method.
- **REWORK:** C/G/D/B/R/S/U, lowercase n, most figures, punctuation optical placement; then rerender.
- **REJECT:** additive-rectangle-as-eraser construction for open round forms; placeholder R=H; interpreting successful cmap/raster output as coherent-family completion.

## Next large block

Do not open T022. Redraw the failed structural families using valid contours rather than additive masks/placeholders, then rerun the same corpus. Only after the drawing gate passes should sidebearing revisions and residual-pair enumeration proceed. Exact LogMate mono comparison remains pending until its actual artifact is available.

## RELATED DOMAIN CHECK

- **Layout:** measured width pressure is string-specific and near Roboto on average in this bounded control, but malformed forms invalidate any identity selection.
- **Web:** no browser transfer yet; the binary is research-only and drawing-invalid.
- **Color:** unchanged and irrelevant to the detected structural defects.
- **Content Design:** literal operational strings were preserved.

## Verdict

**T021 made a substantive advance: executable bounded coverage reached 36/36, but the raster falsified the assumption that encoded expansion equaled coherent family expansion. T021 remains OPEN at the drawing-quality gate. T022 remains BLOCKED.**