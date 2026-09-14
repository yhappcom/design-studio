# Exercise 010 — Encoded sRGB → Linear-Light sRGB → CIE XYZ

Status: PRACTICE COMPLETE / spectral-integration exercise still pending.

Research basis: `research/010-color-science-colorimetry-foundations.md`

## Purpose

Build a calculation bridge between familiar product-design colour values and formal colorimetry. The point is not to memorize one matrix. The point is to stop treating an encoded sRGB component as if it were proportional to emitted light.

## SOURCE

Current CSS Color 4 defines sRGB with D65 white, the standard sRGB primary chromaticities, and the standard piecewise transfer function. It separately defines `srgb-linear` as the same primaries and white point with unity transfer behaviour. Its color-conversion section specifies the conversion sequence:

1. encoded RGB → linear-light RGB;
2. linear RGB → CIE XYZ;
3. chromatic adaptation only when source and destination white points differ;
4. continue to the destination color space as required.

Reference:

- W3C CSS Color Module Level 4: https://www.w3.org/TR/css-color-4/

The W3C sample conversion code is explicitly informative rather than normative, but it publishes a high-precision sRGB ↔ XYZ matrix consistent with the space definition and is suitable for this reproducible study exercise.

## Step 1 — normalize encoded sRGB

For an 8-bit channel value `n`, first compute:

`c = n / 255`

This is still an encoded sRGB component. It is **not** yet linear light.

## Step 2 — decode the sRGB transfer function

For each encoded component `c` in the normal in-gamut range:

If `c <= 0.04045`:

`c_linear = c / 12.92`

Otherwise:

`c_linear = ((c + 0.055) / 1.055)^2.4`

For production conversion libraries that support extended negative values, the transfer function must be extended with sign preservation as specified by the implementation model. The present examples are ordinary in-gamut positive values.

## Step 3 — linear sRGB to XYZ D65

Using the W3C high-precision matrix:

```text
|X|   | 506752/1228815    87881/245763     12673/70218   | |Rlin|
|Y| = |  87098/409605    175762/245763     12673/175545  | |Glin|
|Z|   |   7918/409605     87881/737289   1001167/1053270 | |Blin|
```

No chromatic-adaptation transform is required here because both sRGB and the resulting XYZ reference use D65.

## Calculated examples

The calculations below were reproduced numerically from the equations above.

### White — `#FFFFFF`

Encoded normalized RGB:

`[1.000000, 1.000000, 1.000000]`

Linear RGB:

`[1.000000, 1.000000, 1.000000]`

XYZ D65:

`[0.950456, 1.000000, 1.089058]`

Chromaticity:

`x = 0.312700`

`y = 0.329000`

**CHECK:** the matrix maps equal full-intensity linear sRGB primaries to the D65 white point used by the space.

### Mid encoded gray — `#808080`

Encoded normalized RGB:

`[0.501961, 0.501961, 0.501961]`

Linear RGB:

`[0.215861, 0.215861, 0.215861]`

XYZ D65:

`[0.205166, 0.215861, 0.235085]`

Chromaticity:

`x = 0.312700`

`y = 0.329000`

**CRITICAL LESSON:** an encoded value near 0.5 becomes only about 0.216 in linear-light units. Treating `128/255` as approximately 50% light would be materially wrong.

Because all three linear channels are equal, the neutral retains the D65 chromaticity while its XYZ magnitude falls relative to white.

### Existing Exercise 009 boundary — `#595959`

Encoded normalized RGB:

`[0.349020, 0.349020, 0.349020]`

Linear RGB:

`[0.099899, 0.099899, 0.099899]`

XYZ D65:

`[0.094949, 0.099899, 0.108795]`

Chromaticity:

`x = 0.312700`

`y = 0.329000`

This confirms that the neutral boundary used in Exercise 009 shares the sRGB white chromaticity while differing in luminance magnitude. It does not prove perceptual adequacy by itself; the earlier non-text contrast and contextual tests remain separate evidence.

### Existing Exercise 009 focus blue — `#005FCC`

Encoded normalized RGB:

`[0.000000, 0.372549, 0.800000]`

Linear RGB:

`[0.000000, 0.114435, 0.603827]`

XYZ D65:

`[0.149900, 0.125432, 0.587597]`

Chromaticity:

`x = 0.173710`

`y = 0.145356`

This is a useful contrast with the neutral examples: chromaticity changes because the primary proportions differ, while `Y` remains a separate magnitude component of the tristimulus result.

## Round-trip check

The inverse XYZ → linear-sRGB matrix published in the same W3C sample code was applied to the calculated XYZ values and then the forward sRGB encoding function was restored.

Representative round-trip maximum component error was at floating-point noise level (approximately `5.4e-16` for `#005FCC`; effectively zero for the neutral examples).

**KEEP:** the exercise is internally consistent and reproducible.

## Failure demonstration — encoded arithmetic is not linear-light arithmetic

A naive designer may assume that encoded `#808080` represents about half of the light output of white because `128/255 ≈ 0.502`.

The transfer-function calculation shows the relevant linear component is instead approximately `0.2159`.

Therefore:

- averaging encoded RGB components is not generally the same as averaging light;
- opacity/compositing, gradients, interpolation, image processing, and physical-light reasoning must specify the space in which arithmetic occurs;
- a UI color token is an encoded value, not a direct radiometric quantity.

## SYNTHESIS

1. `#RRGGBB` in ordinary web/UI use normally identifies encoded sRGB values unless another space is explicitly specified.
2. Encoded sRGB and linear-light sRGB have the same primaries and D65 white but different numeric meaning.
3. XYZ conversion requires linear RGB, not gamma-encoded channel values.
4. Neutral encoded sRGB values decode to equal linear components, so their chromaticity remains D65 while their XYZ scale changes.
5. Chromaticity and luminance magnitude are distinct; `x,y` alone do not reconstruct `Y`.

## STUDIO JUDGMENT

For future MintTap product specifications:

- do not describe RGB interpolation or blending as physically/light-linearly meaningful unless the computation space is named;
- when giving a HEX value, state that it is sRGB when that is the intended encoding;
- use linear-light calculations when the design or engineering question actually concerns additive light behaviour;
- use colorimetric/perceptual spaces deliberately rather than because their numeric axes look convenient;
- keep accessibility contrast, colorimetry, and brand semantics as connected but distinct layers of evidence.

## OPEN / next practice

This exercise closes only the **digital bridge** portion of Study 010. It does not complete the colorimetry foundation.

Still required:

1. official CIE 1 nm spectral integration into XYZ using the CIE 1931 observer dataset;
2. a spectrum-scaling experiment showing XYZ magnitude change with invariant chromaticity;
3. a metamerism exercise using spectrally different stimuli rather than RGB triplets;
4. later verification against the IEC sRGB source standard or another directly normative sRGB source where available;
5. later studies of chromatic adaptation, CIELAB/colour difference, Oklab, gamut mapping, ICC, Display P3/Rec.2020, and HDR.

## Status implication

Professional colorimetry remains **in active foundation practice**. The broader `Color / luminance / contrast` studio domain remains **CRITIQUE** because its existing accessibility/context exercises are mature enough for critique, but physical-display validation and the new spectral colorimetry exercises are still incomplete.