# Web Design Specialist Status

Operating state: **ACTIVE — FOUNDATION CLOSURE AUDIT NEXT**  
Governance sync: 2026-09-15  
Primary path: `research/web/`  
Next new-study ID: `W009`

## Operational mission

The Web Design Specialist designs real websites and web applications. It integrates product goals, user tasks, information, brand direction and peer Design Studio evidence into complete Web experiences. Frontend knowledge supports prototyping, feasibility, fidelity and browser validation; it is not the end goal.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE + INTEGRATED CAPSTONE**  
Foundation: **NOT YET PASSED — EXPLICIT CLOSURE AUDIT REQUIRED**

Web now has eight substantive studies:

- `W001` — Web as a flexible/browser-participatory medium; relationship-over-coordinate baseline.
- `W002` — page composition, mechanism selection and reproducible Chromium failure→revision validation; 25/25 bounded assertions across five stress cases.
- `W003` — responsive/adaptive recomposition by relationship ownership; study, specimen and executable Playwright harness; measured results remain OPEN because the current automation environment cannot execute repository code.
- `W004` — information architecture, URL/resource identity, navigation, history, direct entry and wayfinding; route/navigation decision matrix included.
- `W005` — component/page systems, native semantic primitives, variants, independent state dimensions and component/composite/page-pattern boundaries.
- `W006` — complete task surfaces: forms/search/filter/settings/table/dashboard/list-detail integrated with validation, loading/empty/partial/stale, pending/error/retry/outcome-unknown and region-vs-route state ownership.
- `W007` — performance-sensitive design: task/resource priority, first truthful state, interaction readiness, progressive enrichment, geometry stability and design-led measurement contracts.
- `W008` — integrated complete-project Foundation capstone: three materially different portfolio-workspace directions, explicit selection criteria, selected hybrid resource workspace, IA/URL, responsive, semantic component, state/recovery, Type, Color and performance contracts plus an HTML specimen.

The original breadth gap is now substantially closed. The prior **complete-project integration gap is also materially closed by W008**. The remaining immediate Foundation question is no longer “what topic is missing?” but **whether the exact Master Curriculum Stage 1 gate is satisfied by W001–W008**. That decision must be made through a separate closure audit rather than inferred from file count or apparent breadth.

## Four-specialist balance

- **Type:** Stage 1 PRACTICE / CRITIQUE, Foundation NOT PASSED, with deep controlled evidence through T016 across construction/package/render/loading/fallback states.
- **Color:** Stage 1 PASS; Stage 2 entry audit next.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 entry audit next.
- **Web:** Stage 1 NOT YET PASSED; W001–W008 now provide breadth plus a complete integrated project-like exercise. Closure audit is the next highest-value action.

The coordinator `progress/STATUS.md` is intentionally not edited by this specialist and may remain stale.

---

## W002 retained measured evidence

Canonical:
- `research/web/W002-page-composition-flow-grid-density-hierarchy.md`
- `research/web/W002-page-composition-specimen.html`
- `research/web/W002-page-composition-playwright.py`
- `research/web/W002-page-composition-results.json`

Chromium `144.0.7559.96` validation covered 1280, 768, 320, 320 long bilingual and 320 long bilingual + controlled 200% text-size stress. Initial text-growth failure expanded a 320px document to 420px; `overflow-wrap:anywhere` plus `min-width:0` on relevant Grid/Flex children restored document fit. Final result: **25/25 bounded assertions true**.

This is not browser-UI zoom, WCAG conformance, Firefox/Safari parity, screen-reader or human PASS.

---

## W003 — responsive/adaptive recomposition

Canonical:
- `research/web/W003-responsive-adaptive-recomposition.md`
- `research/web/W003-responsive-recomposition-specimen.html`
- `research/web/W003-responsive-recomposition-playwright.py`

Evidence: **PRACTICE + CRITIQUE / TRANSFER VALIDATION / executable harness authored / measured browser results OPEN**.

Core model:

`task → relationship → stress signal → owner → adaptation → invariant → validation`

Retained judgment: use viewport/media-query adaptation for genuinely page/global relationships; container-query adaptation where reusable component allocation differs from viewport; intrinsic flow/wrapping where no discrete task-mode change is required; local 2-D overflow for intrinsically two-dimensional artifacts when stacking destroys meaning.

---

## W004 — IA / URL / navigation / wayfinding

