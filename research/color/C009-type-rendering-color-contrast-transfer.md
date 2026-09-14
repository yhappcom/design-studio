# C009 — Typography→Color Transfer: Nominal Contrast, Raster Coverage, Fallback, and Device-Pixel Dependence

Status: **PRACTICE + CROSS-DOMAIN TRANSFER VALIDATION / controlled Chromium rendering across font weight, Korean fallback, contrast margin, and DPR complete; human readability, physical-device/platform, broader scripts, and production validation pending**

## Why this study exists

Color studies 008/C002/C006/C008 use explicit foreground/background pair contracts. Typography T003–T006 separately show that font construction, fallback, rasterization, and export/runtime choices can change the pixels users actually see.

C009 asks:

> If the declared foreground/background colors do not change, how much can rendered text still change when font weight, fallback, line wrapping, or device-pixel ratio changes?

It also tests a common bad fix:

> When text looks weak, should Color simply darken the token?

C009 does **not** redefine WCAG conformance. It adds a separate rendered-diagnostic layer for product judgment.

Reproducibility artifacts:

- `C009-type-color-rendering-specimen.html`
- `C009-type-color-rendering-playwright.py`
- `C009-type-color-rendering-results.json`

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T006; T005 mixed-script fallback; T006 production outline/raster results; prior T003/T004 renderer/numeral evidence.
- Reusable finding: same nominal size does not imply equal glyph body or coverage; Korean fallback can change width and raster mass; clean source/export decisions can still produce different raster coverage.
- Replication / challenge / transfer opportunity: apply Color-defined foreground/background pairs to real Type conditions and measure the rendered field.
- Dependency / overlap: Type remains canonical owner of font selection, glyph construction, fallback, metrics, hinting, and renderer strategy. C009 studies Color consequences only.

### Color
- Evidence checked: Study 008, C002, C006, C007, C008.
- Reusable finding: contrast is a pair contract; numerical contrast is not complete perceptual proof; Color should not silently repair a peer-domain failure by changing semantic meaning.
- Replication / challenge / transfer opportunity: challenge `same contrast ratio = same practical text prominence`.
- Dependency / overlap: direct extension of Color contrast practice into actual Type rendering.

### Layout / Interaction
- Evidence checked: L003 fallback→layout, L004 tabular numerals, L005 Color-driven feature field, current Layout status through L005/I004.
- Reusable finding: fallback and numeric features can cross wrap thresholds; apparent density is not geometry alone.
- Transfer opportunity: use the exact T005 long Korean label at a bounded width while Color remains unchanged.
- Dependency / overlap: Layout owns wrapping/reflow policy; C009 records the Color consequence of the changed rendered ink field.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web owns real webfont loading/fallback, production CSS integration, cross-browser/device validation, and zoom.
- Implementation opportunity: reproduce C009 with real product `@font-face`, `font-display`, target browsers/OSes, zoom, and devices.
- Dependency / overlap: no substantive W### evidence exists at this checkpoint; Chromium/Linux is not Web PASS.

### Other / Cross-cutting / Future Specialist
- Evidence checked: W3C WCAG 2.2 Understanding SC 1.4.3 and CSS Fonts Module Level 4.
- Reusable finding: WCAG evaluates contrast from specified foreground/background colors because authors do not control font smoothing; the same guidance warns thin/unusual fonts can render much fainter in practice. CSS fallback may select different faces for different characters/runs.
- Dependency / overlap: human readability, low-vision performance, platform rendering, and ambient viewing remain later gates.

### Overlap decision
- **TRANSFER VALIDATION + METHOD CHALLENGE + RENDERED PRACTICE**.
- Why: Type already established raster/fallback variation and Color already established contrast contracts. C009 tests the interface between them.

---

# SOURCE — WCAG contrast and anti-aliased rendering are different evidence layers

Primary source:

- W3C WCAG 2.2, Understanding SC 1.4.3 Contrast (Minimum): `https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html`

W3C states that the 4.5:1 and 3:1 thresholds are evaluated from the specified foreground/background colors. Because authors do not control user-agent anti-aliasing/font smoothing, antialiased screen pixels are not the normative basis of the calculation.

The same guidance warns that thin or unusual fonts can be rendered much fainter than the specified text color and recommends, as best practice, stronger/thicker lines or a color pair that exceeds the normative requirement.

### SYNTHESIS

Keep two questions separate:

1. Does the declared foreground/background pair meet the applicable requirement?
2. Does the final Type + renderer + size + environment produce a robust text role?

A yes to the first does not prove the second.

### STUDIO JUDGMENT

Screenshot-pixel diagnostics must not be relabeled as WCAG conformance failures. Nominal pair compliance and rendered robustness are separate gates.

---

# SOURCE — font fallback can change the actual face beneath one Color token

Primary source:

- W3C CSS Fonts Module Level 4: `https://www.w3.org/TR/css-fonts-4/`

The font matching algorithm iterates the specified family list and selects a face that can render the relevant character/run. Fallback and font-display behavior can therefore cause text to be rendered with a different face while the CSS Color declaration remains unchanged.

