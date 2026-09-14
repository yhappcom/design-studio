# Web Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/web/`  
Next new-study ID: `W002`

## Operational mission

The Web Design Specialist exists to **design real websites and web applications**, not merely to implement other specialists' decisions and not to study frontend engineering as an end in itself.

Its primary responsibility is to turn product goals, user tasks, information, brand direction, and Design Studio research into complete web experiences with strong visual hierarchy, responsive behavior, coherent components, usable interaction, accessibility, and production realism.

Frontend knowledge is a supporting professional capability for prototyping, feasibility judgment, implementation fidelity, browser validation, and preservation of design intent.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The initial Web-specific baseline has now been established through `W001`. The specialist is no longer in onboarding/synchronization state.

W001 provides a medium-level model of the Web, a cross-specialist transfer frame, a bounded Chromium failure→revision exercise, an initial Web failure taxonomy, and an operational project method. It does **not** yet establish complete competency in page composition, navigation, component systems, forms/data surfaces, accessibility, browser/device transfer, or production design.

---

## Canonical Web evidence

### W001 — Web as a Native Medium: History, Flexibility, and Design Contracts

- `research/web/W001-web-as-native-medium-history-flexibility-design-contracts.md`
- `research/web/W001-web-medium-resilience-specimen.html`
- `research/web/W001-web-medium-resilience-playwright.py`
- `research/web/W001-web-medium-resilience-results.json`

Evidence level: **PRACTICE + CRITIQUE / Foundation baseline established / NOT PASS**.

### W001 retained judgment

The Web is modeled as:

`addressable resource`
`→ semantic document / task structure`
`→ source order + browser-native behavior`
`→ normal flow / intrinsic content geometry`
`→ authored hierarchy, layout, type, color, surfaces`
`→ conditional adaptation`
`→ application state and enhancement`
`→ browser/user override + runtime rendering`
`→ validation under real content, input, device, failure and accessibility conditions`.

Primary design consequence:

> Web Design should control relationships, priorities, constraints, states, and adaptation rules more strongly than exact coordinates.

This does not reject precision, fixed dimensions, absolute positioning, custom controls, or dedicated compositions. It rejects using those mechanisms where the product actually requires variable-content relationships or browser-native behavior.

### W001 historical/standards baseline

Revalidated 2026-09-15:
- CERN history of the Web;
- HTML / WHATWG document and application model;
- CSS1/CSS2 historical separation and expansion of presentation;
- DOM Level 1 and ECMAScript historical application transition;
- W3C Device Independence Principles;
- Responsive Web Design historical framing;
- current Media Queries, Flexbox, Grid, CSS Sizing and Container Queries;
- WCAG Reflow;
- WAI table/layout guidance.

Historical influence was used to explain current design constraints, not as authority for modern implementation details where current standards exist.

---

## W001 browser practice

A controlled specimen compared two transfers of comparable semantic content:

1. **fixed-canvas failure**
   - fixed 960px shell;
   - fixed hero height/columns;
   - fixed preview geometry;
   - absolutely positioned action group;
   - no narrow-width recomposition.

2. **web-native revision**
   - bounded fluid inline size;
   - normal-flow actions;
   - wrapping navigation/actions;
   - Grid `auto-fit` + `minmax()`;
   - intrinsic/flexible geometry;
   - fluid padding;
   - content wrapping.

Engine: Chromium through Playwright using `set_content` because the execution environment blocked browser navigation to local file/HTTP URLs.

Tested viewports:
- 1280 CSS px;
- 768 CSS px;
- 320 CSS px.

### Bounded result

Fixed transfer:
- 1280: no viewport overflow;
- 768: 960px shell caused horizontal document overflow;
- 320: horizontal overflow and not all primary actions remained within the viewport.

Web-native revision:
- 1280: fit;
- 768: fit;
- 320: fit;
- primary actions remained within viewport at all three tested widths.

Author CSS removed at 320 CSS px:
- no horizontal overflow;
- 10/10 specimen links remained rendered;
- 4/4 specimen headings remained rendered.

All intended bounded assertions passed.

### What W001 does not prove

