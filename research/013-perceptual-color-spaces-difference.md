# Study 013 — Perceptual Colour Spaces and Colour Difference

Status: FOUNDATION STUDY / controlled visual and production validation still required before PASS.

## Question

How should a professional product colorist move from XYZ colorimetry into perceptual colour coordinates and numerical colour-difference measures without confusing a useful model with a universal measure of appearance, accessibility, or brand acceptability?

This study follows:

- `research/010-color-science-colorimetry-foundations.md`
- `research/011-lms-cone-fundamentals-observer-models.md`
- `research/012-chromatic-adaptation-white-points.md`

## SOURCE — CIELAB is a more-nearly uniform object-colour space, not a perfect perceptual map

Primary reference:

- ISO/CIE 11664-4:2019, *Colorimetry — Part 4: CIE 1976 L*a*b* colour space*: https://www.cie.co.at/publications/colorimetry-part-4-cie-1976-lab-colour-space-1

ISO/CIE 11664-4 specifies the calculation of CIE 1976 L*a*b* coordinates and the associated lightness, chroma, and hue correlates. It is built from CIE tristimulus values relative to a reference white and was standardized because XYZ and xyY are not sufficiently visually uniform for simple geometric distance to track perceived colour difference well.

The standard nevertheless describes CIELAB as a more-nearly uniform space, not as a claim of perfect perceptual uniformity.

### SYNTHESIS

CIELAB changes the coordinate geometry of colorimetry so that equal numerical changes are intended to relate more closely to equal perceived changes than equal XYZ changes do.

The axes have different roles:

- `L*` — lightness correlate;
- `a*` — approximately green↔red opponent direction;
- `b*` — approximately blue↔yellow opponent direction.

The cylindrical representation CIELCh is derived from the same coordinates:

`C* = sqrt(a*^2 + b*^2)`

`h = atan2(b*, a*)`

CIELCh is therefore a coordinate re-expression of CIELAB, not a new underlying colour model.

### STUDIO JUDGMENT

For MintTap Design Studio, CIELAB/CIELCh should be treated as a colorimetric/perceptual working model, not as a palette oracle. A constant `L*`, `C*`, or `h` does not prove identical visual appearance across all hues, surrounds, luminance levels, displays, or users.

## SOURCE — ΔE*ab / CIE76 is simple Euclidean distance

ISO/CIE 11664-4 includes Euclidean distance in CIELAB as a basic colour-difference measure:

`ΔE*ab = sqrt((ΔL*)^2 + (Δa*)^2 + (Δb*)^2)`

### SYNTHESIS

The strength of ΔE*ab is simplicity and interpretability. Its weakness is that residual non-uniformity in CIELAB means equal numerical distances do not always correspond to equal perceived differences.

### STUDIO JUDGMENT

ΔE*ab is useful as a diagnostic baseline. It should not be treated as the final acceptance metric for every colour-matching problem.

## SOURCE — CIEDE2000 corrects known non-uniformity

Primary references:

- ISO/CIE 11664-6:2022, *Colorimetry — Part 6: CIEDE2000 Colour-Difference Formula*: https://www.cie.co.at/publications/colorimetry-part-6-ciede2000-colour-difference-formula-1
- CIE 230:2019, *Validity of Formulae for Predicting Small Colour Differences*: https://www.cie.co.at/publications/validity-formulae-predicting-small-colour-differences

ISO/CIE 11664-6 defines CIEDE2000 as an extension of the CIE 1976 L*a*b* colour-difference formula. It introduces corrections for the non-uniform behaviour of perceived differences with lightness, chroma, hue, and chroma–hue interaction.

CIE 230:2019 compares multiple colour-difference formulae against visual datasets, including small colour differences below 2 CIELAB units, reinforcing that formula performance must be evaluated against psychophysical evidence rather than assumed from coordinate geometry.

### SYNTHESIS

CIEDE2000 is not simply a different colour space. It is a difference formula operating on CIELAB coordinates with additional weighting and interaction terms.

This means:

- two pairs with the same ΔE*ab can have different ΔE00;
- a ranking of “which pair is closer” can change between formulas;
- the formula encodes empirical knowledge about where CIELAB is more or less perceptually stretched.

### Critical scope limit

ISO/CIE 11664-6 is framed for colour stimuli perceived as reflecting or transmitting objects, including displays when they simulate such objects and are appropriately normalized. It is not a universal law for arbitrary self-luminous interface patches viewed as primary light sources.

### STUDIO JUDGMENT

For UI work, ΔE00 can be informative for colour comparison, but it must not be presented as a universal UI visibility, accessibility, or semantic-distinguishability metric.

WCAG contrast and non-colour redundancy answer different questions.

## SOURCE — CIELAB and CIEDE2000 are not contrast metrics

