# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L007`; Interaction `I007`

This file is maintained by the Layout, Spatial & Interaction Specialist. It does not update global `progress/STATUS.md` during ordinary research.

## Mission / stage

Research exists to improve real app, web and product decisions. Research volume is not the objective.

Current stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules  
Foundation: **NOT PASSED**

Human-observer/user-task validation is **DEFERRED TO APP-DEVELOPMENT VALIDATION**. It is not treated as completed or simulated. Non-human research continues.

## Four-specialist sync

- **Type:** through **T015**; next T016. Bounded Chromium Hangul canonical-equivalent rendering evidence exists; cross-browser/native/production Korean shaping remains open.
- **Color:** **Stage 1 PASS** after C014/C015 closure; next C016 / Stage 2 entry audit. This does not imply production/device/human Color completion.
- **Web:** **W001 completed**; next W002. Web has a Stage 1 PRACTICE/CRITIQUE baseline, not production integration PASS.
- **Layout/Interaction:** L001–L006 plus I001–I006; Stage 1 remains NOT PASSED.

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
- `I004-multi-operation-queue-semantics.md` + **20 ordering/compaction/dependency assertions**
- `I004-offline-authorization-finalization-transfer.md` + **18 authorization/finalization/account assertions**
- `I005-ambiguous-outcome-idempotency.md` + **18 independent HTTP replication/extension assertions**
- `I005-business-effect-dedupe-atomicity-transfer.md` + **26 effect/dedupe/outbox/inbox assertions**
- `I006-sequence-collaboration-ot-crdt-boundary.md` + **18 sequence-concurrency boundary assertions**

Shared accessibility baseline: `research/004-accessibility-reflow-targets-focus.md`.

---

# L006 — layer ownership checkpoint

Ownership vector:

`visual owner / pointer hit owner / active gesture-capture owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position / restoration target`

Consistency check:

`declared semantic modality ↔ actual operational modality`

Evidence layers:
1. **Custom visual/interaction ownership — 15/15**.
2. **Native HTML popover/dialog — 13/13**.
3. **Pointer capture/dismissal/lost invoker — 13/13**.
4. **Forced-colors/touch implicit capture/Chromium AX tree — 28/28**.
5. **Custom `aria-modal=true` versus actual modality — 14/14**.

Key rules:
- screenshot appearance cannot prove hit/focus/data ownership;
- pre-existing pointer capture can survive modal entry;
- forced-colors can remove authored elevation while interaction ownership remains;
- AX-tree evidence is not screen-reader PASS;
- `aria-modal=true` describes modality but does not implement inertness, pointer blocking, focus containment or restoration.

Evidence level: **PRACTICE + CRITIQUE**.

Remaining: real Windows High Contrast/AT; Firefox/Safari; physical iOS/Android; stylus/multi-touch/OS gestures; production portals/focus scopes/native frameworks; human layer comprehension.

---

# I004 — concurrency, offline sync, queue and policy-state

I004 spans **six controlled evidence layers**:

1. **Conflict state machine — 17/17**: lost update, safe disjoint merge, same-field preservation, delete-vs-edit identity and recovery.
2. **Real HTTP ETag / If-Match — 16/16**: stale-write prevention, 412 classification, current-validator rebase and create-new-identity recovery.
3. **Durable offline outbox / restart / reconnect — 18/18**: network-pending persistence, historical-base preservation, durable unresolved conflict and delete-vs-edit recovery.
4. **Applied-but-response-lost / operation identity — 15/15**: outcome unknown, own-success 412 ambiguity, duplicate POST and stable operation-ID replay.
5. **Multiple queued operations — 20/20**: order semantics, safe/unsafe compaction, dependency-aware conflict propagation and temp→server identity mapping.
6. **Offline authorization / finalization / account switch — 18/18**: permission block, finalized-record amendment recovery, stale revalidation after permission restoration, actor-bound queue safety.

Critical rules:
- `base state` is historical fact; reconnect `current state` must not rewrite it.
- compaction safety is defined by operation algebra/dependencies, not JSON path equality.
- an outbox is a dependency-aware preserved-intention structure, not merely FIFO retries.
- authorization, version validity, actor ownership and workflow mutability are distinct gates.
- a valid historical edit can become an invalid future mutation without becoming meaningless work.

