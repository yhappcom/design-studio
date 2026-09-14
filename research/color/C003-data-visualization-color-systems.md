# C003 — Data Visualization Color Systems: Categorical, Sequential, Diverging, and Semantic Integrity

Status: **SOURCE STUDY + NUMERICAL PRACTICE + PROJECT-READINESS SYNTHESIS / rendered, CVD, browser/device, and multi-project validation pending**

## Why this study exists

The Color program now covers color science, contrast, perceptual spaces, gamut, ramp authoring, semantic tokens, and web override behavior. A major project-readiness gap remains: **data visualization**.

Real MintTap products can contain financial, operational, trend, comparison, distribution, and status data. A professional Color Specialist must be able to answer not only “which colors look good?” but:

- what kind of data is being encoded;
- whether color is representing category, order, magnitude, sign, deviation, uncertainty, status, or interaction state;
- which palette family fits that semantics;
- which visual channel should carry the primary meaning;
- how the palette behaves under grayscale, color-vision deficiency, dark/light surfaces, small marks, printing, browser rendering, and device variation;
- when a color scale should not be used at all.

This study therefore asks:

> How should Design Studio choose, construct, audit, and reject color systems for categorical, sequential, and diverging data so that color supports truthful interpretation rather than decorating the chart?

This is a Color-owned study. Chart layout, interaction, labeling, navigation, and web implementation remain peer-domain responsibilities where applicable.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md`, `research/type/README.md`, and current T001–T003 status summaries.
- Reusable finding: numerals, labels, fallback, apparent weight, small-size rasterization, and line wrapping can change how chart values and legends are perceived and how much contrast is practically usable.
- Replication / challenge / transfer opportunity: chart labels, legends, axes, direct labels, and numeric columns should use real Type evidence rather than placeholder text.
- Dependency or overlap: Type owns typography and numeric rendering; Color owns color encoding and palette relationships.

### Color
- Evidence checked: Studies 008, 013, 016, 017, C001, and C002.
- Reusable finding: luminance hierarchy and semantic role are distinct from hue; perceptual authoring regularity is not accessibility proof; gamut mapping can compress distinctions; color-only meaning is fragile; literal values and semantic roles must remain separate.
- Replication / challenge / transfer opportunity: data palettes provide a stricter test of these principles because many colors must remain ordered or distinguishable simultaneously.
- Dependency or overlap: direct extension of canonical Color research.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md`, L002 density work, Study 015 state semantics, and I001 navigation/focus findings.
- Reusable finding: visual density is not element count alone; interaction state meaning must be defined before styling; current/focus/selected state should not collide with data-series color.
- Replication / challenge / transfer opportunity: dense charts can become visually noisy from chroma/contrast even when geometry is unchanged; hover/selection/highlight must not destroy the data scale.
- Dependency or overlap: Layout/Interaction owns spatial hierarchy and interaction semantics; Color owns the color scale and its resilience.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web will own complete browser/page integration, responsive chart containers, CSS/SVG/canvas behavior, forced colors, native/browser states, and actual device validation.
- Implementation/application validation opportunity: future W### work should test SVG/canvas/CSS chart colors, theme switching, forced colors, P3/sRGB, browser zoom, and direct-label/legend behavior.
- Dependency or overlap: Color defines palette semantics and failure criteria; Web validates real implementation.

### Other / cross-cutting / future specialist
- Evidence checked: ColorBrewer/Harrower–Brewer; Moreland; Crameri–Shephard–Heron; Okabe–Ito; WCAG 2.2 Use of Color and Non-text Contrast.
- Reusable finding: data type must determine palette type; rainbow-like quantitative maps can distort interpretation; redundant coding is required when color carries meaning; viewing environment and output medium matter.
- Dependency or overlap: accessibility, statistics, data visualization, and human perception are cross-cutting.

### Overlap decision
- Reuse / deliberate repetition / extension / contradiction review / method comparison / transfer validation / project-specific study: **EXTENSION + METHOD COMPARISON + PROJECT-READINESS SYNTHESIS**.
- Why: earlier Color studies provide the color-science tools; C003 applies them to the distinct semantic problem of data encoding.

---

## SOURCE — data semantics should determine the palette family

Primary / authoritative references:

- ColorBrewer scheme guidance: https://colorbrewer2.org/learnmore/schemes_full.html
- Harrower, M. & Brewer, C. A. (2003), *ColorBrewer.org: An Online Tool for Selecting Colour Schemes for Maps*, The Cartographic Journal 40(1), 27–37. DOI: 10.1179/000870403235002042

ColorBrewer distinguishes three major scheme families:

- **Sequential** — ordered data progressing from low to high, with lightness change as a dominant cue;
- **Diverging** — values extending in two directions around a meaningful critical midpoint, with contrasting hue families and a midpoint treatment;
- **Qualitative** — nominal/categorical classes where color should distinguish categories without implying magnitude order.

ColorBrewer also emphasizes end-use context such as display, print, projection, and photocopying.

### SYNTHESIS

The first palette decision is not hue. It is **scale semantics**.

A color scale is structurally wrong when it implies a data relationship that the data does not contain.

### STUDIO JUDGMENT

Before selecting colors, classify the encoded variable:

1. **Nominal / categorical** → qualitative palette;
2. **Ordered magnitude** → sequential palette;
3. **Deviation around a meaningful reference** → diverging palette;
4. **Periodic quantity** such as angle/time-of-day phase → cyclic palette, handled as a separate advanced case;
5. **Binary/status semantics** → semantic status system, not automatically a quantitative scale.

Do not select a diverging palette merely because two colors look balanced. The midpoint must have a real domain meaning.

---

## SOURCE — a diverging midpoint must correspond to a meaningful reference

ColorBrewer states that diverging schemes are most effective when the central break is meaningfully related to the data, citing values such as zero, mean, or median depending on the analytical task.

### SYNTHESIS

A midpoint is a semantic commitment.

Examples where zero can be meaningful:

- profit/loss relative to zero;
- variance from a target;
- change relative to baseline;
- temperature anomaly relative to a reference period.

Examples where a diverging midpoint may be misleading:

- yield values that are all non-negative and have no critical center;
- counts from 0 upward where “half of maximum” has no semantic meaning;
- arbitrary midpoint chosen only to create visual symmetry.

### STUDIO JUDGMENT

For finance products, **positive/negative sign does not automatically justify red/green**. The correct first question is whether the chart is truly about deviation around zero or another reference. If yes, use a diverging structure; hue choice is a later accessibility/brand decision.

---

## SOURCE — rainbow-like maps can introduce perceptual distortion

Primary / authoritative references:

- Moreland, K. (2009), *Diverging Color Maps for Scientific Visualization*, Sandia National Laboratories, SAND2009-4153C.
- Moreland, K. (2016), *Why we use bad color maps and what you can do about it*, DOI: 10.2352/ISSN.2470-1173.2016.16HVEI-133.
- Crameri, F., Shephard, G. E. & Heron, P. J. (2020), *The misuse of colour in science communication*, Nature Communications 11, 5444. DOI: 10.1038/s41467-020-19160-7.

Crameri et al. explicitly criticize uneven colour gradients, rainbow-like maps, and palettes that exclude people with color-vision deficiency. Their argument is not simply aesthetic: nonuniform visual gradients can exaggerate some data changes and suppress others.

Moreland similarly treats rainbow maps as a visualization problem rather than a stylistic preference and advocates color maps whose perceptual behavior better represents the data.

### SYNTHESIS

A continuous quantitative color map should not create strong visual boundaries where the underlying data have no comparable discontinuity.

### STUDIO JUDGMENT

Design Studio rejects “rainbow because it shows more colors” as a default quantitative strategy.

Rainbow/cyclic hue paths may still be legitimate when **cyclic semantics** are the actual data structure, but a cyclic scale must be designed as such. It should not be used for ordinary low→high magnitude.

---

## NUMERICAL PRACTICE — monotonic luminance check

This exercise is a diagnostic, not a claim that WCAG relative luminance is a perceptually uniform data-visualization metric.

### Case A — ColorBrewer YlGnBu 9-class sequential scale

Official ColorBrewer values:

`#ffffd9 #edf8b1 #c7e9b4 #7fcdbb #41b6c4 #1d91c0 #225ea8 #253494 #081d58`

Computed sRGB relative luminance values:

| Step | HEX | Relative luminance |
| --- | --- | ---: |
| 1 | `#ffffd9` | 0.9779 |
| 2 | `#edf8b1` | 0.8831 |
| 3 | `#c7e9b4` | 0.7372 |
| 4 | `#7fcdbb` | 0.5176 |
| 5 | `#41b6c4` | 0.3857 |
| 6 | `#1d91c0` | 0.2432 |
| 7 | `#225ea8` | 0.1117 |
| 8 | `#253494` | 0.0499 |
| 9 | `#081d58` | 0.0163 |