### SYNTHESIS

A semantic Color token can remain identical while glyph geometry, coverage, width, and line breaking change underneath it.

---

# PEER EVIDENCE — Type already proves lower-layer coverage variation

T005 measured different glyph coverage/body metrics across Inter, Noto Sans CJK KR, NanumGothic, and NanumBarunGothic at the same nominal size. Its long Korean transfer string also changed width under different Korean fallbacks.

T006 converted the same clean cubic source into CFF and TrueType forms and still observed grayscale raster-coverage differences. Its largest reported bounded difference was approximately `+2.49%` TTF coverage for `o` at 20ppem versus CFF.

C009 therefore tests whether these Type dependencies materially affect Color-role appearance in Chromium.

---

# CONTROLLED BROWSER SPECIMEN

Environment:

- Chromium `144.0.7559.96` on Linux;
- Playwright Python;
- viewport `1400×700 CSS px`;
- DPR `1` and `2`;
- installed Inter, Noto Sans CJK KR, and NanumGothic confirmed available;
- no font binaries stored in Color research.

Four Color conditions:

| Condition | Foreground | Background | Nominal ratio |
| --- | --- | --- | ---: |
| light-near | `#767676` | `#FFFFFF` | `4.542:1` |
| light-strong | `#595959` | `#FFFFFF` | `7.005:1` |
| dark-near | `#7A858E` | `#11161B` | `4.828:1` |
| dark-strong | `#9CA6AE` | `#11161B` | `7.345:1` |

Primary Type conditions are all 14 CSS px:

- Inter Thin 100;
- Inter Regular 400;
- Inter SemiBold 600;
- Inter + Noto Sans CJK KR fallback;
- Inter + NanumGothic fallback;
- Inter tabular numerals.

A separate `365px` fixed-width Korean case tests whether fallback crosses a wrap threshold.

---

# DIAGNOSTIC METHOD

Each sample is screenshotted independently. Pixels are projected onto the encoded-sRGB foreground↔background line to derive a grayscale-antialiasing **mixture coefficient proxy**. That proxy is used only to compare normalized raster coverage and strong-core pixels.

The harness also calculates WCAG relative-luminance contrast for already-composited screenshot pixels against the background. This is **diagnostic only**. W3C conformance still uses the declared colors and permits anti-aliasing to be ignored.

No C009 pixel statistic is a validated readability score.

---

# RESULT A — same nominal Color pair, very different raster mass

Condition: light-near / DPR1 / nominal `4.542:1`.

| Type | Coverage density in ink bbox | Strong-core share | Median composited-pixel contrast* |
| --- | ---: | ---: | ---: |
| Inter Thin 100 | `0.0606` | `0.0000` | `1.41:1` |
| Inter Regular 400 | `0.1970` | `0.1101` | `2.19:1` |
| Inter SemiBold 600 | `0.2579` | `0.1710` | `2.68:1` |

`*` diagnostic only.

Regular has about **3.25×** the normalized coverage density of Thin in this specimen. SemiBold is about **1.31×** Regular.

All three use the same CSS foreground/background pair and therefore the same normative contrast ratio.

### REJECT

Reject:

> “Both labels are 4.54:1, therefore they have equivalent practical prominence.”

The rendered evidence does not support that claim.

---

# RESULT B — more Color contrast helps, but does not replace Type

At DPR1, Inter Regular on white:

- near pair `4.542:1` → median composited-pixel diagnostic `2.19:1`; `8.3%` of changed pixels ≥ `4.5:1`;
- strong pair `7.005:1` → median diagnostic `2.61:1`; `28.4%` of changed pixels ≥ `4.5:1`.

The stronger Color pair improves the screenshot-pixel contrast distribution.

But Inter Thin remains instructive: its strong-core share is `0` at DPR1 for both the near and strong pairs. Raising nominal contrast did not create full-intensity interior pixels in this 14px Thin specimen.

### STUDIO JUDGMENT

When small text looks weak, diagnose font family, weight/stroke, size, fallback/script, foreground/background pair, renderer/platform, semantic importance, and environment together. Do not automatically darken the global semantic token.

---

# RESULT C — DPR changes the raster field without changing CSS Color

Inter Regular / light-near:

| Metric | DPR1 | DPR2 |
| --- | ---: | ---: |
| Coverage density | `0.1970` | `0.2010` |
| Strong-core share | `0.1101` | `0.1547` |
| Median composited-pixel contrast* | `2.19:1` | `3.41:1` |
| Changed-pixel share ≥4.5* | `8.3%` | `37.9%` |

`*` diagnostic only.

CSS font, size, text, and Color values are unchanged.

### SYNTHESIS

A single desktop screenshot does not prove target-device text robustness. DPR is only one rendering variable; CoreText, DirectWrite, Skia/Flutter, zoom, subpixel strategy, physical density, and viewing distance remain OPEN.

---

# RESULT D — Korean fallback changes raster mass and width under identical Color

