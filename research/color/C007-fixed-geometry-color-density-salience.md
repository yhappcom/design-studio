# C007 — Color-Driven Visual Density and Salience Under Fixed Geometry

Status: **PRACTICE + CROSS-DOMAIN TRANSFER VALIDATION / controlled Chromium fixed-geometry rendering and color-feature analysis complete; human task/perceived-clutter, cross-browser/device, CVD, and physical-environment validation pending**

## Why this study exists

Layout Study L002 established that density cannot be judged by rows-per-screen alone and explicitly handed Color a follow-up problem:

> hold geometry and content constant, then vary luminance/chroma/state treatment to separate color-driven visual load from geometry-driven density.

Color C002/C006 separately established that semantic roles should be separated from literal swatches and that accent/status/action/focus jobs should not be collapsed merely for visual consistency.

C007 combines those two evidence streams.

The question is deliberately bounded:

> If information, DOM structure, dimensions, typography, spacing, and interaction geometry are held constant, can color treatment materially change the rendered feature field and the distribution of salience cues?

This study does **not** claim that a computational image metric is equivalent to perceived clutter or task performance. It establishes a controlled rendered transfer specimen and identifies which color manipulations deserve human validation.

Reproducibility artifacts:

- `C007-fixed-geometry-color-density-specimen.html`
- `C007-fixed-geometry-color-density-playwright.py`
- `C007-fixed-geometry-color-density-results.json`

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T005; T003/T004 renderer evidence; T005 Latin/Korean mixed-script fallback evidence.
- Reusable finding: nominally identical text roles can change rendered mass, width, line box, and wrapping when font/fallback/rendering changes.
- Replication / challenge / transfer opportunity: C007 therefore fixes the font stack and language so Type is not a hidden variable. A later transfer should rerun the color conditions with T004/T005-compatible numeric/localized typography.
- Dependency / overlap: current result isolates Color under one system-font English condition. It is not Type validation.

