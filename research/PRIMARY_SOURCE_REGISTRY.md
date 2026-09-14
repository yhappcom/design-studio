# Primary Source Registry

Status: ACTIVE — expand as modules progress.

This registry prioritizes first-party/authoritative sources. Secondary commentary may be used for orientation but cannot silently replace primary evidence.

## Type design / typography education

### University of Reading — MA Communication Design: Typeface Design Pathway
https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-typeface-design

Why it matters: combines practical skill with historical/theoretical study and explicitly frames typeface work as defining, planning, and designing a family, including character complement and multiscript relationships.

### KABK — Master Type and Media
https://www.kabk.nl/en/programmes/master/type-and-media

Why it matters: explicitly covers contrast, rhythm, proportion, weight, type history, font technology, digitising, and tool development across print, screens, and interactive media.

## Font technology

### Microsoft — OpenType Specification 1.9.1
https://learn.microsoft.com/en-us/typography/opentype/spec/

Why it matters: authoritative technical model for outlines, Unicode mapping, layout behavior, metrics, variation, and TrueType instructions/rasterization-related structures.

### Glyphs Learn / Handbook
https://glyphsapp.com/learn
https://handbook.glyphsapp.com/

Study use: spacing, kerning, sketching/drawing, interpolation, variable fonts, proofing, and production workflow. Individual articles must be cited in the study where used.

### Google Fonts Guide
https://googlefonts.github.io/gf-guide/

Study use: outline quality, variable fonts, production, build reproducibility, tools, and QA. Individual pages must be cited in the study where used.

### fontTools
https://fonttools.readthedocs.io/

Study use: font engineering, inspection, variation/build tooling, and reproducible production literacy.

## Color science / colorimetry

### CIE 015:2018 — Colorimetry, 4th Edition
https://www.cie.co.at/publications/colorimetry-4th-edition

Why it matters: central CIE recommendation covering standard observers, standard illuminants, tristimulus and chromaticity calculations, colour spaces, colour differences, viewing conditions, and advanced colorimetry.

### ISO/CIE 11664-1:2019 — CIE standard colorimetric observers
https://www.cie.co.at/publications/colorimetry-part-1-cie-standard-colorimetric-observers-0

Why it matters: normative definition of the CIE 1931 and CIE 1964 colour-matching functions and their intended field-size/adaptation conditions.

### ISO/CIE 11664-2:2022 — CIE Standard Illuminants
https://www.cie.co.at/publications/colorimetry-part-2-cie-standard-illuminants-0

Why it matters: normative spectral definitions and intended use of standard illuminants A, D65, and D50.

### ISO/CIE 11664-3:2019 — CIE tristimulus values
https://www.cie.co.at/publications/colorimetry-part-3-cie-tristimulus-values-2

Why it matters: normative calculation procedure for deriving tristimulus values from spectral colour-stimulus data, including sampling-range and interval requirements.

### ISO/CIE 11664-4:2019 — CIE 1976 L*a*b* colour space
https://www.cie.co.at/publications/colorimetry-part-4-cie-1976-lab-colour-space-1

Why it matters: normative CIELAB coordinate definition, lightness/chroma/hue correlates, and baseline Euclidean colour-difference framework.

### ISO/CIE 11664-6:2022 — CIEDE2000 Colour-Difference Formula
https://www.cie.co.at/publications/colorimetry-part-6-ciede2000-colour-difference-formula-1

Why it matters: current CIE/ISO definition of CIEDE2000, correcting known non-uniformity in simple CIELAB distance with lightness, chroma, hue, and interaction terms under specified reference conditions.

### CIE 230:2019 — Validity of Formulae for Predicting Small Colour Differences
https://www.cie.co.at/publications/validity-formulae-predicting-small-colour-differences

Why it matters: compares multiple colour-difference formulae against visual datasets, including small differences, and reinforces that formula validity is empirical and condition-dependent.

### CIE 170-1:2006 — Fundamental chromaticity diagram with physiological axes, Part 1
https://www.cie.co.at/publications/fundamental-chromaticity-diagram-physiological-axes-part-1

Why it matters: defines the CIE 2006 physiologically relevant LMS cone fundamentals and the field-size, ocular-media, macular-pigment, photopigment-density, and age factors used to derive them.

### CIE 170-2:2015 — Fundamental chromaticity diagram with physiological axes, Part 2
https://www.cie.co.at/publications/fundamental-chromaticity-diagram-physiological-axes-part-2-spectral-luminous

Why it matters: provides practical cone-fundamental-based colorimetric tools, including spectral luminous-efficiency functions and linear transformations from cone fundamentals to XF/YF/ZF and xF/yF coordinates.

### CIE 254:2024 — A roadmap toward basing CIE colorimetry on cone fundamentals
https://www.cie.co.at/publications/roadmap-toward-basing-cie-colorimetry-cone-fundamentals

Why it matters: current CIE roadmap for a future self-consistent cone-fundamental-based colorimetry, explicitly addressing normal variation from age, field of view, and individual diversity.

### CIE 160:2004 — A review of chromatic adaptation transforms
https://www.cie.co.at/publications/review-chromatic-adaptation-transforms

Why it matters: authoritative review of chromatic-adaptation experiments, datasets, and multiple CAT formulations; prevents treating any one CAT as a universal perceptual law.

### CIE official colorimetric datasets
https://cie.co.at/data-tables

