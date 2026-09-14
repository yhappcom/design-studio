# C005 — ICC CMM Round-Trip, D65→D50 PCS, and Precision Failure Analysis

Status: **PRACTICE + PRODUCTION-PATH VALIDATION / controlled LittleCMS profile evidence complete; float/16-bit, real display/output profiles, soft proof, cross-CMM and physical-output validation pending**

## Why this study exists

Study 012 established why D65-referenced RGB colorimetry cannot simply be relabelled as D50 and why ICC v4 uses a D50 Profile Connection Space (PCS). Until this block, that knowledge was still mostly hand-calculation and standards study.

The production question is different:

> Does a real ICC Color Management Module (CMM) expose the expected D65→D50 profile architecture, and what kinds of error appear when a profile-managed workflow is forced through a low-precision intermediate representation?

The practical goal is not to turn MintTap designers into CMM implementers. It is to make the Color Specialist competent enough to distinguish:

- profile/colorimetry errors;
- chromatic-adaptation errors;
- gamut/rendering-intent effects;
- intermediate encoding/quantization loss;
- output/device limitations.

Without that separation, a production color mismatch can easily be diagnosed at the wrong layer.

Reproducibility artifacts:

- `C005-icc-cmm-roundtrip-validation.py`
- `C005-icc-cmm-results.json`

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md`, especially T003/T004 renderer and alpha-coverage evidence.
- Reusable finding: final appearance can change at the rendering/encoding layer even when source geometry or nominal color values are unchanged.
- Replication / challenge / transfer opportunity: future export/screenshot/marketing-asset tests can combine real rasterized type with managed color pipelines.
- Dependency or overlap: **Not materially relevant to the core ICC matrix/CMM calculation.** Type becomes relevant when color-managed raster output contains real text.

### Color
- Evidence checked: Study 012 chromatic adaptation/white points; Studies 010/011/C004 observer and tristimulus foundations; Studies 016/017 gamut and authoring.
- Reusable finding: sRGB is D65-referenced; ICC v4 PCS is D50; a defined chromatic-adaptation step is required; numerical correctness does not itself prove appearance.
- Replication / challenge / transfer opportunity: this study moves the Study 012 hand matrix into an actual CMM/profile path and deliberately stress-tests precision loss.
- Dependency or overlap: direct extension and partial validation of Study 012.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md`; L002 now has a 216-condition rendered density matrix and I001 has running state/focus evidence.
- Reusable finding: layout/state semantics should not be blamed for failures caused by another rendering layer.
- Replication / challenge / transfer opportunity: later screenshots/exports of L002/I001 specimens could test whether profile/encoding changes preserve thin boundaries, state indicators, and text hierarchy.
- Dependency or overlap: **Not materially relevant to the current profile mathematics.**

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web owns actual browser/device application and production QA; Color should provide explicit profile/gamut/precision failure criteria rather than assuming authored values equal rendered output.
- Implementation/application validation opportunity: image assets, canvas export, screenshots, P3/sRGB assets, embedded profiles, browser image decoding, and OS color management should eventually reproduce or challenge C005 findings.
- Dependency or overlap: no substantive W### evidence exists yet; browser validation is not claimed here.

### Other / cross-cutting / future specialist
- Evidence checked: ICC.1:2022 / profile version 4.4; ICC explanation of D50 PCS; ICC profile-assessment guidance; W3C CSS Color 4 sRGB/D65 and D50/D65 conversion model; controlled LittleCMS execution through Pillow/ImageCms.
- Reusable finding: source/destination profile, PCS, rendering intent, precision, and CMM are separate parts of one reproduction pipeline.
- Dependency or overlap: print/physical proof, display calibration and independent instrument measurement remain future evidence.

### Overlap decision
- Reuse / deliberate repetition / extension / contradiction review / method comparison / transfer validation / project-specific study: **EXTENSION + IMPLEMENTATION VALIDATION + FAILURE ANALYSIS**.
- Why: Study 012 already states the ICC architecture; C005 verifies a real profile/CMM specimen and investigates an actual round-trip failure instead of repeating the theory.