### Color
- Evidence checked: Study 008, C001, C002, C003, C006.
- Reusable finding: luminance hierarchy precedes decorative hue hierarchy; color should have a job; color-only semantics are fragile; semantic-role separation can preserve sparse accent use without forcing a universal palette.
- Replication / challenge / transfer opportunity: C007 challenges the simplistic claim that “more color = more clutter” by adding a zero-chroma high-luminance-contrast control.
- Dependency / overlap: direct extension of C002/C006 and rendered transfer of the visual-density concern in Study 008/C003.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md` through L004/I004; L002 density validation; I003 forced-colors state resilience.
- Reusable finding: density comparisons must preserve content and geometry; visual state semantics should survive color-channel replacement; Layout distinguishes spatial density from color-driven visual load.
- Replication / challenge / transfer opportunity: this study derives a fixed geometry from the L002 intermediate-density portfolio specimen and changes only CSS color custom properties across variants.
- Dependency / overlap: Layout owns density policy and geometry. Color owns the color manipulation and rendered color-feature analysis.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web owns complete browser/page integration and cross-browser/device validation.
- Implementation / application validation opportunity: future W### work should reproduce the fixed-geometry variants with production tokens, actual browser zoom, project fonts, OS color settings, and multiple engines.
- Dependency / overlap: no substantive W### evidence exists at this checkpoint. C007 Chromium evidence does not replace Web canonical validation.

### Other / Cross-cutting / Future Specialist
- Evidence checked: Nothdurft 1993 saliency/feature-contrast experiments; Wolfe & Horowitz 2017 review of visual-search guidance; Rosenholtz et al. 2005/2007 visual-clutter/feature-congestion work; CIE S 017 perceptual-color definition.
- Reusable finding: color and luminance can guide attention; local feature contrast/variability can affect salience and clutter; perceived color depends on context/surround and observer state.
- Dependency / overlap: computational proxies require human task/perception validation before being treated as UX outcomes.

### Overlap decision
- Reuse / replication / extension / contradiction review / method comparison / transfer validation / project-specific study: **CROSS-DOMAIN TRANSFER VALIDATION + METHOD CHALLENGE + RENDERED PRACTICE**.
- Why: L002 already isolated geometry. C007 now isolates Color and explicitly tests whether chroma and luminance-contrast manipulations produce different rendered feature fields without changing layout.

---

# SOURCE — color and luminance can guide visual attention

Primary / peer-reviewed references:

- Nothdurft, H.-C. (1993), *Saliency effects across dimensions in visual search*, Vision Research 33(5–6), 839–844. DOI: `10.1016/0042-6989(93)90202-8`.
- Nothdurft, H.-C. (1993), *The role of features in preattentive vision: Comparison of orientation, motion and color cues*, Vision Research 33(14), 1937–1958. DOI: `10.1016/0042-6989(93)90020-W`.
- Wolfe, J. M. & Horowitz, T. S. (2017), *Five Factors that Guide Attention in Visual Search*, Nature Human Behaviour 1, 0058. DOI: `10.1038/s41562-017-0058`.

Nothdurft's experiments show that salience can be produced by local feature contrast in dimensions including color and luminance, and that salient presentations can materially change visual-search behavior. Wolfe & Horowitz treat color as an established guiding attribute and distinguish bottom-up salience from top-down task guidance.

### SYNTHESIS

Color is not merely decorative surface styling. It can change which elements compete for attention even when the spatial arrangement is unchanged.

### STUDIO JUDGMENT

A dense interface should not distribute high-salience color indiscriminately. The relevant question is not “how many colors are present?” but “where are strong feature differences placed relative to task priority?”

---

# SOURCE — clutter is not equivalent to item count

References:

- Rosenholtz, R., Li, Y., Mansfield, J., & Jin, Z. (2005), *Feature Congestion: A Measure of Display Clutter*, CHI 2005.
- Rosenholtz, R., Li, Y., & Nakano, L. (2007), *Measuring visual clutter*, Journal of Vision 7(2):17. DOI: `10.1167/7.2.17`.

The feature-congestion work operationalizes clutter as a performance-relevant property of representation/organization rather than simply a count of objects. The published work models local feature variability, including color and luminance-related information, and reports correspondence with human clutter judgments in studied displays.

### IMPORTANT METHOD BOUNDARY

C007 does **not** reimplement Rosenholtz Feature Congestion. It uses a much simpler study-specific local Oklab variability proxy solely to compare four otherwise identical screenshots.

Therefore:

- the proxy is not a validated clutter score;
- its absolute magnitude has no standalone UX meaning;
- only within-specimen comparison is used;
- human perceived-clutter/search evidence remains OPEN.

---

# SOURCE — color appearance is contextual

CIE S 017:2020 / e-ILV defines perceived color as dependent not only on spectral stimulus but also on stimulus size/shape/structure/surround, observer adaptation, and experience.

CIE e-ILV term: `colour, <perceptual>`.

### SYNTHESIS

Swatches evaluated in isolation do not establish how the same colors behave inside a dense repeated interface. C007 therefore evaluates color in a complete fixed UI field rather than comparing palette chips alone.

---

# CONTROLLED SPECIMEN

## Geometry basis

The specimen is derived from the L002 intermediate-density portfolio/table structure:

- 1024 px viewport width;
- fixed 24 px page padding;
- 10 px main gaps;
- 8 px row padding;
- 44 px minimum buttons;
- three summary cards;
- five-column table;
- twelve repeated data rows.

C007 adds fixed selected/status/action cues so semantic-emphasis behavior can be compared. It does **not** modify the Layout canonical L002 files.

## Invariants

Across all variants, the following are identical:

- DOM tree;
- text/content;
- font stack and font sizes;
- element dimensions;
- spacing/padding/gaps;
- border widths and radii;
- selected row identity;
- status labels;
- button labels and geometry;
- viewport and DPR.

Only CSS color custom-property values change.

The Playwright geometry snapshot confirms all tracked DOM rectangles are identical to the neutral baseline for all four variants.

## Variants

### A. `neutral`

Low-chroma control condition. Status, positive/negative data, selection, and primary emphasis are intentionally muted toward neutral values.

Purpose: establish a low-color-feature baseline, not a recommended product design.

### B. `overloaded`

Intentionally color-heavy condition:

- blue-tinted canvas/header/boundaries;
- alternating blue row surfaces;
- colored status pills;
- green/red signed values;
- selected mint row;
- saturated blue action.

Purpose: reproduce the common “every semantic difference receives color” failure pattern.

### C. `high-contrast-mono`

Zero-chroma diagnostic control:

- black/gray only;
- strong row striping;
- strong dark boundaries;
- high-contrast action and state surfaces.

Purpose: test whether high visual feature load can arise from luminance contrast even when chroma is removed.

### D. `semantic-sparse`

Revised role-oriented condition:

- neutral structural surfaces;
- strong color localized to primary action, selected marker, status cues, and signed data;
- no decorative row striping;
- unchanged semantic redundancy in labels/signs.

Purpose: preserve local task-relevant color signals while reducing distributed chroma variation.

---

# RENDERING ENVIRONMENT

- Chromium `144.0.7559.96`;
- Playwright Python;
- viewport `1024 × 900`;
- device scale factor `1`;
- full-page screenshot size `1024 × 1013`.

This is controlled Chromium evidence, not browser/device production PASS.

---

# ANALYSIS METHOD

Screenshots are downsampled 4× with area averaging to reduce glyph antialiasing micro-noise while retaining page regions.

Encoded sRGB pixels are converted to linear-light sRGB and then Oklab.

Measured quantities:

1. mean / standard deviation of Oklab `L`;
2. mean / standard deviation / 95th percentile of Oklab chroma `C = sqrt(a²+b²)`;
3. share of pixels above bounded chroma thresholds;
4. mean absolute adjacent-pixel difference in Oklab lightness;
5. mean absolute adjacent-pixel difference in Oklab chroma;
6. a 5×5 local standard-deviation combination over `L,a,b` as a **study-specific feature-variability proxy**;
7. region-average Oklab distance between the primary action and a normal button;
8. region-average Oklab distance between the selected row and its adjacent rows.

Region Oklab distances are not treated as validated perceptual-salience thresholds. They are controlled within-specimen comparison values.

---

# RESULTS

## 1. Geometry isolation succeeded

All four variants report:

`geometry_identical_to_neutral = true`

Tracked body/app/card/row/button/cell rectangles therefore remained unchanged while color varied.

### SYNTHESIS

Any screenshot-statistic difference in this specimen is not caused by changed row count, spacing, typography, wrapping, or target geometry.

---

## 2. Overloaded chroma increases distributed color-feature variation

| Metric | Overloaded | Semantic sparse | Relative change |
| --- | ---: | ---: | ---: |
| mean Oklab chroma | 0.01763 | 0.00403 | `4.37×` |
| pixels with C > 0.04 | 13.31% | 1.36% | `9.82×` |
| mean adjacent chroma difference | 0.003573 | 0.001674 | `2.13×` |
| mean adjacent lightness difference | 0.01794 | 0.01708 | `+5.0%` |
| local feature-variability proxy mean | 0.03249 | 0.02937 | `+10.6%` |

The lightness-adjacency measure remains fairly close while chroma measures rise substantially in the overloaded variant.

### SYNTHESIS

Within this controlled specimen, the overloaded condition introduces much more distributed chroma variation without materially changing geometry and with only a small change in mean adjacent lightness difference.

This is consistent with the hypothesis that color can increase the number/strength of competing visual features independently of information density.

### EVIDENCE LIMIT

This does **not** establish that users will rate the overloaded condition 10.6% more cluttered or perform 10.6% worse. The proxy magnitude is not a psychophysical scale.

---

## 3. Removing chroma does not necessarily reduce visual feature load

The `high-contrast-mono` condition has effectively zero chroma, yet compared with `semantic-sparse`:

- mean adjacent lightness difference: `0.02724` vs `0.01708` → about `+59.5%`;
- Oklab lightness standard deviation: `0.09899` vs `0.06544` → about `+51.3%`;
- local feature-variability proxy mean: `0.04802` vs `0.02937` → about `+63.5%`.

### CONTRADICTION REVIEW

A simplistic rule such as

> “less color means less visual density”

is rejected.

A zero-chroma interface can still create a highly segmented, attention-competing field through strong luminance alternation, borders, striping, and surfaces.

### STUDIO JUDGMENT

When reducing apparent clutter, inspect **luminance segmentation and boundary emphasis as well as chroma**. Desaturation alone is not a density strategy.

---

## 4. Sparse semantic color can keep a focal action strong without distributing chroma everywhere

Primary-vs-normal button region Oklab distance:

- overloaded: `0.4189`;
- semantic-sparse: `0.4285`.

At the same time, mean page chroma is `0.01763` for overloaded vs `0.00403` for semantic-sparse.

### SYNTHESIS

In this specimen, the sparse condition keeps the primary action at least as distinct from ordinary controls in this region-average Oklab comparison while using far less chroma across the whole page.

### STUDIO JUDGMENT

Accent scarcity is not equivalent to weak hierarchy. A strong local accent can coexist with a calm global field when the semantic job is explicit.

Again, the region-distance metric is only a within-study diagnostic; human action-finding time remains OPEN.

---

## 5. Neutral is not automatically better than semantic sparse

The neutral condition has lower chroma than semantic-sparse, but its mean local feature-variability proxy is slightly **higher** (`0.03002` vs `0.02937`).

### SYNTHESIS

Eliminating semantic color is not inherently the optimal way to reduce visual load. A disciplined sparse color system can maintain clear role differentiation without increasing the study-specific overall feature-variability proxy.

### STUDIO JUDGMENT

Do not optimize for minimum chroma. Optimize for **task-relevant distinction with minimum unnecessary competition**.

---

# FAILURE → REVISION

## Failure pattern — color every difference

The overloaded variant gives color to:

- global structure;
- alternating rows;
- boundaries;
- statuses;
- positive/negative values;
- selection;
- primary action.

Even with adequate individual contrast, the page accumulates many simultaneous color differences.

### REJECT

- using color merely because a token/state exists;
- adding alternating chromatic surfaces when row grouping is already structurally clear;
- using saturation to compensate for weak hierarchy everywhere;
- assuming every semantic distinction deserves equal visual salience.

## Revision — semantic sparse

The revised condition:

- returns structural surfaces to mostly neutral values;
- retains color for action, selected state, signed data, and status cues;
- keeps labels/signs as redundant meaning channels;
- leaves geometry unchanged.

### KEEP

- local high-salience signals for high-value tasks/states;
- semantic-role separation from C002/C006;
- neutral structure where color adds no decision value.

### REWORK NEXT

- test selected + focused + critical combinations;
- test CVD/grayscale/hue-removal resilience;
- load realistic T005 Korean fallback and T004 numeric cases;
- run human known-item search and comparison tasks before any claim about perceived clutter or performance.

---

# PROJECT READINESS TEST

## When should this knowledge be used?

Use it when a product:

- feels visually “busy” even though the layout cannot or should not remove information;
- uses many semantic colors/status chips/data colors;
- is a dense dashboard, table, monitoring, finance, operational, or admin surface;
- has a debate framed incorrectly as “reduce data vs keep data” when color hierarchy may be the real variable;
- needs to preserve strong focal actions while calming the rest of the field.

## When should it not be used as the main explanation?

Do not blame color first when:

- task-critical information is genuinely excessive;
- grouping or hierarchy is structurally unclear;
- typography/fallback causes wrapping/density failure;
- interaction states are semantically undefined;
- narrow containers or target geometry are the actual cause;
- a live project has not yet established which information must remain simultaneously visible.

## Required project inputs

Before recommending “reduce color density,” determine:

- primary user task and search target;
- what must remain simultaneously visible;
- semantic status/data roles;
- action/selection/focus priorities;
- current surface/boundary hierarchy;
- light/dark/environment conditions;
- actual typography and localization;
- CVD/accessibility requirements;
- target platform/browser/device.

## Concrete decisions this can change

- whether status chips need filled colored containers or only localized markers/text;
- whether alternating rows need color at all;
- whether borders should be visually strong or merely structural;
- where brand/accent color should be reserved;
- whether selection, action, status, and data colors are competing;
- whether a “simplification” can happen in Color before removing information.

## Trade-offs

- too little differentiation can slow target finding or flatten hierarchy;
- too much distributed contrast/chroma can create competing salience;
- high-contrast monochrome can be as visually aggressive as colorful UI;
- semantic sparsity must not erase status/data distinctions;
- forced-colors/user overrides can still remove authored color and require structural redundancy.

## Validation

For live products:

1. hold content and geometry fixed;
2. make at least two color hierarchies;
3. verify required contrast and non-color semantics;
4. compare rendered images, not swatches;
5. run human task tests for known-item search, comparison, action finding, and error detection;
6. separate objective performance from subjective preference/workload;
7. stress CVD, grayscale, forced colors, localization, text enlargement, and target devices;
8. only then attribute a UX difference to Color with confidence.

---

# OPEN

- Human perceived-clutter ratings for the four conditions.
- Known-item search and comparison time/error across matched variants.
- Eye-tracking or fixation evidence if future project risk justifies it.
- CVD simulation and actual observer testing.
- Light/dark matched transfer.
- Korean/T005 fallback and T004 numeral transfer.
- Actual browser zoom, cross-browser and physical-device evidence.
- Bright/low-light environmental validation.
- More faithful implementation of published visual-clutter models if automated Color QA later becomes project-useful.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: C007 isolates Color with fixed system typography; the next stronger proof should insert T004 numeric and T005 Korean/fallback conditions without changing Color semantics.
- Canonical section: controlled specimen + OPEN.
- Confirmation / contradiction / transfer note: confirms that Type must be held constant before attributing density changes to Color; future Type transfer may limit the present result.
- Scope limit: no Type/fallback/browser-font claim is made here.

### Color
- Useful finding/context: overloaded chroma raises distributed chroma variation; zero-chroma high-contrast treatment can raise luminance feature variability even more; sparse semantic color can retain strong focal-action separation.
- Canonical section: Results 2–5.
- Confirmation / contradiction / transfer note: confirms C002/C006 semantic sparsity as a useful method; contradicts any simplistic “desaturate to declutter” rule.
- Scope limit: computational rendered evidence, not human perceptual PASS.

### Layout / Interaction
- Useful finding/context: L002's claim that visual density is separable from information/spatial density is supported by a fixed-geometry Color transfer. Geometry remained identical while image feature statistics changed materially.
- Canonical section: Geometry isolation + Results 2–3.
- Confirmation / contradiction / transfer note: confirms the need to separate Color from Layout in density diagnosis. I003 remains relevant because a sparse color system still needs structural state redundancy.
- Scope limit: no human task-performance claim; Layout remains owner of density policy.

### Web Design
- Useful finding/context: four fixed-geometry color conditions and a reproducible Chromium harness are available for future production-page reproduction.
- Web application / validation consequence: implement with real tokens/components, CSS forced colors/system colors, project fonts, zoom, multiple browsers and actual device rendering.
- Confirmation / contradiction / transfer note: current evidence is a Color-owned controlled browser experiment; Web should return implementation failures/limitations rather than silently altering the Color method.
- Scope limit: single Chromium/Linux environment only.

---

# Evidence disposition

**KEEP**

- fixed-geometry isolation;
- semantic-sparse vs overloaded comparison;
- monochrome high-contrast control;
- rendering-level Oklab/statistical diagnostics;
- strict separation between computational proxy and human UX outcome.

**REWORK**

- add human tasks before making perceived-clutter or efficiency claims;
- expand Type/localization/CVD/forced-color/device conditions;
- consider a published feature-congestion implementation only if automated clutter diagnostics become a real project need.

**REJECT**

- `more colors = clutter` as a universal rule;
- `desaturate = calm` as a universal rule;
- using the local-feature proxy as a human-clutter score;
- changing layout/content at the same time as Color and then attributing the result to Color.

## Status implication

C007 provides rendered cross-domain evidence that Color can materially change a fixed interface's feature field without changing information or geometry. This improves project diagnosis of visually dense surfaces.

It does **not** pass Color Foundation. Human, CVD, cross-browser/device, environmental, and broader project-transfer evidence remain required.