No claim of:
- universal superiority of fluid layouts;
- universal 320px-fit requirement for intrinsically two-dimensional content;
- WCAG conformance;
- actual 400% browser-zoom behavior;
- keyboard/focus or screen-reader quality;
- production font loading/fallback quality;
- production localization quality;
- Firefox/Safari/physical mobile parity;
- human preference or task-performance superiority.

Those remain separate validation gates.

---

## W001 failure taxonomy

### A. Canvas transplant failure

A reference screenshot is preserved while content/viewport variation breaks the product because coordinates were specified where relationships/constraints were required.

### B. Device-folklore responsiveness

Breakpoints are selected from assumed device categories rather than actual content/layout/task stress.

### C. Visual-semantic inversion

Semantic/source order or browser behavior is distorted solely to reproduce a visual arrangement.

### D. Author-control illusion

The design assumes exact fonts, colors, dimensions, pointer input, or uninterrupted resources and omits valid browser/user/runtime participation.

### E. App exceptionalism

A web application treats URLs, history, document semantics, native controls, or focus as irrelevant because it is “an app.”

### F. Screenshot-only QA

Pixel similarity is treated as proof of interaction, semantics, focus, navigation, overflow, loading, or accessibility correctness.

---

## Current Web Design method

W001 establishes this working sequence for major surfaces:

1. purpose and user task;
2. resource/context and direct-entry behavior;
3. content model;
4. semantic/source order;
5. browser-native baseline;
6. relationship model;
7. intrinsic geometry;
8. constraints;
9. adaptation/recomposition;
10. enhancement and state;
11. stress under real content/preferences/failure;
12. browser/device/human validation at the evidence level the claim requires.

This is a diagnostic framework, not a mandatory waterfall.

---

## Peer evidence currently affecting Web

### Typography / Type

Type is through **T014** at the latest Web synchronization.

Highest-value incoming contracts:
- loading/failure/script/user-substitution fallback are distinct;
- exact font metrics and normalization/subset closure can alter actual browser layout;
- Web must validate delivered WOFF2, font loading/fallback, Korean/English wrapping, zoom/DPR, normalization, and browser/platform behavior.

W001 consequence:
- page structure and core actions should not depend on one exact font metric realization.

### Color

Color is through **C012** at the latest Web synchronization.

Highest-value incoming contracts:
- authored color is not always final used color;
- forced-colors can remove/replace visual channels;
- semantic color, wide-gamut delivery, chart/SVG behavior and browser/device color management require Web transfer.

W001 consequence:
- final Web presentation is a browser/user/runtime negotiation rather than exclusive author pixel ownership.

### Layout / Interaction

Layout/Interaction is through **L006 / I004** at the latest Web synchronization.

Highest-value incoming contracts:
- responsive systems preserve semantic relationships rather than coordinates;
- density is task-dependent;
- type/color can change perceived or actual geometry;
- visual, pointer, active gesture, focus, semantic/AT, data, stack and restoration ownership are separate;
- screenshot QA cannot validate these behavioral layers;
- history/focus restoration, pending/retry, forced-color state resilience, and concurrent conflict/recovery have controlled evidence awaiting full Web product transfer.

W001 consequence:
- later Web studies must integrate spatial and behavioral contracts into complete page systems rather than isolated components.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Web as a medium / historical evolution | **PRACTICE / CRITIQUE** | broader browser/device/project transfer; human evidence where relevant |
| Document/semantic vs presentation model | **PRACTICE / CRITIQUE** | production semantic/source-order and accessibility-tree transfer |
| Responsive/adaptive design philosophy | **PRACTICE / CRITIQUE** | W002/W003 deeper layout/recomposition, zoom, localization, cross-browser/device proof |
| Normal flow / intrinsic geometry | **PRACTICE / CRITIQUE baseline** | deeper Grid/Flex/intrinsic sizing/composition evidence |
| Information architecture / page hierarchy | NOT YET WEB-BASELINED | complete Web-specific study/practice required |
| Navigation / wayfinding | NOT YET WEB-BASELINED | real URL/router/history/direct-entry patterns required |
| Page composition / visual hierarchy / density | **NEXT** | W002 |
| Component/page systems | NOT YET WEB-BASELINED | variants/states/tokens/templates + project transfer |
| Forms/search/tables/dashboards/settings | NOT YET WEB-BASELINED | task-specific pattern and browser-native/custom decisions |
| Web interaction/state systems | INCOMING PEER EVIDENCE ONLY | complete Web page/product transfer required |
| Web typography | INCOMING TYPE EVIDENCE ONLY | exact delivered-font/browser/fallback/zoom practice required |
| Web color/theme/state | INCOMING COLOR EVIDENCE ONLY | real page/browser/device/forced-color practice required |
| Accessibility / zoom / localization | PARTIAL BASELINE | reflow concept only; semantics, keyboard, AT, real zoom, language stress open |
| Performance-sensitive design | NOT YET WEB-BASELINED | runtime-cost/design trade-off study required |
| Design-to-code/browser validation | **PRACTICE baseline** | broader cross-browser/device/production methods required |

