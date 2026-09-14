# Study 010 — Color Science and Colorimetry Foundations

Status: FOUNDATION STUDY / computation and device practice required before PASS.

## Question

What does a professional product colorist need to know before treating RGB values, HEX codes, palettes, contrast ratios, or brand colors as meaningful design evidence?

The answer begins below the UI layer: with the spectral stimulus, a defined observer, an illuminant or emitting source, and a colorimetric system.

## SOURCE — CIE colorimetry is observer- and condition-defined

Primary references:

- CIE 015:2018, *Colorimetry, 4th Edition*: https://www.cie.co.at/publications/colorimetry-4th-edition
- ISO/CIE 11664-1:2019, *Colorimetry — Part 1: CIE standard colorimetric observers*: https://www.cie.co.at/publications/colorimetry-part-1-cie-standard-colorimetric-observers-0
- ISO/CIE 11664-2:2022, *Colorimetry — Part 2: CIE Standard Illuminants*: https://www.cie.co.at/publications/colorimetry-part-2-cie-standard-illuminants-0
- ISO/CIE 11664-3:2019, *Colorimetry — Part 3: CIE tristimulus values*: https://www.cie.co.at/publications/colorimetry-part-3-cie-tristimulus-values-2
- CIE official datasets: https://cie.co.at/data-tables
- CIE S 017:2020 terminology via e-ILV: https://cie.co.at/e-ilv

CIE 015:2018 treats colorimetry as a system that includes standard observers, standard illuminants, reflectance references, viewing/illuminating conditions, tristimulus calculations, chromaticity coordinates, colour spaces, colour differences, and advanced appearance modelling.

The immediate implication is that a numeric triplet is not self-explanatory. A color value only becomes reproducible when its colorimetric meaning and reference conditions are known.

## SOURCE — colour stimulus is spectral before it is a triplet

CIE S 017 defines a colour stimulus as visible radiation entering the eye and producing chromatic or achromatic colour sensation. It defines a colour stimulus function as the spectral distribution of that stimulus.

For an emitting source, the stimulus is described by its spectral distribution. For an object colour, CIE notes that the stimulus function is formed from the illuminant spectrum multiplied by the object's spectral reflectance, radiance factor, or transmittance as appropriate.

Conceptually:

`stimulus spectrum -> standard observer weighting -> tristimulus values`

For a reflecting object the chain includes the illuminant:

`illuminant SPD × spectral reflectance -> colour stimulus -> observer weighting -> tristimulus values`

### SYNTHESIS

A swatch is not an intrinsic property of the object alone. Object colour depends on both the object's spectral behaviour and the illumination under which it is viewed.

### STUDIO JUDGMENT

For screen-product work, HEX/RGB values are useful implementation encodings, but they must not be confused with a complete description of human colour appearance. For physical branding, packaging, print, textiles, or mixed physical/digital identity, spectral and illuminant dependence becomes a first-order design concern rather than a production footnote.

## SOURCE — standard colorimetric observers

ISO/CIE 11664-1:2019 specifies two standard observer sets.

- The CIE 1931 standard colorimetric observer represents normal colour vision for centrally viewed fields of roughly 1° to 4° at photopic adaptation levels.
- The CIE 1964 supplementary standard colorimetric observer represents fields greater than about 4° under sufficiently high photopic levels where rod participation is not expected.

The official CIE datasets provide the corresponding colour-matching functions at 1 nm intervals.

### SYNTHESIS

The observer is part of the measurement model. A colourimetric result is not independent of field size and observer definition.

### STUDIO JUDGMENT

A product colorist should not casually treat one colorimetric coordinate as a perfect model of every user's perception. Standard observers create a reproducible engineering reference; they do not erase individual visual-system differences.

## SOURCE — tristimulus values and XYZ

ISO/CIE 11664-3 specifies methods for calculating tristimulus values from spectral colour-stimulus data. The standard method uses 1 nm summation over 360 nm to 830 nm; abridged methods are permitted only when their effect on the result has been considered.

At a conceptual continuous level, the CIE 1931 tristimulus values are weighted integrals of the stimulus spectrum against the three colour-matching functions:

`X = k ∫ φ(λ) x̄(λ) dλ`

`Y = k ∫ φ(λ) ȳ(λ) dλ`

`Z = k ∫ φ(λ) z̄(λ) dλ`

where `φ(λ)` is the colour-stimulus function and `k` is the normalization factor appropriate to the measurement convention.

In the CIE 1931 standard colorimetric system, `ȳ(λ)` is identical to the photopic luminous-efficiency function `V(λ)`, so `Y` is proportional to luminance for the relevant emitting-stimulus formulation.

### SYNTHESIS

XYZ is not a set of physical RGB primaries. It is a standardized tristimulus system derived from colour matching and designed to provide a common colorimetric reference.

### STUDIO JUDGMENT

When later studying sRGB, Display P3, Rec.2020, Lab, Oklab, ICC, or HDR, XYZ should be treated as one of the central reference bridges that prevents those systems from becoming a collection of unrelated numeric recipes.

## SOURCE — chromaticity coordinates remove scale

CIE defines chromaticity coordinates as the quotient of each tristimulus value by the sum of the three:

`x = X / (X + Y + Z)`

`y = Y / (X + Y + Z)`

`z = Z / (X + Y + Z)`

