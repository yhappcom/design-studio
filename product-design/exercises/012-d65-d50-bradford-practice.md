# Exercise 012 — D65 → D50 Linearized Bradford Practice

Status: PRACTICE COMPLETE / broader CAT comparison and ICC-tool validation pending.

Research basis: `research/012-chromatic-adaptation-white-points.md`

## Purpose

Connect the earlier sRGB→XYZ D65 exercise to the ICC D50 profile connection space, while making the chromatic-adaptation step explicit.

## SOURCE

ICC.1:2022 Annex E defines the linearized Bradford transform used in ICC v4 workflows. ICC Technical Note 02-2003 publishes the D65→D50 adaptation matrix derived from the Bradford matrix and the adopted-white values used by the profile architecture.

References:

- https://www.color.org/specifications/ICC.1-2022-05.pdf
- https://www.color.org/chadtag/
- https://www.color.org/whyd50/

Published D65→D50 matrix:

```text
M =
[ 1.04790738171017    0.0229333845542104  -0.0502016347980104 ]
[ 0.0296059594177168  0.990456039910785   -0.01707552919587   ]
[-0.00924679432678241 0.0150626801401488   0.751791232609078 ]
```

## Check 1 — adopted white maps to adopted white

Using the D65 white point represented in the ICC note, normalized to `Y=1`:

`D65 = [0.9504, 1.0000, 1.0889]`

Applying `M` gives:

`D50 = [0.9642, 1.0000, 0.8249]`

**KEEP:** this verifies the intended white-point mapping of the published matrix.

## Check 2 — previous neutral example

Exercise 010 calculated encoded sRGB `#808080` as approximately:

`XYZ_D65 = [0.205166, 0.215861, 0.235085]`

Applying the ICC Bradford adaptation gives:

`XYZ_D50 ≈ [0.208144, 0.215861, 0.178089]`

The `Y` coordinate stays essentially unchanged in this neutral case while `X` and especially `Z` change because the adopted white changes.

**LESSON:** chromatic adaptation is not an RGB re-encoding operation and not a relabeling of the same XYZ triplet.

## Check 3 — previous focus blue

Exercise 010 calculated `#005FCC` as approximately:

`XYZ_D65 = [0.149900, 0.125432, 0.587597]`

Applying the D65→D50 matrix gives:

`XYZ_D50 ≈ [0.130460, 0.118639, 0.442254]`

All three coordinates change materially.

**LESSON:** adaptation affects chromatic colours, not only the numerical representation of white.

## Failure case — relabel without adaptation

Rejected procedure:

1. calculate sRGB→XYZ using a D65-referenced matrix;
2. write “D50 XYZ” beside the same values;
3. feed those values into a D50 PCS workflow.

This is a coordinate/reference-condition error. ICC documentation explicitly requires non-D50 colorimetry to be chromatically adapted to the D50 PCS in the v4 architecture.

**REJECT.**

## Pipeline distinction

Correct conceptual sequence for an sRGB value entering a classic ICC v4 D50 PCS workflow:

`encoded sRGB`

→ `linear-light sRGB`

→ `XYZ D65`

→ `chromatic adaptation D65→D50`

→ `PCSXYZ D50`

A colour-management system may encapsulate these operations inside a profile/CMM. The design lesson is not to manually duplicate those operations when a managed pipeline already performs them.

## SYNTHESIS

1. White point belongs to the colorimetric reference condition.
2. Chromatic adaptation predicts corresponding colour under a changed adopted white.
3. The ICC D50 PCS is an interoperability convention, not the physical white of every source device.
4. Production conformance and perceptual-research model selection are different questions.
5. A colorist must know whether the application or CMM has already performed the adaptation before applying any manual matrix.

## STUDIO JUDGMENT

For MintTap Design Studio handoff documents:

- name the source RGB space;
- name the expected color-management path;
- do not publish manually D50-adapted UI hex values as replacement design tokens;
- when delivering print/graphic-arts assets, record embedded profile/export intent rather than assuming the recipient will infer it;
- treat conversion math as pipeline evidence, not as proof of final appearance.

## OPEN

- reproduce the same source samples through an actual ICC CMM and compare with the hand calculation;
- inspect round-trip error D65→D50→D65;
- compare Bradford against CAT02/CAT16 on an explicitly defined research dataset;
- test appearance rather than only coordinates under changed viewing conditions.

## Status implication

The chromatic-adaptation calculation bridge is now practiced. It does not change the overall `Color / luminance / contrast` domain from `CRITIQUE` to `PASS`.