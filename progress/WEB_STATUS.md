# Web Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/web/`  
Next new-study ID: `W008`

## Operational mission

The Web Design Specialist designs real websites and web applications. It integrates product goals, user tasks, information, brand direction and peer Design Studio evidence into complete web experiences. Frontend knowledge supports prototyping, feasibility, fidelity and browser validation; it is not the end goal.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

Web now has seven substantive studies:

- `W001` — Web as a flexible/browser-participatory medium; relationship-over-coordinate baseline.
- `W002` — page composition, mechanism selection and reproducible Chromium failure→revision validation; 25/25 bounded assertions across five stress cases.
- `W003` — responsive/adaptive recomposition by relationship ownership; study, specimen and executable Playwright harness; measured results remain OPEN because the current automation environment cannot execute repository code.
- `W004` — information architecture, URL/resource identity, navigation, history, direct entry and wayfinding; route/navigation decision matrix included.
- `W005` — component/page systems, native semantic primitives, variants, independent state dimensions and component/composite/page-pattern boundaries.
- `W006` — complete task surfaces: forms/search/filter/settings/table/dashboard/list-detail integrated with validation, loading/empty/partial/stale, pending/error/retry/outcome-unknown and region-vs-route state ownership.
- `W007` — performance-sensitive design: task/resource priority, first truthful state, interaction readiness, progressive enrichment, geometry stability and design-led measurement contracts.

Web remains the least complete Stage 1 specialist, but the original breadth gap is now substantially reduced. The largest remaining Foundation gaps are **integrated measured browser transfer**, exact Web Type/Color/accessibility transfer, and a **complete project exercise/capstone + explicit Foundation closure audit**. Performance-sensitive design is no longer NOT YET WEB-BASELINED.

## Four-specialist balance

- **Type:** Stage 1 PRACTICE / CRITIQUE, Foundation NOT PASSED, with deep controlled evidence through T016 across construction/package/render/loading/fallback states.
- **Color:** Stage 1 PASS; Stage 2 entry audit next.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 entry audit next.
- **Web:** Stage 1 NOT PASSED; W001–W007 now cover medium, composition, responsive ownership, IA/navigation, component/page systems, complete task surfaces and performance-sensitive design. Integrated measured/project evidence remains behind peers.

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

## W004 — IA / URL / navigation / wayfinding

Canonical:
- `research/web/W004-information-architecture-url-navigation-wayfinding.md`
- `research/web/W004-ia-navigation-route-matrix.csv`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE / TRANSFER VALIDATION**.

Core model:

`user concept ↔ resource identity ↔ addressable location ↔ navigation access ↔ hierarchy ↔ traversal history ↔ page identity ↔ resumable state`

W004 separates resource hierarchy, navigation hierarchy, URL structure and traversal history. It requires canonical routes to survive direct entry rather than assuming the designer's preferred funnel.

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

## W006 — complete task surfaces

Canonical:
- `research/web/W006-complete-task-surfaces-state-recovery-contracts.md`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE + TRANSFER VALIDATION**.

Core model:

`resource/task identity → current authoritative/cached content → user intent/input → validation state → operation state → result/data-view state → recovery/continuation action → navigation/history consequence`

W006 transfers I002/I004/I005 into complete Web page systems while preserving Interaction ownership. It separates route, region, control and operation states and distinguishes unresolved, empty, filtered-zero, partial, stale/offline, failed, unauthorized and outcome-unknown states.

## W007 — performance-sensitive design

Canonical:
- `research/web/W007-performance-sensitive-design-priority-progressive-rendering.md`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE + TRANSFER VALIDATION**.

Core model:

`user task → information/action priority → critical visible structure → resource dependency → fetch/decode/execute/render cost → first truthful presentation → interaction readiness → progressive enrichment → stable continuation → measurement`

