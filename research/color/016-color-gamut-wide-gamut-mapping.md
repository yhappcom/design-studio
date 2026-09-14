# Study 016 — Color Gamut, Wide-Gamut Authoring, and Gamut Mapping

Status: FOUNDATION / INTERMEDIATE BRIDGE STUDY — numerical practice complete in companion exercise; real-device and cross-platform validation still required before PASS.

## Question

How should a professional product colorist reason about colors that are valid in one color space but cannot be reproduced by a target display, and how should MintTap Design Studio distinguish authoring space, destination gamut, and gamut-mapping policy?

This study follows:

- `research/color/010-color-science-colorimetry-foundations.md`
- `research/color/012-chromatic-adaptation-white-points.md`
- `research/color/013-perceptual-color-spaces-difference.md`

## SOURCE — a valid color may still be outside a device gamut

Primary source:

- W3C CSS Color Module Level 4, Candidate Recommendation Draft, 6 August 2026: https://www.w3.org/TR/css-color-4/

CSS Color 4 distinguishes validity from reproducibility. A color value may be syntactically and colorimetrically valid while still lying outside the range that a particular output device can reproduce. The specification calls that condition `out of gamut` for the destination device.

The specification also defines multiple RGB spaces, including sRGB, linear-light sRGB, Display P3, linear-light Display P3, A98 RGB, ProPhoto RGB, and Rec.2020, plus XYZ and perceptual spaces.

For Display P3, CSS defines the DCI-P3 primary chromaticities, a D65 white point, and the sRGB transfer curve. Its gamut is larger than sRGB.

### SYNTHESIS

A coordinate is not simply “a color” detached from a destination. Reproducibility is a relation between:

1. a colorimetric color;
2. a source/authoring representation;
3. a destination gamut;
4. a mapping policy when the destination cannot reproduce that color directly.

### STUDIO JUDGMENT

MintTap Design Studio should never use “P3 color” as shorthand for “better color.” Wide gamut creates additional authoring freedom, but it also creates a new failure mode: colors that cannot be faithfully reproduced on a narrower destination.

## SOURCE — Display P3 and extended RGB are distinct concepts

Primary platform sources:

- Apple Developer Documentation — `Color.RGBColorSpace.displayP3`: https://developer.apple.com/documentation/swiftui/color/rgbcolorspace/displayp3
- Apple Developer Documentation — `kCGColorSpaceExtendedDisplayP3`: https://developer.apple.com/documentation/coregraphics/cgcolorspace/extendeddisplayp3
- Apple Developer Documentation — `extendedSRGB`: https://developer.apple.com/documentation/coregraphics/cgcolorspace/extendedsrgb
- Apple Developer Documentation — determining color values with color spaces: https://developer.apple.com/documentation/uikit/determining-color-values-with-color-spaces

Apple defines Display P3 with P3 primaries, D65 white, and the sRGB transfer function. Apple also provides extended-range sRGB/P3 encodings in which component values may be below 0 or above 1.

Extended range is not the same thing as a wider physical display gamut. It is a representation that can preserve color values through conversions without immediately clamping them to the nominal `[0,1]` channel cube.

### SYNTHESIS

Three ideas must stay separate:

- **wide gamut** — the set of reproducible colors is larger;
- **extended range encoding** — component values outside nominal channel bounds can be represented;
- **HDR** — luminance/dynamic-range and transfer-function questions beyond ordinary SDR gamut alone.

### STUDIO JUDGMENT

Do not describe extended sRGB as if it were a new wider-gamut display standard. Do not describe Display P3 as HDR merely because both appear in modern Apple color APIs.

## SOURCE — clipping is the simplest mapping, but can distort hue and lightness

CSS Color 4 describes clipping as converting to the destination RGB space and clamping out-of-range components to their legal bounds.

This is computationally simple, but it does not preserve perceptual relationships. Large out-of-gamut excursions can shift hue, lightness, or chroma substantially.

### SYNTHESIS

Clipping optimizes channel legality, not perceptual fidelity.

### STUDIO JUDGMENT

Naive clipping is acceptable only when the perceptual consequence is known to be negligible for the actual color and task. It should not be the studio default merely because it is easy to implement.

## SOURCE — CSS gamut mapping uses OkLCh-based chroma reduction

CSS Color 4 currently specifies three gamut-mapping algorithms for individual SDR colors destined for RGB displays:

- Binary Search Gamut Mapping with Local MINDE;
- EdgeSeeker;
- Ray Trace.

The specification states that they implement relative-colorimetric behaviour for in-gamut colors, leaving those colors unchanged. For out-of-gamut colors, the algorithms aim for constant-lightness, constant-hue chroma reduction in OkLCh.

The Binary Search with Local MINDE method compares the candidate color with its clipped result using `deltaEOK`, with a JND threshold of `0.02` in the current draft.

### Important status note

CSS Color 4 is a Candidate Recommendation Draft, not a final W3C Recommendation. Its current algorithms are strong interoperability evidence for web production, but the studio must continue tracking changes before treating draft details as immutable universal policy.

