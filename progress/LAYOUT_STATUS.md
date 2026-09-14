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

- **Type:** through `T005`; numeral/runtime and Latin/Korean fallback evidence remain active transfer inputs.
- **Color:** through `C007`; its fixed-geometry density/salience study independently confirms and complements Layout L005.
- **Web:** no substantive `W###` yet; `W001` remains next. Do not invent Web evidence.

Web remains the complete page/browser integration partner. Layout/Interaction may independently validate browser behavior in its own domain when useful, without replacing Web canonical ownership.

---

## Canonical evidence

### Layout / spatial

- `006-grid-composition-hierarchy.md`
- `014-perceptual-grouping-spatial-grammar.md`
- `L001-figure-ground-balance-optical-centering.md`
- `L001-optical-centering-raster-validation.md` + Playwright/results
- `L001-border-ownership-cue-isolation-validation.md` + specimen/Playwright/results
- `L002-whitespace-density-spatial-rhythm.md` + 216-condition validation artifacts
- `L003-type-fallback-density-reflow-transfer.md` + Playwright/results
- `L004-tabular-numerals-dense-comparison-transfer.md` + Playwright/results
- `L005-color-driven-density-salience-transfer.md` + Playwright/results
- `L006-layer-ownership-cross-contract.md` + specimen/Playwright/results
- `L006-native-layer-primitives-transfer.md` + specimen/Playwright/results
- retained earlier grid/responsive/grouping/L001 product-design exercises.

### Interaction

- `007-interaction-agency-feedback-errors.md`
- `015-directness-state-modes-reversibility.md`
- `I001-navigation-history-focus-restoration-interruption.md` + 14-assertion validation
- `I002-latency-pending-optimistic-retry.md` + 19-assertion validation
- `I003-forced-colors-state-semantic-resilience.md` + 14-assertion validation
- `I004-concurrent-edits-conflict-merge-recovery.md` + 17-assertion validation
- retained state-matrix / Study 015 practice evidence.

### Shared accessibility evidence

- `research/004-accessibility-reflow-targets-focus.md`
- retained accessibility geometry practice/critique.

---

## Latest completed block — L006 layer ownership

L006 transfers L001 figure-ground/border ownership into realistic overlapping UI and couples it to Interaction ownership.

### Custom paired proof

Three structures were rendered as broken/revised pairs:

1. non-modal popover;
2. sticky controls over row content;
3. modal sheet over an editor.

For every pair:

- foreground/background geometry is identical;
- borders/shadows/surfaces are identical;
- foreground/background actions share the same screen coordinate;
- workspace and foreground screenshots are pixel-identical.

Only behavioral ownership differs.

#### Broken result

With the visual foreground using `pointer-events:none`:

- popover: visible foreground action position activates background `Delete record`;
- sticky layer: visible `Filter` position activates the row beneath;
- modal sheet: visible `Confirm` position activates background commit;
- reverse keyboard traversal escapes: `Confirm → background input → background Commit`.

#### Revised result

The same pixels are retained while:

- foreground receives pointer input inside its visible overlap;
- modal background is `inert`;
- forward and reverse traversal stay within the foreground task.

Controlled custom-DOM result: **15/15 assertions PASS**.

### Native HTML transfer

The same ownership contract was then tested with actual browser primitives in Chromium `144.0.7559.96`.

#### Native popover

Confirmed:

- `:popover-open` is active;
- overlap hit-testing resolves to the popover action;
- underlying action does not fire;
- opening a non-modal popover does **not** globally inert the page.

#### Native `<dialog>.showModal()`

Confirmed:

- dialog enters `:modal` / top-layer modality;
- background pointer activation is blocked;
- controlled keyboard traversal never reached background page controls;
- a nested popover inside the modal becomes the topmost hit owner;
- closing the dialog restores focus to the invoker in the controlled case.

Important limitation:

- `document.activeElement` transiently became `<body>` at some Tab/Shift+Tab boundaries;
- therefore **background controls were not reached**, but **strict “activeElement always remains a dialog descendant” containment was false** in this run.

This distinguishes HTML modal inertness/top-layer behavior from the stronger APG cyclic focus-containment interaction pattern.

Native-primitives matrix: **13/13 PASS for the bounded assertions**.

### Ownership vector

For layered components, record separately:

`visual owner / pointer owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position`

Modality changes the contract:

- non-modal popover: foreground owns its overlap; outside background may remain active;
- sticky header/toolbar: foreground owns the region it covers, not the whole page;
- modal sheet/dialog: foreground owns the active task; underlay is inert;
- nested overlays: ownership is a stack, not a single foreground/background boolean.

### Evidence level

**PRACTICE + CRITIQUE / realistic L001 transfer + Interaction coupling + bounded native-browser transfer**.