---

# SOURCE — ICC v4 uses a fixed D50 PCS

Primary sources:

- ICC Specifications: https://www.color.org/icc_specs2/
- ICC.1:2022 v4 specification: https://www.color.org/icc-1_specification/
- ICC.1:2022 PDF: https://www.color.org/specification/ICC.1-2022-05.pdf
- ICC explanation of D50 display-profile white: https://www.color.org/whyd50/
- ICC profile assessment guidance: https://www.color.org/profiles/assessment/

At this study date, ICC identifies **ICC.1:2022, profile version 4.4.0.0** as the current v4 specification, with ISO 15076-1:2025 as the corresponding ISO publication.

ICC.1 uses a D50-based PCS. When a profile's actual adopted white differs from the PCS adopted white, the chromatic adaptation is represented by the `chromaticAdaptationTag` (`chad`) as required by the specification.

ICC explicitly describes the D50 PCS as an interoperability convention: source and destination colorimetry may be based on other whites, but must be transformed into the PCS consistently.

### SYNTHESIS

The correct production question is not “is this display D50?”

It is:

> What device/reference colorimetry does the profile describe, and how is it connected to the D50 PCS?

### STUDIO JUDGMENT

Do not manually pre-adapt normal runtime UI token values merely because ICC uses D50 internally. Let the defined color space/profile pipeline perform the required connection unless a documented asset-production workflow specifically requires explicit conversion.

---

# SOURCE — sRGB is D65-referenced

Primary source:

- W3C CSS Color Module Level 4: https://www.w3.org/TR/css-color-4/

CSS Color 4 defines sRGB and linear-light sRGB with D65 white. It also distinguishes `xyz-d65` from `xyz-d50` and specifies chromatic adaptation when color spaces use different white points.

### SYNTHESIS

The chain

`encoded sRGB → linear-light sRGB → XYZ D65`

is not yet the same numeric coordinate system as

`ICC PCS XYZ D50`.

A D65→D50 connection step remains necessary in an ICC v4 profile architecture.

---

# PRACTICE ENVIRONMENT

Controlled toolchain used for this block:

- Python `3.13.5`
- Pillow `12.3.0`
- Pillow `ImageCms`
- LittleCMS reported by ImageCms: `2.19`

Profiles created for the controlled specimen:

### sRGB profile

- description: `sRGB built-in`
- profile version: `4.4`
- device class: monitor (`mntr`)
- profile connection space: `XYZ`
- profile media white: `[0.9642, 1.0, 0.8249]` — D50

### Lab identity profile

- description: `Lab identity built-in`
- profile version: `2.1`
- device class: abstract (`abst`)
- connection space: `Lab`
- media white: `[0.9642, 1.0, 0.8249]`

These generated profiles are **controlled toolchain specimens**, not project-specific display/printer profiles.

---

# PRACTICE A — inspect the sRGB profile `chad`

The generated sRGB v4 profile exposes this chromatic-adaptation matrix:

```text
[ 1.047886003223   0.022918765175  -0.050216095312 ]
[ 0.029581782498   0.990483518491  -0.017078707704 ]
[-0.009251880839   0.015072607487   0.751678133618 ]
```

Using the standard sRGB D65 linear-RGB→XYZ matrix, sRGB white is:

```text
XYZ_D65 ≈ [0.950455927052, 1.000000000000, 1.089057750760]
```

Applying the profile `chad` gives:

```text
XYZ_D50 ≈ [0.9642, 1.0000, 0.8249]
```

within floating-point precision.

### REPLICATION

The D65-referenced sRGB primary matrix was also adapted with the profile `chad` and compared with the profile's stored red/green/blue colorants.

Stored D50 colorant matrix:

```text
[0.436041251616  0.385112910798  0.143045837586]
[0.222484540229  0.716905078608  0.060610381162]
[0.013920187471  0.097067238697  0.713912573832]
```

`chad × sRGB_D65_matrix` reproduces the stored matrix with maximum absolute residual:

`4.44 × 10⁻16`

### SYNTHESIS

