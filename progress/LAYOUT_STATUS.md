# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L007`; Interaction `I005`

This file is maintained by the Layout, Spatial & Interaction Specialist. It must not update global `progress/STATUS.md` during ordinary research.

## Mission / stage

Research exists to improve real app, web and product decisions. Live projects must receive project-specific guidance on hierarchy, grouping, density, responsive behavior, navigation, state, feedback, latency, recovery, concurrency, layer ownership, target placement, accessibility, localization, platform/device and implementation trade-offs.

Current stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules  
Foundation: **NOT PASSED**

Spatial evidence remains under `research/layout/`; behavioral evidence remains under `research/interaction/`.

## Four-specialist sync

- **Type:** through **T007**. Source→CFF/TTF evidence now extends into two-master variable-font compatibility and adversarial intermediate-instance validation. Delivered build + axis value are Layout inputs; a successful build is not proof of correct runtime geometry.
- **Color:** through **C009**. C007 independently confirms L005 fixed-geometry density/salience findings; C009 shows fixed semantic Color pairs do not normalize Type weight/fallback rendering or spatial footprint.
- **Web:** no substantive `W###` yet; `W001` remains next. Do not invent Web evidence.

## Canonical evidence

### Layout
- `006-grid-composition-hierarchy.md`
- `014-perceptual-grouping-spatial-grammar.md`
- `L001-figure-ground-balance-optical-centering.md`
- `L001-optical-centering-raster-validation.md` + Playwright/results
- `L001-border-ownership-cue-isolation-validation.md` + specimen/Playwright/results
- `L002-whitespace-density-spatial-rhythm.md` + **216-condition** validation
- `L003-type-fallback-density-reflow-transfer.md` + Playwright/results
- `L004-tabular-numerals-dense-comparison-transfer.md` + Playwright/results
- `L005-color-driven-density-salience-transfer.md` + Playwright/results
- `L006-layer-ownership-cross-contract.md` + specimen/Playwright/results
- `L006-native-layer-primitives-transfer.md` + specimen/Playwright/results
- `L006-pointer-capture-touch-lost-invoker-transfer.md` + specimen/Playwright/results
- `L006-forced-colors-touch-ax-transfer.md` + specimen/Playwright/results
- `L006-custom-aria-modal-inertness-transfer.md` + specimen/Playwright/results

### Interaction
- `007-interaction-agency-feedback-errors.md`
- `015-directness-state-modes-reversibility.md`
- `I001-navigation-history-focus-restoration-interruption.md` + **14 assertions**
- `I002-latency-pending-optimistic-retry.md` + **19 assertions**
- `I003-forced-colors-state-semantic-resilience.md` + **14 assertions**
- `I004-concurrent-edits-conflict-merge-recovery.md` + **17 controlled assertions**
- `I004-http-precondition-etag-transfer.md` + real HTTP/1.1 ETag/If-Match harness + **16 assertions**

Shared accessibility baseline: `research/004-accessibility-reflow-targets-focus.md`.

---

## Latest completed block — L006 layer ownership

L006 treats layered UI as a cross-contract, not a z-index/elevation question.

Ownership vector:

`visual owner / pointer hit owner / active gesture-capture owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position / restoration target`

Additional consistency check:

`declared semantic modality ↔ actual operational modality`

### 1. Custom visual/interaction ownership — **15/15**

Pixel-identical broken/revised popover, sticky and modal-sheet pairs proved that a foreground can look correct while pointer/focus ownership remains with obscured background controls. Revised pairs repaired hit ownership, inertness and bidirectional focus containment without changing the pixels.

**Rule:** screenshot QA cannot validate overlay interaction ownership.

### 2. Native HTML popover/dialog — **13/13 bounded assertions**

Chromium 144:
- native popover owns its overlap without globally inerting the page;
- `dialog.showModal()` blocks outside pointer interaction and underlay availability;
- nested popover can become topmost;
- close restored focus to the invoker in the bounded case.

Limitation: `activeElement` transiently became `<body>` at some Tab boundaries. Outside controls stayed unreachable, but native modality did not prove the stronger “activeElement always remains a dialog descendant” APG-style focus loop.

