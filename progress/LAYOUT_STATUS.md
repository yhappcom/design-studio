# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L003`; Interaction `I003`

This file is maintained by the Layout, Spatial & Interaction Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist studies spatial organization and interaction to improve real app, web and product decisions. Research volume and curriculum speed are not the goal.

When a project arrives, the specialist must convert accumulated knowledge into project-specific guidance on information/spatial hierarchy, grouping, density, responsive behavior, navigation, state, feedback, latency, recovery, target placement, accessibility, implementation trade-offs, validation strategy, uncertainty and failure conditions.

Self-directed research remains ACTIVE. Adjacent Type, Color, Web Design, Accessibility, Human Factors, browser/platform or implementation knowledge may be studied when it materially improves judgment, replication, transfer validation or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied spatial and interaction modules; Foundation is not passed.

Spatial and temporal/behavioral evidence remain separately indexed under `research/layout/` and `research/interaction/` so those claim types are not conflated.

## Four-specialist collaboration sync

Design Studio operates with four official peer specialists:

1. Typography / Type Design
2. Color
3. Layout, Spatial & Interaction
4. Web Design

Web Design is the main real-web application/validation partner for this role. At the latest synchronization point, `progress/WEB_STATUS.md` still listed `W001` as not yet begun. Do not invent Web evidence; re-check Web status and `research/web/` before every substantial block.

## Canonical evidence already established