This controlled profile is internally coherent with the architecture studied in Study 012:

`D65 source colorimetry → chad → D50 PCS colorants`.

### Important comparison with Study 012

Study 012 records ICC's published historical D65→D50 matrix using its stated white values. The maximum coefficient difference between that matrix and this generated profile's `chad` is approximately:

`1.13 × 10⁻4`.

Applying the Study 012 matrix to the modern high-precision sRGB D65 white gives approximately:

`[0.9642507, 0.9999990, 0.8250181]`

rather than `[0.9642, 1.0, 0.8249]` exactly.

### STUDIO JUDGMENT

Do **not** call such a small matrix difference a contradiction before checking the adopted white coordinates and rounding convention used to generate each matrix.

Matrix coefficients cannot be meaningfully compared while silently changing their source/destination white definitions.

This is a general production-debugging rule: compare assumptions before comparing numbers.

---

# PRACTICE B — CMM result vs independent hand calculation

A 17-step-per-channel RGB cube was used:

`0, 16, 32, ..., 240, 255`

Total samples:

`17³ = 4,913` colors.

For every color, two paths were compared.

## Independent path

`8-bit sRGB → inverse sRGB transfer → XYZ D65 → profile chad → XYZ D50 → CIELAB D50`

## CMM path

`8-bit sRGB → sRGB ICC profile → LittleCMS relative-colorimetric transform → 8-bit Lab identity profile`

Pillow's 8-bit `LAB` result was decoded as:

- `L* = byte × 100/255`
- `a* = byte − 128`
- `b* = byte − 128`

## Results

Maximum absolute CMM-vs-hand difference:

- `L*`: `0.19773`
- `a*`: `0.50508`
- `b*`: `0.50513`

Mean absolute difference:

- `L*`: `0.09859`
- `a*`: `0.24760`
- `b*`: `0.25079`

95th percentile absolute difference:

- `L*`: `0.18627`
- `a*`: `0.47409`
- `b*`: `0.47618`

### SYNTHESIS

The observed error envelope is consistent with the quantization resolution of the 8-bit Lab output representation:

- one L* code step ≈ `100/255 = 0.39216`, so half-step ≈ `0.19608`;
- a*/b* are integer-coded here, so half-step ≈ `0.5`.

The measured maxima sit at those expected quantization boundaries.

### STUDIO JUDGMENT

Within the precision of this 8-bit Lab observation path, the LittleCMS profile conversion agrees with the independent D65→D50→Lab calculation.

This is useful CMM evidence, but it is **not** a float-precision CMM proof. A later study should repeat the transform with a floating-point or higher-bit-depth API.

---

# PRACTICE C — representative sample colors

## Mint example `#A8F0E9`

Independent calculation:

`Lab_D50 ≈ [89.9148, -24.2991, -4.1558]`

8-bit CMM Lab decode:

`[89.8039, -24, -4]`

Absolute difference:

`[0.1109, 0.2991, 0.1558]`

## Blue example `#005FCC`

Independent calculation:

`Lab_D50 ≈ [40.9987, 10.9949, -64.1933]`

8-bit CMM Lab decode:

`[41.1765, 11, -64]`

Absolute difference:

`[0.1777, 0.0051, 0.1933]`

### STUDIO JUDGMENT

These are **conversion examples**, not evidence that either color is a recommended product color. The role of the sample is to make the production path concrete.

---

# FAILURE → DIAGNOSIS → REVISION

## Initial expectation

A naive first expectation was that an sRGB → Lab → sRGB profile-managed round-trip would reproduce most 8-bit RGB values nearly exactly.

## Observed failure

Across the same 4,913-color grid, the route

`sRGB 8-bit → Lab 8-bit → sRGB 8-bit`

produced:

- maximum single-channel RGB error: `36` code values;
- mean absolute channel error: `1.5289`;
- 95th percentile channel error: `7`;
- exact RGB pixel recovery: `8.24%`;
- all three channels within ±1: `47.26%`;
- all three channels within ±2: `60.51%`.

Some high-chroma boundary colors showed the largest reconstructed RGB differences.

