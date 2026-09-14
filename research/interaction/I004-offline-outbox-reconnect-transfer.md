# I004 Extension — Durable Offline Outbox, Reconnect, and Multi-Client Conflict Transfer

Status: **PRACTICE + CRITIQUE / DURABLE OUTBOX + REAL HTTP RECONNECT TRANSFER — restart persistence, 412 rebase, same-field hold, and delete-vs-edit recovery established; production mobile/web storage, physical multi-device, background sync, AT and human validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist — Interaction stream  
Parent studies:
- `research/interaction/I004-concurrent-edits-conflict-merge-recovery.md`
- `research/interaction/I004-http-precondition-etag-transfer.md`

Reproducible artifacts:
- `research/interaction/I004-offline-outbox-http-validation.py`
- `research/interaction/I004-offline-outbox-http-results.json`

## Question

I004 already established a controlled conflict state machine and actual HTTP `ETag` / `If-Match` lost-update prevention. The next unresolved question was whether the same semantic contract survives:

`authoritative base → local offline draft → durable queued mutation → app/process restart → remote change while offline → reconnect → stale precondition → semantic conflict resolution`.

This extension asks whether local work survives unavailable network/restart, whether the original base validator stays attached to the queued intent, whether disjoint changes rebase only after stale detection, whether same-field conflicts remain durable, and whether delete-vs-edit preserves work under a new identity rather than silently resurrecting the original.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through **T014**.
- Reusable finding: exact runtime input representation matters; T013/T014 show semantically equivalent text can reach downstream systems through materially different code-point/package states.
- Transfer opportunity: future conflict/outbox UI must preserve exact local/remote content through localization, normalization, fallback and long-text wrapping.
- Dependency: no Type construction or shaping claim is made here.

### Color
- Evidence checked: `progress/COLOR_STATUS.md` through **C012**.
- Reusable finding: semantic state precedes Color encoding; Color cannot repair a lost draft or ambiguous sync state.
- Transfer opportunity: queued/pending/conflict/deleted/merged states must remain distinguishable under forced-colors and production themes.
- Dependency: no Color threshold or palette conclusion is claimed.

### Layout / Interaction
- Evidence checked: I001–I004, especially I002 outcome-unknown/retry semantics and I004 conflict taxonomy.
- Reusable finding: retry is not conflict resolution; drafts need a lifecycle; conflict semantics require base/current/local state; delete-vs-edit changes object identity semantics.
- Extension opportunity: add a durable outbox and restart/reconnect lifecycle around the existing HTTP precondition proof.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; still no substantive `W###` evidence.
- Implementation opportunity: later reproduce the same contract using real IndexedDB/service-worker/background-sync/framework data layers and target browsers.
- Scope limit: current fallback harness is not Web production evidence.

### Other / cross-cutting
Authoritative/current sources checked:
- RFC 9110 HTTP Semantics — conditional preconditions and `If-Match` lost-update protection: https://www.rfc-editor.org/rfc/rfc9110.html
- Android Developers, offline-first data layer — offline local/network divergence requires reconciliation and often version metadata/history: https://developer.android.com/topic/architecture/data-layer/offline-first
- MDN IndexedDB transaction/storage guidance — browser-local persistence is transactional and useful for offline applications, but durability semantics are implementation-specific: https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API and https://developer.mozilla.org/en-US/docs/Web/API/IDBTransaction

### Overlap decision
- **EXTENSION + TRANSFER VALIDATION + FAILURE-PREVENTION PRACTICE**.
- Why: original I004 state-machine and HTTP-precondition proofs did not yet establish persistence across an offline/restart/reconnect lifecycle.

---

# SOURCE / SYNTHESIS BOUNDARY

## SOURCE

RFC 9110 establishes that an origin server evaluates `If-Match` before applying a state-changing request and returns `412 Precondition Failed` when the condition is false, unless the server can determine that the requested change already succeeded.

Android's offline-first guidance treats local/network divergence as a reconciliation problem and notes that version metadata/history is often required. It presents last-write-wins as one possible strategy, not a universal semantic rule.

IndexedDB documentation establishes browser-local transactional persistence suitable for offline applications while documenting durability nuances. This study does **not** claim SQLite and IndexedDB are equivalent implementations.

## SYNTHESIS