### 3. Pointer capture / dismissal / lost invoker — **13/13**

Failure: a background drag with explicit `setPointerCapture()` continued to receive move/up and committed hidden mutation after modal entry.

Revision: release capture + cancel the domain gesture before entering the modal; commit changed `1 → 0`.

Also established:
- bounded touch overlap belonged to foreground;
- `page → modal → nested popover` dismisses topmost-first;
- missing invoker caused native close to fall to `BODY`; explicit logical fallback repaired restoration.

**Rule:** new-hit ownership and already-active gesture/capture ownership are different contracts.

### 4. Forced-colors / touch implicit capture / Chromium AX tree — **28/28**

Forced-colors reciprocal failure:
- shadow-only foreground kept correct hit/action ownership;
- Chromium forced-colors removed `box-shadow`, foreground/page surfaces merged, and an isolated boundary strip lost its distinguishing pixels.

Revision: `outline: 3px solid CanvasText` preserved a system-color-resolved structural boundary. `forced-color-adjust:none` preserved author shadow only as a diagnostic/exception, not a generic fix.

Touch implicit capture:
- direct-manipulation touch began already captured;
- modal entry alone left capture active and hidden background commit occurred;
- explicit release + gesture cancellation changed commit `1 → 0`.

Chromium AX tree:
- non-modal popover adds its region/action while background remains exposed;
- modal dialog removes page background from exposed AX tree;
- nested popover remains inside the modal exposure stack;
- close restores page background exposure.

**Limit:** AX-tree evidence is not screen-reader PASS.

### 5. Custom `aria-modal=true` versus actual modality — **14/14**

Broken custom portal:
- AX dialog exposes role `dialog`, name, and `modal=true`;
- DOM underlay is not inert;
- background destructive button remains exposed **and focusable** in Chromium AX tree;
- `Shift+Tab` escapes `Confirm → background destructive action → opener`;
- forward Tab leaves the dialog task;
- backdrop permits pointer hit-through;
- background destructive action activates while the dialog is semantically modal.

Revised, with the same role/name/`aria-modal` declaration:
- underlay becomes `inert`;
- background controls disappear from Chromium AX tree;
- Tab/Shift+Tab stay within the dialog;
- backdrop blocks hidden background actions;
- close restores focus to the opener.

**Rule:** `aria-modal=true` describes modality; it does not implement DOM inertness, pointer blocking, focus containment or restoration. Declared semantic modality and actual operational modality must agree.

### L006 evidence level

**PRACTICE + CRITIQUE / custom DOM + native browser + gesture transition + forced-colors + Chromium AX-tree + semantic/behavior contradiction validation.**

Not PASS: actual Windows High Contrast; NVDA/JAWS/Narrator/VoiceOver/TalkBack; Firefox/Safari; physical iOS/Android; stylus/multi-touch/OS gesture arbitration; production framework portals/native frameworks; human layer comprehension.

---

## Other established blocks

### L001 figure-ground / optical centering
- Border-ownership cue isolation: nine stimuli, pixel-identical local shared-edge crop after failure→revision; blinded Left/Right/Ambiguous human protocol ready; no human data fabricated.
- Optical centering: fixed 48×48 target, six asymmetric shapes, 16/24/32/40px at DPR1/2; no universal optical-offset token; raster mass is diagnostic, not perceived center.

### L002 density / spatial rhythm
**216-condition Chromium validation** rejected fake compactness from clipping/undersized targets. Adaptive density preserves semantic content, required targets and grouping while compressing discretionary whitespace.

### L003 Type fallback → Layout
T005-compatible Latin/Korean fallback stacks crossed different browser wrap thresholds. Semantic-lane recomposition stabilized object identity instead of font-specific breakpoints.

### L004 tabular numerals → dense Layout
`tabular-nums` equalized tested browser digit/decimal positions but widened Inter enough to break an 88px placeholder-derived track; intrinsic numeric width removed overflow.

### L005 Color → Layout
Fixed geometry separated spatial density from Color-driven feature variability and semantic collision. Color C007 independently confirms the main direction with complementary metrics.