### SYNTHESIS

A good gamut-mapping algorithm may deliberately preserve the authoring color until it approaches the actual gamut boundary, then reduce chroma or use a locally clipped result when the perceptual error is below a defined threshold.

### STUDIO JUDGMENT

For MintTap token tooling, OkLCh chroma reduction is a strong candidate mapping strategy for individual UI colors. However, the exact CSS algorithm must not be silently promoted into a universal print, photo, HDR, or brand-production rule.

## SOURCE — image gamut mapping and isolated UI-color mapping are different problems

CSS Color 4 explicitly distinguishes individual color mapping from image mapping. It notes that image reproduction must preserve relationships among neighboring pixels, detail, texture, and tonal structure; a perceptual rendering intent may therefore alter even colors that are individually inside the destination gamut.

ICC likewise defines several rendering intents and explains that perceptual and saturation mappings are profile/vendor-dependent compromises, while colorimetric intents prioritize in-gamut accuracy.

Primary ICC source:

- ICC introduction / profile connection space and rendering intents: https://www.color.org/getting-started/

### SYNTHESIS

The “best mapped color” is not always obtained by minimizing error for each pixel independently.

### STUDIO JUDGMENT

Do not use a UI-token gamut mapper as an image-reproduction engine. UI semantic colors, brand swatches, photographic imagery, charts, print proofs, and HDR video may require different mapping objectives.

## SOURCE — HSL is unsuitable as a perceptual-equality model

CSS Color 4 explicitly notes that HSL hue is not perceptually uniform. Equal angular steps in HSL can produce highly unequal visual hue differences. It also gives the classic lightness failure: saturated sRGB blue and yellow both have HSL `L=50%` even though their visual lightness differs dramatically.

The same specification recommends Oklab when perceptually even interpolation is the goal and OkLCh when retaining chroma through hue-aware interpolation is desirable.

### SYNTHESIS

HSL remains a convenient cylindrical control model around encoded sRGB, but its `H`, `S`, and `L` should not be interpreted as perceptually uniform design dimensions.

### STUDIO JUDGMENT

MintTap should not generate systematic palette ramps by “same HSL saturation, equally spaced lightness” and then assume the result has equal visual hierarchy. HSL can remain an input convenience, not a perceptual specification layer.

## Gamut-mapping decision framework

### Case A — in-gamut sRGB product color

Keep the color unchanged if sRGB is the intended shipping space. Do not introduce a P3 variant solely for novelty.

### Case B — P3 enhancement where sRGB fallback must remain faithful

Maintain a canonical colorimetric/design intent and explicitly define:

- P3 value;
- sRGB fallback or mapped value;
- whether the difference is acceptable for brand identity and UI semantics;
- which version is authoritative when the two cannot match perfectly.

### Case C — OkLCh-authored token outside target gamut

Do not clamp blindly. Compare:

1. naive channel clipping;
2. constant-L/H chroma reduction to the destination boundary;
3. a local-MINDE or platform-standard mapping where available.

Then validate the result visually and semantically.

### Case D — chart/data-viz colors

Preserve category distinguishability and ordering, not only single-color fidelity. If multiple colors map toward the same gamut boundary, re-optimize the set as a system.

### Case E — photography / illustration

Use an image-aware color-management/rendering pipeline. Do not independently map each semantic “palette color” and assume the image will remain coherent.

## Product implications for MintTap Design Studio

1. Every wide-gamut proposal must declare the target color space.
2. A P3-only accent needs an explicit sRGB degradation/fallback review.
3. Gamut mapping is part of the design specification when authoring occurs outside the shipping gamut.
4. The source OkLCh coordinate is not itself the production value; final encoded outputs must be recorded.
5. HSL is not approved as the studio’s perceptual token-generation model.
6. For design systems, preserve semantic relationships across mappings: primary action, warning, success, chart series, and brand accent must remain distinguishable as a set.
7. Extended-range storage should not be mistaken for proof that a target display can reproduce the color.
8. Gamut mapping must be tested together with accessibility. A mapped warning color that preserves hue but loses contrast still fails the product task.

## OPEN

- Real sRGB vs Display P3 device comparison has not yet been completed.
- Browser/platform agreement on current CSS gamut-mapping behaviour needs implementation testing.
- High-chroma OkLCh ramps need real-display inspection for hue/lightness regularity.
- Display P3 → sRGB brand-fidelity tolerances remain product-specific and should not be assigned a universal ΔE threshold.
- HDR, PQ/HLG, EDR, tone mapping, and luminance adaptation remain a later advanced module.
- Multi-color palette gamut optimization for charts needs a dedicated data-visualization exercise.

## Status implication

Wide-gamut and gamut-mapping literacy has moved from OPEN into active professional practice. The overall `Color / luminance / contrast` domain remains `CRITIQUE` pending real-device/environmental validation and broader production evidence.
