# L002 Validation Report — Density, Reflow, and Adaptive Whitespace

Status: **PRACTICE + CRITIQUE / controlled Chromium rendering and failure → revision → re-proof complete; human task-performance validation still OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Canonical research being validated: `research/layout/L002-whitespace-density-spatial-rhythm.md`

Reproducible artifacts:

- `research/layout/L002-density-validation-specimen.html`
- `research/layout/L002-density-validation-playwright.py`
- `research/layout/L002-density-validation-results-summary.json`

## Objective

Turn L002 from a source-grounded density framework into rendered evidence that can answer a project question:

> When should a product use compact, intermediate, or spacious density, and which parts of density may adapt under narrow viewports, long localization, and enlarged text without sacrificing meaning or interaction geometry?

This block intentionally does **not** claim human search-time or preference results. It measures only browser-rendered geometry and information-preservation consequences that can be observed directly.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `progress/TYPE_STATUS.md` through T004;
  - `research/type/T004-native-numeral-punctuation-renderer-proof.md`;
  - prior T001/T003 handoffs summarized in Type status.
- Reusable finding:
  - source metrics do not alone guarantee final rendered alignment;
  - compact typography must be evaluated under actual renderer/size conditions;
  - fixed tabular source advances can still show renderer-dependent hinted advances.
- Replication / challenge / transfer opportunity:
  - the L002 specimen uses real browser text rather than placeholder rectangles, but it uses the system-font stack rather than the T004 research font. A later Type→Layout transfer should load T004/T005 specimens and test actual numeric alignment, fallback, Korean/Latin metrics, and wrapping.
- Dependency / overlap:
  - Layout chooses spatial density according to the task; Type owns font construction, fallback, metrics, and rendering behavior.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md` through C003;
  - `research/color/C003-data-visualization-color-systems.md`;
  - prior C001/C002 handoffs summarized in Color status.
- Reusable finding:
  - visual density can change through contrast/chroma/feature variability even when geometry is unchanged;
  - data identity and interaction state must remain semantically separate.
- Replication / challenge / transfer opportunity:
  - this validation deliberately holds color treatment nearly constant to isolate spatial density. A later controlled transfer should hold geometry constant and vary Color-defined luminance/chroma/state treatment.
- Dependency / overlap:
  - no conclusion here says that geometry alone explains perceived clutter.

### Layout / Interaction
- Evidence checked:
  - `research/layout/006-grid-composition-hierarchy.md`;
  - `research/layout/014-perceptual-grouping-spatial-grammar.md`;
  - `research/layout/L001-figure-ground-balance-optical-centering.md`;
  - `research/layout/L002-whitespace-density-spatial-rhythm.md`;
  - current `progress/LAYOUT_STATUS.md` including I001 running validation.
- Reusable finding:
  - spacing is relational and must preserve semantic grouping;
  - responsive systems preserve relationships rather than coordinates;
  - target geometry and temporal/navigation cost must not be collapsed into a single visual-density number.
- Replication / challenge / transfer opportunity:
  - the current specimen directly tests whether density changes preserve content, target geometry, and reflow across matched content.
- Dependency / overlap:
  - this block is spatial evidence. Human search, comparison, and motor performance remain separate empirical gates.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md` through the currently approved but not-yet-published W001 state.
- Reusable finding:
  - Web Design owns complete real-page/browser/device integration and should later reproduce this matrix inside a real page system.
- Implementation/application validation opportunity:
  - real CSS component system, actual fonts, browser zoom, real router, forced colors, native controls, framework behavior, and multiple browser/device engines.
- Dependency / overlap:
  - this is Layout-owned controlled browser evidence, not Web canonical PASS evidence.

### Other / cross-cutting / future specialist
- Evidence checked:
  - the perceptual/search literature already synthesized in L002;
  - existing shared accessibility/reflow/target evidence referenced by the Layout status.
- Reusable finding:
  - enlarged text and narrow width are structural stress conditions, not edge-case screenshots.
- Dependency / overlap:
  - human performance and preference cannot be inferred from geometry alone.

### Overlap decision
- **PRACTICE + INDEPENDENT VALIDATION + FAILURE ANALYSIS + TRANSFER PREPARATION**.
- Why:
  - L002 already established the conceptual model. The missing evidence was whether materially different density strategies survive actual browser rendering and stress without confusing “more visible rows” with “better design.”

---

