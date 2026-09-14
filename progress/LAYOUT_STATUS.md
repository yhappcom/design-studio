# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L003`; Interaction `I002`

This file is maintained by the Layout, Spatial & Interaction Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist studies spatial organization and interaction to improve real app, web and product decisions. Research volume and curriculum speed are not the goal.

When a project arrives, the specialist must convert accumulated knowledge into project-specific guidance on information/spatial hierarchy, grouping, density, responsive behavior, navigation, state, feedback, recovery, target placement, accessibility, implementation trade-offs, validation strategy, uncertainty and failure conditions.

Self-directed research remains ACTIVE. Adjacent Type, Color, Web Design, Accessibility, Human Factors, browser/platform or implementation knowledge may be studied when it materially improves judgment, replication, transfer validation or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied spatial and interaction modules; Foundation is not passed.

Spatial and temporal/behavioral evidence remain separately indexed under `research/layout/` and `research/interaction/` so those claim types are not conflated.

## Four-specialist collaboration sync

Design Studio operates with four official peer specialists:

1. Typography / Type Design
2. Color
3. Layout, Spatial & Interaction
4. Web Design

Web Design is the main real-web application/validation partner for this role. At the latest synchronization point, `progress/WEB_STATUS.md` still listed `W001` as not yet begun. Do not invent Web evidence; re-check Web status and `research/web/` before every substantial block.

## Canonical evidence already established

