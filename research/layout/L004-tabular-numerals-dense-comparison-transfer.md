# L004 — Tabular Numerals as a Layout Contract: Dense Comparison, Alignment, and Width Cost

Status: **PRACTICE + CRITIQUE / TYPE→LAYOUT TRANSFER VALIDATION — controlled Chromium evidence established; production-font, cross-browser/device, T004-research-font, and human comparison validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Canonical path: `research/layout/`

Reproducible artifacts:

- `research/layout/L004-tabular-numerals-playwright.py`
- `research/layout/L004-tabular-numerals-results-summary.json`

## Question

When a dense data surface needs rapid numeric comparison, does enabling tabular numerals actually improve browser-layout alignment, what spatial cost does it introduce, and which parts of the result belong to Type versus Layout?

This study transfer-tests:

- `research/type/T004-native-numeral-punctuation-renderer-proof.md`;
- `research/layout/L002-whitespace-density-spatial-rhythm.md`;
- `research/layout/L003-type-fallback-density-reflow-transfer.md`.

The experiment deliberately uses installed open-source control fonts rather than copying Type-owned font binaries into Layout. It therefore tests the **runtime layout contract implied by T004**, not the exact T004 research font.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `progress/TYPE_STATUS.md` through T005;
  - `research/type/T004-native-numeral-punctuation-renderer-proof.md`;
  - `research/type/T005-latin-korean-mixed-script-fallback.md`.
- Reusable finding:
  - T004 defines tabular figures as an equal-source-advance contract and shows that raw hinted advances can still split under some FreeType modes;
  - runtime client positioning therefore remains part of approval;
  - T005 reinforces that actual renderer/layout transfer must be measured rather than inferred from source metrics.
- Replication / challenge / transfer opportunity:
  - test CSS `font-variant-numeric: tabular-nums` in Chromium and measure digit advances, decimal alignment, and dense-column width cost.
- Dependency / overlap:
  - Type owns glyph design, OpenType feature construction, source metrics, hinting, and production font suitability; Layout owns whether the numeric column allocates enough space and supports the comparison task.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md` through C006.
- Reusable finding:
  - finance/data roles and interaction states should remain semantically distinct, but the present question isolates geometry/type behavior.
- Replication / challenge / transfer opportunity:
  - later hold numeric geometry fixed while testing Color-defined finance/data emphasis if needed.
- Dependency / overlap:
  - **Not materially relevant to the current browser-width experiment after checking.**

### Layout / Interaction
- Evidence checked:
  - L002 density framework and rendered validation;
  - L003 fallback/reflow transfer;
  - current `progress/LAYOUT_STATUS.md`.
- Reusable finding:
  - compactness is invalid when content is clipped merely to preserve row count;
  - typography is a spatial input near thresholds;
  - intrinsic content requirements may legitimately take space away from secondary content depending on task priority.
- Replication / challenge / transfer opportunity:
  - test whether a fixed numeric column that fits proportional figures can fail after enabling a comparison-oriented numeric feature.
- Dependency / overlap:
  - primary ownership of the resulting spatial allocation remains Layout.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`; no substantive `W###` result was available at study start.
- Reusable finding:
  - Web owns production font loading, complete table/page systems, browser/device matrices, zoom/DPR, framework behavior, and design-to-code transfer.
- Implementation / application validation opportunity:
  - reproduce this matrix using real production fonts, CSS delivery, target browsers/devices, actual tables, sorting/filtering, localization, and zoom.
- Dependency / overlap:
  - this is a Layout-owned controlled browser transfer, not Web canonical proof.

### Other / cross-cutting / future specialist
- Evidence checked:
  - W3C CSS Fonts Module Level 4, numerical formatting;
  - current Microsoft OpenType feature registry.
- Reusable finding:
  - CSS `font-variant-numeric: tabular-nums` maps to OpenType `tnum` when supported;
  - `tnum` is the registered Tabular Figures feature.
- Dependency / overlap:
  - human comparison speed and error rate are not established by geometric alignment alone.

### Overlap decision
- **TRANSFER VALIDATION + METHOD COMPARISON + FAILURE ANALYSIS**.
- Why:
  - T004 established a font-level risk; L004 asks whether that risk survives at the browser layout layer and what new spatial trade-off appears when tabular numerals are actually used.

---

# 1. SOURCE — CSS exposes tabular numerals as a numeric-spacing control

Current CSS Fonts Level 4 defines `font-variant-numeric` and maps `tabular-nums` to OpenType `tnum`. The specification explicitly presents tabular figures as a way for columns of numbers to line up when the font supports the feature.

Authoritative source:

- https://www.w3.org/TR/css-fonts-4/#font-variant-numeric-prop

The current OpenType feature registry lists `tnum` as **Tabular Figures**.

Authoritative source:

- https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist

### SYNTHESIS

`tnum` is a type-system capability. A product still needs a layout/formatting contract that decides:

- which numeric roles require it;
- how values are aligned;
- whether decimals/signs/currency/grouping are formatted consistently;
- how much width the numeric column reserves;
- what happens when localization or larger values increase intrinsic width.

### STUDIO JUDGMENT

Do not equate “font supports tabular figures” with “the table is aligned.” Type supplies the numeric spacing behavior; Layout supplies the column and formatting geometry.

---

# 2. Controlled browser experiment

Environment:

- Chromium `144.0.7559.96`;
- CSS `tabular-nums` support confirmed;
- local control fonts confirmed available: Inter, Roboto, Noto Sans;
- sizes: 14, 16, 20, 32px;
- values for decimal-alignment test: `+1111.11`, `-8888.88`, `+6060.60`, `+1234.56`, `-9876.54`;
- dense-column values include `$11,242.88`, `$18,888.88`, `$9,111.11`, `$12,606.60`.

Measured quantities:

1. per-digit DOM advance width for `0–9`;
2. decimal-point x-position in a 160px right-aligned numeric field;
3. overflow in an 88px fixed numeric column;
4. overflow after changing the numeric column to intrinsic `max-content` allocation.

Control fonts are experimental transfer conditions, not product recommendations.

---

# 3. Finding A — browser tabular layout equalized digit advances in all tested controls

Across Inter, Roboto, and Noto Sans, at 14/16/20/32px:

- proportional digit-width spread was non-zero;
- tabular digit-width spread was `0` in DOM layout for every tested font/size.

At 16px:

| Font | Proportional digit spread | Tabular digit spread |
| --- | ---: | ---: |
| Inter | 3.828px | 0px |
| Roboto | 2.359px | 0px |
| Noto Sans | 2.375px | 0px |

For Inter 16px, proportional digits ranged from about `6.516px` (`1`) to `10.344px` (`4`), while every tested tabular digit measured `10.375px`.

### TRANSFER VALIDATION

This **confirms the comparison benefit at the Chromium CSS-layout layer** for these control fonts.

It does **not contradict T004's raw hinted-advance split**. T004 measured a lower-level FreeType raw-hinting condition; Chromium's shaping/layout client can position glyphs with its own fractional advances and feature application. These are different evidence layers.

### STUDIO JUDGMENT

When exact horizontal comparison is important, approval should distinguish:

`source feature/metrics → shaping/layout advance → rasterized glyph appearance`.

Do not reject or approve a numeric system from only one layer.

---

# 4. Finding B — tabular numerals plus right alignment removed decimal drift in the controlled strings

The five right-aligned values used identical sign/decimal-format structure but different digits.

At 16px, decimal-point x-position spread was:

| Font | Proportional | Tabular |
| --- | ---: | ---: |
| Inter | 7.969px | 0px |
| Roboto | 4.719px | 0px |
| Noto Sans | 4.750px | 0px |

The same zero-spread tabular result persisted at 14/20/32px in these controls.

### SYNTHESIS

Tabular digits are most useful when the formatting contract also supports the comparison task.

For this controlled case, **fixed fractional precision + right alignment + tabular digits** produced aligned decimal positions.

### Scope limit

This does not prove alignment for arbitrary financial strings. Decimal alignment can still be disturbed by:

- variable fractional precision;
- suffixes after the number;
- locale-specific separators;
- accounting parentheses;
- units/currencies in inconsistent positions;
- fallback fonts lacking equivalent feature behavior;
- missing-value symbols;
- scientific notation;
- mixed scripts or bidirectional content.

A real table must define its number-format contract separately.

---

# 5. Failure — enabling `tnum` can increase intrinsic width and break a previously “working” compact column

The dense specimen used a 360px row with an 88px fixed numeric column.

At 16px Inter:

- proportional values fit the 88px column;
- tabular values expanded enough that **3 of 4** tested cells overflowed;
- maximum required width was about `91px`.

Roboto and Noto Sans did not cross the same 88px threshold in this particular control.

### Why this matters

A layout can appear stable during design with proportional figures and break only after Type correctly enables tabular figures for comparison.

That is not necessarily a Type defect.

The numeric role may simply require more intrinsic width.

### Revision

The controlled revision changed:

`fixed 88px numeric track`

into

`max-content numeric track + flexible label track`.

Result for Inter tabular figures:

- overflow count: `3 → 0`;
- numeric track expands to the actual formatted value width (about `91.5px` for the widest tested strings);
- the flexible label column absorbs the small width cost.

### STUDIO JUDGMENT

For a comparison-centric dense table, reserve numeric width from the **actual production number format with the approved numeric feature**, not from placeholder values or proportional-figure screenshots.

But `max-content` is not a universal prescription. On very narrow surfaces it can starve the object-label column. The project must state which information is primary:

- if numeric comparison is primary, protect the numeric track and recompose/shorten secondary labels;
- if object identity is primary, preserve the label and move secondary metrics to another line/region;
- if both are primary and simultaneous comparison is essential, the surface may need horizontal scrolling, a different table architecture, or a larger device class rather than silent truncation.

---

# 6. Project decision framework

## Use tabular numerals when

- users compare repeated numeric values across rows/columns;
- financial/operational monitoring requires stable horizontal rhythm;
- timer/counter/readout changes should not cause layout jitter;
- numeric scanning is a primary or repeated task.

## Do not apply automatically when

- numbers occur mainly in prose;
- compact reading flow benefits from proportional figures;
- the selected font lacks a credible tabular set;
- the values are not formatted consistently enough for the feature to solve the real comparison problem.

## Required project inputs

Before approving dense numeric layout, identify:

1. font/fallback stack and whether the relevant face supports `tnum`;
2. target number formats, locales, signs, units, currencies and missing values;
3. expected min/max magnitudes;
4. precision rules;
5. whether comparison, object identity, or action access has first spatial priority;
6. target widths and text scaling/zoom conditions;
7. whether values update dynamically;
8. browser/platform stack.

## Failure conditions

Reject the current layout if:

- enabling the approved numeric feature causes clipping/overlap;
- decimal/sign alignment varies in a comparison-critical column without a deliberate reason;
- numeric width was sized from unrealistic placeholder values;
- label space collapses below the task's identification needs merely to protect a fixed metric column;
- localization changes the format beyond the tested width contract;
- fallback silently disables or changes numeric behavior;
- alignment is judged from source font metrics without runtime proof.

---

# 7. Evidence classification

## SOURCE

- CSS Fonts Level 4 maps `tabular-nums` to OpenType `tnum` and describes it as a numerical-spacing control useful for aligned tabular data.
- OpenType registers `tnum` as Tabular Figures.

## REPLICATION / TRANSFER VALIDATION

- three installed control fonts;
- four CSS font sizes;
- DOM advance measurements;
- right-aligned decimal-position measurements;
- fixed-width vs intrinsic numeric-column stress.

## SYNTHESIS

- tabular figures can improve numeric comparison while increasing spatial demand;
- source/raw renderer evidence and browser layout evidence are distinct layers;
- the layout must be validated **after** numeric-feature activation.

## STUDIO JUDGMENT

Treat dense numeric alignment as a joint contract:

**number semantics + formatting + Type feature/runtime behavior + Layout track allocation**.

## OPEN

- exact T004 research font inside Chromium;
- production `@font-face` loading and fallback;
- Safari/Firefox/mobile engines;
- actual browser zoom/DPR/device rendering;
- Korean and other locale number formatting;
- accounting and variable-precision formats;
- dynamic-update jitter;
- T004 slashed-zero/punctuation transfer;
- human comparison speed/error evidence;
- screen reader/AT behavior for complex numeric tables;
- full Web Design page-system transfer.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: Chromium CSS layout produced zero digit-advance spread under `tabular-nums` for Inter/Roboto/Noto Sans at 14–32px, even though T004 documented raw hinted-advance splitting in a lower-level FreeType condition.
- Canonical section: L004 Sections 3–5.
- Confirmation / contradiction / transfer note: **CONFIRMATION + LAYER LIMITATION** — the `tnum` comparison contract survives in the tested browser controls, but raw hint metrics alone do not predict client layout; Inter's tabular set also increased required column width enough to expose a Layout failure.
- Scope limit: this does not validate the exact T004 research font or production font quality.

### Color
- Useful finding/context: dense finance numeric geometry is now measurable with the type feature held fixed.
- Canonical section: L004 controlled numeric specimen.
- Confirmation / contradiction / transfer note: future Color salience work can keep the numeric geometry stable while varying color roles.
- Scope limit: no Color conclusion is claimed in L004.

### Layout / Interaction
- Useful finding/context: `tnum` must be activated before finalizing numeric-column widths; fixed placeholder-derived widths can fail after the correct Type feature is applied.
- Canonical section: L004 Section 5.
- Confirmation / contradiction / transfer note: extends L002/L003 — typography is not decoration applied after geometry; it can alter the valid density allocation.
- Scope limit: human comparison benefit remains unmeasured.

### Web Design
- Useful finding/context: reproducible Chromium matrix for `font-variant-numeric`, decimal alignment, and intrinsic-width failure.
- Web application / validation consequence: reproduce with production fonts, `@font-face`, localization, table components, sorting/filtering, actual zoom/DPR and target browser/device stack.
- Confirmation / contradiction / transfer note: return whether production browser/layout behavior confirms, limits, or contradicts the control result.
- Scope limit: current evidence is Chromium + installed local control fonts only.
