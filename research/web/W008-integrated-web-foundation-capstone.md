# W008 — Integrated Web Foundation Capstone: Resource Workspace, Alternatives & Transfer Contracts

Status: **PRACTICE / CRITIQUE — COMPLETE-PROJECT FOUNDATION CAPSTONE**  
Evidence intent: **INTEGRATION + TRANSFER VALIDATION + PROJECT-LIKE PRACTICE**  
Date: 2026-09-15

## PURPOSE

W001–W007 established Web-specific foundations in separate blocks. W008 tests whether those findings can be combined into one coherent product surface rather than remaining isolated notes.

Controlled project: a portfolio-tracking Web workspace in which a user can:

- arrive directly at a portfolio or holding URL;
- understand current location and portfolio context;
- compare holdings in a dense table;
- search/filter without losing criteria context;
- inspect a selected holding;
- edit a bounded setting/annotation;
- refresh one data region without blanking the whole page;
- distinguish empty, stale, pending, failed and outcome-unknown states;
- continue the task across wide and narrow allocations;
- preserve truthful hierarchy while resources/fonts/data resolve progressively.

This is not a MintTap production specification and does not claim user validation. It is a controlled project-like exercise intended to test Web Foundation integration.

---

## RELATED DOMAIN CHECK

### Type

Checked `progress/TYPE_STATUS.md`, especially T016 and Type Study 009.

Reused findings:

- typography participates in information architecture;
- preferred-loaded, fallback-visible and preferred-failed states can produce different geometry;
- long Korean/English labels and numeric columns must not depend on one exact preferred-font realization.

Transfer decision: page regions use content-driven height, wrapping and bounded table overflow. The capstone does not claim exact production-font calibration.

### Color

Checked `progress/COLOR_STATUS.md` through C015 Stage 1 PASS.

Reused findings:

- hierarchy must survive grayscale;
- state semantics cannot rely on hue alone;
- attractive swatches are not evidence of semantic fitness;
- contrast is a pair/context property rather than a token property.

Transfer decision: the specimen uses text, structure, labels and borders for status before authored color. No production gamut/device PASS is claimed.

### Layout / Interaction

Checked `progress/LAYOUT_STATUS.md`, especially L002/L003/L006 and I001/I002/I004/I005.

Reused findings:

- responsive design preserves relationships rather than coordinates;
- visual, pointer, focus, semantic and data ownership can diverge;
- location, hierarchy, traversal history and focus are different contracts;
- pending, failed and outcome-unknown are distinct;
- retry safety depends on operation semantics rather than button styling.

Transfer decision: the capstone uses region-owned async states, stable resource identity, explicit current-location cues and native controls where possible.

### Web

Checked W001–W007.

- W001: browser-participatory medium.
- W002: flow/grid/density and local 2-D overflow.
- W003: adaptation ownership.
- W004: resource identity, URL, navigation, direct entry.
- W005: native semantics, independent state dimensions, component/page boundaries.
- W006: complete task-surface state/recovery ownership.
- W007: temporal priority, first truthful state, interaction readiness.

### Overlap classification

**INTEGRATION + TRANSFER VALIDATION.** W008 deliberately repeats earlier contracts in one complete surface to test whether they remain mutually coherent when combined.

---

## CURRENT SOURCE CHECK — 2026-09-15

Current WHATWG HTML still treats hyperlinks as connections to resources and defines navigation/session-history behavior independently from visual page hierarchy. Current HTML forms remain functional without client-side scripting for many tasks, with script available as enhancement. Current W3C CSS work continues to define the 2026 CSS snapshot and current layout/query modules. The W3C Web Performance Working Group continues to publish timing APIs such as Resource Timing, Paint Timing, Event Timing and Largest Contentful Paint.

These standards provide browser contracts and measurement primitives. They do not select this capstone's product architecture.

---

# 1. PROJECT QUESTION

How should a portfolio Web workspace let users **find, compare, inspect and edit holdings** while preserving:

1. direct-entry resource identity;
2. clear current location;
3. dense comparison where simultaneous columns matter;
4. narrow-screen usability without erasing comparison semantics;
5. local loading/error ownership;
6. stable state and recovery language;
7. native semantics and keyboard-reachable controls;
8. long bilingual content resilience;
9. truthful progressive rendering;
10. reusable component/page-system contracts without component-driven sameness?

---

# 2. REQUIRED PRODUCT INPUTS

The exercise fixes the following assumptions so design judgment can be evaluated:

