# C004 — Spectral Integration, Observer Comparison, and Metamerism Practice

Status: **PRACTICE + REPLICATION / CIE 1931↔1964 constructed-spectrum evidence complete; full-spectrum, current LMS, measured-SPD, and device validation pending**

## Why this study exists

Studies 010 and 011 established the conceptual chain

`spectral stimulus → observer weighting → tristimulus values → chromaticity`

and distinguished standardized observer models from physiological cone fundamentals. Their largest unresolved Foundation gap was numerical practice using CIE spectral data.

This block closes part of that gap with a deliberately bounded question:

> Can two spectrally different stimuli be constructed to match under the CIE 1931 2° observer, and does that match remain when the same spectra are evaluated with the CIE 1964 10° observer?

A second objective is methodological: establish a defensible dataset-provenance procedure instead of silently using whichever public CSV is easiest to retrieve.

This study does **not** claim a measured physical-device metamer, an individual-observer prediction, or a CIE 2006 LMS numerical result.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md`, `research/type/README.md`, especially T003/T004 renderer evidence.
- Reusable finding: Type now provides controlled raster/alpha evidence that can later be combined with Color viewing-condition tests.
- Replication / challenge / transfer opportunity: not required for the spectral calculation itself; later transfer can test whether device/viewing-condition changes alter practical text/color outcomes.
- Dependency or overlap: no Type dependency for the present tristimulus mathematics.

### Color
- Evidence checked: `010-color-science-colorimetry-foundations.md`, `011-lms-cone-fundamentals-observer-models.md`, `012-chromatic-adaptation-white-points.md`, `016-color-gamut-wide-gamut-mapping.md`.
- Reusable finding: observer definition is part of the colorimetric result; equal tristimulus values do not imply equal spectra; production color spaces must continue to use the observer/model required by their governing specification.
- Replication / challenge / transfer opportunity: this study converts the previously conceptual metamerism/observer claims into a controlled numerical proof.
- Dependency or overlap: direct Foundation extension of Studies 010/011.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md`, especially I001 state semantics and Color handoffs.
- Reusable finding: user-facing state meaning must not depend on hue alone.
- Replication / challenge / transfer opportunity: not materially relevant to the spectral integration itself. Later product transfer should preserve non-color state redundancy regardless of observer sophistication.
- Dependency or overlap: none for the current numerical proof.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web owns actual CSS/browser/device application and must follow standardized sRGB/P3/CSS definitions rather than substitute research observer models ad hoc.
- Implementation / application validation opportunity: later wide-gamut/browser/device testing can investigate whether spectral/device differences expose observer-sensitive cases.
- Dependency or overlap: no substantive W### evidence exists yet; browser validation is not claimed here.

### Other / cross-cutting / future specialist
- Evidence checked: CIE 015:2018; ISO/CIE 11664-1:2019; official CIE 1931 2° and CIE 1964 10° dataset records; official CIE 2006 LMS dataset records.
- Reusable finding: standards define the observer and dataset conditions; provenance/version control is part of reproducible colorimetry.
- Dependency or overlap: physical color measurement and individual-observer research remain future evidence needs.

### Overlap decision
- Reuse / deliberate repetition / extension / contradiction review / method comparison / transfer validation / project-specific study: **REPLICATION + EXTENSION + FOUNDATION VALIDATION**.
- Why: Studies 010/011 already state the theory; this block tests it numerically and exposes an important dataset-version/provenance issue.

---

## SOURCE — CIE standard observer data are explicit datasets, not generic lookup tables

Primary references:

- CIE 1931 2° colour-matching functions, DOI `10.25039/CIE.DS.xvudnb9b`
- CIE 1964 10° colour-matching functions, DOI `10.25039/CIE.DS.sqksu2n5`
- ISO/CIE 11664-1:2019, *Colorimetry — Part 1: CIE standard colorimetric observers*
- CIE 015:2018, *Colorimetry, 4th Edition*

The official CIE dataset metadata describe both standard-observer tables at 1 nm spacing over 360–830 nm.

Current CIE-published checksums observed for this study:

- `CIE_xyz_1931_2deg.csv` — MD5 `17cca777db64b17170f06f67ce9d3ab7`
- `CIE_xyz_1964_10deg.csv` — MD5 `cd6135a724480eb8c5e7668bae914445`

### SYNTHESIS

The filename alone is insufficient provenance. Public mirrors can contain older or differently serialized versions of a dataset carrying the same filename.

### STUDIO JUDGMENT

For research-grade numerical Color work, record at least:

- dataset title / observer;
- DOI or governing standard;
- wavelength range and increment;
- published checksum/version information when available;
- retrieval source;
- any discrepancy between the retrieved copy and current authoritative metadata.

