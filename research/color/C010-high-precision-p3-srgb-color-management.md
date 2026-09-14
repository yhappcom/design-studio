# C010 — High-Precision Display-P3→sRGB Color Management: Float, Integer, Gamut, and Profile Semantics

Status: **PRACTICE + PRODUCTION-PATH VALIDATION / LittleCMS 2.19 float/16-bit/8-bit P3→sRGB proof complete; real device/output profiles, cross-CMM, browser/OS, soft proof, and physical validation pending**

## Why this study exists

C005 established a real ICC/CMM path but observed the result through an 8-bit Lab intermediate. That was sufficient to diagnose quantization as a major source of round-trip error, but it left an important production question open:

> What changes when the same color-management problem is tested with a floating-point CMM path, and how should the studio distinguish mathematical out-of-gamut representation from actual destination-gamut delivery?

C010 also addresses a second recurring production risk:

> Is an out-of-gamut floating-point RGB triplet portable across CSS, ICC/CMM, image-processing, and export pipelines merely because all of them call the destination space “sRGB”?

The answer is **no** unless the extended-range transfer/extrapolation semantics are also defined.

Reproducibility artifacts:

- `C010-high-precision-p3-srgb-color-management.py`
- `C010-high-precision-p3-srgb-results.json`

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T006 and Color C009.
- Reusable finding: source intent, intermediate representation, final rasterization, and downstream reproduction are distinct layers. C009 already showed that declared Color values do not normalize actual text rendering.
- Replication / challenge / transfer opportunity: future marketing/export specimens should combine real T006/C009 raster content with the C010 managed-color path.
- Dependency or overlap: Type is not materially relevant to the P3→sRGB matrix/CMM calculation itself. It becomes relevant when real text assets enter the managed pipeline.

### Color
- Evidence checked: C005, Studies 010/012/016/017, C004.
- Reusable finding: encoded RGB, linear-light RGB, XYZ/PCS, destination gamut, rendering precision, and physical appearance must not be collapsed into one “color value.”
- Replication / challenge / transfer opportunity: repeat C005 using `TYPE_RGB_DBL`, add Display-P3→sRGB gamut transfer, compare independent CSS-style colorimetry with ICC/CMM output, and deliberately test out-of-range floating values.
- Dependency or overlap: direct extension of C005 and Study 016.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md` through L006/I004.
- Reusable finding: failures in layer ownership, state behavior, and geometry should be diagnosed at their own layer; Color production failures should likewise not be repaired by changing unrelated layout/state semantics.
- Replication / challenge / transfer opportunity: later export L006/I003 thin boundaries/state indicators through managed asset pipelines to test whether destination-gamut or quantization decisions alter required cues.
- Dependency or overlap: not materially relevant to the core numerical transform.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web owns real CSS/browser/device integration and must eventually validate P3/sRGB rendering, image profiles, canvas/export, screenshot behavior, and system color management.
- Implementation/application validation opportunity: reproduce C010 using CSS `color(display-p3 ...)`, tagged P3/sRGB images, canvas/export, browser screenshots, and actual wide-gamut displays.
- Dependency or overlap: no substantive W### evidence exists at this checkpoint. C010 is Color-owned CMM evidence, not Web PASS.

### Other / Cross-cutting / Future Specialist
- Evidence checked:
  - ICC.1:2022 / profile version 4.4 and ICC v4 architecture;
  - W3C CSS Color Module Level 4 Display-P3 and sRGB definitions;
  - LittleCMS 2.19 engine and current formatter/unbounded-mode documentation.
- Reusable finding: high-precision and floating-point transforms can preserve extended/unbounded values, but destination delivery still requires an explicit gamut/encoding policy.
- Dependency or overlap: print proofing, calibrated displays, and instrumented validation remain production dependencies.

### Overlap decision
- **EXTENSION + IMPLEMENTATION VALIDATION + METHOD COMPARISON + FAILURE ANALYSIS**.
- Why: C005 already established the ICC architecture. C010 closes part of its precision gap and adds a materially different wide-gamut destination problem rather than repeating the same Lab8 test.

---

# SOURCE — current ICC v4 architecture and precision are not the same question

Primary source:

- ICC v4 specification index: `https://www.color.org/icc-1_specification/`
- ICC specifications overview: `https://www.color.org/icc_specs2/`
- ICC.1:2022 PDF: `https://www.color.org/specifications/ICC.1-2022-05.pdf`

ICC identifies ICC.1:2022 as profile version `4.4.0.0`. The current v4 architecture defines the profile format and connection model; profile/CMM use is conceptually separate from the numeric precision of the image buffers used by an application.