### I001–I004
- I001 navigation/state: **14/14** controlled assertions.
- I002 async/retry/cancel: **19/19**.
- I003 forced-colors state resilience: **14/14**.
- I004 concurrent edit/conflict/merge/recovery: **17/17 controlled state-machine + 16/16 real HTTP precondition assertions**.

None is production PASS.

---

## Cross-specialist consequences

### Type — through T007
- Validate **actual delivered font build + axis value** near wrap, numeric-column, density and overlay-boundary thresholds.
- T007 strengthens the warning: a variable font can build while a glyph is frozen or an intermediate instance is malformed.

### Color — through C009
- C007 ↔ L005 = **CONFIRMATION + COMPLEMENTARY METHOD**.
- C009 reinforces that semantic Color values do not normalize Type/rendered geometry.
- L006 forced-colors = **CONFIRMATION + REALISTIC LAYER TRANSFER** of C001 channel-loss risk.
- Color cannot repair wrong interaction ownership; Layout/Type failures should not be disguised with color compensation.

### Web Design
No substantive W### yet. Web should reproduce L001–L006 and I001–I004 using production page/components, actual portals/focus scopes, delivered fonts/localization/zoom, real OS accessibility modes/AT and Firefox/Safari/mobile matrices.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | human observation; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real rendering; text-growth/cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context + human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue isolation + realistic transfer complete; blinded observers/broader platforms pending |
| Layer ownership / visual-interaction coupling | **PRACTICE / CRITIQUE** | **15 + 13 + 13 + 28 + 14** assertion layers; real OS/AT, Firefox/Safari, physical mobile, production portals/native and human evidence pending |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | stronger centroid datasets; observers/broader transfer |
| Optical centering | PRACTICE / CRITIQUE | raster proof complete; blinded humans, physical devices, icon+text/RTL/platform transfer pending |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | rendered cycle complete; human task/project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002/L003 evidence; real zoom/cross-browser/device/page transfer pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | L003/L004 + T006/T007 dependency; delivered-font/axis/cross-platform/human evidence pending |
| Dense numeric comparison geometry | PRACTICE / CRITIQUE | locale/accounting/dynamic update/human comparison pending |
| Color-driven feature density / salience | PRACTICE / CRITIQUE | L005 + C007 + C009 transfer; human/CVD/device/environment pending |
| Interaction agency / feedback / errors | CRITIQUE | real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device/human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser pending |
| Color-channel-independent state semantics | PRACTICE / CRITIQUE | real OS/other browsers/AT/production components pending |
| Concurrent edits / conflict / merge / recovery | PRACTICE / CRITIQUE | controlled 17 + real HTTP ETag/If-Match 16 assertions; production backend/DB/offline/multi-device/CRDT-OT/AT/human pending |

---

## Active next queue

1. **Human evidence when participants exist** — L001 border ownership, optical centering; L002/L005/C007 task performance/error separate from preference/workload.
2. **L006 production/platform transfer** — actual Windows High Contrast and screen readers; Firefox/Safari; physical mobile; stylus/multi-touch/OS gestures; real framework portals/focus scopes; complex nested/routing/remount restoration; native mobile overlays.
3. **I004 production transfer** — real project backend/DB transaction semantics, offline/reconnect, multi-device/tab, authorization/finalization, CRDT/OT where relevant, AT and human conflict resolution.
4. **L004 only if project-relevant** — delivered production font/exact T004, locale/accounting, dynamic update, actual zoom/DPR.
5. **I003 higher fidelity** — real OS high contrast/AT/production tokens using L006 realistic layer cases.
6. Consume future W### evidence and independently reproduce high-risk findings.
7. Open `L007` or `I005` only for a genuinely higher-value new question.

## Open research-quality gaps