Canonical:
- `research/web/W004-information-architecture-url-navigation-wayfinding.md`
- `research/web/W004-ia-navigation-route-matrix.csv`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE / TRANSFER VALIDATION**.

Core model:

`user concept ↔ resource identity ↔ addressable location ↔ navigation access ↔ hierarchy ↔ traversal history ↔ page identity ↔ resumable state`

W004 separates resource hierarchy, navigation hierarchy, URL structure and traversal history. Canonical routes must survive direct entry rather than assuming the designer's preferred funnel.

---

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
- components, composites, page patterns and page templates own different contracts.

---

## W006 — complete task surfaces

Canonical:
- `research/web/W006-complete-task-surfaces-state-recovery-contracts.md`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE + TRANSFER VALIDATION**.

Core model:

`resource/task identity → current authoritative/cached content → user intent/input → validation state → operation state → result/data-view state → recovery/continuation action → navigation/history consequence`

W006 transfers I002/I004/I005 into complete Web page systems while preserving Interaction ownership. It separates route, region, control and operation states and distinguishes unresolved, empty, filtered-zero, partial, stale/offline, failed, unauthorized and outcome-unknown states.

---

## W007 — performance-sensitive design

Canonical:
- `research/web/W007-performance-sensitive-design-priority-progressive-rendering.md`

Evidence: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE + TRANSFER VALIDATION**.

Core model:

`user task → information/action priority → critical visible structure → resource dependency → fetch/decode/execute/render cost → first truthful presentation → interaction readiness → progressive enrichment → stable continuation → measurement`

Retained judgments:
- performance is hierarchy over time, not merely bytes or a benchmark score;
- first paint and first usefulness are different;
- visible UI must not imply interaction readiness when behavior is unavailable;
- progressive insertion should preserve focus/context and geometry;
- resource hints implement a priority decision but do not define that decision.

---

## W008 — integrated Web Foundation capstone

Canonical:
- `research/web/W008-integrated-web-foundation-capstone.md`
- `research/web/W008-integrated-web-foundation-capstone-specimen.html`

Evidence: **SOURCE + SYNTHESIS + ORIGINAL PRACTICE + CRITIQUE + INTEGRATION + TRANSFER VALIDATION**.

Controlled project: portfolio-tracking Web workspace supporting direct entry, comparison, filtering, detail inspection, bounded edit, regional refresh/recovery, responsive transfer and progressive rendering.

Three materially different complete directions were compared:

1. **Object-deep hierarchy** — strong identity/auditability, weaker compare→inspect continuity.
2. **Task-domain control center** — strong repeated task efficiency, weaker direct-entry portfolio identity.
3. **Hybrid resource workspace — SELECTED** — stable portfolio/holding resource identity combined with task-oriented comparison workspace.

Selection criteria explicitly compared direct-entry identity, compare→inspect continuity, copied-link clarity, dense comparison, narrow recomposition, state-ownership complexity, implementation risk and fit to the fixed dominant task.

W008 integrates:

- W004 resource/URL/direct-entry contracts;
- W002/W003 composition and responsive ownership;
- W005 native semantic and component/page boundaries;
- W006 regional loading/error/recovery and outcome-unknown semantics;
- W007 first-truthful-state and performance priority;
- Type T016 loading/fallback geometry as a full-page dependency;
- Color Stage 1 hierarchy/state-channel principles;
- Layout/Interaction responsive, navigation/history, focus/ownership and async-state evidence.

### W008 bounded conclusion

The prior Web status identified a complete-project exercise as the largest remaining Foundation gap. **W008 materially closes that gap.**

