# T002 — Raster Proof and Redraw Cycle: Join Darkness, Compact Survival, and Optical-Size Decisions

Status: **FOUNDATION / PRACTICE + CRITIQUE — surrogate raster cycle complete; compiled-font/device validation still OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Evidence artifact: `research/type/T002-raster-proof-redraw-cycle.svg`

## Purpose

The existing Exercise 002 critique identified the near-monoline lowercase `n` as having an intentionally dark stem-to-shoulder join and required a raster-driven redraw cycle before Optical Correction or Bézier practice could advance.

T002 performs that cycle rather than adding a new stylistic hypothesis.

The core question is:

> If a join that looks too dark at enlarged outline scale is relieved, does the correction remain structurally sound at compact raster sizes, or does the correction create a new small-size failure?

This is a controlled **vector → grayscale raster surrogate**, not a compiled-font or platform-rendering test. The distinction is central to the study.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `research/type/002-metrics-spacing-optical-rhythm.md`
  - `research/type/003-stroke-contrast-bezier-optics.md`
  - `research/type/005-numerals-punctuation-systems.md`
  - `research/type/009-typography-as-information-architecture.md`
  - `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`
  - `type-design/exercises/002-construction-curve-optics.svg`
  - `type-design/exercises/002-construction-curve-optics-critique.md`
- Reusable finding:
  - outline form, optical compensation, spacing, and raster behavior are different diagnostic layers;
  - intended-size proof is required before a large-outline correction is accepted;
  - sidebearings must not be used to hide internal weight accumulation.
- Replication / challenge / transfer opportunity:
  - reproduce the original dark-join diagnosis quantitatively and test whether a redraw actually improves the intended condition without causing a new failure.
- Dependency or overlap:
  - a real font source and renderer matrix are still needed before this can become production evidence.

### Color
- Evidence checked:
  - `research/color/008-color-luminance-contrast-hierarchy.md`
  - `research/color/C001-web-color-user-override-resilience.md`
- Reusable finding:
  - apparent edge definition and hierarchy depend on luminance/contrast and viewing conditions; one dark-on-light proof cannot establish all rendered conditions.
- Replication / challenge / transfer opportunity:
  - future proof should composite the same glyph rasters under representative light/dark and reduced-contrast conditions while holding geometry constant.
- Dependency or overlap:
  - Color owns canonical contrast/viewing-condition evidence; Type owns the contour/raster consequence for letterform survival.

### Layout / Interaction
- Evidence checked:
  - `research/layout/L002-whitespace-density-spatial-rhythm.md`
  - latest `progress/LAYOUT_STATUS.md`, including I001 handoffs.
- Reusable finding:
  - compactness is task-dependent; dense interfaces must use real typography rather than placeholder geometry;
  - narrow/dense/localized states provide realistic type stress contexts.
- Replication / challenge / transfer opportunity:
  - later place the same research font into compact, standard, and spacious density contexts instead of choosing the minimum type size from an isolated specimen.
- Dependency or overlap:
  - Layout determines whether a 14px-like role is actually required by the product; Type determines whether the face survives that role.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`
  - `research/web/README.md`
- Reusable finding:
  - Web owns actual browser/page integration and must validate Type findings under browser font loading, zoom, responsive layout, localization, and device conditions.
- Implementation/application validation opportunity:
  - once a minimal research font exists, render the same R0/R1 forms in browser conditions and compare real CSS sizing, zoom, DPR, fallback, and antialiasing behavior.
- Dependency or overlap:
  - no substantive `W###` study was available at the start of T002, so no browser result is inferred here.

### Other / cross-cutting / future specialist
- Evidence checked:
  - Microsoft OpenType TrueType fundamentals and glyph-instruction guidance;
  - FreeType outline/grid-fitting and glyph-metric documentation;
  - OpenType registered `opsz` axis documentation.
- Reusable finding:
  - a stored outline is scaled, potentially grid-fitted/hinted, then scan-converted before becoming pixels;
  - grid-fitting can materially alter small-size dimensions and metrics;
  - optical-size variation exists specifically to vary design for different text sizes.
- Dependency or overlap:
  - actual renderer behavior and human reading performance remain outside what this surrogate alone proves.

### Overlap decision
- Reuse / deliberate repetition / extension / contradiction review / method comparison / transfer validation / project-specific study:
  - **REPLICATION + EXTENSION + TRANSFER VALIDATION PREPARATION**.
- Why:
  - Exercise 002 already diagnosed the dark join, but it did not prove the diagnosis at intended size or show a redraw cycle. T002 repeats the same form deliberately to determine whether the correction survives raster reduction and to define the next real-renderer test.

