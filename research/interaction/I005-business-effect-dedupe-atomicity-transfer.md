# I005 Extension — Business-Effect / Dedupe Atomicity, Transactional Outbox, and Consumer Inbox

Status: **PRACTICE + CRITIQUE / DATABASE-BOUNDARY FAILURE→REVISION — split-commit duplicate, same-DB atomic effect+ledger, external-provider boundary, transactional outbox, and consumer inbox evidence established; production DB/provider/distributed validation remains OPEN**

Owner: Layout, Spatial & Interaction Specialist — Interaction stream

Parent studies:
- `research/interaction/I002-latency-pending-optimistic-retry.md`
- `research/interaction/I004-ambiguous-outcome-idempotency-transfer.md`
- `research/interaction/I005-ambiguous-outcome-idempotency.md`

Reproducible artifacts:
- `research/interaction/I005-business-effect-dedupe-atomicity-validation.py`
- `research/interaction/I005-business-effect-dedupe-atomicity-results.json`

## Question

I005 established that one duplicate-sensitive user intent needs one stable semantic identity across retry attempts. A remaining production risk was explicit in that study:

> What if the business side effect commits, but the idempotency/dedupe record does not?

A key ledger only prevents duplicates if its relationship to the business effect is itself reliable. This study therefore separates three atomicity boundaries:

1. business effect and dedupe ledger in the **same database**;
2. business effect in an **external provider/system** plus a local dedupe ledger;
3. local business state plus an **outbox message**, followed by potentially duplicate delivery to a consumer.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Latest Type evidence checked through T015.
- No Type mechanism is tested.
- Recovery status text must distinguish `unknown`, `replayed`, `duplicate prevented`, and `external reconciliation required` without collapsing them.

### Color
- Color Stage 1 PASS acknowledged; production/device/human Color remains separate.
- Atomicity/retry states are semantic roles before visual encoding.
- Color must not be the sole channel for `outcome unknown`, `replay confirmed`, `duplicate`, or `reconciliation required`.

### Layout / Interaction
- I002 established `outcome unknown ≠ failure`.
- I004/I005 established durable intent identity, response-loss duplicate failure, and same-key replay/concurrent-duplicate handling.
- This extension tests the unresolved storage/commit boundary beneath that interaction contract.

### Web Design
- W001 is available; next W002.
- Future Web/product transfer should inspect actual client mutation libraries and backend architecture rather than assuming an idempotency header/key implies end-to-end atomicity.

### Other / architecture sources
Authoritative/primary implementation source:
- SQLite transaction documentation: https://www.sqlite.org/lang_transaction.html

Architecture guidance:
- AWS Prescriptive Guidance — Transactional Outbox Pattern: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html

Relevant source boundaries:
- SQLite supports explicit transactions with COMMIT/ROLLBACK; the lab uses this to test one-database atomic grouping.
- AWS describes the transactional outbox as a response to the **dual-write** problem when one operation must both persist database state and publish a message/event. It also warns that duplicate messages can still occur and consumers should be idempotent.
- AWS guidance is architecture guidance, not a universal protocol standard.

### Overlap decision
**I005 EXTENSION + FAILURE REPRODUCTION + ATOMICITY-SCOPE VALIDATION**.

---

# Experimental environment

Three independent SQLite databases were used as controlled boundaries:

- application DB;
- external-provider DB;
- consumer DB.

Tables model:
- business effects;
- idempotency/dedupe ledger;
- business state;
- transactional outbox;
- consumer inbox.

Crash windows are deliberately inserted between specific commits or before transaction COMMIT.

Final result: **26 / 26 assertions PASS**.

SQLite is a lab substrate. This does not imply SQLite is the required production implementation.

---

# Scenario 1 — same database, split commits: ledger exists in theory but duplicate still occurs

Broken flow:

1. operation `op1` inserts business effect `e1`;
2. effect transaction commits;
3. process crashes before inserting `op1 → e1` into the dedupe ledger;
4. retry checks ledger and sees no key;
5. retry inserts business effect `e2`;
6. retry records `op1 → e2`.

Observed:
- effect count after first commit/crash = `1`;
- ledger count = `0`;
- effect count after retry = **`2`**.

## Finding

A dedupe table is not sufficient if the business effect and dedupe record can commit independently.

## Rule

> **Idempotency protection is only as strong as the atomicity boundary connecting the business effect and the dedupe result.**

---

# Scenario 2 — same database, one transaction: effect + dedupe can share the crash boundary

Revised flow:

`BEGIN → insert effect → insert dedupe record → COMMIT`

## Pre-COMMIT crash

The harness raises a simulated crash before COMMIT and rolls back the transaction.

Observed:
- effect count = `0`;
- dedupe count = `0`.

Retry then performs the full transaction and commits one effect plus one ledger record.

## Post-COMMIT response loss

After successful commit, the client is assumed not to have received the result. A retry with the same semantic key finds the ledger and returns the original effect result.

Observed:
- original effect id = retry effect id;
- retry mode = `replay`;
- total effect count remains **`1`**.

Same key with a materially different payload is rejected in the bounded contract.

## Finding

For state fully contained in one transactional database, effect and dedupe state can share a commit boundary.

This does **not** mean every database/framework has identical durability semantics, nor does it prove distributed exactly-once execution.

---

# Scenario 3 — external provider effect + local ledger: local transaction cannot make the remote effect atomic

The provider is represented by a separate database.

Broken flow:

1. provider commits payment-like effect `p1`;
2. client/app crashes before recording `pay-op → p1` in its local ledger;
3. local retry sees no dedupe entry;
4. provider receives the operation again and creates `p2`;
5. local app then records only the second result.

Observed provider effect count: **`1 → 2`**.

## Finding

