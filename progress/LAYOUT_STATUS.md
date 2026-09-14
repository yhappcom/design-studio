# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L005`; Interaction `I004`

This file is maintained by the Layout, Spatial & Interaction Specialist. It must not update global `progress/STATUS.md` during ordinary research.

## Operational mission

This specialist studies spatial organization and interaction to improve real app, web and product decisions. Research volume and curriculum speed are not success metrics.

For live projects, accumulated evidence must become project-specific guidance on hierarchy, grouping, density, responsive behavior, navigation, state, feedback, latency, recovery, target placement, accessibility, localization, platform/device constraints, implementation trade-offs, validation, uncertainty and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules; Foundation is **not passed**.

Spatial evidence stays under `research/layout/`; temporal/behavioral evidence stays under `research/interaction/`.

## Four-specialist sync

Latest relevant peer state:

- **Type:** through `T005`; numeral/runtime and Latin/Korean fallback evidence are active transfer inputs.
- **Color:** through `C006`; semantic-token transfer now has two-context practice, while C001/C002/C003 remain key Layout/Interaction dependencies.
- **Web:** no substantive `W###` at latest check; `W001` remains next. Do not invent Web evidence.

Web remains the complete page/browser integration partner. Layout/Interaction may independently validate browser behavior in its own domain when useful, without replacing Web canonical ownership.

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
- `research/layout/L004-tabular-numerals-dense-comparison-transfer.md`
- `research/layout/L004-tabular-numerals-playwright.py`
- `research/layout/L004-tabular-numerals-results-summary.json`
- retained grid/responsive/grouping/L001 product-design exercises.

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
- `research/interaction/I003-forced-colors-state-semantic-resilience.md`
- `research/interaction/I003-forced-colors-validation-playwright.py`
- `research/interaction/I003-forced-colors-results-summary.json`
- retained state-matrix and Study 015 practice/critique evidence.

### Shared accessibility evidence

- `research/004-accessibility-reflow-targets-focus.md`
- retained accessibility geometry practice/critique.

---

## Latest completed block — L004 tabular numerals → dense Layout transfer

L004 independently transfer-tests T004's runtime numeric-alignment concern using Chromium CSS layout and installed control fonts.

### Controlled environment

- Chromium `144.0.7559.96`;
- fonts: Inter, Roboto, Noto Sans;
- sizes: 14/16/20/32px;
- proportional vs `font-variant-numeric: tabular-nums`;
- per-digit DOM advance measurement;
- decimal x-position in right-aligned values;
- 88px fixed numeric track vs intrinsic `max-content` track.

### Alignment result

For all three control fonts at all four sizes:

- proportional digit advance spread was non-zero;
- tabular digit advance spread was `0` at the DOM-layout layer.

At 16px, proportional decimal-position spread across controlled signed values was:

- Inter: about `7.97px`;
- Roboto: about `4.72px`;
- Noto Sans: about `4.75px`.

With tabular digits + fixed fractional precision + right alignment, decimal-position spread became `0` for all three controls.

### T004 transfer interpretation

This **confirms T004's comparison contract at the tested Chromium layout layer but limits raw hinted metrics as a browser-layout predictor**.

T004 showed that equal source tabular advances can split in some raw FreeType hinted modes. L004 shows that Chromium's shaping/layout client can still expose equal DOM advances. These are different evidence layers, not a contradiction.

### Failure → revision

A 360px dense row used an 88px fixed numeric track.

At 16px Inter:

- proportional values fit;
- enabling tabular numerals caused **3 of 4** controlled values to overflow;
- required width rose to about `91px`.

Revision:

- replace the placeholder-derived fixed numeric width with an intrinsic `max-content` numeric track and flexible label track.

Re-proof:

- Inter tabular overflow `3 → 0`;
- widest numeric width about `91.5px`;
- spatial cost is transferred explicitly to the flexible label region instead of hidden as clipping.

### Professional conclusion

Dense numeric alignment is a joint contract:

**number semantics + formatting + Type runtime behavior + Layout track allocation**.

