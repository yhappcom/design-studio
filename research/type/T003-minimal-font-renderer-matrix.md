# T003 — Minimal Research Font + FreeType Renderer Matrix

Status: **FOUNDATION / PRACTICE + TRANSFER VALIDATION — real compiled font evidence established; platform/browser/device validation still OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Reproducible source: `research/type/T003-minimal-research-font-renderer-matrix.py`  
Evidence artifact: `research/type/T003-minimal-font-renderer-matrix.svg`

## Purpose

T002 showed a useful but limited result: a join-relief redraw improved the enlarged lowercase `n` while becoming more fragile in a simple unhinted grayscale raster surrogate.

T003 asks the next professional question:

> Does that R0/R1 difference survive when the same contours are put into an actual TrueType font and rendered through a real font engine with different hinting strategies?

The objective is not to select R0 or R1. It is to determine which parts of T002 are genuinely outline-driven, which are renderer-dependent, and what a project must know before approving an optical correction or minimum use size.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `research/type/002-metrics-spacing-optical-rhythm.md`
  - `research/type/003-stroke-contrast-bezier-optics.md`
  - `research/type/T002-raster-proof-redraw-cycle.md`
  - current `progress/TYPE_STATUS.md`
- Reusable finding:
  - intended-size raster proof is part of type design, not an implementation afterthought;
  - drawing, spacing, metrics, and raster behavior must be diagnosed separately;
  - T002's R0/R1 pair provides a controlled redraw question rather than a new stylistic direction.
- Replication / challenge / transfer opportunity:
  - repeat T002 with a compiled TrueType font and compare multiple FreeType hinting modes.
- Dependency / overlap:
  - manual TrueType instructions, CoreText, DirectWrite, browser engines, device rasterization, and production font QA remain open.

### Color
- Evidence checked:
  - `research/color/008-color-luminance-contrast-hierarchy.md`
  - `research/color/C001-web-color-user-override-resilience.md`
  - latest `progress/COLOR_STATUS.md`, including C002.
- Reusable finding:
  - grayscale coverage is not the same as perceived weight under every foreground/background or display condition;
  - text roles must be validated in real rendering contexts.
- Replication / challenge / transfer opportunity:
  - later composite identical FreeType alpha maps under Color-defined light/dark/reduced-contrast conditions.
- Dependency / overlap:
  - Color owns luminance/contrast/viewing conditions; T003 only measures the font-engine output alpha map.

### Layout / Interaction
- Evidence checked:
  - `research/layout/L002-whitespace-density-spatial-rhythm.md`
  - latest `progress/LAYOUT_STATUS.md`, including I001.
- Reusable finding:
  - density is task-dependent and compact surfaces must use real typography rather than placeholder boxes;
  - navigation and responsive contexts provide real long-label/fallback stress cases.
- Replication / challenge / transfer opportunity:
  - apply renderer-tested type to L002 compact/standard/spacious surfaces before deciding a product minimum size.
- Dependency / overlap:
  - Layout determines whether compact type is necessary; Type determines whether a chosen face survives it.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`
  - `research/web/README.md`
- Reusable finding:
  - Web owns real browser/page/font-loading/zoom/device validation.
- Implementation/application validation opportunity:
  - use the T003 font-source method to build a later browser specimen instead of drawing SVG approximations.
- Dependency / overlap:
  - no substantive `W###` evidence was available at the start of T003, so no browser behavior is inferred.

### Other / cross-cutting / future specialist
- Evidence checked:
  - Microsoft TrueType fundamentals and OpenType glyph-instruction guidance;
  - FreeType glyph outline, metric, loading, and render-mode documentation;
  - OpenType `opsz` documentation from T002.
- Reusable finding:
  - grid-fitting may alter outline positions, bitmap dimensions, bearings, and advances;
  - FreeType exposes no-hint, normal auto-hint, and light auto-hint behaviors with different goals;
  - strong auto-hint positioning requires attention to `lsb_delta` / `rsb_delta`.
- Dependency / overlap:
  - actual user reading quality and platform-specific text stacks remain outside this experiment.

### Overlap decision
- Reuse / deliberate repetition / extension / contradiction review / method comparison / transfer validation / project-specific study:
  - **REPLICATION + METHOD COMPARISON + TRANSFER VALIDATION**.
- Why:
  - T002 deliberately left renderer validity open. T003 repeats the same controlled R0/R1 geometry in a real font engine to test whether the prior conclusion is stable across rendering methods.

---

