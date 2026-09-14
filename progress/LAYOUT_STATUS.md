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

Human-observer/user-task validation is **DEFERRED TO APP-DEVELOPMENT VALIDATION**. It is not treated as completed or simulated.

## Four-specialist sync

- **Type:** through **T014**. Exact delivered font/package plus normalization/fallback state are prerequisites for stable Korean Layout regression.
- **Color:** through **C012**. C011 adds forced-colors/SVG transfer and C012 strengthens provenance discipline; appearance, semantic state and operational ownership remain separate validation layers.
- **Web:** no substantive `W###` yet; `W001` remains next. Do not invent Web production evidence.

---

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
- `I004-http-precondition-etag-transfer.md` + **16 real HTTP precondition assertions**
- `I004-offline-outbox-reconnect-transfer.md` + **18 durable offline/restart/reconnect assertions**
- `I004-ambiguous-outcome-idempotency-transfer.md` + **15 real HTTP ambiguous-result/idempotency assertions**

Shared accessibility baseline: `research/004-accessibility-reflow-targets-focus.md`.

---

# L006 — layer ownership

Ownership vector:

`visual owner / pointer hit owner / active gesture-capture owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position / restoration target`

Consistency check:

`declared semantic modality ↔ actual operational modality`

Evidence layers:

1. **Custom visual/interaction ownership — 15/15**: screenshot appearance cannot prove hit/focus ownership.
2. **Native HTML popover/dialog — 13/13**: bounded top-layer/inertness/nested-overlay/restoration behavior; strict APG-style focus loop remains a separate browser/AT gate.
3. **Pointer capture/dismissal/lost invoker — 13/13**: pre-existing capture can survive modal entry; nested dismissal is topmost-first; lost invoker needs logical fallback.
4. **Forced-colors/touch implicit capture/Chromium AX tree — 28/28**: shadow-only layer cues can disappear while operational ownership remains; touch implicit capture can survive modal entry; AX tree is evidence, not screen-reader PASS.
5. **Custom `aria-modal=true` versus actual modality — 14/14**: ARIA declaration does not implement inertness, pointer blocking, focus containment or restoration.

Evidence level: **PRACTICE + CRITIQUE**.

Remaining: real Windows High Contrast/AT; Firefox/Safari; physical iOS/Android; stylus/multi-touch/OS gestures; production portal/focus-scope/native frameworks; human layer comprehension.

---

# I004 / I002 — concurrency, offline sync, and ambiguous outcomes

I004 now has four evidence layers.

## 1. Conflict state machine — **17/17**

Established naive lost update, semantically safe disjoint merge, same-field preservation, delete-vs-edit identity semantics and resolution recovery.

## 2. Real HTTP ETag / If-Match — **16/16**

Established real stale-write prevention, 412 classification, current-validator rebase, same-field no-auto-winner and `If-None-Match:*` create-new-identity recovery.

## 3. Durable offline outbox / restart / reconnect — **18/18**

Real HTTP/1.1 server + two durable SQLite client stores used as a lab persistence substrate.

Established:
- network-unavailable queue retention;
- draft/outbox survival across client restart;
- historical base ETag preservation;
- stale detection before merge;
- current-state fetch + semantic rebase;
- same-field durable conflict hold;
- delete-vs-edit without resurrection;
- keep-as-new recovery;
- queue clearing only after authoritative success.

Critical rule:

> `base state` is a historical fact attached to the queued intent. Reconnect produces `current state`; it must not rewrite the remembered base.

The intended Chromium+localhost+IndexedDB integration was blocked by environment policy `ERR_BLOCKED_BY_ADMINISTRATOR`; no browser conclusion is inferred. Exact IndexedDB/service-worker transfer remains Web/live-project work.

## 4. Applied-but-response-lost / idempotency — **15/15**

Real HTTP server deliberately applied state changes then closed the connection before sending a response.

Established:
- transport correctly becomes **outcome unknown**, not known failure;
- a successful conditional PUT whose response was lost can later return 412 against its own changed validator;
- therefore 412 after outcome-unknown does not prove another actor caused a conflict;
- if server/domain can establish requested PUT state is already current, retry can confirm `already-applied` without a second effect;
- blind retry of non-idempotent POST duplicated a side effect (`1 → 2`);
- application-specific semantic operation identity replayed the original result without duplication (`1 → 1`);
- reusing the same operation identity with a different payload was rejected.

The lab `X-Operation-Id` is an application contract, **not claimed as a standardized HTTP field**. Current HTTPAPI Idempotency-Key draft material is not treated as a standard.

Updated result-state model:

`not sent / sending / known rejected / outcome unknown / confirmed applied / confirmed already-applied-replayed / actual external conflict / operation-identity mismatch`.

### I004/I002 reusable rules

- Local persistence success is not remote commit success.
- Retry is not conflict resolution.
- Outcome unknown is not failure.
- A 412 after outcome-unknown needs own-success detection before conflict escalation.
- `If-Match` prevents stale mutation but does not choose semantic winners.
- Base/current/local are separate state dimensions.
- A durable outbox is a preserved-intention store, not merely a retry list.
- Do not replace queued base validator with the latest fetched ETag.
- Queue clearing follows authoritative confirmation.
- Auto-merge only semantically independent changes.
- Preserve local drafts across conflicts/restarts.
- Delete-vs-edit may require new identity rather than resurrection.
- Do not blindly retry non-idempotent side effects after an ambiguous response.
- If retry safety depends on semantic operation identity, persist the **same identity** across retries and bind it to the exact intent/payload.