The sequence is monotonic from light to dark.

### Case B — synthetic equal-hue HSV rainbow

For a deliberately simple comparison, nine fully saturated/value HSV colors were generated at equal hue steps from 240°→0°:

`blue → azure → cyan → spring green → green → chartreuse → yellow → orange → red`

Computed relative luminance:

`0.0722 → 0.2266 → 0.7874 → 0.7308 → 0.7152 → 0.7611 → 0.9278 → 0.3670 → 0.2126`

The luminance path repeatedly reverses direction.

### SYNTHESIS

Equal hue increments do not imply ordered visual magnitude. A rainbow path can produce strong local lightness changes and reversals unrelated to the underlying numeric order.

### STUDIO JUDGMENT

For ordered product data, require at least:

- monotonic order in the chosen perceptual/lightness design dimension where the task depends on ordered reading;
- no accidental internal extrema that create false emphasis;
- rendered inspection at actual mark size;
- accessibility and color-vision checks;
- target-gamut validation.

Do **not** interpret the luminance calculation above as proof that YlGnBu is universally optimal. It is one controlled example showing why scale geometry matters.

---

## SOURCE — color must not be the only information channel

Primary / authoritative references:

- WCAG 2.2, SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
- WCAG Technique G111, Using color and pattern: https://www.w3.org/WAI/WCAG22/Techniques/general/G111.html
- Okabe, M. & Ito, K., *Color Universal Design — How to make figures and presentations that are friendly to Colorblind people*: https://jfly.uni-koeln.de/color/

WCAG requires that color not be the only visual means of conveying information. Okabe–Ito similarly recommend redundant coding with combinations such as shape, position, line type, pattern, and direct labeling, and specifically note the difficulty of matching colors across distant chart elements and separate legends.

### SYNTHESIS

A “colorblind-friendly palette” is not a substitute for redundant information architecture.

Even a carefully chosen categorical palette can fail because:

- marks are too small;
- lines are too thin;
- categories are spatially separated from the legend;
- several series are similar in lightness/chroma;
- hover/selection overlays alter the palette;
- the display or print condition compresses differences;
- users must remember color names rather than identify objects directly.

### STUDIO JUDGMENT

For critical categorical data, prefer this hierarchy:

1. direct labels where practical;
2. position/shape/line style/grouping as additional encodings;
3. color as a fast reinforcing channel;
4. a separate legend only when direct identification would create more clutter than it removes.

Do not claim “accessible because Okabe–Ito/ColorBrewer was used.” The actual chart must still be validated.

---

## Categorical / qualitative palette model

### Use when

- categories are unordered;
- identity matters more than magnitude;
- examples: portfolio tickers, aircraft types, account groups, strategy categories.

### Design objective

Maximize category discrimination without creating an accidental rank hierarchy.

### STUDIO JUDGMENT

Categorical systems should evaluate:

- pairwise distinguishability in the actual display context;
- color-vision diversity;
- similarity of mark size and area;
- legend/direct-label distance;
- whether one category receives disproportionate salience;
- collision with semantic status colors such as error/success;
- collision with interaction colors such as selected/focus/hover;
- dark/light theme behavior.

If the category count exceeds what remains reliably distinguishable, change the visualization structure rather than endlessly adding hues. Group, filter, facet, label, or split the view.

---

## Sequential palette model

### Use when

- data have a meaningful low→high order;
- magnitude or intensity is the primary reading task;
- examples: cumulative distribution amount, utilization, counts, exposure, age, duration.

### Design objective

The visual ordering should track the data ordering.

### STUDIO JUDGMENT

A sequential scale should normally maintain a monotonic perceptual progression, often dominated by lightness with controlled chroma/hue changes.

Check:

- monotonic lightness/order;
- sufficient separation at the expected mark size;
- no gamut-induced bunching at one end;
- legibility of overlaid labels;
- dark-theme reversal or remapping rather than naive inversion;
- whether zero/missing values are distinguishable from valid low values.

---

## Diverging palette model

### Use when

- the data vary in two meaningful directions around a reference;
- examples: gain/loss around zero, deviation from target, actual-vs-plan variance.

### Design objective

