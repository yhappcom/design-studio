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

The role combines spatial composition and interaction because geometry, state, navigation, feedback, target placement and responsive behavior must form one product experience. Spatial and temporal/behavioral evidence remain separately indexed under `research/layout/` and `research/interaction/` so those claim types are not conflated.

## Four-specialist collaboration sync

Design Studio operates with four official peer specialists:

1. Typography / Type Design
2. Color
3. Layout, Spatial & Interaction
4. Web Design

Web Design is an independent design specialist and the main real-web application/validation partner for this role. Layout/Interaction provides canonical spatial and behavioral evidence; Web integrates and stress-tests it in complete page systems, responsive/browser contexts, native controls, real content, mixed input, history, loading/network, localization and implementation conditions.

At the latest synchronization point, `progress/WEB_STATUS.md` still listed `W001` as not yet begun. Do not invent Web evidence. Re-check Web status and `research/web/` before every substantial block.

## Canonical evidence already established

### Layout / spatial

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`
- `research/layout/L001-figure-ground-balance-optical-centering.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`
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

## Latest completed block — I001 running validation cycle

The I001 source framework was converted into a running HTML/JavaScript state specimen and exercised with Playwright in headless Chromium.

### Controlled scenario

- Records list → detail → edit;
- top-level Records / Reports switch;
- hierarchy `Up`;
- session-history `Back` / `Forward`;
- deep-link-style detail entry;
- dirty draft navigation;
- modal discard confirmation and `Escape`;
- route focus and modal focus restoration;
- async save pending → failure → retry → success;
- top-level workspace resumption with object identity.

### Failure → revision evidence

The first executions exposed concrete defects:

1. route focus landed on `Up` rather than route context;
2. dirty Back traversal had no explicit restorable draft policy;
3. save-success status was erased during rerender;
4. top-level restoration remembered view type but lost the semantic object;
5. focusing a heading while `Up` preceded it in DOM order caused forward-Tab skip risk;
6. Retry was incorrectly placed inside the live `role="status"` region;
7. top-level resume state could become stale after history traversal.

The specimen was revised to:

- focus the route heading on route transitions;
- align DOM order with route-focus behavior;
- preserve and restore a local draft in this controlled policy;
- preserve object identity in resumable top-level state;
- keep success status through the destination render;
- separate non-interactive live status from recovery action;
- update resumable state from the actual rendered route.

### Re-proof

The final Playwright harness executed **14/14 PASS** checks covering keyboard route entry, Tab reachability of Up, modal entry/exit focus, dirty-draft Back traversal, workspace object restoration, draft restoration, async failure/retry/success, deep-link entry, hierarchy Up and session-history Back.

Evidence level: **PRACTICE + CRITIQUE / controlled Chromium prototype evidence**.

This is not production PASS. The environment used same-document hash routing on `about:blank` because browser access to localhost/network origins was blocked. Real router/URL navigation, assistive technology, cross-browser/device, real network, localization/fallback stress and representative human resumption evidence remain open.

## Previous completed block — I001 source framework

`I001-navigation-history-focus-restoration-interruption.md` established navigation as a user-facing state model rather than a menu/arrow/animation problem.

Key distinctions:

- semantic location;
- traversal history;
- product hierarchy;
- task/work state;
- presentation state;
- focus/selection state;
- transient-layer state;
- data/commitment state;
- Back vs Up vs Close vs top-level switching;
- deep-link/context-poor entry;
- interruption/resumption and restoration validity.

## Previous spatial block — L002

`L002-whitespace-density-spatial-rhythm.md` established a task-dependent density model rather than a universal “more whitespace is better” rule.

Key distinctions:

- information density;
- visual density;
- interaction density;
- navigation/temporal density;
- local vs global density;
- whitespace as a structural resource with explicit jobs;
- progressive disclosure as an exchange of spatial density for interaction/navigation cost;
- objective task performance vs visual preference.

Controlled matched-content rendered practice and human/task evidence remain open.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; multilingual/enlarged-text/browser transfer |
| Grid / alignment systems | CRITIQUE | real-browser proof; text-growth stress; broader responsive transfer |
| Perceptual grouping | CRITIQUE | broader context validation and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants; realistic layering; blinded human comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | controlled centroid dataset; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size device proof; blinded comparison; RTL/text-context transfer |
| Whitespace / density / spatial rhythm | IN STUDY | L002 framework complete; controlled density variants; objective task evidence; localization/zoom/browser/human validation |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | real content; multilingual labels; enlarged text; browser/device proof |
| Interaction agency / feedback / errors | CRITIQUE | controlled running proof exists; broader recovery, real platform and assistive-technology validation |
| State / modes / reversibility / directness | CRITIQUE | controlled async failure/retry proof exists; broader real network/conflict/input/AT validation |
| Navigation / task-flow integration | **CRITIQUE** | I001 running Back/Up/deep-link/focus/workspace/draft proof complete; real router/URL, AT, cross-browser/device, richer interruption/resumption and human evidence pending |

## Primary ownership

### Spatial

Canonical ownership includes:

- grouping, regions, figure-ground, grid, alignment and hierarchy through geometry;
- whitespace, density, proportion, visual mass, balance and optical centering;
- responsive/adaptive recomposition, reflow and target geometry.

### Interaction

Canonical ownership includes:

- affordance/signifiers, mapping, feedback, agency and discoverability;
- actions, destinations, navigation and task flow;
- state, modes, directness, reversibility and temporal behavior;
- async/pending behavior, interruption, errors and recovery;
- keyboard/pointer/touch/gesture paths, focus-flow consequences and status communication.

Primary ownership is not a learning prohibition. Cross-domain replication, transfer validation and adjacent study are allowed when they materially improve project judgment.

## Peer evidence currently affecting Layout / Interaction

### From Type

Type now includes `T001`, `T002` and `T003`.

Most relevant current findings:

- T001: fallback and vertical metrics can change wrapping, row height, navigation-label width and reflow;
- T003: identical source metrics can produce different rendered advances/coverage depending on renderer, hinting and positioning.

Consequences for this role:

- compact density cannot be validated with placeholder rectangles or source geometry alone;
- route labels, tabs, breadcrumbs, dense rows and target placement must eventually be tested with actual renderer output, fallback and enlargement;
- a Layout failure may originate in Type/rendering, so diagnosis must preserve ownership boundaries.

### From Color

Color now includes `C001` and `C002`.

Most relevant current findings:

- C001: forced-colors/user overrides can replace or remove authored fills, shadows, borders and color channels;
- C002: primitive color values, semantic roles, component roles and context resolution should remain separate; state semantics must precede Color encoding.

Consequences for this role:

- current location, selection, focus, pending/error/success and navigation state must survive without color-only meaning;
- status and recovery action should be semantically separate before Color assigns roles;
- apparent density or mass may be partly color-driven and should not automatically be diagnosed as geometry.

### From Web Design

No substantive `W###` study was available at the latest synchronization point.

