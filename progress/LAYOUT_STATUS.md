# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L006`; Interaction `I005`

This file is maintained by the Layout, Spatial & Interaction Specialist. It must not update global `progress/STATUS.md` during ordinary research.

## Operational mission

This specialist studies spatial organization and interaction to improve real app, web and product decisions. Research volume and curriculum speed are not success metrics.

For live projects, accumulated evidence must become project-specific guidance on hierarchy, grouping, density, responsive behavior, navigation, state, feedback, latency, concurrency, recovery, target placement, accessibility, localization, platform/device constraints, implementation trade-offs, validation, uncertainty and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules; Foundation is **not passed**.

Spatial evidence stays under `research/layout/`; temporal/behavioral evidence stays under `research/interaction/`.

## Four-specialist sync

Latest relevant peer state at this checkpoint:

- **Type:** through `T005`; numeral/runtime and Latin/Korean fallback evidence remain active transfer inputs.
- **Color:** through `C006`; `C007` remains unstarted and Color itself identifies fixed-geometry L002 density/salience transfer as a high-value next question.
- **Web:** no substantive `W###` yet; `W001` remains next. Do not invent Web evidence.

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
- `research/layout/L005-color-driven-density-salience-transfer.md`
- `research/layout/L005-color-density-salience-playwright.py`
- `research/layout/L005-color-density-salience-results-summary.json`
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
- `research/interaction/I004-concurrent-edits-conflict-merge-recovery.md`
- `research/interaction/I004-conflict-validation-playwright.py`
- `research/interaction/I004-conflict-results-summary.json`
- retained state-matrix and Study 015 practice/critique evidence.

### Shared accessibility evidence

- `research/004-accessibility-reflow-targets-focus.md`
- retained accessibility geometry practice/critique.

---

## Latest completed block — L005 Color-driven density/salience with geometry fixed

L005 independently transfer-tests Color C001/C002/C003/C006 against the L002/L004 density framework.

### Controlled setup

A 12-row finance comparison surface was rendered in five color conditions while holding constant:

- DOM/content;
- viewport `1280×900`;
- typography;
- row/card/control dimensions;
- target size;
- grid tracks;
- padding/gaps;
- border widths;
- selected-row identity;
- numeric formatting.

Automated rectangle comparison returned:

**geometry_equal = true** across all five conditions.

Declared primary text/status/action pairs were also kept at or above `4.5:1` in the bounded specimen so obvious low text contrast was not the intended manipulation.

### Five conditions

1. `neutral_minimal` — nearly all treatment neutral; weak semantic emphasis by design.
2. `role_separated` — C006-style job separation for action/selection/focus/positive-negative/status.
3. `chroma_overloaded` — broad chromatic treatment across surfaces, borders, values, status and actions.
4. `luminance_overloaded` — no meaningful chroma, but strong grayscale luminance competition.
5. `semantic_collision` — one teal family reused for action/selection/positive/success-review/focus.

### Rendered feature result

`role_separated`:

- mean OKLab chroma ≈ `0.0109`;
- high-chroma (`C > 0.06`) pixel fraction ≈ `4.03%`;
- chroma-gradient proxy ≈ `0.00163`.

`chroma_overloaded` with identical geometry:

- mean OKLab chroma ≈ `0.0182`;
- high-chroma pixel fraction ≈ `7.01%`;
- chroma-gradient proxy ≈ `0.00446`.

`luminance_overloaded`:

- `L_std ≈ 0.1775`, highest of all conditions;
- luminance-gradient proxy ≈ `0.02109`, also highest;
- effectively zero chroma.

`semantic_collision` did not have the highest pixel variability (`C_mean ≈ 0.0077`, `L_std ≈ 0.1214`) despite intentionally weak semantic role mapping.

### Interpretation

L005 therefore separates four problems that must not be collapsed into one “density” complaint:

1. **spatial density** — geometry, whitespace, grouping and simultaneous content;
2. **feature variability** — luminance/chroma/boundary/weight variation;
3. **semantic emphasis distribution** — how broadly attention-demanding treatment is assigned;
4. **semantic collision** — one visual role carrying incompatible meanings.

A surface can become visually competitive without any spatial change. Conversely, a visually restrained palette can remain semantically weak if one accent means too many things.

### Evidence boundary

The image metrics are deliberately simple OKLab/image-gradient proxies. They are **not** Rosenholtz Feature Congestion and are **not** human perceived-complexity/search-performance measures.

Human search/comparison/error/preference/workload evidence remains OPEN.

