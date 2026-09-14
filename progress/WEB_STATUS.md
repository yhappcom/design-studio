# Web Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/web/`  
Next new-study ID: `W003`

## Operational mission

The Web Design Specialist exists to design real websites and web applications, not merely implement peer decisions or study frontend engineering for its own sake.

Its responsibility is to turn product goals, user tasks, information, brand direction, and Design Studio evidence into complete web experiences with strong hierarchy, responsive behavior, coherent components, usable interaction, accessibility and production realism. Frontend knowledge is a supporting capability for prototyping, feasibility judgment, implementation fidelity and browser validation.

---

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

Web now has two substantive canonical studies:

- `W001` establishes the Web as a flexible/browser-participatory medium and a relationship-over-coordinate baseline.
- `W002` establishes page-composition mechanism judgment and adds a reproducible Chromium failure→revision validation across wide, threshold, narrow, bilingual-long-content and text-growth stress cases.

This is materially stronger than the previous W001-only baseline, but Web remains the least complete Stage 1 specialist because major Foundation areas are still not Web-baselined: information architecture, navigation/wayfinding, component/page systems, forms/search/tables/dashboard patterns as complete task systems, web interaction/state integration, and broader accessibility/browser/device transfer.

---

## Canonical Web evidence

### W001 — Web as a Native Medium

Canonical:

- `research/web/W001-web-as-native-medium-history-flexibility-design-contracts.md`
- `research/web/W001-web-medium-resilience-specimen.html`
- `research/web/W001-web-medium-resilience-playwright.py`
- `research/web/W001-web-medium-resilience-results.json`

Evidence level: **PRACTICE + CRITIQUE**.

Retained model:

`addressable resource`
`→ semantic document/task structure`
`→ source order + browser-native behavior`
`→ normal flow/intrinsic geometry`
`→ authored hierarchy/layout/type/color`
`→ conditional adaptation`
`→ application state/enhancement`
`→ browser/user/runtime participation`
`→ validation under real content/input/device/failure/accessibility conditions`.

Primary design consequence:

> Web Design should control relationships, priorities, constraints, states and adaptation rules more strongly than exact coordinates.

W001 browser practice showed a fixed 960px/canvas-style transfer failing at narrower widths while an intrinsic/fluid revision preserved the document and primary actions across controlled Chromium widths. It did not claim WCAG, cross-browser, font-loading or human PASS.

### W002 — Page Composition, Flow, Grid, Density & Visual Hierarchy

Canonical:

- `research/web/W002-page-composition-flow-grid-density-hierarchy.md`
- `research/web/W002-page-composition-specimen.html`
- `research/web/W002-page-composition-playwright.py`
- `research/web/W002-page-composition-results.json`

Evidence level: **PRACTICE + CRITIQUE / TRANSFER VALIDATION / Chromium bounded validation**.

W002 extends W001 from a general relationship-over-coordinate principle into a project decision procedure:

1. classify the relationship first;
2. identify content/runtime stress;
3. decide what may wrap/stack/reorder and what must remain aligned;
4. distinguish document-level reflow from legitimate component-local 2-D overflow;
5. only then choose ordinary flow, Flexbox, Grid, positioning, sizing constraints or local overflow.

Three materially different directions were produced for the same investment-tracking content:

- sequential editorial;
- comparison workspace;
- dense data with local 2-D preservation.

Each includes KEEP / REWORK / REJECT conditions. Direction B remains the default STUDIO JUDGMENT for a general tracker, not a human-performance result.

---

## Latest completed block — W002 browser validation

Engine: Chromium `144.0.7559.96` via Playwright.

Controlled cases:

1. 1280px normal;
2. 768px normal;
3. 320px normal;
4. 320px + long bilingual English/Korean content;
5. 320px + long bilingual content + controlled 200% text-size stress.

Assertions covered:

- no unintended document-level horizontal overflow;
- expected two-column vs one-column workspace relation;
- expected table-local overflow state;
- semantic table/header structure retained;
- stable source/focusable sequence.

### Failure → revision

Initial `320px + 200% text` stress produced unwanted document overflow (`420px` scroll width against a `320px` client width).

The specimen was revised with:

- `overflow-wrap:anywhere` for emergency heading/paragraph break opportunities;
- `min-width:0` on relevant Grid/Flex children so intrinsic minimums do not force ancestor expansion.

The harness also corrected one false assumption: at 768px the table is already narrower than its intrinsic minimum, so local overflow is expected and semantically valid even while the comparison workspace remains side-by-side.

### Final result

**25/25 bounded assertions true across 5/5 cases.**

Representative measurements:

- 1280px: document fits; comparison workspace remains ~697px + 336px; table fits without local overflow.
- 768px: document fits; workspace remains ~362px + 288px; table scrolls locally (`729px` content inside `674px`).
- 320px: document fits; workspace stacks to `254px`; table remains local overflow (`729px` inside `254px`).
- 320px long bilingual: no document overflow.
- 320px long bilingual + 200% text: after revision, document returns to `320/320`; table expands internally to ~1330px but remains inside the local scroll region.

This is not browser-UI 400% zoom proof, WCAG conformance, screen-reader PASS, Firefox/Safari parity or human validation.

---

## Peer evidence currently affecting Web

### Typography / Type

Type is through T016. Highest-value incoming contract: exact font/loading/fallback geometry can change wrapping and downstream page layout. W002 transfers that principle but does not yet reproduce downloadable-font lifecycle behavior inside the complete page.