`tnum` should be enabled **before** final numeric-column sizing. A layout that only works with proportional placeholder figures is not production-ready for a comparison role.

Evidence level: **PRACTICE + CRITIQUE / Type→Layout browser transfer validation**.

Not PASS: exact T004 research font, production `@font-face`, fallback, localization/accounting formats, actual zoom/DPR, Safari/Firefox/mobile, dynamic-update behavior, AT and human comparison performance remain open.

---

## Previous key blocks

### I003 — forced-colors state-semantic resilience

Chromium forced-colors emulation reproduced C001's predicted failure:

- fill-only selected states converged;
- color-only async states converged;
- box-shadow focus disappeared.

Structural/current/text/programmatic cues survived. Controlled result: **14/14 assertions PASS**. State: **PRACTICE / CRITIQUE**, not production PASS.

### L003 — Type fallback → Layout transfer

Four T005-compatible Latin/Korean fallback stacks crossed different browser wrap thresholds. Reallocating semantic lanes rather than adding font-specific breakpoints stabilized critical object identity. State: **PRACTICE / CRITIQUE**.

### L002 — whitespace / density / spatial rhythm

**216-condition Chromium validation** showed that clipping/undersized controls create fake compactness, while rigid spaciousness becomes costly under narrow/enlarged/localized constraints. Adaptive density preserves content/targets/grouping while compressing discretionary whitespace. State: **PRACTICE / CRITIQUE**.

### I001 — navigation as state

Back/Up/Close/deep-link/workspace/focus/draft model; **14/14 controlled assertions PASS after failure → revision → re-proof**. State: **CRITIQUE**.

### I002 — latency / pending / retry / cancellation