- dominant task: compare holdings, then inspect/edit one holding;
- direct links to portfolios and holdings are valuable;
- portfolio context matters on every holding view;
- filtering is reversible and shareable enough to justify URL-query consideration;
- simultaneous row/column comparison matters more than eliminating all local horizontal scrolling;
- stale read-only data can remain visible if clearly labeled, but consequential writes require authoritative confirmation;
- human testing is deferred; no preference or task-speed claim is made.

---

# 3. THREE MATERIALLY DIFFERENT DIRECTIONS

## Direction A — Object-deep hierarchy

Structure:

`Portfolios → Portfolio → Holdings → Holding → Edit`

Design:

- strong breadcrumb and nested resource identity;
- holding detail is a separate page;
- filtering/table comparison lives mainly at portfolio level;
- edits route to a dedicated form page.

### KEEP

Use when deep object identity, sharing and auditability dominate and users rarely compare while editing.

### REWORK

If comparison context is needed during inspection, preserve a contextual summary or split workspace.

### REJECT

For this exercise, repeated route transitions create excessive context switching for the dominant compare→inspect→edit loop.

---

## Direction B — Task-domain control center

Structure:

`Overview / Holdings / Income / Tax / Settings`, with portfolio as persistent selector/filter.

Design:

- high-density task tabs;
- holdings table owns most interaction;
- detail appears in an in-page side region;
- portfolio identity is ambient state rather than route hierarchy.

### KEEP

Use when cross-portfolio task repetition dominates and users think in domains rather than objects.

### REWORK

Make portfolio identity explicit in URLs/headings if direct entry and sharing matter.

### REJECT

For this exercise, ambient portfolio context is too easy to lose on direct entry and can make copied links ambiguous.

---

## Direction C — Hybrid resource workspace **SELECTED**

Structure:

- stable portfolio/holding URLs;
- task-oriented portfolio workspace;
- holding selection opens a bounded detail region while canonical holding links remain available;
- filters can map to URL query state where sharing/reload value justifies it.

Design:

- page identity and portfolio context at route level;
- holdings comparison remains central;
- detail region owns selection/detail state;
- edit uses a native form in a bounded region/dialog only if its focus/restoration contract is preserved;
- regional refresh does not erase valid comparison data.

### KEEP

Use when object identity and fast in-context comparison are both important.

### REWORK

If route/detail synchronization becomes confusing, prefer a full detail route rather than hiding history semantics behind a drawer.

### REJECT

If users almost never compare and only work one record at a time, the hybrid workspace adds unnecessary density and state ownership.

---

# 4. EXPLICIT SELECTION CRITERIA

| Criterion | A Object-deep | B Task-domain | C Hybrid |
| --- | --- | --- | --- |
| direct-entry identity | strong | medium | strong |
| compare→inspect continuity | weak-medium | strong | strong |
| copied-link clarity | strong | medium | strong |
| dense comparison | medium | strong | strong |
| narrow recomposition | simple | moderate | moderate |
| state ownership complexity | low-medium | medium | high |
| implementation risk | low | medium | medium-high |
| fit to fixed dominant task | medium | medium | **high** |

**Selected direction: C — Hybrid resource workspace.**

Selection is not aesthetic. It wins because the fixed task requires both addressable object identity and repeated in-context comparison.

---

# 5. INFORMATION / URL CONTRACT

Canonical resource candidates:

- `/portfolios`
- `/portfolios/{portfolioId}`
- `/portfolios/{portfolioId}/holdings/{ticker}`

Shareable/reloadable view-state candidates:

- `?q=...`
- `?period=1y`
- `?sort=yield-desc`

Transient state by default:

- open filter disclosure;
- pointer hover;
- temporary validation message;
- unsaved field dirtiness;
- non-resumable edit-layer visibility.

Rule: a transient layer does not become a route merely because implementation uses a router. A stable resource does not become transient merely because it can be shown in a drawer.

Direct-entry invariant: every canonical route must identify itself, expose parent portfolio context, explain not-found/permission failure, and provide valid next navigation without assuming prior traversal.

---

# 6. PAGE / REGION OWNERSHIP

Selected page template:

1. **Global navigation** — product-level destinations.
2. **Page identity region** — portfolio name, page heading, freshness/status.
3. **Criteria region** — search, period, sort/filter controls.
4. **Summary region** — bounded KPIs; independent refresh allowed only where interpretation remains truthful.
5. **Collection region** — holdings table; owns collection loading/empty/filter-zero/error state.
6. **Detail region** — selected holding identity/details; never inferred only from row position.
7. **Mutation region** — edit form and save operation state.
8. **Page status region** — only for status whose scope is genuinely page-level.

