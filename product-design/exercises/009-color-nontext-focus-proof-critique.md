# Exercise 009 Critique — Non-text Contrast and Focus Geometry

Status: CRITIQUE COMPLETE / real-device environmental inspection still required for foundation PASS.

Related artifact: `product-design/exercises/009-color-nontext-focus-proof.svg`

Research basis: `research/008-color-luminance-contrast-hierarchy.md`

Primary-source baseline:
- WCAG 2.2, 1.4.11 Non-text Contrast: https://www.w3.org/TR/WCAG22/#non-text-contrast
- WCAG 2.2, 1.4.1 Use of Color: https://www.w3.org/TR/WCAG22/#use-of-color
- WCAG 2.2, 2.4.13 Focus Appearance: https://www.w3.org/TR/WCAG22/#focus-appearance

## Test

The artifact adds the missing measured non-text examples to the earlier color/luminance exercise:
- selected-row boundary and redundant selection marker;
- explicit keyboard-focus ring geometry;
- a deliberately weak pale-outline control;
- grayscale status states that retain text and shape semantics.

## Measured examples

### Selected row

The selected operational row uses a `#595959` boundary on white, approximately 7.0:1 by the WCAG relative-luminance formula. The selected state does not depend on that boundary alone: a dark marker and the word `SELECTED` remain available when hue is removed.

**KEEP** because state meaning survives color removal and the required boundary comfortably exceeds the 3:1 non-text threshold.

### Focus indicator

The focus example uses an external 3 px ring in `#005FCC` against white, approximately 6.23:1. The ring is outside the component boundary and visibly encloses the control, avoiding the common failure where focus merges with an existing border.

The artifact explicitly treats WCAG focus-area geometry as a measurable floor rather than as a universal stylistic prescription.

### Weak control

The pale-outline example is **REJECTED** because selection is carried by a fragile low-salience outline with no semantic redundancy. Even before environmental testing, this is inferior to the robust example because a single visual channel bears the entire state distinction.

## Grayscale/state-removal critique

`BOARDING ▶` and `DELAYED !` remain distinguishable without hue because words and shapes encode state. This satisfies the methodological requirement that color be supplemental rather than exclusive.

## Environmental stress model

The SVG cannot reproduce real glare or dark-adapted perception. It therefore avoids claiming that a simulated overlay proves environmental performance. Instead, it records what should fail first under stress:
- subtle interior fills;
- small tonal differences;
- decorative separators.

Required state remains attached to stronger geometry, text, and explicit symbols. This is the correct hypothesis to take to physical-device inspection.

## Transferable conclusion

The transferable method is:

**measure required component contrast → remove hue → verify redundant semantics → isolate focus from existing boundaries → test on actual displays.**

This does not prescribe `#005FCC`, a particular palette, or a universal focus treatment.

## Remaining evidence before PASS

- inspect at least one rendered implementation on physical displays under controlled bright and low-light conditions;
- verify interactive keyboard focus rather than only static geometry;
- include at least one disabled/non-interactive state so low contrast is not confused with an active control.

## Status implication

`Color / luminance / contrast` remains **CRITIQUE**. The measured non-text gap is closed, but rendered-device environmental validation is still missing.