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
Overall state: **CRITIQUE** in studied modules  
Foundation: **NOT PASSED**

Spatial evidence remains under `research/layout/`; temporal/behavioral evidence remains under `research/interaction/`.

---

## Four-specialist sync

Latest synchronized peer state:

- **Type:** through `T006`; source→CFF/TTF production-outline transfer now exists in addition to T004 numerals and T005 Latin/Korean fallback evidence.
- **Color:** through `C009`; C007 independently confirms L005 fixed-geometry density/salience findings, while C009 shows fixed semantic Color pairs do not normalize Type weight/fallback rendering or spatial footprint.
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
- `L006-pointer-capture-touch-lost-invoker-transfer.md` + specimen/Playwright/results
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

# Latest completed block — L006 higher-fidelity layer ownership

L006 now spans three evidence layers:

1. custom visual/interaction ownership pairs;
2. native HTML popover/dialog transfer;
3. transition-time pointer capture, touch, nested dismissal and lost-invoker recovery.

## 1. Custom paired proof

Three broken/revised structures were rendered with pixel-identical foreground/background geometry:

- non-modal popover;
- sticky controls over row content;
- modal sheet over an editor.

Broken versions allowed foreground-looking regions to pass pointer or keyboard ownership to obscured background controls. Revised versions retained the same pixels while repairing hit ownership, background inertness and keyboard containment.

Controlled custom-DOM result: **15/15 assertions PASS**.

Key conclusion:

> A screenshot cannot tell whether the visible foreground owns input, focus, semantics or mutation.

## 2. Native HTML transfer

Chromium `144.0.7559.96`:

### Native popover
- shown popover owns its overlap coordinate;
- underlying action does not fire;
- non-modal popover does not globally inert the page.

### Native `<dialog>.showModal()`
- modal enters top-layer modality;
- outside pointer activation is blocked;
- tested keyboard traversal did not reach background page controls;
- nested popover can become the topmost hit owner;
- closing the dialog restored focus to the invoker in the bounded case.

Important limitation:

- `document.activeElement` transiently became `<body>` at some Tab/Shift+Tab boundaries;
- therefore outside controls were unreachable, but strict “activeElement is always a dialog descendant” was not established.

This keeps HTML modal inertness distinct from the stronger APG cyclic focus-containment pattern.

Native-primitives matrix: **13/13 bounded assertions PASS**.

## 3. Pointer capture / touch / nested dismissal / lost invoker

New controlled Chromium matrix: **13/13 assertions PASS**.

### Failure reproduced — captured background gesture survives modal entry

Sequence:

- background drag receives `pointerdown`;
- `setPointerCapture()` succeeds;
- modal `showModal()` opens while pointer remains down;
- pointer moves over the visible modal action;
- captured background still receives subsequent moves and `pointerup`;
- controlled background drag commit becomes `1`.

Observed broken event path included:

`gotpointercapture → move… → modal opens → move… → pointerup(capture=true, commit=true) → lostpointercapture`

Therefore, in this Chromium run:

> **modal inertness did not cancel a pointer stream that was already captured before the modal transition.**

### Revision

Before modal entry:

- explicitly release capture;
- cancel the underlying gesture/data commit;
- then open the modal.

Observed revised result:

- `lostpointercapture` occurs before modal interaction proceeds;
- no background `pointerup` commit is used;
- background drag commit changes `1 → 0`.

### Touch overlap transfer

With a Playwright touch source and popover/underlay controls at the same coordinate:

- hit testing resolved to the popover action;
- foreground touch action count = `1`;
- underlying action count = `0`.

This is bounded Chromium touch evidence, not physical mobile-browser PASS.

### Nested dismissal stack

Controlled stack:

`page → modal dialog → nested auto popover`

Observed:

- first `Escape` dismisses the topmost popover only;
- second `Escape` dismisses the parent dialog;
- focus returns to the parent dialog invoker when that invoker remains present.

### Lost invoker

When the dialog opener is removed before dismissal:

- native dismissal settled with focus on `BODY` rather than an adjacent logical workflow control.

With an explicit application fallback:

- focus moves to the declared logical fallback control.

This confirms I001/APG continuity logic: “return to opener” is conditional, not universal.

## Updated ownership vector

Layer review now records separately:

`visual owner / pointer hit owner / active gesture-capture owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position / restoration target`

The new distinction is critical:

- **pointer hit owner** describes a new hit now;
- **active gesture-capture owner** describes an input stream that may have started before the layer transition.

They can differ.