A local refresh failure does not blank the entire page when prior valid data remains usable.

---

# 7. RESPONSIVE CONTRACT

## Wide allocation

- criteria + summary may share a row;
- collection and detail can coexist in a two-region workspace;
- table preserves simultaneous comparison.

## Medium allocation

- detail region moves below/above collection according to task priority;
- controls wrap without changing source/task order;
- summary cards reflow by available container space.

## Narrow allocation

- page becomes primarily sequential;
- detail is reached from explicit selection/navigation rather than an always-visible side pane;
- dense table retains local horizontal overflow if stacking columns would destroy comparison semantics;
- global navigation may collapse, but destination identity/order/current-state semantics remain.

Invariant: responsive adaptation changes presentation/availability of space, not resource identity, state semantics or source-order logic without explicit justification.

---

# 8. COMPONENT / SEMANTIC CONTRACT

Use native semantics first:

- links for navigation to resources;
- buttons for commands;
- form controls for search/filter/edit input;
- table markup for genuinely tabular comparison;
- headings/landmarks for page/region structure.

Independent state dimensions remain independent:

- focus;
- selected holding;
- expanded filter controls;
- form validity;
- pending save;
- stale data;
- permission restriction;
- outcome unknown.

Do not encode all of these as one visual `state` variant.

---

# 9. COMPLETE STATE MATRIX

| Scope | State | Required truthful presentation | Unsafe shortcut |
| --- | --- | --- | --- |
| route | unresolved | identify acquisition/loading without claiming empty | render empty portfolio |
| collection | empty | valid zero-state + next action | generic error |
| collection | filtered-zero | preserve criteria + clear/revise path | onboarding empty-state copy |
| collection | stale | retain data + freshness label | silently present as current |
| collection | refresh failed | preserve valid prior content + retry | replace whole page with error |
| detail | not selected | explain selection affordance | show arbitrary first row as selected |
| detail | not found | preserve portfolio context | generic blank panel |
| edit | locally invalid | specific correction + preserved input | red border only |
| save | pending | operation accepted, prevent unsafe duplicate semantics | pretend success |
| save | known failure | correction/safe retry path | clear form |
| save | outcome unknown | state uncertainty explicitly; reconcile before duplicate-sensitive retry | “Save failed” as fact |

---

# 10. TYPE TRANSFER

Typography roles:

- page identity;
- portfolio context;
- primary numeric value;
- table header/value/meta;
- control label/helper/error;
- stale/pending/error status.

Stress conditions:

- long Korean portfolio names;
- English financial labels;
- large numeric values;
- preferred webfont loading;
- fallback-visible and preferred-failed states.

Design response:

- no fixed-height text containers for content whose role allows wrapping;
- numeric alignment is preserved where comparison requires it;
- fallback geometry must not hide/truncate primary actions;
- exact production font metrics remain a later project validation gate.

---

# 11. COLOR TRANSFER

Foundation rule:

1. establish hierarchy in structure/typography/spacing first;
2. use color to reinforce roles;
3. ensure state remains understandable without hue;
4. validate actual text/non-text pairs in the final theme/browser/device context.

Example states use icon/text/border/position plus color, not color alone:

- stale — “Last confirmed 09:41” + status mark;
- pending — “Saving…” + progress/status text;
- invalid — specific error text linked to field;
- destructive — explicit command language plus visual treatment.

No wide-gamut/device-environment PASS is inferred from this capstone.

---

# 12. PERFORMANCE / TEMPORAL COMPOSITION

First truthful task state should prioritize:

1. page/portfolio identity;
2. primary navigation and criteria controls;
3. last confirmed or initial holdings structure/state;
4. critical comparison content;
5. detail enrichment;
6. tertiary visualization/media.

Controls must not look ready before they are operable. Late font/data/media insertion must not casually displace the active task. Stable dimensions and content-driven layout should be used where known/appropriate.

Measurement candidates for later executable transfer:

- request/resource timing by region dependency;
- primary-control visible-and-operable time;
- layout shift around font/data enrichment;
- focus continuity during detail/refresh updates;
- route/history behavior during selection/filter changes.

No measured timing result is claimed here.

---

# 13. FAILURE → REVISION CRITIQUE

## Failure A — screenshot-perfect fixed workspace