Relevant normative accessibility source:

- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/

WCAG text and non-text contrast are based on relative luminance contrast, not perceptual colour-difference formulas such as ΔE*ab or ΔE00.

### SYNTHESIS

A pair of colours may have a measurable perceptual hue/chroma difference while still having poor luminance contrast for text or boundaries. Conversely, two neutrals may have strong luminance contrast while their chroma difference is effectively zero.

### STUDIO JUDGMENT

Never substitute ΔE for WCAG contrast. Never substitute WCAG contrast for colour-match fidelity. They measure different properties.

## SOURCE — Oklab / OkLCh as a modern D65 perceptual working space

Primary-author and platform references:

- Björn Ottosson, *A perceptual color space for image processing*: https://bottosson.github.io/posts/oklab/
- W3C CSS Color Module Level 4: https://www.w3.org/TR/css-color-4/

Oklab was introduced in 2020 as a perceptual colour space aimed at image-processing operations such as smooth gradients, lightness-preserving adjustments, and more stable hue/chroma manipulation. It uses a D65 white point and a simple non-linear transform from XYZ/linear RGB.

CSS Color 4 now defines `oklab()` and `oklch()` alongside CIE Lab/LCH and notes improved hue, lightness, and chroma behaviour compared with CIELAB/CIELCh for many web-colour operations.

### SYNTHESIS

Oklab and OkLCh solve a different practical problem from CIEDE2000:

- Oklab provides a coordinate space intended to behave more uniformly for common image/UI operations;
- ΔE00 is a CIE-standardized difference formula built on CIELAB for specified colour-difference evaluation conditions.

They are not interchangeable standards.

### STUDIO JUDGMENT

For modern digital product palette construction, interpolation, token generation, and controlled chroma/lightness edits, OkLCh is a strong candidate working space.

For formal colour-difference reporting, manufacturing/print tolerances, or workflows governed by CIE/ISO requirements, use the formula required by that workflow rather than substituting ΔEOK because it is computationally simpler.

## Gamut remains a separate problem

Neither CIELCh nor OkLCh guarantees that a requested coordinate is inside sRGB, Display P3, or another output gamut.

Therefore a palette operation such as “hold hue and lightness, increase chroma” can eventually create an out-of-gamut colour.

### STUDIO JUDGMENT

Perceptual coordinates improve authoring logic; they do not remove the need for explicit gamut checking and gamut mapping.

Future MintTap color-token tooling should distinguish:

1. authoring space;
2. target output gamut;
3. gamut-mapping policy;
4. final encoded RGB value.

## Decision framework

### Use CIELAB / CIELCh when

- the workflow is tied to CIE/ICC object-colour practice;
- D50/D65 adaptation and reference-white handling are explicitly managed;
- compatibility with established colour-measurement workflows matters.

### Use CIEDE2000 when

- a governed workflow calls for CIEDE2000;
- small object-colour differences need a better perceptual correlation than raw ΔE*ab;
- the reference conditions and stimulus class are appropriate.

### Use Oklab / OkLCh when

- digital palette authoring, interpolation, gradients, or token generation benefit from more regular hue/lightness/chroma behaviour;
- D65-aligned digital work makes the space operationally convenient;
- the result will still be gamut-checked in the target output space.

### Use WCAG contrast when

- the question is legibility or visibility of text, UI boundaries, or focus/state cues under WCAG-defined accessibility criteria.

Do not replace one category with another merely because all of them produce numbers.

## Product implications for MintTap Design Studio

1. Palette generation may use OkLCh as an authoring aid, but release values remain explicit sRGB/P3/etc. encodings.
2. Brand-colour QA should record which difference formula is used and why.
3. Manufacturing/print tolerance language should use the applicable industry/CIE method, not UI heuristics.
4. Accessibility review must stay anchored to contrast, geometry, text/icon redundancy, and context—not ΔE alone.
5. A colour-pair “distance” should never be published without naming the space/formula.
6. Low-chroma colours need special care because hue angle becomes unstable as chroma approaches zero.
7. Gamut mapping must be documented separately from perceptual-space editing.

## OPEN

- Controlled visual comparison of CIE76, CIEDE2000, and ΔEOK across the same sample pairs is required.
- The studio still needs an explicit gamut-mapping study for sRGB ↔ Display P3 and high-chroma OkLCh values.
- CAM16-UCS and other appearance-model-based uniform spaces remain advanced topics.
- The formal limits of ΔEOK for acceptance tolerances need stronger psychophysical evidence before studio policy is written.
- Physical-display and environmental validation from earlier colour exercises remains outstanding.

## Status implication

Perceptual-space and colour-difference literacy has moved from OPEN to studied foundation. The overall `Color / luminance / contrast` domain remains `CRITIQUE`, not `PASS`.