# 1. Controlled specimen

The specimen uses the same 12-row portfolio dataset in every condition and varies only the density policy, spacing profile, viewport, text scale, and localization string set.

## Content structure

Each surface includes:

- toolbar controls;
- three summary values;
- 12 repeated rows;
- name;
- status;
- value;
- change;
- row action.

The long Korean dataset intentionally creates longer real text instead of placeholder rectangles.

## Viewports

- `1440 × 900` — wide desktop;
- `1024 × 768` — desktop;
- `768 × 800` — tablet-like width;
- `390 × 844` — narrow mobile-like width.

## Text scales

- `1.0×`;
- `1.25×`;
- `2.0×`.

## Locales

- English;
- long Korean labels.

## Density profiles

- compact;
- intermediate;
- spacious.

This produces 72 conditions per policy.

---

# 2. Three policy cycles

## Cycle 0 — `naive`

The deliberately weak implementation equated compactness with:

- smaller controls (`32px` compact, `40px` intermediate);
- single-line truncation/ellipsis;
- hiding Value and Change on narrow screens;
- preserving a visually short row even when information no longer fit.

This is not intended as a recommendation. It is the failure baseline.

## Cycle 1 — `preserve`

The first revision separates density from semantic loss:

- minimum control geometry is kept at `44px` in the specimen contract;
- critical text is allowed to wrap;
- narrow rows recompose rather than hide Value/Change;
- compact/intermediate/spacious differ primarily through padding and gap relationships;
- no content is intentionally clipped to win viewport density.

The `44px` value here is a **controlled specimen contract**, not a universal Design Studio law.

## Cycle 2 — `adaptive`

Cycle 1 exposed a second problem: preserving the desktop spaciousness ratio under narrow width + 200% text created excessive vertical expansion.

Cycle 2 therefore preserves:

- information;
- grouping;
- control geometry;
- text enlargement;
- narrow-screen recomposition;

while reducing only comfort/decorative spacing for intermediate/spacious modes under the most constrained condition.

This tests an important L002 hypothesis:

> A density profile is not a fixed pixel identity. Its semantic relationships may survive while absolute whitespace adapts to available space and text demand.

---

# 3. Metrics

The Playwright harness records:

- total scroll height / viewport height (`scrollRatio`);
- maximum number of complete data rows that can theoretically fit in one viewport (`maxRowsPerViewport`);
- average/min/max rendered row height;
- clipped critical cells;
- hidden critical cells;
- horizontal overflow;
- minimum rendered button height;
- wrapped cell count;
- table height.

### Scope limit

`maxRowsPerViewport` is a geometric simultaneity metric. It is **not** a human search-time metric.

Likewise, a lower `scrollRatio` is not automatically better if it was achieved by hiding or clipping content.

---

# 4. Cycle 0 failure results

Across 72 naive conditions:

- `32` conditions rendered a control below the specimen's 44px interaction-geometry contract;
- `580` critical cell instances were clipped/ellipsized;
- `432` critical cell instances were hidden by the narrow-screen policy;
- average scroll ratio was only about `1.47`;
- average maximum visible-row capacity was about `10.7`.

### SYNTHESIS

The naive implementation appears “efficient” if the metric is only rows-per-screen or scroll length.

That conclusion is false because the implementation changed the task-relevant information and target geometry to obtain the result.

### STUDIO JUDGMENT

**Do not compare density variants until semantic content and required interaction geometry are held constant.**

A compact design does not earn credit for fitting more rows if it silently removes columns, truncates identifiers, or shrinks critical targets below the product's interaction contract.

---

# 5. Cycle 1 preservation result

Across all 72 `preserve` conditions:

- controls below the 44px specimen contract: `0`;
- horizontal overflow: `0`;
- clipped critical cells: `0`;
- hidden critical cells: `0`.

The cost was real:

- average scroll ratio increased to about `2.09`;
- average maximum visible-row capacity decreased to about `8.6`.

### SYNTHESIS

Preserving information and interaction geometry exposes the true spatial cost that the naive layout had been hiding.

This is a more honest basis for comparing density strategies.

---

# 6. The extreme stress case exposes a fixed-whitespace failure

Condition:

- viewport `390 × 844`;
- text scale `2.0×`;
- long Korean labels.

Under `preserve`:

| Density | Scroll ratio | Max rows / viewport | Average row height | Critical content lost |
| --- | ---: | ---: | ---: | ---: |
| compact | 5.17 | 2 | 321.9px | 0 |
| intermediate | 6.31 | 2 | 395.2px | 0 |
| spacious | 8.61 | 1 | 548.2px | 0 |

### Finding

The spacious policy remained semantically correct but became operationally expensive. It preserved desktop-style comfort space even after text and narrow width had already consumed most of the available geometry.

### STUDIO JUDGMENT

Accessibility does not mean preserving ornamental whitespace ratios at all costs.

When text enlargement or narrow width consumes space, first preserve:

1. content meaning;
2. required control geometry;
3. grouping relationships;
4. reading/focus order;
5. distinguishability of actions and values.

Only then preserve discretionary comfort space.

---

# 7. Cycle 2 adaptive re-proof

The adaptive policy compresses only intermediate/spacious comfort whitespace under the narrow + 200% condition.

Across all 72 adaptive conditions:

- controls below the specimen contract: `0`;
- horizontal overflow: `0`;
- clipped critical cells: `0`;
- hidden critical cells: `0`;
- average scroll ratio improved from `2.09` (`preserve`) to about `1.98`.

In the extreme Korean condition:

| Density | Preserve scroll ratio | Adaptive scroll ratio | Preserve rows | Adaptive rows |
| --- | ---: | ---: | ---: | ---: |
| compact | 5.17 | 5.17 | 2 | 2 |
| intermediate | 6.31 | 5.32 | 2 | 2 |
| spacious | 8.61 | 5.68 | 1 | 2 |

Spacious average row height reduced from about `548.2px` to `352.2px` while preserving all critical content and the control-geometry contract.

### SYNTHESIS

The identity of a “spacious” mode should be relational, not absolute.

It can remain more spacious than compact while its absolute gaps shrink under a constrained environment.

### STUDIO JUDGMENT — adaptive density hierarchy

Treat density tokens as **bounded relationships** rather than immutable numbers.

A production system can define:

- semantic spacing tiers;
- preferred values;
- minimum/maximum bounds;
- recomposition rules;
- target/content constraints that are never compressed merely to preserve visual rhythm.

---

# 8. Normal desktop result — spaciousness still has a measurable cost

At `1024 × 768`, 1.0× text, English, adaptive policy:

| Density | Scroll ratio | Max rows / viewport | Average row height | Wrapped cells |
| --- | ---: | ---: | ---: | ---: |
| compact | 1.09 | 12 | 52.9px | 0 |
| intermediate | 1.28 | 12 | 60.9px | 0 |
| spacious | 1.55 | 10 | 72.9px | 0 |

### Interpretation

This does **not** prove compact is better.

It proves that spaciousness consumes simultaneous-comparison capacity even before localization and enlargement become difficult.

For comparison/monitoring tasks, that cost may matter. For first-run comprehension, sparse editorial content, or high-risk decisions, the extra separation may be worth it.

The task decides the trade-off.

---

# 9. Narrow default-text result — localization changes the density cost

At `390 × 844`, 1.0× text, long Korean labels, adaptive policy:

| Density | Scroll ratio | Max rows / viewport | Average row height | Wrapped cells |
| --- | ---: | ---: | ---: | ---: |
| compact | 1.93 | 7 | 108.9px | 8 |
| intermediate | 2.24 | 6 | 124.9px | 11 |
| spacious | 2.70 | 5 | 148.9px | 12 |

### SYNTHESIS

Localization does not merely “make text longer.” It changes the spatial cost curve of the density system.

The same nominal density mode can therefore produce different practical throughput across languages.

### OPEN

This specimen uses generic system-font rendering and one synthetic long-Korean dataset. T005 or later Type evidence should independently test actual Latin/Korean fallback/metrics, and live projects must test their real strings.

---

# 10. Project decision protocol derived from the validation

Before recommending compact/intermediate/spacious density, collect:

1. primary task: comparison, monitoring, search, reading, editing, onboarding, decision review;
2. simultaneous-information requirement;
3. content fields that may never be hidden/truncated;
4. target/input contract;
5. typical and worst-case label lengths;
6. languages/scripts;
7. expected text enlargement/zoom;
8. narrowest supported container;
9. whether users can move between density modes;
10. whether the same surface is novice-facing, expert-facing, or both.

Then separate four decisions:

### A. Semantic information density
What must remain visible together?

