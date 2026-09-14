# Study 012 — Chromatic Adaptation and White-Point Transforms

Status: FOUNDATION STUDY / production validation and broader CAT comparison still required before PASS.

## Question

Why can a D65-referenced colour not be converted to a D50-referenced colour by simply relabelling its XYZ values, and what does a professional colorist need to know before moving colours between viewing conditions or ICC profile connection spaces?

## SOURCE — chromatic adaptation is a corresponding-colour problem

Primary references:

- CIE 160:2004, *A review of chromatic adaptation transforms*: https://www.cie.co.at/publications/review-chromatic-adaptation-transforms
- CIE 248:2022, *The CIE 2016 Colour Appearance Model for Colour Management Systems: CIECAM16*: https://www.cie.co.at/publications/cie-2016-colour-appearance-model-colour-management-systems-ciecam16
- ICC.1:2022 v4 specification: https://www.color.org/icc-1_specification/
- ICC FAQ on D50/D65 conversion: https://www.color.org/faqs/

CIE 160 reviews chromatic-adaptation experiments and thirteen chromatic adaptation transforms. The report makes clear that chromatic adaptation is not solved by one historically inevitable matrix; different transforms model corresponding colours under changed adaptation conditions with different assumptions.

CIECAM16 goes further by embedding chromatic adaptation inside a viewing-condition-specific colour appearance model.

### SYNTHESIS

A white point is not merely metadata attached after XYZ calculation. Changing the adopted white changes the visual adaptation state against which a colour is interpreted. A corresponding-colour transform attempts to predict what XYZ values under one adopted white correspond visually to values under another adopted white.

### STUDIO JUDGMENT

“D65 XYZ” and “D50 XYZ” are not interchangeable coordinate labels. A production pipeline must name the source reference condition and the transform used to move into the destination reference condition.

## SOURCE — ICC v4 uses a D50 PCS

Primary references:

- ICC.1:2022, Annex E: https://www.color.org/specifications/ICC.1-2022-05.pdf
- ICC explanation of D50 display-profile white: https://www.color.org/whyd50/
- ICC Technical Note 02-2003, D65→D50 `chad` tag: https://www.color.org/chadtag/

ICC.1 v4 uses D50 as its profile connection space adopted white. When source colourimetry is referenced to another adopted white such as D65, the data are chromatically adapted to D50. The profile records the chromatic adaptation matrix in the `chad` tag where applicable.

ICC documents the linearized Bradford transform for this purpose. For the historical CIE/ICC white values used by the technical note:

`D65 = [95.04, 100, 108.89]`

`D50 = [96.42, 100, 82.49]`

and the Bradford cone-response matrix is:

```text
[ 0.8951  0.2664 -0.1614 ]
[-0.7502  1.7135  0.0367 ]
[ 0.0389 -0.0685  1.0296 ]
```

The resulting published D65→D50 floating-point adaptation matrix is:

```text
[ 1.04790738171017   0.0229333845542104  -0.0502016347980104 ]
[ 0.0296059594177168 0.990456039910785   -0.01707552919587   ]
[-0.00924679432678241 0.0150626801401488  0.751791232609078 ]
```

### SYNTHESIS

ICC's D50 PCS is a connection convention that makes profile linking unambiguous. It does not mean every source device or display is physically D50.

### STUDIO JUDGMENT

For MintTap production work, “convert to ICC PCS” must not be described as a simple XYZ matrix from RGB primaries alone. If the RGB space is D65-referenced and the ICC PCS is D50, chromatic adaptation is a separate and explicit step.

## SOURCE — Bradford is important, but not universal

CIE 160:2004 reviewed multiple chromatic adaptation transforms and did not identify one transform as universally superior for every context. ICC nevertheless standardizes a linearized Bradford procedure for its v4 architecture because interoperability requires a defined convention.

CIE's current technical work also continues to examine incomplete chromatic adaptation, especially for low-CCT and off-Planckian whites.

Reference:

- CIE JTC 16, *Validity of Chromatic Adaptation*: https://cie.co.at/technicalcommittees/validity-chromatic-adaptation

### SYNTHESIS

There are two different questions:

1. **Which transform is mandated by a production standard?**
2. **Which model best predicts human corresponding-colour appearance for a research condition?**

The answers need not be identical.

### STUDIO JUDGMENT

Use the standard-mandated transform for conformance. Use comparative appearance models for research. Do not replace the production transform merely because another CAT appears newer or perceptually stronger in a paper.

## Practical implications

1. sRGB is D65-referenced; ICC v4 PCS is D50-referenced.
2. sRGB → linear RGB → XYZ D65 is not yet the same as sRGB → ICC PCSXYZ.
3. D65→D50 adaptation must be applied before claiming D50 PCSXYZ.
4. A profile's `chad` information records how source colorimetry was adapted; it is not decorative metadata.
5. White-point adaptation changes all three XYZ coordinates of most colours; it is not a “white-only” correction.
6. A successful numerical CAT does not prove appearance in arbitrary surrounds or luminance levels; full colour-appearance modelling and real viewing tests remain separate.

## Product implications for MintTap Design Studio

- UI design tokens should retain their native color-space definitions rather than being manually pre-adapted for ICC unless an asset-production workflow explicitly requires it.
- Print/export/marketing pipelines that cross D65 display design and D50 ICC/graphic-arts workflows must document adaptation and profile handling.
- Brand colour QA should distinguish encoded RGB equality, ICC conversion fidelity, and perceived appearance under the actual viewing condition.
- For physical/digital brand matching, illuminant adaptation and metamerism must be tested together rather than separately assumed away.

## OPEN

- CAT02, CAT16, CMCCAT2000, and Bradford need a controlled comparison on common data before any research preference is stated.
- Partial/incomplete adaptation needs an advanced study.
- Mixed illumination is not covered by this foundation block.
- Real ICC-profile round trips and soft-proof behaviour remain to be validated with production tools.
- This study does not replace the pending official CIE spectral integration exercise.

## Status implication

Chromatic-adaptation literacy has moved from OPEN to studied foundation. The broader colour domain remains `CRITIQUE`, not `PASS`, because spectral observer comparison, real-device environmental tests, and production-profile validation are still outstanding.