Retained judgments:
- performance is **hierarchy over time**, not merely bytes or a benchmark score;
- first paint and first usefulness are different;
- visible UI must not imply interaction readiness when behavior is unavailable;
- W006 region ownership determines which areas may resolve progressively;
- late media/font/data insertion must preserve reading position, focus and target geometry;
- `loading`, `fetchpriority`, preload and responsive-image mechanisms implement a task-priority decision; they do not define that decision;
- for ordinary task-oriented Web products, task-first progressive composition is the Foundation default unless showcase-first or snapshot-first semantics are justified.

W007 compares three materially different directions — showcase-first, task-first progressive shell, snapshot-first resilient workspace — with KEEP/REWORK/REJECT conditions.

OPEN: executable W007 browser specimen; Resource/Paint/Event Timing; layout/readiness assertions; cache/network/CPU transfer; physical/cross-browser testing; field Core Web Vitals only on a live project; human perceived-speed/task evidence deferred where required.

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
| Forms/search/tables/dashboards/settings | PRACTICE / CRITIQUE — W006 | integrated browser + real-project transfer |
| Web interaction/state | PRACTICE / CRITIQUE — W004–W006 + peer transfer | measured page/product state systems |
| Web typography | PARTIAL TRANSFER | exact delivered-font/full-page loading/fallback/zoom |
| Web color/theme/state | PARTIAL TRANSFER | real page/browser/device/forced-color practice |
| Accessibility / zoom / localization | PARTIAL PRACTICE | actual zoom, keyboard/AT, broader language stress |
| Performance-sensitive design | **PRACTICE / CRITIQUE — W007** | executable browser measurement + live-project field transfer |
| Design-to-code/browser validation | PRACTICE | cross-browser/device/production methods |

## Active next queue

1. **Integrated complete-project Web exercise/capstone candidate:** combine W002–W007 into one coherent task surface with IA/URL, responsive composition, semantic components, task-state ownership, Type/Color application, performance priority and explicit alternative directions. This should be project-like rather than another isolated mechanism note.
2. Where execution becomes available, run **measured integrated browser transfer for W003–W007**: route/history/direct-entry, query state, native/custom validation, keyboard/focus, local/global loading/error ownership, safe recovery, resource/paint/readiness timing and long bilingual stress. Do not invent measurements.
3. Integrated Web Type/Color/accessibility: exact fonts, themes/system colors, forced colors, actual zoom, keyboard/focus/AT and cross-browser/device transfer.
4. **Foundation closure audit after the complete-project exercise.** Map the exact Master Curriculum Stage 1 gate to evidence and separate genuine Foundation gaps from later production/human/platform gates.
5. Human findability/task/accessibility/perceived-speed validation remains deferred to app/project stage where instructed.

## HANDOFFS TO OTHER SPECIALISTS

### Type
W007 transfers T016 into page-level temporal composition: font loading/failure is a priority and stability state, not only a Type implementation detail.

### Color
W006/W007 expose state and progressive-rendering semantics that Color may reinforce but must not collapse or encode through hue alone. Performance optimization must not silently erase contrast/state differentiation.

### Layout / Interaction
W007 extends L003/I002 into temporal composition. Progressive insertion should preserve focus/context and must not imply operability before behavior exists.

## Latest checkpoint

- W001: PRACTICE + CRITIQUE.
- W002: PRACTICE + CRITIQUE with reproducible Chromium validation; **25/25 bounded assertions after failure→revision**.
- W003: PRACTICE + CRITIQUE; executable harness committed; measured results OPEN.
- W004: PRACTICE + CRITIQUE; IA/URL/navigation/wayfinding baseline + route matrix.
- W005: PRACTICE + CRITIQUE; component/page-system native semantics and state-contract baseline.
- W006: PRACTICE + CRITIQUE; complete task-surface state/validation/recovery integration.
- W007: **PRACTICE + CRITIQUE; performance-sensitive design priority/progressive-rendering baseline with three alternative directions.**
- Web Foundation: **NOT PASSED**.
- Next new Web study ID: **W008**.