Current Web relationship remains a validation contract:

- Web should test Layout/Interaction findings in real page systems, routers, intrinsic sizing, responsive reflow, native controls, browser history, mixed input, zoom, localization and actual network/content conditions;
- Layout/Interaction should classify returned failures as theory limits, platform conventions, context dependencies, implementation mismatches or project-specific errors rather than silently rewriting principles.

## Incoming dependencies

- Type needs realistic responsive/dense contexts for text-growth, long-label, navigation and scaling stress.
- Color needs realistic surface/state/navigation/focus/error contexts for semantic-color validation.
- Web Design needs canonical grouping, hierarchy, density, responsive logic, navigation/history, focus restoration, state, feedback, recovery and target-geometry evidence.

## Cross-domain opportunities

### Type

High-value tests:

- L002 compact/intermediate/spacious layouts with actual T003 renderer output;
- navigation titles/tabs/breadcrumbs under T001 fallback and Korean/Latin long labels;
- enlarged text and narrow-container route focus/order checks.

### Color

High-value tests:

- hold geometry constant while varying luminance/chroma to separate spatial from color-driven mass/clutter;
- run I001 current-location/focus/pending/error/success states under C001 forced-color conditions;
- map I001 semantic states into C002 semantic roles without collisions such as brand = selected = success.

### Web Design

Immediate transfer targets:

1. Study 006 / responsive Exercise 007 — intrinsic sizing, real font metrics, localization, zoom and narrow containers;
2. Study 014 — grouping/containment/over-containerization in complete page/component systems;
3. L001 — border ownership, mass and optical centering at real browser/device sizes;
4. L002 — compact/intermediate/spacious task-performance comparison in dashboards/forms/settings/lists/tables;
5. Study 015 + I001 validation matrix — Back/Forward, Up, Close/Escape, route focus, modal focus restoration, dirty drafts, async failure/retry, top-level workspace restoration and deep-link entry;
6. shared accessibility geometry — native semantics and actual focus/target behavior.

## Active next queue

Research remains ACTIVE. Expected-value priorities:

1. **Convert L002 into controlled practice**: matched-content compact/intermediate/spacious variants; known-item search and comparison tasks; separate objective performance from preference; include narrow, enlarged-text and localized stress.
2. **Extend I001 validation only where evidence value is high**: real URL/router when possible, assistive technology, richer async/network conflict and human interruption/resumption. Do not create complexity merely to increase test count.
3. Convert L001 into stronger evidence with controlled centroid/border-ownership variants, intended-size raster proof and blinded comparison.
4. Test responsive/grid work with real text metrics, long labels, multilingual expansion and enlarged text using Type evidence.
5. Use C001/C002 to run state/focus/current-location transfer tests without relying on authored color.
6. Consume future `W###` findings and independently reproduce high-risk Web results when useful.
7. Open `L003` or `I002` for the next genuinely new question only when validation work or a live project no longer has higher expected value.

## Open research-quality gaps

- controlled human-observation evidence for grouping, figure-ground, balance and optical-centering;
- real rendered/device validation of optical corrections;
- controlled density variants with objective task evidence and preference/performance separation;
- responsive transfer under multilingual, enlarged-text and dense-data conditions;
- cross-surface systems across phone/tablet/desktop;
- actual router/URL navigation and browser-history transfer beyond same-document controlled history;
- screen-reader/assistive-technology validation of route headings, status, modal focus and recovery;
- cross-browser/device mixed-input validation;
- real network abort/timeout/conflict/duplicate-submission behavior;
- interruption/resumption evidence on representative product tasks;
- integration of spatial and temporal hierarchy without collapsing them into one concept;
- stronger cross-validation with real Type, Color and future Web behavior.

## Handoffs to other specialists

### Typography / Type

- I001 validation shows route titles, Up/Back/Close labels and workspace identity are part of orientation, so wrapping/fallback can become interaction failures rather than cosmetic differences.
- L002 provides compact/standard/spacious contexts for T003 renderer and T001 fallback transfer.
- Scope limit: Layout/Interaction does not select font internals or rendering strategy.

### Color

- I001 validation confirms state meaning is structurally defined before visual encoding.
- Live status and recovery action are separate semantic channels; C002 can assign Color roles without collapsing them.
- Current location/focus/error/pending/success remain strong C001 forced-colors transfer targets.
- Scope limit: no forced-color or display validation was performed in this block.

### Web Design

- `I001-navigation-state-validation-specimen.html` and the Playwright harness provide a reusable **14-assertion transfer matrix**.
- Web should reproduce it with a real router, real URLs, native/custom controls, browser/device matrix, page refresh where relevant, actual network behavior and assistive technology.
- Return confirmation, limitation, contradiction or transfer failure rather than silently adapting the behavior.
- Scope limit: current result is controlled Chromium same-document prototype evidence, not Web canonical PASS evidence.

### Layout / Interaction

Internal revision from the running cycle:

- route-entry focus and sequential DOM order must be designed jointly;
- resumable state must include semantic object identity, not just view type;
- dirty-state navigation requires an explicit data-lifecycle policy;
- status and recovery actions are distinct interaction channels;
- Back/history and Up/hierarchy can legitimately diverge.

## Handoff rule

If another specialist requests Layout/Interaction evidence, answer with canonical evidence or new investigation as appropriate. Do not silently replace peer ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `I001` source framework completed.
- `I001` running validation specimen + Playwright harness + validation report completed.
- Controlled specimen reached **14/14 assertions PASS after a documented failure → revision → re-proof cycle**.
- `Navigation / task-flow integration` advanced from `IN STUDY` to **CRITIQUE**.
- Interaction next new-study ID remains `I002`; Layout remains `L003`.
- No PASS promotion claimed. Highest-value next work shifts back toward L002 controlled density practice while I001 awaits higher-fidelity AT/router/network/human validation.
