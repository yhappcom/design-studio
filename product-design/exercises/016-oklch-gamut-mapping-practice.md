# Exercise 016 — OkLCh Out-of-Gamut Mapping: Clipping vs Chroma Reduction

Status: PRACTICE COMPLETE / real-display and browser implementation validation pending.

Research basis: `research/016-color-gamut-wide-gamut-mapping.md`

## Purpose

Demonstrate with reproducible calculations that:

1. an OkLCh-authored color can be valid yet outside sRGB;
2. naive clipping and constant-lightness/constant-hue chroma reduction produce different colors;
3. clipping can sometimes be locally acceptable and sometimes not;
4. the mapping decision must be tied to the destination gamut and perceptual objective.

## SOURCE / algorithm basis

- W3C CSS Color Module Level 4, §14 Gamut Mapping: https://www.w3.org/TR/css-color-4/
- Björn Ottosson, Oklab transform: https://bottosson.github.io/posts/oklab/

The calculations use the standard Oklab/OkLCh transforms and the sRGB transfer function already established in Exercise 010.

For simple constant-L/H chroma reduction, chroma is reduced until the linear-light sRGB coordinates first fall inside `[0,1]`.

For the clipping comparison, the out-of-gamut color is converted to sRGB and each channel is clamped to `[0,1]`.

`ΔEOK` is ordinary Euclidean distance in Oklab coordinates for this exercise.

This practice is not a full independent implementation of every CSS gamut-mapping algorithm.

## Case A — Mint-family high-chroma mint

Reference hue/lightness derived from MintTap mint `#A8F0E9`:

- `L ≈ 0.90584`
- reference `C ≈ 0.07203`
- `h ≈ 188.37°`

Stress color:

`oklch(0.90584 0.18000 188.37)`

This is deliberately far more chromatic than the existing brand color.

### Raw conversion to encoded sRGB

Approximate components:

`[-1.2893, 1.0226, 0.9680]`

The negative red and green above 1 prove the color is outside sRGB.

### Naive clipping

Clipped sRGB:

`[0, 1, 0.9680]`

Converted back to OkLCh:

- `L ≈ 0.90271`
- `C ≈ 0.15558`
- `h ≈ 190.63°`

Approximate `ΔEOK` from the source: `0.02549`.

### Constant-L/H chroma-boundary reduction

Maximum sRGB chroma at the source lightness/hue is approximately:

`C_boundary ≈ 0.14802`

Mapped encoded sRGB:

`[0.2248, 1.0000, 0.9519]`

This preserves the source L and h by construction.

Approximate `ΔEOK` from the source: `0.03198`.

### Critique

The simple boundary reduction has a larger Euclidean OkLab distance than direct clipping, but clipping shifts hue and lightness. This demonstrates why “smallest raw distance” and “preserve authoring axes” are not always the same design objective.

The current CSS Local-MINDE JND is `0.02`. The direct clip here is above that threshold, so the current source color is not an obvious case for immediate local clipping under that draft method.

**KEEP:** explicit comparison.

**REJECT:** claim that chroma reduction is always numerically closer.

## Case B — saturated focus blue

Existing focus blue `#005FCC` is approximately:

- `L ≈ 0.50689`
- `C ≈ 0.18548`
- `h ≈ 257.73°`

Stress color:

`oklch(0.50689 0.23000 257.73)`

### Raw encoded sRGB

Approximately:

`[-0.2402, 0.3451, 0.8944]`

Out of gamut because red is negative.

### Naive clipping

`[0, 0.3451, 0.8944]`

Back-converted OkLCh:

- `L ≈ 0.51332`
- `C ≈ 0.22409`
- `h ≈ 261.16°`

Approximate `ΔEOK`: `0.01615`.

### Constant-L/H chroma-boundary reduction

Boundary chroma is approximately the original production blue:

`C_boundary ≈ 0.18548`

Mapped sRGB returns approximately:

`[0, 0.37255, 0.80000]` → `#005FCC`

