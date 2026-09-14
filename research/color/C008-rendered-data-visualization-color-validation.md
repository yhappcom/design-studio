# C008 — Rendered Data-Visualization Color Validation: Categorical, Sequential, Diverging, CVD, and State Integrity

Status: **PRACTICE + CRITIQUE / controlled light-dark Chromium rendering, CVD diagnostic, small-mark/state failure→revision, and semantic-scale checks complete; human interpretation, real CVD observers, forced-colors, cross-browser/device, localization, and production-chart validation pending**

## Why this study exists

C003 established the semantics of qualitative/categorical, sequential, and diverging color systems, but its strongest remaining gap was explicitly rendered practice.

C008 asks a project-facing question:

> When the same chart geometry is rendered in realistic light/dark conditions, which color-system failures become visible that a palette table or isolated swatch cannot expose?

The study deliberately includes three different data problems:

1. **categorical identity** — five line-series identities plus an interaction-selected series;
2. **sequential magnitude** — a low→high ordered heat strip under small-mark stress;
3. **diverging variance** — values around a meaningful zero plus missing data.

The goal is not to produce a universal MintTap chart palette. It is to turn C003 into a reusable validation method that can diagnose category identity, ordering, midpoint semantics, missing data, theme transfer, color-vision risk, and interaction-state collisions.

Reproducibility artifacts:

- `C008-rendered-data-visualization-specimen.html`
- `C008-rendered-data-visualization-playwright.py`
- `C008-rendered-data-visualization-results.json`

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T005, especially T004 numerals/punctuation and T005 Latin/Korean fallback.
- Reusable finding: chart labels, numeric readouts, direct labels, and legends can change practical readability and geometry through rasterization, fallback, and localization even when the color token is unchanged.
- Replication / challenge / transfer opportunity: C008 fixes typography to a system-font English control so that color is the main variable. A stronger later transfer should use T004/T005-compatible numeric and Korean labels.
- Dependency / overlap: Type owns label/numeral/fallback rendering. Color owns the data-color system and color-related acceptance criteria.

