# Study 011 — LMS Cone Fundamentals and Observer Models

Status: FOUNDATION STUDY / numerical observer comparison and device validation still required before PASS.

## Question

How should a professional product colorist connect human cone physiology to CIE colorimetry without confusing physiological cone responses, standardized colour-matching functions, XYZ coordinates, and perceptual colour appearance?

This study follows `research/010-color-science-colorimetry-foundations.md`. Study 010 established the chain from spectral stimulus to standardized tristimulus values. Study 011 goes one level deeper into the observer model.

## SOURCE — CIE 2006 cone fundamentals

Primary references:

- CIE 170-1:2006, *Fundamental chromaticity diagram with physiological axes — Part 1*: https://www.cie.co.at/publications/fundamental-chromaticity-diagram-physiological-axes-part-1
- CIE official datasets: https://cie.co.at/data-tables
- CIE 2006 LMS cone fundamentals, 2° field: https://cie.co.at/datatable/cie-2006-lms-cone-fundamentals-2-field-size-terms-energy
- CIE 2006 LMS cone fundamentals, 10° field: https://www.cie.co.at/datatable/cie-2006-lms-cone-fundamentals-10-field-size-terms-energy

CIE 170-1:2006 defines physiologically relevant long-wave-, middle-wave-, and short-wave-sensitive cone fundamentals. The report derives 10° cone fundamentals and then derives 2° and intermediate-field fundamentals by accounting for physiological factors including ocular-media absorption, macular pigment, and photopigment optical density.

The report explicitly allows field size from 1° to 10° and includes age-related lens absorption as part of the model.

### SYNTHESIS

`L`, `M`, and `S` are not simply informal names for red, green, and blue display channels. They are standardized spectral sensitivity functions representing the three cone classes within a defined physiological observer model.

The spectral sensitivities seen at the corneal plane are affected by the optical path before photons reach the cone pigments. Field size and age therefore matter because the effective observer is not a fixed set of three wavelength peaks detached from the eye.

### STUDIO JUDGMENT

The studio must avoid statements such as “L cone = red channel” or “RGB is equivalent to LMS.” RGB spaces are engineering coordinate systems defined by specific primaries, white point, and transfer behaviour. LMS is an observer-response model. A linear transform can relate suitable tristimulus coordinate systems, but the meanings of the axes are not interchangeable.

## SOURCE — one cone alone does not encode wavelength identity

Authoritative educational references:

- NCBI Bookshelf, *Neuroscience — Cones and Color Vision*: https://www.ncbi.nlm.nih.gov/books/NBK11059/
- NCBI Bookshelf, *Webvision — Visual Responses of Ganglion Cells*: https://www.ncbi.nlm.nih.gov/books/NBK11550/

The neuroscience literature explains a central principle of trichromacy: the response of an individual cone reflects photon capture but does not, by itself, uniquely identify wavelength. Many photons at a less-sensitive wavelength can produce a response similar to fewer photons near that cone's region of higher sensitivity. Colour information therefore depends on comparisons among cone classes.

Retinal processing subsequently combines cone signals into luminance-like and colour-opponent pathways. This means the three cone responses are an early encoding stage, not a complete description of perceived hue.

### SYNTHESIS

Trichromacy gives a three-dimensional matching structure, but colour appearance is not obtained by reading `L`, `M`, and `S` values independently. Post-receptoral comparison, adaptation, spatial context, and later neural processing all matter.

### STUDIO JUDGMENT

LMS should be used as a physiological foundation, not as a simplistic user-interface palette model. A product colorist may use LMS-based models to understand observer variation and colour matching, but product hierarchy and appearance still require contextual and perceptual validation.

## SOURCE — CIE 2015 cone-fundamental-based colorimetry

Primary reference:

- CIE 170-2:2015, *Fundamental Chromaticity Diagram with Physiological Axes — Part 2: Spectral Luminous Efficiency Functions and Chromaticity Diagrams*: https://www.cie.co.at/publications/fundamental-chromaticity-diagram-physiological-axes-part-2-spectral-luminous

CIE 170-2 provides practical colorimetric tools based on the cone fundamentals. It defines cone-fundamental-based spectral luminous-efficiency functions and presents linear transformations from cone fundamentals to `X_F, Y_F, Z_F` tristimulus values and `x_F, y_F` chromaticity coordinates.

Related official datasets include:

- CIE cone-fundamental-based spectral tristimulus values, 2° field: https://cie.co.at/datatable/cie-cone-fundamental-based-spectral-tristimulus-values-2-degree-field-size
- CIE cone-fundamental-based spectral luminous-efficiency function, 2° field: https://cie.co.at/datatable/cie-cone-fundamental-based-spectral-luminous-efficiency-function-2-field-size-terms-energy

### SYNTHESIS

Modern physiologically based colorimetry does not discard the idea of tristimulus coordinates. Instead, it rebuilds practical colorimetric coordinates from physiologically meaningful cone fundamentals.

A linear transformation can change coordinates while preserving the three-dimensional colour-matching information within the assumptions of the observer model.

### STUDIO JUDGMENT

A newer observer model is not automatically a drop-in replacement for every existing RGB, ICC, CSS, accessibility, or device standard. Production specifications are defined against particular standards. Replacing the observer ad hoc would break interoperability even if the newer model is physiologically more informative.

The correct professional behaviour is:

1. use the observer required by the specification when conformance/interoperability is the task;
2. use modern cone-fundamental models when studying observer physiology, mismatch, field-size effects, or advanced colour science;
3. document explicitly when the two are being compared.

## SOURCE — normal observer variation matters

Primary reference:

- CIE 254:2024, *A roadmap toward basing CIE colorimetry on cone fundamentals*: https://www.cie.co.at/publications/roadmap-toward-basing-cie-colorimetry-cone-fundamentals

CIE 254:2024 proposes a future complete, self-consistent cone-fundamental-based CIE colorimetric framework. The roadmap explicitly calls out normal variation caused by:

- age;
- field of view;
- individual diversity.

It proposes further work on LMS-based measures, an approximately uniform LMS-based colour space, a global study of cone-fundamental diversity, and the colorimetric effects of that diversity.

### SYNTHESIS

The “standard observer” is an engineering reference observer, not a claim that all people with nominally normal colour vision have identical cone fundamentals.

Observer metamerism follows from this: two stimuli that match for one observer model can mismatch for another observer whose spectral sensitivities differ.

### STUDIO JUDGMENT

MintTap Design Studio must not treat a single colorimetric coordinate or one designer's calibrated display as proof of universal appearance. The standard observer gives reproducibility; user diversity still requires robust hierarchy, redundancy, accessibility, and real-device testing.

This is particularly important for:

- narrow-band or highly saturated display primaries;
- wide-gamut display work;
- spectral matches between emissive screens and reflective materials;
- brand colours whose identity depends on very small hue differences;
- products used by broad age groups.

## Observer-model decision framework

### CIE 1931 2° standard observer

Use when the governing standard or color-space definition requires the traditional CIE 1931 framework. It remains embedded in a large amount of current device, web, imaging, and color-management infrastructure.

Do not interpret this as proof that a 2° model perfectly predicts large-screen appearance.

### CIE 1964 10° supplementary standard observer

Use when a relevant standard or measurement problem specifies the 10° observer and larger fields are the intended colorimetric condition.

Do not substitute it silently into color spaces whose matrices/primaries were defined in the 1931 system.

### CIE 2006 LMS / cone-fundamental-based CIE 2015 tools

Use for physiologically grounded analysis of cone responses, field-size/age modelling, observer effects, and advanced colorimetric research.

Do not call it a universal “better RGB” or a product-token space.

## Critical distinctions

### LMS is not RGB

- **RGB**: device/encoding coordinate system tied to specified primaries, white, and transfer function.
- **LMS**: cone-fundamental response coordinates tied to an observer model.

### LMS is not opponent colour space

Cone fundamentals describe receptor-level spectral sensitivities. Opponent processing compares cone signals in later neural pathways. Therefore `L-M` and `S-(L+M)`-type relationships are useful conceptual models of opponent signals, but raw `L`, `M`, `S` axes themselves are not “redness”, “greenness”, and “blueness”.

### XYZ is not physiological cone excitation

XYZ is a standardized tristimulus coordinate system. It was designed for colorimetric convenience and interoperability, not as literal cone-isomerization counts.

### A colour match is observer-conditional

Metamerism and observer variation mean “matching coordinates” always carry assumptions about the observer and condition.

## Product implications for MintTap Design Studio

1. Keep the current production color-space standard intact when shipping UI assets or tokens; do not replace established RGB/ICC definitions with experimental observer coordinates.
2. Use cone-fundamental knowledge to diagnose why apparently equivalent colours can diverge across field size, observer, material, or spectral-primary conditions.
3. Treat age and field size as genuine visual-system variables when evaluating products intended for large displays, tablets/EFBs, or broad age ranges.
4. Preserve semantic redundancy: physiologically sophisticated colorimetry does not make color-only communication acceptable.
5. For brand governance, separate three questions: “same encoded value?”, “same standard-observer colorimetry?”, and “same appearance to representative users?”
6. For future P3/HDR studies, explicitly ask whether narrower display spectra and higher luminance expose observer-variation issues that are invisible in simple sRGB swatch review.

## Practice completed in this block

A conceptual observer-model decision test was applied to four cases:

| Case | Required model / evidence | Rejected shortcut |
| --- | --- | --- |
| CSS/sRGB token conversion | Follow the standardized sRGB/XYZ definition used by the platform/spec | Replace the observer model because a newer physiological model exists |
| Large colour-field laboratory comparison | Use the observer specified by the measurement protocol; investigate 10° or cone-fundamental tools when appropriate | Assume 2° results automatically predict all large-field perception |
| Physical brand sample vs emissive display | Standard colorimetry plus spectral/illuminant and observer-mismatch investigation | Approve solely because HEX or nominal XYZ matches |
| UI warning/status state | Accessible luminance/geometry/text redundancy plus device/context validation | Assume precise colorimetry makes hue-only state communication robust |

**KEEP:** model selection is driven by the task and governing standard.

**REJECT:** “newer = universally replace older”.

**REJECT:** “LMS is a palette space”.

**REWORK:** future wide-gamut/HDR exercises must add explicit observer-diversity stress cases.

## OPEN

- Official CIE 1 nm datasets have been located and their dataset pages/checksums identified, but the raw CSV files were not retrievable through the current execution environment in this work block. No spectral-integration result is claimed without those values.
- Numerical comparison of CIE 1931, CIE 1964, and cone-fundamental-based observers remains to be executed on the same spectra.
- Individual-observer models beyond the standard age/field framework require a dedicated advanced study.
- Opponent-processing and colour appearance need deeper treatment before any perceptual-uniform-space recommendation is made.
- Chromatic adaptation remains a separate next-stage topic.

## Status implication

This study strengthens the scientific foundation for `Color / luminance / contrast` but does **not** move it to PASS. The next numerical priority remains official spectral integration and observer comparison; the next product-validation priority remains physical-display bright/low-light and interactive-focus testing.