## 1. SOURCE — hinting can change more than visual sharpness

Microsoft's TrueType fundamentals describe the raster process as outline scaling → grid-fitting/instruction processing → scan conversion. The purpose of grid-fitting includes preserving characteristics such as stem consistency, spacing, and avoiding pixel dropouts.

Sources:
- https://learn.microsoft.com/en-us/typography/opentype/otspec170/ttch01
- https://learn.microsoft.com/en-us/typography/truetype/

FreeType likewise documents that grid-fitting can change glyph width/height, bearings, and advances. Its API distinguishes unhinted linear advance from the hinted advance returned after loading.

Sources:
- https://freetype.org/freetype2/docs/glyphs/glyphs-2.html
- https://freetype.org/freetype2/docs/glyphs/glyphs-3.html
- https://freetype.org/freetype2/docs/reference/ft2-glyph_retrieval.html

### SYNTHESIS

A type-design decision at compact size is partly an outline problem and partly a renderer contract. “Same source metrics” does not guarantee identical hinted pixel metrics at every size and mode.

---

## 2. SOURCE — FreeType normal and light hinting have different horizontal behavior

FreeType documents `FT_LOAD_TARGET_NORMAL` as the normal gray-level hinting algorithm. `FT_LOAD_TARGET_LIGHT` uses lighter hinting and primarily vertical snapping, which is intended to preserve horizontal spacing more closely.

FreeType also documents `lsb_delta` and `rsb_delta` for correct positioning with strong auto-hinting and warns that ignoring them can create incorrect spacing.

Source:
- https://freetype.org/freetype2/docs/reference/ft2-glyph_retrieval.html

### STUDIO JUDGMENT

Renderer comparisons must report not only bitmap appearance but also:

- hinted advance;
- linear/unhinted advance;
- sidebearing deltas where the engine exposes them;
- the positioning algorithm used for repeated text.

A screenshot of one glyph is not enough to approve a compact UI face.

---

## 3. Reproducible research font

T003 creates a minimal, non-production quadratic TrueType font in code using FontTools.

### Font structure

- UPM: `1000`
- x-height: `500`
- cap height: `700`
- glyphs: `.notdef`, `space`, `H`, `O`, `n`, `n.alt`, `o`
- R0 is mapped to normal lowercase `n` (`U+006E`)
- R1 is mapped to `U+E000` only to enable side-by-side research rendering
- R0 and R1 both have source advance width `560`
- no manual TrueType instructions are authored

### Outline conversion

The T002 cubic study paths are normalized into a 1000-UPM space and converted into TrueType quadratic contours with a controlled `cu2qu` tolerance.

Inspectability check on the generated font:

| Glyph | Contours | Points | Bounding box | Source advance |
| --- | ---: | ---: | --- | ---: |
| R0 `n` | 2 | 24 | `(40, 0, 482, 500)` | 560 |
| R1 `n.alt` | 2 | 23 | `(40, 0, 482, 500)` | 560 |

A TTX export/compile round trip preserved glyph order, UPM, x-height, contour counts, bounding boxes, and metrics. Byte identity is not claimed or required.

### Scope limit

This is the first **actual compiled font** in this learning sequence, but it is still a research instrument. It does not claim:

- final node placement;
- production overlap removal;
- manual hinting quality;
- complete character set;
- shaping/OpenType feature system;
- production naming/versioning;
- cross-platform compatibility;
- FontBakery/production QA.

---

## 4. Renderer matrix

The generated TrueType font was rendered through FreeType at `14 / 16 / 24 / 48 ppem` using three modes:

1. **no-hint** — `FT_LOAD_NO_HINTING`;
2. **autohint-normal** — forced FreeType auto-hinter with `FT_LOAD_TARGET_NORMAL`;
3. **autohint-light** — forced auto-hinter with `FT_LOAD_TARGET_LIGHT`.

The bitmap output is real FreeType 8-bit coverage data. No SVG rasterizer is involved in this stage.

### Measurement

For each glyph/mode/size:

- total alpha coverage was converted to pixel-equivalent ink area;
- pixels with alpha `>=128` were counted as a simple strong-coverage diagnostic;
- bitmap width/height and hinted advance were recorded.

These measures are comparison instruments, not readability scores.

---

## 5. Core results

### Coverage difference R1 relative to R0

| ppem | no-hint | autohint-normal | autohint-light |
| ---: | ---: | ---: | ---: |
| 14 | -6.0% | -2.9% | -1.9% |
| 16 | -6.7% | **-12.1%** | -6.0% |
| 24 | -6.2% | -3.7% | -1.9% |
| 48 | -6.4% | -8.9% | -8.5% |

