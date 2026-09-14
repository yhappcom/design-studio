# I004 Extension — Multiple Queued Operations, Ordering, Compaction, Dependencies, and Conflict Propagation

Status: **PRACTICE + CRITIQUE / REAL HTTP + DURABLE QUEUE TRANSFER — ordering, semantic compaction, dependency-aware conflict propagation, and temp-identity remapping established; production framework/database/background-sync validation remains OPEN**

Owner: Layout, Spatial & Interaction Specialist — Interaction stream

Parents:
- `research/interaction/I004-concurrent-edits-conflict-merge-recovery.md`
- `research/interaction/I004-http-precondition-etag-transfer.md`
- `research/interaction/I004-offline-outbox-reconnect-transfer.md`
- `research/interaction/I004-ambiguous-outcome-idempotency-transfer.md`

Reproducible artifacts:
- `research/interaction/I004-multi-operation-queue-validation.py`
- `research/interaction/I004-multi-operation-queue-results.json`

## Question

Previous I004 evidence established one durable queued intent, reconnect, conflict detection, ambiguous outcomes, and idempotent retry boundaries.

The next product question is different:

> When several offline operations accumulate, which order must be preserved, which operations can be compacted, which later operations depend on earlier ones, and how far should one conflict propagate?

This matters because a production outbox is not just a bag of retryable requests. It can contain a partially ordered set of user intentions with identity, causality, and semantic dependencies.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Latest status checked through **T015**.
- Reusable method: exact runtime artifact/state must be tested rather than inferred from structural metadata alone.
- Transfer: queue/conflict UI must preserve exact local/remote text identity; normalization/fallback can matter to diffing and comparison.
- No Type mechanism is claimed here.

### Color
- Latest status checked through **C014**, with Stage 1 closure work active.
- Reusable rule: semantic states such as queued, blocked, conflict, confirmed, deleted, and dependency-blocked must exist before Color encoding.
- Color must not be the sole differentiator.

### Layout / Interaction
- I002/I004 and all current extensions checked.
- Reusable findings: retry is not conflict resolution; base/current/local are distinct; operation identity may need persistence; queue clearing follows authoritative confirmation.
- This study extends those rules from one queued item to several related items.

### Web Design
- Latest status checked through **W001**.
- W001 confirms browser/product behavior must be validated as relationships and state contracts rather than screenshot fidelity.
- Future Web transfer should reproduce this queue model with the production local store, service worker/background sync or chosen framework.

### Other / standards
- RFC 9110 — HTTP conditional requests / `If-Match`: https://www.rfc-editor.org/rfc/rfc9110.html
- RFC 6902 — JSON Patch: https://www.rfc-editor.org/rfc/rfc6902.html
- Android offline-first guidance: https://developer.android.com/topic/architecture/data-layer/offline-first

Relevant source facts:
- RFC 6902 defines a patch as an **ordered sequence**; operations are applied sequentially and each result becomes the input to the next.
- RFC 9110 allows `If-Match` to prevent stale state-changing requests.
- Android offline-first guidance explicitly uses persistent queues and notes that stronger ordering guarantees require a robust persistent queue rather than assuming a simple worker queue is sufficient.

### Overlap decision
**I004 EXTENSION + FAILURE REPRODUCTION + QUEUE-ALGEBRA PRACTICE**.

---

# Experimental environment

- actual local HTTP/1.1 origin server;
- strong version ETags;
- conditional PATCH-like operations using `If-Match`;
- SQLite-backed outbox as a durable lab substrate;
- multiple resource identities;
- explicit operation dependencies and temp→server identity mapping.

SQLite is only the persistence substrate for the lab. It is not a recommendation for Web, Flutter, Android, or iOS.

Final result: **20 / 20 assertions PASS**.

---

# 1. Ordering is part of meaning

Controlled operation sequence:

1. append `departed`;
2. append `arrived`.

Applied in queued order:

`["departed", "arrived"]`

Applied in reverse order:

`["arrived", "departed"]`

Both requests were technically valid, but they represented different histories.

## SYNTHESIS

A queue sequence number is not always implementation metadata. For order-sensitive operations, it is part of the user/domain intent.

## STUDIO JUDGMENT

Do not sort, batch, parallelize, or compact operations merely because doing so is operationally convenient. First classify whether operations commute.

---

# 2. Compaction depends on operation semantics, not field/path equality

## Case A — replace→replace

Two pure state-setting operations on the same field:

- title → `Flight 101A`
- title → `Flight 101B`

In the bounded model, compacting them to only the final replace produced the same authoritative final state as applying both in sequence.

This is a candidate for safe compaction **only when**:
- intermediate values have no required side effects/audit meaning;
- no later queued operation depends on the intermediate value;
- the original historical base is preserved;
- product/domain invariants still hold.

## Case B — increment→increment

Two operations:

- landings `+1`
- landings `+1`

Sequential result: `2`.

Naive “same path, keep only the last operation” compaction produced `1`.

A semantic compactor that combined deltas to `+2` preserved intent.

## Rule

**Path equality does not define compaction safety. Operation algebra does.**

Possible classifications include:
- last-state-wins replace;
- additive/commutative delta;
- ordered append;
- destructive delete;
- external side effect;
- identity-producing create;
- operation with explicit dependency.

Compaction must be defined by product semantics, not generic JSON/path deduplication.

---

