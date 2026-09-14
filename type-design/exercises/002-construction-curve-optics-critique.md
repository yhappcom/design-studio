# Exercise 002 Critique — Construction, Curves, and Optical Equality

Status: PRACTICE / REWORK REQUIRED

Related specimen:
- `type-design/exercises/002-construction-curve-optics.svg`

Research basis:
- `research/003-stroke-contrast-bezier-optics.md`

## Intent

This exercise tests whether the studio can make and critique multiple native construction hypotheses without treating geometric scaling, novelty, or one attractive glyph as proof of a coherent type system.

## What improved over Exercise 001

### KEEP

- Three uppercase `H/O` hypotheses are now actually present.
- Hypotheses are redrawn as separate shapes rather than being represented by a scaled group.
- Two lowercase `n/o` systems explicitly name their construction assumptions.
- Overshoot is visualized as a separate optical zone rather than hidden in the contour.
- The specimen labels what it does **not** prove: exported topology, hinting, and raster quality.

This is stronger evidence of method than Exercise 001 because the failure in that exercise — substituting scaling for native construction — is explicitly corrected.

## H/O hypothesis review

### A — constructed / low contrast

**KEEP**
- Clean control case for distinguishing monoline geometry from optical compensation.
- Round overshoot can be compared directly with flat cap/base zones.

**REWORK**
- The `O` is still too dependent on a generic symmetric construction to demonstrate nuanced curve continuity.
- Equal visual simplicity risks making the exercise about geometry rather than perceived text color.

**REJECT as style evidence**
- Nothing here supports selecting a geometric grotesk direction for a product.

### B — writing-derived / diagonal stress

**KEEP**
- It demonstrates that stress can be treated as a system hypothesis rather than a decorative slash.

**REWORK**
- The red stress cue is annotation, not proof that the outer and inner contours embody coherent expansion logic.
- More letters would be required to show whether this stress survives in `C/G/S/D/P/R` and numerals.

**Risk**
- “Writing-derived” must not become an aesthetic label attached after drawing. Future practice should begin from an actual stroke skeleton or pen model before outline construction.

### C — broad optical / unequal width

**KEEP**
- Correctly tests whether metric/counter relationships can improve perceived rhythm without cell parity.

**REWORK**
- Broadness alone does not demonstrate optical superiority.
- Requires string-level comparison beside A/B at actual size.

## n/o construction review

### D — constructed arch / near-monoline

The intentionally dark arch/stem join is useful because it exposes a classic category error: sidebearing changes cannot solve weight accumulation inside the glyph.

**Disposition: REWORK.** Thin or reshape the junction before spacing adjustments.

### E — expansion-derived stress / compensated join

The join is visually less abrupt, but the exercise still does not prove a writing-derived system because only two glyphs are present.

**Disposition: KEEP FOR NEXT ROUND, NOT PASS.** Extend to `h m r u p d b q` before claiming coherent construction behavior.

## Bézier-quality audit

The SVG uses declarative path commands, but this is not equivalent to a font-editor source with inspectable node types, path direction, contour closure QA, compatible masters, or exported raster evidence.

Therefore:

- `Bézier drawing discipline` remains **PRACTICE**, not PASS;
- `Stroke / contrast / construction` may advance to **PRACTICE** because explicit hypotheses now exist;
- `Optical correction` remains **PRACTICE** pending measured raster comparison.

## Required next proof

1. Export or rasterize A/B/C and D/E at `14 / 24 / 48 px`.
2. Put forms into repeated strings, not isolated specimens.
3. Compare perceived cap/x-height equality and join darkness.
4. Record at least one redraw triggered by the raster proof.
5. Create a real font-source or equivalent editable curve artifact where node placement, extrema, and contour direction can be audited.
6. Only after that consider moving Bézier/optics toward CRITIQUE.

## Transfer lesson

The meaningful progress here is not aesthetic. It is procedural:

**a hypothesis must be represented by a native construction, and critique must distinguish structural defects from spacing or rendering defects.**

That lesson transfers directly to responsive interface work: a new size/state deserves a designed composition when geometry changes materially; blindly scaling a prior state is not equivalent.
