# Study 017 — Perceptual Ramp Authoring for Product Color Systems

Status: FOUNDATION / INTERMEDIATE BRIDGE STUDY — numerical practice complete in companion exercise; rendered/browser/device validation still required before PASS.

## Question

When a product needs a multi-step color scale, which coordinate system should control the steps, and what evidence is required before calling that scale perceptually regular or production-safe?

This study follows:

- `research/color/013-perceptual-color-spaces-difference.md`
- `research/color/016-color-gamut-wide-gamut-mapping.md`

## SOURCE — HSL is convenient geometry, not perceptual geometry

Primary platform reference:

- W3C CSS Color Module Level 4: https://www.w3.org/TR/css-color-4/

CSS Color 4 explicitly discusses perceptual shortcomings of HSL. HSL is a cylindrical re-expression around encoded sRGB and is useful as a familiar authoring control, but equal changes in HSL lightness or hue do not imply equal perceived changes.

A canonical example is that saturated blue and saturated yellow can share the same HSL lightness while appearing very different in visual lightness.

### SYNTHESIS

A numerical scale can be internally regular yet perceptually irregular if the coordinate axes are not designed to approximate perceptual dimensions.

### STUDIO JUDGMENT

MintTap Design Studio may use HSL for convenience, inspection, or legacy interoperability, but HSL is not approved as the primary generator for systematic semantic ramps, neutral ramps, chart ramps, or brand tonal scales when perceptual regularity is the design objective.

## SOURCE — CIELAB/CIELCh provides a standardized perceptual working model

Primary reference:

- ISO/CIE 11664-4:2019, CIE 1976 L*a*b* colour space: https://www.cie.co.at/publications/colorimetry-part-4-cie-1976-lab-colour-space-1

CIELAB was standardized as a more-nearly uniform object-colour space than XYZ. CIELCh is a cylindrical re-expression of CIELAB using lightness, chroma, and hue angle.

### SYNTHESIS

Holding CIELCh chroma and hue approximately constant while stepping L* is much more defensible than assuming HSL lightness steps are perceptually equal. It is still not proof of universal visual uniformity, and it remains reference-white and viewing-condition dependent.

### STUDIO JUDGMENT

CIELCh remains important where CIE/ICC workflows, physical samples, print, measurement, or governed colour-difference practice are involved. It should not be displaced merely because a newer digital authoring space is easier to use.

## SOURCE — Oklab/OkLCh is designed for modern digital color operations

Primary-author and platform references:

- Björn Ottosson, Oklab: https://bottosson.github.io/posts/oklab/
- W3C CSS Color Module Level 4: https://www.w3.org/TR/css-color-4/

Oklab was designed for perceptual image-processing operations and is now defined by CSS Color 4. OkLCh exposes lightness, chroma, and hue coordinates that are operationally useful for digital palette construction and interpolation.

### SYNTHESIS

For digital token authoring, equal OkLCh lightness steps at fixed chroma/hue provide a much more regular model-space path than equal HSL lightness steps.

This is a model property, not proof that every resulting UI step will have equal salience, contrast, readability, or perceived distance under every viewing condition.

### STUDIO JUDGMENT

OkLCh is the current preferred candidate authoring space for systematic digital product-color ramps when its geometry is useful, subject to explicit target-gamut mapping and real-context validation.

## Critical distinction — lightness is not relative luminance

Perceptual lightness coordinates such as CIELAB L* and Oklab L are not the same quantity as WCAG relative luminance.

Therefore:

- equal perceptual-lightness steps do not create equal WCAG contrast-ratio steps;
- a visually regular ramp is not automatically an accessibility scale;
- text/background pair selection must still be measured using the applicable accessibility method.

### STUDIO JUDGMENT

A product color scale should separate at least three questions:

1. **authoring regularity** — are tonal/chroma/hue changes coherent in the working model?
2. **semantic hierarchy** — do actual UI roles read in the intended order?
3. **accessibility/conformance** — do specific foreground/background/state pairs meet required thresholds and redundant-cue rules?

One scale cannot answer all three merely by being mathematically smooth.

## Gamut changes the ramp

Study 016 established that OkLCh and CIELCh coordinates may lie outside the destination gamut. A constant-chroma ramp can therefore cross the sRGB boundary at dark, light, or high-chroma ends.

When this happens, preserving a fixed numeric chroma value is no longer a valid shipping instruction. The author must choose a gamut-mapping policy.

### STUDIO JUDGMENT

For UI token ramps:

- preserve the intended lightness ordering first;
- avoid abrupt hue drift caused by naive clipping;
- reduce chroma when necessary to remain inside the target gamut;
- inspect whether gamut mapping creates perceptual bunching near one end of the scale;
- re-check accessibility after mapping;
- record final encoded production values separately from source authoring coordinates.

## Ramp-design decision framework

### HSL ramp

Use only when compatibility or simple editing is the goal and perceptual irregularity is acceptable or manually corrected.

### CIELCh ramp

Use when established CIE/ICC or physical-colour workflows are important, with explicit white-point/reference handling and gamut checks.

### OkLCh ramp

Use as a strong candidate for digital product token construction, interpolation, and controlled tonal/chroma editing, with destination-gamut and device validation.

### Neutral ramp

Near zero chroma, hue is unstable or meaningless. Build neutrals around lightness/luminance and contextual contrast rather than preserving an arbitrary hue angle.

### Semantic status ramp

Do not generate warning/success/error scales by equal numeric steps alone. Semantic recognition, contrast, color-vision diversity, non-color redundancy, and cross-state distinguishability are separate requirements.

## Product implications for MintTap Design Studio

1. Do not treat `50, 60, 70...` token labels as proof of perceptual spacing.
2. When a ramp is generated algorithmically, store the authoring space and parameters used.
3. Store final target-space values separately; an OkLCh source token is not itself the whole shipping specification.
4. For brand families, compare mapped sRGB and P3 results as systems, not isolated swatches.
5. For finance/data products, evaluate multiple adjacent states and chart colors together so gamut mapping does not collapse category separation.
6. For LogMate or other dark interfaces, test ramps at actual surface luminance and environmental brightness rather than judging them on a white palette sheet.

## OPEN

- Companion numerical practice establishes model-space behaviour but not human visual judgments.
- A rendered comparison on controlled displays is required.
- Browser implementation of current CSS Color 4 gamut mapping should be tested rather than inferred from hand calculations.
- A separate data-visualization study is required for categorical/sequential/diverging palette-system optimization.
- Dark-interface ramps require bright-environment and low-light physical-display validation.

## Status implication

Perceptual ramp-authoring literacy is now studied and numerically exercised, but the Color domain remains `CRITIQUE`. The remaining gate is dominated by rendered/browser/device evidence, physical viewing conditions, and production color-management validation rather than missing conceptual foundations.