Both sides of the midpoint must remain ordered, and the center must communicate the reference rather than merely “a pale color.”

### STUDIO JUDGMENT

A diverging scale must define:

- midpoint semantic meaning;
- whether both sides have equal or unequal numeric ranges;
- whether visual emphasis should be symmetric or intentionally asymmetric;
- how zero/reference and missing/no-data differ;
- whether positive/negative also receive symbols/signs/text;
- whether one side collides with existing semantic colors.

Do not force symmetric color steps when the analytical domain is asymmetric. Visual symmetry is not a reason to distort the data model.

---

## Missing, zero, neutral, and unavailable are different states

### STUDIO JUDGMENT

Data color systems must distinguish at least where relevant:

- numeric zero;
- meaningful midpoint/reference;
- missing/null;
- not applicable;
- not yet loaded/pending;
- suppressed/redacted;
- outlier/overflow beyond displayed scale.

A common failure is to render missing values with the palest sequential color, making “no data” look like “very low data.”

Use a separate visual/semantic treatment and label where ambiguity would matter.

---

## Finance-specific transfer examples

These are examples of applying the method, not universal MintTap color rules.

### Portfolio return / P&L around zero

Possible structure: diverging.

Required checks:

- zero is actually the decision-relevant midpoint;
- sign is also encoded numerically (`+` / `−`) or through position/direction;
- red/green alone is not used as the only distinction;
- the brand accent is not confused with “positive” or “selected.”

### Distribution yield / recovery rate from low to high

Possible structure: sequential.

A diverging palette is unjustified unless a real threshold or target changes the interpretation.

### ETF/ticker comparison

Possible structure: qualitative.

If many tickers are shown simultaneously, direct labeling/faceting/filtering may be more reliable than assigning an ever-growing palette.

### Actual vs target

Possible structure: diverging around target deviation, not necessarily around numeric zero.

The data transformation should make the comparison semantics explicit before color is assigned.

---

## Interaction-state collision

A chart often needs both data color and interaction state.

Examples:

- hover;
- selected series;
- keyboard focus;
- filtered/de-emphasized;
- hidden/muted;
- error/invalid data;
- live/pending update.

### STUDIO JUDGMENT

Do not solve selection by replacing the selected series with a semantically unrelated highlight color if doing so destroys the data identity.

Prefer interaction strategies such as:

- stroke/outline emphasis;
- mark size or line-weight change;
- opacity reduction of nonselected items, with caution about contrast/background effects;
- direct label emphasis;
- halo/outline that remains visible under accessibility modes;
- positional callout.

Interaction owns what “selected” means; Color ensures the visual encoding does not corrupt the data scale.

---

## Light/dark and environment transfer

A palette that works on a light canvas is not automatically valid on a dark surface.

Dark-mode transfer can alter:

- apparent lightness spacing;
- local contrast;
- salience of highly saturated colors;
- thin-line visibility;
- label/readout contrast;
- background interaction with transparency.

### STUDIO JUDGMENT

For charts, treat light and dark schemes as **related mappings of one data semantics**, not as RGB inversions.

Validate the ordering and category identity in both contexts.

---

## Project-readiness decision framework

Before recommending a data palette, gather:

1. variable type: nominal / ordinal / quantitative / signed deviation / cyclic;
2. number of categories or scale steps;
3. meaningful zero, baseline, target, or threshold;
4. expected chart/mark type and minimum mark size;
5. whether direct labels are feasible;
6. light/dark/theme requirements;
7. interaction states;
8. output media: phone, tablet, desktop, print, screenshot/export;
9. color-vision/accessibility requirements;
10. brand/status colors already reserved elsewhere;
11. target gamut and browser/platform constraints;
12. whether exact cross-chart color identity must persist over time.

### Alternatives to compare

- color scale vs direct labeling / grouping / faceting;
- single-hue vs multi-hue sequential;
- symmetric vs asymmetric diverging mapping;
- qualitative palette vs small multiples;
- literal legend vs direct labels;
- authored chromatic scale vs neutral + one highlight when only one comparison matters.

---

## Failure modes