Not PASS: human layer perception, screen-reader/AT, browser-chrome focus behavior, Firefox/Safari/mobile, touch/gesture/pointer capture, framework portals, lost-invoker cases, production content/localization and native mobile remain open.

---

## Other established blocks

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
- shape, size and axis alter the candidate;
- raster mass remains diagnostic, not perceived center.

### L002 density / spatial rhythm

**216-condition Chromium validation** rejected fake compactness from clipping/undersized targets. Adaptive density preserves semantic content, required targets and grouping while compressing discretionary whitespace.

### L003 Type fallback → Layout

Four T005-compatible Latin/Korean fallback stacks crossed different browser wrap thresholds. Semantic-lane recomposition stabilized critical object identity instead of font-specific breakpoints.

### L004 tabular numerals → dense Layout

Chromium control fonts showed zero DOM digit/decimal spread under `tabular-nums`; enabling tabular numerals widened Inter enough to break an 88px placeholder-derived track. Intrinsic numeric width removed overflow.

### L005 Color → Layout

Fixed-geometry rendering separates spatial density from Color-driven feature variability and semantic collision. Color C007 independently confirms the main direction with complementary metrics.

### I001–I004

- I001 navigation/state: **14/14** controlled assertions.
- I002 async/retry/cancel: **19/19** controlled assertions.
- I003 forced-colors state resilience: **14/14** controlled assertions.
- I004 concurrent edit/conflict/merge/recovery: **17/17** controlled assertions.

None is production PASS.

---

## Cross-specialist comparison — Color C007 ↔ Layout L005

Classification: **CONFIRMATION + COMPLEMENTARY METHOD**.

Both studies independently establish under fixed geometry that:

- distributed chroma can materially change the rendered feature field without changing spatial density;
- zero/low chroma does not guarantee a calmer field because luminance segmentation may remain strong;
- semantic emphasis should be localized by task value rather than assigned to every difference;
- screenshot/image proxies are not human perceived-clutter/performance measures.

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
| Figure-ground / border ownership | **PRACTICE / CRITIQUE** | cue isolation + realistic L006 transfer complete; blinded observers and broader platform transfer pending |
| Layer ownership / visual-interaction coupling | **PRACTICE / CRITIQUE** | custom 15-assertion + native 13-assertion proof; strict focus-policy nuance, AT, touch/gesture, cross-browser/native/framework and human layer judgment pending |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | stronger centroid datasets; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | raster mass/size/DPR proof; blinded human comparison, physical device, icon+text/RTL/platform transfer pending |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | L002 rendered cycle complete; human task/broader project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002/L003 evidence; actual zoom/cross-browser/device/production page transfer pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | L003 fallback + L004 numeric transfer; production-font/cross-platform/human evidence pending |
| Dense numeric comparison geometry | PRACTICE / CRITIQUE | L004 proof; locale/accounting/dynamic-update/human comparison evidence pending |
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
- L001 reinforces separation of source geometry, raster result and perception.
- L006 adds future localization stress cases because text growth can move overlay edges/hit regions.

### Color

Color is through C007.

- C001/C002/I003: critical state meaning must survive authored color replacement.
- C003: data color and interaction state remain separate semantics.
- C006: action/selection/focus/status remain separate jobs.
- C007 independently confirms L005 and rejects `desaturate = declutter`.
- L006 proves the reciprocal boundary: pixel-identical visual layers can still have opposite interaction ownership.

### Web Design

No substantive W### at latest synchronization.

Web should independently reproduce L001–L006 and I001–I004 inside complete page/component systems, especially:

- native `<dialog>` and `popover`;
- framework portals/overlay managers;
- sticky headers/toolbars;
- production focus/inertness/restoration handling;
- actual font loading/localization/zoom;
- browser/OS/device/AT matrices.

---

## Active next queue

1. **Human evidence when participants are available**
   - L001 border ownership Left/Right/Ambiguous judgments;
   - L001 optical `0/+δ/−δ` perceived-centering comparisons;
   - L002/L005/C007 known-item search/comparison/action/error tests.
2. **L006 higher-fidelity layer transfer**
   - Firefox/Safari/mobile and AT;
   - browser-chrome / strict focus-scope behavior;
   - touch/gesture/pointer capture;
   - lost-invoker and nested overlay/portal stacks;
   - forced-colors/reduced-visual-effect conditions;
   - production framework portals when Web/project context exists.
3. **I004 higher-fidelity transfer** — real ETag/If-Match or transaction backend, offline/reconnect, multi-device/tab, delete/finalization semantics and AT.
4. **L004 extension only if project-relevant** — production font/exact T004, locale/accounting formats, dynamic updates, actual zoom/DPR.
5. **I003 higher-fidelity transfer** — real OS high-contrast/AT/production tokens.
6. Consume future W### evidence and independently reproduce high-risk findings where useful.
7. Open `L007` or `I005` only for a genuinely new question with higher value than current validation gaps.

---

## Open research-quality gaps