### Color

Color Stage 1 is PASS. Web should apply Color after structural hierarchy exists and later test semantic/theme/state behavior in actual browser/user override conditions.

### Layout / Interaction

Layout/Interaction Stage 1 is PASS and now entering Stage 2 audit. W002 directly reuses L002 density/rhythm, L003 Type-dependent reflow and L006 ownership principles. W002 returns Web-specific evidence that separate relationship classes can require different stress thresholds: the table enters local overflow at 768px while the comparison workspace remains side-by-side.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Web as a medium / historical evolution | PRACTICE / CRITIQUE | broader project/browser/device transfer |
| Document/semantic vs presentation model | PRACTICE / CRITIQUE | accessibility-tree/production source-order transfer |
| Responsive/adaptive philosophy | PRACTICE / CRITIQUE | W003 deeper recomposition, actual zoom, component-local adaptation |
| Normal flow / intrinsic geometry | PRACTICE / CRITIQUE | broader content/media/form systems |
| Page composition / hierarchy / density | **PRACTICE / CRITIQUE — W002** | cross-browser/device + real project/human evidence |
| Information architecture / page hierarchy | NOT YET WEB-BASELINED | dedicated Web practice required |
| Navigation / wayfinding | NOT YET WEB-BASELINED | URL/router/history/direct-entry/wayfinding practice |
| Component/page systems | NOT YET WEB-BASELINED | variants/states/tokens/templates + project transfer |
| Forms/search/tables/dashboards/settings | PARTIAL via W002 table only | complete task-specific browser-native/custom practice |
| Web interaction/state systems | INCOMING PEER EVIDENCE ONLY | complete page/product transfer required |
| Web typography | PARTIAL TRANSFER | exact delivered-font loading/fallback/zoom practice required |
| Web color/theme/state | INCOMING COLOR EVIDENCE ONLY | real page/browser/device/forced-color practice |
| Accessibility / zoom / localization | PARTIAL PRACTICE | actual browser zoom, keyboard/AT, language stress beyond specimen |
| Performance-sensitive design | NOT YET WEB-BASELINED | runtime-cost/design trade-off study |
| Design-to-code/browser validation | PRACTICE | Firefox/Safari/physical device/production methods |

---

## Current next queue

### 1. W003 — Responsive / Adaptive Recomposition

Highest-value next integrated Foundation block unless a newer repository state changes the balance.

Required questions:

- detect layout stress from content/task failure rather than device folklore;
- media query vs container query by ownership/relationship;
- component-local vs page-global adaptation;
- preserve priority while stacking/wrapping/hiding/reordering;
- navigation, table, form and dashboard recomposition;
- long Korean/English strings;
- exact Type loading/fallback transfer where executable;
- actual browser zoom distinct from viewport and text-size proxies;
- source/focus order under visual rearrangement;
- mixed input implications.

W003 must remain design-led; it should not become a query-syntax catalogue.

### 2. IA / navigation / wayfinding

After or alongside responsive foundations, establish URL/resource hierarchy, direct entry, navigation models, history/resume and wayfinding as complete Web design decisions.

### 3. Component/page systems and task surfaces

Build Foundation evidence for forms, search, filters, settings, tables, dashboards, list/detail, loading/error/empty/partial states and browser-native vs custom controls.

### 4. Integrated Web Type / Color / accessibility

Transfer exact delivered fonts, themes/system colors, forced colors, real zoom, keyboard/focus/AT and cross-browser/device behavior into complete page systems.

---

## Open research-quality gaps

- actual browser-UI zoom rather than viewport/text-size proxy;
- Firefox/Safari and physical iOS/Android browser evidence;
- routed URL/history/direct-entry/resume evidence;
- navigation/wayfinding baseline;
- component/page-system baseline;
- forms/search/filter/settings/dashboards as complete task systems;
- exact downloadable webfont loading/fallback/normalization in full page context;
- forced-colors and real OS high-contrast transfer;
- real keyboard/focus/screen-reader behavior;
- native/custom control comparison;
- image/media/aspect-ratio composition;
- performance/loading effects on hierarchy and interaction;
- complete real-project design/redesign exercise;
- human comprehension/search/comparison/task evidence where claims require it.

Human evidence is not fabricated and remains project-stage work when suitable participants/context exist.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

W002 adds a project-level text-growth failure→revision case and confirms that page resilience requires more than one preferred-font screenshot. Exact downloadable-font lifecycle transfer remains open.

### Color

W002 preserves structural hierarchy before chromatic reinforcement; later Web theme/state work should test whether Color strengthens or flattens that hierarchy.

### Layout / Interaction

W002 provides complete-page transfer evidence for relationship-specific breakpoints, local 2-D overflow, source/focus sequence and text-growth resilience. It supports choosing recomposition from relationship failure rather than one global device breakpoint.

---

## Latest checkpoint

- W001: PRACTICE + CRITIQUE baseline complete.
- W002: **PRACTICE + CRITIQUE with reproducible Chromium validation complete; 25/25 bounded assertions after one real failure→revision cycle.**
- Web Foundation: **NOT PASSED**.
- Next new Web study ID: **W003**.
- Current largest Web Foundation gaps: responsive/adaptive recomposition depth, IA/navigation, component/page systems, task surfaces, integrated accessibility/Type/Color and broader browser/device transfer.