Problem: fixed two-column geometry works at one desktop width but overflows or hides actions with bilingual text.

Revision: relationship-driven Grid/flow, `min-width:0`, wrapping, bounded local table overflow and narrow sequential recomposition.

## Failure B — global spinner

Problem: refreshing one KPI blanks valid table/detail context.

Revision: region-owned pending/failure where semantic independence is real.

## Failure C — drawer as fake route

Problem: selected holding appears in a drawer but URL/history/direct entry do not represent the resource, so Back/Forward and copied links lie about current context.

Revision: either synchronize stable resource identity intentionally or keep the layer explicitly transient and provide a canonical detail link.

## Failure D — generic gray unavailable controls

Problem: native disabled, permission denied, pending and not-applicable all look identical.

Revision: preserve distinct product semantics and appropriate discoverability/action/recovery.

## Failure E — performance-first hiding

Problem: critical comparison columns/context are removed solely to improve rendering or narrow fit.

Revision: reduce resource/layout cost without changing task truth; preserve local 2-D comparison when it is intrinsically necessary.

---

# 14. ORIGINAL PRACTICE OUTPUT

W008 provides an original integrated design exercise rather than only definitions:

- one fixed task model;
- three materially different complete architecture directions;
- explicit KEEP/REWORK/REJECT conditions;
- explicit selection criteria;
- selected page/region ownership model;
- URL/direct-entry model;
- responsive transfer rules;
- component/native-semantics model;
- complete state matrix;
- Type/Color transfer;
- performance/temporal contract;
- failure→revision critique;
- accompanying HTML specimen: `W008-integrated-web-foundation-capstone-specimen.html`.

---

# 15. PROJECT-READINESS TEST

### When this knowledge should be used

Use for task-oriented Web products with addressable resources, data comparison, filters/search, local mutations and responsive requirements.

### When it should not be used unchanged

Do not impose this workspace architecture on editorial/marketing sites, single-step forms, intrinsically canvas-like tools, or products whose task/state semantics differ.

### Inputs required

- dominant tasks and context-switch frequency;
- stable resource identities;
- direct-entry/sharing/history requirements;
- data density/comparison needs;
- state/freshness/retry semantics;
- target content/languages/fonts;
- browser/device/input constraints;
- performance/resource dependencies.

### Concrete decisions changed

- route vs transient state;
- page vs region state ownership;
- table overflow vs stacked cards;
- full-page vs in-context detail;
- native primitive vs custom behavior;
- progressive rendering order;
- what must be validated in browser/project transfer.

---

# 16. FOUNDATION GATE IMPLICATION

W008 materially closes the previous **complete-project integration** gap. It demonstrates that W001–W007 can be combined into a coherent project-like design with original alternatives, critique and peer evidence reuse.

However, W008 does **not by itself declare Web Stage 1 PASS**.

A separate explicit closure audit should now map the exact Master Curriculum Stage 1 gate against W001–W008 and decide whether any genuine Foundation requirement remains, while keeping later browser/platform/human/production gaps in their correct stages.

---

## OPEN

- executable integrated browser harness for W008/W003–W007 contracts;
- actual route/history/direct-entry behavior;
- keyboard/focus and accessibility-tree validation;
- exact preferred/fallback font transfer across the complete page;
- forced-colors/system-color transfer;
- actual browser zoom and larger localization corpus;
- Firefox/Safari/physical mobile transfer;
- measured performance/resource/readiness evidence;
- live-project data/backend semantics;
- human findability/comparison/task evidence, deferred to project/app stage.

These are not silently promoted to Foundation blockers without the closure audit checking the exact curriculum boundary.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type

The capstone consumes T016 as a page-level geometry/stability dependency. Future project validation should provide exact delivered font/fallback pairs and long Korean/English content rather than generic font assumptions.

### Color

The capstone preserves state semantics structurally before color. Production theme/forced-color/device checks should validate the selected project's actual palette rather than this controlled specimen.

### Layout / Interaction

The capstone transfers responsive relationship ownership, navigation/history separation and regional async/recovery state into a complete Web workspace. Any future browser harness should return contradictions to L/I if real page behavior exposes ownership/focus/history failures.

---

## EVIDENCE LEVEL

**SOURCE + SYNTHESIS + ORIGINAL PRACTICE + CRITIQUE + INTEGRATION + TRANSFER VALIDATION.**

No browser/device/human PASS is claimed. The next appropriate Web step is an explicit **Stage 1 Foundation closure audit**, not another unrelated Foundation topic.