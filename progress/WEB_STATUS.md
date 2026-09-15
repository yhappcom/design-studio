# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 1 PASSED / STAGE 2 PRACTICE / RUNTIME TRANSFER ACTIVE**  
Governance sync: 2026-09-15  
Primary path: `research/web/`  
Next new-study ID: `W013`

## Current level

Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority:
- W009 — Stage 1 Foundation closure
- W010 — Stage 2 entry audit
- W011 — iconography/non-text signal direct practice
- W012 — executed responsive runtime transfer / contradiction review

The coordinator-maintained `progress/STATUS.md` is stale relative to specialist evidence and remains outside Web's writing boundary.

## Latest evidence — W012

Canonical:
- `research/web/W012-responsive-runtime-transfer-validation.md`
- `research/web/W012-responsive-runtime-results.json`

Reason for repetition: **TRANSFER VALIDATION + CONTRADICTION REVIEW**. W003 had a prepared Chromium harness but no executed canonical result; Web's largest relative weakness was runtime execution depth.

Execution environment: Chromium `144.0.7559.96` through Playwright.

Four cases were executed: 1180px wide, 820px mid, 390px narrow, and 390px narrow with a long English/Korean label.

Measured findings:
- at 1180px the same viewport gave main/aside container widths `734.41 / 305.59px` and container-query modes `2 / 1` columns;
- at 820px those widths were `474 / 206px`, still `2 / 1` columns;
- at 390px both local containers were `308px` and both recomposed to one column;
- no case produced document-level horizontal overflow;
- table overflow activated locally at mid/narrow allocations but was unnecessary at wide allocation;
- source/focus sequence remained stable in all four cases;
- long bilingual label stress did not create document horizontal overflow.

The original W003 assertion set returned **15/16**, but the single failure was classified as an **ASSERTION-MODEL DEFECT**, not a layout failure. The old predicate required table overflow to be active even when the wide allocation had enough room. W012 establishes the stronger testing distinction:

`fallback ownership != fallback activation`.

A fallback mechanism should activate only when its stress condition exists. This rule transfers to scrolling, disclosure, truncation, compact navigation, sticky behavior and recovery UI.

## Stage 2 snapshot

| Requirement | Current state |
| --- | --- |
| task analysis / primary question | established |
| information hierarchy / IA | established |
| dense vs low-density composition | strong; W002 executed |
| responsive/adaptive | **PRACTICE + Chromium transfer executed in W012** |
| forms/tables/search/settings/state | established; integrated runtime still open |
| typography across roles | established; exact production transfer open |
| iconography/non-text signals | direct W011 practice; runtime open |
| component systems | strong conceptual practice |
| async/recovery | strong peer transfer; Web runtime open |
| comparative alternatives + explicit selection | strong |
| critique / KEEP-REWORK-REJECT | strong |
| cross-specialist handoff | strong |

Stage 2 is not passed. Runtime depth is improving but remains uneven across navigation/history, native/custom semantics, integrated task state, icon/target/enlargement behavior and temporal readiness.

## Four-specialist balance

- **Type:** Stage 1 PASS; Stage 2 PRACTICE. T021 has actual outline build/raster execution and a diagnosed lowercase drawing defect.
- **Color:** Stage 1 PASS; Stage 2 entry audit pending; strong quantitative/rendered/browser evidence already exists.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 entry audit pending; deep assertion-based spatial/state/async evidence.
- **Web:** Stage 1 PASS; Stage 2 PRACTICE. W011 closed the explicit iconography content gap; W012 now adds real Chromium transfer, but runtime coverage remains the largest relative weakness.

## Current OPEN / blockers

Highest-value executable gaps:
1. correct and rerun W003's canonical overflow assertion contract;
2. W004 real Back/Forward/reload/direct-entry/focus restoration;
3. W005 native vs custom keyboard/focus/semantic behavior;
4. W006 integrated search/filter/table/edit async/recovery execution;
5. W011 accessible-name/target/enlargement/forced-color icon harness;
6. W007 request/paint/readiness/stability measurement;
7. broader integrated capstone execution.

Later/platform gaps:
- actual browser-UI zoom;
- exact production fonts/CDN/cache/service-worker behavior;
- Firefox/Safari/physical mobile parity;
- screen-reader/AT evidence;
- physical-device and field performance evidence.

Human findability/task/perceived-speed/icon-recognition evidence remains deferred to live project/app validation and is not simulated.

## Active next queue

1. Re-evaluate all four specialists before choosing the next study.
2. If Web remains the largest imbalance, prioritize another **executed browser transfer**, not a new theory topic.
3. W004 navigation/history or W005 native/custom semantic-control execution is currently higher value than broadening content coverage.
4. Preserve failure→critique→revision evidence rather than designing harnesses that only prove authored success states.
5. Hand browser findings back to Type, Color and Layout/Interaction when they confirm, limit or contradict canonical peer evidence.

## HANDOFFS TO OTHER SPECIALISTS

### Type
Responsive activation thresholds can move with exact font geometry; ownership of the adaptation mechanism is separate from the font-specific threshold.

### Color
Forced-color/theme fallback capability and activation should likewise be asserted separately.

### Layout / Interaction
W012 confirms relationship/ownership reasoning in Chromium and adds a validation rule: fallback ownership and fallback activation are separate assertions. This applies to disclosure, overlays, retry and compact-state transitions.

## Latest checkpoint

- W009: **Stage 1 PASS**.
- W010: **Stage 2 entry accepted**.
- W011: **iconography/non-text direct practice established**.
- W012: **Chromium runtime transfer executed; W003 assertion-model defect identified**.
- Stage 2: **NOT PASSED**.
- Next new Web study ID: **W013**.