It does **not** itself declare Stage 1 PASS. The next step is a separate closure audit against the exact `curriculum/MASTER_CURRICULUM.md` Stage 1 gate.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Web as medium / history | PRACTICE / CRITIQUE | later broader project/browser/device transfer |
| Document/semantic vs presentation | PRACTICE / CRITIQUE + W008 integration | later accessibility-tree/production transfer |
| Responsive/adaptive philosophy | PRACTICE / CRITIQUE — W003 + W008 | measured integrated run remains open |
| Normal flow / intrinsic geometry | PRACTICE / CRITIQUE — W002/W008 | broader production transfer |
| Page composition / hierarchy / density | PRACTICE / CRITIQUE — W002 + W008 | complete capstone integration now exists |
| Information architecture | PRACTICE / CRITIQUE — W004 + W008 | human/live-product validation later |
| Navigation / wayfinding | PRACTICE / CRITIQUE — W004 + W008 | routed browser/history measurement later |
| Component/page systems | PRACTICE / CRITIQUE — W005 + W008 | browser/task production transfer later |
| Forms/search/tables/dashboards/settings | PRACTICE / CRITIQUE — W006 + W008 | integrated project-like practice exists |
| Web interaction/state | PRACTICE / CRITIQUE — W004–W008 + peer transfer | measured product state execution later |
| Web typography | PARTIAL TRANSFER + W008 application | exact delivered-font/full-page measured transfer later |
| Web color/theme/state | PARTIAL TRANSFER + W008 application | real page/forced-color/device transfer later |
| Accessibility / zoom / localization | PARTIAL PRACTICE + W008 structural application | actual zoom/keyboard/AT later unless closure audit finds a genuine Foundation gate gap |
| Performance-sensitive design | PRACTICE / CRITIQUE — W007 + W008 | executable browser measurement + live-project field transfer later |
| Design-to-code/browser validation | PRACTICE | W001/W002 measured; W003–W008 integrated measurement still open |
| Complete project integration | **PRACTICE / CRITIQUE — W008 COMPLETE** | explicit Foundation closure audit next |

---

## Active next queue

1. **W009 — Stage 1 Foundation closure audit.** Re-read the exact Master Curriculum Stage 1 visual/interaction gate and map every requirement to W001–W008 plus correctly reused Type/Color/Layout/Interaction evidence. Separate genuine Foundation gaps from Stage 2–5, production/platform and human-validation gaps. Do not promote PASS unless the exact gate is satisfied.
2. If the audit finds a real missing Foundation exercise, perform only that gap before PASS; do not start unrelated expansion.
3. If Stage 1 passes, move to a **Stage 2 entry audit** rather than immediately expanding theory.
4. Where execution becomes available, run measured integrated browser transfer for W003–W008: route/history/direct-entry, query state, native/custom validation, keyboard/focus, local/global loading/error ownership, safe recovery, resource/paint/readiness timing and long bilingual stress.
5. Human findability/task/accessibility/perceived-speed validation remains deferred to app/project stage where instructed.

---

## Preserved later-stage / production OPEN items

- W003 measured browser run;
- W004 real route/history/direct-entry execution;
- W005 native/custom keyboard/focus browser comparison;
- W006 integrated state/recovery execution;
- W007 resource/paint/readiness measurement;
- W008 integrated route/state/focus/performance harness;
- actual browser zoom;
- exact production font loading/fallback/localization;
- forced colors/system colors;
- Firefox/Safari/physical mobile;
- screen-reader/AT and accessibility-user evidence;
- field performance data;
- live backend/API semantics and real project constraints.

These must not be silently treated as Foundation blockers unless W009 demonstrates that the exact Stage 1 gate requires them.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type

W008 consumes T016 as a full-page geometry/stability dependency. Future live-project validation should use exact shipped preferred/fallback pairs and long Korean/English content.

### Color

W008 preserves state semantics structurally before Color application. Production theme/forced-color/device checks should validate exact project palettes rather than this controlled specimen.

### Layout / Interaction

W008 transfers responsive relationship ownership, history/hierarchy separation and regional async/recovery state into a complete Web workspace. Future executable page evidence should be handed back when it confirms, limits or contradicts L/I abstractions.

---

## Latest checkpoint

- W001: PRACTICE + CRITIQUE.
- W002: PRACTICE + CRITIQUE with reproducible Chromium validation; **25/25 bounded assertions after failure→revision**.
- W003: PRACTICE + CRITIQUE; executable harness committed; measured results OPEN.
- W004: PRACTICE + CRITIQUE; IA/URL/navigation/wayfinding baseline + route matrix.
- W005: PRACTICE + CRITIQUE; component/page-system native semantics and state-contract baseline.
- W006: PRACTICE + CRITIQUE; complete task-surface state/validation/recovery integration.
- W007: PRACTICE + CRITIQUE; performance-sensitive priority/progressive-rendering baseline.
- **W008: integrated complete-project Foundation capstone complete with three alternative directions, explicit selection criteria, cross-specialist transfer and HTML specimen.**
- Web Foundation: **NOT YET PASSED — W009 closure audit next.**
- Next new Web study ID: **W009**.
