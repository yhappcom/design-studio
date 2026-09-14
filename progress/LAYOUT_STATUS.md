# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L004`; Interaction `I003`

This file is maintained by the Layout, Spatial & Interaction Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist studies spatial organization and interaction to improve real app, web and product decisions. Research volume and curriculum speed are not the goal.

For live projects, accumulated evidence must become project-specific guidance on hierarchy, grouping, density, responsive behavior, navigation, state, feedback, latency, recovery, target placement, accessibility, localization, platform/device constraints, implementation trade-offs, validation, uncertainty and failure conditions.

Self-directed research remains ACTIVE. Adjacent Type, Color, Web, Accessibility, Human Factors, browser/platform or implementation evidence may be studied or independently validated when it materially improves project judgment.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied spatial and interaction modules; Foundation is **not passed**.

Spatial and temporal/behavioral evidence remain separately indexed under `research/layout/` and `research/interaction/` so those claim types are not conflated.

## Four-specialist sync

Current peers:

1. Typography / Type Design
2. Color
3. Layout, Spatial & Interaction
4. Web Design

Latest peer sync relevant to this role:

- **Type:** through `T005`; mixed Latin/Korean fallback now has measured metric/raster evidence and an explicit L002 transfer case.
- **Color:** through `C004`; color science, semantic/state systems and data-color research remain available for transfer, but no Color finding replaces spatial/state semantics.
- **Web:** `W001` still not substantively published at latest check. Do not invent Web evidence.

Web remains the principal complete-page/browser validation partner. Layout/Interaction may independently validate browser behavior in its own area when analytically useful, but that does not replace Web canonical ownership of full web application/design integration.

---

## Canonical evidence