## First wrong diagnosis to reject

> “The ICC CMM or Bradford adaptation is inaccurate.”

The direct CMM-vs-hand Lab comparison does **not** support that diagnosis. The CMM and hand calculation agree to the expected 8-bit Lab quantization envelope.

## Revised diagnosis

The tested round-trip includes a **low-precision 8-bit Lab intermediate representation**. Quantization in Lab, followed by nonlinear conversion back into RGB near gamut boundaries, can amplify code-value differences.

Therefore the round-trip error mixes:

- 8-bit Lab quantization;
- RGB gamma re-encoding;
- local RGB sensitivity near gamut boundaries;
- the profile transform path.

It cannot be assigned to chromatic adaptation alone.

### KEEP

- profile/CMM agreement check against independent colorimetry;
- explicit profile-tag inspection;
- separate measurement of intermediate representation precision.

### REJECT

- blaming a CMM from RGB round-trip error without isolating intermediate precision and gamut behavior;
- assuming that “profile-managed” means “lossless”;
- repeatedly converting production assets through low-bit-depth intermediate spaces without a reason.

### REWORK

- next production test should use float or higher-bit-depth transforms;
- use actual source/destination profiles, not only generated identities;
- add cross-CMM comparison before attributing a difference to one implementation.

---

# What C005 changes in professional Color practice

A color-management debugging sequence should now be:

1. identify the encoded source values;
2. identify the declared/embedded source color space or ICC profile;
3. identify source white/observer assumptions;
4. identify the destination profile/output condition;
5. identify rendering intent and black-point/gamut policy where relevant;
6. identify the CMM and platform path;
7. identify every intermediate numeric encoding and bit depth;
8. inspect whether chromatic adaptation/profile tags are internally coherent;
9. compare CMM output with an independent bounded calculation when possible;
10. only then attribute visible error to profile, CMM, quantization, gamut, display, print, or viewing environment.

This is more reliable than treating every mismatch as “the HEX changed.”

---

# Product implications for MintTap Design Studio

## Runtime app/web UI

For ordinary CSS/sRGB/P3 UI tokens, keep the native color-space definition and let the platform/browser perform its specified color conversion. Do not convert token values manually to ICC D50 PCS as a design step.

## Marketing/export assets

When screenshots, web graphics, App Store/Play Store images, PDFs, print collateral, or exported charts move between color-managed applications, preserve/inspect:

- source profile;
- destination/output profile;
- bit depth;
- export profile embedding/stripping;
- rendering intent when applicable;
- gamut clipping/mapping;
- platform preview behavior.

## Brand color

A brand-color acceptance workflow should distinguish:

- same source RGB values;
- same managed PCS colorimetry;
- same destination-device colorimetry;
- same physical/display appearance under representative viewing conditions.

C005 validates only part of the second layer.

---

# PROJECT READINESS TEST

## When should this knowledge be used?

Use it when:

- assets cross applications or devices through ICC profiles;
- D65 display color is converted into a D50 PCS/print-oriented workflow;
- screenshots/marketing assets do not match the source application;
- wide-gamut assets are exported to sRGB or print;
- a brand color changes between design, export, browser, PDF, preview, print, or display;
- a workflow repeatedly converts between RGB/Lab/CMYK or other profiled spaces.

## When should it not be used?

Do not introduce ICC PCS conversion merely to design an ordinary button, text color, or semantic token whose platform color-space path is already defined.

Do not use this evidence to claim that one CMM, display, printer, or profile is universally superior.

## Required project inputs

Before making a production recommendation, obtain:

- source file/color space/profile;
- destination device/media/profile;
- target platform/application;
- required output format;
- bit depth/internal precision where known;
- rendering intent/gamut requirements;
- whether the task is colorimetric fidelity, perceptual matching, or brand consistency;
- whether physical viewing conditions matter.

## Design decisions this can change

C005 can change:

- export format/profile strategy;
- whether to embed profiles;
- whether to keep a higher-bit-depth intermediate;
- whether a wide-gamut master plus sRGB derivative is justified;
- whether a mismatch should be corrected in the source palette or in the production pipeline;
- whether a print/display proof is required before approval.