Do not silently promote an unverified mirror to “official current CIE data.”

---

## DATASET PROVENANCE AUDIT

Direct retrieval from the CIE file host was unavailable in the current execution environment, so mirrors were inspected against CIE-published metadata.

### CIE 1931 2°

A public mirror carries CIE metadata with the same DOI, 360–830 nm / 1 nm description, and MD5 `17cca777db64b17170f06f67ce9d3ab7`, matching the current CIE-published checksum.

This mirror was used for the sampled 1931 numerical values below.

### CIE 1964 10°

An older public mirror was found whose metadata carried MD5 `6140e032...`, which does **not** match the current CIE-published MD5 `cd6135a724480eb8c5e7668bae914445`. That copy was rejected for the current calculation.

A separate mirror explicitly states that its tables were downloaded from CIE and carries CIE metadata with the current published MD5 `cd6135a724480eb8c5e7668bae914445`. Its sampled rows were used for the 1964 comparison.

### CIE 2006 LMS

The current CIE dataset record publishes MD5 `27c74cc0f98edecadc02fc71f540b116` for the 2° LMS file. A public documented replication attempt was also found reporting a downloaded file whose MD5 did not match that value.

Therefore this study does **not** promote any mirror-based LMS calculation to canonical current-CIE evidence. The current cone-fundamental numerical comparison remains OPEN until a checksum-verified dataset can be obtained or independently hashed in the execution environment.

### Evidence boundary

The checksum comparison above is based on metadata published by CIE and metadata carried by the mirrors. This run did not independently compute the MD5 of the remote raw files locally. It is therefore **provenance-strengthened row-level evidence**, not an independent byte-for-byte checksum certification.

---

## SOURCE — tristimulus integration is linear in the stimulus spectrum

Study 010 records the standard conceptual formulation:

`X = k ∫ φ(λ) x̄(λ) dλ`

`Y = k ∫ φ(λ) ȳ(λ) dλ`

`Z = k ∫ φ(λ) z̄(λ) dλ`

For a 1 nm discrete practice with arbitrary relative line weights and common normalization, the bounded calculation reduces to weighted summation of the sampled colour-matching functions.

This exercise uses idealized 1 nm line bins. It is a mathematical colorimetric specimen, not a claim about the finite bandwidth of real LEDs, displays, or reflective materials.

---

# PRACTICE A — CIE 1931 sparse-spectrum integration

## Sampled 1931 2° CMF rows

| λ (nm) | x̄ | ȳ | z̄ |
| ---: | ---: | ---: | ---: |
| 450 | 0.336200 | 0.038000 | 1.772110 |
| 470 | 0.195360 | 0.090980 | 1.287640 |
| 530 | 0.165500 | 0.862000 | 0.042160 |
| 550 | 0.4334499 | 0.9949501 | 0.008749999 |
| 610 | 1.002600 | 0.503000 | 0.000340 |
| 650 | 0.283500 | 0.107000 | 0.000000 |

Define Spectrum A as three unit-weight narrow line bins:

- 450 nm × 1
- 530 nm × 1
- 610 nm × 1

Then:

`XYZ_A,1931 = [1.504300, 1.403000, 1.814610]`

and

`xy_A,1931 = [0.318578710734, 0.297125527594]`.

### SYNTHESIS

Even this deliberately sparse stimulus demonstrates the basic colorimetric operation: the spectral weights are projected through the observer functions to obtain a three-number match representation.

---

# PRACTICE B — spectrum scaling leaves chromaticity unchanged

Scale every line weight in Spectrum A by `2.5`.

The resulting tristimulus values are:

`XYZ_2.5A,1931 = [3.760750, 3.507500, 4.536525]`.

They are exactly `2.5 × XYZ_A` within numerical precision.

Chromaticity remains:

`xy_2.5A,1931 = [0.318578710734, 0.297125527594]`.

### SYNTHESIS

For the linear tristimulus model, global spectral scaling changes tristimulus magnitude but not normalized chromaticity.

### STUDIO JUDGMENT

This is why an `x,y` coordinate is not a complete specification of stimulus intensity or displayed luminance. Product documents should not treat chromaticity alone as a complete appearance specification.

---

# PRACTICE C — construct a CIE 1931 metamer pair

Spectrum B deliberately uses a different set of wavelengths:

- 470 nm
- 550 nm
- 650 nm

We solve the 3×3 linear system so that its CIE 1931 tristimulus vector equals Spectrum A.

The resulting relative line weights are:

- 470 nm × `1.402623185370`
- 550 nm × `0.975575150354`
- 650 nm × `2.848044384984`