### Layout / spatial

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`
- `research/layout/L001-figure-ground-balance-optical-centering.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`
- `research/layout/L002-density-validation-specimen.html`
- `research/layout/L002-density-validation-playwright.py`
- `research/layout/L002-density-validation-results-summary.json`
- `research/layout/L002-density-validation-report.md`
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

### Shared accessibility evidence relevant to this role

- `research/004-accessibility-reflow-targets-focus.md`
- retained accessibility geometry practice and critique under `product-design/exercises/`.

## Latest completed block — I002 latency / pending / retry validation

I002 converts Study 015's generic pending/commitment distinction into a project-facing latency and recovery model, then validates that model in a running Chromium specimen.

### Source/project model

I002 separates:

- idle;
- accepted locally;
- pending;
- progressing;
- confirmed;
- failed;
- canceled;
- **outcome unknown**.

Key project conclusions:

- timeout is not automatically authoritative failure;
- Retry safety depends on operation semantics/idempotency/reconciliation, not button availability;
- optimistic UI is a commitment strategy, not a speed effect;
- Cancel may mean stop work, stop waiting, dismiss UI, continue in background, or undo later — those contracts must not be conflated;
- determinate progress must correspond to meaningful work progress rather than fabricated elapsed-time percentages;
- live status and interactive recovery actions are distinct channels.

### Controlled validation specimen

Three operation classes were implemented:

1. optimistic reversible Favorite;
2. high-consequence Transfer with committed remote result but lost response;
3. determinate Export with cancellation.

### Failure → revision evidence

The baseline and early corrected versions exposed four meaningful failures:

1. native `disabled` during pending caused the focused origin control to lose focus;
2. lost response after a possible high-consequence commit was mislabeled as failure and exposed unsafe Retry;
3. Cancel changed the UI to `Canceled` but allowed underlying work to continue and later become `Export complete`;
4. transient Retry / Check Status / Cancel controls disappeared after resolution and could leave focus on `body`.

The final specimen was revised to:

- preserve a focusable pending locus where appropriate using `aria-disabled` plus explicit activation guards in this controlled case;
- represent ambiguous transport outcome as `outcome unknown`;
- preserve an operation ID and use `Check status` before any retry;
- keep high-consequence commit count at one;
- stop and invalidate underlying simulated work on Cancel;
- restore focus from disappearing recovery controls to stable logical controls;
- keep `role=status` regions non-interactive and separate from Retry/Check/Cancel actions.

### Re-proof

The final Playwright harness reached **19/19 PASS** assertions covering:

- optimistic local update;
- pending focus preservation;
- `aria-busy`;
- duplicate activation guarding;
- known failure rollback;
- safe retry;
- retry focus restoration;
- ambiguous outcome;
- unsafe-retry suppression;
- Check Status exposure;
- operation identity;
- authoritative reconciliation;
- reconciliation focus restoration;
- no duplicate commit;
- determinate progress;
- real cancellation of the simulated operation;
- cancel focus restoration;
- live status not stealing focus.

Evidence level: **PRACTICE + CRITIQUE / controlled Chromium JavaScript state-machine evidence**.

This is not production PASS. Real HTTP/API semantics, server idempotency/deduplication, AbortController/request cancellation, offline/reconnect, refresh/process restoration, screen readers, cross-browser/device behavior, localization/fallback and human task evidence remain open.

## Previous completed block — L002 rendered density validation

L002 now includes a **216-condition** Chromium matrix across naive/preserve/adaptive policies, compact/intermediate/spacious modes, four viewports, three text scales and English/long-Korean content.

Key result:

- naive compactness appeared efficient by hiding/clipping content or shrinking controls;
- preserve policy exposed the true spatial cost while keeping critical content and target geometry intact;
- rigid spaciousness became very expensive under 390px + 200% text + long Korean;
- adaptive policy preserved content/targets/grouping while compressing discretionary comfort whitespace.

Professional conclusion:

> Density modes are relational policies, not immutable pixel identities.

`Whitespace / density / spatial rhythm` is now **PRACTICE / CRITIQUE**. Human search/comparison/action performance remains OPEN.

## Previous interaction block — I001 navigation/state validation

I001 models navigation as state rather than menu/animation styling and separates Back/history, Up/hierarchy, Close/dismissal, top-level switching, deep-link entry, focus restoration, drafts and workspace identity.

Its controlled Playwright specimen reached **14/14 PASS** after a documented failure → revision → re-proof cycle.

Evidence remains controlled Chromium proof, not production router/URL/AT/cross-browser/human PASS.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; multilingual/enlarged-text/browser transfer |
| Grid / alignment systems | CRITIQUE | real-browser proof; text-growth stress; broader responsive transfer |
| Perceptual grouping | CRITIQUE | broader context validation and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants; realistic layering; blinded human comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | controlled centroid dataset; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size device proof; blinded comparison; RTL/text-context transfer |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | 216-condition L002 rendered cycle complete; human task evidence, actual zoom and Type/Color/Web transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002 adds narrow/enlarged/localized reflow evidence; actual browser zoom/device and broader transfer pending |
| Interaction agency / feedback / errors | CRITIQUE | controlled running proof exists; broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | I001/I002 running proof exists; broader multi-user/conflict/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | I001 controlled proof complete; real router/URL, AT, cross-browser/device and human resumption pending |
| Latency / pending / optimistic / retry / cancellation | **PRACTICE / CRITIQUE** | I002 source + 19-assertion controlled proof complete; real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |

## Primary ownership

### Spatial

Canonical ownership includes grouping, regions, figure-ground, grid, alignment, geometry-driven hierarchy, whitespace, density, rhythm, proportion, visual mass, balance, optical centering, responsive/adaptive recomposition, reflow and target geometry.

### Interaction

Canonical ownership includes affordance/signifiers, mapping, feedback, agency, actions, destinations, navigation, task flow, state, modes, directness, reversibility, latency, async/pending behavior, optimistic/pessimistic commitment, interruption, errors/recovery, retry/cancellation policy, pointer/touch/keyboard/gesture paths, focus flow and status communication.

Primary ownership is not a learning prohibition. Cross-domain replication and transfer validation are encouraged when they improve project judgment.

## Peer evidence currently affecting Layout / Interaction

### From Type

Type now includes T001–T004.

Most relevant findings:

- T001: fallback/vertical metrics can change wrapping, row height and reflow;
- T003: identical source metrics can produce different rendered advances/coverage depending on renderer/hinting/positioning;
- T004: even equal source tabular advances can split under some hinted rendering modes; compact numeric systems require actual-stack validation.

Consequences:

- L002 density and I001/I002 labels cannot be validated with placeholder rectangles;
- status/recovery strings must later be tested with localization/fallback/enlargement;
- layout failures may originate in Type/rendering and should be diagnosed accordingly.

### From Color

Color now includes C001–C003.

Most relevant findings:

- C001: forced-colors/user overrides can remove authored color channels;
- C002: semantic roles must remain separate from primitive/component values;
- C003: information semantics and interaction state should not collide, and apparent density may change through chroma/luminance even when geometry is fixed.

Consequences:

- pending, failed, confirmed, outcome-unknown, current location and focus must survive without color-only meaning;
- I002 now supplies explicit state semantics that Color can map without collapsing failure and uncertainty into one warning hue.

### From Web Design

No substantive `W###` study was available at the latest synchronization point.

Web should reproduce current Layout/Interaction matrices in complete page systems and real network/browser conditions and return confirmation, limitation, contradiction or transfer failure rather than silently adapting conclusions.

## Incoming dependencies

- Type needs realistic dense/responsive/status/recovery contexts for localization, fallback and text-growth stress.
- Color needs realistic surface/navigation/focus/data-density/pending/error/unknown/success contexts for semantic-color validation.
- Web Design needs grouping, density, responsive logic, navigation/history, async state, retry/cancel, focus, recovery and target-geometry evidence.

## Cross-domain opportunities

### Type

High-value next transfers:

- load T004/T005 typography/fallback evidence into L002 compact/intermediate/spacious surfaces;
- stress I002 labels such as `Checking status`, `Outcome unknown`, `Retry`, `Canceled`, `Confirmed` under Korean/Latin localization and enlargement;
- distinguish Layout wrapping failures from Type metric/fallback failures.

### Color

High-value next transfers:

- hold L002 geometry constant while varying C002/C003 luminance/chroma/state roles;
- run I001/I002 states under C001 forced-color conditions;
- ensure `failed` and `outcome unknown` remain distinct without assigning meaning solely by hue.