ICC v4 also retains the D50 PCS architecture studied in C005. C010 does not replace that architecture; it changes the **pixel representation and destination-gamut problem** being tested.

### SYNTHESIS

A profile-managed workflow can still fail through:

- insufficient intermediate precision;
- destination-gamut loss;
- implicit clipping;
- differing extended-range conventions;
- profile-version/profile-content differences;
- browser/OS/device behavior.

“Uses ICC” is therefore not a sufficient production acceptance criterion.

---

# SOURCE — Display-P3 and sRGB share D65 and the sRGB transfer curve, but not primaries

Primary source:

- W3C CSS Color Module Level 4: `https://www.w3.org/TR/css-color-4/`

CSS Color 4 defines:

### sRGB
- D65 white;
- red `(0.640, 0.330)`;
- green `(0.300, 0.600)`;
- blue `(0.150, 0.060)`.

### Display-P3
- D65 white;
- red `(0.680, 0.320)`;
- green `(0.265, 0.690)`;
- blue `(0.150, 0.060)`;
- same transfer curve as sRGB.

Because both use D65, a direct colorimetric P3→sRGB comparison can be made through linear-light RGB/XYZ without a change of white point. An ICC profile connection may still traverse its PCS internally.

### SYNTHESIS

The practical gamut question is not whether a P3 triplet can be numerically converted to sRGB. It always can be represented mathematically.

The question is whether the resulting **destination sRGB coordinates lie inside the deliverable `[0,1]` gamut** and, if they do not, what the production pipeline does next.

---

# SOURCE — LittleCMS supports floating-point and unbounded transforms

Primary implementation references:

- LittleCMS API documentation: `https://www.littlecms.com/LittleCMS2.18%20API.pdf`
- LittleCMS engine/tutorial: `https://www.littlecms.com/LittleCMS2.17%20tutorial.pdf`
- LittleCMS 2.19 release: `https://littlecms.com/blog/2026/04/17/lcms2-2.19/`

LittleCMS formatters include floating-point RGB, Lab, and XYZ representations such as `TYPE_RGB_FLT`, `TYPE_RGB_DBL`, and `TYPE_Lab_DBL`. Its unbounded-mode architecture permits floating values outside the ordinary encoded interval, while integer formats remain bounded by their numeric representation.

The flag `cmsFLAGS_NONEGATIVES` suppresses negative floating output. It is **not** equivalent to a complete perceptual gamut-mapping algorithm.

---

# CONTROLLED PRACTICE ENVIRONMENT

Measured toolchain:

- Python `3.13.5`;
- Pillow `12.3.0`;
- LittleCMS `2.19` loaded from Pillow's bundled shared library;
- relative-colorimetric intent;
- `cmsFLAGS_NOOPTIMIZE` for the core comparison;
- no physical display or print device in the loop.

## Source profile

A controlled Display-P3-like ICC v4.4 matrix/shaper profile was generated with:

- D65 white `(0.3127, 0.3290)`;
- P3 primaries from CSS Color 4;
- duplicated sRGB tone-response curves from the same LittleCMS engine.

This is a **controlled research profile**, not a measured Apple/device P3 profile.

## Destination profile

Primary destination:

- LittleCMS built-in sRGB profile.

Secondary cross-profile check:

- installed Artifex Software sRGB ICC Profile;
- ICC version `2.1`;
- SHA-256 `eddaf344b5edea13269e0d20055f335610e5e0b6e33e6e536f2701bc18c5f7d5`.

The Artifex profile is useful as a real distributed on-disk profile comparison. It is not a measured monitor profile and does not constitute a second CMM.

---

# PRACTICE A — independent matrix calculation versus float CMM

A uniform encoded Display-P3 grid was created with `33` values per channel:

`33³ = 35,937` samples.

Independent path:

`encoded P3 → sRGB transfer decode → linear P3 → XYZ D65 → linear sRGB → sRGB transfer encode`

CMM path:

`Display-P3 ICC → LittleCMS TYPE_RGB_DBL → sRGB ICC`

## In-gamut result

Samples whose independent CSS-style sRGB result was fully inside `[0,1]`:

`16,879`

For those samples:

- maximum absolute channel difference: `8.53 × 10⁻8`;
- mean absolute channel difference: `1.20 × 10⁻8`;
- 95th percentile absolute difference: `3.56 × 10⁻8`.

### REPLICATION RESULT

Within the tested in-gamut matrix/shaper domain, the high-precision CMM output agrees extremely closely with the independent D65 P3→sRGB calculation.