Study use: authoritative 1 nm colour-matching functions, chromaticity data, standard illuminants, LMS cone fundamentals, and related numerical datasets for reproducible exercises.

### CIE S 017:2020 — International Lighting Vocabulary / e-ILV
https://cie.co.at/e-ilv

Study use: normative terminology for colour stimulus, stimulus function, metamerism, chromaticity, adapted white, and related concepts. Definitions should be checked here rather than reconstructed from secondary glossaries.

### CIE 248:2022 — CIECAM16
https://www.cie.co.at/publications/cie-2016-colour-appearance-model-colour-management-systems-ciecam16

Why it matters: authoritative viewing-condition-specific colour appearance model; used later to distinguish tristimulus specification from appearance prediction.

### NCBI Bookshelf — Neuroscience / Webvision colour-vision chapters
https://www.ncbi.nlm.nih.gov/books/NBK11059/
https://www.ncbi.nlm.nih.gov/books/NBK11550/

Study use: authoritative neuroscience background for the principle of univariance at individual cones and for post-receptoral comparison/opponent processing. These sources support physiology education; CIE remains the colorimetric authority.

### International Color Consortium — ICC.1:2022 v4.4
https://www.color.org/icc-1_specification/

Why it matters: current ICC v4 profile architecture and profile-connection-space model for device-independent colour management; a later production module will study PCSXYZ/PCSLAB, profiles, rendering, and HDR-related metadata in detail.

### ICC Technical Note 02-2003 — D65 to D50 chromatic-adaptation tag
https://www.color.org/chadtag/

Why it matters: publishes the linearized Bradford D65→D50 matrix used for ICC v4 profile-building practice and shows explicitly how non-D50 source colorimetry is adapted to the D50 PCS.

### ICC — Why is the media white point of a display profile always D50?
https://www.color.org/whyd50/

Study use: authoritative explanation of the D50 profile connection space, adopted-white normalization, and the role of the `chad` tag in display profiles.

### W3C — CSS Color Module Level 4
https://www.w3.org/TR/css-color-4/

Why it matters: current web-platform definition of sRGB, linear-light RGB, Display P3, CIE Lab/LCH, Oklab/OkLCh, XYZ conversion paths, and modern CSS colour syntax. Use as platform specification, not as a replacement for CIE measurement standards.

### Björn Ottosson — Oklab primary author documentation
https://bottosson.github.io/posts/oklab/

Study use: primary derivation, matrices, intended image-processing properties, and design rationale for Oklab. Oklab is useful for modern digital authoring but is not itself a CIE standard.

### Sharma, Wu, Dalal — CIEDE2000 implementation notes and test data
https://hajim.rochester.edu/ece/sites/gsharma/ciede2000/

Study use: peer-reviewed implementation guidance and supplemental test data for detecting common CIEDE2000 coding errors. It is not an official CIE implementation and must be identified as such.

## Product / interaction / visual design

### Apple Human Interface Guidelines
https://developer.apple.com/design/human-interface-guidelines

Why it matters: first-party platform guidance covering accessibility, color, layout, materials, typography, patterns, components, and inputs. Use as platform evidence, not as a universal visual style.

### W3C — WCAG 2.2
https://www.w3.org/TR/WCAG22/

Why it matters: normative accessibility reference for contrast, text adaptation, reflow, focus, target size, and non-color-dependent communication.

### Wagemans et al. (2012) — A Century of Gestalt Psychology in Visual Perception I
https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/
https://pubmed.ncbi.nlm.nih.gov/22845751/

Why it matters: peer-reviewed modern synthesis of classical and later perceptual-grouping and figure-ground research. It prevents reducing Gestalt theory to a simplified design-school checklist and documents interactions among proximity, similarity, common region, uniform connectedness, contour grouping, attention, depth, and border ownership.

### Kubovy, Holcombe & Wagemans (1998) — On the Lawfulness of Grouping by Proximity
https://pubmed.ncbi.nlm.nih.gov/9520318/

Why it matters: quantitative evidence that proximity grouping strength changes systematically with relative distance in the studied dot-lattice paradigm. Use to support relational spacing reasoning, not to invent universal UI pixel thresholds.

### Palmer (1992) — Common Region: A New Principle of Perceptual Grouping
https://pubmed.ncbi.nlm.nih.gov/1516361/

Why it matters: original peer-reviewed evidence that shared spatial regions can provide a grouping factor independent of proximity and similarity and can participate in hierarchical perceptual organization.

### Palmer & Rock (1994) — Rethinking Perceptual Organization: The Role of Uniform Connectedness
https://pubmed.ncbi.nlm.nih.gov/24203413/

Why it matters: original theoretical and experimental work on uniform connectedness as an early perceptual-unit formation principle. Useful when reasoning about joined surfaces, segmented controls, paths, and when visual connection changes the apparent object structure.

## Graduate design education references

Planned primary review:

- Yale School of Art — Graphic Design MFA
- Carnegie Mellon School of Design — MDes / Design for Interactions
- University of Reading — Communication Design pathways and research methods

These references are used to benchmark depth of study, critique, theory, and authorship; they are not product-design prescriptions.

## Source-use rule

Every research note must distinguish:

- **SOURCE** — what the reference explicitly says;
- **SYNTHESIS** — the transferable principle inferred across sources;
- **STUDIO JUDGMENT** — our design position or method;
- **OPEN** — what still requires evidence.