An offline mutation needs more than a payload. To resolve reconnect safely, the durable queue must retain enough context to answer:
- which authoritative state the user edited;
- which validator represented that base;
- what local intent changed;
- what current authoritative state now exists;
- whether those intentions can coexist semantically.

## STUDIO JUDGMENT

A practical queued mutation record should retain, where domain value justifies it:

`operation id / object identity / base validator / base representation or sufficient base diff context / local intent or patch / preserved local draft / queue status`.

Do not erase the base validator merely because reconnect discovers a newer server representation. The newer representation is the **current state**, not retroactively the base of the offline edit.

---

# Experimental environment

The intended first harness used Chromium + a local HTTP origin + IndexedDB. The installed Chromium environment blocked localhost navigation with `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Launch variations did not change that policy.

This is an **experimental infrastructure limitation**, not a product/browser conclusion.

The fallback harness separates the contracts:
- actual HTTP/1.1 origin-server requests using Python `urllib`;
- durable per-client outbox/draft persistence using separate SQLite files.

SQLite is a **test persistence substrate**, not a recommendation that Web use SQLite or proof of IndexedDB behavior. Two independent local databases represent two client installations/processes; restart is simulated by closing and reopening the database-backed client.

Final result: **18 / 18 assertions PASS**.

---

# Scenario 0 — network unavailable: queue must remain durable

Client A fetches r1 at `"r1-v1"`, edits notes locally, writes mutation+draft to durable storage, becomes offline and attempts flush. Flush becomes `network_pending`; nothing is removed. The client process is then recreated from the same local database.

Validated:
- outbox still contains the original base ETag;
- local draft remains intact;
- status remains pending;
- no success state is fabricated merely because local persistence succeeded.

### Rule

**Local persistence success is not remote commit success.**

Distinguish at least:

`saved locally / queued for sync / remotely confirmed / conflict / outcome unknown`.

---

# Scenario 1 — disjoint offline edit, remote edit, reconnect, safe rebase

Initial server:
- r1 v1: title `Flight 101`, notes `Routine`;
- A and B both observe ETag `"r1-v1"`.

While A is offline:
- A queues notes → `Weather diversion` against base v1;
- A process closes;
- B changes title → `Flight 101A`, server becomes v2.

After A restarts and reconnects:
1. durable outbox still says base `"r1-v1"`;
2. queued `PUT If-Match: "r1-v1"` receives 412;
3. current `GET` observes v2/`"r1-v2"`;
4. local changed field = `notes`;
5. remote changed field = `title`;
6. controlled domain declares them semantically independent;
7. merged representation is written with `If-Match: "r1-v2"`;
8. server becomes v3;
9. only after authoritative success are outbox and draft cleared.

Final state preserves both `Flight 101A` and `Weather diversion`.

### Rule

**Reconnect does not mean replay until success.**

Safe flow:

`replay with original base validator → stale detection → fetch current → semantic classification → rebase if safe → conditional write against current validator`.

Queue clearing follows authoritative confirmation.

---

# Scenario 2 — same-field conflict remains durable and unresolved

A queues title `Flight 101B` from v1 while offline; B changes title to `Flight 101A` and commits v2. On reconnect, stale conditional write fails and current v2 is fetched. Both local and remote changed `title` relative to the same base.

Validated:
- no automatic server write occurs;
- authoritative server remains `Flight 101A`, v2;
- local draft `Flight 101B` remains durable;
- outbox remains with `conflict_same_field`;
- overlap metadata identifies `title`.

### Rule

A durable outbox is not only a retry queue. It can become a **durable unresolved-intention store**.

Do not delete or rewrite the queued local intent merely because current server state was fetched.

---

# Scenario 3 — remote delete while offline edit exists

A queues notes `Keep this local note` from r1 v1 while offline. B deletes r1. A restarts and reconnects; stale write receives 412 and current GET returns 404.

Validated:
- conflict becomes `deleted_conflict`;
- r1 remains deleted;
- local draft and outbox remain durable;
- no automatic resurrection occurs.

Explicit recovery:
- user/domain chooses `keep as new`;
- local content is written as r2 with `If-None-Match: *`;
- r2 is created at v1;
- r1 remains 404;
- only after r2 commit succeeds are pending outbox/draft cleared.

### Rule

**Sync recovery must preserve identity semantics.**

“Keep my work” can mean “create a new object”, not “force the deleted identity back into existence”.

---

# What this adds to I004

I004 now has three distinct evidence layers:
1. **17/17 controlled Chromium state-machine assertions** — conflict taxonomy and UX/recovery semantics;
2. **16/16 real HTTP ETag/If-Match assertions** — stale-write prevention and conditional recovery;
3. **18/18 durable offline/restart/reconnect assertions** — pending outbox persistence, safe rebase, same-field retention, delete-vs-edit identity recovery.

The third layer adds a temporal distinction:

`base state` is a historical fact attached to the queued user intent.

A reconnect fetch produces `current state`; it must not silently overwrite the queued operation's memory of its base.

---

# Product design contract for offline sync

For important user-authored records, specify these states explicitly:
1. **Local draft** — not yet queued or committed.
2. **Queued / saved locally** — durable on device, not remotely confirmed.
3. **Syncing** — attempt in progress.
4. **Remote confirmed** — authoritative commit established.
5. **Network pending** — no authoritative result yet; local work remains durable.
6. **Mergeable stale base** — server changed, but domain can safely combine intentions.
7. **Conflict requiring resolution** — competing semantic intent remains.
8. **Deleted/finalized remotely** — object identity/workflow may no longer accept mutation.
9. **Recovered as new/compensating action** — local work preserved through a new semantic operation.

Do not collapse these into binary `synced / error`.

---

# Failure modes rejected

- clearing the outbox when local persistence succeeds;
- clearing the outbox before remote confirmation;
- replacing a queued operation's base validator with the latest fetched ETag;
- automatic stale-write retry until it wins;
- last-write-wins without an explicit accepted loss model;
- discarding the draft on 412;
- auto-merging different JSON fields without domain independence evidence;
- silently recreating a remotely deleted object;
- representing `network pending`, `same-field conflict`, and `remote deletion` as one generic error;
- assuming a persistent queue implementation alone solves sync semantics.

---

# Evidence limits / OPEN

This study does **not** establish:
- IndexedDB-specific behavior or browser storage eviction semantics;
- Service Worker / Background Sync behavior;
- Android Room/DataStore, iOS Core Data/SwiftData, Flutter local database behavior;
- physical multi-device timing/races;
- multi-operation queue ordering or compaction;
- duplicate-delivery/idempotency under ambiguous network outcomes;
- authorization changes while offline;
- server finalization/approval/payment side effects;
- text/list/order CRDT/OT behavior;
- production database transaction/isolation behavior;
- encryption/key-loss/logout/account-switch handling for queued data;
- AT announcements or human understanding of sync/conflict state.

The localhost Chromium policy prevented browser-origin + IndexedDB + HTTP integration in this environment. That exact Web transfer remains OPEN for Web Design/live project infrastructure.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Offline conflict surfaces can preserve long local and remote strings across restart and must not normalize away meaningful content during comparison.
- T013/T014 normalization evidence should be considered when exact text identity matters to diff/merge.
- Scope limit: I004 does not define normalization or shaping policy.

### Color
- `queued`, `network pending`, `mergeable stale`, `same-field conflict`, `remote deleted`, and `confirmed` are distinct semantics.
- Color may encode them but must not collapse them or become the sole channel.
- Scope limit: no visual threshold claim.

### Layout / Interaction
- Base/current/local are three different state dimensions.
- A durable outbox is a preserved-intention store, not merely a retry list.
- Queue clearing is an interaction/data commitment decision and should follow authoritative confirmation.
- Delete-vs-edit recovery may require new identity.

### Web Design
- Reproduce this contract with actual IndexedDB/service-worker/background-sync or the chosen production framework.
- Specifically verify queue persistence across reload/crash, storage eviction policy, reconnect races, concurrent tabs, exact ETag handling, and UI status/focus/AT behavior.
- The failed localhost Chromium navigation in this environment is an infrastructure limitation, not browser-product evidence.

---

# Evidence level

**PRACTICE + CRITIQUE / real HTTP origin + durable two-client SQLite outbox + process restart/reconnect transfer.**

Not PASS. Production storage, browser/mobile framework, real multi-device, ambiguous-result idempotency, queue ordering, authorization/finalization, AT and human evidence remain open.