---

## 1. SOURCE — the outline is not the final rendered glyph

Microsoft's TrueType fundamentals describe a rendering path in which the stored outline is scaled to the requested size, instructions may grid-fit the scaled outline, and the resulting outline is scan-converted to a bitmap.

Sources:
- https://learn.microsoft.com/en-us/typography/opentype/otspec170/ttch01
- https://learn.microsoft.com/en-us/typography/truetype/

Microsoft further describes grid-fitting as a way to preserve important design characteristics such as consistent stem weight, text color, spacing, and dropout control at different sizes/devices.

### SYNTHESIS

A contour correction cannot be accepted merely because the enlarged vector looks cleaner. The relevant evidence is the final rendered behavior at the intended size and renderer.

### STUDIO JUDGMENT

For Type practice, every correction to a compact-use glyph should be classified through at least two views:

1. outline/construction view;
2. intended-size raster view.

When the two disagree, the raster failure is not automatically a reason to keep a bad outline; instead, identify whether the problem belongs to outline design, hinting/grid-fitting, renderer behavior, or an optical-size strategy.

---

## 2. SOURCE — grid-fitting can change dimensions and metrics

FreeType's glyph documentation notes that small-size scaling can create artifacts and that grid-fitting/hinting aligns important features to the target pixel grid. Its metric documentation explicitly notes that grid-fitting may change glyph width/height, bearings, and advances, and that the effect is resolution-dependent.

Sources:
- https://freetype.org/freetype2/docs/glyphs/glyphs-2.html
- https://freetype.org/freetype2/docs/glyphs/glyphs-3.html
- https://freetype.org/freetype2/docs/reference/ft2-glyph_retrieval.html

### SYNTHESIS

The surrogate result below is useful for exposing geometry-to-pixel pressure, but it is deliberately weaker evidence than a compiled font rendered through FreeType/DirectWrite/CoreText/browser stacks.

### OPEN

T002 does not answer how native TrueType hints, CFF hints, autohinting, grayscale/LCD rendering, or platform text engines would alter R0/R1.

---

## 3. SOURCE — size-specific design is a legitimate family strategy, not a rescue assumption

OpenType registers `opsz` as the Optical Size design-variation axis, used to vary a design for different text sizes. The specification also cautions that perceived size depends on actual display scaling and viewing conditions, not only a nominal font-size number.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/otspec190/dvaraxistag_opsz

### SYNTHESIS

T002's finding that one redraw improves a large-outline problem while weakening compact pixels makes optical-size strategy **relevant to investigate**, but does not prove that an `opsz` axis is required.

### STUDIO JUDGMENT

Do not add an optical-size axis because a single glyph is difficult. First determine whether a robust common outline can satisfy the product's real size range. Only consider separate optical cuts or `opsz` when repeated family-level evidence shows materially different size requirements.

---

## 4. Controlled method

### 4.1 Source form R0

R0 is the original Exercise 002 D `n` construction. Its stem remains 38 source units wide, with an intentionally dark arch/stem transition.

Original shoulder path:

```text
M158 735
C200 668 295 666 328 736
C338 757 341 785 341 820
L341 900
L303 900
L303 810
C303 743 280 712 237 712
C194 712 158 750 158 815
Z
```

### 4.2 Redraw R1

R1 changes the shoulder/join geometry without altering the stem rectangle. The objective is to remove excess black accumulation rather than disguise it with spacing.

Redrawn shoulder path:

```text
M158 748
C196 684 288 677 327 739
C338 758 341 787 341 820
L341 900
L303 900
L303 810
C303 750 280 715 238 715
C198 715 170 746 158 795
Z
```

### 4.3 Raster surrogate

- source x-height model: 250 design units (`650 → 900`);
- mapped to x-height-equivalent targets: `14 / 24 / 48 px`;
- renderer: CairoSVG grayscale coverage rasterization;
- no hinting;
- no shaping;
- no font metrics;
- no OS/browser text renderer;
- no compiled font.

The SVG evidence embeds the exact raster samples rather than relying on a browser to redraw the vector at display time.

### 4.4 Measurement

Nine source-x positions across the shoulder were sampled:

```text
158, 165, 175, 190, 205, 220, 240, 260, 280
```

For each sample column, the contiguous shoulder run was measured after thresholding grayscale at `L < 128`.

This threshold measurement is not a human legibility score. It is a controlled comparison of how much strong-coverage black survives between R0 and R1.

---

## 5. Results

