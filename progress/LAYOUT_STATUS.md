# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L007`; Interaction `I005`

This file is maintained by the Layout, Spatial & Interaction Specialist. It does not update global `progress/STATUS.md` during ordinary research.

## Mission / stage

Research exists to improve real app, web and product decisions. Research volume is not the objective.

Current stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules  
Foundation: **NOT PASSED**

Human-observer/user-task validation is currently **DEFERRED TO APP-DEVELOPMENT VALIDATION**, not treated as completed or fabricated.

## Four-specialist sync

- **Type:** through **T014**. Type now covers source/build/package/normalization contracts through Hangul NFC↔NFD subset closure. Layout consequence: exact delivered font/package plus actual normalization/fallback state are spatial inputs before Korean wrap/density regression is considered stable.
- **Color:** through **C012**. Color now adds C010 production color-management, C011 forced-colors/SVG semantic transfer, and C012 spectral provenance/sampling evidence. Layout consequence: appearance, semantic state and operational ownership remain separate validation layers.
- **Web:** no substantive `W###` yet; `W001` remains next. Do not invent Web production evidence.

---

## Canonical evidence

### Layout / spatial
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
- `I004-http-precondition-etag-transfer.md` + **16 real HTTP precondition assertions**
- `I004-offline-outbox-reconnect-transfer.md` + **18 durable offline/restart/reconnect assertions**

Shared accessibility baseline: `research/004-accessibility-reflow-targets-focus.md`.

---

# L006 — layer ownership evidence

L006 treats layered UI as a cross-contract rather than a z-index/elevation problem.

Ownership vector:

`visual owner / pointer hit owner / active gesture-capture owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position / restoration target`

Consistency check:

`declared semantic modality ↔ actual operational modality`

Evidence layers:

1. **Custom visual/interaction ownership — 15/15**  
   Pixel-identical broken/revised popover, sticky and modal-sheet pairs proved screenshot appearance cannot validate pointer/focus ownership.

2. **Native HTML popover/dialog — 13/13 bounded assertions**  
   Native popover overlap, `showModal()` underlay blocking, nested top-layer behavior and bounded invoker restoration established. Strict APG-style focus-loop behavior remains a separate target-browser gate.

3. **Pointer capture / dismissal / lost invoker — 13/13**  
   A pre-existing captured background drag survived modal entry until explicitly released. Nested dismissal is topmost-first. Missing invoker requires a logical restoration fallback.

4. **Forced-colors / touch implicit capture / Chromium AX tree — 28/28**  
   Shadow-only layer cues can disappear while operational ownership remains foreground. System-color structural outlines survive the controlled forced-colors condition. Touch implicit capture can survive modal entry. Chromium AX-tree modality was validated but is not screen-reader PASS.

5. **Custom `aria-modal=true` versus actual modality — 14/14**  
   `aria-modal=true` can declare modal semantics while pointer/focus/background behavior remains non-modal. Revised version required real inertness, pointer blocking, focus containment and restoration.

Evidence level: **PRACTICE + CRITIQUE**.

Remaining L006 gates: real Windows High Contrast; NVDA/JAWS/Narrator/VoiceOver/TalkBack; Firefox/Safari; physical iOS/Android; stylus/multi-touch/OS gesture arbitration; production portal/focus-scope/native-framework behavior; human layer comprehension.

---

# I004 — concurrent edits / conflict / offline sync

I004 now has three evidence layers.

## 1. Controlled conflict state machine — **17/17**

Established:
- naive lost update;
- disjoint safe merge when semantic independence is known;
- same-field conflict with local draft preservation;
- delete-vs-edit as a distinct identity conflict;
- focus/recovery behavior after resolution.

## 2. Real HTTP `ETag` / `If-Match` — **16/16**

Established over an actual HTTP origin-server exchange:
- stale whole-record mutation can lose parallel work when unprotected;
- strong ETag + `If-Match` blocks stale mutation with 412;
- disjoint merge must rebase against the newest validator;
- same-field winner is not decided by HTTP preconditions;
- delete-vs-edit can preserve work as a new identity with `If-None-Match:*`.

## 3. Durable offline outbox / restart / reconnect — **18/18**

Test substrate: real HTTP/1.1 server + two independent durable SQLite client stores. SQLite is a lab persistence substrate, not a Web/mobile storage recommendation.

