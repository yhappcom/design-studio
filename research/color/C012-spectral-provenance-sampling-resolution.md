# C012 — Spectral Dataset Provenance and Sampling Resolution: Current CIE 1931 Verification, Smooth-SPD Integration, and Narrowband Failure Boundaries

Status: **PRACTICE + PROVENANCE VALIDATION / current CIE 1931 checksum reconstruction + full 360–830 nm smooth-spectrum integration complete; current CIE 1964 byte verification and CIE 2006 LMS identity remain incomplete; measured SPD/device validation pending**

## Why this study exists

C004 proved observer-conditional metamerism with sparse spectral lines, but deliberately left three scientific gaps open:

1. no full 360–830 nm integration over a complete smooth spectrum;
2. no independently strengthened current-dataset provenance beyond mirror metadata;
3. no current CIE 2006 LMS numerical result because the accessible file identity could not be reconciled with the checksum published by CIE.

C012 addresses those gaps without lowering the evidence standard.

The practical question is not merely:

> Can the studio integrate a spectrum?

It is:

> Can the studio identify exactly which observer table it is using, prove enough provenance to trust the numerical exercise, understand when spectral sampling resolution matters, and refuse to turn an unresolved dataset identity into a production claim?

Reproducibility artifacts:

- `C012-spectral-provenance-sampling-resolution.py`
- `C012-spectral-provenance-sampling-results.json`

The CIE data files themselves are **not copied into Design Studio**. The script requires a locally obtained dataset and verifies its checksum before calculation.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T014 and Color C009.
- Reusable finding: source/package/render provenance must be explicit before downstream visual conclusions are trusted; T013/T014 show that semantically similar content can still reach different shipped artifacts.
- Replication / challenge / transfer opportunity: the same provenance discipline applies to Color datasets and eventually to measured display SPDs used behind actual Type specimens.
- Dependency or overlap: Type is not required for the spectral integration itself. It becomes relevant only when spectral/device results are transferred to rendered text roles.

### Color
- Evidence checked: Studies 010/011, C004, C005, C010 and current Color status.
- Reusable finding: the observer and spectral dataset are part of the colorimetric definition; spectral equivalence, tristimulus equivalence and physical appearance are separate claims.
- Replication / challenge / transfer opportunity: replace C004's sparse-line-only practice with complete smooth synthetic SPDs and explicitly test spectral sampling resolution.
- Dependency or overlap: direct extension of C004 and the largest remaining scientific Foundation gap.

### Layout / Interaction
- Evidence checked: current `progress/LAYOUT_STATUS.md`, especially I003 and L006.
- Reusable finding: failures must be diagnosed at the correct layer; an interaction/state failure should not be repaired by changing colorimetry, and a spectral-measurement problem should not be repaired by changing semantic state definitions.
- Replication / challenge / transfer opportunity: not materially relevant to the present integration calculation.
- Dependency or overlap: none for the core numerical work.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md` and `research/web/README.md`.
- Reusable finding: Web must eventually validate real browser/device behavior, but CSS/sRGB/P3 coordinates should not be silently replaced by a research observer model.
- Implementation/application validation opportunity: future wide-gamut display work can use C012 to decide when device spectral measurements or narrow-primary checks are worth requesting.
- Dependency or overlap: no substantive W### evidence exists at this checkpoint. C012 is scientific Color evidence, not browser/device proof.

### Other / Cross-cutting / Future Specialist
- Evidence checked: current CIE dataset metadata/DOIs, ISO/CIE 11664-1 relationship, pinned public mirrors, exact mirror blob identities, and a public independent report of the same CIE 2006 LMS checksum mismatch encountered here.
- Reusable finding: filename and table resemblance are weaker provenance than DOI + current published checksum + immutable retrieved artifact identity.
- Dependency or overlap: physical spectroradiometry, instrument bandwidth, wavelength accuracy, calibration and human-observer work remain future evidence.

### Overlap decision
- **REPLICATION + EXTENSION + PROVENANCE VALIDATION + FAILURE ANALYSIS**.
- Why: C004 already established the theory and sparse calculations. C012 tests complete spectra, improves provenance, and adds a materially new spectral-sampling failure mode.

---

# SOURCE — current CIE dataset identities

Authoritative dataset records used as the reference identities for this study:

### CIE 1931 2° standard colorimetric observer

- dataset: `CIE_xyz_1931_2deg.csv`
- DOI: `10.25039/CIE.DS.xvudnb9b`
- wavelength range: `360–830 nm`
- increment: `1 nm`
- current published MD5: `17cca777db64b17170f06f67ce9d3ab7`
- related standard: ISO/CIE 11664-1:2019

Authoritative page:

`https://cie.co.at/datatable/cie-1931-colour-matching-functions-2-degree-observer`

