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

Latest relevant peer state:

- **Type:** through `T005`; numeral/runtime and Latin/Korean fallback evidence remain active transfer inputs.
- **Color:** through **`C007`**; Color independently completed a fixed-geometry density/salience study that directly overlaps L005 with complementary methods.
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
- `research/layout/L001-border-ownership-cue-isolation-validation.md`
- `research/layout/L001-border-ownership-specimen.html`
- `research/layout/L001-border-ownership-playwright.py`
- `research/layout/L001-border-ownership-results-summary.json`
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

## Latest completed block — L001 border-ownership cue isolation

L001 figure-ground theory now has a reproducible rendered stimulus set designed for later blinded observer testing.

### Core experimental contract

Nine stimuli share the same central vertical edge and neutral local field:

- baseline `B0`;
- enclosure mirror pair `E-L / E-R`;
- contour-junction mirror pair `T-L / T-R`;
- attachment/continuity mirror pair `C-L / C-R`;
- cue-conflict mirror pair `X-L / X-R`.

The experiment deliberately changes **remote context** while holding the tested local edge constant.

### Failure → revision

The initial HTML accidentally applied T-junction classes at both card and stage scope. The harness caught local contamination:

- T pair local-crop difference ≈ `1.625%`;
- conflict pair inherited the same problem.

After scoping cue classes to the stage only:

- all 9 stimuli share one identical local-crop SHA-256;
- `all_local_crops_equal_baseline = true`;
- every mirrored pair has `local_crop_diff_fraction = 0`;
- remote context remains different.

Remote-context difference after masking the local crop:

- enclosure pair ≈ `2.24%`;
- T-junction pair ≈ `1.25%`;
- attachment pair ≈ `3.89%`;
- cue-conflict pair ≈ `3.44%`.

These percentages are implementation checks, **not perceptual effect sizes**.

### Human-test readiness

A blinded protocol is now defined:

- present one stimulus at intended size with ID hidden;
- ask which side appears to own the central boundary: Left / Right / Ambiguous;
- collect confidence separately;
- randomize order per observer;
- analyze mirror consistency, baseline ambiguity, cue-agreement vs cue-conflict, and generic left/right response bias.

No human response data have been fabricated.

### Evidence level

**PRACTICE + CRITIQUE / controlled stimulus-isolation validation**.

Figure-ground remains not PASS until actual observers establish whether and how these contextual manipulations change perceived ownership, followed by transfer into realistic UI layering.

---

## Cross-specialist comparison — Color C007 ↔ Layout L005

Color `C007-fixed-geometry-color-density-salience.md` was completed independently after L005.

### Shared confirmation

Both studies keep geometry fixed and independently show:

- distributed chroma can materially change the rendered feature field without changing spatial density;
- zero/low chroma does **not** guarantee a calmer field because luminance segmentation can be strong;
- semantic emphasis should be localized according to task value rather than applied to every difference;
- screenshot/image proxies are not human perceived-clutter or performance measures.

### Complementary methods

**L005**

- 1280×900 finance surface;
- five variants, including an explicit `semantic_collision` condition;
- simple OKLab page statistics and gradient proxies;
- separates spatial density, feature variability, emphasis distribution and semantic collision.

**C007**

- 1024×900 L002-derived surface;
- four variants including `high-contrast-mono` and `semantic-sparse`;
- downsampled Oklab local-variability proxy plus action/selected-region comparisons;
- shows sparse semantic color can preserve strong local action distinction while reducing page-wide chroma.

### Classification

**CONFIRMATION + COMPLEMENTARY METHOD**, no substantive contradiction found.

Do not merge the files or treat either proxy as a universal clutter score. Human search/comparison/error/preference/workload evidence remains the common gate.

---

## Other established blocks

### L001 optical centering

Fixed 48×48 hit target; six asymmetric shapes; visual sizes 16/24/32/40px; DPR1/2. Raster darkness-centroid evidence shows no universal optical-offset token: direction/magnitude vary by shape and size, and some whole-pixel corrections overshoot. Raster mass remains diagnostic rather than human perceived center.

### L002 density / spatial rhythm

**216-condition Chromium validation** rejected fake compactness from clipping/undersized targets and showed adaptive density can preserve content/targets/grouping while compressing discretionary whitespace.

### L003 Type fallback → Layout

Four T005-compatible Latin/Korean fallback stacks crossed different browser wrap thresholds. Semantic-lane recomposition stabilized critical object identity rather than using font-specific breakpoints.

