# Exercise 013 — CIELAB, CIEDE2000, and Oklab Difference Comparison

Status: PRACTICE COMPLETE / controlled visual comparison and gamut stress still pending.

Research basis: `research/013-perceptual-color-spaces-difference.md`

## Purpose

Compare several colour-difference representations on the same practical sRGB pairs and verify that:

1. the chosen metric changes the numeric result;
2. raw magnitudes from different metrics are not interchangeable;
3. colour-difference numbers do not replace accessibility contrast or semantic validation.

## Sources

- ISO/CIE 11664-4:2019 — CIELAB: https://www.cie.co.at/publications/colorimetry-part-4-cie-1976-lab-colour-space-1
- ISO/CIE 11664-6:2022 — CIEDE2000: https://www.cie.co.at/publications/colorimetry-part-6-ciede2000-colour-difference-formula-1
- Sharma, Wu, Dalal (2005), implementation notes and supplemental test data: https://hajim.rochester.edu/ece/sites/gsharma/ciede2000/
- W3C CSS Color 4 — Lab/LCH and Oklab/OkLCh: https://www.w3.org/TR/css-color-4/
- Björn Ottosson — Oklab: https://bottosson.github.io/posts/oklab/

## Calculation pipeline

For CIELAB / CIEDE2000:

`encoded sRGB`

→ inverse sRGB transfer function

→ `linear-light sRGB`

→ `XYZ D65`

→ ICC-style linearized Bradford D65→D50 adaptation

→ `CIELAB D50`

→ `ΔE*ab` and `ΔE00`

For Oklab:

`encoded sRGB`

→ inverse sRGB transfer function

→ `linear-light sRGB`

→ Oklab D65 transform

→ Euclidean `ΔEOK`

The different distance scales are reported side by side only for comparative behaviour. They are **not normalized to a shared unit**.

## Implementation sanity check

The CIEDE2000 implementation was checked against the well-known Sharma/Wu/Dalal supplemental test pair:

- reference: `L*=50, a*=2.6772, b*=-79.7751`
- sample: `L*=50, a*=0, b*=-82.7485`
- expected `ΔE00 ≈ 2.0425`
- reproduced result: `2.04246`

This does not make the exercise an official CIE software implementation; it only reduces the risk of a coding error in this practice calculation.

## Pair A — operational blue shift

`#005FCC` → `#0066D0`

CIELAB D50:

- `#005FCC ≈ [40.999, 11.002, -64.201]`
- `#0066D0 ≈ [43.284, 8.145, -62.796]`

CIELCh D50:

- first ≈ `[L 40.999, C 65.137, h 279.725°]`
- second ≈ `[L 43.284, C 63.321, h 277.390°]`

Differences:

- `ΔE*ab ≈ 3.919`
- `ΔE00 ≈ 2.502`
- `ΔEOK ≈ 0.01887`

### Observation

CIE76 reports a larger raw distance than CIEDE2000 because ΔE00 applies perceptual weighting and interaction corrections. `ΔEOK` is on an entirely different numeric scale and cannot be compared to “2.502” by magnitude alone.

## Pair B — neutral tonal shift

`#595959` → `#616161`

CIELAB D50:

- first `L* ≈ 37.824`
- second `L* ≈ 41.143`
- chromatic components are effectively neutral numerical residue.

Differences:

- `ΔE*ab ≈ 3.318`
- `ΔE00 ≈ 2.898`
- `ΔEOK ≈ 0.02861`

### Observation

For this pair, most of the difference is lightness. The relationship between CIE76 and CIEDE2000 is different from the blue pair, demonstrating that a single global conversion factor between the two metrics would be invalid.

## Pair C — warm critical-state variation

`#D9605D` → `#D85A59`

CIELAB D50:

- first ≈ `[56.572, 48.316, 26.414]`
- second ≈ `[55.291, 50.433, 27.061]`

Differences:

- `ΔE*ab ≈ 2.558`
- `ΔE00 ≈ 1.370`
- `ΔEOK ≈ 0.01217`

### Observation

Again CIEDE2000 compresses the difference substantially relative to raw Euclidean CIELAB distance. This is exactly why a tolerance written only as “ΔE < N” is incomplete unless the formula is named.

## Pair D — MintTap-family mint variation

`#A8F0E9` → `#9EEAE2`

CIELAB D50:

- first ≈ `[89.915, -24.290, -4.165]`
- second ≈ `[87.583, -25.674, -3.996]`

OkLCh:

- first ≈ `[L 0.90584, C 0.07203, h 188.369°]`
- second ≈ `[L 0.88529, C 0.07587, h 187.585°]`

Differences:

- `ΔE*ab ≈ 2.717`
- `ΔE00 ≈ 1.646`
- `ΔEOK ≈ 0.02093`

### Observation

The hue is relatively stable while lightness/chroma shift. A brand review could legitimately care about this difference, but whether it is acceptable cannot be decided from one number without specifying medium, viewing condition, reproduction tolerance, and brand intent.

## Failure case 1 — treating ΔE as WCAG contrast

Rejected claim:

> “These two colours are ΔE00 = 3 apart, therefore the text/UI state is accessible.”

**REJECT.**

ΔE00 is a colour-difference model. WCAG contrast evaluates relative-luminance contrast for specified accessibility questions. The two are not substitutes.

## Failure case 2 — comparing ΔE00 and ΔEOK raw numbers

Rejected claim:

> “0.02 ΔEOK is much smaller than 2.5 ΔE00, therefore Oklab says the colours are 125× closer.”

**REJECT.**

The coordinates and scales differ. Cross-formula raw magnitude ratios have no such interpretation.

## Failure case 3 — assuming cylindrical hue is meaningful at zero chroma

The near-neutral pair produces a numerically computable hue angle from tiny residual `a*`/`b*` values. That angle is not useful as a perceived-hue descriptor because chroma is effectively zero.

**REJECT:** using hue angle as a stable token property near the neutral axis.

## SYNTHESIS

1. Name the colour-difference formula every time a tolerance is specified.
2. CIE76 is a useful baseline but retains CIELAB non-uniformity.
3. CIEDE2000 changes weighting by lightness, chroma, hue, and their interactions.
4. Oklab/OkLCh is operationally attractive for digital authoring but does not erase gamut or viewing-condition problems.
5. ΔE values are not accessibility contrast ratios.
6. Hue becomes ill-conditioned as chroma approaches zero.
7. Colour-match acceptance remains task- and medium-specific.

## STUDIO JUDGMENT

For MintTap Design Studio:

- use OkLCh preferentially as a candidate palette-authoring coordinate system when its behaviour is advantageous;
- retain explicit target sRGB/P3 values for production handoff;
- use CIEDE2000 only when its stimulus/reference-condition assumptions are appropriate or when a governed workflow requires it;
- never write a naked tolerance such as `ΔE < 2` without the formula, reference condition, and medium;
- keep brand fidelity, accessibility, and perceptual palette construction as separate review gates.

## OPEN / next practice

1. Build equal-step ramps in HSL, CIELCh, and OkLCh and compare perceived lightness/hue regularity on real displays.
2. Force high-chroma OkLCh samples outside sRGB and compare clipping versus chroma-reduction gamut mapping.
3. Compare CIEDE2000 and ΔEOK against controlled visual judgments for a limited UI-oriented sample set without claiming universal psychophysical validity.
4. Continue the pending CIE spectral-integration/observer-comparison exercise.

## Status implication

Perceptual colour-space practice has begun and a formula-selection failure analysis is now recorded. The broader colour domain remains `CRITIQUE` pending real-display/environmental validation, spectral work, and production colour-management evidence.