### STUDIO JUDGMENT

This is much stronger evidence than C005's 8-bit Lab observation for **this bounded transform**, but it is still not evidence that every ICC profile/CMM combination behaves identically. LUT profiles, rendering intents, black-point compensation, output profiles, and other CMMs remain separate cases.

---

# PRACTICE B — do not turn the test grid into a gamut-volume claim

Of the uniform 33³ **encoded RGB grid**, `19,058` samples produced at least one CSS-style sRGB component outside `[0,1]`:

`53.03%` of this particular grid.

### IMPORTANT LIMIT

This is **not** a perceptual volume ratio between Display-P3 and sRGB.

The sample grid is uniform in encoded RGB coordinates, not in a perceptually uniform color space, and it does not estimate physical or perceptual gamut volume.

### STUDIO JUDGMENT

Do not write statements such as:

> “53% of P3 is outside sRGB.”

C010 establishes only that destination-gamut loss is common in a deliberately broad encoded-P3 sampling exercise.

---

# PRACTICE C — floating out-of-gamut values can remain reversible without being displayable

The unbounded float transform produced:

- `18,418` channel components below `0`;
- `5,161` channel components above `1`.

The same float output was then transformed back through the sRGB profile into the generated P3 profile.

Across all `35,937` samples, including the out-of-sRGB-gamut set:

- maximum absolute P3 round-trip error: `4.05 × 10⁻7`;
- mean absolute error: `1.33 × 10⁻8`.

### SYNTHESIS

An unbounded floating representation can preserve information that a bounded destination encoding cannot physically deliver.

### REJECT

Reject:

> “The conversion is lossless, therefore the sRGB destination can reproduce the original P3 color.”

The round trip is numerically reversible because the extended values are retained. A normal bounded sRGB image/display path cannot emit negative or >1 channel values as ordinary in-gamut sRGB.

---

# PRACTICE D — CSS extended sRGB numbers and ICC/CMM unbounded numbers are not automatically interchangeable

Representative P3 green:

`display-p3 [0, 1, 0]`

Independent CSS-style extended sRGB calculation:

`[-0.511605, 1.018266, -0.310675]`

LittleCMS unbounded sRGB result:

`[-2.906227, 1.018266, -1.015978]`

Both are out of sRGB gamut, but the negative encoded numbers are materially different.

Yet the LittleCMS unbounded result transforms back to approximately:

`[-0.000000405, 0.999999940, -0.000000026]` in the controlled P3 profile.

### DIAGNOSIS

The disagreement outside the ordinary gamut is not evidence that the in-gamut P3→sRGB matrix is wrong. The in-gamut comparison already agrees to around `10⁻8`.

The issue is that **extended-range encoded RGB requires a specified curve/extrapolation convention**. CSS extended color conversion and an ICC CMM's unbounded parametric-curve behavior must not be assumed numerically identical outside the normal domain.

### STUDIO JUDGMENT

Whenever an engineering/design pipeline passes negative or >1 RGB values between systems, record:

- color space;
- transfer function;
- whether values are encoded or linear;
- permitted numeric range;
- extrapolation convention;
- clipping/gamut-mapping stage.

A label such as “extended sRGB float” is incomplete unless these semantics are known.

---

# PRACTICE E — `cmsFLAGS_NONEGATIVES` is not gamut mapping

Enabling LittleCMS `cmsFLAGS_NONEGATIVES` changed at least one component for approximately:

`45.41%` of the sampled P3 grid.

Example P3 green:

unbounded:

`[-2.906227, 1.018266, -1.015978]`

with `NONEGATIVES`:

`[0.000000, 1.018266, 0.000000]`

The value above `1` remains above `1`.

### REJECT

Do not describe `NONEGATIVES` as a complete “convert P3 safely to sRGB” policy.

It suppresses negative floating outputs. It does not choose a perceptually appropriate in-gamut substitute, preserve brand intent, or guarantee `[0,1]` delivery.

---

# PRACTICE F — bounded integer output makes precision and gamut policy visible

The same grid was converted using 16-bit and 8-bit integer RGB output and compared with the **clipped floating CMM result at the corresponding quantized input**.

## 16-bit

- maximum absolute normalized channel difference: `7.63 × 10⁻6`;
- mean absolute difference: `2.93 × 10⁻6`.

## 8-bit

- maximum absolute normalized channel difference: `0.0019608`;
- mean absolute difference: `0.0007508`.

The 8-bit maximum is essentially a half-code-step scale (`0.5 / 255 ≈ 0.0019608`).

### SYNTHESIS