The same contour difference does **not** produce a fixed rendered difference. The renderer and ppem can suppress or amplify it.

### 14 ppem — T002's compact-difference signal can be suppressed

- no-hint strong pixels: `13 → 11`;
- autohint-normal: `15 → 15`;
- autohint-light: `13 → 13`.

In other words, the auto-hinter can largely regularize the compact strong-pixel difference that looked more severe in the T002 simple surrogate.

**Result:** T002's compact-fragility finding is not renderer-invariant.

### 16 ppem — normal autohint can amplify the difference

At 16 ppem:

- no-hint coverage difference: `-6.7%`;
- autohint-normal: `-12.1%`;
- autohint-light: `-6.0%`.

Normal auto-hinting does not always “repair” the lighter redraw. At this size it makes the R0/R1 rendered-area difference larger than the no-hint condition.

### 24 ppem — source-equal advances can become different hinted advances

Both R0 and R1 have the same `560` source-unit advance and the same unhinted linear advance.

At 24 ppem:

- no-hint advance: `13.4375 → 13.4375 px`;
- autohint-light: `13 → 13 px`;
- autohint-normal raw hinted advance: `14 → 13 px`.

Using FreeType's documented integer delta-correction procedure for repeated same-glyph text, the 24ppem normal-hint origins still progress at 14px for R0 and 13px for R1 in this experiment.

**Result:** renderer mode can turn an outline difference into a spacing/metric difference even when source advances are identical.

### 48 ppem — delta-aware positioning can neutralize a raw advance difference

At 48 ppem autohint-normal the raw hinted advances are `26 → 27 px`. However, applying FreeType's documented integer delta correction makes repeated glyph origins step at `27px` for both R0 and R1.

This is important because it prevents an overclaim from raw advance values alone.

**Result:** final spacing depends on the client positioning method as well as the hinted glyph metrics.

---

## 6. What T003 changes about T002

T002 concluded that R1 reduced the join mass but appeared fragile in a simple compact grayscale surrogate.

T003 **limits rather than rejects** that conclusion.

### Confirmed

- R1 is materially lighter than R0 in a real compiled font;
- the difference remains visible across sizes;
- large-size join relief is real rather than an SVG-only artifact.

### Limited

- compact fragility is not a fixed property of R1 alone;
- autohinting can suppress, amplify, or reshape the difference depending on ppem/mode;
- source-equal advances can become different hinted metrics;
- delta-aware positioning can sometimes normalize those differences and sometimes not.

### New conclusion

**The unit of approval is not “outline at size X.” It is outline + source metrics + hinting strategy + renderer + positioning behavior + actual product context.**

---

## 7. Design implications

### Do not choose R0 or R1 yet

R0 remains too dark at the join in larger views. R1 remains a plausible relief direction, but compact behavior depends strongly on renderer mode.

The next contour decision should compare at least one compromise R2 only after defining the relevant product renderer/minimum-size context.

### Do not infer `opsz` necessity from one glyph

T003 strengthens the reason to investigate size-specific design, but it also shows that a renderer can materially alter the same outline. An optical-size axis should be considered only if family-level problems remain after real target-renderer testing.

### Hinting policy is a product decision when compact rendering matters

For a product with dense operational text, a font pipeline should explicitly decide whether it relies on:

- manual/native hints;
- auto-hinting;
- mostly unhinted grayscale rendering;
- platform-specific rasterization behavior;
- a minimum size above the problematic range.

The answer can differ for web, iOS, Android, Windows, or embedded environments.

### Data/table alignment needs renderer proof

If tabular data relies on exact horizontal alignment, it is insufficient to inspect only `hmtx` source advances. Hinted advances and client positioning behavior must be tested in the actual stack.

---

## 8. Project Readiness Test

### When should this knowledge be applied?

Use it when a project:

- uses a custom font in compact UI/data roles;
- needs reliable column/identifier alignment;
- targets multiple rendering stacks;
- is considering a bespoke font, optical sizes, or hinting investment;
- observes that the same font appears materially different across platforms/sizes.

### When should it not be over-applied?

Do not create a renderer matrix for every ordinary system-font screen. The effort is justified when custom type, dense information, brand identity, ambiguity, or cross-platform consistency makes rendering quality consequential.

### Required project inputs