### Layout / spatial

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`
- `research/layout/L001-figure-ground-balance-optical-centering.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`
- `research/layout/L002-density-validation-specimen.html`
- `research/layout/L002-density-validation-playwright.py`
- `research/layout/L002-density-validation-results-summary.json`
- `research/layout/L002-density-validation-report.md`
- `research/layout/L003-type-fallback-density-reflow-transfer.md`
- `research/layout/L003-type-layout-transfer-playwright.py`
- `research/layout/L003-type-layout-transfer-results-summary.json`
- retained product-design exercises for grid, responsive transfer, grouping and L001 critique.

### Interaction

- `research/interaction/007-interaction-agency-feedback-errors.md`
- `research/interaction/015-directness-state-modes-reversibility.md`
- `research/interaction/I001-navigation-history-focus-restoration-interruption.md`
- `research/interaction/I001-navigation-state-validation-specimen.html`
- `research/interaction/I001-navigation-state-validation-playwright.py`
- `research/interaction/I001-navigation-state-validation-report.md`
- `research/interaction/I002-latency-pending-optimistic-retry.md`
- `research/interaction/I002-async-validation-specimen.html`
- `research/interaction/I002-async-validation-playwright.py`
- `research/interaction/I002-async-validation-results-summary.json`
- `research/interaction/I002-async-validation-report.md`
- retained state-matrix and Study 015 practice/critique evidence under `product-design/exercises/`.

### Shared accessibility evidence

- `research/004-accessibility-reflow-targets-focus.md`
- retained accessibility geometry practice/critique under `product-design/exercises/`.

---

## Latest completed block — L003 Type fallback → Layout transfer

`L003-type-fallback-density-reflow-transfer.md` directly tests T005's Latin/Korean fallback evidence inside a Chromium density/reflow layout.

### Controlled Type inputs

The study uses T005-compatible experimental control stacks:

- Inter + Noto Sans CJK KR;
- Inter + NanumGothic;
- Inter + NanumBarunGothic;
- Noto Sans + Noto Sans CJK KR.

These are controls, not product recommendations.

### Browser transfer result

For the exact transferred L002/T005 string at 20px:

`국제 분산 커버드콜 수익전략 포트폴리오 / $11,242 +1.8%`

Chromium measured approximately:

- Inter + Noto CJK: `489.95px`;
- Inter + NanumGothic: `496.75px`;
- Inter + NanumBarun: `480.42px`;
- Noto + Noto CJK: `486.95px`.

Corresponding one-line thresholds were roughly `490 / 497 / 481 / 487px`.

This **confirms** T005's warning that fallback variation can affect Layout but **limits** standalone FreeType/unshaped width as a production wrap predictor because browser results are not numerically identical.

### Failure → revision

At `500px / 125% text / intermediate density`, the baseline layout gave the primary name only the space remaining beside its action.

Result:

- three stacks wrapped the transferred long label to two lines;
- Inter + NanumBarun remained one line;
- average row height and scan rhythm therefore diverged under the same nominal density/viewport.

The revision did **not** create a font-specific breakpoint. It changed semantic lane priority:

- primary object name receives the full first row;
- the secondary action moves beside status in the next lane;
- metric/change remain below.

Re-proof:

- all four stacks keep the transferred long label to one line at `500px / 125% / intermediate`;
- spacious wrapping also drops materially;
- at `390px / 200% / compact`, the baseline long label ranged about `3–5` lines by stack, while the revised structure produces `2` lines across all four controls.

### Professional conclusion

**Fallback/font state is a spatial input near reflow thresholds.**

A robust responsive contract should not be only:

`viewport width → fixed component arrangement`.

It should also preserve semantic priority under plausible typography variance.

Preferred order:

1. preserve primary object identity/content;
2. preserve required interaction geometry;
3. reallocate semantic lanes / recompose;
4. adapt discretionary whitespace;
5. only then consider truncation where the task genuinely permits it.

Layout should absorb reasonable valid fallback variance. It should return the problem to Type when the pairing itself has unacceptable line-box, body-scale, width, weight, punctuation/numeral or clipping behavior.

Evidence level: **PRACTICE + CRITIQUE / Type→Layout transfer validation in controlled Chromium**.

Not PASS: production `@font-face`, actual zoom, Safari/Firefox/mobile/Flutter, broader Korean line breaking, T004 custom-font numeric feature application, AT and human-task evidence remain open.

---

## Previous key blocks

### L002 — whitespace / density / spatial rhythm

Source framework + **216-condition Chromium validation** across naive/preserve/adaptive policies, compact/intermediate/spacious modes, four viewports, three text scales and English/long-Korean content.

Key result:

- compactness obtained through clipped/hidden content or undersized controls is invalid;
- preserving semantics/targets exposes the true spatial cost;
- rigid spaciousness can become operationally expensive under narrow + enlarged + localized conditions;
- adaptive density should preserve content/targets/grouping while compressing discretionary comfort whitespace.

State: **PRACTICE / CRITIQUE**. Human search/comparison/action evidence remains OPEN.

### I001 — navigation as state

Models Back/history, Up/hierarchy, Close/dismissal, top-level switching, deep links, drafts, object identity and focus restoration.

Controlled running specimen: **14/14 assertions PASS after failure → revision → re-proof**.

State: **CRITIQUE**, not production PASS.

### I002 — latency / pending / retry / cancellation

Separates accepted/pending/progress/confirmed/failed/canceled/**outcome unknown** and ties retry/cancel to operation/data semantics.

Controlled running specimen: **19/19 assertions PASS after failure → revision → re-proof**.

Key findings include:

- timeout ≠ authoritative failure;
- unsafe retry must be suppressed for ambiguous high-consequence outcomes;
- Cancel must stop what it claims to stop;
- transient recovery controls need a focus-restoration destination;
- status and recovery actions are separate channels.

State: **PRACTICE / CRITIQUE**, not production PASS.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real-rendering proof; text-growth and cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants; realistic layering; blinded human comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | controlled centroid dataset; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size device proof; blinded comparison; text/RTL transfer |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | L002 rendered cycle complete; human task and broader project transfer pending |
| Responsive/adaptive recomposition | **PRACTICE / CRITIQUE** | L002 + L003 provide localized/enlarged/fallback evidence; actual zoom, cross-browser/device, production font/page-system transfer pending |
| Type-dependent spatial robustness | **PRACTICE / CRITIQUE** | L003 browser transfer complete for four control stacks; production font loading/fallback, T004 runtime numeric behavior, human/cross-platform evidence pending |
| Interaction agency / feedback / errors | CRITIQUE | broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/conflict/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device and human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |

---

## Primary ownership

### Spatial

Canonical ownership includes grouping, regions, figure-ground, grid, alignment, geometry-driven hierarchy, whitespace, density, rhythm, proportion, visual mass, balance, optical centering, responsive/adaptive recomposition, reflow and target geometry.

### Interaction

Canonical ownership includes affordance/signifiers, mapping, feedback, agency, actions, destinations, navigation, task flow, state, modes, directness, reversibility, latency, async/pending behavior, optimistic/pessimistic commitment, interruption, errors/recovery, retry/cancel policy, pointer/touch/keyboard/gesture paths, focus flow and status communication.

Primary ownership is not a learning prohibition.

---

## Peer evidence currently affecting this role

### Typography / Type

Type is through `T005`.

Most relevant current findings:

- T001: loading/script fallback and vertical metrics can change reflow;
- T003: rendered advances/coverage depend on renderer/hinting/positioning;
- T004: equal source tabular metrics do not alone prove runtime numeric alignment;
- T005: Latin/Korean fallback pairs differ in vertical metrics, Hangul body and long-label width; blind Latin x-height matching is not a generic Hangul fallback solution.

L003 now independently confirms that fallback differences can cross real browser wrap thresholds and that browser results need not equal standalone font measurements.

### Color

Color is through `C004`.

Most relevant project consequences remain:

- state meaning precedes Color encoding;
- forced/user color overrides may remove authored visual channels;
- apparent density can be color-driven as well as spatial;
- data-series color and interaction-state color must not collide;
- observer/color-science research does not replace the platform definitions governing CSS/device output.

### Web Design

No substantive `W###` result was available at latest synchronization.

Current Layout/Interaction evidence should be handed to Web for real complete-page/router/font-loading/network/zoom/device/AT validation when W work begins.

---

## Incoming dependencies / collaboration value