Established:
- unavailable network leaves queued operation and draft durable;
- queued intent survives client/process restart;
- original base ETag remains attached to the queued intent;
- reconnect first retries against that historical base and receives stale detection;
- safe disjoint rebase occurs only after fetching current state and establishing semantic independence;
- same-field conflict remains durable and does not auto-write;
- delete-vs-edit remains pending without resurrection;
- explicit keep-as-new creates a separate identity;
- queue/draft clear only after authoritative success.

Critical rule:

> `base state` is a historical fact attached to the queued user intent. A reconnect fetch creates `current state`; it must not silently rewrite the operation's remembered base.

Offline sync state model now distinguishes:

`local draft / queued-saved-locally / syncing / remote confirmed / network pending / mergeable stale base / conflict requiring resolution / remote deleted-finalized / recovered as new or compensating action`.

Do not collapse this to `synced / error`.

### Infrastructure limitation recorded

The intended Chromium + localhost HTTP + IndexedDB harness could not run because the installed Chromium policy returned `ERR_BLOCKED_BY_ADMINISTRATOR` for localhost navigation, including after launch-flag checks. No browser product conclusion is inferred.

Browser IndexedDB/service-worker/background-sync transfer remains a future Web/live-project gate.

Evidence level: **PRACTICE + CRITIQUE / state-machine + real HTTP + durable offline/reconnect transfer**.

Remaining I004 gates:
- actual production DB/transaction/isolation behavior;
- IndexedDB/service worker or real mobile local database transfer;
- physical multi-device races;
- ambiguous-result duplicate delivery/idempotency;
- multiple queued operation ordering/compaction;
- authorization/account change/finalization while offline;
- CRDT/OT for text/list/order domains;
- AT and human conflict comprehension.

---

## Other established blocks

### L001 figure-ground / optical centering
- Border ownership: nine local-edge-controlled stimuli + blinded observer protocol. Human data deferred to app-development validation.
- Optical centering: fixed 48×48 target, six asymmetric shapes, 16/24/32/40px at DPR1/2; no universal offset token; raster mass is diagnostic rather than perceived center.

### L002 density / spatial rhythm
**216-condition Chromium validation** rejected fake compactness from clipping/undersized targets. Adaptive density preserves content, required targets and grouping while compressing discretionary whitespace.

### L003 Type fallback → Layout
Mixed Latin/Korean fallback stacks crossed different browser wrap thresholds. Semantic-lane recomposition stabilized object identity instead of font-specific breakpoints. T013/T014 now add normalization state as another prerequisite for stable Korean transfer.

### L004 tabular numerals → dense Layout
`tabular-nums` equalized tested browser digit/decimal positions but widened Inter enough to break a fixed track; intrinsic numeric width removed overflow.

### L005 Color → Layout
Fixed geometry separated spatial density from Color-driven feature variability and semantic collision. Color C007 independently confirmed the main direction. C011/L006 strengthen channel-loss/override transfer.

### I001–I003
- I001 navigation/state: **14/14**.
- I002 async/retry/cancel: **19/19**.
- I003 forced-colors state resilience: **14/14**.

None is production PASS.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | human observation deferred; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real rendering; text-growth/cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context; human observation deferred |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue isolation + realistic transfer complete; human/platform transfer pending |
| Layer ownership / visual-interaction coupling | PRACTICE / CRITIQUE | **15 + 13 + 13 + 28 + 14** assertion layers; real OS/AT/cross-browser/mobile/production/human pending |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | broader centroid/context; observers deferred |
| Optical centering | PRACTICE / CRITIQUE | raster proof complete; human/physical-device/icon+text/RTL transfer pending |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | rendered cycle complete; human task/project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | real zoom/cross-browser/device/page transfer pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | exact delivered font/package/axis/normalization state and cross-platform transfer pending |
| Dense numeric comparison geometry | PRACTICE / CRITIQUE | locale/accounting/dynamic update/human comparison pending |
| Color-driven feature density / salience | PRACTICE / CRITIQUE | L005+C007/C009/C011 context; human/device/environment pending |
| Interaction agency / feedback / errors | CRITIQUE | real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device/human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | production API/idempotency/abort/offline/AT/cross-browser pending |
| Color-channel-independent state semantics | PRACTICE / CRITIQUE | real OS/AT/production components pending |
| Concurrent edits / conflict / merge / recovery | PRACTICE / CRITIQUE | **17 state + 16 HTTP + 18 offline/restart/reconnect assertions**; production DB/storage/multi-device/idempotency/queue ordering/CRDT-OT/AT/human pending |

---

## Current reusable rules