Separates confirmed/failed/**outcome unknown**, ties Retry/Cancel to data contracts, and preserves recovery focus; **19/19 controlled assertions PASS**. State: **PRACTICE / CRITIQUE**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real-rendering proof; text-growth/cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants; realistic layering; blinded comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | controlled centroid data; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size device proof; blinded comparison; text/RTL transfer |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | L002 rendered cycle complete; human task/broader project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002/L003 localized/enlarged/fallback evidence; actual zoom/cross-browser/device/production page transfer pending |
| Type-dependent spatial robustness | **PRACTICE / CRITIQUE** | L003 fallback + L004 numeric runtime transfer established; production font loading/T004 exact font/cross-platform/human evidence pending |
| Dense numeric comparison geometry | **PRACTICE / CRITIQUE** | L004 `tnum`/decimal/intrinsic-width proof established; locale/accounting/dynamic update/human comparison evidence pending |
| Interaction agency / feedback / errors | CRITIQUE | broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/conflict/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device/human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |
| Color-channel-independent state semantics | PRACTICE / CRITIQUE | I003 controlled proof complete; real OS/other browsers/AT/production token-component/human evidence pending |

---

## Peer evidence affecting this role

### Type

Type is through T005.

- T004: equal source tabular metrics do not alone prove runtime numeric alignment;
- T005: valid Latin/Korean fallback pairs can alter width/vertical behavior and browser thresholds.

L003/L004 now provide Layout-owned browser transfer evidence for both classes of Type dependency.

### Color

Color is through C006.

Relevant current consequences:

- C001/C002: interaction meaning must survive color replacement and semantic role must remain separate from literal values;
- C003: data-color semantics must not collide with interaction state;
- C006: finance and operational contexts preserve action/selection/focus/status as distinct semantic jobs even when literal primitives are shared.

I003 confirms the forced-color failure mechanism at the Interaction layer. L002/L004 now provide stable geometry for future Color-driven density/salience transfer.

### Web Design

No substantive `W###` at latest synchronization.

Web should reproduce L002/L003/L004/I001/I002/I003 with production page systems, font loading, localization, zoom, network/API, target browsers/devices, OS accessibility modes and AT.

---

## Active next queue

Choose by expected project value, not file count.

1. **L002 human task validation when participants are available** — known-item search, comparison and action selection; performance separate from preference/workload.
2. **Color → Layout density/salience transfer** — coordinate with/consume C007 when available; hold L002/L004 geometry constant while varying luminance/chroma/emphasis.
3. **L001 stronger validation** — controlled border-ownership/centroid/optical-centering raster evidence and blinded observation where possible.
4. **L004 extension only if useful** — exact T004 research font or production `@font-face`, locale/accounting formats, dynamic numeric update and real zoom/DPR.
5. **I003 higher-fidelity transfer** — real OS high-contrast/AT/production tokens when environment exists.
6. **I001/I002 higher-fidelity transfer** — real router/service/abort/offline/idempotency/AT when suitable Web/project environments exist.
7. Consume future W### evidence and independently reproduce high-risk findings where useful.
8. Open `L005` or `I004` only for a genuinely new high-value question after current validation gaps are considered.

---

## Open research-quality gaps

- human search/comparison/action evidence for density/fallback/numeric layouts;
- controlled human observation for grouping, figure-ground, balance and optical centering;
- actual browser zoom rather than synthetic scaling;
- production `@font-face` loading/failure/fallback and exact T004 research-font browser transfer;
- locale/accounting/variable-precision/dynamic numeric format stress;
- geometry-fixed Color density/salience transfer;
- real OS forced-color/high-contrast environments;
- cross-browser/device and cross-surface validation;
- real router/history and service/network evidence;
- screen-reader/AT validation of navigation, state, status, busy/progress and dense table semantics;
- interruption/resumption evidence on representative tasks;
- stronger future Web integration.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- **Useful finding/context:** Chromium `tabular-nums` produced equal DOM digit advances for Inter/Roboto/Noto Sans at 14–32px and zero decimal drift in the controlled right-aligned format.
- **Canonical section:** `research/layout/L004-tabular-numerals-dense-comparison-transfer.md` Sections 3–5.
- **Confirmation / contradiction / transfer note:** **CONFIRMATION + LAYER LIMITATION** — supports the runtime comparison value of tabular figures while showing that raw hinted-advance behavior does not alone predict browser layout; Inter's tabular figures also increased required numeric-column width enough to create a Layout failure.
- **Scope limit:** exact T004 research font and production font quality remain Type-owned and unvalidated here.

### Color

- L002/L004 provide fixed dense-data geometry ready for Color-driven density/salience transfer.
- I003 confirms state meaning must survive forced-color replacement.
- C006's separation of data/status/interaction roles should be preserved in future dense finance specimens.
- Scope limit: L004 claims no Color result.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- viewport width alone is insufficient near Type/fallback thresholds;
- enable the approved numeric feature before finalizing numeric-column width;
- numeric comparison needs consistent formatting + Type runtime behavior + Layout alignment;
- timeout and known failure are distinct;
- retry/cancel depend on operation/data contracts;
- disappearing recovery controls need explicit focus lifecycle;
- current/focus/pending/failed/unknown/confirmed must survive authored color-channel loss.

### Web Design

Reusable transfer evidence now includes:

- L002: **216-condition density/reflow matrix**;
- L003: mixed-script fallback / wrap-threshold / semantic-lane transfer;
- L004: browser tabular-numeral / decimal-alignment / intrinsic-width transfer;
- I001: **14-assertion navigation/state matrix**;
- I002: **19-assertion latency/retry/cancellation matrix**;
- I003: **14-assertion forced-colors state-semantic matrix**.

Web should reproduce with production fonts/tokens/pages, actual zoom/localization, real router/network/API, target browser/device matrix, OS accessibility modes and AT.

---

## Latest checkpoint

- `L002`: density validation → **PRACTICE / CRITIQUE**.
- `L003`: T005 fallback→Layout transfer → **PRACTICE / CRITIQUE**.
- `L004`: browser `tnum`/decimal/intrinsic-width transfer → **PRACTICE / CRITIQUE**.
- `I001`: navigation/state validation → **CRITIQUE**.
- `I002`: async/retry/cancel validation → **PRACTICE / CRITIQUE**.
- `I003`: forced-colors semantic resilience → **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L005`; Interaction `I004`.
- No PASS promotion claimed. Highest-value remaining work is human evidence plus production Color/Web/Type/service/AT transfer rather than research volume.
