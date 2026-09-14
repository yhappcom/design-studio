# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L007`; Interaction `I005`

This file is maintained by the Layout, Spatial & Interaction Specialist. It must not update global `progress/STATUS.md` during ordinary research.

## Operational mission

This specialist studies spatial organization and interaction to improve real app, web and product decisions. Research volume and curriculum speed are not success metrics.

For live projects, accumulated evidence must become project-specific guidance on hierarchy, grouping, density, responsive behavior, navigation, state, feedback, latency, concurrency, recovery, layer ownership, target placement, accessibility, localization, platform/device constraints, implementation trade-offs, validation, uncertainty and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules; Foundation is **not passed**.

Spatial evidence stays under `research/layout/`; temporal/behavioral evidence stays under `research/interaction/`.

## Four-specialist sync

Latest relevant peer state:

- **Type:** through `T005`; numeral/runtime and Latin/Korean fallback evidence remain active transfer inputs.
- **Color:** through `C007`; its fixed-geometry density/salience study independently confirms and complements Layout L005.
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
- `research/layout/L006-layer-ownership-cross-contract.md`
- `research/layout/L006-layer-ownership-specimen.html`
- `research/layout/L006-layer-ownership-playwright.py`
- `research/layout/L006-layer-ownership-results-summary.json`
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

## Latest completed block — L006 layer ownership cross-contract

L006 transfers L001 figure-ground/border ownership into realistic overlapping UI and couples it to Interaction ownership.

### Controlled pair design

Three paired structures were rendered:

1. non-modal popover;
2. sticky controls over row content;
3. modal sheet over an editor.

For every broken/revised pair:

- foreground/background geometry is identical;
- borders/shadows/surfaces are identical;
- foreground/background actions are placed at the same screen coordinate;
- workspace screenshots are pixel-identical;
- foreground-layer screenshots are pixel-identical.

Only behavioral ownership differs.

### Broken failure reproduced

Broken foreground layers use `pointer-events:none`.

At the visible foreground-action coordinate:

- popover: background `Delete record` receives the click;
- sticky layer: underlying row action receives the click;
- modal sheet: background commit action receives the click.

Modal keyboard failure is also reproduced:

`foreground Confirm → Shift+Tab → background input → Shift+Tab → background Commit`.

This proves that visual elevation/boundary treatment does not itself establish interaction ownership.

### Revised re-proof

Revised layers keep the same pixels but:

- foreground receives pointer input in its visible overlap;
- modal background is `inert`;
- both forward and reverse keyboard traversal remain inside the modal task.

Controlled Chromium result: **15 / 15 assertions PASS**.

### Ownership vector

For layered components, record separately:

`visual owner / pointer owner / keyboard-focus owner / semantic-AT owner / action-data owner`

Expected contracts differ by modality:

- non-modal popover: foreground owns its overlap, while outside background may remain interactive;
- sticky header/toolbar: foreground owns the covered region only;
- modal sheet/dialog: foreground owns the active task and underlay is inert.

### Evidence level

**PRACTICE + CRITIQUE / realistic L001 transfer + Interaction coupling**.

Not PASS: human layer perception, screen reader/AT, touch/gesture/pointer capture, nested overlays, production `popover`/`dialog`, framework portals, other browsers/OS/native platforms and focus restoration remain open.

---

## Important established blocks

### L001 figure-ground / optical centering

**Border ownership cue isolation**
- baseline plus enclosure, contour-junction, attachment/continuity and cue-conflict mirror pairs;
- all nine stimuli use a pixel-identical local shared-edge crop after failure→revision;
- blinded Left/Right/Ambiguous observer protocol is ready;
- no human ownership data fabricated.

**Optical centering**
- fixed 48×48 hit target;
- six asymmetric shapes;
- 16/24/32/40px visual sizes and DPR1/2;
- raster darkness-centroid shows no universal optical-offset token;
- shape, size and axis alter the measured candidate;
- raster mass remains diagnostic, not human perceived center.

### L002 density / spatial rhythm

**216-condition Chromium validation** rejected fake compactness from clipping/undersized targets. Adaptive density preserves semantic content, required targets and grouping while compressing discretionary whitespace.

### L003 Type fallback → Layout

Four T005-compatible Latin/Korean fallback stacks crossed different browser wrap thresholds. Semantic-lane recomposition stabilized critical object identity instead of font-specific breakpoints.

