# C011 — Forced Colors and Semantic/Data-Color Resilience: State, SVG, Used-Value, and Opt-Out Policy

Status: **PRACTICE + CROSS-DOMAIN TRANSFER VALIDATION / Chromium forced-colors state + SVG + focus + opt-out evidence complete; Windows High Contrast, Firefox/Safari, AT, human comprehension and production Web validation pending**

## Why this study exists

C001 established the Color-side hypothesis that authored color can be replaced by the user agent and that state meaning should not depend on literal color alone. Interaction I003 independently validated that hypothesis for current/focus/async states.

C008 then added a different problem: charts may use color for **data identity**, not only interaction state.

C011 asks:

> When forced colors is active, what actually happens to HTML semantic colors, focus styling, and inline-SVG data colors, and what Color policy should a product use when the browser can either replace or preserve authored chart colors?

A second question is intentionally adversarial:

> Is `forced-color-adjust:none` a safe generic escape hatch?

C011 answers **no**.

Reproducibility artifacts:

- `C011-forced-colors-semantic-data-specimen.html`
- `C011-forced-colors-semantic-data-playwright.py`
- `C011-forced-colors-semantic-data-results.json`

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: current Type status through T014 and C009 Type→Color transfer.
- Reusable finding: visible text labels and localized strings are a robust non-color channel only if the actual shipped Type/fallback/normalization path preserves them.
- Replication / challenge / transfer opportunity: later replace the simple labels with Korean/English localized chart labels and exact shipped webfonts.
- Dependency or overlap: Type owns font/fallback/normalization/shaping. C011 holds Type simple and studies Color-channel replacement.

### Color
- Evidence checked: C001, C002, C003, C008, C009, C010.
- Reusable finding: semantic role must precede literal color; data identity and interaction emphasis are separate axes; browser/user color replacement is a production boundary rather than a palette defect.
- Replication / challenge / transfer opportunity: independently transfer C001/I003 into chart/data-color behavior and challenge the naive assumption that all SVG colors automatically collapse.
- Dependency or overlap: direct Color extension and contradiction refinement.

### Layout / Interaction
- Evidence checked: I003 forced-colors state resilience and current Layout/Interaction status through L006/I004.
- Reusable finding: current/focus/pending/failed/confirmed are semantic states before they are styled; box-shadow-only focus is fragile in forced colors.
- Replication / challenge / transfer opportunity: reuse I003 state semantics, then extend into chart/data identity while preserving Interaction ownership.
- Dependency or overlap: Interaction owns state meaning and behavior. Color owns the visual encoding and replacement/resilience policy.

### Web Design
- Evidence checked: current Web status and `research/web/README.md`.
- Reusable finding: Web owns complete browser/page/device integration and should eventually validate target browsers/OSes and actual components.
- Implementation/application validation opportunity: repeat with actual production tokens, SVG/canvas chart libraries, Windows High Contrast, browser zoom, target OS/device and AT.
- Dependency or overlap: no substantive W### evidence exists at this checkpoint. C011 is Color-owned Chromium transfer evidence, not Web PASS.

### Other / Cross-cutting / Future Specialist
- Evidence checked:
  - W3C CSS Color Adjustment Module Level 1, Candidate Recommendation Snapshot 2025-12-16;
  - WCAG 2.2 Understanding 1.4.1 Use of Color;
  - WCAG 2.2 Understanding 1.4.11 Non-text Contrast.
- Reusable finding: forced colors can replace used colors and suppress shadows; visible alternatives to color remain necessary.
- Dependency or overlap: real user high-contrast preferences and assistive-technology behavior remain external validation.

### Overlap decision
- **INDEPENDENT VALIDATION + TRANSFER VALIDATION + CONTRADICTION REFINEMENT + IMPLEMENTATION VALIDATION**.
- Why: I003 already proved state-color collapse. C011 adds chart/SVG behavior and discovers that default inline-SVG forced-color policy is materially different from ordinary HTML color replacement.

---