Evidence level: **PRACTICE + CRITIQUE / Color→Layout transfer validation in controlled Chromium**.

---

## Previous key blocks

### I004 — concurrent edits / conflict / merge / recovery

Version-aware controlled specimen distinguishes disjoint merge, same-field conflict and delete-vs-edit; naive whole-record save reproduced a lost update. Final harness reached **17/17 assertions PASS**. State: **PRACTICE / CRITIQUE**.

### L004 — tabular numerals → dense Layout transfer

Chromium controls showed zero DOM digit/decimal spread under `tabular-nums`, but Inter tabular figures widened an 88px numeric track enough to create `3/4` overflow; intrinsic numeric width removed overflow. State: **PRACTICE / CRITIQUE**.

### I003 — forced-colors state-semantic resilience

Chromium forced-colors emulation reproduced fill/shadow-only state failures; structural/current/text/programmatic cues survived. **14/14 assertions PASS**. State: **PRACTICE / CRITIQUE**.

### L003 — Type fallback → Layout transfer

Four T005-compatible Latin/Korean fallback stacks crossed different wrap thresholds; semantic-lane recomposition stabilized critical object identity. State: **PRACTICE / CRITIQUE**.

### L002 — whitespace / density / spatial rhythm

**216-condition Chromium validation** rejected fake compactness from clipping/undersized controls and showed adaptive density can preserve content/targets/grouping while compressing discretionary whitespace. State: **PRACTICE / CRITIQUE**.

### I001 — navigation as state

Back/Up/Close/deep-link/workspace/focus/draft model; **14/14 controlled assertions PASS** after failure → revision → re-proof. State: **CRITIQUE**.

### I002 — latency / pending / retry / cancellation