### Layout / spatial

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`
- `research/layout/L001-figure-ground-balance-optical-centering.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`
- `research/layout/L002-density-validation-specimen.html`
- `research/layout/L002-density-validation-playwright.py`
- `research/layout/L002-density-validation-results-summary.json`
- `research/layout/L002-density-validation-report.md`
- retained product-design exercises for grid, responsive transfer, grouping and L001 critique.

### Interaction

- `research/interaction/007-interaction-agency-feedback-errors.md`
- `research/interaction/015-directness-state-modes-reversibility.md`
- `research/interaction/I001-navigation-history-focus-restoration-interruption.md`
- `research/interaction/I001-navigation-state-validation-specimen.html`
- `research/interaction/I001-navigation-state-validation-playwright.py`
- `research/interaction/I001-navigation-state-validation-report.md`
- retained state-matrix and Study 015 practice/critique evidence under `product-design/exercises/`.

### Shared accessibility evidence relevant to this role

- `research/004-accessibility-reflow-targets-focus.md`
- retained accessibility geometry practice and critique under `product-design/exercises/`.

## Latest completed block — L002 rendered density validation

L002 was converted from a source/project framework into a running browser-rendered density experiment.

### Controlled matrix

The specimen compares the same 12-row portfolio dataset across:

- three policies: `naive`, `preserve`, `adaptive`;
- compact / intermediate / spacious density;
- 1440×900, 1024×768, 768×800, 390×844 viewports;
- 1.0×, 1.25× and 2.0× text scale;
- English and long Korean strings.

This produces **72 conditions per policy / 216 rendered conditions total**.

### Failure → revision evidence

`naive` compactness intentionally used smaller controls, truncation and narrow-screen field hiding.

Across its 72 conditions:

- 32 conditions rendered a control below the specimen's 44px contract;
- 580 critical cells were clipped/ellipsized;
- 432 critical cells were hidden.

This demonstrated that rows-per-screen or low scroll height are invalid density-quality metrics when content or interaction geometry changes to obtain them.

`preserve` then held semantic content and target geometry constant:

- below-contract controls: 0;
- horizontal overflow: 0;
- clipped critical cells: 0;
- hidden critical cells: 0.

The true spatial cost became visible: average scroll ratio rose from about 1.47 to 2.09.

### Second failure — rigid spaciousness under extreme text/container stress

At 390×844, 200% text and long Korean labels under `preserve`:

- compact: scroll ratio 5.17, max 2 rows/viewport;
- intermediate: 6.31, max 2 rows;
- spacious: 8.61, max 1 row; average row height about 548.2px.

The layout was semantically intact but operationally expensive because comfort whitespace remained too rigid after text had already consumed the available geometry.

### Adaptive re-proof

`adaptive` preserves content, target geometry and grouping while compressing discretionary intermediate/spacious whitespace under the strongest constraint.

Across all 72 adaptive conditions:

- below-contract controls: 0;
- horizontal overflow: 0;
- clipped critical cells: 0;
- hidden critical cells: 0.

At the extreme Korean condition:

- intermediate scroll ratio improved 6.31 → 5.32;
- spacious improved 8.61 → 5.68;
- spacious max simultaneous rows improved 1 → 2;
- spacious average row height reduced about 548.2px → 352.2px.

### Professional conclusion

A density mode should be treated as a **relational policy**, not an immutable pixel identity.

Preserve, in order:

1. task-critical content;
2. required interaction geometry;
3. semantic grouping;
4. reading/focus order;
5. distinguishability of actions and values;

then adapt discretionary comfort whitespace and recompose structure as constraints tighten.

Evidence level: **PRACTICE + CRITIQUE / controlled Chromium rendering evidence**.

This does not establish human search time, comparison accuracy, preference, motor error, actual browser zoom, cross-browser/device behavior, screen reader behavior, real T004/T005 font transfer or real Web page-system behavior.

## Previous completed block — I001 running validation

The I001 source framework was converted into a running HTML/JavaScript state specimen and exercised with Playwright in headless Chromium.

The controlled flow includes list → detail → edit, top-level switching, hierarchy Up, session-history Back/Forward, deep-link entry, dirty drafts, modal Escape/Close, route/modal focus restoration, async failure/retry/success and workspace resumption.

A failure → revision → re-proof cycle corrected seven state/focus defects. The final harness reached **14/14 controlled assertions PASS**.

Evidence level: **PRACTICE + CRITIQUE / controlled Chromium prototype evidence**, not production PASS. Real router/URL, assistive technology, cross-browser/device, real network and human resumption evidence remain open.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; multilingual/enlarged-text/browser transfer |
| Grid / alignment systems | CRITIQUE | real-browser proof; text-growth stress; broader responsive transfer |
| Perceptual grouping | CRITIQUE | broader context validation and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants; realistic layering; blinded human comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | controlled centroid dataset; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size device proof; blinded comparison; RTL/text-context transfer |
| Whitespace / density / spatial rhythm | **PRACTICE / CRITIQUE** | L002 216-condition rendered cycle complete; human search/comparison/action evidence, actual zoom, Type/Color/Web transfer and broader product validation pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002 adds narrow/enlarged/localized reflow evidence; actual browser zoom/device and broader real-content transfer pending |
| Interaction agency / feedback / errors | CRITIQUE | controlled running proof exists; broader recovery, real platform and assistive-technology validation |
| State / modes / reversibility / directness | CRITIQUE | controlled async failure/retry proof exists; broader real network/conflict/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | I001 running Back/Up/deep-link/focus/workspace/draft proof complete; real router/URL, AT, cross-browser/device, richer interruption/resumption and human evidence pending |

## Primary ownership

### Spatial

Canonical ownership includes grouping, regions, figure-ground, grid, alignment, geometry-driven hierarchy, whitespace, density, rhythm, proportion, visual mass, balance, optical centering, responsive/adaptive recomposition, reflow and target geometry.

### Interaction

Canonical ownership includes affordance/signifiers, mapping, feedback, agency, actions, destinations, navigation, task flow, state, modes, directness, reversibility, async/pending behavior, errors/recovery, pointer/touch/keyboard/gesture paths, focus flow and status communication.

Primary ownership is not a learning prohibition. Cross-domain replication and transfer validation are encouraged when they improve project judgment.

## Peer evidence currently affecting Layout / Interaction

### From Type

Type now includes T001–T004.

Most relevant findings:

- T001: fallback and vertical metrics can change wrapping, row height and reflow;
- T003: identical source metrics can produce different rendered advances/coverage depending on renderer/hinting/positioning;
- T004: even equal source tabular advances can split under some hinted rendering modes; compact numeric systems require actual-stack validation.

Consequences:

- density cannot be validated with placeholder rectangles;
- rows, navigation labels and numeric comparisons need actual typography/fallback/rendering transfer;
- L002's current system-font specimen is Layout evidence, not a Type PASS.

### From Color

Color now includes C001–C003.

Most relevant findings:

- C001: forced-colors/user overrides can replace or remove authored color channels;
- C002: semantic roles must remain separate from primitive/component color values;
- C003: information semantics and interaction state must not collide, and visual density may change through chroma/luminance even when geometry is fixed.

Consequences:

- current location, focus, pending/error/success must survive without color-only meaning;
- L002 isolates geometry by holding color nearly constant; a later transfer should hold geometry constant and vary Color conditions.

### From Web Design

No substantive `W###` study was available at the latest synchronization point.

Web should reproduce current Layout/Interaction matrices in complete page systems and return confirmation, limitation, contradiction or transfer failure rather than silently adapting conclusions.

## Incoming dependencies

- Type needs realistic dense/responsive contexts for text growth, numeric alignment, localization and fallback stress.
- Color needs realistic surface/state/navigation/focus/data-density contexts for semantic-color validation.
- Web Design needs grouping, density, responsive logic, navigation/history, state, focus, recovery and target-geometry evidence.

## Cross-domain opportunities

### Type

High-value next transfers:

- load T004/T005 evidence into L002 compact/intermediate/spacious data surfaces;
- test Korean/Latin fallback, real numeric alignment, long route labels and enlarged text;
- distinguish Layout wrapping failure from Type metric/fallback failure.

