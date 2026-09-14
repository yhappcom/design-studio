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
- `research/layout/L001-optical-centering-raster-validation.md`
- `research/layout/L001-optical-centering-playwright.py`
- `research/layout/L001-optical-centering-results-summary.json`
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

## Latest completed block — L001 optical-centering raster validation

L001's optical-centering protocol was converted into a controlled Chromium raster-mass experiment without claiming that screenshot centroids equal human optical judgment.

### Controlled contract

- fixed `48×48 CSS px` hit target;
- only the visual child may move;
- visual sizes `16/24/32/40px`;
- DPR 1 and 2;
- six asymmetric/directional shapes;
- black-on-white rendering to isolate geometry/raster mass from Color;
- darkness-weighted raster centroid measured against target center.

### Shape/size dependence

For the play triangle at DPR1, zero-placement horizontal mass-centroid error grew with visual size:

- 16px: about `−0.66px`;
- 24px: `−0.99px`;
- 32px: `−1.35px`;
- 40px: `−1.66px`.

The rounded candidate therefore changed from `+1px` at 16–32px to `+2px` at 40px.

At 24px, `+1px` reduced the measured residual to about `0.01px`.

Chevron and send shapes had the same general rightward correction direction at these sizes but different measured magnitudes.

The irregular stepped mark and badge object often had sub-pixel mass offsets for which a whole-pixel correction would overshoot.

The bookmark produced mainly vertical bias and crossed from no integer correction at 16–24px to a `+1px` downward candidate at 32–40px.

### DPR transfer

DPR2 preserved the broad direction and magnitude of the measured biases. This is useful renderer replication but not physical-device perceptual evidence.

### Professional conclusion

**No universal optical-offset token is supported.**

Even before human perception is measured:

- correction depends on shape;
- correction can depend on visual size;
- correction can be horizontal or vertical;
- some shapes should remain unshifted rather than rounded to a whole pixel;
- hit target and visual child must remain separate.

Raster mass is a diagnostic, not the verdict. Human blinded comparison is still required before claiming perceptual superiority.

Evidence level: **PRACTICE + CRITIQUE / controlled raster validation**.

---

## Previous completed block — L005 Color-driven density/salience with geometry fixed

L005 independently transfer-tests Color C001/C002/C003/C006 against the L002/L004 density framework.

### Controlled setup

A 12-row finance comparison surface was rendered in five color conditions while DOM/content/viewport/typography/geometry/targets/grid/gaps and numeric formatting were held constant.

Automated rectangle comparison returned **geometry_equal = true** across all five conditions. Primary declared text/status/action pairs were held at or above `4.5:1` in this bounded specimen.

### Rendered feature result

`role_separated`:

- mean OKLab chroma ≈ `0.0109`;
- high-chroma (`C > 0.06`) pixel fraction ≈ `4.03%`;
- chroma-gradient proxy ≈ `0.00163`.

`chroma_overloaded` with identical geometry:

- mean OKLab chroma ≈ `0.0182`;
- high-chroma pixel fraction ≈ `7.01%`;
- chroma-gradient proxy ≈ `0.00446`.

`luminance_overloaded` produced the highest luminance variability (`L_std ≈ 0.1775`, luminance-gradient ≈ `0.02109`) despite effectively zero chroma.

`semantic_collision` did not have the highest pixel variability despite intentionally reusing one accent family for incompatible jobs.

### Diagnostic conclusion

Do not collapse “too dense/busy” into one spacing problem. Separate:

1. spatial density;
2. feature variability;
3. semantic emphasis distribution;
4. semantic collision.

The image metrics are deliberately simple proxies, **not** Rosenholtz Feature Congestion and not human perceived-complexity/search-performance evidence.

Evidence level: **PRACTICE + CRITIQUE / Color→Layout transfer validation**.

---

## Other key blocks

### I004 — concurrent edits / conflict / merge / recovery

Version-aware specimen distinguishes disjoint merge, same-field conflict and delete-vs-edit; naive whole-record save reproduced a lost update. Final harness: **17/17 assertions PASS**. State: **PRACTICE / CRITIQUE**.

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
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated rendered controls; realistic layering; blinded human comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | stronger controlled centroid dataset plus observer ratings/broader transfer |
| Optical centering | **PRACTICE / CRITIQUE** | L001 raster mass/size/DPR proof complete; human blinded comparison, physical device, icon+text/RTL/platform transfer pending |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | L002 rendered cycle complete; human task/broader project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002/L003 localized/enlarged/fallback evidence; actual zoom/cross-browser/device/production page transfer pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | L003 fallback + L004 numeric runtime transfer established; production font loading/exact T004/cross-platform/human evidence pending |
| Dense numeric comparison geometry | PRACTICE / CRITIQUE | L004 proof established; locale/accounting/dynamic-update/human comparison evidence pending |
| Color-driven feature density / salience diagnosis | PRACTICE / CRITIQUE | L005 fixed-geometry rendered proof established; validated clutter metric, dark/theme/device/CVD and human task evidence pending |
| Interaction agency / feedback / errors | CRITIQUE | broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device/human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |
| Color-channel-independent state semantics | PRACTICE / CRITIQUE | I003 controlled proof complete; real OS/other browsers/AT/production token-component/human evidence pending |
| Concurrent edits / conflict / merge / recovery | PRACTICE / CRITIQUE | I004 controlled proof complete; real service/offline/multi-device/CRDT-OT/AT/human validation pending |