### Color
- Evidence checked: C003, C007, Studies 008/013/016/017, C001/C002/C006.
- Reusable finding: data semantics determine scale family; luminance/chroma hierarchy matters; theme resolution is separate from semantic role; color-only meaning is fragile; interaction color should not destroy data identity; wide-gamut authoring does not remove accessibility/gamut obligations.
- Replication / challenge / transfer opportunity: C008 renders C003's categorical/sequential/diverging claims and adversarially tests selection, small marks, theme transfer, CVD simulation, incorrect midpoint choice, and missing-data treatment.
- Dependency / overlap: direct rendered extension of C003.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md` through L005/I004, especially L004 dense numeric comparison and I003 forced-colors state resilience.
- Reusable finding: chart geometry and data identity should remain independent from interaction-state styling; semantic current/selected/focus states should survive color-channel loss; rendered density can change through Color without layout change.
- Replication / challenge / transfer opportunity: categorical failure intentionally replaces the selected series' identity color, while the revision retains identity and adds a separate halo/weight channel.
- Dependency / overlap: Interaction owns what selection means; Color owns how the series identity and selection overlay coexist.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web owns complete chart/page integration, responsive behavior, SVG/canvas/CSS rendering, forced colors, browser/device testing, and real design-token application.
- Implementation/application validation opportunity: reproduce these SVG conditions with production chart libraries, real page containers, system/user themes, forced colors, browser zoom, and target devices.
- Dependency / overlap: no substantive W### evidence exists at this checkpoint. C008 is controlled Color-owned Chromium evidence, not Web production PASS.

### Other / Cross-cutting / Future Specialist
- Evidence checked:
  - ColorBrewer scheme guidance / Harrower & Brewer;
  - Crameri, Shephard & Heron 2020;
  - Machado, Oliveira & Fernandes 2009 CVD model;
  - WCAG 2.2 Use of Color and Non-text Contrast.
- Reusable finding: scale type should follow data semantics; uneven/rainbow gradients can distort quantitative interpretation; CVD simulation can identify risk but is not equivalent to human CVD validation; meaningful chart information must not depend on color alone.
- Dependency / overlap: statistics, human perception, and accessibility remain cross-cutting.

### Overlap decision
- Reuse / replication / extension / contradiction review / method comparison / transfer validation / project-specific study: **RENDERED PRACTICE + ADVERSARIAL REVIEW + TRANSFER VALIDATION**.
- Why: C003 already contains the theory. C008 tests whether those rules survive a real SVG/browser specimen and records concrete failure→revision evidence instead of adding another abstract palette summary.

---

# SOURCE — scale family follows data semantics

Primary / authoritative references:

- ColorBrewer, scheme guidance: https://colorbrewer2.org/learnmore/schemes_full.html
- Harrower, M. & Brewer, C. A. (2003), *ColorBrewer.org: An Online Tool for Selecting Colour Schemes for Maps*, The Cartographic Journal 40(1), 27–37. DOI: `10.1179/000870403235002042`.

ColorBrewer distinguishes:

- qualitative schemes for nominal categories;
- sequential schemes for ordered low→high data;
- diverging schemes for values extending around a meaningful central reference.

Its diverging guidance explicitly treats the central break as a meaningful analytical value such as zero, mean, or median depending on the task.

### SYNTHESIS

A chart palette can be colorimetrically attractive and still be structurally wrong if its scale family implies a relationship the data do not contain.

---

# SOURCE — uneven quantitative color gradients can distort data reading

Reference:

- Crameri, F., Shephard, G. E. & Heron, P. J. (2020), *The misuse of colour in science communication*, Nature Communications 11, 5444. DOI: `10.1038/s41467-020-19160-7`.

Crameri et al. warn that uneven gradients and rainbow-like maps can exaggerate some data changes, suppress others, and exclude people with color-vision deficiencies.

### STUDIO JUDGMENT

For ordered product data, a useful diagnostic is not “does the palette contain many distinct colors?” It is:

- does visual order follow data order;
- are there internal reversals or accidental extrema;
- does the behavior survive the actual theme and mark size;
- do users have non-color ways to identify meaning where required?

---

# SOURCE — color must not be the only semantic channel

Primary source:

- WCAG 2.2, Understanding SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
- WCAG 2.2, Understanding SC 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG22/understanding/non-text-contrast.html

WCAG requires information conveyed by color differences to remain available through additional visual information. For meaningful graphical objects, non-text contrast obligations can also apply depending on whether the graphical information is required for understanding and whether equivalent text/alternative information is present.

### STUDIO JUDGMENT

A “CVD-friendly palette” alone is not a complete chart-accessibility strategy. Direct labels, symbols, line styles, sign, position, text, and alternate representations remain part of the design contract.

---

# SOURCE — CVD simulation is a model, not a human-observer substitute

Reference:

- Machado, G. M., Oliveira, M. M. & Fernandes, L. A. F. (2009), *A Physiologically-Based Model for Simulation of Color Vision Deficiency*, IEEE Transactions on Visualization and Computer Graphics 15(6), 1291–1298. DOI: `10.1109/TVCG.2009.113`.

The paper presents a physiologically based model spanning anomalous trichromacy and dichromacy and reports experimental validation with color-vision-deficient and normal-vision groups.

C008 uses severity-1 protan/deutan/tritan transformation matrices as a **diagnostic simulation**.

### IMPORTANT METHOD BOUNDARY

- simulated colors are not what every person with a given CVD type literally sees;
- Oklab distances after simulation are not validated category-identification thresholds;
- the result is useful for exposing fragile palettes, not for declaring human accessibility PASS.

---

# CONTROLLED SPECIMEN

## Browser environment

- Chromium `144.0.7559.96`;
- Playwright Python;
- viewport `1280 × 820`;
- device scale factor `1`;
- inline SVG charts;
- system-font English labels.

Four matched conditions are rendered:

- light / failure;
- light / revised;
- dark / failure;
- dark / revised.

Panel and chart rectangles remain identical across all four conditions.

---

# PRACTICE A — categorical series identity vs interaction state

## Failure

Five series use hue-only identity with:

- thin `1.5px` lines;
- no point markers;
- no direct end labels;
- legend lookup required;
- **selected Series C has its line color replaced by an interaction accent**.

Series C identity color:

`#2C7BB6`

Rendered selected stroke:

`#E69F00`

The interaction state therefore destroys the original categorical color identity and moves it close to another warm/orange category.

### REJECT

Do not implement selection by replacing a categorical series' identity color unless losing that identity is explicitly acceptable.

## Revision

The revised categorical system uses:

- five distinct identity colors;
- `2.5px` lines;
- five different dash/marker strategies;
- direct end labels A–E;
- legend retained as secondary support;
- selected Series C retains its identity color and receives a separate wider neutral/theme-aware halo.

Series C revised identity and rendered stroke are both:

`#009E73`

`identity_preserved_under_selection = true`

### SYNTHESIS

**Data identity and interaction emphasis are different semantic axes.**

Selection should normally add a channel — weight, halo, marker emphasis, direct label, de-emphasis of other series — rather than silently rewrite the data identity.

---

# CVD DIAGNOSTIC — categorical palette

The harness computes the minimum pairwise Oklab distance among the five categorical colors before and after Machado severity-1 simulations.

| Condition | Failure palette min | Revised palette min |
| --- | ---: | ---: |
| Normal model | `0.16961` | `0.15582` |
| Protanopia simulation | `0.04507` | `0.09554` |
| Deuteranopia simulation | `0.03302` | `0.07609` |
| Tritanopia simulation | `0.04056` | `0.08542` |

### CONTRADICTION / TRADE-OFF

The revised palette does **not** maximize the normal-model minimum Oklab distance; its normal minimum is slightly smaller than the failure palette's. Yet the worst pairwise separations under all three simulated CVD cases are substantially larger.

This is useful evidence against a one-metric palette-selection rule.

### STUDIO JUDGMENT

Do not optimize a categorical palette solely for one normal-observer distance score. Balance:

- CVD robustness;
- actual mark size;
- direct labeling;
- line/marker redundancy;
- hierarchy/salience;
- semantic collision with status/action colors;
- target theme/gamut/device.

The revised chart remains understandable even if its colors become less separable because series identity is also encoded through direct labels, dash/marker differences, and position.

---

# PRACTICE B — sequential magnitude and theme transfer

## Failure — equal-step HSV rainbow

Both light and dark failure modes use the same 9-step rainbow:

`blue → azure → cyan → spring-green → green → chartreuse → yellow → orange → red`

Rendered Oklab L values:

`0.4520 → 0.6152 → 0.9054 → 0.8751 → 0.8664 → 0.8907 → 0.9680 → 0.7319 → 0.6280`

There are **3 direction reversals** in the Oklab-L path.

### Failure implication

The visual lightness order does not track the numeric order consistently. A smooth data increase can therefore create false internal emphasis and reversals.

## Revised light theme

Light mode uses the 9-step ColorBrewer YlGnBu path already studied in C003.

Rendered Oklab L:

`0.9904 → 0.9542 → 0.8960 → 0.7926 → 0.7171 → 0.6179 → 0.4837 → 0.3795 → 0.2604`

- monotonic: `true`;
- direction reversals: `0`.

## Revised dark theme

Dark mode does **not** simply invert the light screenshot or reverse the hue semantics. It uses a separately authored low-yellow/olive → high-blue/cyan sequence with increasing lightness:

`#2B2A0F #3B4720 #3E6240 #3A7C67 #3B948E #4EADC0 #72C2E1 #A0D6F2 #D2ECFF`

Rendered Oklab L:

`0.2789 → 0.3770 → 0.4589 → 0.5367 → 0.6117 → 0.6981 → 0.7742 → 0.8483 → 0.9300`

- monotonic: `true`;
- direction reversals: `0`.

### SYNTHESIS

A semantic scale can preserve **low→high ordering and broad hue direction** while changing its luminance strategy for the surrounding appearance.

### STUDIO JUDGMENT

Dark-mode data color should be authored as a context-specific mapping, not generated through global inversion. The required invariants are the analytical meaning and ordered reading, not literal pixel identity across themes.

### Small-mark stress

The specimen also renders each sequential step as a `6×6px` mark. No claim of human discriminability is made from this render alone. It exists to prevent approval based only on large palette swatches.

---

# PRACTICE C — diverging midpoint and missing-data semantics

Data specimen:

`[-3, 0, +2, +5, +8, +12, N/A]`

