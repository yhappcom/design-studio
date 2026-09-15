# Web Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/web/`  
Next new-study ID: `W006`

## Operational mission

The Web Design Specialist designs real websites and web applications. It integrates product goals, user tasks, information, brand direction and peer Design Studio evidence into complete web experiences. Frontend knowledge supports prototyping, feasibility, fidelity and browser validation; it is not the end goal.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

Web now has five substantive studies:

- `W001` — Web as a flexible/browser-participatory medium; relationship-over-coordinate baseline.
- `W002` — page composition, mechanism selection and reproducible Chromium failure→revision validation; 25/25 bounded assertions across five stress cases.
- `W003` — responsive/adaptive recomposition by relationship ownership; study, specimen and executable Playwright harness; measured results remain OPEN because this automation environment cannot execute repository code.
- `W004` — information architecture, URL/resource identity, navigation, history, direct entry and wayfinding; route/navigation decision matrix included.
- `W005` — component/page systems, native semantic primitives, variants, independent state dimensions, disabled/unavailable decisions, component/composite/page-pattern boundaries and three system strategies.

Web remains the least complete Stage 1 specialist, but the breadth gap is shrinking. Largest remaining Foundation gaps are complete task surfaces (forms/search/filter/settings/dashboard/list-detail), integrated Web interaction/state/accessibility, performance-sensitive design, browser validation of W003/W004/W005, and a complete project exercise.

## Four-specialist balance

- **Type:** Stage 1 PRACTICE / CRITIQUE, Foundation NOT PASSED, but deep controlled evidence through T016 across construction/package/render/loading/fallback states.
- **Color:** Stage 1 PASS; Stage 2 entry audit next.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 entry audit next.
- **Web:** Stage 1 NOT PASSED; W001–W005 now cover medium, composition, responsive ownership, IA/navigation and component/page-system foundations, but breadth and measured transfer remain behind peers.

The coordinator `progress/STATUS.md` is intentionally not edited by this specialist and may remain stale.

## W002 retained evidence

Canonical:
- `research/web/W002-page-composition-flow-grid-density-hierarchy.md`
- `research/web/W002-page-composition-specimen.html`
- `research/web/W002-page-composition-playwright.py`
- `research/web/W002-page-composition-results.json`

Chromium `144.0.7559.96` validation covered 1280, 768, 320, 320 long bilingual and 320 long bilingual + controlled 200% text-size stress. Initial text-growth failure expanded a 320px document to 420px; `overflow-wrap:anywhere` plus `min-width:0` on relevant Grid/Flex children restored document fit. Final result: **25/25 bounded assertions true**. This is not browser-UI zoom, WCAG conformance, Firefox/Safari parity, screen-reader or human PASS.

## W003 — responsive/adaptive recomposition

Canonical:
- `research/web/W003-responsive-adaptive-recomposition.md`
- `research/web/W003-responsive-recomposition-specimen.html`
- `research/web/W003-responsive-recomposition-playwright.py`

Evidence: **PRACTICE + CRITIQUE / TRANSFER VALIDATION / executable harness authored / measured browser results OPEN**.

Core model:

`task → relationship → stress signal → owner → adaptation → invariant → validation`

Retained judgment: viewport/media-query adaptation for genuinely page/global relationships; container-query adaptation where reusable component allocation differs from viewport; intrinsic flow/wrapping where no discrete task-mode change is required; local 2-D overflow for intrinsically two-dimensional artifacts when stacking destroys meaning.

OPEN: execute harness; exact font lifecycle; actual browser zoom; Firefox/Safari/physical mobile; navigation disclosure/AX transfer; human evidence deferred to project stage.

## W004 — IA / URL / navigation / wayfinding

Canonical:
- `research/web/W004-information-architecture-url-navigation-wayfinding.md`
- `research/web/W004-ia-navigation-route-matrix.csv`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE / TRANSFER VALIDATION**.

Core model:

`user concept ↔ resource identity ↔ addressable location ↔ navigation access ↔ hierarchy ↔ traversal history ↔ page identity ↔ resumable state`

W004 separates resource hierarchy, navigation hierarchy, URL structure and traversal history. It requires canonical routes to survive direct entry rather than assuming the designer's preferred funnel. Portfolio-centric, task-domain and hybrid IA directions were compared by task/context-switching/direct-entry criteria.

OPEN: routed browser specimen; Back/Forward/reload; focus/scroll restoration; deleted/unauthorized deep links; responsive navigation state; long bilingual labels; human findability/orientation deferred.

## W005 — component/page systems

Canonical:
- `research/web/W005-component-page-systems-native-semantics-state-contracts.md`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE / TRANSFER VALIDATION**.

Core model:

`user intent → semantic role → native/platform primitive candidate → state machine → content contract → geometry/adaptation → visual treatment → accessibility/input behavior → page-system placement → validation`

Key retained judgments:

- visual similarity does not establish semantic/interaction equivalence;
- native-first is a decision test, not a ban on visual customization;
- availability, focus, pointer, selection, toggle, expansion, validity, async, permission and destructive-risk dimensions must not be flattened into one generic state enum;
- native `disabled`, discoverable unavailable (`aria-disabled` pattern), hidden/not-applicable and permission-denied are different product decisions;
- components, composites, page patterns and page templates own different contracts;
- prefer native-semantic thin layers or task-pattern-led systems as Foundation defaults; highly polymorphic component platforms require stronger scale/production evidence.

W005 source checks revalidated current WHATWG form-control behavior and W3C APG Button, Disclosure, Menu Button and keyboard-interface guidance. No browser/AT PASS is inferred from source reading.

OPEN: browser specimen comparing native and semantically collapsed controls; Tab/Enter/Space and disabled/`aria-disabled` measurement; long bilingual/text-growth stress; forced-colors transfer; async form/recovery pattern transfer; two-product component-boundary exercise; cross-browser/mobile/AT later gates.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Web as medium / history | PRACTICE / CRITIQUE | broader project/browser/device transfer |
| Document/semantic vs presentation | PRACTICE / CRITIQUE | production accessibility-tree/source-order transfer |
| Responsive/adaptive philosophy | PRACTICE / CRITIQUE — W003 | measured run, zoom, navigation/task transfer |
| Normal flow / intrinsic geometry | PRACTICE / CRITIQUE | broader media/form/task systems |
| Page composition / hierarchy / density | PRACTICE / CRITIQUE — W002 | cross-browser/device + project evidence |
| Information architecture | **PRACTICE / CRITIQUE — W004** | browser/project/human transfer |
| Navigation / wayfinding | **PRACTICE / CRITIQUE — W004** | routed browser/history/direct-entry validation |
| Component/page systems | **PRACTICE / CRITIQUE — W005** | browser/task/project transfer |
| Forms/search/tables/dashboards/settings | PARTIAL | complete task-system practice |
| Web interaction/state | PARTIAL — W004/W005 + peer transfer | complete page/product state systems |
| Web typography | PARTIAL TRANSFER | exact delivered-font/full-page loading/fallback/zoom |
| Web color/theme/state | PARTIAL TRANSFER | real page/browser/device/forced-color practice |
| Accessibility / zoom / localization | PARTIAL PRACTICE | actual zoom, keyboard/AT, broader language stress |
| Performance-sensitive design | **NOT YET WEB-BASELINED** | runtime-cost/design trade-off study |
| Design-to-code/browser validation | PRACTICE | cross-browser/device/production methods |

## Active next queue

1. **W006 candidate — complete task surfaces:** forms, search, filters, settings, tables, dashboards/list-detail with loading, empty, partial, validation, pending, error, retry and outcome-unknown behavior. Integrate W002–W005 with I002/I004 rather than studying isolated widgets.
2. Execute W003 browser harness when execution-capable environment is available; do not invent measurements.
3. Browser validation for W004/W005: history/direct entry and native/custom state/focus contracts.
4. Integrated Web Type/Color/accessibility: exact fonts, themes/system colors, forced colors, actual zoom, keyboard/focus/AT and cross-browser/device transfer.
5. Performance-sensitive design and one complete real-project design/redesign exercise.

## HANDOFFS TO OTHER SPECIALISTS

### Type
W005 transfers T016's runtime-font lesson: reusable component geometry must survive realistic font/fallback and long-label conditions rather than assuming one preferred-font metric state.

### Color
W005 exposes concrete semantic state dimensions for later Color→Web transfer; hue must not become the sole carrier of focus/selection/toggle/validity/async/permission/destructive meaning.

### Layout / Interaction
W004/W005 transfer I001/L006 and state-ownership evidence into Web resource/navigation/component contracts. Future complete task surfaces should preserve focus, restoration, async and conflict/recovery distinctions.

## Latest checkpoint

- W001: PRACTICE + CRITIQUE.
- W002: PRACTICE + CRITIQUE with reproducible Chromium validation; **25/25 bounded assertions after failure→revision**.
- W003: PRACTICE + CRITIQUE; executable harness committed; measured results OPEN.
- W004: **PRACTICE + CRITIQUE; IA/URL/navigation/wayfinding baseline + route matrix committed.**
- W005: **PRACTICE + CRITIQUE; component/page-system native semantics and state-contract baseline committed.**
- Web Foundation: **NOT PASSED**.
- Next new Web study ID: **W006**.