- actual observer judgments for border ownership, grouping, balance and optical centering;
- human perceived-clutter/search/comparison/action evidence for L002/L005/C007;
- human layer-ownership/comprehension evidence in realistic overlays;
- screen-reader/AT layer ownership and modal/non-modal semantics;
- browser-chrome and strict focus-scope behavior for modal dialogs;
- touch/gesture/pointer capture across layers;
- nested overlay/portal ownership beyond the bounded popover-inside-dialog case;
- lost-invoker restoration and complex dismissal stacks;
- actual browser zoom rather than synthetic scaling;
- production font loading/fallback and exact T004 browser transfer;
- real OS forced-color/high-contrast environments;
- real multi-device/offline conflict and sync reconciliation;
- CRDT/OT/list/text/order conflict behavior where relevant;
- real router/history and service/network evidence;
- interruption/resumption evidence on representative tasks;
- stronger future Web integration.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- L003 confirms fallback width can cross Layout thresholds.
- L004 confirms browser tabular alignment while exposing numeric-column width cost.
- L001 reinforces geometry/raster/perception method isolation.
- L006 adds overlay/localization cases where wrapping can change boundary and hit-test geometry.
- Scope limit: Layout/Interaction does not define font/glyph production decisions.

### Color

- C007 ↔ L005 remains **CONFIRMATION + COMPLEMENTARY METHOD**.
- L006 shows pixel-identical visual layers can have opposite interaction ownership, so elevation/color treatment cannot establish behavior by itself.
- Future L006 transfer should test forced-colors/dark/reduced-effect conditions without using extra color as a behavioral fix.
- Scope limit: no human salience or color threshold claim.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- diagnose “busy/dense” across spatial density, feature variability, emphasis distribution and semantic collision;
- border ownership is contextual; diagnose remote cues while controlling local edges;
- visual, pointer, keyboard, semantic, data ownership and layer-stack position are separate contracts;
- a screenshot cannot validate overlay interaction ownership;
- modal and non-modal ownership require different background policies;
- modal testing must include `Shift+Tab`, not only forward Tab;
- distinguish `outside controls are inert/unreachable` from the stronger `activeElement always stays on a dialog descendant` contract;
- native `showModal()` provides valuable modality/inertness but does not remove target-browser keyboard/AT validation;
- nested overlays require ownership-stack reasoning;
- dimming does not create inertness;
- optical correction starts geometric, keeps hit target fixed and remains shape/size/context-specific;
- raster centroid is diagnostic, not perceived center;
- timeout, failure and outcome-unknown are distinct;
- retry is not conflict resolution;
- auto-merge only when semantic independence is established;
- preserve local drafts across conflict;
- critical state meaning must survive authored color-channel loss.

### Web Design

Reusable transfer evidence:

- L001 border ownership: pixel-identical local-edge cue-isolation set + blinded observer protocol;
- L001 optical centering: fixed-target raster/size/DPR matrix;
- L002: 216-condition density/reflow matrix;
- L003: mixed-script fallback/wrap-threshold/semantic-lane transfer;
- L004: browser tabular-numeral/decimal/intrinsic-width transfer;
- L005 + C007: independent fixed-geometry Color/feature-density validation;
- L006 custom: **15-assertion visual/pointer/keyboard ownership matrix**;
- L006 native: **13-assertion popover/dialog/top-layer/inertness/restoration matrix**, including a strict-focus-containment limitation;
- I001: 14-assertion navigation/state matrix;
- I002: 19-assertion latency/retry/cancel matrix;
- I003: 14-assertion forced-colors matrix;
- I004: 17-assertion conflict matrix.

Web should reproduce with production components, portals, fonts/tokens, zoom/localization, router/API/offline behavior, target browser/device matrix, OS accessibility modes and AT.

---

## Latest checkpoint

- `L001`: optical raster + border cue isolation → **PRACTICE / CRITIQUE**; observer judgments OPEN.
- `L002`: density validation → **PRACTICE / CRITIQUE**.
- `L003`: T005 fallback→Layout transfer → **PRACTICE / CRITIQUE**.
- `L004`: browser `tnum`/decimal/intrinsic-width transfer → **PRACTICE / CRITIQUE**.
- `L005`: fixed-geometry Color→Layout transfer → **PRACTICE / CRITIQUE**; independently confirmed/complemented by C007.
- `L006`: custom layer ownership **15/15** + native popover/dialog **13/13 bounded assertions**, with strict focus-containment nuance → **PRACTICE / CRITIQUE**.
- `I001`: navigation/state → **CRITIQUE**.
- `I002`: async/retry/cancel → **PRACTICE / CRITIQUE**.
- `I003`: forced-colors resilience → **PRACTICE / CRITIQUE**.
- `I004`: concurrent edit/conflict/merge/recovery → **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L007`; Interaction `I005`.
- No PASS promotion claimed.