---

## Peer evidence affecting this role

### Type

Type is through T005. L003/L004 provide Layout-owned browser transfer evidence for fallback and numeric-feature dependencies. The L001 raster block reinforces the shared method distinction between source geometry, raster evidence and optical/perceptual judgment. Production font/glyph decisions remain Type-owned.

### Color

Color is through C006; C007 remains unstarted at this checkpoint.

Relevant current consequences:

- C001/C002/I003: current/focus/status/conflict meaning must survive color replacement;
- C003: data color must not collide with interaction state;
- C006: finance/operational contexts keep action, selection/current, focus and domain status as separate semantic jobs;
- L005 supplies independent fixed-geometry Layout evidence that chroma/luminance feature distribution can change materially without spatial-density change;
- L005 also shows semantic collision is not reducible to pixel variability;
- L001 optical raster proof holds Color constant, leaving color-driven visual-mass transfer as a later distinct experiment.

This does not replace Color ownership of palette/token/contrast/color-science conclusions.

### Web Design

No substantive `W###` at latest synchronization.

Web should reproduce L001/L002/L003/L004/L005/I001/I002/I003/I004 under production page/component/icon systems, fonts/tokens, localization, real router/service/API/offline behavior, target browser/device/OS accessibility modes and AT.

---

## Active next queue

Choose by expected project value, not file count.

1. **L002/L005 human task validation when participants are available** — known-item search, comparison, alert detection and action selection; performance/error separate from preference/workload.
2. **Consume/compare future Color C007** — preserve both studies; classify confirmation, method difference, contradiction or complementary scope rather than merging silently.
3. **L001 figure-ground/border-ownership controls** — build cue-isolated rendered stimuli and a blinded human-test protocol; do not claim ownership judgments without observers.
4. **L001 optical-centering human validation when observers are available** — randomized `0/+δ/−δ` comparisons at intended size; separate preference from perceived centering.
5. **I004 higher-fidelity transfer** — real ETag/If-Match or transaction backend, offline/reconnect, multiple devices/tabs, delete/finalization semantics and AT when a suitable environment exists.
6. **L004 extension only if useful** — exact T004 research font or production `@font-face`, locale/accounting formats, dynamic update and real zoom/DPR.
7. **I003 higher-fidelity transfer** — real OS high-contrast/AT/production tokens when environment exists.
8. Consume future `W###` evidence and independently reproduce high-risk findings where useful.
9. Open `L006` or `I005` only for a genuinely new high-value question after current validation gaps are considered.

---

## Open research-quality gaps

- human perceived-complexity/search/comparison/action evidence for L002/L005;
- validated feature-congestion or equivalent clutter-metric transfer to these UI specimens;
- human conflict-resolution comprehension/error evidence;
- controlled human observation for grouping, figure-ground and visual balance;
- blinded human optical-centering comparison at intended sizes;
- dark-theme, CVD, grayscale, physical-display and environmental transfer for L005;
- optical-centering transfer to production icons, adjacent text, RTL and physical devices;
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
- L005 shows feature density can shift through Color while Type/geometry remain fixed; reciprocal Type tests should hold Color stable.
- L001 raster validation confirms a method boundary useful to Type: geometric center, rendered mass and perceived optical center are different evidence layers; correction changes with shape/size.
- I004 adds local/remote value comparison, version/user metadata and preserved drafts as localization/wrapping stress contexts.
- Scope limit: Layout/Interaction does not define font/glyph production offsets.

### Color

- L005 independently renders five color systems over identical finance geometry and supports C006 role separation without claiming a universal “less color is better” rule.
- L001 optical proof fixes black-on-white to establish geometry/raster baseline; Color may later test whether luminance/chroma shifts measured or human-perceived mass.
- Scope limit: no Color threshold, CVD/device result or human clutter/performance claim is made.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- diagnose “busy/dense” feedback across spatial density, feature variability, semantic emphasis distribution and semantic collision;
- do not use whitespace to repair broad color-emphasis competition before testing the color system itself;
- optical correction starts from geometry, keeps hit target fixed and is shape/size/context-specific;
- a raster centroid is diagnostic evidence, not perceived optical center;
- enable approved numeric features before finalizing numeric tracks;
- viewport width alone is insufficient near Type/fallback thresholds;
- timeout, failure and outcome-unknown are distinct;
- retry is not conflict resolution;
- auto-merge only when semantic independence is established;
- preserve local drafts across conflict;
- critical state meaning must survive authored color-channel loss.

### Web Design

Reusable transfer evidence:

- L001: fixed-target optical-centering raster/size/DPR matrix;
- L002: **216-condition density/reflow matrix**;
- L003: mixed-script fallback / wrap-threshold / semantic-lane transfer;
- L004: browser tabular-numeral / decimal / intrinsic-width transfer;
- L005: fixed-geometry color-driven feature-density / semantic-collision transfer;
- I001: **14-assertion navigation/state matrix**;
- I002: **19-assertion latency/retry/cancellation matrix**;
- I003: **14-assertion forced-colors matrix**;
- I004: **17-assertion concurrent-edit/conflict matrix**.

Web should reproduce these with production icons/fonts/tokens/pages, actual zoom/localization, real router/API/offline/multi-device behavior, target browser/device matrix, OS accessibility modes and AT.

---

## Latest checkpoint

- `L001`: optical-centering raster mass/size/DPR validation added → **PRACTICE / CRITIQUE**, human optical judgment still OPEN.
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