High-precision CMM accuracy and low-bit-depth delivery are different gates.

A pipeline can be colorimetrically coherent at float precision and still lose information through the final bounded encoding.

---

# PRACTICE G — gradient probe

A `4,097`-sample P3 gradient that remained inside sRGB after float conversion was transformed through float, 16-bit, and 8-bit paths.

Unique RGB triplets retained:

- 16-bit path: `4,097 / 4,097`;
- 8-bit path: `485 / 4,097`.

The input itself also collapsed to `485` unique triplets when quantized to 8-bit, so this result is primarily an **encoding-resolution demonstration**, not an accusation against the CMM.

### STUDIO JUDGMENT

For smooth gradients, repeated compositing, adjustment layers, wide-gamut masters, or other numerically sensitive production work, keep higher precision as long as the toolchain supports it. Reduce to 8-bit only at a justified delivery boundary.

This does not imply that every ordinary UI asset requires 16-bit storage.

---

# PRACTICE H — one real on-disk sRGB profile is not numerically identical to another

The generated P3 profile was also converted into the installed Artifex Software sRGB ICC v2.1 profile and compared with LittleCMS's built-in sRGB destination for the `16,879` CSS-defined in-gamut samples.

Differences:

- maximum absolute channel difference: `0.0018998`;
- mean absolute difference: `0.0000649`;
- 95th percentile: `0.0001317`.

The largest tested difference occurred near a low red destination component for one greenish sample.

### SYNTHESIS

Even two profiles both described as “sRGB” can contain different profile versions, tag conventions, white-point handling, tone-curve representations, or quantization details.

### IMPORTANT LIMIT

This is a **cross-profile** comparison using the same CMM. It is not:

- a cross-CMM test;
- proof that one profile is more correct;
- a physical display comparison.

### STUDIO JUDGMENT

In production debugging, “both files are sRGB” is not enough. Record the actual embedded profile identity/hash when exact reproduction matters.

---

# FAILURE → DIAGNOSIS → REVISION

## Failure policy 1

> “P3→sRGB conversion succeeded because the CMM returned numbers.”

### Diagnosis

Numbers outside `[0,1]` can remain in a float buffer even though the destination's ordinary deliverable gamut cannot reproduce them.

### Revision

Separate:

1. colorimetric conversion;
2. gamut classification;
3. gamut mapping/clipping policy;
4. delivery encoding;
5. target device validation.

## Failure policy 2

> “The CSS extended-sRGB and ICC float values disagree, so one implementation is wrong.”

### Diagnosis

The disagreement is concentrated in out-of-gamut extended values. In-gamut output agrees to roughly `10⁻8`.

### Revision

Compare representation semantics before comparing out-of-range numbers.

## Failure policy 3

> “Use 8-bit because the final screen is 8-bit anyway.”

### Diagnosis

Repeated edits/transforms can accumulate quantization before the final delivery stage, and higher-precision pipelines retain substantially more intermediate states.

### Revision

Use the precision required by the production chain, then quantize deliberately at the output boundary.

---

# Project-facing decision method

When a project asks whether to use Display-P3, sRGB, or a wide-gamut master, first identify:

1. whether the **source design intent actually uses colors outside sRGB**;
2. target app/web/browser/device coverage;
3. fallback requirements;
4. whether assets will be edited repeatedly or merely delivered once;
5. required export formats and profile embedding;
6. whether brand fidelity is more important than maximum saturation;
7. whether out-of-gamut colors may be clipped, chroma-reduced, perceptually mapped, or separately authored;
8. whether gradients/photographic assets justify higher precision;
9. whether print or other profiled outputs are part of the same pipeline;
10. what real devices/viewing conditions must be approved.

### Project recommendation pattern

- If all required colors are comfortably inside sRGB and compatibility dominates: **sRGB-only may be the better system.**
- If P3 provides a meaningful visual/brand/data benefit on target devices: maintain a **wide-gamut master plus explicit sRGB fallback/derivative policy**.
- If a color only looks “better” because it clips differently across systems: **do not approve it as a brand or semantic color until the fallback behavior is intentional**.
- If exact reproduction is critical: preserve profile identity, bit depth, rendering intent, and output QA rather than relying on color-space names alone.

---

# PROJECT READINESS TEST

## When should this knowledge be used?

Use it for:

- Display-P3 app/web colors;
- wide-gamut brand colors;
- App Store/Play Store/marketing exports;
- P3 screenshots or image assets that must reach sRGB clients;
- smooth gradients or repeated image/color transforms;
- debugging mismatches between design tools, export tools, browsers, and image pipelines.

