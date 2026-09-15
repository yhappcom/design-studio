# Web Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/web/`  
Next new-study ID: `W004`

## Operational mission

The Web Design Specialist designs real websites and web applications. It integrates product goals, user tasks, information, brand direction and peer Design Studio evidence into complete web experiences. Frontend knowledge is supporting capability for prototyping, feasibility, fidelity and browser validation, not an end in itself.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

Web now has three substantive studies:

- `W001` — Web as a flexible/browser-participatory medium; relationship-over-coordinate baseline.
- `W002` — page composition, mechanism selection and reproducible Chromium failure→revision validation; 25/25 bounded assertions across five stress cases.
- `W003` — responsive/adaptive recomposition by relationship ownership; SOURCE-grounded media/container-query distinction, adaptation-ownership model, three-direction practice and companion specimen. Browser harness/results remain OPEN.

Web remains the least complete Stage 1 specialist. Major Foundation gaps remain information architecture, navigation/wayfinding, component/page systems, complete task surfaces, integrated Web state/accessibility, and broader browser/device transfer.

## Four-specialist balance

- **Type:** Stage 1 PRACTICE / CRITIQUE, Foundation NOT PASSED, but deep controlled evidence through T016 across font construction/package/render/loading/fallback states.
- **Color:** Stage 1 PASS; Stage 2 entry audit next.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 entry audit underway/next.
- **Web:** Stage 1 NOT PASSED; W001–W003 now cover medium, composition and responsive ownership, but breadth remains materially behind peers.

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

Evidence level: **PRACTICE + CRITIQUE / TRANSFER VALIDATION / browser validation OPEN**.

### Current synthesis

Responsive design is modeled as:

`task → relationship → stress signal → owner → adaptation → invariant → validation`.

Three ownership questions are separated:

1. trigger ownership — what fact changed;
2. recomposition ownership — page, component or intrinsic artifact;
3. invariant — what task/meaning must survive.

Current judgment:

- use viewport/media-query adaptation for genuinely page/global relationships;
- use container-query adaptation where a reusable component's allocated space can differ materially from viewport space;
- prefer intrinsic flow/wrapping where no discrete task-mode change is required;
- preserve local 2-D overflow for intrinsically two-dimensional artifacts when forced stacking would destroy meaning.

The companion specimen places equivalent KPI content in wide main and narrow aside allocations at the **same viewport width**, contrasting viewport-owned versus container-owned behavior. It also includes intrinsic action wrapping and a semantic table with local overflow.

### W003 OPEN

- reproducible Chromium failure→revision harness/results;
- same viewport/different container and same container/different viewport measurements;
- long Korean/English labels;
- exact preferred-font loading/failure transfer;
- source/focus sequence across recomposition;
- hover-independent essential actions;
- actual browser-UI zoom;
- Firefox/Safari/physical iOS/Android;
- navigation disclosure/accessibility-tree transfer;
- human evidence, deferred to project-stage validation.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Web as medium / history | PRACTICE / CRITIQUE | broader project/browser/device transfer |
| Document/semantic vs presentation | PRACTICE / CRITIQUE | production accessibility-tree/source-order transfer |
| Responsive/adaptive philosophy | **PRACTICE / CRITIQUE — W003** | executable harness, zoom, navigation/task transfer |
| Normal flow / intrinsic geometry | PRACTICE / CRITIQUE | broader media/form/task systems |
| Page composition / hierarchy / density | PRACTICE / CRITIQUE — W002 | cross-browser/device + project/human evidence |
| Information architecture | **NOT YET WEB-BASELINED** | dedicated Web practice |
| Navigation / wayfinding | **NOT YET WEB-BASELINED** | URL/router/history/direct-entry/resume |
| Component/page systems | **NOT YET WEB-BASELINED** | variants/states/tokens/templates + project transfer |
| Forms/search/tables/dashboards/settings | PARTIAL | complete task-system practice |
| Web interaction/state | INCOMING PEER EVIDENCE ONLY | complete Web page/product transfer |
| Web typography | PARTIAL TRANSFER | exact delivered-font/full-page loading/fallback/zoom |
| Web color/theme/state | INCOMING COLOR EVIDENCE ONLY | real page/browser/device/forced-color practice |
| Accessibility / zoom / localization | PARTIAL PRACTICE | actual zoom, keyboard/AT, broader language stress |
| Performance-sensitive design | **NOT YET WEB-BASELINED** | runtime-cost/design trade-off study |
| Design-to-code/browser validation | PRACTICE | cross-browser/device/production methods |

## Peer evidence currently affecting Web

### Typography / Type

Type T016 establishes that downloadable-font loading/failure/fallback can change wrapping and downstream geometry. W003 treats font realization as a stress input rather than breakpoint authority; exact full-page transfer remains open.

### Color

Color Stage 1 PASS is acknowledged. Responsive modes must retain semantic/task distinctions without making hue the sole information channel.

### Layout / Interaction

Layout/Interaction Stage 1 PASS is acknowledged. W003 transfers L002/L003/L006 into explicit Web adaptation ownership and preserves source/focus/task-order questions for executable validation.

## Active next queue

1. **Complete W003 executable browser validation** before claiming stronger responsive evidence: deliberate failure→revision, same viewport/different containers, long bilingual content, source/focus order and local overflow.
2. **W004 candidate — Information Architecture, URL Resource Structure, Navigation & Wayfinding.** This is the largest remaining untouched Foundation block after responsive depth.
3. Component/page systems and complete task surfaces: forms, search, filters, settings, tables, dashboards, list/detail, loading/error/empty/partial states.
4. Integrated Web Type/Color/accessibility: exact fonts, themes/system colors, forced colors, real zoom, keyboard/focus/AT and cross-browser/device transfer.
5. Performance-sensitive design and complete real-project design/redesign exercise.

## HANDOFFS TO OTHER SPECIALISTS

### Type

Provide exact delivered preferred/fallback pairs when available so W003 can test whether component-local thresholds survive real font lifecycle changes.

### Color

Later theme/forced-color transfer should exercise every responsive mode, not only the wide state.

### Layout / Interaction

W003's adaptation-ownership model should be challenged against simultaneous page-global and component-local recomposition, especially source/focus/task sequence.

## Latest checkpoint

- W001: PRACTICE + CRITIQUE.
- W002: PRACTICE + CRITIQUE with reproducible Chromium validation; **25/25 bounded assertions after failure→revision**.
- W003: **PRACTICE + CRITIQUE; study + specimen committed; browser harness/results OPEN**.
- Web Foundation: **NOT PASSED**.
- Next new Web study ID: **W004**, but W003 validation is the immediate continuation unless newer repository state changes the balance.