### L004 tabular numerals → dense Layout

Chromium controls showed zero DOM digit/decimal spread under `tabular-nums`, while Inter tabular figures widened an 88px placeholder-derived track enough to create overflow. Intrinsic numeric width fixed the Layout failure.

### L005 Color → Layout

Fixed-geometry rendering separates spatial density from Color-driven feature variability and semantic collision. Color C007 independently confirms the main direction with complementary metrics.

### I001 navigation as state

Back/Up/Close/deep-link/workspace/focus/draft model; **14/14 controlled assertions PASS** after failure→revision→re-proof.

### I002 latency / pending / retry / cancellation

Separates confirmed/failed/**outcome unknown**, ties Retry/Cancel to operation/data contracts; **19/19 controlled assertions PASS**.

### I003 forced-colors state resilience

Fill/shadow-only state failures reproduced; structural/text/programmatic cues survive; **14/14 controlled assertions PASS**.

### I004 concurrent edits / conflict / merge / recovery

Naive whole-record save reproduced a lost update; version-aware flow distinguishes disjoint merge, same-field conflict and delete-vs-edit; **17/17 controlled assertions PASS**.

---

## Cross-specialist comparison — Color C007 ↔ Layout L005

Classification: **CONFIRMATION + COMPLEMENTARY METHOD**.

Both studies independently establish under fixed geometry that:

- distributed chroma can materially change the rendered feature field without changing spatial density;
- zero/low chroma does not guarantee a calmer field because luminance segmentation may remain strong;
- semantic emphasis should be localized by task value rather than assigned to every difference;
- screenshot/image proxies are not human perceived-clutter or performance measures.

Complement:
- L005 adds explicit semantic-collision diagnosis;
- C007 adds stronger local feature/action-region comparison.

Do not merge the studies or promote either proxy into a universal clutter score.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real-rendering proof; text-growth/cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context and human observation |
| Figure-ground / border ownership | **PRACTICE / CRITIQUE** | cue isolation + realistic L006 transfer complete; blinded observers, production layering and broader platform transfer pending |
| Layer ownership / visual-interaction coupling | **PRACTICE / CRITIQUE** | L006 15-assertion proof; AT, touch/gesture, nested overlays, native/browser/framework transfer and human layer judgment pending |
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

Type is through T005.

- L003/L004 provide browser transfer evidence for fallback and numeric-feature dependencies.
- L001 optical/border work reinforces separation of source geometry, raster result and human perception.
- L006 creates future localization stress cases because text growth can move overlay edges/hit regions.

### Color

Color is through C007.

- C001/C002/I003: critical state meaning must survive authored color replacement.
- C003: data color and interaction state remain separate semantics.
- C006: action/selection/focus/status remain separate semantic jobs.
- C007 independently confirms L005 and rejects `desaturate = declutter`.
- L006 demonstrates the reciprocal boundary: identical color/elevation pixels can still encode the wrong interaction owner.

### Web Design

No substantive W### at latest synchronization.

Web should reproduce L001–L006 and I001–I004 inside complete page/component systems, especially:

- native `<dialog>` and `popover`;
- framework portals/overlay managers;
- sticky headers/toolbars;
- production focus/inertness handling;
- actual font loading/localization/zoom;
- multiple browser/OS/device/AT combinations.

---

## Active next queue

Choose by expected project value, not file count.

1. **Human evidence when participants are available**
   - L001 border ownership Left/Right/Ambiguous judgments;
   - L001 optical `0/+δ/−δ` perceived-centering comparisons;
   - L002/L005/C007 known-item search/comparison/action/error tests;
   - separate performance/error from preference/workload.
2. **L006 higher-fidelity layer transfer**
   - actual `<dialog>` / `popover`;
   - nested overlays;
   - touch/gesture/pointer capture;
   - focus restoration;
   - forced-colors/reduced-visual-effect conditions;
   - production framework portals when Web/project context exists.
3. **I004 higher-fidelity transfer**
   - real ETag/If-Match or transaction backend;
   - offline/reconnect;
   - multi-device/tab;
   - delete/finalization semantics;
   - AT.
4. **L004 extension only if project-relevant**
   - production font / exact T004;
   - locale/accounting formats;
   - dynamic numeric updates;
   - actual zoom/DPR.
5. **I003 higher-fidelity transfer**
   - real OS high-contrast/AT/production tokens.
6. Consume future W### evidence and independently reproduce high-risk findings where useful.
7. Open `L007` or `I005` only for a genuinely new question with higher value than current validation gaps.

---

## Open research-quality gaps

- actual observer judgments for border ownership, grouping, balance and optical centering;
- human perceived-clutter/search/comparison/action evidence for L002/L005/C007;
- validated feature-congestion/equivalent metric transfer to UI specimens;
- human layer-ownership/comprehension evidence in realistic overlays;
- screen-reader/AT layer ownership and modal/non-modal semantics;
- touch/gesture/pointer-capture behavior across layered surfaces;
- nested overlay and portal ownership;
- focus restoration after dismissal;
- actual browser zoom rather than synthetic scaling;
- production font loading/fallback and exact T004 browser transfer;
- real OS forced-color/high-contrast environments;
- real multi-device/offline conflict and sync reconciliation;
- CRDT/OT/list/text/order conflicts where relevant;
- real router/history and service/network evidence;
- interruption/resumption evidence on representative tasks;
- stronger future Web integration.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- L003 confirms fallback width can cross Layout thresholds.
- L004 confirms browser tabular alignment while exposing numeric-column width cost.
- L001 optical/border work reinforces method isolation across geometry/raster/perception.
- L006 adds overlay/localization cases where wrapping can change boundary and hit-test geometry.
- Scope limit: Layout/Interaction does not define font/glyph production decisions.

### Color

- C007 ↔ L005 remains **CONFIRMATION + COMPLEMENTARY METHOD**.
- L006 shows that pixel-identical visual layers can have opposite interaction ownership, so elevation/color treatment cannot establish behavior by itself.
- L006 should later be transferred to forced-colors/dark/reduced-effect conditions without using extra color as a behavioral fix.
- Scope limit: no human salience or color threshold claim.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- diagnose “busy/dense” across spatial density, feature variability, emphasis distribution and semantic collision;
- border ownership is contextual; diagnose remote cues while controlling local edges;
- visual ownership, pointer ownership, keyboard ownership, semantic ownership and data ownership are separate contracts;
- a screenshot cannot validate overlay interaction ownership;
- modal and non-modal ownership require different background policies;
- modal keyboard testing must include `Shift+Tab`, not only forward Tab;
- dimming does not create inertness;
- optical correction starts geometric, keeps the hit target fixed and remains shape/size/context-specific;
- raster centroid is diagnostic, not human perceived center;
- enable approved numeric features before finalizing numeric tracks;
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
- L003: mixed-script fallback/wrap-threshold/semantic-lane transfer;
- L004: browser tabular-numeral/decimal/intrinsic-width transfer;
- L005 + C007: independent fixed-geometry Color/feature-density validation;
- L006: **15-assertion layered visual/pointer/keyboard ownership matrix**;
- I001: 14-assertion navigation/state matrix;
- I002: 19-assertion latency/retry/cancel matrix;
- I003: 14-assertion forced-colors matrix;
- I004: 17-assertion conflict matrix.

Web should reproduce these with production components, actual browser primitives, portals, fonts/tokens, zoom/localization, router/API/offline behavior, target browser/device matrix, OS accessibility modes and AT.

---

## Latest checkpoint

- `L001`: optical raster validation + border-ownership cue isolation → **PRACTICE / CRITIQUE**; observer judgments OPEN.
- `L002`: density validation → **PRACTICE / CRITIQUE**.
- `L003`: T005 fallback→Layout transfer → **PRACTICE / CRITIQUE**.
- `L004`: browser `tnum`/decimal/intrinsic-width transfer → **PRACTICE / CRITIQUE**.
- `L005`: fixed-geometry Color→Layout transfer → **PRACTICE / CRITIQUE**; independently confirmed/complemented by C007.
- `L006`: realistic layer-ownership visual/pointer/keyboard transfer → **PRACTICE / CRITIQUE**, 15/15 controlled assertions.
- `I001`: navigation/state validation → **CRITIQUE**.
- `I002`: async/retry/cancel validation → **PRACTICE / CRITIQUE**.
- `I003`: forced-colors semantic resilience → **PRACTICE / CRITIQUE**.
- `I004`: concurrent edit/conflict/merge/recovery → **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L007`; Interaction `I005`.
- No PASS promotion claimed.