Light-near / DPR1 / identical Korean string:

| Fallback | DOM width | Coverage density | Strong-core share |
| --- | ---: | ---: | ---: |
| Inter + Noto Sans CJK KR | `362.97px` | `0.1940` | `0.1188` |
| Inter + NanumGothic | `367.72px` | `0.1671` | `0.0670` |

Noto's normalized coverage density is about **1.16×** NanumGothic in this bounded browser specimen.

This does not establish that one fallback is better. It establishes that one Color token does not equalize fallback appearance.

The exact magnitude differs from T005 because font size and rendering pipeline differ. The transferable conclusion is the dependency itself, not a universal numeric ratio.

---

# RESULT E — a small fallback width difference can cross a layout threshold

The same Korean label was placed in a fixed `365px` border-box.

- Noto fallback stays on one line: `32.80px` element height;
- NanumGothic fallback wraps: `49.59px` element height.

The Color values are identical.

### SYNTHESIS

Fallback can change how much colored ink occupies a surface by changing line count and spatial footprint.

### STUDIO JUDGMENT

Do not repair a locale/fallback wrap problem by silently assigning that locale a different secondary-text Color. First solve the Type/Layout problem. Reassess Color only after the final rendered role exists.

---

# FAILURE → REVISION MODEL

## Failure policy

> “Secondary text is above 4.5:1, therefore it is approved everywhere.”

This incorrectly collapses Color math, Type, fallback, rasterization, and device conditions into one number.

## Revised policy

Use two layers:

1. **Declared pair contract** — verify the required foreground/background pair mathematically.
2. **Target-rendered role validation** — for fragile roles, test representative font family/weight, scripts/fallbacks, minimum size, theme, renderer/platform, DPR/zoom/device, real strings, numeric punctuation, and relevant environment.

If the role is weak, decide whether the fix is stronger Type, larger Type, more Color contrast margin, different surface, reduced competing salience, or a combination.

---

# PROJECT READINESS TEST

Apply C009 especially when text is small, secondary, dense, operational, numeric, chart-adjacent, multilingual, thin-stroked, or close to a minimum contrast threshold.

Do **not** turn every text role into screenshot-pixel analysis, and do not use C009 metrics as a WCAG replacement, universal readability score, mandate for one weight, mandate for 7:1 everywhere, or justification for script-specific Color tokens by default.

Before final recommendation collect: semantic importance, font/fallback stack, weight/style, smallest actual size, scripts/locales, foreground/background surfaces, target platform/renderers/devices, theme, environment, and whether the role is numeric/chart/interaction-critical.

Failure conditions include:

- the pair passes but target Type is visibly fragile at intended size/environment;
- fallback materially changes prominence or wrapping;
- Color is being used to hide an unresolved Type/Layout defect;
- critical thin text sits barely above the minimum without target-render validation;
- theme transfer preserves token naming but destroys practical hierarchy;
- one screenshot/DPR is treated as universal proof.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: C009 confirms that the same semantic foreground token does not normalize weight/fallback raster mass. Inter Thin/Regular/SemiBold at 14px differed materially; Noto/Nanum fallback changed width and coverage, and a 365px specimen crossed from one line to two.
- Canonical section: Results A, D, E.
- Confirmation / contradiction / transfer note: **CONFIRMATION + TRANSFER** of T005/T006 into Color roles; exact magnitudes remain pipeline-specific.
- Scope limit: Color does not choose the font, fallback, hinting, or preferred weight.

### Layout / Interaction
- Useful finding/context: fallback can change the area occupied by a Color role without a token change; hierarchy diagnosis should separate pair, glyph coverage, and geometry.
- Canonical section: Result E and Failure→Revision model.
- Confirmation / contradiction / transfer note: confirms L003/L004/L005 separation of fallback geometry and feature-field effects.
- Scope limit: no optimal-width or human task-performance claim.

### Web Design
- Useful finding/context: real webfont/fallback states can alter text geometry and practical raster prominence while CSS colors remain unchanged.
- Web application / validation consequence: rerun with product `@font-face`, target `font-display`, relevant browsers/OSes, zoom, actual devices/themes, and localized strings.
- Confirmation / contradiction / transfer note: current Chromium/Linux result is a baseline, not Web production proof.
- Scope limit: no network font-load lifecycle or cross-browser result yet.

---

# Evidence level

Established: four pair contracts; 14px Inter weight comparison; T005-compatible Korean fallback comparison; fixed-width wrap transfer; DPR1↔DPR2 same-engine comparison; screenshot-derived coverage/core diagnostics; explicit WCAG-vs-rendered evidence separation; failure→revision project method.

Not established: human readability/reading speed, low-vision performance, real CVD observers, physical-device/ambient-light result, CoreText/DirectWrite/Skia/Flutter equivalence, real webfont load/swap/failure, broader scripts, or production project PASS.

Therefore C009 is **PRACTICE + CROSS-DOMAIN TRANSFER VALIDATION**, not PASS.
