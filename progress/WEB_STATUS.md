# Web Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/web/`  
Next new-study ID: `W007`

## Operational mission

The Web Design Specialist designs real websites and web applications. It integrates product goals, user tasks, information, brand direction and peer Design Studio evidence into complete web experiences. Frontend knowledge supports prototyping, feasibility, fidelity and browser validation; it is not the end goal.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

Web now has six substantive studies:

- `W001` — Web as a flexible/browser-participatory medium; relationship-over-coordinate baseline.
- `W002` — page composition, mechanism selection and reproducible Chromium failure→revision validation; 25/25 bounded assertions across five stress cases.
- `W003` — responsive/adaptive recomposition by relationship ownership; study, specimen and executable Playwright harness; measured results remain OPEN because the current automation environment cannot execute repository code.
- `W004` — information architecture, URL/resource identity, navigation, history, direct entry and wayfinding; route/navigation decision matrix included.
- `W005` — component/page systems, native semantic primitives, variants, independent state dimensions, disabled/unavailable decisions and component/composite/page-pattern boundaries.
- `W006` — complete task surfaces: forms/search/filter/settings/table/dashboard/list-detail integrated with validation, loading/empty/partial/stale, pending/error/retry/outcome-unknown and region-vs-route state ownership.

Web remains the least complete Stage 1 specialist, but the breadth gap is materially smaller. The largest remaining Foundation gaps are measured browser transfer for W003–W006, integrated Web accessibility/Type/Color under real browser states, performance-sensitive design, and a complete project exercise/capstone sufficient to audit the Foundation gate.

## Four-specialist balance

- **Type:** Stage 1 PRACTICE / CRITIQUE, Foundation NOT PASSED, with deep controlled evidence through T016 across construction/package/render/loading/fallback states.
- **Color:** Stage 1 PASS; Stage 2 entry audit next.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 entry audit next.
- **Web:** Stage 1 NOT PASSED; W001–W006 now cover medium, composition, responsive ownership, IA/navigation, component/page systems and complete task-surface state/recovery foundations, but measured transfer and integrated project evidence remain behind peers.

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

W004 separates resource hierarchy, navigation hierarchy, URL structure and traversal history. It requires canonical routes to survive direct entry rather than assuming the designer's preferred funnel.

OPEN: routed browser specimen; Back/Forward/reload; focus/scroll restoration; deleted/unauthorized deep links; responsive navigation state; long bilingual labels; human findability/orientation deferred.

## W005 — component/page systems

Canonical:
- `research/web/W005-component-page-systems-native-semantics-state-contracts.md`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE / TRANSFER VALIDATION**.

Core model:

`user intent → semantic role → native/platform primitive candidate → state machine → content contract → geometry/adaptation → visual treatment → accessibility/input behavior → page-system placement → validation`

Retained judgments:
- visual similarity does not establish semantic/interaction equivalence;
- native-first is a decision test, not a ban on customization;
- availability, focus, pointer, selection, toggle, expansion, validity, async, permission and destructive-risk dimensions must not be flattened into one generic state enum;
- native `disabled`, discoverable unavailable, hidden/not-applicable and permission-denied are different product decisions;
- components, composites, page patterns and page templates own different contracts.

OPEN: browser/native-custom keyboard/focus validation; long bilingual/text-growth; forced-colors; async form/recovery transfer; cross-browser/mobile/AT later gates.

## W006 — complete task surfaces

Canonical:
- `research/web/W006-complete-task-surfaces-state-recovery-contracts.md`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE + TRANSFER VALIDATION**.

Core model:

`resource/task identity → current authoritative/cached content → user intent/input → validation state → operation state → result/data-view state → recovery/continuation action → navigation/history consequence`

W006 deliberately transfers I002/I004/I005 into complete Web page systems rather than redefining Interaction semantics.

Key retained judgments:
- route, region, control and operation states should be owned at the smallest truthful task boundary;
- initial unresolved, valid empty, filtered-zero, partial, stale/offline cached, failed acquisition and unauthorized/not-found are different states;
- local validity, remote/business validity, accepted intent, pending, confirmed, known non-commit failure and outcome-unknown must remain distinguishable;
- search/filter criteria state and result state are separate; URL/history ownership follows W004 when share/reload/traversal matters;
- dense data surfaces should separate query, summary, collection, selection, detail, mutation and freshness ownership so local failure does not automatically destroy valid context;
- retry safety depends on operation semantics and backend identity/atomicity guarantees, not the presence of a Retry button;
- region-owned progressive workspace is the Foundation default unless product requirements establish atomicity or offline-first constraints.