A local database transaction cannot retroactively make a separately committed external side effect part of the same transaction.

## Rule

When the effect crosses a system boundary, safety requires a contract at that boundary, such as:
- provider-supported stable idempotency/operation identity;
- authoritative provider lookup/reconciliation;
- domain-specific compensating action;
- transactional messaging/outbox at a suitable boundary;
- another explicitly validated distributed consistency strategy.

Do not claim “exactly once” merely because the local application has an idempotency table.

---

# Scenario 4 — provider-level stable operation identity repairs the bounded external retry case

The external provider is revised to own its own atomic:

`operation key + payload → provider effect/result`

First request:
- provider effect `p1` commits;
- local application does not record the result (simulated crash/response loss).

Retry:
- same operation key;
- same payload;
- provider returns `p1` as replay;
- no new provider effect occurs;
- local application can then reconcile/store the returned result.

Observed provider effect count remains **`1`**.

## Finding

The idempotency contract must exist **where the duplicate-sensitive side effect is actually committed** or the system must have an equally strong reconciliation strategy.

---

# Scenario 5 — transactional outbox repairs one dual-write boundary, but delivery can still duplicate

## Producer side

Broken dual-write risk:
- business database change and event/message publication are two separate effects.

Lab revision:

`BEGIN → write business row → write outbox row → COMMIT`

A simulated crash before COMMIT rolls back both.

Observed:
- business count = `0`;
- outbox count = `0`.

Successful retry commits:
- business row = `1`;
- outbox row = `1`.

This demonstrates the **local producer-side atomic boundary** of the transactional outbox pattern.

## Consumer side — naive duplicate delivery

The same outbox message is delivered twice to a consumer that simply performs its side effect.

Observed consumer effect count = **`2`**.

Therefore transactional outbox does not itself imply exactly-once downstream effect.

## Consumer-side inbox/dedupe revision

Consumer transaction:

`BEGIN → check/insert message id in inbox → apply consumer effect → COMMIT`

A simulated crash before COMMIT rolls back both inbox and consumer effect.

On delivery/retry:
- first committed delivery produces one effect and one inbox record;
- second delivery with the same message id returns/replays without another effect.

Observed:
- consumer effect count = `1`;
- inbox count = `1`.

## Finding

Reliable producer publication and duplicate-safe consumption are **two different boundaries**.

---

# Updated atomicity model

Before approving duplicate-sensitive retry, locate the authoritative effect and its dedupe contract:

### Boundary A — same transactional store
Can business effect + dedupe result commit/rollback together?

### Boundary B — external provider
Does the provider itself support a stable operation identity or authoritative reconciliation? A local ledger alone cannot cover the remote commit window.

### Boundary C — producer database + message broker
Can business state + outbox intent commit together? How is message relay retried?

### Boundary D — message consumer
Can consumer side effect + processed-message/inbox marker commit together, or is the consumer's own effect external again?

### Boundary E — client knowledge
Even when server-side execution is safe, does the UI distinguish:
- still processing;
- outcome unknown;
- replay-confirmed;
- reconciliation required;
- actual failure?

---

# Failure modes rejected

- “We have an idempotency table, so duplicate execution is solved” without checking commit boundaries;
- effect COMMIT followed by dedupe COMMIT as two independent writes;
- wrapping only the local ledger in a transaction while the business effect is external;
- assuming transactional outbox means exactly-once message delivery or consumption;
- consumer side effect without duplicate-delivery protection where duplicate messages are possible;
- generating a new operation/message identity after uncertain outcome;
- clearing client intent because a local write succeeded while authoritative external outcome is unresolved;
- using the phrase `exactly once` without defining **which effect, store, consumer, and failure boundary** it refers to.

---

# Product / interaction consequence

Atomicity architecture changes which UI states are truthful.

If the system cannot establish whether an external effect committed, the UI must remain in `outcome unknown / reconciliation required` rather than fabricating `failed` or encouraging a fresh duplicate-sensitive intent.

If server/provider replay proves the same operation already committed, the correct UI state is recovery/confirmation of the **existing intent**, not creation of a second intent.

Interaction design therefore needs the backend's real commit/idempotency boundaries as an input.

---

# Evidence limits / OPEN

This study does not establish:
- PostgreSQL/MySQL/Firestore/DynamoDB transaction equivalence;
- real payment/booking/message-provider guarantees;
- two-phase commit;
- saga correctness;
- Kafka/SQS/PubSub delivery semantics;
- multi-region replication;
- actual process/power-loss durability at storage-engine/fsync level;
- outbox relay leasing/concurrency/order at scale;
- dedupe/inbox retention and garbage collection;
- transactional boundaries spanning arbitrary external providers;
- security/replay policy;
- production gateway/proxy retry behavior;
- browser/mobile persistence;
- AT or human comprehension.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Recovery copy must distinguish `outcome unknown`, `replay confirmed`, and `external reconciliation required` precisely.
- No Type construction policy is defined.

### Color
- These result states are semantic, not palette variants. Color may reinforce but cannot define them.

### Layout / Interaction
- Stable intent identity is insufficient without a reliable effect↔dedupe atomicity/reconciliation boundary.
- The phrase “retry safe” must name the protected effect and boundary.
- `exactly once` should not be used as a generic UX/backend property.

### Web Design
- When transferring I005 into a real product, inspect the actual API/provider architecture.
- Test response loss **after** business commit, not only failed connection before send.
- Verify whether backend dedupe state commits atomically with the protected effect, and whether framework retry middleware can cross that boundary safely.

---

# Evidence level

**PRACTICE + CRITIQUE / SQLite transaction crash-window reproduction + separate-provider dual-write failure + provider-level idempotency revision + transactional-outbox/consumer-inbox transfer.**

**26 / 26 bounded assertions PASS.**

No production PASS.