- Compactness may not sacrifice meaning or required target geometry.
- Density modes are relational policies, not immutable spacing tokens.
- Separate spatial density, feature variability, emphasis distribution and semantic collision.
- Border ownership is contextual; control the local edge while diagnosing remote cues.
- Visual, hit, active-gesture, focus, semantic/AT, data, stack and restoration ownership are separate.
- Screenshot QA cannot validate overlay interaction ownership.
- Forced-colors can remove authored elevation while operational ownership remains intact.
- `aria-modal=true` describes but does not implement modality.
- Active pointer capture can survive modal entry; define explicit finish/cancel/release policy.
- AX-tree membership is evidence, not screen-reader PASS.
- Timeout, failure and outcome-unknown are distinct.
- Retry is not conflict resolution.
- `If-Match` prevents stale mutation but does not choose semantic winners.
- Base/current/local are separate state dimensions.
- A durable outbox is a preserved-intention store, not merely a retry list.
- Do not replace a queued operation's base validator with the latest fetched ETag.
- Queue clearing follows authoritative confirmation, not local persistence.
- Auto-merge only semantically independent changes.
- Preserve local drafts across conflicts and restarts.
- Delete-vs-edit may require a new identity rather than resurrection.
- Critical state meaning must survive authored color-channel loss.

---

## Active next queue

Human work is deferred until app-development validation and does not block non-human research.

1. **I004 next executable gap — ambiguous-result idempotency + duplicate delivery**: request applied but response lost; durable outbox retry must not duplicate side effects or misclassify own successful write as an external conflict.
2. **I004 queue semantics** — multiple queued operations, ordering, compaction/squashing, dependency between operations and conflict propagation.
3. **I004 authorization/finalization while offline** — queued mutation meets changed permission, finalized/locked record, or side-effect boundary.
4. **L006 production/platform transfer** when actual OS/AT/cross-browser/mobile/framework environments become available.
5. **I002 production async transfer** — idempotency/abort/outcome-unknown integrated with the I004 outbox model.
6. **L004 extension only if project-relevant** — real delivered font, locale/accounting formats, dynamic updates, actual zoom/DPR.
7. Consume future W### evidence and independently reproduce high-risk findings.
8. Open `L007` or `I005` only for a genuinely higher-value new question than these existing validation gaps.

## APP-DEVELOPMENT VALIDATION queue

Do not fabricate or simulate human evidence. Execute when a live app/prototype and suitable participants exist:

- L001 border ownership Left/Right/Ambiguous judgments;
- L001 optical-centering blinded comparisons;
- L002/L005/C007 task performance/error separate from preference/workload;
- L006 layer comprehension/dismissal expectations;
- I004 conflict-resolution comprehension/error;
- real accessibility-user validation where applicable.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- T013/T014 make normalization representation a prerequisite for stable Korean Layout regression.
- Offline conflict/diff surfaces may need exact text preservation; do not normalize away semantically relevant local/remote content without a product contract.
- Scope limit: Interaction does not define normalization/shaping policy.

### Color
- Offline sync now has distinct `queued`, `network pending`, `mergeable stale`, `same-field conflict`, `remote deleted`, `confirmed` semantics. Color may encode them but must not collapse them or become the sole channel.
- L006 forced-colors remains realistic confirmation of channel-loss risk.

### Web Design
Reusable transfer contracts now include:
- L001 cue isolation/optical raster;
- L002 216-condition density;
- L003 mixed-script wrap + Type normalization prerequisite;
- L004 numeric alignment/intrinsic width;
- L005/C007 fixed-geometry Color density;
- L006 five assertion layers for overlays/modality;
- I001 14, I002 19, I003 14;
- I004 **17 state + 16 HTTP + 18 durable offline/reconnect assertions**.

Highest-value Web transfer: reproduce I004 with actual IndexedDB/service worker/background sync or chosen framework, including reload/crash persistence, storage eviction policy, concurrent tabs, exact ETag handling, queue ordering/idempotency and UI/AT status behavior.

---

## Latest checkpoint

- `L001`–`L006`: all studied modules remain **PRACTICE / CRITIQUE** where applicable; no human/platform PASS inferred.
- `I001`: navigation/state → CRITIQUE.
- `I002`: async/retry/cancel → PRACTICE / CRITIQUE.
- `I003`: forced-colors resilience → PRACTICE / CRITIQUE.
- `I004`: now spans **17/17 controlled state + 16/16 real HTTP + 18/18 durable offline/restart/reconnect** assertions → PRACTICE / CRITIQUE.
- Next IDs remain Layout `L007`; Interaction `I005`.
- Human validation explicitly deferred to app-development stage.
- No PASS promotion claimed.