---

## Active next queue

### 1. W002 — Page Composition, Flow, Grid, Density & Visual Hierarchy

Highest-priority next integrated block.

Required scope:
- normal flow as a design baseline, not a coding detail;
- intrinsic sizing and content-driven geometry;
- block/inline flow and writing-direction implications;
- Flexbox vs Grid vs ordinary flow by relationship type;
- fixed, fluid, min/max/clamp constraints;
- page/container measure and readable/content widths without universal constants;
- alignment systems and visual hierarchy;
- whitespace, density and rhythm using Layout L002 rather than “more whitespace is better”;
- full-bleed vs constrained content regions;
- section composition and page-level rhythm;
- simultaneous comparison vs sequential stacking;
- cards, split layouts, sidebars and multi-column structures as task relationships rather than pattern catalogues;
- long Korean/English content and font-metric stress;
- actual zoom/reflow distinction;
- browser-rendered failure→revision practice;
- explicit reasons to choose ordinary flow, Flexbox, Grid, positioning, or local overflow.

W002 must **not** become a CSS feature catalogue. The output must improve page-design judgment.

### 2. W003 candidate — Responsive / Adaptive Recomposition

After W002 geometry is grounded:
- layout stress points;
- media vs container query decision;
- component-local adaptation;
- priority changes vs hiding;
- navigation/table/form/dashboard recomposition;
- zoom/text growth/localization/device/input transfer.

### 3. Later Foundation blocks

- IA / navigation / wayfinding;
- components / page systems / design systems;
- forms, search, tables, dashboards and data-dense surfaces;
- browser-native vs custom controls;
- async/loading/error/empty/partial states;
- integrated Web typography and Color transfer;
- accessibility and actual AT/browser/device validation;
- performance-sensitive design;
- one or more complete website/web-app design/redesign exercises.

---

## Open research-quality gaps

- Firefox/Safari and physical iOS/Android browser evidence;
- actual browser zoom rather than narrow viewport proxy;
- long Korean/English production content and localization stress;
- exact delivered webfont loading/fallback/normalization transfer;
- forced-colors and actual OS high-contrast transfer;
- real keyboard/focus/screen-reader behavior;
- routed URL/history/direct-entry/resume evidence;
- native/custom control comparison;
- image/media/aspect-ratio composition under real content;
- responsive tables/forms/navigation/dashboards;
- performance/loading effects on visual hierarchy and interaction;
- real project design exercises;
- human comprehension/search/comparison/task evidence where claims require it.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

W001 supports T001's project-level premise: Web layouts should not require exact preferred-font metrics to preserve core structure/actions. Future W work should validate exact delivered fonts, Korean/English reflow, fallback, loading, normalization and actual browser zoom.

### Color

W001 incorporates C001's broader implication that browser/user participation can change final presentation. Future Web specimens should combine responsive geometry with forced colors and system-color behavior rather than treating geometry and color resilience as independent forever.

### Layout / Interaction

W001 browser practice provides a bounded Web confirmation of the relationship-over-coordinate direction. It does not replace L002/L003/L006 or I-series evidence. W002 will deepen actual page composition; later Web studies must carry focus/history/layer/state contracts into complete page systems.

---

## Latest checkpoint

- Initial repository synchronization: complete.
- First substantive Web study: **W001 complete at PRACTICE + CRITIQUE**.
- First reproducible Web browser specimen/harness/results: committed.
- Foundation baseline: **established but NOT PASSED**.
- Next new-study ID: **W002**.
- Current next major work: **Page Composition, Flow, Grid, Density & Visual Hierarchy**.