- **Type → Layout:** production fallback/font loading, T004 numeric feature application, T005 line-box and mixed-script behavior in actual stacks.
- **Layout → Type:** L002/L003 supply realistic density/reflow thresholds showing when Type variance becomes a product-level spatial problem.
- **Color → Layout/Interaction:** forced-color/state resilience and color-driven clutter tests with geometry held fixed.
- **Layout/Interaction → Color:** explicit states and fixed geometry for semantic-color validation.
- **Web → Layout/Interaction:** real router/history, font loading/fallback, intrinsic sizing, actual zoom, network, mixed input, AT and page-system transfer evidence.

---

## Active next queue

Research remains ACTIVE. Choose by expected project value, not file count.

1. **L002 human task validation when participants are available** — known-item search, comparison, action selection; objective performance separated from preference/workload. Do not fabricate human evidence.
2. **T004 numeric → Layout transfer** — test browser `tnum`/numeric-column behavior in dense comparison surfaces when the reproducible research font or suitable production-font condition can be exercised.
3. **Color → Layout/Interaction transfer** — hold geometry/state semantics fixed while varying C001/C002/C003 conditions; especially density, focus, failed vs outcome-unknown, and selected/current-location states.
4. **L001 stronger validation** — controlled border-ownership/centroid/optical-centering raster evidence and blinded observation where possible.
5. **I001/I002 higher-fidelity transfer** — real router/service/abort/offline/idempotency/AT only when a suitable Web/project environment exists.
6. Consume future `W###` evidence and independently reproduce high-risk findings where useful.
7. Open `L004` or `I003` only for a genuinely new high-value question after current validation opportunities are considered.

---

## Open research-quality gaps

- human search/comparison/action evidence for density and fallback-sensitive layouts;
- controlled human observation for grouping, figure-ground, balance and optical centering;
- actual browser zoom rather than synthetic root scaling;
- production `@font-face` loading/failure/script fallback and exact run/line-box behavior;
- T004 custom/research-font numeric feature transfer into dense rows;
- Color transfer with geometry/semantics held constant;
- cross-browser/device and cross-surface validation;
- real router/URL history beyond controlled same-document history;
- real HTTP/API abort, timeout, idempotency, reconciliation, offline/reconnect and duplicate-submission evidence;
- screen-reader/assistive-technology validation of navigation, status, busy/progress and recovery;
- interruption/resumption evidence on representative product tasks;
- stronger integration with future Web evidence.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- **Useful finding/context:** T005's fallback-risk hypothesis transfers into actual Layout thresholds. Chromium long-label one-line thresholds ranged about `481–497px` across four control stacks.
- **Canonical section:** `research/layout/L003-type-fallback-density-reflow-transfer.md` Sections 2–6.
- **Confirmation / contradiction / transfer note:** **CONFIRMATION + LIMITATION** — confirms mixed-script fallback affects spatial behavior; limits standalone FreeType/unshaped width as a production wrap predictor.
- **Scope limit:** Layout does not choose the font stack or define acceptable script/body/metric matching.

### Color

- **Useful finding/context:** L002/L003 provide controlled geometry/typography contexts for color-driven density tests; I001/I002 provide explicit state semantics.
- **Canonical section:** L002/L003 density/fallback validation plus I001/I002 state models.
- **Confirmation / contradiction / transfer note:** Color can vary luminance/chroma/forced-color conditions without redefining geometry or state.
- **Scope limit:** no Color/environmental PASS is claimed here.

### Layout / Interaction

Internal current rules:

- compactness is invalid if obtained through lost meaning or required-target shrinkage;
- density modes are relational policies, not immutable spacing tokens;
- viewport width alone is not a complete responsive contract near typography/fallback thresholds;
- give primary semantic identity spatial priority before clipping/shrinking it for a secondary action;
- absorb reasonable font variance through recomposition, but return intrinsically bad font pairing problems to Type;
- timeout and known failure are distinct;
- retry/cancel semantics depend on the operation/data contract;
- disappearing recovery controls require explicit focus lifecycle.

### Web Design

Reusable transfer matrices now available:

- L002: **216-condition density/reflow matrix**;
- L003: mixed-script fallback / wrap-threshold / semantic-lane recomposition transfer;
- I001: **14-assertion navigation/state matrix**;
- I002: **19-assertion latency/retry/cancellation matrix**.

Web should reproduce these with real page systems, production fonts/tokens, actual zoom, router/history, browser/device matrix, network/API contracts and assistive technology, then return confirmation, limitation, contradiction or transfer failure.

---

## Latest checkpoint

- `L002`: source framework + 216-condition Chromium validation; density is **PRACTICE / CRITIQUE**.
- `L003`: Type T005 → Layout transfer completed with browser wrap-threshold evidence and semantic-lane failure→revision→re-proof; Type-dependent spatial robustness is **PRACTICE / CRITIQUE**.
- `I001`: source framework + 14-assertion navigation/state validation; navigation is **CRITIQUE**.
- `I002`: source framework + 19-assertion async validation; latency/retry/cancellation is **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L004`; Interaction `I003`.
- No PASS promotion claimed. Highest-value remaining work is human evidence plus production Type/Color/Web/service transfer, not additional file volume.