## When should it not be used?

Do not introduce P3 or ICC complexity into a product whose required palette is already inside sRGB and gains no meaningful project benefit.

Do not interpret float out-of-range RGB numbers as physically displayable colors.

Do not use the uniform-grid 53% result as a gamut-volume statistic.

## Inputs required before recommending a production policy

- authored source space and profile;
- actual palette coordinates;
- destination platforms/devices;
- browser/app support requirements;
- export formats;
- precision/bit-depth chain;
- profile embedding rules;
- gamut/fallback strategy;
- brand/data/semantic importance;
- physical viewing requirements.

## Failure conditions

A recommendation fails when:

- out-of-gamut source colors are clipped accidentally;
- P3 and sRGB variants change semantic meaning;
- negative/>1 float values cross systems with undefined transfer semantics;
- profile metadata is stripped or misinterpreted;
- repeated low-bit-depth conversions introduce avoidable banding/quantization;
- a “same sRGB” assumption hides different actual profiles;
- browser/device output is accepted without target validation;
- production errors are incorrectly repaired by changing the source palette.

## Validation plan

For production-grade approval:

1. test real source and destination profiles;
2. compare float/high-bit-depth and final delivery paths;
3. classify in-gamut/out-of-gamut colors explicitly;
4. compare clipping and candidate gamut-mapping strategies on important colors;
5. verify embedded profile metadata after export;
6. test actual browsers/apps/OS color-management paths;
7. inspect wide-gamut and non-wide-gamut target devices;
8. test gradients and screenshots separately from flat UI tokens;
9. use a second CMM/toolchain where reproduction risk warrants it;
10. perform physical/instrumented proofing for critical brand/print outputs.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: high-precision color conversion can preserve numerical data while final bounded output still clips/quantizes; text raster evidence should therefore be tested after the actual output pipeline, not only before it.
- Canonical section: `PRACTICE F/G` and `Project-facing decision method`.
- Confirmation / contradiction / transfer note: extends C009/T006's layer-separation logic downstream into color management.
- Scope limit: no Type raster asset was transformed in C010.

### Layout / Interaction
- Useful finding/context: thin state boundaries and semantic markers can be affected by output encoding or gamut handling after interaction/layout logic is already correct.
- Canonical section: `FAILURE → DIAGNOSIS → REVISION`.
- Confirmation / contradiction / transfer note: confirms the broader diagnostic principle that visible failure must be assigned to the correct layer.
- Scope limit: C010 does not test L006/I003 specimens directly.

### Web Design
- Useful finding/context: CSS Display-P3, tagged images, canvas/export, screenshot capture, browser profile handling, and actual display output can represent different stages of one color path.
- Web application / validation consequence: test in-gamut and out-of-gamut P3 colors separately; inspect real CSS P3→sRGB fallback, tagged image rendering, canvas export, screenshot/profile behavior, wide-gamut vs standard-gamut devices, and forced/system modes.
- Confirmation / contradiction / transfer note: C010 gives a high-precision Color-side baseline against which browser behavior can later be compared.
- Scope limit: no substantive W### evidence exists yet; this is not browser/device PASS.

---

# OPEN

- real measured Display-P3 monitor/profile instead of the controlled generated matrix profile;
- real printer/output profile and RGB→print soft proof;
- cross-CMM comparison against a second independent engine;
- browser/OS CSS P3 and tagged-image transfer;
- canvas/screenshot/export profile retention;
- explicit perceptual gamut-mapping comparison for important brand/data colors;
- physical wide-gamut/non-wide-gamut display proof under controlled ambient light;
- HDR/PQ/HLG as a separate luminance/transfer problem rather than conflating it with P3 gamut;
- higher-precision image-file pipeline tests such as 16-bit PNG/TIFF/OpenEXR where project requirements justify them.

## Status implication

C010 materially advances the C005 precision gap:

- real `TYPE_RGB_DBL` CMM path executed;
- high-precision in-gamut P3→sRGB result independently reproduced;
- out-of-gamut unbounded behavior isolated from destination delivery;
- float round-trip versus integer bounded delivery separated;
- 16-bit/8-bit quantization measured;
- one independent on-disk sRGB profile compared;
- extended-range representation mismatch identified as a production contract issue.

The **Chromatic adaptation / ICC color management** module remains `PRACTICE / CRITIQUE`, but with the previous float/high-bit-depth gap partially closed.

The **Gamut / wide-gamut mapping** module advances in production-path evidence but does not reach PASS because actual gamut-mapping policy, browser/device transfer, and physical output remain open.