Queued-operation validity can depend on:

`intent / local-server identity / historical base / current state / operation identity / actor-account / authorization / workflow mutability / sequence / dependencies / external side-effect state`

Evidence level: **PRACTICE + CRITIQUE**.

---

# I005 — duplicate-sensitive intent and atomicity boundary

## Stable intent identity / concurrent duplicate — **18/18**

I005 independently replicated I004's ambiguous-outcome finding and extended it with concurrent same-key processing.

Core model:

`one user intent id → one payload/fingerprint contract → many transport attempts → at most one duplicate-sensitive side effect`

Key rule:

> Retry attempts may multiply; user intent identity must not.

## Business effect ↔ dedupe atomicity — **26/26**

New extension separates the commit boundaries beneath an idempotency ledger.

### Same database, split commits
`effect COMMIT → crash → dedupe absent → retry` produced **two effects**.

### Same database, one transaction
`BEGIN → effect + dedupe → COMMIT`:
- pre-COMMIT crash rolled both back;
- successful retry committed one effect+ledger;
- post-COMMIT response-loss retry replayed the original result; effect count remained one.

### External provider + local ledger
Provider effect committed, local ledger write was lost, and retry duplicated the provider effect. A local transaction cannot make a separately committed external side effect atomic.

### Provider-owned idempotency
Stable operation identity at the provider returned the original result on retry; provider effect count remained one.

### Transactional outbox / consumer inbox
Producer transaction atomically persisted business state + outbox row. Duplicate relay still duplicated a naive consumer. Consumer-side inbox + effect in one transaction reduced repeated delivery to one effect.

Critical rule:

> **Idempotency protection is only as strong as the atomicity/reconciliation boundary connecting the protected business effect and the dedupe result.**

Do not use `exactly once` without naming which effect/store/consumer/failure boundary is meant.

Evidence level: **PRACTICE + CRITIQUE / deliberate replication + SQLite crash-window + dual-write/outbox/inbox transfer**.

Remaining: production DBs/providers/gateways/distributed systems, retention/security, real browser/mobile stack, AT and app-stage human validation.

---

# I006 — sequence collaboration boundary

I006 asks when I004-style record/field merge is structurally too coarse for collaborative text/list/document data.

Controlled matrix: **18/18**.

Established:
- whole-field LWW converged by discarding one concurrent insertion;
- raw base-index operations kept both edits but diverged across replicas (`AYXB` vs `AXYB`);
- a deliberately minimal OT-like transform control preserved both inserts and converged to `AXYB`;
- a deliberately minimal stable-anchor/operation-ID CRDT-like control converged independent of delivery order;
- retaining a deleted anchor as a tombstone-like reference allowed a concurrent insertion to remain positionable in the bounded control;
- deterministic concurrent list-move resolution converged but discarded one participant's move intent;
- whole-field conflict detection can also over-escalate disjoint text edits that a sequence-aware model could combine.

Central distinction:

> **Convergence, intent preservation, and domain-semantic correctness are three different gates.**

Decision boundary:
- versioned record/field merge remains suitable for many scalar/map business records;
- investigate OT/CRDT/serialization/locking/domain operations when the same sequence is concurrently authored, offline multi-writer editing matters, positions shift under concurrency, and independent edits should normally survive automatically.

The OT-like and CRDT-like controls are didactic failure-isolation models, not production algorithm proofs.

Evidence level: **PRACTICE + CRITIQUE / sequence concurrency boundary study**.

Remaining: production OT/CRDT library correctness, rich text, Unicode/IME, selections, collaborative undo, schema evolution, metadata GC, performance/network/security, real app/browser/native integration and human collaboration quality.

---

## Other established blocks