- actual target OS/browser/rendering stack;
- minimum and typical font-size roles;
- device class and density/DPR;
- languages/scripts and fallback behavior;
- whether numeric alignment is task-critical;
- expected platform hinting/antialiasing behavior;
- performance/font-format constraints;
- whether the product can choose alternate optical cuts or features reliably.

### Concrete decisions this can change

- minimum approved type size;
- whether a custom face is allowed in compact operational roles;
- whether to use one robust outline or optical variants;
- whether hinting/autohinting needs engineering attention;
- how to test tabular figure alignment;
- whether a platform/system font should handle small UI while the custom face handles identity/readout roles.

### Trade-offs

**One robust unhinted outline**
- simpler architecture and fewer renderer assumptions;
- may sacrifice precision at the smallest sizes.

**Hinting/autohint-dependent compact quality**
- can improve pixel regularity;
- may vary by engine/mode and influence metrics.

**Optical cuts / `opsz`**
- permits size-specific drawing;
- increases source/interpolation/application complexity and still requires renderer validation.

**System font for compact roles + custom identity face**
- reduces small-size engineering risk;
- reduces visual continuity and bespoke character in operational UI.

### Failure conditions

Rework or reject a typography recommendation when:

1. compact quality is approved from vector outlines only;
2. a renderer-specific success is described as universal;
3. hinted advance changes break a task-critical alignment contract;
4. auto-hinting is enabled without testing `lsb_delta`/`rsb_delta` positioning consequences;
5. optical-size complexity is added before a family-level need is demonstrated;
6. a custom font is forced into a compact role that a system font handles more reliably;
7. platform differences are discovered only after production implementation.

### Validation plan

Next evidence should expand from one engine into target stacks:

1. preserve this minimal font-source method;
2. add an R2 compromise contour rather than immediately choosing R0/R1;
3. extend the control set to `H O n o` repeated strings and then `0 1 I l`;
4. test FreeType modes again with proper delta-aware text positioning;
5. render the same font through at least one platform/browser stack;
6. compare compact/standard/spacious use contexts from Layout;
7. composite representative Color conditions;
8. only then decide minimum size, hinting expectations, or optical-size architecture.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: T002's compact-fragility conclusion is now bounded by real font-engine evidence; FreeType mode and ppem materially change R0/R1 differences.
- Canonical section: `5. Core results` and `6. What T003 changes about T002`.
- Confirmation / contradiction / transfer note: confirms the need for raster validation, limits any outline-only conclusion, and adds metric/positioning evidence.
- Scope limit: one minimal Latin control font, one font engine, no manual hints.

### Color
- Useful finding/context: T003 provides exact alpha coverage maps that can be composited under controlled light/dark/reduced-contrast conditions without changing geometry.
- Canonical section: `Renderer matrix` and evidence SVG.
- Confirmation / contradiction / transfer note: suitable transfer specimen for testing whether perceived weight changes alter the R0/R1 judgment.
- Scope limit: no perceptual/color conclusion is made here.

### Layout / Interaction
- Useful finding/context: compact density cannot assume that a source font's nominal advance or outline survives the renderer unchanged.
- Canonical section: 24ppem/48ppem metric findings and project-readiness inputs.
- Confirmation / contradiction / transfer note: strengthens L002's requirement to use actual typography in density experiments.
- Scope limit: Type does not decide which density strategy the product needs.

### Web Design
- Useful finding/context: a reproducible compiled research font and controlled R0/R1 renderer question now exist for browser transfer validation.
- Web application / validation consequence: Web can load a later generated font in real CSS and compare browser/font-loading/zoom/DPR behavior rather than reproducing the glyphs as SVG.
- Confirmation / contradiction / transfer note: T003 is a Type-side implementation-validation baseline waiting for browser evidence.
- Scope limit: no `W###` browser validation exists yet.

---

## Status implication

T003 closes one important Foundation gap: the Type program now has **reproducible compiled-font + real font-engine evidence**, not only SVG construction/raster surrogates.

It does **not** close Foundation because the evidence is still narrow:

- only one key glyph pair is being compared;
- no manual/native TrueType hint program is authored;
- no CoreText/DirectWrite/browser/device comparison exists;
- no full numeral/punctuation system exists;
- no multilingual/fallback family proof exists;
- no human reading/recognition validation exists.

**T002's R1 is neither accepted nor rejected.** Its behavior is renderer-dependent enough that the next design iteration should be based on the intended product rendering contract, not outline preference.

**Foundation gate remains CLOSED.**