and `x + y + z = 1`, so two coordinates are sufficient to specify chromaticity.

### SYNTHESIS

Chromaticity describes the proportional relationship of the tristimulus values, not their overall magnitude. Two stimuli can share the same chromaticity while having different luminance.

### STUDIO JUDGMENT

A chromaticity diagram is therefore not a complete picture of perceived colour. Reading a gamut triangle only as 'which colours exist' ignores luminance, adaptation, appearance, transfer functions, and viewing conditions.

## SOURCE — standard illuminants are spectral references

ISO/CIE 11664-2:2022 defines standard illuminants A, D65, and D50.

- A represents typical tungsten-filament illumination, approximately 2856 K Planckian radiation.
- D65 represents average daylight with correlated colour temperature around 6500 K.
- D50 represents daylight around 5000 K and is extensively used in graphic arts and photography.

The standard provides their relative spectral power distributions at 1 nm intervals from 300 nm to 830 nm.

### SYNTHESIS

A white point label such as D65 is not merely a pair of `x,y` coordinates. The standard illuminant is defined by a spectral distribution; chromaticity is a reduced colorimetric description of it.

### STUDIO JUDGMENT

When a UI specification says 'D65' in a color-space definition, the studio should understand what role that white point plays instead of treating it as decorative technical metadata. When physical materials are involved, spectral mismatch under different illumination must be investigated explicitly.

## SOURCE — metamerism proves that equal tristimulus values do not imply equal spectra

CIE S 017 defines metameric colour stimuli as spectrally different stimuli having the same tristimulus values in a specified colorimetric system. The corresponding property is metamerism.

### SYNTHESIS

Human trichromatic matching compresses spectral information. Different spectra can map to the same colorimetric triplet under a specified observer/system.

Consequences:

- matching XYZ does not establish matching spectra;
- two physical samples can match under one illuminant and diverge under another;
- different observers can experience mismatches differently;
- display primaries can reproduce a visual match without reproducing an object's spectrum.

### STUDIO JUDGMENT

'Same HEX' and 'same colour' are not interchangeable statements across different physical and display systems. Digital brand governance should specify reproduction conditions; physical brand governance must add illumination/material/print evidence where relevant.

## SOURCE — colorimetry is not the whole of appearance

CIE 015:2018 includes advanced colorimetry and colour-appearance models. CIE 248:2022 defines CIECAM16 as a viewing-condition-specific transformation between XYZ and perceptual-attribute correlates for related colours.

Reference:

- CIE 248:2022, *The CIE 2016 Colour Appearance Model for Colour Management Systems: CIECAM16*: https://www.cie.co.at/publications/cie-2016-colour-appearance-model-colour-management-systems-ciecam16

### SYNTHESIS

Tristimulus equality under a standard system does not by itself model every appearance effect. Surround, adaptation, luminance level, and viewing conditions matter.

### STUDIO JUDGMENT

For UI practice, this means numerical contrast and color-space coordinates are necessary evidence but not sufficient evidence. Real interface context and real viewing conditions remain part of validation.

## Product implications for MintTap Design Studio

1. Never publish an implementation colour value without an explicit color-space assumption when ambiguity matters.
2. Separate `encoded RGB value`, `colorimetric coordinate`, `perceptual appearance`, and `brand meaning`; they are different layers.
3. Do not use a gamut diagram alone to argue that one display space is 'better'.
4. Treat white point, transfer behaviour, gamut, and viewing condition as part of a display-colour specification.
5. Treat physical brand samples as illuminant/material-dependent and test metamerism where colour matching is commercially important.
6. Preserve grayscale/luminance/accessibility work from Study 008, but place it on top of this more fundamental colorimetric model.
7. Do not infer universal user perception from the CIE standard observer; use the standard observer as a reproducible engineering model.

## Practice required next

### Exercise A — spectral integration

Using official CIE 1 nm datasets:

1. choose or construct representative spectral stimuli;
2. compute CIE 1931 XYZ through numerical summation;
3. derive `x,y` chromaticity;
4. verify that scaling the spectrum changes XYZ magnitude while preserving chromaticity;
5. document normalization assumptions.

### Exercise B — metamer construction/inspection

Find or construct two spectrally different stimuli that are close in XYZ under one observer/condition, then compare their behaviour under a changed illuminant or observer model. Record what is measurement fact versus appearance inference.

### Exercise C — digital bridge

Convert representative sRGB values through the correct inverse transfer function into linear-light RGB, then into XYZ. This exercise must explicitly distinguish encoded sRGB from linear RGB.

## OPEN

- Numerical integration practice has not yet been completed in the repository.
- Individual-observer variability and observer metamerism need a dedicated advanced study.
- Cone fundamentals and the relationship between LMS-based physiology and historical XYZ colorimetry need a dedicated study.
- Chromatic adaptation transforms require separate treatment before being used in production recommendations.
- CIELAB, colour-difference formulae, Oklab/OkLCh, and perceptual-uniformity limits remain later modules.
- Display characterization, ICC profiles, gamut mapping, P3/Rec.2020, HDR transfer functions, and tone mapping remain later modules.

## Status implication

This study expands the foundation beneath `Color / luminance / contrast`; it does **not** move that domain to PASS. Existing practical colour work remains at CRITIQUE because physical-display bright/low-light and interactive-focus validation are still outstanding, while professional colorimetry now adds new computation/practice requirements.