- **L001**: border-ownership cue isolation + optical raster proof. Human observation deferred.
- **L002**: 216-condition density/reflow proof; fake compactness rejected.
- **L003**: mixed-script/fallback wrap-threshold transfer.
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
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | exact delivered font/package/axis/normalization/shaping/cross-platform pending |
| Dense numeric comparison | PRACTICE / CRITIQUE | locale/accounting/dynamic/human pending |
| Color-driven density/salience | PRACTICE / CRITIQUE | device/environment/human pending |
| Interaction agency/state/navigation | CRITIQUE | broader real platform/AT/human pending |
| Async/retry/cancel | PRACTICE / CRITIQUE | production API/proxy/background-sync/AT pending |
| Color-channel-independent semantics | PRACTICE / CRITIQUE | real OS/AT/production pending |
| Concurrent edits/offline conflict | PRACTICE / CRITIQUE | **I004: 17+16+18+15+20+18**; production DB/storage/multi-device pending |
| Ambiguous outcome / duplicate-sensitive intent | PRACTICE / CRITIQUE | **I005: 18+26**; production/distributed/provider/gateway/browser/mobile pending |
| Sequence collaboration / OT-CRDT boundary | PRACTICE / CRITIQUE | **I006: 18** bounded assertions; production algorithms/editor/platform/human pending |

---

## Active next queue

Human work is deferred to app-development validation and does not block non-human research.

1. **Stage 1 Layout/Interaction closure audit** — re-read the actual Master Curriculum and distinguish true Foundation blockers from later production/human/platform validation, following the useful Color C014 precedent without copying its conclusions.
2. **I004 production local-store / multi-device partitioning** when suitable real framework/storage infrastructure becomes available.
3. **I005 production provider/gateway retry transfer** when a real project/API stack exists.
4. **I006 production sequence-collaboration transfer** only if a live product actually requires collaborative text/list editing; do not adopt CRDT/OT for study volume.
5. **L006 production/platform transfer** when real OS/AT/cross-browser/mobile/framework environments become available.
6. **Consume W001/W002+ evidence** and independently reproduce high-risk Web findings where useful.
7. **L004 only if project-relevant** — delivered font, locale/accounting, dynamic update, actual zoom/DPR.
8. Open `L007` or `I007` only for a genuinely higher-value new question after the closure audit.

## APP-DEVELOPMENT VALIDATION queue

Execute only with live app/prototype and suitable participants:
- L001 border ownership and optical-centering judgments;
- L002/L005/C007 task performance/error vs preference/workload;
- L006 layer comprehension/dismissal expectations;
- I004/I005 sync/conflict/retry/authorization-recovery comprehension;
- I006 collaborative-editing comprehension if relevant to a live product;
- real accessibility-user validation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type
- T015 strengthens exact runtime-state testing before Layout geometry conclusions.
- I006 adds a collaboration boundary: text operation identity must not be confused with Unicode normalization, grapheme segmentation, shaping or raster position.

### Color
- Color Stage 1 PASS is acknowledged without implying production/device/human PASS.
- Sync/collaboration states remain semantic Interaction roles; Color may reinforce but not define them.

### Web Design
- W001 is now available as the first Web baseline.
- Highest-value future transfer includes L006 overlay matrices, I004/I005 offline/idempotency contracts, and I006 only where a real collaborative editor exists.
- W001's relationship-first model supports the queue conclusion: correctness depends on relationships among operations, resources, actors, identities and states—not only request order or pixels.
- Web should verify actual `fetch`/retry/storage behavior, dependency-aware queues, account partitioning, provider idempotency boundaries, and—when applicable—browser editor/IME/selection behavior with the chosen collaboration library.

---

## Latest checkpoint

- `L001`–`L006`: studied spatial modules remain PRACTICE / CRITIQUE where applicable.
- `I001`: CRITIQUE.
- `I002` / `I003` / `I004` / `I005` / `I006`: PRACTICE / CRITIQUE.
- I004 evidence: **17/17 + 16/16 + 18/18 + 15/15 + 20/20 + 18/18**.
- I005 evidence: **18/18 + 26/26**.
- I006 boundary evidence: **18/18**.
- Next IDs: Layout `L007`; Interaction `I007`.
- Human validation remains explicitly deferred to app-development stage.
- No Layout/Interaction Foundation PASS promotion claimed.