# SOURCE — forced colors changes used color, not necessarily the authored/computed token

Primary source:

- W3C CSS Color Adjustment Module Level 1: `https://www.w3.org/TR/css-color-adjust-1/`

The current Candidate Recommendation says that when forced colors is active and `forced-color-adjust:auto` applies, color components of properties such as `background-color`, `border-color`, `color`, `fill`, `stroke`, and `outline-color` are force-adjusted to the user's palette.

It also states that `box-shadow` and `text-shadow` compute to `none` in forced colors.

### SYNTHESIS

A design token can remain conceptually correct while the browser deliberately substitutes a different **used color**.

Therefore:

`semantic role != authored token != computed color != forced used color != physical appearance`.

### STUDIO JUDGMENT

Color QA for user override modes must test rendered/used behavior, not just inspect source tokens.

---

# SOURCE — SVG has a special forced-color policy

The same CSS Color Adjustment specification says user agents are expected to apply:

```css
svg|svg { forced-color-adjust: preserve-parent-color; }
svg|foreignObject { forced-color-adjust: auto; }
```

The stated purpose is to avoid breaking SVG content whose exact illustration colors may be meaningful while keeping inherited text color coherent.

### SYNTHESIS

The statement:

> “Forced colors replaces all chart SVG colors.”

is too broad.

SVG is a special case. The browser can preserve authored SVG paint unless the author explicitly changes the forced-color policy.

This creates a **design choice**, not an automatic accessibility solution.

---

# SOURCE — opting out is exceptional, not a default fix

`forced-color-adjust:none` restores author control over colors. The specification explicitly advises authors to use it only when they are themselves making color/contrast adjustments needed to provide an appropriate experience.

### STUDIO JUDGMENT

Reject:

> “Our chart looks wrong in forced colors, so set `forced-color-adjust:none` on the app.”

Opt-out bypasses user-agent adjustment. It transfers responsibility back to the product.

Use it only for a bounded element with an explicit accessibility reason, redundant semantics, and target-environment validation.

---

# SOURCE — WCAG still requires visible alternatives to color

Primary sources:

- `https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html`
- `https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html`

WCAG 1.4.1 requires a visible alternative where information depends on distinguishing color. Accessible names alone do not replace the visible alternative for sighted users who cannot distinguish the colors.

### SYNTHESIS

Forced-color resilience and color-vision resilience overlap, but are not identical.

A chart can preserve its original SVG colors in forced colors and still fail users who cannot distinguish the series.

---

# CONTROLLED SPECIMEN

Environment:

- Chromium `144.0.7559.96`;
- Playwright Python;
- headless Linux;
- viewport `1200×720`;
- DPR `1`;
- `forced_colors="active"` media emulation.

The specimen includes:

1. HTML status chips with color-only failure and text/shape revision;
2. a shadow-only focus failure and structural-outline revision;
3. a color-only inline SVG using Chromium's default SVG forced-color behavior;
4. the same color-only SVG with explicit `forced-color-adjust:auto` on SVG descendants;
5. a revised SVG with `auto` plus dash patterns, marker geometry, direct labels and selected-series stroke width;
6. an explicit `forced-color-adjust:none` opt-out specimen.

The harness uses both computed-style inspection and raster screenshots.

---

# RESULT A — HTML color-only state fills collapse

Normal state-chip fills:

- pending: `rgb(244,197,66)`;
- failed: `rgb(216,74,74)`;
- confirmed: `rgb(46,159,97)`.

Under forced colors all three become:

`rgb(255,255,255)` in this Chromium emulation.

The failure variant hides the text, so the three visible meanings collapse.

The revised variant retains:

- explicit visible labels;
- `…`, `!`, `✓` symbols;
- different border structures.

### TRANSFER VALIDATION

This reproduces I003/C001 on a Color-owned specimen.

---

# RESULT B — shadow-only focus disappears; outline survives

Naive focus:

- normal: box-shadow glow present;
- forced colors: `box-shadow: none`;
- outline remains `none`.

Robust focus:

- forced colors: `outline-style: solid`;
- outline width: `3px`;
- outline color is browser/system resolved.

### STUDIO JUDGMENT

Do not use shadow/glow as the only focus channel.

The literal focus color can be user-agent controlled while the focus geometry remains authored.

---

# RESULT C — default inline SVG preserved all four author series colors

This was the first contradiction/refinement.

The default color-only SVG uses four series colors:

- `#D62728`;
- `#2CA02C`;
- `#1F77B4`;
- `#9467BD`.

Under Chromium forced-colors emulation, raster analysis still found all four authored RGB values:

- red: `827` exact pixels;
- green: `881`;
- blue: `920`;
- purple: `913`.

The computed `forced-color-adjust` on the SVG paths was `preserve-parent-color`.

### CONTRADICTION REFINEMENT

Reject the overgeneralized rule:

> “Forced colors will automatically collapse every SVG data series.”

It did not in this browser/specimen.

### IMPORTANT LIMIT

This does **not** make a hue-only chart robust.

The browser preserved the colors; a user with CVD, monochrome rendering, poor display conditions, or a different browser/OS policy may still not distinguish the series.

---

# RESULT D — explicit SVG `forced-color-adjust:auto` removes the authored series colors

C011 applies `forced-color-adjust:auto` to the SVG and descendants.

Important implementation nuance:

`getComputedStyle(...).stroke` still reports the authored stroke values in this Chromium run.

However raster screenshot analysis shows **zero exact pixels** for all four authored series colors in the forced-color image.

This follows the specification's distinction between computed value and forced **used value**.

### STUDIO JUDGMENT

For forced-color QA, a computed CSS value is insufficient evidence when the specification allows used-value substitution.

Use rendered evidence or an implementation test that observes the actual result.

---

# RESULT E — revised chart survives author-color removal structurally

The revised chart also opts its SVG descendants into `forced-color-adjust:auto`.

Raster analysis confirms all four authored series colors are removed.

Yet the chart retains:

- four distinct dash patterns;
- four endpoint marker geometries;
- direct series labels;
- explicit `C selected` text;
- selected series stroke width `6px` versus `3px` peers.

### SYNTHESIS

Data identity can survive color replacement if identity is not stored in hue alone.

For high-value charts, candidates include:

- direct labels;
- line pattern;
- marker shape;
- stroke weight for interaction emphasis;
- position/grouping;
- explicit status/reference annotations.

Do not apply every redundant channel mechanically. Choose the minimum set that preserves the task.

---

# RESULT F — `forced-color-adjust:none` preserves author colors, but that is not accessibility proof

The opt-out specimen retains its authored:

- foreground `#A8F0E9`;
- background `#0D1317`;
- border `#A8F0E9`.

Its computed `forced-color-adjust` is `none`.

### REJECT

Reject:

> “The opt-out keeps our brand colors, therefore it is the accessible solution.”

The result proves author control, not user suitability.

---

# AUTOMATED RESULT

Final harness:

**21 / 21 bounded assertions PASS.**

The assertions cover:

- forced-colors media activation;
- HTML state-fill collapse;
- visible revised labels/borders;
- default SVG author-color preservation;
- default SVG `preserve-parent-color`;
- explicit SVG-auto raster author-color removal;
- four surviving dash patterns;
- surviving selected-series width;
- surviving direct labels;
- shadow-focus removal;
- outline-focus survival;
- opt-out author-color preservation;
- revised chart structural survival after color replacement.

The assertion suite deliberately treats reproduced failures as successful experimental assertions.

---

# FAILURE → REVISION MODEL

## Failure 1 — assume every authored color survives

Fails for ordinary HTML surfaces/state colors.

## Failure 2 — assume every authored color collapses

Fails for default inline SVG in the tested Chromium/spec path.

## Failure 3 — use `forced-color-adjust:none` globally

Preserves author colors by bypassing the user's forced palette and transfers the accessibility burden to the product.

## Revision

For each semantic/data-color surface, define:

`semantic job → default forced-color policy → surviving non-color channels → explicit system-color adaptation if needed → opt-out justification if any → target-browser/OS/device validation`.

---

# PROJECT READINESS TEST

## When should this knowledge be used?

Use it for:

- selected/current/focus/status components;
- charts and dashboards;
- SVG icon/data systems;
- products with Windows/high-contrast accessibility requirements;
- custom controls;
- any semantic color system deployed on the web.

## When should it not be over-applied?

Do not add patterns/icons/labels to every decorative color difference.

Do not force exact brand colors through user overrides when the color carries no essential meaning.

Do not infer native-app behavior directly from Chromium forced-colors evidence.

## Required project inputs

- which distinctions are semantic;
- which distinctions are data identity;
- chart technology: SVG/canvas/DOM/image;
- target browsers/OSes;
- whether exact color itself is essential content;
- user accessibility requirements;
- interaction states and focus requirements;
- whether direct labels/patterns/markers are feasible;
- production Type/localization constraints.

## Decisions this can change

- whether SVG should keep the UA default `preserve-parent-color`;
- whether a bounded chart should opt into `forced-color-adjust:auto`;
- whether system colors should be supplied in `@media (forced-colors:active)`;
- whether `forced-color-adjust:none` is defensible for a specific element;
- which redundant channels are required;
- whether hue-only series identity is acceptable;
- how selected/current/focus/status is expressed.

## Failure conditions

- color-only meaning;
- hidden labels under user palette replacement;
- shadow-only focus;
- `getComputedStyle` mistaken for actual forced used value;
- global opt-out;
- preserved SVG hues mistaken for CVD robustness;
- alternate encodings so dense that they damage chart legibility.

## Validation plan

1. normal light/dark theme;
2. forced-colors emulation;
3. real Windows High Contrast where relevant;
4. target Chromium/Firefox/Safari/Edge behavior;
5. actual SVG/canvas/chart library;
6. keyboard focus and interaction-state combinations;
7. CVD/monochrome diagnostic;
8. localized/direct-label stress;
9. human series/state identification when risk warrants it;
10. physical target devices where visual conditions matter.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: direct labels are a major non-color resilience channel for charts.
- Canonical section: Results E and Project Readiness.
- Confirmation / contradiction / transfer note: extends C009; label robustness still depends on actual font/fallback/normalization.
- Scope limit: C011 does not validate production webfonts or Korean shaping.

### Layout / Interaction
- Useful finding/context: state meaning survives best when Color encodes already-defined semantics with structural redundancy; shadow-only focus again fails.
- Canonical section: Results A/B and Failure→Revision.
- Confirmation / contradiction / transfer note: confirms I003 and extends it into Color/data-viz policy.
- Scope limit: C011 does not redefine current/focus/pending/failed/selected semantics.

### Web Design
- Useful finding/context: inline SVG has a special forced-color policy; computed style may not reveal forced used paint; author opt-in/opt-out must be tested in actual chart/browser stacks.
- Web application / validation consequence: reproduce with production SVG/canvas libraries, Windows High Contrast, Edge/Firefox/Safari, system colors, zoom, Type, AT and real devices.
- Confirmation / contradiction / transfer note: provides Color-side implementation evidence and a concrete browser acceptance matrix.
- Scope limit: no W### production proof exists yet.

---

# OPEN

- real Windows High Contrast / Edge behavior;
- Firefox/Safari forced/user-color parity;
- assistive-technology behavior;
- production SVG and canvas chart libraries;
- whether canvas requires an alternate DOM/table representation in specific products;
- real CVD users and human series-identification tasks;
- Korean/localized direct-label stress;
- forced-colors combined with zoom, text enlargement and responsive reflow;
- physical-display/environment interaction;
- exact policy for brand-critical illustrations versus semantic charts.

## Status implication

C001 Web color override resilience advances from source/transfer framing into stronger **PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION**.

C008 data-visualization color gains its first forced-colors SVG transfer proof.

Neither reaches PASS.