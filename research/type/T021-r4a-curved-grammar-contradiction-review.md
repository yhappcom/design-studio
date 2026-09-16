# T021 — R4A Curved-Grammar Prototype / Contradiction Review

Status: **EXECUTED / 14–17–24PX RASTERED / REJECT AS CANONICAL R4 DIRECTION**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Purpose

R3 exact CI established a drawing-gate failure dominated by coarse rectangular/polygonal round and bowl grammar. R4A tested the tempting repair hypothesis that replacing those primitives with quadratic curves would materially improve coherent-family drawing.

This is a **CONTRADICTION REVIEW + METHOD COMPARISON**. It deliberately tests the implied hypothesis `more curves → more mature family` rather than assuming it.

## RELATED DOMAIN CHECK

- **Type:** T021 R3 exact CI/raster critique is the direct failure substrate. Its gate order remains binding: drawing → intended-size raster → general spacing → pair residual → kerning.
- **Color:** not materially causal; all ambiguity remains monochrome and must not depend on hue.
- **Layout/Interaction:** literal operational strings remain unchanged; layout expansion is not used to hide glyph defects.
- **Web:** browser transfer remains downstream of a stable drawing candidate.
- **Content:** literal identifiers/numerics remain unchanged; wording is not shortened around weak glyphs.

## Prototype

A bounded R4A font prototype was built locally with fontTools `FontBuilder`/`TTGlyphPen` and rastered with Pillow/FreeType at 14, 17 and 24 px. Kerning remained OFF.

The prototype concentrated on the R3 failure cluster rather than adding repertoire:

`S B D O C G R U n o 0 5 1 8`

Quadratic contours were introduced for O/o, C/G, D/B/R/U bowls/joins, n shoulder, S spine, 5 lower bowl and selected figures. Existing explicit ambiguity mechanisms were retained: S remains structurally different from 5 and zero remains slashed relative to O.

Stress strings were held constant across sizes:

- `S5 5S SSS 555`
- `0O O0 000 OOO`
- `B8 8B BBB 888`
- `BDOCGRU`
- `nono noon`
- `S0B8 5O18`

Machine measurements are retained in `T021-r4a-curved-grammar-prototype-results.json`.

## Result

### KEEP — the experiment falsified a weak design shortcut

The 17 px raster demonstrates that simply substituting quadratic contours for rectangles does **not** establish a mature family. Curve presence is an implementation property, not a design-quality criterion.

### REJECT — R4A as the canonical R4 drawing direction

The prototype removed some obvious rectangular primitives but introduced a compressed/malformed round-and-bowl rhythm. O/0, B/8 and the broader `BDOCGRU` cluster still fail to read as one controlled professional construction system. The S is more curved than R3 but the overall system is not sufficiently coherent to justify replacing the exact R3 candidate.

The experiment therefore rejects the hypothesis that R3's drawing failure can be repaired by a mechanical `rectangles → quadratic curves` transformation.

### KEEP — ambiguity separation remains a constraint, not the design objective

S/5 and 0/O remain structurally distinguishable. That is necessary operationally but still insufficient for coherent-family PASS. R4 must optimize family rhythm, counters, joins, terminals and proportions while preserving ambiguity separation, rather than optimizing ambiguity in isolation.

## Revised R4 method

The next R4 iteration should not redraw every failing glyph independently. It should first define a small shared construction grammar:

1. one outer/inner oval proportion and overshoot policy for O/o/0;
2. one bowl tension/counter policy transferred to D/B/P/R/8;
3. one terminal/aperture policy transferred to C/G/S/5;
4. one shoulder policy linking n to the curved capital vocabulary;
5. figure widths and internal counters treated as a coordinated system, with slashed zero retained only as one candidate;
6. only after these shared primitives survive 14/17/24 raster should glyph-specific correction proceed.

This changes R4 from **glyph-by-glyph curve replacement** to **shared primitive → family transfer → target-size critique**.

## Gate consequence

- R3 exact-source/CI/raster evidence: **UNCHANGED / PASS through raster production**.
- R4A prototype execution: **PASS as experiment**.
- R4A design direction: **REJECT**.
- coherent-family drawing: **FAIL / still open**.
- general spacing: **BLOCKED**.
- T022 kerning: **BLOCKED**.

No R4 exact-CI claim is made because R4A was rejected before promotion into the canonical generator. This avoids spending CI/repository integration effort on a visibly inferior direction.

## HANDOFFS TO OTHER SPECIALISTS

- **Layout/Interaction:** do not compensate for Type's drawing failure with wider columns or looser global density.
- **Web:** no browser font transfer yet; R4A is rejected before that gate.
- **Content:** preserve literal operational controls; ambiguity is a Type responsibility.
- **Color:** continue treating character identity as color-independent.

## Verdict

**R4A is useful negative evidence. It demonstrates that the R3 failure is not a primitive-type problem alone: coherent type drawing requires a shared family grammar of proportions, counters, joins, terminals and optical correction. The next executable Type block should construct and transfer that grammar before another full candidate is promoted to exact CI.**