Separates confirmed/failed/**outcome unknown**, ties Retry/Cancel to operation/data contracts and preserves recovery focus; **19/19 controlled assertions PASS**. State: **PRACTICE / CRITIQUE**.

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
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | L003 fallback + L004 numeric runtime transfer established; production font loading/exact T004/cross-platform/human evidence pending |
| Dense numeric comparison geometry | PRACTICE / CRITIQUE | L004 proof established; locale/accounting/dynamic-update/human comparison evidence pending |
| Color-driven feature density / salience diagnosis | **PRACTICE / CRITIQUE** | L005 fixed-geometry rendered proof established; validated clutter metric, dark/theme/device/CVD and human task evidence pending |
| Interaction agency / feedback / errors | CRITIQUE | broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device/human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |
| Color-channel-independent state semantics | PRACTICE / CRITIQUE | I003 controlled proof complete; real OS/other browsers/AT/production token-component/human evidence pending |
| Concurrent edits / conflict / merge / recovery | PRACTICE / CRITIQUE | I004 controlled proof complete; real service/offline/multi-device/CRDT-OT/AT/human validation pending |

---

## Peer evidence affecting this role

### Type

Type is through T005. L003/L004 provide Layout-owned browser transfer evidence for fallback and numeric-feature dependencies. Production font/fallback quality remains Type-owned.

### Color

Color is through C006; C007 remains unstarted at this checkpoint.

Relevant current consequences:

- C001/C002/I003: current/focus/status/conflict meaning must survive color replacement;
- C003: data color must not collide with interaction state;
- C006: finance/operational contexts keep action, selection/current, focus and domain status as separate semantic jobs;
- L005 now supplies independent fixed-geometry Layout evidence that chroma/luminance feature distribution can change materially without spatial-density change;
- L005 also shows semantic collision is not reducible to pixel variability.

This does not replace Color ownership of palette/token/contrast/color-science conclusions.

### Web Design

No substantive `W###` at latest synchronization.

Web should reproduce L002/L003/L004/L005/I001/I002/I003/I004 under production page systems, fonts/tokens, localization, real router/service/API/offline behavior, target browser/device/OS accessibility modes and AT.

---

## Active next queue

Choose by expected project value, not file count.

1. **L002/L005 human task validation when participants are available** — known-item search, comparison, alert detection and action selection; performance/error separate from preference/workload.
2. **Consume/compare future Color C007** — preserve both studies; classify confirmation, method difference, contradiction or complementary scope rather than merging silently.
3. **L001 stronger validation** — controlled border-ownership/centroid/optical-centering raster evidence and blinded observation where possible.
4. **I004 higher-fidelity transfer** — real ETag/If-Match or transaction backend, offline/reconnect, multiple devices/tabs, delete/finalization semantics and AT when a suitable environment exists.
5. **L004 extension only if useful** — exact T004 research font or production `@font-face`, locale/accounting formats, dynamic update and real zoom/DPR.
6. **I003 higher-fidelity transfer** — real OS high-contrast/AT/production tokens when environment exists.
7. Consume future `W###` evidence and independently reproduce high-risk findings where useful.
8. Open `L006` or `I005` only for a genuinely new high-value question after current validation gaps are considered.

---

## Open research-quality gaps

- human perceived-complexity/search/comparison/action evidence for L002/L005;
- validated feature-congestion or equivalent clutter metric transfer to these UI specimens;
- human conflict-resolution comprehension/error evidence;
- controlled human observation for grouping, figure-ground, balance and optical centering;
- dark-theme, CVD, grayscale, physical-display and environmental transfer for L005;
- actual browser zoom rather than synthetic scaling;
- production font loading/fallback and exact T004 browser transfer;
- real OS forced-color/high-contrast environments;
- real multi-device/offline conflict and sync reconciliation;
- CRDT/OT/list/text/order conflict behavior where relevant;
- real router/history and service/network evidence;
- screen-reader/AT validation of navigation, state, status, conflict, busy/progress and dense table semantics;
- interruption/resumption evidence on representative tasks;
- stronger future Web integration.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- L004 confirms browser-level tabular alignment while exposing numeric-column width cost.
- L005 shows apparent/feature density can shift through Color while Type/geometry remain fixed; future Type density transfer should reciprocally hold Color stable.
- I004 adds local/remote value comparison, version/user metadata and preserved drafts as localization/wrapping stress contexts.
- Scope limit: Layout/Interaction does not define font internals or production fallback stacks.

### Color

- **Useful finding/context:** L005 independently renders five color systems over identical finance geometry. Role-separated vs chroma-overloaded conditions show materially different chroma coverage/gradient while geometry is identical; luminance-only overload creates strong feature variation with zero meaningful chroma; semantic collision remains independent of those pixel proxies.
- **Canonical section:** `research/layout/L005-color-driven-density-salience-transfer.md` Results / Project Diagnostic Model.
- **Confirmation / contradiction / transfer note:** **CONFIRMATION + METHOD SEPARATION** — supports C006 semantic-role separation and Color's C007 candidate question, while explicitly rejecting a universal “less color = better” rule.
- **Scope limit:** no Color threshold, CVD result, device result or human clutter/performance claim is made.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- diagnose “busy/dense” feedback across spatial density, feature variability, semantic emphasis distribution and semantic collision;
- do not use whitespace to repair broad color-emphasis competition before testing the color system itself;
- enable approved numeric features before finalizing numeric tracks;
- viewport width alone is insufficient near Type/fallback thresholds;
- timeout, failure and outcome-unknown are distinct;
- retry is not conflict resolution;
- auto-merge only when semantic independence is established;
- preserve local drafts across conflict;
- critical state meaning must survive authored color-channel loss.

### Web Design

Reusable transfer evidence:

- L002: **216-condition density/reflow matrix**;
- L003: mixed-script fallback / wrap-threshold / semantic-lane transfer;
- L004: browser tabular-numeral / decimal / intrinsic-width transfer;
- L005: fixed-geometry color-driven feature-density / semantic-collision transfer;
- I001: **14-assertion navigation/state matrix**;
- I002: **19-assertion latency/retry/cancellation matrix**;
- I003: **14-assertion forced-colors matrix**;
- I004: **17-assertion concurrent-edit/conflict matrix**.

Web should reproduce these with production fonts/tokens/pages, actual zoom/localization, real router/API/offline/multi-device behavior, target browser/device matrix, OS accessibility modes and AT.

---

## Latest checkpoint

- `L002`: density validation → **PRACTICE / CRITIQUE**.
- `L003`: T005 fallback→Layout transfer → **PRACTICE / CRITIQUE**.
- `L004`: browser `tnum`/decimal/intrinsic-width transfer → **PRACTICE / CRITIQUE**.
- `L005`: fixed-geometry Color→Layout feature-density/semantic-collision transfer → **PRACTICE / CRITIQUE**.
- `I001`: navigation/state validation → **CRITIQUE**.
- `I002`: async/retry/cancel validation → **PRACTICE / CRITIQUE**.
- `I003`: forced-colors semantic resilience → **PRACTICE / CRITIQUE**.
- `I004`: concurrent edit/conflict/merge/recovery → **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L006`; Interaction `I005`.
- No PASS promotion claimed. Highest-value remaining work is human evidence plus production Color/Web/Type/service/AT transfer rather than research volume.