### Web Design

Immediate transfer targets:

1. Study 006 / Exercise 007 — intrinsic sizing, actual font metrics, localization, zoom and narrow containers;
2. Study 014 — grouping/containment in complete page/component systems;
3. L001 — border ownership, mass and optical centering at real browser/device sizes;
4. L002 — reproduce the 216-condition density matrix with actual zoom, project fonts/components and page constraints;
5. I001 — reproduce the 14-assertion navigation/state matrix with real router/URL/history/AT;
6. I002 — reproduce the 19-assertion async matrix with real `fetch`, duplicate submissions, API idempotency/reconciliation, request abort, offline/reconnect and screen readers;
7. shared accessibility geometry — native semantics and actual target/focus behavior.

## Active next queue

Research remains ACTIVE. Expected-value priorities:

1. **L002 human task validation when participants are available** — known-item search, comparison and action selection; objective performance separate from preference/workload. Do not fabricate human evidence.
2. **Type→Layout transfer** — rerun L002/I002 with actual T004/T005 typography/fallback evidence when appropriate artifacts are available.
3. **Color→Layout/Interaction transfer** — hold geometry/semantics fixed while varying Color conditions for density and async/navigation states.
4. **I002 real service/Web transfer** — real request/abort/offline/idempotency/reconciliation/AT validation when a suitable Web or project environment is available.
5. Extend I001 only where evidence value is high: real router/URL, assistive technology, real network conflict and representative interruption/resumption.
6. Convert L001 into stronger controlled observer/raster evidence.
7. Consume future `W###` work and independently reproduce high-risk Web results when useful.
8. Open `L003` or `I003` only when a genuinely new question has higher expected value than current validation gaps or a live project requires it.

## Open research-quality gaps

- human search/comparison/action evidence for density variants and preference/performance separation;
- controlled human observation for grouping, figure-ground, balance and optical centering;
- actual browser zoom and broader localization/data stress beyond the controlled L002 surrogate;
- actual T004/T005 font/fallback transfer into density and async surfaces;
- Color transfer with geometry/semantics held constant;
- cross-surface systems across phone/tablet/desktop;
- real router/URL navigation beyond same-document controlled history;
- real HTTP/API abort, timeout, idempotency, reconciliation, offline/reconnect and duplicate-submission evidence;
- screen-reader/assistive-technology validation of navigation, status, busy/progress and recovery;
- cross-browser/device mixed-input validation;
- interruption/resumption evidence on representative product tasks;
- stronger integration with future Web evidence.

## Handoffs to other specialists

### Typography / Type

- L002 supplies a reproducible density/reflow matrix with long Korean stress.
- I002 adds realistic status/recovery strings and transient-control focus contexts.
- T004/T005 can be transfer-tested inside compact data and async surfaces, especially numeric alignment, fallback, wrapping and text enlargement.
- Scope limit: current specimens use system-font browser rendering and do not validate Type internals.

### Color

- L002 supplies fixed geometry for color-driven clutter tests.
- I001/I002 supply explicit semantic states before Color encoding.
- `failed` and `outcome unknown` must remain separate; pending/confirmed/focus/recovery must survive C001 forced-color conditions.
- Scope limit: no Color override/environmental validation was performed in I002.

### Web Design

- `L002-density-validation-specimen.html` + harness provide a reproducible **216-condition density/reflow transfer matrix**.
- `I001-navigation-state-validation-specimen.html` + harness provide a **14-assertion navigation/state transfer matrix**.
- `I002-async-validation-specimen.html` + harness provide a **19-assertion latency/retry/cancellation transfer matrix**.
- Web should reproduce these with real page systems, project fonts/tokens, actual network/API contracts, router/history, browser/device matrix and assistive technology.
- Return real limitations or contradictions explicitly rather than silently adapting the behavior.

### Layout / Interaction

Internal revisions from current practice:

- compactness cannot be credited when content or required target geometry is sacrificed;
- density modes are bounded relational policies rather than fixed pixel identities;
- timeout and known failure are distinct states;
- retry safety depends on the operation/data contract;
- Cancel must state whether it stops work or only dismisses the UI;
- disappearing inline recovery controls require explicit focus restoration;
- status and recovery actions are separate interaction channels.

## Handoff rule

If another specialist requests Layout/Interaction evidence, answer with canonical evidence or new investigation as appropriate. Do not silently replace peer ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `L002` source framework plus **216-condition naive → preserve → adaptive Chromium validation** complete; density module is **PRACTICE / CRITIQUE**.
- `I001` source framework plus **14-assertion navigation/state validation** complete; navigation module is **CRITIQUE**.
- `I002` source framework plus **19-assertion async latency/retry/cancellation validation** complete after documented failure → revision → re-proof; latency module is **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L003`; Interaction `I003`.
- No PASS promotion claimed. Highest-value remaining work is higher-fidelity human/Type/Color/Web/service transfer, not additional file volume.
