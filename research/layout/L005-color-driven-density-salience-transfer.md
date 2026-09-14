# L005 — Color-Driven Density and Salience With Geometry Held Constant

Status: **PRACTICE + CRITIQUE / COLOR→LAYOUT TRANSFER VALIDATION — controlled Chromium rendering and image-feature proxy evidence established; human perceived-complexity/search evidence remains OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Canonical path: `research/layout/`

Reproducible artifacts:

- `research/layout/L005-color-density-salience-playwright.py`
- `research/layout/L005-color-density-salience-results-summary.json`

## Question

When content, component count, position, spacing, target geometry, typography and viewport are held constant, can changes in color distribution materially change the rendered feature field enough that a surface may feel or behave differently even though **spatial density has not changed**?

A second question is deliberately separated:

> Can a color system be semantically ambiguous even when its rendered pixel variability is not especially high?

L005 transfer-tests Color C001/C002/C003/C006 against Layout L002/L004 without taking over Color's canonical ownership of palette, color science, contrast or semantic token architecture.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T005; L003/L004 transfer results.
- Reusable finding: apparent density and hierarchy can change through actual rendered glyph coverage/metrics even when color and nominal CSS size are unchanged.
- Replication / challenge / transfer opportunity: later repeat a bounded subset with actual production typography or T004/T005 conditions while holding Color fixed.
- Dependency or overlap: L005 holds typography constant; no Type conclusion is inferred from pixel-color metrics.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md` through C006;
  - `C001-web-color-user-override-resilience.md`;
  - `C002-semantic-color-role-token-architecture.md`;
  - `C003-data-visualization-color-systems.md`;
  - `C006-semantic-token-transfer-two-contexts.md`.
- Reusable finding:
  - visual hierarchy is not geometry alone;
  - semantic role and literal color must remain separate;
  - finance surfaces are especially vulnerable to collision among brand/action/selection/status/positive-negative roles;
  - Color's own queue identifies L002 fixed geometry as the next high-value density/salience transfer context.
- Replication / challenge / transfer opportunity:
  - independently hold Layout geometry constant and vary luminance/chroma/semantic distribution.
- Dependency or overlap:
  - Color owns whether a palette/value/role mapping is colorimetrically and semantically appropriate. Layout owns whether spatial diagnosis changes when the feature field changes without geometry changing.

### Layout / Interaction
- Evidence checked:
  - `L002-whitespace-density-spatial-rhythm.md` and its 216-condition validation;
  - L003/L004 rendered transfer evidence;
  - I003 color-channel-independent state semantics.
- Reusable finding:
  - spatial density, semantic grouping and interaction state should be diagnosed separately;
  - a dense-looking surface is not automatically a spacing problem;
  - state meaning must survive Color removal/replacement.
- Replication / challenge / transfer opportunity:
  - create matched geometry where only color distribution changes and quantify the rendered difference.
- Dependency or overlap:
  - primary ownership of the diagnostic separation remains Layout/Interaction.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web owns complete page/component/browser/device integration.
- Implementation/application validation opportunity:
  - reproduce the matched specimens with production design tokens, real page systems, dark/light themes, forced colors, target browsers/devices and project typography.
- Dependency or overlap:
  - no substantive W### study existed at L005 start; this is Layout-owned controlled browser transfer evidence, not Web PASS.

### Other / cross-cutting / future specialist
- Evidence checked:
  - Rosenholtz, Li & Nakano (2007), *Measuring visual clutter*, Journal of Vision 7(2):17, DOI `10.1167/7.2.17`;
  - Engmann et al. (2009), *Saliency on a natural scene background: effects of color and luminance contrast add linearly*, DOI `10.3758/APP.71.6.1337`;
  - Frey, Honey & König (2008/2009), category-dependent effects of color features on overt attention, PMID `19146307`;
  - Chu et al. (2026), *What Makes a Visualization Image Complex?*, IEEE TVCG 32(1), DOI `10.1109/TVCG.2025.3633827`.
- Reusable finding:
  - color variability can contribute to visual clutter measures;
  - color and luminance contrasts can influence salience/attention, but the effect is context-dependent;
  - recent visualization research finds both low-level and high-level image features contribute to perceived visual complexity.
- Dependency or overlap:
  - natural-scene/visualization findings do not provide universal UI thresholds. L005 therefore does not convert pixel statistics into claimed human search times or perceived-complexity scores.

### Overlap decision
- **INDEPENDENT VALIDATION + TRANSFER VALIDATION + METHOD SEPARATION**.
- Why:
  - C006 establishes semantic role architecture; L002 establishes spatial density. L005 tests the boundary: color can alter rendered feature competition while spatial geometry is unchanged, and semantic collision can exist even when feature variability is modest.

---

# SOURCE

## Visual clutter is not only item count or geometry

Rosenholtz, Li and Nakano (2007) tested image-based clutter measures and reported that Feature Congestion correlated with visual-search performance in complex imagery. Their additional experiment indicated that **color variability matters** for visual clutter in a way not represented by edge density alone.

This does not mean their metric can be copied as a universal product-design score. It does establish that a display can change perceptually when feature variability changes even if the object count does not.

## Color and luminance can both contribute to attentional salience

Engmann et al. (2009) manipulated luminance contrast and color-contrast/saturation gradients in natural scenes. Both biased fixation toward higher-contrast regions, and combined gradients were consistent with additive effects in that experimental setting.

Other work shows the influence of color on overt attention varies by image category, which is a useful limit: **do not universalize one salience recipe across all products or tasks**.

## Visualization complexity has both pixel-level and semantic/object-level contributors

Chu et al. (2026) collected perceived-complexity ratings for 1,800 visualization images from 349 participants and compared multiple metrics. Distinct colors, corners and context-dependent clutter measures contributed to perceived complexity. This reinforces a key L005 distinction: image statistics are useful evidence, but human complexity also depends on higher-level structure.

---

# CONTROLLED EXPERIMENT

## Geometry/content contract

The same 12-row finance comparison surface is rendered in all conditions.

Held constant:

- viewport `1280×900`;
- DOM tree and content;
- 12 rows;
- row/card/control dimensions;
- typography;
- target sizes;
- grid columns;
- padding/gaps;
- borders widths;
- selected row identity;
- numeric formatting.

Automated DOM rectangle comparison confirms:

**geometry_equal = true** across all five conditions.

Declared primary text/status/action pairs also remain at or above `4.5:1` in this bounded specimen so obvious low text contrast is not the intended manipulation.

## Five color conditions

### 1. `neutral_minimal`
Almost all state/value treatment is neutral. This minimizes chroma but also deliberately weakens semantic emphasis.

### 2. `role_separated`
Uses the C006 finance-style method: action, selection, focus, positive/negative and status jobs remain distinct while most surface area stays neutral.

### 3. `chroma_overloaded`
Spreads saturated/chromatic treatment across row backgrounds, boundaries, secondary text, actions, values, status chips and focus.

Geometry is unchanged.

### 4. `luminance_overloaded`
Uses no meaningful chroma but introduces stronger grayscale surface/boundary/status luminance variation.

This tests the false assumption that only “too many colors” can produce visual competition.

### 5. `semantic_collision`
Uses one teal family for primary action, selected/current treatment, positive data, success/review emphasis and focus.

This condition is intentionally important because it can be semantically weak without requiring the highest pixel-level variability.

---

# MEASUREMENT METHOD

Screenshots are converted from sRGB to OKLab and measured with deliberately simple image-feature proxies:

- mean/standard deviation of OKLab `L`;
- mean/standard deviation of OKLab chroma `C`;
- proportion of pixels above bounded chroma thresholds;
- mean adjacent-pixel gradient magnitude for `L`;
- mean adjacent-pixel gradient magnitude for `C`;
- number of unique declared token values;
- DOM rectangle equality;
- bounded relative-luminance contrast pairs.

## Critical scope limit

These are **L005 diagnostic proxies**, not a validated implementation of Rosenholtz Feature Congestion and not a human perceived-complexity model.

Do not call a variant “more cluttered to users” merely because one proxy is larger.

---

# RESULTS

## Geometry remained identical

All five variants returned identical measured DOM rectangles.

Therefore the changes below are not caused by spacing, wrapping, target size, row count or component repositioning.

## Chroma-spread comparison

`role_separated`:

- mean OKLab chroma ≈ `0.0109`;
- pixels with `C > 0.06` ≈ `4.03%`;
- mean chroma-gradient proxy ≈ `0.00163`.

`chroma_overloaded`:

- mean OKLab chroma ≈ `0.0182`;
- pixels with `C > 0.06` ≈ `7.01%`;
- mean chroma-gradient proxy ≈ `0.00446`.

With the same geometry, broad color distribution increased both chromatic coverage and local chromatic variation materially.

### SYNTHESIS

If a dense surface feels visually competitive after a palette change, **do not immediately reduce information or increase spacing**. First ask whether chromatic emphasis has been distributed too broadly.

## Luminance-spread comparison

`luminance_overloaded` produced:

- `L_std ≈ 0.1775`, the highest of the five conditions;
- mean luminance-gradient proxy ≈ `0.02109`, also the highest;
- effectively zero chroma.

### SYNTHESIS

A monochrome interface can still create strong feature competition through luminance/boundary variation.

“Use fewer colors” is therefore not sufficient density advice.

## Semantic-collision counterexample

`semantic_collision` did **not** have the largest mean chroma or luminance-variation proxy:

- `C_mean ≈ 0.0077`;
- `L_std ≈ 0.1214`.

Yet it intentionally assigns one hue family to several different jobs: action, selection/current, positive data, success/review emphasis and focus.

### SYNTHESIS

Pixel variability and semantic ambiguity are different dimensions.

A visually restrained palette can still have weak information architecture if one visual role means too many things.

Conversely, a role-separated palette can legitimately use several colors when those colors map to different domain/interaction jobs and remain bounded.

---

# STUDIO JUDGMENT — PROJECT DIAGNOSTIC MODEL

When a surface is described as “too dense,” “too busy,” or “everything is shouting,” diagnose at least four independent layers before changing spacing:

1. **Spatial density** — amount, spacing, grouping, alignment, whitespace and simultaneous content;
2. **Feature variability** — luminance/chroma/boundary/weight variation across otherwise identical geometry;
3. **Semantic emphasis distribution** — how many roles are visually promoted and whether promotion corresponds to task priority;
4. **Semantic collision** — whether one visual role is overloaded with incompatible meanings.

### Wrong diagnosis example

Problem: every row, status, metric and action uses high-emphasis color.

Weak response:

> Increase row padding from 8px to 16px.

This reduces spatial density but leaves the attentional/emphasis field unchanged and consumes more viewport.

Better sequence:

1. identify which content actually needs salience;
2. demote routine/default states;
3. preserve explicit semantic-role separation;
4. re-evaluate the same geometry;
5. only then adjust spacing if spatial density remains a problem.

### Opposite failure

Do not strip all color merely to reduce visual variability. If role/status/action distinctions become harder to find, the cure can be worse than the problem.

The objective is not minimum colorfulness. It is **task-aligned salience with restrained competition**.

---

# PROJECT READINESS TEST

## Apply this knowledge when

- a dashboard/table/list is described as visually busy despite acceptable spacing;
- brand/accent color is applied broadly;
- many semantic statuses compete in one viewport;
- dark/light redesign changes perceived hierarchy without geometry change;
- a team proposes solving “clutter” exclusively through whitespace;
- data color and interaction-state color compete;
- a redesign reduces item count but still feels visually noisy.

## Do not over-apply it when

- the actual problem is wrapping, target size, grouping or content overload;
- color is domain-critical data encoding and removing it destroys information;
- environmental/display conditions, contrast or CVD are the main unresolved problem;
- human task evidence contradicts the designer's visual impression.

## Project information required

- primary task: scan, compare, monitor, search, edit or decide;
- which states/events require immediate attention;
- which colors encode domain data versus interaction state;
- brand constraints;
- theme/environment requirements;
- accessibility/user override requirements;
- actual content frequency: rare alert vs common/default status;
- whether salience must persist across one row, a whole page or multiple panels.

## Validation plan

For a real project:

1. freeze geometry/content;
2. compare color-role alternatives;
3. verify contrast and non-color redundancy;
4. inspect feature distribution at intended size;
5. test known-item search / comparison / alert detection with representative users;
6. record preference separately from performance/error rate;
7. repeat under light/dark/forced-color and relevant display conditions;
8. only then change geometry if spatial density remains independently problematic.

---

# OPEN

- No participant-rated perceived density/complexity exists for these five specimens.
- No known-item search, comparison speed, alert-detection time or error rate was measured.
- The image proxies are not Rosenholtz Feature Congestion and have no universal acceptance thresholds.
- One light finance surface was tested; dark operational/context transfer is open.
- CVD, grayscale, physical-display and environmental illumination evidence remain open.
- Browser/device differences are open beyond this Chromium build.
- Actual C006 production token implementation is open.
- Interaction frequency matters: an always-present colorful status can create a different attention economy from a rare alert even with identical pixels at one moment.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: L005 holds typography constant and shows color distribution alone can materially change rendered feature variability; future Type raster transfer should therefore keep Color fixed when isolating font-driven density.
- Canonical section: Results / Project Diagnostic Model.
- Confirmation / contradiction / transfer note: **METHOD SEPARATION** — Type-driven and Color-driven apparent density should be isolated before assigning cause.
- Scope limit: no Type judgment or readability result is claimed.

### Color
- Useful finding/context: C006's role-separated finance method produces lower chroma-spread proxies than the deliberately chroma-overloaded condition while preserving explicit role distinctions; semantic-collision remains a separate problem not captured by pixel variability alone.
- Canonical section: Results / Semantic-collision counterexample.
- Confirmation / contradiction / transfer note: **CONFIRMATION + LAYOUT DIAGNOSTIC EXTENSION** — supports Color's semantic-role separation and provides fixed-geometry rendered transfer evidence. Does not establish a universal “less chroma is better” rule.
- Scope limit: Color remains canonical owner of palette/token/contrast/color-science conclusions.

### Layout / Interaction
- Useful finding/context: “density” complaints must be decomposed into spatial density, feature variability, semantic emphasis distribution and semantic collision.
- Canonical section: Studio Judgment — Project Diagnostic Model.
- Confirmation / contradiction / transfer note: **EXTENSION** of L002: geometry can be identical while the feature field changes materially.
- Scope limit: no human perceptual threshold or task-performance improvement is claimed.

### Web Design
- Useful finding/context: reproduce matched geometry with production CSS tokens and complete pages; test whether component/theme implementation adds visual competition through surfaces, borders, status chips and state colors.
- Web application / validation consequence: a page can become visually busy without any layout change, so browser/page critique should not treat all “density” feedback as spacing feedback.
- Confirmation / contradiction / transfer note: transfer using real design-system tokens, actual dark/light themes, target devices and human tasks.
- Scope limit: current evidence is one controlled Chromium specimen, not full-page Web validation.