### L004 tabular numerals → dense Layout

Chromium control fonts showed zero DOM digit/decimal spread under `tabular-nums`; enabling tnum widened Inter enough to break an 88px placeholder-derived track. Intrinsic numeric width removed overflow. Numeric comparison is a joint formatting + Type runtime + Layout track contract.

### L005 Color → Layout

Fixed-geometry rendered transfer separates spatial density from Color-driven feature variability and semantic collision. Independent C007 now confirms the main direction with a different method.

### I001 navigation as state

Back/Up/Close/deep-link/workspace/focus/draft model; **14/14 controlled assertions PASS** after failure → revision → re-proof.

### I002 latency / pending / retry / cancellation

Separates confirmed/failed/**outcome unknown**, ties Retry/Cancel to operation/data contracts; **19/19 controlled assertions PASS**.

### I003 forced-colors state resilience

Fill/shadow-only state failures reproduced; structural/text/programmatic cues survived; **14/14 controlled assertions PASS**.

### I004 concurrent edits / conflict / merge / recovery

Naive whole-record save reproduced a lost update; version-aware flow distinguishes disjoint merge, same-field conflict and delete-vs-edit; **17/17 controlled assertions PASS**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real-rendering proof; text-growth/cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context and human observation |
| Figure-ground / border ownership | **PRACTICE / CRITIQUE** | L001 local-edge-controlled cue set complete; blinded observers + realistic layering transfer pending |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | stronger centroid datasets; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | raster mass/size/DPR proof complete; blinded human comparison, physical device, icon+text/RTL/platform transfer pending |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | L002 rendered cycle complete; human task/broader project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002/L003 evidence; actual zoom/cross-browser/device/production page transfer pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | L003 fallback + L004 numeric transfer established; production-font/cross-platform/human evidence pending |
| Dense numeric comparison geometry | PRACTICE / CRITIQUE | L004 proof established; locale/accounting/dynamic-update/human comparison evidence pending |
| Color-driven feature density / salience | PRACTICE / CRITIQUE | L005 + independent C007 confirmation; human task/CVD/device/environment transfer pending |
| Interaction agency / feedback / errors | CRITIQUE | broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device/human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |
| Color-channel-independent state semantics | PRACTICE / CRITIQUE | real OS/other browsers/AT/production token-component/human evidence pending |
| Concurrent edits / conflict / merge / recovery | PRACTICE / CRITIQUE | real service/offline/multi-device/CRDT-OT/AT/human validation pending |

---

## Peer evidence affecting this role

### Type

Type is through T005. L003/L004 provide browser transfer evidence for fallback and numeric-feature dependencies. L001 optical work reinforces the shared distinction between geometric/source position, raster evidence and human optical judgment.

### Color

Color is through **C007**.

- C001/C002/I003: critical state meaning must survive authored color replacement;
- C003: data color and interaction state are separate semantics;
- C006: action/selection/focus/status should remain separate semantic jobs;
- C007 independently confirms L005's fixed-geometry conclusion and rejects `desaturate = declutter`;
- L005 contributes the complementary semantic-collision distinction that C007's image metrics alone cannot represent.

This does not replace Color ownership of palette/token/color-science conclusions.

### Web Design

No substantive W### at latest synchronization.

Web should reproduce L001/L002/L003/L004/L005/I001/I002/I003/I004 and relevant C007 findings inside complete production-like page/component systems.

---

## Active next queue

Choose by expected project value, not file count.

1. **Human evidence when participants are available**:
   - L001 border ownership Left/Right/Ambiguous judgments;
   - L001 optical `0/+δ/−δ` perceived-centering comparisons;
   - L002/L005/C007 known-item search/comparison/action/error tests;
   - separate performance/error from preference/workload.
2. **Realistic L001 layering transfer** — abstract ownership controls → popover/card/table/sheet/sticky-header examples while preserving cue isolation.
3. **I004 higher-fidelity transfer** — real ETag/If-Match or transaction backend, offline/reconnect, multi-device/tab, delete/finalization semantics and AT when suitable environment exists.
4. **L004 extension only if useful** — exact T004/production font, locale/accounting formats, dynamic update, real zoom/DPR.
5. **I003 higher-fidelity transfer** — real OS high-contrast/AT/production tokens.
6. Consume future W### evidence and independently reproduce high-risk findings where useful.
7. Open `L006` or `I005` only for a genuinely new question with higher value than current validation gaps.

---

## Open research-quality gaps

- actual observer judgments for border ownership, grouping, balance and optical centering;
- human perceived-clutter/search/comparison/action evidence for L002/L005/C007;
- validated feature-congestion/equivalent metric transfer to UI specimens;
- realistic layer ownership under content, Color and interaction-state combinations;
- human conflict-resolution comprehension/error evidence;
- actual browser zoom rather than synthetic scaling;
- production font loading/fallback and exact T004 browser transfer;
- real OS forced-color/high-contrast environments;
- real multi-device/offline conflict and sync reconciliation;
- CRDT/OT/list/text/order conflicts where relevant;
- real router/history and service/network evidence;
- screen-reader/AT validation of navigation, state, status, conflict, busy/progress and dense table semantics;
- interruption/resumption evidence on representative tasks;
- stronger future Web integration.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- L004 confirms browser-level tabular alignment while exposing numeric-column width cost.
- L003 confirms fallback width can cross layout thresholds.
- L001 optical/border work reinforces method isolation: geometric/raster/context/perception are separate evidence layers.
- Conflict/version UI from I004 remains a useful localization/wrapping stress case.
- Scope limit: Layout/Interaction does not define font/glyph production decisions.

### Color

- **C007 ↔ L005:** CONFIRMATION + COMPLEMENTARY METHOD. Both fixed-geometry experiments reject a pure spacing explanation for all “busy” feedback and reject `less chroma = automatically calmer`.
- L005 adds explicit semantic-collision diagnosis; C007 adds stronger local feature/action-region comparisons.
- L001 border-ownership validation fixes Color while varying context, the reciprocal experimental design to L005/C007.
- Scope limit: no human clutter/salience threshold is claimed.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- diagnose “busy/dense” across spatial density, feature variability, emphasis distribution and semantic collision;
- do not use whitespace to repair broad color-emphasis competition before testing the color system;
- border ownership is contextual: diagnose remote cues while controlling the local edge;
- do not claim perceptual ownership from a rendered stimulus without observers;
- optical correction starts geometric, keeps the hit target fixed, and is shape/size/context-specific;
- raster centroid is diagnostic, not perceived optical center;
- enable approved numeric features before finalizing numeric tracks;
- viewport width alone is insufficient near Type/fallback thresholds;
- timeout, failure and outcome-unknown are distinct;
- retry is not conflict resolution;
- auto-merge only when semantic independence is established;
- preserve local drafts across conflict;
- critical state meaning must survive authored color-channel loss.

### Web Design

Reusable transfer evidence now includes:

- L001 border ownership: pixel-identical local-edge cue-isolation set + blinded observer protocol;
- L001 optical centering: fixed-target raster/size/DPR matrix;
- L002: 216-condition density/reflow matrix;
- L003: mixed-script fallback / wrap-threshold / semantic-lane transfer;
- L004: browser tabular-numeral / decimal / intrinsic-width transfer;
- L005 + Color C007: independent fixed-geometry Color/feature-density validation;
- I001: 14-assertion navigation/state matrix;
- I002: 19-assertion latency/retry/cancel matrix;
- I003: 14-assertion forced-colors matrix;
- I004: 17-assertion conflict matrix.

Web should reproduce these with production icons/fonts/tokens/pages, actual zoom/localization, router/API/offline/multi-device behavior, target browser/device matrix, OS accessibility modes and AT.

---

## Latest checkpoint

- `L001`: optical raster validation + **border-ownership cue-isolation/re-proof** complete → PRACTICE / CRITIQUE; observer judgments still OPEN.
- `L002`: density validation → PRACTICE / CRITIQUE.
- `L003`: T005 fallback→Layout transfer → PRACTICE / CRITIQUE.
- `L004`: browser `tnum`/decimal/intrinsic-width transfer → PRACTICE / CRITIQUE.
- `L005`: fixed-geometry Color→Layout transfer → PRACTICE / CRITIQUE; now independently confirmed/complemented by Color C007.
- `I001`: navigation/state validation → CRITIQUE.
- `I002`: async/retry/cancel validation → PRACTICE / CRITIQUE.
- `I003`: forced-colors semantic resilience → PRACTICE / CRITIQUE.
- `I004`: concurrent edit/conflict/merge/recovery → PRACTICE / CRITIQUE.
- Next IDs remain Layout `L006`; Interaction `I005`.
- No PASS promotion claimed.