## Alternatives and trade-offs

- **Simple sRGB-only pipeline:** maximum compatibility, smaller gamut.
- **Wide-gamut master + managed derivatives:** greater source capability, more QA burden.
- **Low-precision intermediate:** smaller/simple files, greater quantization risk.
- **High-precision/float pipeline:** stronger transform fidelity, potentially greater storage/tooling complexity.
- **Manual numeric adaptation:** transparent for bounded research, high risk if used as an undocumented production substitute for profiles/CMMs.

## Failure modes

- missing/wrong source profile;
- untagged RGB interpreted in the wrong space;
- silent profile stripping;
- repeated low-precision conversions;
- gamut clipping misdiagnosed as a profile error;
- matrix comparison with inconsistent white-point constants;
- assuming an ICC-managed preview predicts the physical viewing environment;
- changing the product palette to compensate for an export-path defect.

## Validation plan

For production-grade acceptance:

1. repeat with project source profile and destination profile;
2. use high-precision transforms;
3. compare at least one independent CMM/toolchain where risk warrants it;
4. test in-gamut and out-of-gamut patches separately;
5. inspect embedded profile metadata after export;
6. compare target application/browser/device rendering;
7. for print/physical media, perform instrumented and visual proofing under controlled conditions;
8. preserve failed conversions as evidence rather than manually correcting values without documenting the cause.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: profile-managed output can introduce precision/reproduction changes after type has already rasterized correctly.
- Canonical section: `FAILURE → DIAGNOSIS → REVISION`.
- Confirmation / contradiction / transfer note: complements T003/T004's renderer-layer evidence by adding a downstream color-management layer.
- Scope limit: C005 does not test actual text raster assets or typography readability.

### Layout / Interaction
- Useful finding/context: thin boundaries, state indicators, and small colored marks in rendered specimens can be altered downstream by export/profile/precision decisions.
- Canonical section: `Product implications` and `Failure modes`.
- Confirmation / contradiction / transfer note: supports the principle that apparent UI failure must be diagnosed at the correct layer rather than automatically blamed on geometry/state design.
- Scope limit: no L002/I001 specimen was transformed in this block.

### Web Design
- Useful finding/context: authored CSS color, embedded image color, canvas/export color, and OS/browser output can involve different color-management paths.
- Web application / validation consequence: future W### work should test profile-tagged sRGB/P3 images, screenshots/exports, browser rendering, canvas paths, and profile stripping/retention instead of assuming one browser representation.
- Confirmation / contradiction / transfer note: C005 provides Color-side failure criteria; real browser/device evidence is still required.
- Scope limit: this is LittleCMS/Pillow evidence, not browser evidence.

---

# OPEN

- repeat the CMM comparison with a float/16-bit transform API rather than an 8-bit Lab observation buffer;
- test an independently sourced ICC v4 sRGB profile and actual device/output profiles;
- test Display P3 → sRGB and RGB → print-profile workflows with explicit in-gamut/out-of-gamut separation;
- compare LittleCMS with another production CMM/toolchain where practical;
- perform soft-proof validation and measure where rendering intent changes results;
- verify embedded-profile behavior in actual PNG/JPEG/PDF export pipelines;
- test browser and OS color management through Web Design;
- test physical display and print output under controlled viewing conditions;
- run bounded Bradford/CAT02/CAT16 comparison separately rather than treating ICC's interoperable Bradford convention as a universal appearance winner.

## Status implication

Study 012's `real ICC-profile round trip` gap is **partially closed**:

- real v4 profile architecture inspected;
- actual CMM transform executed;
- `chad`→D50 behavior reproduced;
- profile colorants independently reconstructed;
- CMM Lab result checked against hand calculation over 4,913 colors;
- low-precision round-trip failure diagnosed rather than hidden.

The chromatic-adaptation/color-management module advances to **PRACTICE / CRITIQUE**.

It does **not** reach PASS because high-precision, actual device/output profile, cross-CMM, browser/device, soft-proof, and physical-output evidence remain open.
