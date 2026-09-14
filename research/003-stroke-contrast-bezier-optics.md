# Study 003 — Stroke Logic, Contrast, Bézier Construction, and Optical Correction

Status: FOUNDATION STUDY / supports practice, not a completed gate.

## Question

How should a designer move from a conceptual writing/construction model to clean digital outlines without confusing geometric consistency with optical quality?

## SOURCE — construction begins from a tool or a deliberate abstraction

Glyphs' `Sketching` tutorial describes multiple ways to discover letterforms but notes a recurring idea: shapes are often traced back to a specific writing tool. Its Latin example uses the broad nib, where nib width is fixed and nib angle remains comparatively stable. It also explicitly allows pointed-pen, brush, or geometric approaches.

Source:
- https://glyphsapp.com/learn/sketching

The professional lesson is not that every Latin typeface must look calligraphic. It is that a design needs an intelligible **construction model**. Stroke contrast, stress, joins, terminals, and counter behavior should not be invented independently glyph by glyph.

### Studio rule

Before drawing a family, state which model is being explored:

1. writing-derived expansion/translation logic;
2. constructed/geometric logic;
3. hybrid logic with explicit rules.

A model can later be abstracted heavily, but the family should still reveal coherent decisions about where weight accumulates and how curves join stems.

## SOURCE — start from reusable control structures

Glyphs recommends beginning a Latin lowercase with `n` because its stem/arch structure recurs in `h i m r u` and related forms. The tutorial then moves from rough structural points to alignment, equalized stems, curves, and optical adjustment.

Source:
- https://glyphsapp.com/learn/sketching

Consequence: the correct unit of study is a **shape family**, not an isolated showcase glyph.

For foundation practice, `n/o` and `H/O` are useful because they expose:

- straight versus round color;
- stem versus arch/bowl weight;
- counter openness;
- overshoot;
- transition/join darkness;
- sidebearing rhythm.

## SOURCE — extrema, handles, and curve continuity

Glyphs places nodes at corners, extrema, and curve-to-straight transitions before precision work. It states that handles around extrema should be horizontal or vertical, and discusses matching curvature around a node to remove visible bumps.

Source:
- https://glyphsapp.com/learn/sketching

Google Fonts' outline-quality guide adds production constraints:

- cubic Bézier segments use two off-curve control points;
- smooth connections depend on aligned handles/tangency;
- missing extrema can weaken technical control and hinting;
- almost-straight segments, zero handles, redundant collinear segments, and over-complex outlines create rendering/production risk;
- outline quality must ultimately be tested through exported fonts across environments.

Source:
- https://googlefonts.github.io/gf-guide/outlines.html

### Studio synthesis — curve quality has three layers

1. **Topological correctness** — closed contours, correct direction, useful extrema, no accidental self-intersection.
2. **Geometric continuity** — tangents and handle relationships produce intentional smoothness rather than kinks.
3. **Optical continuity** — a mathematically smooth curve can still look lumpy because curvature changes too abruptly.

A pass at layer 1 does not prove layers 2 or 3.

## SOURCE — overshoot is perceptual compensation

Glyphs describes overshoot as a deliberate extension of a round/arched form beyond a nominal alignment zone so that it appears equal in height to a flat form. Its tutorial offers example magnitudes for one exercise but those values are not universal design laws.

Source:
- https://glyphsapp.com/learn/sketching

### Studio rule

Do not copy an overshoot number between designs.

Instead test:

- display versus text size;
- stroke weight;
- shape width;
- curvature tension;
- screen rasterization;
- adjacent flat forms.

The correct question is not “what percentage should overshoot be?” but “what correction makes the round and flat forms appear optically equal under the intended conditions?”

## Optical weight compensation

A consistent coordinate thickness does not ensure consistent perceived weight.

Foundation diagnoses should separate:

- **vertical vs horizontal apparent weight**;
- **diagonal vs vertical apparent weight**;
- **join accumulation** where multiple strokes meet;
- **inside vs outside curvature tension**;
- **counter collapse** at small sizes.

The goal is not mathematical uniformity. The goal is coherent apparent color and structure.

## Bézier drawing protocol for the studio

For each new foundation glyph family:

1. state the construction hypothesis before vector drawing;
2. set UPM and alignment zones;
3. block the skeleton/form with a minimal useful point structure;
4. place required extrema and curve/straight transitions;
5. align obvious flat zones;
6. establish stems and broad weight relationships;
7. introduce curves with minimal, controlled handles;
8. inspect tangent continuity;
9. inspect curvature continuity at large scale;
10. inspect optical continuity at intended size;
11. classify defects as drawing, optical compensation, spacing, or raster problems;
12. export/raster-test before claiming small-size quality.

## Failure modes to reject

- horizontally or vertically scaling an existing glyph and treating the result as a new master construction;
- excessive nodes used to chase local contour defects;
- fixing a dark join by adding sidebearing instead of redrawing the join;
- forcing equal numerical stems where perceived color becomes uneven;
- tracing a display-size curve into a small-text role without compensation;
- declaring Bézier quality from an SVG preview without export/raster evidence.

## Transfer to product/UI design

This type-design lesson transfers to interface design at a methodological level:

- a mathematically consistent grid can still be optically unbalanced;
- repeated scaling of one component is not the same as designing each responsive state;
- local padding changes should not compensate for a wrong component silhouette or hierarchy;
- technical validity and perceptual quality are separate gates;
- dense interfaces need small-size compensation just as type does.

The transfer is conceptual, not a claim that UI and glyph geometry use identical rules.

## Practice required before PASS

1. redraw three native `H/O` hypotheses without scaling shortcuts;
2. draw at least two `n/o` construction hypotheses from explicit stroke models;
3. annotate node/extrema/handle strategy;
4. compare flat/round overshoot at multiple sizes;
5. rasterize proofs at three pixel sizes;
6. critique join darkness and curve continuity;
7. redo at least one failed curve based on critique.

Until those exercises exist, `Stroke / contrast / construction`, `Bézier drawing discipline`, and `Optical correction` remain below PASS.