# 3. Conflict propagation should follow dependencies, not freeze the whole queue

Controlled queue:

- `q1` — r1 notes change;
- `q2` — r1 title change, depends on q1;
- `q3` — independent r2 notes change;
- `q4` — r1 status change, depends on q2.

Sequence:
1. q1 commits;
2. q2 is rebased to q1's returned validator;
3. remote writer changes r1 title;
4. q2 receives `412 Precondition Failed`;
5. q2 becomes `conflict_same_field`;
6. q4 becomes `blocked_dependency`;
7. q3, which is independent, continues and commits.

Final statuses:

- q1 `confirmed`
- q2 `conflict_same_field`
- q3 `confirmed`
- q4 `blocked_dependency`

Authoritative r1 preserved the remote title; independent r2 still updated successfully.

## SYNTHESIS

Two naive strategies are both wrong:

### A. Stop the entire outbox on the first conflict
Overly conservative. Independent work is delayed for no semantic reason.

### B. Continue every later operation
Unsafe. Descendants can execute against a state whose prerequisite never committed.

## STUDIO JUDGMENT

Conflict propagation follows the **dependency graph / aggregate semantics**, not simply queue position.

A practical drainer needs to distinguish:
- confirmed predecessor;
- unresolved predecessor;
- independent operation;
- same aggregate but semantically independent operation;
- descendant whose meaning assumes predecessor success.

---

# 4. Create→edit requires identity dependency

Offline queue:

1. create `temp-1`;
2. edit notes on `temp-1`, depending on the create.

Naive attempt to send the edit before creation returned `404`.

Revised flow:

1. create commits;
2. server returns new identity `r3` + validator;
3. durable temp→server identity mapping is recorded;
4. dependent queued edit is rewritten to target `r3`;
5. edit uses the returned validator;
6. final record contains both the created content and the offline dependent edit.

## Rule

Identity production is part of queue dependency semantics.

A queue item can depend on:
- an earlier state mutation;
- a generated server identity;
- a returned validator/version;
- an authorization/finalization decision;
- an external side-effect result.

A FIFO list alone does not express all of these relationships.

---

# Updated queue model

For important offline mutations, represent at least:

`operation identity`
`resource/local identity`
`server identity if known`
`historical base validator`
`operation semantics`
`payload/intent`
`sequence`
`dependencies`
`status`
`authoritative result`
`conflict metadata`

Relevant statuses now include:

`queued`
`network pending`
`ready`
`confirmed`
`outcome unknown`
`conflict`
`blocked dependency`
`deleted/finalized`
`already applied`
`identity mapping pending`
`recovered as new`

---

# Queue compaction decision

Before squashing two queued operations, ask:

1. Do they target the same aggregate/object?
2. Are they order-sensitive?
3. Do they commute?
4. Is either operation externally observable?
5. Does an intermediate value have audit/workflow meaning?
6. Does a later operation depend on the intermediate result?
7. Does either operation produce an identity or validator?
8. Can the compacted operation still be reconciled against the **original historical base**?
9. Would compaction change retry/idempotency behavior?
10. Can the product prove semantic equivalence, not just data-shape similarity?

If these questions cannot be answered, preserve the operations separately.

---

# Failure modes rejected

- generic “same field/path → keep last” compaction;
- reordering an outbox by type or convenience when order is semantic;
- clearing the entire queue because one item conflicts;
- continuing descendants after an unresolved prerequisite;
- assuming FIFO order alone captures identity/dependency relationships;
- editing a temporary object identity before its server identity exists;
- replacing the earliest historical base with a later local pseudo-base during compaction;
- combining external side effects merely because their payloads look similar;
- hiding `blocked_dependency` inside a generic sync error.

---

# Evidence limits / OPEN

This study does not establish:
- production IndexedDB/Room/Core Data/Flutter database behavior;
- service-worker/background-sync scheduling;
- real multi-process/mobile race timing;
- graph scheduling at scale;
- queue compaction across app upgrades/schema migrations;
- authorization or finalization changes while offline;
- external payment/message/booking side effects;
- distributed server ordering;
- CRDT/OT for collaborative text/list/order domains;
- transactionally atomic outbox + domain-state persistence;
- human understanding or AT announcements.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Conflict/queue surfaces may need to show several queued operations, dependency reasons, exact local/remote strings and generated identities.
- Preserve exact text semantics; do not let normalization/fallback assumptions silently change diff meaning.
- Scope limit: no Type policy is defined here.

### Color
- `blocked dependency`, `conflict`, `pending`, `confirmed`, `identity mapping pending`, and `outcome unknown` are separate semantic states.
- Color can support these distinctions but must not become the only channel.

### Layout / Interaction
- An outbox should be modeled as a **dependency-aware preserved-intention structure**, not just FIFO network retries.
- Compaction is a domain operation-algebra decision.
- Conflict propagation should block semantic descendants while allowing independent work to continue.

### Web Design
- Reproduce using the production local-store and synchronization stack.
- Test reload/crash, concurrent tabs, service-worker/background retries, temp-ID mapping, conditional requests, dependency blocking, queue compaction and UI/AT exposure.
- W001's relationship-first principle applies directly: sync correctness depends on relationships among operations, not only request order.

---

# Evidence level

**PRACTICE + CRITIQUE / real HTTP + durable queue + ordered-operation + semantic-compaction + dependency-graph transfer.**

No production PASS.