The domain meaning is **variance around zero**.

## Failure — visual midpoint from observed numeric range

A naive implementation centers the color scale at the arithmetic midpoint of observed non-missing range:

`(-3 + 12) / 2 = +4.5`

This produces visual classes:

`negative, negative, negative, positive, positive, positive, missing`

Expected semantic classes are:

`negative, zero, positive, positive, positive, positive, missing`

Two semantic failures occur:

1. `0` is shown on the negative side instead of at the reference center;
2. `+2` is also shown with the negative-side hue family.

The failure mode also renders `N/A` using the midpoint color, making missing data look like a small/neutral valid value.

## Revision — zero is the semantic center

The revised scale:

- fixes the center at `0`;
- scales the negative and positive ranges independently because the numeric ranges are asymmetric;
- labels positive values with `+` and negative values with `−`;
- gives missing data a non-scale structural treatment (`N/A` + crossed outline) rather than a scale color;
- uses an explicit zero/reference line.

Result:

`semantic_mismatch_count = 0`

in both light and dark revised conditions.

### SYNTHESIS

A diverging midpoint is not a palette-layout convenience. It is part of the data model.

### STUDIO JUDGMENT

Do not derive the diverging center from `min/max` automatically when the domain has a known reference such as zero, target, baseline, threshold, or expected value.

Missing/null values must be outside the quantitative scale unless the domain explicitly defines them as a quantitative value.

---

# LIGHT / DARK RESULT

The revised architecture keeps the same data semantics across themes while allowing literal color mappings to differ.

What remains invariant:

- category identity;
- selected-vs-identity separation;
- sequential low→high order;
- diverging zero midpoint;
- positive/negative side semantics;
- missing-data semantics;
- labels and structural redundancy.

What changes:

- literal sequential luminance mapping;
- diverging surface colors;
- selection halo / text / grid values appropriate to the theme.

### STUDIO JUDGMENT

Theme equivalence should be specified as **semantic equivalence**, not screenshot-level RGB equivalence.

---

# FAILURE → REVISION SUMMARY

## REJECT

- categorical identity encoded only by hue when many series are important;
- changing a data-series color merely to show selection;
- using a rainbow low→high scale because its hues are visually distinct;
- choosing a diverging midpoint from the observed range when the domain reference is known;
- mapping missing values to the lightest/center scale color;
- treating dark mode as automatic color inversion;
- declaring a palette accessible from CVD simulation alone.

## KEEP

- data type → palette type before hue selection;
- direct labels/shape/dash/position as redundant categorical channels;
- interaction emphasis that preserves data identity;
- monotonic ordered progression for sequential reading;
- explicit semantic midpoint for diverging data;
- missing state outside the quantitative scale;
- theme-specific literal mapping with stable semantics.

## REWORK NEXT

- real CVD participant or stronger human task evidence;
- forced-colors/OS high-contrast behavior;
- chart-library/SVG/canvas production transfer;
- T004 numeric and T005 Korean/fallback labels;
- actual browser zoom and narrow responsive chart containers;
- physical-display glare/low-light validation;
- human small-mark discrimination/search/comparison tasks.

---

# PROJECT READINESS TEST

## When should this knowledge be used?

Use it whenever a product chart encodes:

- unordered categories;
- ordered magnitude;
- deviation from a reference;
- positive/negative values;
- missing/no-data states;
- series selection/highlight;
- theme variants.

## What must be known before choosing the palette?

- data type and scale;
- true analytical midpoint/reference, if any;
- expected category count;
- whether users compare, search, rank, or monitor;
- mark size and line thickness;
- label/direct-label feasibility;
- interaction states;
- missing/null semantics;
- light/dark/theme requirements;
- CVD/accessibility requirements;
- output medium, gamut, and device conditions.

## What concrete decisions can change?

- qualitative vs sequential vs diverging palette choice;
- whether direct labels replace or supplement a legend;
- whether selection changes color or adds another channel;
- whether a heatmap needs monotonic lightness;
- whether dark mode needs a separately authored scale;
- how zero/reference is represented;
- how missing values are encoded;
- when category count should trigger faceting/filtering instead of more hues.

## Failure modes