### CIE 1964 10° standard colorimetric observer

- dataset: `CIE_xyz_1964_10deg.csv`
- DOI: `10.25039/CIE.DS.sqksu2n5`
- wavelength range: `360–830 nm`
- increment: `1 nm`
- current published MD5: `cd6135a724480eb8c5e7668bae914445`
- related standard: ISO/CIE 11664-1:2019

Authoritative page:

`https://cie.co.at/datatable/cie-1964-colour-matching-functions-10-degree-observer`

### CIE 2006 2° LMS cone fundamentals

- dataset: `CIE_lms_cf_2deg.csv`
- DOI: `10.25039/CIE.DS.tijidesg`
- source: CIE 170-1:2006, Table 6.7
- current published MD5 observed for this research: `27c74cc0f98edecadc02fc71f540b116`

Authoritative page:

`https://cie.co.at/datatable/cie-2006-lms-cone-fundamentals-2-field-size-terms-energy`

### SYNTHESIS

A dataset name is not enough. The minimum reproducibility record for scientific Color calculations should include:

`observer/model → DOI/standard → wavelength grid → current checksum → retrieved artifact identity → calculation code`.

---

# PROVENANCE PRACTICE A — current CIE 1931 identity materially strengthened

A pinned copy was inspected at:

- repository: `wetadigital/physlight`
- commit: `9d076d1074aad7257c04c39581a4d21f97fd2527`
- Git blob SHA: `9b4e3f73b4bb412a762a6d03cb8060bfea652a6e`

The retrieved table contains exactly:

- `471` wavelength rows;
- `360` through `830 nm`;
- continuous `1 nm` spacing.

The numerical column sums reproduce the dataset validation metadata:

- wavelength sum: `280245`;
- x̄ sum: `106.865469489595`;
- ȳ sum: `106.8569171011719`;
- z̄ sum: `106.892251278636`.

The connector-returned text normalized to LF has MD5:

`5a60da02f27032ef3c050dfd1e913f0f`

Reconstructing the CRLF serialization shown by the pinned blob gives:

`17cca777db64b17170f06f67ce9d3ab7`

which equals the current CIE-published MD5 exactly.

### REPLICATION RESULT

C012 therefore upgrades C004's 1931 provenance from **metadata-matched mirror evidence** to an independently recomputed serialization/checksum match tied to an immutable Git blob.

### Evidence boundary

The execution environment did not retrieve the CIE host file directly as raw bytes. The result is a checksum reconstruction from a pinned public copy whose row text, grid, validation sums and CRLF serialization reproduce the CIE-published identity.

This is substantially stronger than filename/metadata matching, but the canonical authority remains CIE.

---

# PROVENANCE PRACTICE B — CIE 1964 current and legacy copies must not be mixed

C004 had already encountered a 1964 mirror with stale metadata. C012 reproduced that distinction.

## Older pinned mirror

`wetadigital/physlight` at the pinned commit reports MD5:

`6140e032f9326d88c5a0959b29b4d8f3`

This does **not** equal the current CIE-published MD5:

`cd6135a724480eb8c5e7668bae914445`.

It is retained only as evidence that public copies can outlive a dataset revision/serialization change.

## Current-metadata-matched mirror found

A second pinned source was found:

- repository: `chran554/pathtracer`
- commit: `ec602c93c253c7d88646e5a7551ac554c75f46d0`
- Git blob SHA: `d3040193ae654fe5fc33ea0e1f1a7b24c45fca9c`

Its metadata reports:

- DOI `10.25039/CIE.DS.sqksu2n5`;
- MD5 `cd6135a724480eb8c5e7668bae914445`;
- SHA-256 `c800ae88d20868427e09482d7b5c026e7f5001dc00bec18cd9dcd3a0006da396`.

### OPEN / evidence boundary

In this execution, the current 1964 mirror's MD5 was **not independently recomputed from a local raw byte file**. Therefore C012 does not upgrade 1964 to the same provenance tier as 1931 and does not use it for a new canonical current-observer numerical comparison.

C004's observer-comparison conclusion remains valid within its documented evidence; C012 does not pretend the remaining byte-verification gate is closed.

---

# PROVENANCE PRACTICE C — CIE 2006 LMS remains blocked, and that is a valid research result

A pinned accessible LMS copy was inspected at:

- repository: `wetadigital/physlight`
- commit: `9d076d1074aad7257c04c39581a4d21f97fd2527`
- Git blob SHA: `5e9069337cf5aef005e8dab64870bfff38911359`.

Reconstructing its CRLF serialization produced MD5:

`dba2e9d1f5e6667575aa069832159510`.

The current CIE dataset record publishes:

`27c74cc0f98edecadc02fc71f540b116`.

A separate public research run was also found reporting the same pair — expected `27c74...`, obtained `dba2...` — when attempting to use the CIE 2006 LMS data.

### REJECT

Do not respond to this mismatch by:

- ignoring the checksum;
- assuming the accessible copy is wrong merely because the checksum differs;
- assuming the published checksum is stale merely because multiple copies agree;
- calculating LMS values and labeling them "current official CIE" anyway.

### STUDIO JUDGMENT

Until the authoritative identity is resolved, **current CIE 2006 LMS numerical comparison remains OPEN**.

A correctly preserved blocker is better evidence than a fabricated completion.

---

# PRACTICE D — full 360–830 nm integration with complete synthetic SPDs

With current CIE 1931 provenance strengthened, the study moves beyond C004's sparse line bins.

All four test spectra are synthetic **emissive relative SPDs** defined at every 1 nm wavelength from 360 to 830 nm.

They are not measured devices.

## Spectrum definitions

### Broad warm

`G(610, σ45) + 0.25 G(470, σ30)`

### Broad cool

`G(460, σ28) + 0.55 G(540, σ55)`

### Narrow display-like diagnostic

`G(452.3, σ8) + 0.85 G(531.7, σ10) + 0.75 G(608.4, σ8)`

### Ultra-narrow laser-like diagnostic

`G(452.3, σ2.5) + 0.85 G(531.7, σ3) + 0.75 G(608.4, σ2.5)`

where `G(μ,σ)` is a Gaussian on the wavelength grid.

The last two labels describe **test-shape bandwidth**, not claims about a particular commercial display or projector.

---

# RESULT — CIE 1931 1 nm full-spectrum integration

Using

`XYZ = Σ SPD(λ) · [x̄(λ), ȳ(λ), z̄(λ)] · Δλ`

with `Δλ = 1 nm`:

| Synthetic SPD | X | Y | Z | x | y |
| --- | ---: | ---: | ---: | ---: | ---: |
| Broad warm | 72.913233 | 59.167863 | 19.900423 | 0.479750653 | 0.389309590 |
| Broad cool | 45.121995 | 52.767404 | 99.078229 | 0.229083304 | 0.267898865 |
| Narrow display-like | 25.451435 | 26.964134 | 35.295012 | 0.290175194 | 0.307421681 |
| Ultra-narrow laser-like | 8.022514 | 8.345033 | 11.270379 | 0.290271934 | 0.301941369 |

The absolute XYZ magnitudes depend on the arbitrary relative SPD amplitudes. The chromaticities are useful only inside this controlled numerical exercise.

---

# PRACTICE E — 5 nm sampling-grid sensitivity

To test whether "5 nm is close enough" can be treated as a universal rule, C012 deliberately subsamples the same 1 nm SPD/CMF grid every 5 nm.

Five phase offsets are tested:

`0, 1, 2, 3, 4 nm`.

Each sampled sum is multiplied by 5.

This is a **sampling-grid diagnostic only**. It does not model:

- spectroradiometer optical bandwidth;
- slit function;
- wavelength calibration error;
- stray light;
- noise;
- interpolation/reconstruction method.

## Maximum error across the five phase offsets

| Synthetic SPD | max `Δxy` | max absolute relative Y error |
| --- | ---: | ---: |
| Broad warm | `1.60 × 10⁻7` | `7.91 × 10⁻7` |
| Broad cool | `1.17 × 10⁻7` | `1.20 × 10⁻6` |
| Narrow display-like | `3.82 × 10⁻6` | `1.89 × 10⁻6` |
| Ultra-narrow laser-like | `0.001920` | `0.004559` (`0.456%`) |

### SYNTHESIS

For the two broad synthetic SPDs, simple 5 nm phase changes were numerically negligible in this exercise.

The σ8–10 nm narrow diagnostic also remained stable under this particular 5 nm test.

The ultra-narrow diagnostic did not. Its chromaticity estimate changed materially with the phase of the 5 nm grid, and its Y estimate varied by up to roughly 0.46% relative to the 1 nm reference.

### REJECT

Reject both universal claims:

> "5 nm spectral data is always sufficient."

and

> "5 nm spectral data is inherently unusable for colorimetry."

The relevant variables include spectral bandwidth, peak location, measurement/integration method, instrument response and required tolerance.

### Important metric boundary

`Δxy` here is a coordinate-space diagnostic, **not a perceptual color-difference metric**. It must not be translated into a JND or ΔE claim.

---

# What C012 changes in professional Color practice

C012 adds a production-facing spectral intake checklist.

When spectral data is supplied for a display, LED, projector, material, illuminant or brand-match problem, Color should identify:

1. what was measured — emission SPD, spectral reflectance, transmittance, illuminant, or derived data;
2. wavelength range and sample interval;
3. instrument optical bandwidth / spectral bandwidth if available;
4. wavelength accuracy/calibration;
5. governing observer and standard;
6. raw data provenance/version/checksum;
7. whether the source is narrowband enough that sampling resolution may become material;
8. whether the business decision actually requires spectral evidence rather than standard encoded RGB/XYZ.

### STUDIO JUDGMENT

Do not request spectral measurements for routine UI tokens merely to appear more rigorous.

Do request stronger spectral evidence when the problem genuinely involves:

- physical ↔ emissive brand matching;
- narrow-primary displays/projectors;
- LED/laser source comparison;
- metamerism across materials/illuminants;
- instrument disagreement;
- cross-technology high-value color approval.

---

# FAILURE → REVISION MODEL

## Failure 1 — filename authority

**Failure:** `CIE_xyz_1964_10deg.csv` is assumed current because the filename is correct.

**Revision:** record DOI + current authoritative checksum + pinned artifact identity; reject known stale metadata.

## Failure 2 — checksum inconvenience

**Failure:** LMS checksum mismatch is treated as a nuisance and ignored so the curriculum can move on.

**Revision:** preserve the mismatch and keep the numerical conclusion OPEN.

## Failure 3 — smooth-spectrum generalization

**Failure:** the broad-spectrum 5 nm result is generalized to narrowband emitters.

**Revision:** explicitly stress-test spectral bandwidth and sampling phase.

## Failure 4 — narrowband panic

**Failure:** one ultra-narrow failure is turned into a universal requirement for 1 nm data.

**Revision:** define resolution from actual spectrum, instrument characteristics and acceptance tolerance.

---

# PROJECT READINESS TEST

## When should this knowledge be used?

Use C012 when a project supplies or depends on spectral data, especially for display/LED/projector technology, physical brand samples, print/material matching, metamerism or cross-medium color approval.

## When should it not be used?

Do not require spectral integration to choose an ordinary semantic UI color already defined in sRGB/P3 and governed by platform/browser standards.

Do not replace a production standard observer with CIE 1964 or cone fundamentals simply because those models are scientifically relevant.

## Required project inputs

- target medium/device technology;
- whether stimulus is emissive or reflective;
- actual spectral data and metadata;
- wavelength range/resolution/instrument details;
- governing color standard/observer;
- target color space/output;
- viewing geometry and environment where relevant;
- business tolerance and failure cost.