- human border ownership/grouping/balance/optical-centering judgments;
- human density/clutter/search/comparison/action evidence;
- human layer-comprehension evidence;
- real screen-reader announcement/navigation behavior;
- actual Windows High Contrast rather than Chromium emulation;
- Firefox/Safari focus/AX behavior;
- physical mobile layer behavior;
- stylus/multi-touch/OS gesture arbitration;
- production framework portal/focus-scope behavior;
- complex custom nested overlay/routing/remount restoration;
- actual browser zoom;
- production delivered static/variable font regression;
- production backend/database transaction behavior, real multi-device/offline conflict/sync, CRDT/OT/list/text/order conflicts;
- real router/history/service/network evidence;
- representative interruption/resumption evidence;
- stronger Web integration.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- T006/T007 require regression of actual delivered static/variable builds and axis instances near L003/L004/L006 boundaries.
- L006 supplies overlay/localization cases where text/axis changes can move boundaries, hit regions and restoration targets.
- Scope limit: Layout/Interaction does not define font/glyph production decisions.

### Color
- C007 ↔ L005 remains confirmation + complementary method.
- L006 forced-colors confirms C001 in realistic layering: shadow-only elevation can disappear while behavior stays foreground-owned.
- `forced-color-adjust:none` worked only as a diagnostic control and is not a generic repair.
- Scope limit: no human salience/Color threshold claim.

### Layout / Interaction reusable rules
- compactness may not sacrifice meaning or required target geometry;
- density modes are relational policies, not immutable tokens;
- separate spatial density, feature variability, emphasis distribution and semantic collision;
- border ownership is contextual; control the local edge while diagnosing remote cues;
- visual, hit, active-gesture, focus, semantic/AT, data, stack and restoration ownership are separate;
- screenshot QA cannot validate overlay interaction ownership;
- forced-colors can remove authored elevation while interaction ownership remains intact;
- use structurally robust/system-color-compatible boundary channels when overrides can remove shadow/fill cues;
- `aria-modal=true` describes but does not implement modality;
- semantic declaration and operational behavior must agree;
- active pointer capture can survive modal entry; define finish/cancel/release policy;
- modal QA must include Shift+Tab, active gesture transition, AX exposure, topmost-first dismissal and lost-invoker restoration;
- AX-tree membership is evidence, not screen-reader PASS;
- nested overlays require stack reasoning;
- dimming does not create inertness;
- timeout, failure and outcome-unknown are distinct; retry is not conflict resolution;
- 412 Precondition Failed is conflict detection, not a generic Save failure; resolve/rebase against the newest validator before another write;
- `If-Match` prevents stale mutation but does not decide same-field semantic winners; `If-None-Match:*` can protect create-new-identity recovery;
- auto-merge only semantically independent changes; preserve local drafts across conflict;
- critical state meaning must survive authored color-channel loss.

### Web Design transfer matrices
- L001 border cue isolation + human protocol;
- L001 optical raster matrix;
- L002 **216-condition** density matrix;
- L003 mixed-script wrap transfer;
- L004 numeric alignment/intrinsic-width transfer;
- L005 + C007 fixed-geometry Color validation;
- L006 **15** custom ownership assertions;
- L006 **13** native popover/dialog assertions;
- L006 **13** gesture/restoration assertions;
- L006 **28** forced-colors/implicit-capture/AX assertions;
- L006 **14** custom ARIA-modal vs actual-modality assertions;
- I001 14; I002 19; I003 14; I004 **17 controlled + 16 real HTTP precondition** assertions.

---

## Latest checkpoint

- `L001` → PRACTICE / CRITIQUE; observer judgments OPEN.
- `L002` → PRACTICE / CRITIQUE.
- `L003` → PRACTICE / CRITIQUE.
- `L004` → PRACTICE / CRITIQUE.
- `L005` → PRACTICE / CRITIQUE; independently confirmed/complemented by C007.
- `L006` → **PRACTICE / CRITIQUE**, now spanning **15 + 13 + 13 + 28 + 14** controlled assertions across visual/pointer/focus/gesture/forced-color/AX/semantic-modal mismatches.
- `I001` → CRITIQUE.
- `I002` / `I003` → PRACTICE / CRITIQUE.
- `I004` → **PRACTICE / CRITIQUE**, with **17/17 controlled state-machine + 16/16 real HTTP ETag/If-Match** evidence; production/offline/multi-device/human gates remain.
- Next IDs remain Layout `L007`; Interaction `I005`.
- No PASS promotion. Highest-value next evidence is real OS/AT/cross-browser/production-framework/human transfer, not more isolated Chromium volume.