## Professional rules from L006

- modal transition requires an explicit policy for active drag/resize/press-hold gestures;
- do not assume `inert`, backdrop or top-layer entry cancels prior pointer capture;
- nested overlays are a stack, not one foreground/background boolean;
- one Escape/back action should have a defined topmost dismissal target;
- focus restoration needs a lost-invoker fallback when the opener can disappear;
- visual elevation cannot establish pointer/focus/gesture/data ownership by itself;
- modal testing must include reverse Tab, active-gesture transition and dismissal restoration.

Evidence level: **PRACTICE + CRITIQUE / realistic + native-browser + transition-time input validation**.

Not PASS: Firefox/Safari, physical iOS/Android, touch drag/implicit capture, stylus/multi-touch, AT, browser chrome, framework portals, native frameworks and human layer comprehension remain open.

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

## Cross-specialist evidence affecting this role

### Type — through T006

- L003/L004 already establish browser-level Layout transfer for fallback/numerals.
- T006 adds source→CFF/TTF evidence: technically clean production-outline/export changes can still alter compact raster coverage.
- Consequence for Layout: use delivered font builds near wrapping, numeric-column and overlay-boundary thresholds; do not validate geometry from source/editor appearance alone.

### Color — through C009

- C007 ↔ L005 remains **CONFIRMATION + COMPLEMENTARY METHOD**.
- C009 shows identical semantic foreground/background pairs can render with materially different Type weight/fallback coverage and can cross wrap thresholds while Color values remain fixed.
- Consequence for Layout: do not use Color changes to disguise Type/Layout fallback failures; overlay and dense-surface geometry must be retested with actual fallback/render conditions.
- L006 reciprocally shows pixel-identical appearance can hide opposite interaction/gesture ownership.

### Web Design

No substantive `W###` at latest synchronization.

Web should independently reproduce L001–L006 and I001–I004 inside complete page/component systems, especially:

- native `<dialog>` and `popover`;
- framework portals/overlay managers;
- active pointer capture during modal transitions;
- sticky headers/toolbars;
- lost-invoker restoration;
- production focus/inertness/AT behavior;
- actual font loading/localization/zoom;
- Firefox/Safari/mobile/browser-OS matrices.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real-rendering proof; text-growth/cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue isolation + realistic L006 transfer complete; blinded observers and broader platform transfer pending |
| Layer ownership / visual-interaction coupling | **PRACTICE / CRITIQUE** | custom 15 + native 13 + higher-fidelity 13 assertion matrices; Firefox/Safari/mobile/AT, implicit touch capture, framework/native and human evidence pending |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | stronger centroid datasets; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | raster mass/size/DPR proof; blinded human comparison, physical device, icon+text/RTL/platform transfer pending |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | L002 rendered cycle complete; human task/broader project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002/L003 evidence; actual zoom/cross-browser/device/production page transfer pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | L003/L004 + T006 dependency established; production delivered-font/cross-platform/human evidence pending |
| Dense numeric comparison geometry | PRACTICE / CRITIQUE | L004 proof; locale/accounting/dynamic-update/human comparison evidence pending |
| Color-driven feature density / salience | PRACTICE / CRITIQUE | L005 + independent C007 confirmation; C009 Type/Color transfer noted; human task/CVD/device/environment pending |
| Interaction agency / feedback / errors | CRITIQUE | broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device/human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |
| Color-channel-independent state semantics | PRACTICE / CRITIQUE | real OS/other browsers/AT/production token-component/human evidence pending |
| Concurrent edits / conflict / merge / recovery | PRACTICE / CRITIQUE | real service/offline/multi-device/CRDT-OT/AT/human validation pending |

---

## Active next queue

1. **Human evidence when participants are available**
   - L001 border ownership Left/Right/Ambiguous judgments;
   - L001 optical `0/+δ/−δ` perceived-centering comparisons;
   - L002/L005/C007 known-item search/comparison/action/error tests.
2. **L006 remaining higher-fidelity transfer**
   - Firefox/Safari and physical mobile browsers;
   - screen reader / AT layer ownership;
   - touch drag/implicit capture, stylus, multi-touch and OS gesture competition;
   - framework portals/overlay managers;
   - forced-colors/reduced-visual-effect conditions;
   - complex lost-invoker/replacement cases.