| x-height surrogate | R0 mean run | R1 mean run | Change | Median | ≤1px sample columns |
| --- | ---: | ---: | ---: | --- | --- |
| 14 px | 2.00 px | 1.44 px | -27.8% | 2 → 1 px | 2/9 → 5/9 |
| 24 px | 3.22 px | 2.22 px | -31.0% | 3 → 2 px | 0/9 → 2/9 |
| 48 px | 6.67 px | 4.89 px | -26.7% | 6 → 4 px | 0/9 → 0/9 |

### Observation A — the redraw is not cosmetic

R1 removes roughly 27–31% of the thresholded shoulder thickness across all three surrogate sizes. The changed join is therefore materially different, not a negligible vector tweak.

### Observation B — R1 repairs the enlarged dark-join diagnosis

At 48px-equivalent scale, R1 produces a visibly lighter shoulder transition and reduces the measured median run from 6px to 4px.

This confirms the original critique's diagnosis that the join could be relieved through drawing rather than through spacing.

### Observation C — the same correction creates a compact-size risk

At 14px-equivalent scale, the median strong-coverage shoulder run falls from 2px to 1px and five of nine sampled positions become one pixel or less at the chosen threshold.

R1 therefore introduces a new failure hypothesis: **compact fragility**.

### Classification

- R0 enlarged problem: **drawing / optical compensation**.
- R1 compact problem: **drawing × raster interaction**.
- Not primarily a spacing problem.
- Kerning/sidebearing changes would be the wrong repair mechanism for either defect.

---

## 6. The important learning result: failure → redraw → new failure

T002 is valuable precisely because the first correction is not declared successful.

The cycle is:

1. **Failure identified:** R0's join is too dark at enlarged construction scale.
2. **Redraw:** R1 removes weight from the join/shoulder.
3. **Re-proof:** R1 is materially lighter, but the compact raster loses strong-coverage thickness.
4. **New diagnosis:** one outline may be fighting incompatible optical requirements across the tested size range.
5. **Gate remains open:** renderer/hinting evidence is needed before deciding whether the outline itself is too thin at compact size.

This is stronger professional evidence than simply producing a more attractive redraw.

---

## 7. Alternatives now justified for further testing

### A. One robust compromise outline

Develop an R2 between R0 and R1 and test whether a single contour can keep the join calm at 36–48px-like roles while retaining enough shoulder mass around 14–16px-like roles.

**Benefit:** simplest production architecture.

**Risk:** compromise may be merely mediocre at both ends.

### B. Separate static optical cuts

Use a compact/text drawing and a larger/display drawing if repeated family-level proof shows materially different needs.

**Benefit:** explicit control without requiring a variable axis.

**Risk:** more sources, testing, naming, and application logic.

### C. `opsz` or another optical-size family strategy

If multiple glyph families show the same size-dependent conflict, investigate a continuous optical-size axis or equivalent family architecture.

**Benefit:** systematic size adaptation.

**Risk:** engineering complexity, browser/app activation behavior, interpolation QA, and false precision if the product's actual rendered size/viewing distance is not controlled.

### Current disposition

**No option is selected.** The next evidence must come from a real research font and renderer matrix.

---

## 8. Project Readiness Test

### When should this knowledge be applied?

Use this method when:

- a custom or highly controlled typeface must work in compact UI/data roles;
- joins, counters, apertures, diagonals, or thin features appear different between outline view and target size;
- one family is expected to serve both compact operational text and larger identity/readout roles;
- a design decision is being made about hinting, optical cuts, `opsz`, or minimum approved size.

### When should it not be over-applied?

Do not create optical variants merely because one enlarged curve can be refined further. Do not use this workflow to micromanage a system font whose raster behavior is already an accepted platform dependency unless the project has evidence of an actual task failure.

### Project information required before deciding

- smallest and typical rendered text roles;
- actual CSS/logical size and device-pixel context where relevant;
- target operating systems, browsers, app rendering stacks, and devices;
- device-pixel ratio / display class;
- intended light/dark and contrast conditions;
- languages/scripts and fallback families;
- whether the face is used for dense operational data, prose, navigation, or sparse display identity;
- font format, performance, loading, and implementation constraints;
- whether the application can reliably select optical variants/features.

### Concrete design decisions this can change

- minimum approved use size;
- join/counter/aperture compensation;
- whether compact UI should use a different face or optical cut from display/brand roles;
- whether manual hinting/autohinting is worth the engineering cost;
- whether one common outline is sufficient;
- whether `opsz` or static optical sizes deserve family-level prototyping.