Evaluation under CIE 1931 2° gives:

`XYZ_B,1931 = [1.504300, 1.403000, 1.814610]`

with numerical residual at machine-precision scale (`≈ 3.1 × 10⁻16` in Euclidean XYZ norm in the calculation environment).

Therefore:

`xy_B,1931 = xy_A,1931 = [0.318578710734, 0.297125527594]`

within calculation precision.

### SOURCE / DEFINITION CONNECTION

CIE metamerism describes spectrally different stimuli that have the same tristimulus values in a specified colorimetric system.

### SYNTHESIS

Spectrum A and Spectrum B are a constructed numerical metamer pair **under the CIE 1931 2° system**.

They are not spectrally equivalent. They occupy different wavelength bins and only become equivalent after projection through the specified observer model.

---

# PRACTICE D — same spectra under the CIE 1964 10° observer

Using the current-checksum-metadata-matched 1964 rows:

| λ (nm) | x̄₁₀ | ȳ₁₀ | z̄₁₀ |
| ---: | ---: | ---: | ---: |
| 450 | 0.370702 | 0.089456 | 1.994800 |
| 470 | 0.195618 | 0.185190 | 1.317560 |
| 530 | 0.236491 | 0.875211 | 0.030451 |
| 550 | 0.529826 | 0.991761 | 0.003988 |
| 610 | 1.030480 | 0.527960 | 0.000000 |
| 650 | 0.268329 | 0.107633 | 0.000000 |

The same physical spectral definitions now produce:

### Spectrum A

`XYZ_A,1964 = [1.637673, 1.492627, 2.025251]`

`xy_A,1964 = [0.317652371201, 0.289518423928]`

### Spectrum B

`XYZ_B,1964 = [1.555476323665, 1.533832735677, 1.851930797816]`

`xy_B,1964 = [0.314794741529, 0.310414547769]`

### Difference

`XYZ_B − XYZ_A = [-0.082196676335, +0.041205735677, -0.173320202184]`

Euclidean distance between the two `xy` coordinates:

`≈ 0.02109061495`

The B stimulus also has approximately `+2.7606%` higher `Y` than A under the 1964 observer.

### SYNTHESIS — observer-conditional metamerism

The pair was constructed to be indistinguishable **in CIE 1931 tristimulus coordinates**, but the equality does not survive substitution of the CIE 1964 10° standard observer.

This is direct numerical evidence for the statement:

> A colorimetric match is conditional on the observer/system used to define the match.

### Interpretation boundary

This does **not** mean that `xy` distance `0.02109` is a universal perceptual difference, nor that it predicts the experience of two particular people. CIE 1931 and CIE 1964 are standardized observer models with different field assumptions; this exercise compares those models.

---

## REPLICATION / QUALITY CONTROL

### What was independently checked in this block

- the metamer weights were solved from the 1931 3×3 CMF matrix rather than copied from a source;
- the 1931 match was re-evaluated numerically and the residual checked;
- spectrum scaling was separately re-evaluated;
- the same spectrum definitions were evaluated with the 1964 functions;
- dataset metadata/checksum discrepancies were recorded rather than silently normalized away.

### What was deliberately rejected

- treating an older 1964 mirror whose metadata checksum differed from current CIE as current authoritative evidence;
- promoting an unverified CIE 2006 LMS mirror to canonical numerical evidence;
- calling the sparse line spectra representative of an actual display or material;
- interpreting standard-observer coordinate differences as measured individual human perception.

---

## Product-readiness consequences

### When this knowledge should materially affect a project

Use it when color matching depends on spectral reproduction rather than only an agreed digital encoding, especially:

- physical brand sample ↔ display matching;
- print/material ↔ emissive display consistency;
- narrow-band LED/display primaries;
- wide-gamut/HDR display work where spectral-primary differences may matter;
- large visual fields or measurement protocols where observer choice is explicit;
- high-value brand colors where small cross-medium mismatch has commercial consequences.

### When not to over-apply it

Do **not** replace the observer/model embedded in sRGB, Display P3, ICC, CSS, accessibility, or platform standards merely because CIE 1964 or cone-fundamental models yield different coordinates.

Ordinary UI tokens still need interoperable standardized definitions. Observer-comparison research informs risk and validation; it does not authorize ad-hoc changes to a production color space.

### Project information required before advising

- emissive vs reflective object;
- governing color standard and target color space;
- actual display/material/ink/light-source technology;
- whether spectral power/reflectance data are available;
- field size and viewing distance where relevant;
- ambient illumination and adaptation conditions;
- age/user-population concerns where observer diversity is material;
- acceptable cross-medium color-difference tolerance and business risk.

