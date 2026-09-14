# Study 002 — Metrics, Spacing, and Optical Rhythm

Status: FOUNDATION STUDY / supports practice, not a completed gate.

## Question

What changes when spacing is treated as a first-class design system rather than cleanup performed after glyph drawing?

## SOURCE — OpenType metric structure

### `head`: units and coordinate granularity

The OpenType `head` table stores global font information including `unitsPerEm`. Microsoft specifies a valid `unitsPerEm` range of 16–16384 and explains that UPM determines the granularity of the font coordinate grid used for outline points and anchors.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/head

Consequence: a design-unit number has meaning only inside a declared coordinate system. A sidebearing of `60` is not intrinsically loose or tight without UPM, glyph proportions, and intended size.

### `hmtx`: advance width and sidebearing are layout data

Microsoft's OpenType specification states that horizontal layout uses advance widths, sidebearings, and glyph x bounds. The `hmtx` table supplies each glyph's advance width and left sidebearing. Right sidebearing is derived from advance width, left sidebearing, and outline bounds:

`rsb = aw - (lsb + xMax - xMin)`

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/hmtx

Consequence: the visible contour and the metric box are separate but coupled systems. Moving a contour without understanding its bearings changes texture; changing advance width without understanding the contour changes rhythm.

### `hhea`: font-wide horizontal behavior

The `hhea` table contains horizontal-layout data including typographic ascent/descent/line gap, maximum advance width, minimum left/right sidebearings, and xMax extent. Microsoft also notes that applications/platforms may consult different vertical-metric fields, requiring target-environment evaluation.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/hhea

Consequence: metrics cannot be reduced to per-glyph aesthetics. Font-wide and platform layout behavior matters.

## SOURCE — spacing before kerning

Glyphs defines spacing as adjusting glyph sidebearings to create even rhythm in text. Its Latin workflow recommends beginning with `n/o`, and uppercase with `H/O`, because stable straight/round control forms allow other glyphs to inherit or relate to their metric behavior.

It explicitly recommends:

- judge at the intended size;
- use repeated context strings rather than isolated pairs;
- get as far as possible without kerning;
- revisit sidebearings if many tiny kerning pairs seem necessary.

Sources:
- https://glyphsapp.com/learn/spacing
- https://glyphsapp.com/learn/kerning
- https://handbook.glyphsapp.com/spacing/
- https://handbook.glyphsapp.com/spacing-and-kerning/

## SOURCE — optical correction

Glyphs' sketching guidance uses overshoot as an explicit optical compensation: a curved arch extends beyond a nominal alignment zone so it can appear equal in height to a flat form.

Source:
- https://glyphsapp.com/learn/sketching

This is important because equal coordinates do not imply equal perception.

## SYNTHESIS — five metric layers

Spacing decisions should be evaluated at five layers:

1. **Contour bounds** — where black form begins and ends.
2. **Sidebearings** — white space owned by the glyph.
3. **Advance width** — the layout cell consumed before the next glyph origin.
4. **Sequence rhythm** — perceived alternation of black and white in repeated strings.
5. **Target-size raster result** — whether the intended rhythm survives pixels and antialiasing.

Kerning enters only after the general rhythm is sufficiently stable that remaining problems are pair-specific.

## Practical distinction

### A spacing problem

If `HOH`, `HOOH`, `OOHO`, and many unrelated words all show the same side imbalance around `O`, change `O`'s bearing or contour/spacing relation.

### A kerning problem

If general spacing is stable but `VA`, `To`, or another specific pair creates exceptional white space because of complementary shapes, a pair adjustment may be justified.

### A drawing problem disguised as spacing

If a bowl is too flat, a diagonal junction too dark, or a counter too small, repeatedly altering bearings may only move the defect. Fix form before metrics.

## Studio exercise protocol derived from sources

For a Latin control study:

1. declare UPM and alignment zones;
2. draw `H/O` (and later `n/o`) as system controls;
3. set sidebearings with no kerning enabled;
4. inspect `HHOO`, `HHOH`, `OOHO`, `HOHOHO`, and mixed words;
5. inspect at intended text and display sizes, not only enlarged outline scale;
6. blur/squint/flip to reduce semantic bias;
7. classify each defect as drawing, spacing, or true kerning;
8. only then create pair-specific corrections.

For data-centric products, add numeric/control strings after alphabet controls:

- `00112233445566778899`
- `010101 808080 111888`
- `1+05 12+40 999+59`

These do not replace `H/O/n/o`; they test an additional use context.

## Transfer to UI design

The same principle generalizes without turning font metrics into a literal UI grid:

- a component's visible rectangle and its interaction/layout box are not the same thing;
- mathematical equality does not guarantee optical equality;
- local pair fixes should not substitute for a broken global spacing system;
- repeated rhythm reveals defects that isolated screenshots hide;
- evaluation must occur at intended device scale.

This is a transferable method, not a mandate that UI spacing copy font metrics.

## OPEN

- actual drawing practice with multiple construction hypotheses;
- measured critique of overshoot and perceived equality;
- lowercase control-family exercise;
- raster comparison at multiple pixel sizes;
- numerals and punctuation as independent spacing systems.