### Failure modes

1. **Outline-only approval:** a smooth enlarged curve is assumed to be a good text glyph.
2. **Compact overcorrection:** weight is removed to fix a large-size dark spot and a critical feature becomes one-pixel fragile.
3. **Spacing disguise:** sidebearings are changed to compensate for an internal contour defect.
4. **Renderer inference:** an SVG raster is treated as proof of DirectWrite/CoreText/FreeType/browser behavior.
5. **Optical-axis enthusiasm:** `opsz` is added before family-level evidence shows a repeatable size-dependent problem.
6. **Context blindness:** minimum size is chosen without knowing whether the product actually needs the compact role.
7. **Contrast blindness:** a contour is approved on one foreground/background pair and assumed to survive all viewing conditions.

### Which specialist evidence must be combined?

- **Color:** representative contrast, background, viewing, and environmental conditions.
- **Layout / Interaction:** actual density and task contexts that determine required minimum text roles.
- **Web Design:** browser font loading, CSS sizing, zoom, DPR, responsive context, and real browser rendering for web deployment.

### How should the recommendation change under different constraints?

- If the product never uses the face below a large display role, R1-like relief may be more viable and a compact optical strategy may be unnecessary.
- If the face must operate in dense 14–16px-like data rows, compact survival becomes a first-order requirement and a stronger/common outline or compact optical cut may be preferable.
- If platform/system fonts are acceptable for operational UI, a bespoke face can be restricted to identity/readout roles rather than forcing one family to solve every size.
- If cross-platform renderer consistency is critical, hinting and renderer-specific validation become more important than a single local SVG proof.

### Validation plan

The next Type validation should build a **minimal non-production research font** containing enough control glyphs to test the same problem through real font machinery. Minimum useful set:

```text
H O n o
```

Preferably extend with:

```text
0 1 I l : + , . / -
```

Then render at matched sizes through:

1. FreeType with hinting off;
2. FreeType native/autohint modes as appropriate;
3. grayscale versus other relevant target modes;
4. at least one actual platform/browser stack when Web evidence becomes available;
5. representative light/dark/contrast contexts from Color;
6. compact/standard/spacious contexts informed by L002.

Record whether the R0/R1 distinction is confirmed, limited, reversed, or made irrelevant by the real renderer.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: a genuine failure→redraw→re-proof cycle now exists for the D `n`; R1 fixes enlarged join mass but creates compact-size fragility in the surrogate.
- Canonical section: `5. Results` and `6. The important learning result`.
- Confirmation / contradiction / transfer note: confirms Study 003's warning that enlarged outline quality does not prove target-size quality.
- Scope limit: no compiled-font or hinting proof yet.

### Color
- Useful finding/context: R0/R1 should be held geometrically constant while foreground/background contrast and viewing conditions vary.
- Canonical section: `8. Project Readiness Test` and validation plan.
- Confirmation / contradiction / transfer note: transfers Color's context-dependent edge/contrast principle into a controlled Type raster question.
- Scope limit: T002 does not establish color thresholds or environmental performance.

### Layout / Interaction
- Useful finding/context: if a project chooses a compact density strategy, minimum type size becomes a contour/raster constraint, not merely a spacing token decision.
- Canonical section: `7. Alternatives` and project inputs.
- Confirmation / contradiction / transfer note: supports L002's requirement to use real text metrics and task-dependent density.
- Scope limit: T002 does not determine which density strategy a product should use.

### Web Design
- Useful finding/context: the same R0/R1 forms are a ready transfer test for actual browser rendering, CSS sizing, zoom, DPR, and fallback conditions once a minimal research font exists.
- Web application / validation consequence: compare final browser pixels and layout behavior rather than redrawing the SVG directly in-browser.
- Confirmation / contradiction / transfer note: T002 defines a Type-side failure condition that Web can confirm or falsify.
- Scope limit: no browser evidence is claimed here.

---

## Status implication

T002 completes a **real failure → redraw → re-proof cycle** at the surrogate-raster level.

This strengthens the Type program's evidence for:

- optical-correction critique;
- raster-awareness;
- diagnosing drawing vs spacing errors;
- resisting premature optical-size decisions.

It does **not** promote the following to PASS:

- Bézier drawing discipline;
- Optical Correction;
- rasterization/rendering;
- family construction;
- platform/browser typography.

The next highest-value Type block is a minimal real font-source + renderer matrix for these control forms, unless a live project makes native numeral/punctuation or mixed-script fallback more urgent.

**Foundation gate remains CLOSED.**