## Concrete decisions this can change

- accept/reject a supplied SPD dataset for color approval;
- request higher spectral resolution or instrument metadata;
- decide whether standard XYZ/encoded RGB is sufficient;
- require multiple illuminant/device proofs for a brand-critical physical color;
- identify whether a mismatch is likely spectral, color-management, gamut, display, or design-system related.

## Trade-offs

- higher spectral resolution can improve narrowband characterization but increases data/instrument burden;
- broad-spectrum workflows may not benefit from unnecessarily fine sampling;
- spectral measurement adds physical evidence but does not replace human/viewing-condition validation;
- standard observer consistency improves interoperability but does not model every individual observer.

## Failure conditions

C012 should be considered insufficient when:

- the source spectrum is measured but instrument bandwidth/calibration is unknown and the tolerance is tight;
- device SPDs are narrow and the sample interval is comparable to the spectral features;
- current observer/cone datasets cannot be authenticated;
- a physical appearance claim is being made without physical measurement/viewing evidence;
- an individual-observer conclusion is inferred from standard-observer tables.

## Validation plan for a real project

1. acquire the exact raw measured spectrum and instrument metadata;
2. preserve file hash/version;
3. integrate with the governing standard observer at appropriate resolution;
4. quantify sensitivity to interpolation/sample interval where spectral features are narrow;
5. compare with an independent measurement/toolchain when risk is high;
6. validate actual display/material under specified viewing conditions;
7. add human-observer evidence only when the business question requires it.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: physical display/spectral evidence can alter actual rendered appearance after Type geometry/raster decisions are already fixed.
- Canonical section: `What C012 changes in professional Color practice`.
- Confirmation / contradiction / transfer note: complements Type's source/build/render provenance discipline with spectral/device provenance.
- Scope limit: no text legibility or glyph-rendering conclusion is made here.

### Layout / Interaction
- Useful finding/context: advanced spectral accuracy must not substitute for redundant state semantics or correct interaction ownership.
- Canonical section: `When should it not be used?` and failure conditions.
- Confirmation / contradiction / transfer note: reinforces layer-specific diagnosis; does not redefine Layout/Interaction semantics.
- Scope limit: no user task or interaction behavior was tested.

### Web Design
- Useful finding/context: routine CSS/P3 UI should continue to follow platform standards, while high-value wide-gamut/narrow-primary device approval may justify spectral/device evidence.
- Web application / validation consequence: if a web project promises wide-gamut brand fidelity, Web should supply actual target browser/device conditions; Color can determine whether device/SPD validation is warranted.
- Confirmation / contradiction / transfer note: scientific risk-screening input only, not browser/device PASS.
- Scope limit: no W### production browser/device evidence exists yet.

---

# OPEN

- independently recompute the raw current CIE 1964 MD5 in an execution path that preserves exact file bytes;
- resolve the CIE 2006 LMS published-checksum versus accessible-copy mismatch before claiming current LMS numerical results;
- then compare **the same complete smooth spectra** under current verified 1931, 1964 and cone-fundamental-based models;
- obtain measured display SPDs, including at least one narrow-primary technology;
- add actual spectroradiometer bandwidth/sample-interval comparison instead of the current mathematical subsampling diagnostic;
- test reflective spectra under explicit illuminants;
- connect spectral/device differences to physical-display and representative-human validation where product risk justifies it.

## Status implication

C012 materially advances the spectral/observer Foundation module:

- current CIE 1931 provenance: **upgraded to independently recomputed checksum reconstruction**;
- full 360–830 nm smooth-spectrum 1 nm integration: **completed**;
- sampling-resolution stress test: **completed**;
- stale/current CIE 1964 mirror separation: **improved, but current raw-byte MD5 recomputation still OPEN**;
- current CIE 2006 LMS comparison: **correctly BLOCKED / OPEN because identity mismatch remains unresolved**;
- measured physical SPD/device/human validation: **OPEN**.

Color remains **CRITIQUE / Foundation NOT PASSED**. The scientific method is stronger, but the remaining physical-device, human-observer, current-LMS, browser/OS, and real-project gates are substantial.