1. **Data-type mismatch** — qualitative colors used for magnitude or sequential ramp used for nominal identity.
2. **False midpoint** — diverging center chosen for visual symmetry rather than domain meaning.
3. **Rainbow distortion** — uneven visual gradients create false boundaries or suppress variation.
4. **Red/green dependence** — gain/loss or pass/fail is unreadable for some users without redundant cues.
5. **Missing-as-zero** — no-data value visually collapses into a valid endpoint.
6. **Legend memory load** — many separated series require constant distant color matching.
7. **Category explosion** — too many hues are added instead of changing the chart structure.
8. **Semantic collision** — chart series uses the same accent that elsewhere means success, error, selection, or brand action.
9. **Theme inversion** — light palette is mechanically inverted for dark mode and loses ordering/identity.
10. **Gamut collapse** — wide-gamut authoring maps several distinct colors into nearly identical sRGB output.
11. **Interaction corruption** — hover/selection changes the data color so much that identity or magnitude semantics are lost.
12. **Small-mark failure** — palette tested as large swatches fails on 1–2 px lines or tiny points.

---

## Validation protocol

For a production data-color system, validate at least:

1. **semantic classification** — palette family matches the variable type;
2. **numeric/color-space audit** — ordered scales have intentional lightness/chroma behavior and are inside target gamut after mapping;
3. **grayscale test** — ordered hierarchy and redundant information remain interpretable where appropriate;
4. **CVD simulation + human review** — simulation is diagnostic, not sole proof;
5. **direct-label / legend test** — measure whether distant color matching is avoidable;
6. **small-mark test** — actual minimum line/point/bar size;
7. **light/dark surface test**;
8. **interaction-state test** — focus/selected/hover/filter without data-semantic corruption;
9. **missing/zero/reference test**;
10. **device/browser/export/print test** where relevant;
11. **real task test** — identification, ordering, comparison, anomaly detection, not only palette preference.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: data color cannot compensate for weak direct labels, poor numeral alignment, small/light text, or fallback-induced wrapping.
- Canonical section: `SOURCE — color must not be the only information channel`, categorical model, validation protocol.
- Confirmation / contradiction / transfer note: reinforces T001/T003 need for real rendered chart labels and numeric roles.
- Scope limit: C003 does not define font, numeral, or label-placement rules.

### Color
- Useful finding/context: palette family must derive from data semantics; ordered scales need controlled perceptual progression; categorical scales require system-level discrimination; missing/reference/status roles must not collapse.
- Canonical section: entire C003.
- Confirmation / contradiction / transfer note: extends Studies 013/016/017 and C002 into data encoding.
- Scope limit: rendered/CVD/device/human-task validation remains open.

### Layout / Interaction
- Useful finding/context: direct labeling/faceting can be more reliable than adding color categories; data color and interaction state need independent semantics; L002 density can be color-driven as well as spatial.
- Canonical section: categorical model, interaction-state collision, failure modes.
- Confirmation / contradiction / transfer note: confirms that state semantics precede color styling and adds chart-specific transfer conditions.
- Scope limit: C003 does not define chart layout, navigation, interaction flow, or focus order.

### Web Design
- Useful finding/context: C003 defines browser validation targets for SVG/canvas/CSS chart palettes, light/dark mapping, forced colors, P3→sRGB behavior, small marks, direct labels, and interaction states.
- Web application / validation consequence: future W### chart/dashboard studies should return confirmation, limitation, contradiction, or transfer failure to Color.
- Confirmation / contradiction / transfer note: new outgoing Color→Web contract.
- Scope limit: actual browser implementation evidence is not claimed here.

---

## OPEN

- Controlled CVD simulation and human-observation comparison of representative categorical palettes remains to be executed.
- A dedicated cyclic-colormap study is still needed before formal cyclic guidance is written.
- Multi-series category-count limits should not be universalized without mark/task/context evidence.
- Sequential and diverging palettes need rendered practice in both light and dark UI surfaces.
- Wide-gamut → sRGB mapping must be tested on multi-color chart sets, not just individual colors.
- Data visualization under forced colors requires a dedicated browser implementation test and alternate representation policy.
- Uncertainty visualization, bivariate color maps, heatmaps, choropleths, and high-dimensional encodings require separate advanced studies.
- Color semantics across cultures/locales require evidence before assigning universal “good/bad” hue meanings.

## Status implication

C003 closes the **conceptual data-visualization palette-family gap** and adds a numerical ordered-scale practice, but it does not move the Color program to PASS.

Professional readiness now requires rendered, CVD, browser/device, dark/light, real-task, and multi-project transfer evidence. The scientific Foundation gaps in official CIE spectral integration and ICC/CMM validation also remain open.