Evidence level: **PRACTICE + CRITIQUE / state-machine + real HTTP + durable offline/restart + applied-response-lost/idempotency transfer**.

Remaining I004/I002 gates:
- production DB transaction/isolation and dedupe-ledger atomicity;
- browser/mobile local database and background sync;
- physical multi-device races;
- multiple queued operation ordering/compaction/dependencies;
- crashes between external side effect and dedupe-record commit;
- authorization/account change/finalization while offline;
- CRDT/OT for text/list/order domains;
- reverse proxies/API gateways/retry middleware;
- external payment/booking/message APIs;
- AT and human comprehension.

---

## Other established blocks

- **L001**: local-edge-controlled border-ownership stimuli; optical raster proof. Human observation deferred.
- **L002**: 216-condition density/reflow proof; fake compactness rejected.
- **L003**: Korean/Latin fallback wrap thresholds; T013/T014 now add normalization prerequisite.
- **L004**: tabular-number alignment plus intrinsic-width consequence.
- **L005**: fixed-geometry Color density/salience; independent C007 confirmation.
- **I001** navigation/state: 14/14.
- **I002** async/retry/cancel: 19/19 plus ambiguous-outcome transfer above.
- **I003** forced-colors semantic resilience: 14/14.

None is production PASS.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | human deferred; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real rendering/text-growth transfer |
| Perceptual grouping | CRITIQUE | broader context; human deferred |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue isolation + realistic transfer; human/platform pending |
| Layer ownership | PRACTICE / CRITIQUE | **15+13+13+28+14**; real OS/AT/cross-browser/mobile/production/human pending |
| Visual mass / optical centering | PRACTICE / CRITIQUE | raster evidence; human/physical-device/RTL/context transfer pending |
| Whitespace / density / responsive | PRACTICE / CRITIQUE | human/project + real zoom/cross-browser/device pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | exact delivered font/package/axis/normalization/cross-platform pending |
| Dense numeric comparison | PRACTICE / CRITIQUE | locale/accounting/dynamic/human pending |
| Color-driven density/salience | PRACTICE / CRITIQUE | device/environment/human pending |
| Interaction agency/state/navigation | CRITIQUE | broader real platform/AT/human pending |
| Async/retry/cancel | PRACTICE / CRITIQUE | production API/proxy/background-sync/AT pending |
| Color-channel-independent semantics | PRACTICE / CRITIQUE | real OS/AT/production pending |
| Concurrent edits/offline conflict | PRACTICE / CRITIQUE | **17 state + 16 HTTP + 18 offline + 15 ambiguous/idempotency**; production DB/storage/multi-device/queue-ordering/CRDT-OT/AT/human pending |

---

## Active next queue

Human work is deferred to app-development validation and does not block non-human research.

1. **I004 queue semantics** — multiple queued operations, ordering, compaction/squashing, dependencies and conflict propagation.
2. **I004 authorization/finalization while offline** — permission change, locked/finalized records and compensating actions.
3. **I002/I004 production retry boundaries** — backoff/retry middleware/proxy behavior and dedupe-ledger atomicity when suitable infrastructure exists.
4. **L006 production/platform transfer** when real OS/AT/cross-browser/mobile/framework environments become available.
5. **L004 only if project-relevant** — delivered font, locale/accounting, dynamic update, actual zoom/DPR.
6. Consume future W### evidence and independently reproduce high-risk findings.
7. Open `L007` or `I005` only for a genuinely higher-value new question.

## APP-DEVELOPMENT VALIDATION queue

Execute only with live app/prototype and suitable participants:
- L001 border ownership and optical-centering judgments;
- L002/L005/C007 task performance/error vs preference/workload;
- L006 layer comprehension/dismissal expectations;
- I004 conflict-resolution comprehension/error;
- real accessibility-user validation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type
- T013/T014 normalization representation is a prerequisite for stable Korean Layout and exact conflict/diff text identity.

### Color
- Sync states `queued`, `network pending`, `outcome unknown`, `conflict`, `deleted`, `confirmed`, `already applied` are semantically distinct; Color must not collapse them or become sole channel.

### Web Design
Highest-value transfer contracts now include:
- L006 five overlay/modality assertion layers;
- I001 14, I002 19, I003 14;
- I004 **17 state + 16 HTTP + 18 durable offline + 15 ambiguous/idempotency assertions**.

Web should reproduce I004 using actual IndexedDB/service worker/background sync or chosen framework, including reload/crash persistence, concurrent tabs, ETag handling, operation identity persistence, applied-but-response-lost cases, automatic retry middleware, queue ordering and UI/AT status behavior.

---

## Latest checkpoint

- `L001`–`L006`: studied spatial modules remain PRACTICE / CRITIQUE where applicable.
- `I001`: CRITIQUE.
- `I002` / `I003` / `I004`: PRACTICE / CRITIQUE.
- `I004` now spans **17/17 + 16/16 + 18/18 + 15/15** controlled evidence layers.
- Next IDs remain Layout `L007`; Interaction `I005`.
- Human validation explicitly deferred to app-development stage.
- No PASS promotion claimed.