Approximate source-to-boundary `ΔEOK`: `0.04452`.

### Critique

Here direct clipping has `ΔEOK < 0.02`, which illustrates why the CSS local-MINDE idea can sometimes accept a clipped color before reducing all the way to the strict constant-L/H boundary.

But this does **not** prove clipping is universally better. The source itself was selected near a gamut face where the clipped result stays relatively close.

**KEEP:** local decision based on measured behavior.

**REJECT:** “clipping is bad in every case.”

## Case C — high-chroma critical red

Reference from `#D9605D`:

- `L ≈ 0.63881`
- reference `C ≈ 0.15312`
- `h ≈ 23.80°`

Stress color:

`oklch(0.63881 0.29000 23.80)`

### Raw encoded sRGB

Approximately:

`[1.0642, -0.4947, 0.1236]`

Out of gamut on both red and green.

### Naive clipping

`[1, 0, 0.1236]`

Back-converted OkLCh:

- `L ≈ 0.62911`
- `C ≈ 0.25620`
- `h ≈ 26.74°`

Approximate `ΔEOK`: `0.03784`.

### Constant-L/H chroma-boundary reduction

`C_boundary ≈ 0.24680`

Mapped encoded sRGB:

`[1.0000, 0.1204, 0.2224]`

Approximate `ΔEOK`: `0.04320`.

### Critique

Again clipping is numerically a little closer in ΔEOK, yet it changes both hue and lightness. The correct production choice depends on whether brand/semantic hue stability or closest local color is the higher priority and which platform mapping algorithm governs rendering.

The direct clip is well above the draft Local-MINDE `0.02` threshold.

## Cross-case result

The three cases disprove several simplistic rules:

### False rule 1

“Out-of-gamut colors should always be RGB-clipped.”

**REJECT.** Clipping can shift hue/lightness and may be visibly damaging.

### False rule 2

“Constant-L/H chroma reduction always minimizes perceptual distance.”

**REJECT.** A clipped point can be closer in Euclidean Oklab distance, especially near certain gamut surfaces.

### False rule 3

“If OkLCh is perceptual, any OkLCh coordinate is safe to ship.”

**REJECT.** OkLCh is unbounded relative to practical RGB device gamuts.

### False rule 4

“A wider authoring gamut automatically improves the product.”

**REJECT.** It can create fallback inconsistency and production ambiguity.

## Transferable method

For an individual UI color authored outside the target gamut:

1. record source OkLCh and intended semantic role;
2. convert to the target RGB space without clipping and detect out-of-range channels;
3. compute a simple channel-clipped candidate;
4. compute a constant-lightness/constant-hue chroma-reduced candidate;
5. when the shipping platform defines a mapping algorithm, test that actual algorithm too;
6. compare color difference, hue/lightness drift, accessibility contrast, and semantic role;
7. validate on the real destination display.

## Product implication — MintTap mint

The existing MintTap `#A8F0E9` is safely inside sRGB and does not need a P3 version merely because P3 is available.

If a future brand refresh seeks a more saturated mint outside sRGB, the studio must explicitly decide whether:

- the saturated P3 version is the canonical brand appearance;
- the sRGB mapped fallback is still recognizably the same identity;
- the difference is acceptable across screenshots, web, Android, print, and marketing assets.

That decision cannot be made from the P3 swatch alone.

## OPEN / next practice

1. Reproduce the cases in a browser that implements current CSS Color 4 wide-gamut syntax and inspect actual used colors.
2. Compare current browser gamut mapping with the hand-calculated simple clipping and simple chroma boundary.
3. Display the same P3/sRGB pair on a real P3-capable device and an sRGB-limited reference.
4. Build equal-step HSL vs OkLCh ramps and record visual hierarchy failures.
5. Extend from individual colors to a categorical chart palette so mapping is evaluated as a system.

## Status implication

Gamut-mapping calculation practice is now recorded. The broader color domain remains `CRITIQUE`, not `PASS`, because real-device/platform validation remains outstanding.