3. **I004 higher-fidelity transfer** — real ETag/If-Match or transaction backend, offline/reconnect, multi-device/tab, delete/finalization semantics and AT.
4. **L004 extension only if project-relevant** — delivered production font/exact T004, locale/accounting formats, dynamic updates, actual zoom/DPR.
5. **I003 higher-fidelity transfer** — real OS high-contrast/AT/production tokens.
6. Consume future W### evidence and independently reproduce high-risk findings where useful.
7. Open `L007` or `I005` only for a genuinely new question with higher value than these validation gaps.

---

## Open research-quality gaps

- actual observer judgments for border ownership, grouping, balance and optical centering;
- human perceived-clutter/search/comparison/action evidence for L002/L005/C007;
- human layer-ownership/comprehension evidence in realistic overlays;
- screen-reader/AT layer ownership and modal/non-modal semantics;
- Firefox/Safari/browser-chrome focus behavior;
- physical mobile-browser layer behavior;
- touch drag/implicit pointer capture, stylus, multi-touch and OS gesture arbitration;
- nested portal/overlay ownership beyond native bounded cases;
- complex lost-invoker replacement/restoration;
- actual browser zoom rather than synthetic scaling;
- production font loading/fallback and exact delivered-font regression;
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
- T006 increases the need to regression-test actual delivered font output near those thresholds.
- L006 adds overlay/localization cases where wrapping can change boundaries, hit regions and restoration targets.
- Scope limit: Layout/Interaction does not define font/glyph production decisions.

### Color

- C007 ↔ L005 remains **CONFIRMATION + COMPLEMENTARY METHOD**.
- C009 reinforces that semantic Color values do not normalize Type/rendered geometry.
- L006 shows appearance, inertness and active gesture ownership are separate; more elevation/color cannot cancel a captured background pointer stream.
- Scope limit: no human salience or Color threshold claim.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- diagnose “busy/dense” across spatial density, feature variability, emphasis distribution and semantic collision;
- border ownership is contextual; diagnose remote cues while controlling local edges;
- visual owner, new-hit owner, active gesture/capture owner, focus owner, semantic owner, data owner, stack position and restoration target are distinct contracts;
- a screenshot cannot validate overlay interaction ownership;
- modal and non-modal ownership require different background policies;
- modal transition during an active gesture needs an explicit finish/cancel/release policy;
- `inert`/top-layer entry does not prove prior pointer capture was canceled;
- modal testing must include `Shift+Tab`, active gesture transitions, topmost-first dismissal and lost-invoker restoration;
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

Reusable transfer evidence now includes:

- L001 border ownership: local-edge cue-isolation set + blinded observer protocol;
- L001 optical centering: fixed-target raster/size/DPR matrix;
- L002: 216-condition density/reflow matrix;
- L003: mixed-script fallback/wrap-threshold/semantic-lane transfer;
- L004: tabular numeral/decimal/intrinsic-width transfer;
- L005 + C007: independent fixed-geometry Color/feature-density validation;
- L006 custom: **15-assertion visual/pointer/keyboard ownership matrix**;
- L006 native: **13-assertion popover/dialog/top-layer/inertness matrix**;
- L006 higher fidelity: **13-assertion pointer-capture/touch/nested-dismissal/lost-invoker matrix**;
- I001: 14-assertion navigation/state matrix;
- I002: 19-assertion latency/retry/cancel matrix;
- I003: 14-assertion forced-colors matrix;
- I004: 17-assertion conflict matrix.

Web should reproduce these with production components, portals, delivered fonts/tokens, zoom/localization, router/API/offline behavior, target browser/device matrix, OS accessibility modes and AT.

---

## Latest checkpoint

- `L001`: optical raster + border cue isolation → **PRACTICE / CRITIQUE**; observer judgments OPEN.
- `L002`: density validation → **PRACTICE / CRITIQUE**.
- `L003`: T005 fallback→Layout transfer → **PRACTICE / CRITIQUE**.
- `L004`: browser `tnum`/decimal/intrinsic-width transfer → **PRACTICE / CRITIQUE**.
- `L005`: fixed-geometry Color→Layout transfer → **PRACTICE / CRITIQUE**; independently confirmed/complemented by C007.
- `L006`: custom **15/15** + native **13/13** + higher-fidelity pointer/touch/restoration **13/13 bounded assertions** → **PRACTICE / CRITIQUE**.
- `I001`: navigation/state → **CRITIQUE**.
- `I002`: async/retry/cancel → **PRACTICE / CRITIQUE**.
- `I003`: forced-colors resilience → **PRACTICE / CRITIQUE**.
- `I004`: concurrent edit/conflict/merge/recovery → **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L007`; Interaction `I005`.
- No PASS promotion claimed.