### B. Interaction geometry
What target/spacing constraints must not shrink merely to fit more content?

### C. Comfort whitespace
Which gaps may flex when space becomes constrained?

### D. Recomposition
When should the layout change structure instead of continuing to compress?

---

# 11. Failure conditions

Reject or rework a density strategy when:

- a “compact” mode gains capacity mainly by hiding task-critical data;
- truncation removes the part of an identifier needed for recognition;
- smaller spacing also silently shrinks input/target geometry;
- a “spacious” mode preserves desktop whitespace under extreme enlargement while forcing unnecessary scrolling;
- long localization is treated as a content problem rather than a layout stress case;
- density tokens are frozen values that cannot respond to container/text constraints;
- progressive disclosure removes simultaneous comparison required by the task;
- a density comparison changes typography/color/content at the same time, making causal interpretation impossible;
- preference is reported as evidence of task efficiency;
- rows-per-screen is reported as quality without accounting for lost content or interaction cost.

---

# 12. Evidence strength

## Established in this block

- real Chromium layout/reflow measurements across 216 policy/configuration combinations;
- explicit naive failure baseline;
- failure → preservation revision;
- preservation → adaptive-whitespace revision;
- no-clipping/no-hiding/no-horizontal-overflow result in the preserve/adaptive policies;
- quantified cost of rigid spaciousness under narrow + 200% text;
- a reproducible test harness.

## Not established

- human known-item search time;
- comparison accuracy;
- subjective preference;
- motor error rate;
- screen-reader behavior;
- real product data distributions;
- actual browser zoom rather than CSS-controlled font-scale surrogate;
- cross-browser/device behavior;
- actual T004/T005 font rendering and fallback;
- forced-colors/light-dark Color transfer;
- real Web Design page-system integration.

Therefore this block advances L002 from `IN STUDY` to **PRACTICE + CRITIQUE**, not PASS.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - density comparisons become invalid when text is treated as fixed placeholder geometry;
  - long Korean labels materially change row height/wrap cost;
  - compact data surfaces are a strong context for T004/T005 numeric/fallback transfer.
- Canonical section:
  - Sections 6–9 and the reproducible specimen.
- Confirmation / contradiction / transfer note:
  - confirms Type's warning that rendering/metrics must be tested in real spatial contexts; this block does not test T004 itself.
- Scope limit:
  - system-font browser rendering only; no Type-owned browser/font PASS.

### Color
- Useful finding/context:
  - the current experiment holds color nearly constant, so geometry-driven density cost is isolated;
  - perceived clutter can now be transfer-tested by keeping this geometry fixed while varying C002/C003 luminance/chroma/state roles.
- Canonical section:
  - controlled specimen and Cycle 2 adaptive policy.
- Confirmation / contradiction / transfer note:
  - does not contradict Color's visual-density findings; it creates a controlled base for separating spatial from color-driven clutter.
- Scope limit:
  - no forced-colors, CVD, light/dark, or environmental validation here.

### Layout / Interaction
- Useful finding/context:
  - interaction geometry and semantic content are invariants that should be separated from discretionary whitespace;
  - density should adapt relationally under extreme text/container constraints.
- Canonical section:
  - Sections 4–7.
- Confirmation / contradiction / transfer note:
  - extends L002 from conceptual framework into rendered practice and refines the meaning of “adaptive density.”
- Scope limit:
  - human task efficiency remains open.

### Web Design
- Useful finding/context:
  - reusable 216-condition density/reflow matrix with naive/preserve/adaptive policies;
  - concrete stress cases for real page-system reproduction.
- Web application / validation consequence:
  - reproduce with actual browser zoom, project typography, real CSS component tokens, localization, framework containers, and representative dashboards/forms/tables.
- Confirmation / contradiction / transfer note:
  - current result is controlled Layout-owned Chromium evidence; Web should return platform/page-system limitations explicitly.
- Scope limit:
  - not a complete web product or cross-browser/device PASS.

---

# Next evidence step

Highest-value next validation for L002 is **human task evidence**, not another spacing variant.

Use matched preserve/adaptive variants to test at least:

- known-item search;
- two-row or multi-column comparison;
- error-free action selection;
- subjective workload/preference separately from objective performance.

Randomize variant order and avoid letting users infer that one density is the expected answer.

Until that evidence exists, the studio may recommend density conditionally from task structure and rendered constraints, but should not claim a universal optimal density.