### Decisions this can change

- whether HEX/XYZ matching is sufficient or spectral measurement is required;
- whether a physical brand proof must be checked under multiple illuminants;
- whether a wide-gamut/device approval requires multiple display technologies;
- whether large-field validation should supplement a small colorimeter-style swatch review;
- whether a brand-critical color needs representative-user/device observation in addition to standard colorimetry.

### Failure modes

1. **Coordinate equivalence fallacy** — equal XYZ under one observer is called universally identical color.
2. **Spectral equivalence fallacy** — same displayed appearance is assumed to mean same spectrum.
3. **Observer substitution** — a newer/different observer is inserted into a production standard without authorization.
4. **Mirror provenance failure** — a public CSV is treated as canonical without checking version/metadata.
5. **Physical-generalization failure** — ideal delta-line calculations are presented as evidence for a real display/material.
6. **Accessibility distraction** — advanced observer science is used to justify hue-only semantics instead of robust redundant communication.

---

## Validation path for production use

When spectral/observer sensitivity matters in a real project, escalate evidence in this order:

1. governing-standard identification;
2. checksum/version-controlled colorimetric datasets;
3. complete measured or defensibly modeled spectra;
4. standard-observer calculations with documented normalization;
5. alternative-observer/field-size analysis only when relevant;
6. actual display/material measurement;
7. representative viewing-condition/device checks;
8. human-observer evidence when the business risk warrants it.

A sparse mathematical metamer is a Foundation exercise, not a shipping proof.

---

## OPEN

- Obtain and independently hash checksum-verified raw current CIE files inside the execution environment where possible.
- Perform full 360–830 nm / 1 nm integration on complete smooth or measured spectra, not only sparse line bins.
- Complete a current CIE 2006 LMS / cone-fundamental comparison only after checksum-verified data access.
- Compare CIE 1931, CIE 1964, and cone-fundamental-based observers on the **same complete spectra**.
- Add measured display SPDs and reflective-material spectra in a later production study.
- Study individual-observer diversity beyond standard 2°/10° models without confusing population variation with standard-observer definitions.
- Connect observer variation to P3/HDR/narrow-primary device validation rather than treating it as a standalone laboratory curiosity.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: actual appearance is conditional on display/viewing system; T003/T004 raster evidence can later be composited under Color-defined display/background/viewing cases.
- Canonical section: Product-readiness consequences and validation path.
- Confirmation / contradiction / transfer note: extends Type’s renderer-dependence finding by adding Color/display observer dependence; no typography rule changes in this block.
- Scope limit: Color does not define glyph construction, metrics, or renderer strategy.

### Color
- Useful finding/context: Studies 010/011 now have a concrete 1931 metamer, scaling proof, and 1931→1964 observer-mismatch example.
- Canonical section: Practices A–D.
- Confirmation / contradiction / transfer note: confirms the theoretical observer-conditionality claim while adding a provenance/version-control requirement.
- Scope limit: full spectra, current LMS and physical-device evidence remain OPEN.

### Layout / Interaction
- Useful finding/context: sophisticated colorimetry does not make color-only interaction semantics robust.
- Canonical section: Product failure modes.
- Confirmation / contradiction / transfer note: confirms existing state-semantic separation; no Layout/Interaction conclusion is replaced.
- Scope limit: no state/focus usability test was performed here.

### Web Design
- Useful finding/context: observer-comparison research must not silently redefine CSS/sRGB/P3 production coordinates; Web should follow platform specifications and validate actual devices/browsers separately.
- Web application / validation consequence: wide-gamut/narrow-primary device tests may later use this study to identify observer-sensitive risk cases.
- Confirmation / contradiction / transfer note: scientific Foundation evidence only; no current browser implementation result.
- Scope limit: CSS rendering, gamut mapping and browser/device parity remain Web/Color transfer validation work.

---

## Status implication

C004 closes an important portion of the open scientific Foundation practice:

- CIE 1931 sparse spectral integration: **completed**;
- spectrum scaling / chromaticity invariance: **completed**;
- constructed metamer under CIE 1931: **completed**;
- same-spectrum CIE 1931 ↔ CIE 1964 observer comparison: **completed**;
- dataset-provenance/version discrepancy audit: **completed**;
- current checksum-verified CIE 2006 LMS numerical comparison: **OPEN**;
- full-spectrum measured/device validation: **OPEN**.

The Color domain therefore remains **CRITIQUE**, not PASS. This block improves the scientific evidence base but does not close the browser, ICC/CMM, physical-display, environmental, CVD/human-task, or multi-project transfer gates.