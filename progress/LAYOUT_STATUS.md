# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L007`; Interaction `I006`

This file is maintained by the Layout, Spatial & Interaction Specialist. It does not update global `progress/STATUS.md` during ordinary research.

## Mission / stage

Research exists to improve real app, web and product decisions. Research volume is not the objective.

Current stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules  
Foundation: **NOT PASSED**

Human-observer/user-task validation is **DEFERRED TO APP-DEVELOPMENT VALIDATION**. It is not treated as completed or simulated.

## Four-specialist sync

- **Type:** through **T015**; next T016. Bounded Chromium Hangul canonical-equivalent rendering evidence now exists, but Firefox/Safari/native platform/production Korean shaping remain open.
- **Color:** **Stage 1 PASS** after C014/C015 closure; next C016 / Stage 2 entry audit. This does not imply production/device/human Color completion.
- **Web:** **W001 completed**; next W002. Web now has a Stage 1 PRACTICE/CRITIQUE baseline, but no production integration PASS.
- **Layout/Interaction:** L001–L006 plus I001–I005; Stage 1 remains NOT PASSED.

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
- `I005-ambiguous-outcome-idempotency.md` + **18 independent HTTP replication/extension assertions**

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
Established network-unavailable queue retention; restart persistence; historical base ETag preservation; stale detection before merge; current-state fetch + semantic rebase; same-field durable conflict hold; delete-vs-edit without resurrection; keep-as-new recovery; queue clearing only after authoritative success.

Critical rule:

> `base state` is a historical fact attached to the queued intent. Reconnect produces `current state`; it must not rewrite the remembered base.

## 4. Applied-but-response-lost / application operation identity — **15/15**
Established outcome-unknown after response loss; own-success 412 ambiguity; desired-state already-applied confirmation; blind non-idempotent POST duplicate; application-specific operation identity dedupe; payload mismatch rejection.

The lab `X-Operation-Id` is an application contract, not a standardized HTTP field.

Evidence level: **PRACTICE + CRITIQUE**.

---

# I005 — stable intent identity and concurrent duplicate recovery

I005 deliberately **replicates and extends** I004's ambiguous-outcome result rather than pretending the topic was new.

Authoritative basis:
- RFC 9110 idempotent-method semantics;
- HTTPAPI `draft-ietf-httpapi-idempotency-key-header-07`, explicitly treated as an **expired Internet-Draft / work in progress**, not an RFC.

Fresh real HTTP/1.1 harness: **18/18 assertions PASS**.

Confirmed independently:
- server can commit a side effect while the client receives only a transport error;
- naive POST retry can create a second side effect;
- same stable intent key + same payload can replay the original result without duplication;
- generating a fresh key for the retry defeats the protection;
- same key + different payload is rejected in the bounded draft-pattern harness.

New evidence beyond I004:
- when a duplicate with the same key arrives **while the first request is still processing**, the harness rejects concurrent execution with 409;
- after the first completes, the same-key retry returns the original result and side-effect count remains one.

Core model:

`one user intent id → one payload/fingerprint contract → potentially many transport attempts → at most one duplicate-sensitive side effect`

and separately:

`client knowledge = queued / in flight / outcome unknown / confirmed / replay-confirmed / concurrent duplicate / identity mismatch / rejected`.

Reusable rule:

> Retry attempts may multiply; user intent identity must not.

For duplicate-sensitive actions, stable operation identity belongs to the durable interaction/data lifecycle, not merely to a transient HTTP request function.

Evidence level: **PRACTICE + CRITIQUE / deliberate replication + concurrent-duplicate extension**.

Not PASS: production business-effect/dedupe-ledger atomicity, gateway/proxy retries, distributed systems, key expiry/security, real browser/mobile stack, AT and app-stage human validation remain open.

---

## Other established blocks

- **L001**: local-edge-controlled border-ownership stimuli; optical raster proof. Human observation deferred.
- **L002**: 216-condition density/reflow proof; fake compactness rejected.
- **L003**: Korean/Latin fallback wrap thresholds; normalization/runtime font state remain prerequisites.
- **L004**: tabular-number alignment plus intrinsic-width consequence.
- **L005**: fixed-geometry Color density/salience; independent C007 confirmation.
- **I001** navigation/state: 14/14.
- **I002** async/retry/cancel: 19/19 plus ambiguous-outcome transfer.
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
| Concurrent edits/offline conflict | PRACTICE / CRITIQUE | **17 state + 16 HTTP + 18 offline + 15 ambiguous**; production DB/storage/multi-device/queue-ordering/CRDT-OT pending |
| Ambiguous outcome / duplicate-sensitive intent | PRACTICE / CRITIQUE | **I004 15 + I005 18 replication/extension**; atomicity/distributed/gateway/browser/mobile pending |

---

## Active next queue

Human work is deferred to app-development validation and does not block non-human research.

1. **Multiple queued operation semantics** — ordering, dependencies, compaction/squashing, partial failure and conflict propagation.
2. **Authorization/finalization while offline** — permission change, locked/finalized records and compensating actions.
3. **Production retry boundaries** — proxy/middleware behavior and business-effect/dedupe-ledger atomicity when suitable infrastructure exists.
4. **L006 production/platform transfer** when real OS/AT/cross-browser/mobile/framework environments become available.
5. **Web W001 transfer consumption** — inspect/reproduce high-risk Web findings as W-series grows.
6. **L004 only if project-relevant** — delivered font, locale/accounting, dynamic update, actual zoom/DPR.
7. Open `L007` or `I006` only for a genuinely higher-value new question.

## APP-DEVELOPMENT VALIDATION queue

Execute only with live app/prototype and suitable participants:
- L001 border ownership and optical-centering judgments;
- L002/L005/C007 task performance/error vs preference/workload;
- L006 layer comprehension/dismissal expectations;
- I004/I005 conflict/retry-state comprehension/error;
- real accessibility-user validation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type
- T015 strengthens the need to test exact delivered/runtime Korean text state before treating Layout geometry as stable.
- Recovery/conflict surfaces need exact long/localized strings without destroying semantic distinctions.

### Color
- Color Stage 1 PASS is acknowledged; Layout/Interaction does not infer production/device/human Color PASS.
- Sync/retry states `queued`, `outcome unknown`, `processing duplicate`, `conflict`, `deleted`, `confirmed`, `replay-confirmed`, `identity mismatch` remain distinct semantics; Color must not collapse them or become sole channel.

### Web Design
- W001 is now available as the first Web baseline.
- Highest-value future transfer includes L006 overlay matrices and I004/I005 network/offline contracts using actual browser/framework/page behavior.
- Web should verify stable operation identity across `fetch` retries/reload/offline, page-level outcome-unknown messaging, concurrent activation, and framework retry middleware.

---

## Latest checkpoint

- `L001`–`L006`: studied spatial modules remain PRACTICE / CRITIQUE where applicable.
- `I001`: CRITIQUE.
- `I002` / `I003` / `I004` / `I005`: PRACTICE / CRITIQUE.
- I004 evidence: **17/17 + 16/16 + 18/18 + 15/15**.
- I005 independent replication/extension: **18/18**.
- Next IDs: Layout `L007`; Interaction `I006`.
- Human validation remains explicitly deferred to app-development stage.
- No Layout/Interaction Foundation PASS promotion claimed.