Source checks revalidated current WHATWG form/constraint-validation behavior and W3C WAI Forms validation/notification guidance. Reading does not imply browser/AT PASS.

OPEN: integrated browser specimen; native constraint validation vs custom error summary; keyboard/focus/status announcements; actual zoom; long bilingual error/recovery text; forced colors; W004 query/history integration; real fetch abort/offline/response-loss; cross-browser/mobile/AT; complete project exercise.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Web as medium / history | PRACTICE / CRITIQUE | broader project/browser/device transfer |
| Document/semantic vs presentation | PRACTICE / CRITIQUE | production accessibility-tree/source-order transfer |
| Responsive/adaptive philosophy | PRACTICE / CRITIQUE — W003 | measured run, zoom, navigation/task transfer |
| Normal flow / intrinsic geometry | PRACTICE / CRITIQUE | broader media/task systems |
| Page composition / hierarchy / density | PRACTICE / CRITIQUE — W002 | cross-browser/device + project evidence |
| Information architecture | PRACTICE / CRITIQUE — W004 | browser/project/human transfer |
| Navigation / wayfinding | PRACTICE / CRITIQUE — W004 | routed browser/history/direct-entry validation |
| Component/page systems | PRACTICE / CRITIQUE — W005 | browser/task/project transfer |
| Forms/search/tables/dashboards/settings | **PRACTICE / CRITIQUE — W006** | integrated browser + real-project transfer |
| Web interaction/state | **PRACTICE / CRITIQUE — W004–W006 + peer transfer** | measured page/product state systems |
| Web typography | PARTIAL TRANSFER | exact delivered-font/full-page loading/fallback/zoom |
| Web color/theme/state | PARTIAL TRANSFER | real page/browser/device/forced-color practice |
| Accessibility / zoom / localization | PARTIAL PRACTICE | actual zoom, keyboard/AT, broader language stress |
| Performance-sensitive design | **NOT YET WEB-BASELINED** | runtime-cost/design trade-off study |
| Design-to-code/browser validation | PRACTICE | cross-browser/device/production methods |

## Active next queue

1. **Measured integrated browser transfer for W004–W006** when execution-capable environment is available: route/history/direct-entry, query state, native/custom validation, keyboard/focus, local/global loading/error ownership, safe recovery and long bilingual stress. Do not invent measurements.
2. **W007 candidate — performance-sensitive design:** loading priority, image/font/script cost, perceived hierarchy, progressive rendering, interaction readiness and design trade-offs; keep it design-led rather than generic performance engineering.
3. Integrated Web Type/Color/accessibility: exact fonts, themes/system colors, forced colors, actual zoom, keyboard/focus/AT and cross-browser/device transfer.
4. **Foundation closure/capstone audit after the performance baseline and at least one integrated complete-project exercise.** Identify exact gate gaps rather than treating later production/human work as perpetual Foundation blockers.
5. Human findability/task/accessibility validation remains deferred to app/project stage where instructed.

## HANDOFFS TO OTHER SPECIALISTS

### Type
W006 makes validation/status/recovery copy part of live geometry. Future Type→Web transfer should include long bilingual failure/outcome-unknown states, not only steady-state labels.

### Color
W006 exposes page semantics — empty, filtered-zero, stale, partial, pending, known failure, outcome unknown, confirmed — that Color may reinforce but must not collapse or encode through hue alone.

### Layout / Interaction
W006 confirms I002/I004/I005 usefulness inside complete Web surfaces while preserving Interaction ownership. Future browser transfer should test whether region-owned states preserve focus/context and whether recovery actions remain semantically safe.

## Latest checkpoint

- W001: PRACTICE + CRITIQUE.
- W002: PRACTICE + CRITIQUE with reproducible Chromium validation; **25/25 bounded assertions after failure→revision**.
- W003: PRACTICE + CRITIQUE; executable harness committed; measured results OPEN.
- W004: PRACTICE + CRITIQUE; IA/URL/navigation/wayfinding baseline + route matrix.
- W005: PRACTICE + CRITIQUE; component/page-system native semantics and state-contract baseline.
- W006: **PRACTICE + CRITIQUE; complete task-surface state/validation/recovery integration and three materially different workspace directions.**
- Web Foundation: **NOT PASSED**.
- Next new Web study ID: **W007**.