### Color

High-value next transfers:

- hold L002 geometry constant while varying C002/C003 luminance/chroma/state roles;
- run I001 current-location/focus/pending/error/success under C001 override conditions;
- detect semantic collisions between data color and interaction state.

### Web Design

Immediate transfer targets:

1. Study 006 / Exercise 007 — intrinsic sizing, actual font metrics, localization, zoom and narrow containers;
2. Study 014 — grouping/containment in complete page/component systems;
3. L001 — border ownership, mass and optical centering at real browser/device sizes;
4. L002 — reproduce the 216-condition density matrix using actual browser zoom, project typography, real components and page constraints;
5. Study 015 + I001 — Back/Forward, Up, Close/Escape, focus restoration, drafts, async recovery, top-level workspace and deep-link entry;
6. shared accessibility geometry — native semantics and actual target/focus behavior.

## Active next queue

Research remains ACTIVE. Expected-value priorities:

1. **L002 human task validation** — use matched preserve/adaptive variants for known-item search, comparison and action selection; record objective performance separately from preference/workload. Do not infer human performance from geometry.
2. **Type→Layout transfer** — rerun L002 with actual T004/T005 typography/fallback evidence when suitable artifacts are available.
3. **Color→Layout transfer** — hold geometry fixed and vary Color-defined luminance/chroma/state conditions to separate color-driven from spatial clutter.
4. Extend I001 only where evidence value is high: real router/URL, assistive technology, real network conflict and representative interruption/resumption.
5. Convert L001 into stronger controlled observer/raster evidence.
6. Consume future `W###` work and independently reproduce high-risk Web results when useful.
7. Open `L003` or `I002` only when a genuinely new question has higher expected value than the current validation gaps or a live project requires it.

## Open research-quality gaps

- human search/comparison/action evidence for density variants and preference/performance separation;
- controlled human-observation evidence for grouping, figure-ground, balance and optical centering;
- real rendered/device validation of optical corrections;
- actual browser zoom and broader localization/data stress beyond the controlled L002 surrogate;
- actual T004/T005 font/fallback transfer into density surfaces;
- Color transfer with geometry held constant;
- cross-surface systems across phone/tablet/desktop;
- actual router/URL navigation beyond same-document controlled history;
- screen-reader/assistive-technology validation;
- cross-browser/device mixed-input validation;
- real network abort/timeout/conflict/duplicate-submission behavior;
- interruption/resumption evidence on representative product tasks;
- stronger integration with future Web evidence.

## Handoffs to other specialists

### Typography / Type

- L002 now supplies a reproducible density/reflow matrix rather than placeholder rectangles.
- Long Korean labels materially change row-height and wrap cost.
- T004/T005 can be transfer-tested inside the compact/intermediate/spacious surfaces, especially numeric alignment and fallback.
- Scope limit: current specimen uses system-font browser rendering and does not validate Type internals.

### Color

- L002 now supplies fixed geometry for future color-driven clutter tests.
- Hold the adaptive geometry constant while varying luminance/chroma/state roles from C002/C003.
- I001 current-location/focus/error/pending/success remains a C001 forced-colors transfer target.
- Scope limit: no Color override/environmental validation was performed in the L002 block.

### Web Design

- `L002-density-validation-specimen.html` and harness provide a reproducible **216-condition density/reflow transfer matrix**.
- Web should reproduce it with actual browser zoom, project fonts, real design tokens/components, localization, framework containers and representative dashboard/form/table contexts.
- `I001-navigation-state-validation-specimen.html` remains the reusable **14-assertion navigation/state transfer matrix**.
- Return browser/page-system limitations explicitly rather than silently adapting behavior.

### Layout / Interaction

Internal revisions from current practice:

- compactness must not be credited when it is achieved through lost content or reduced required target geometry;
- required interaction geometry and semantic content are separate from discretionary whitespace;
- spacious/intermediate modes may compress absolute gaps under extreme constraints while preserving their relational hierarchy;
- density tokens should be treated as bounded relationships plus recomposition rules, not immutable pixels;
- human task efficiency remains unproven until observed.

## Handoff rule

If another specialist requests Layout/Interaction evidence, answer with canonical evidence or new investigation as appropriate. Do not silently replace peer ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `I001` source framework and controlled 14-assertion running validation are complete at CRITIQUE evidence level.
- `L002` source framework plus **216-condition naive → preserve → adaptive Chromium validation** are complete.
- `Whitespace / density / spatial rhythm` advanced from `IN STUDY` to **PRACTICE / CRITIQUE**.
- Layout next new-study ID remains `L003`; Interaction remains `I002`.
- No PASS promotion claimed. Highest-value L002 evidence gap is now human task validation, not another spacing variant.