- false extrema from a non-monotonic quantitative map;
- positive values mapped into the negative side of a diverging scale;
- missing data interpreted as zero/low data;
- selected series losing identity;
- categories collapsing under CVD;
- legend matching becoming difficult at small marks/distant positions;
- dark theme changing analytical meaning;
- interaction/status colors colliding with data colors.

## Validation sequence

1. validate data semantics and scale family;
2. calculate/inspect palette order and gamut;
3. render at actual mark sizes;
4. inspect light/dark mappings;
5. simulate grayscale/CVD as diagnostics;
6. verify non-color redundancy;
7. test selection/focus/hover without destroying identity;
8. test missing/reference states;
9. run human interpretation/search/comparison tasks;
10. validate real browser/device/export behavior.

---

# OPEN

- Real human category-identification/search/error rates.
- Real CVD observers; simulation is not sufficient.
- Grayscale/print/photocopy production proof.
- Forced-colors/high-contrast behavior and alternate chart representation.
- Actual chart-library behavior in SVG/canvas.
- T004/T005 label and numeric transfer.
- Korean/other localization and long direct labels.
- Browser zoom/narrow container/responsive re-layout.
- Wide-gamut/device/export behavior.
- Physical-display and environmental viewing validation.
- Cyclic, uncertainty, bivariate, and multivariate color systems.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: chart identity now depends partly on direct end labels, numeric signs, and `N/A` labeling rather than color alone.
- Canonical section: categorical revision, diverging revision, small-mark stress.
- Confirmation / contradiction / transfer note: C008 strengthens the need to test T004/T005 typography in real chart roles because label failure can remove the redundancy that makes the color system robust.
- Scope limit: current proof uses system-font English only.

### Color
- Useful finding/context: rendered failure→revision evidence now exists for categorical identity/state separation, sequential monotonicity in light/dark, CVD diagnostic trade-offs, zero-centered divergence, and missing data.
- Canonical section: Practices A–C.
- Confirmation / contradiction / transfer note: confirms C003's scale-semantics framework; limits any one-metric palette optimization; adds a concrete dark-theme authoring method.
- Scope limit: no human/CVD/device PASS.

### Layout / Interaction
- Useful finding/context: categorical selection should normally preserve series identity and add a separate emphasis channel; category count/label distance can make a legend problem structural rather than purely chromatic.
- Canonical section: Practice A.
- Confirmation / contradiction / transfer note: consistent with I003's state-first/structural-redundancy model and L005/C007 separation of visual-feature load from geometry.
- Scope limit: Color does not define chart layout, navigation, brushing, tooltip, keyboard, or focus behavior.

### Web Design
- Useful finding/context: complete SVG specimen/harness is available for light/dark chart transfer and can be reproduced in a production chart library.
- Web application / validation consequence: test SVG/canvas, CSS/system themes, forced colors, browser zoom, responsive containers, real chart interaction, P3/sRGB/export, and OS/device differences.
- Confirmation / contradiction / transfer note: current Chromium evidence should be challenged by production Web implementation rather than silently treated as cross-browser proof.
- Scope limit: no W### production evidence yet.

---

# Evidence disposition

**KEEP**

- data semantics before palette family;
- selected-state overlay that preserves series identity;
- direct labels/marker/dash redundancy;
- light/dark semantic equivalence with separately authored mappings;
- monotonicity diagnostic for ordered scales;
- explicit zero/reference midpoint;
- missing data outside the numeric scale;
- CVD simulation as diagnostic only.

**REWORK**

- replace controlled system text with real Type roles;
- add human/CVD/forced-colors/production chart evidence;
- test larger category counts and responsive layout constraints.

**REJECT**

- rainbow as default low→high encoding;
- selected series color replacement as a default interaction strategy;
- automatic midpoint from observed min/max when domain reference is known;
- center/low scale color for `N/A`;
- dark-mode auto-inversion;
- CVD simulation or Oklab distance as accessibility PASS.

## Status implication

C003 advances from **IN STUDY / NUMERICAL PRACTICE** to **PRACTICE / CRITIQUE** because its three principal scale families now have controlled rendered failure→revision evidence across light/dark contexts plus bounded CVD/state diagnostics.

Color Foundation remains **NOT PASSED**.
