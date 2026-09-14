# I005 — Ambiguous Outcome, Idempotent Intent, and Duplicate-Submission Recovery

Status: **PRACTICE + CRITIQUE / REAL HTTP FAILURE→REVISION — ambiguous response loss, duplicate side effect, stable intent key, payload fingerprint mismatch, and concurrent duplicate handling established; production API/storage/mobile/browser/AT/human validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist — Interaction stream

Reproducible artifacts:
- `research/interaction/I005-ambiguous-outcome-idempotency-validation.py`
- `research/interaction/I005-ambiguous-outcome-idempotency-results.json`

## Question

I002 established that timeout/transport failure can produce **outcome unknown**, not necessarily failure. I004 then established conflict prevention, durable offline intent, and an initial **15/15 applied-but-response-lost / application-operation-ID** proof. I005 is therefore a deliberate replication and extension, not a claim that duplicate execution was previously untested.

The remaining high-value question is whether the prior application-specific result survives an independently rebuilt harness that follows the latest available HTTPAPI draft pattern more closely and adds **concurrent same-key processing**:

> If a non-idempotent user action may already have committed but its response is lost, how can the product retry without performing the same user intent twice?

This study separates:
- transport/result knowledge;
- user intent identity;
- operation side effect;
- retry attempt identity;
- request payload fingerprint;
- concurrent duplicate processing.

The target is not payments specifically. The same contract can matter for create/send/submit/export/booking-like actions whose duplicate side effect is materially harmful.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through **T015** at study start.
- Reusable finding: exact delivered/runtime representation must be fixed before downstream claims.
- Transfer opportunity: idempotency fingerprinting and user-facing recovery must not casually normalize or rewrite semantically meaningful payload content.
- Scope limit: no Type construction/shaping claim.

### Color
- Evidence checked: `progress/COLOR_STATUS.md`; Stage 1 is now **PASS**, Stage 2 entry audit next.
- Reusable finding: semantic states precede Color encoding.
- Transfer opportunity: `pending`, `outcome unknown`, `confirmed`, `duplicate replay`, and `conflict` must not collapse into one color-coded error.
- Scope limit: no Color threshold/palette claim.

### Layout / Interaction
- Evidence checked: I002 and I004 including HTTP preconditions and durable offline outbox.
- Reusable finding: `outcome unknown ≠ failure`; retry is not automatically safe; durable intent must survive restart/reconnect.
- Existing overlap: `I004-ambiguous-outcome-idempotency-transfer.md` already reproduced duplicate POST after response loss and repaired it with an application-specific `X-Operation-Id`.
- Replication/extension: I005 independently reproduces the duplicate failure with a fresh harness, then adds the expired draft-07 `Idempotency-Key`-style fingerprint/replay model and a **same-key concurrent in-flight request** case.
- Value: confirms the earlier direction while testing a failure class I004 did not cover: a duplicate arriving **before** the original operation completes.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; **W001 now exists** and Web is in Stage 1 PRACTICE/CRITIQUE.
- Transfer opportunity: later reproduce this contract using production `fetch`, framework mutation layers, real API gateway/proxy behavior, browser reload/offline, and page-level status/recovery.
- Scope limit: this local HTTP harness is not Web production PASS.

### Other / cross-cutting
Authoritative/current sources checked:
- RFC 9110 §9.2.2 Idempotent Methods: https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods
- IETF HTTPAPI `draft-ietf-httpapi-idempotency-key-header-07`: https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/

Important status boundary: as of this study, draft-07 is **expired Internet-Draft / work in progress**, not an RFC. Its `Idempotency-Key`, fingerprint, replay, 409 and 422 patterns are used as bounded practice evidence, not as a claim of standardized final semantics.

### Overlap decision
- **DELIBERATE REPLICATION + EXTENSION + ADVERSARIAL FAILURE REPRODUCTION**.
- Why: I004 already proved response-loss duplicate POST and application-level dedupe. I005 independently checks that conclusion and adds draft-pattern payload fingerprinting plus concurrent same-key processing. The added evidence, not repetition alone, justifies the new study.

---

# SOURCE / SYNTHESIS BOUNDARY

## SOURCE

RFC 9110 defines a method as idempotent when multiple identical requests have the same intended server effect as one request. It identifies PUT, DELETE and safe methods as idempotent, and states that a client should not automatically retry a non-idempotent request unless it knows the request semantics are actually idempotent or can determine the original request was not applied.

The expired HTTPAPI Idempotency-Key draft proposes a client-generated unique key for recognizing retries of the same request, optional payload fingerprinting, replay of a previously completed result, conflict for a concurrent same-key request, and rejection of key reuse with a different payload.

## SYNTHESIS

A transport attempt is not the same thing as a user intent.

For duplicate-sensitive operations, the product may need a durable identity for the **intent** that remains stable across:
- network retry;
- timeout;
- response loss;
- process restart;
- reconnect;
- UI retry activation.

Generating a fresh idempotency identity for every transport attempt defeats that contract.

## STUDIO JUDGMENT

Model at least:

`user intent id → payload/fingerprint → attempt(s) → authoritative operation result`

and separately:

`client knowledge state = pending / confirmed / rejected / outcome unknown`.

A response-loss state must not be rendered as definite failure if the server may already have committed the operation.

---

# Experimental environment

- actual local HTTP/1.1 origin;
- Python `ThreadingHTTPServer`;
- independent `http.client` requests;
- server-side side-effect ledger;
- optional intent-key/fingerprint ledger;
- deliberate connection termination **after side effect commit but before response delivery**;
- concurrent same-key request case.

Final result: **18 / 18 assertions PASS**.

This is protocol/application-behavior practice. It does not prove production gateway, database, queue, payment, mobile or browser behavior.

---

# Scenario A — response lost after commit + naive POST retry

The server commits effect `e1`, then intentionally closes the connection before the client receives a response.

Client knowledge:
- transport result = `RemoteDisconnected`;
- actual server state = `e1` already exists.

The client naively repeats the same POST without a stable intent identity.

Observed:
- second request creates `e2`;
- two distinct effects now exist for one user intention.

### Failure

**Transport failure was incorrectly treated as operation failure.**

### Rule

If the method/action is not safely retryable by semantics, a lost response creates **outcome unknown** until the system can prove or reconcile the authoritative result.

---

# Scenario B — stable intent key across the ambiguous retry

The same failure is repeated, but the user intent receives one stable key before the first attempt.

First request:
- effect `e1` commits;
- response is lost.

Retry:
- same intent key;
- same payload fingerprint;
- server recognizes the completed operation;
- original `e1` result is returned;
- no `e2` is created.

Observed side-effect count: **1**.

### Rule

**Retry attempts may multiply; user intent identity must not.**

For duplicate-sensitive operations, generate/retrieve the idempotency identity at intent creation/queueing, not inside each network-attempt function.

---

# Scenario C — fresh key on retry defeats idempotency

The first attempt commits and loses its response. The retry uses a newly generated key.

Observed:
- first intent-key creates `e1`;
- retry-key creates `e2`;
- duplicate side effect returns.

### Rule

An idempotency key stored only in transient request code is insufficient.

The key belongs with the durable queued/user intent when retry can cross timeout, reconnect or restart boundaries.

---

# Scenario D — same key with a different payload

First request:
- key K;
- amount 100;
- commits `e1`.

Second request:
- same K;
- amount 200.

The harness fingerprint detects different payload semantics and rejects the second request with **422**, following the bounded pattern described in expired draft-07.

No second side effect is created.

### Rule

A key cannot safely mean “whatever request happens to use this string.”

Bind intent identity to the intended operation/payload contract. Reusing one key for materially different intent is an error.

---

# Scenario E — concurrent duplicate before first completion

The first same-key request is deliberately held in processing. A second same-key request arrives before the first completes.

Observed:
- concurrent duplicate receives **409** in this harness;
- original request completes once;
- a later same-key retry returns the completed original result;
- side-effect count remains **1**.

### Rule

`already completed` and `currently processing` are different states.

A retry policy should not turn an in-flight duplicate into a second concurrent execution.

---

# Interaction-state consequences

The following states must remain distinct:

1. **Accepted locally** — intent exists locally.
2. **Queued** — durable but not yet attempted/confirmed.
3. **In flight** — transport attempt active.
4. **Outcome unknown** — transport ended without authoritative knowledge.
5. **Confirmed** — authoritative result known.
6. **Replay confirmed** — retry recovered the already-completed authoritative result.
7. **Concurrent duplicate / still processing** — same intent is already active.
8. **Intent-key misuse / payload mismatch** — identity contract violated.
9. **Rejected operation** — authoritative rejection, distinct from unknown outcome.

Do not map all non-2xx/transport failures to a single `Failed — Retry` state.

---

# Relationship to I002 and I004

I002:
- established the semantic category **outcome unknown**.

I004:
- established `base/current/local` for representation conflicts;
- established durable outbox persistence and conditional replay.

I005 adds a separate axis:

`one user intent ↔ potentially many transport attempts ↔ at most one duplicate-sensitive side effect`.

This means an offline outbox record for such an operation may need both:
- conflict/version context where the target representation can change; and
- a stable operation/idempotency identity where duplicate execution is dangerous.

They solve different failure classes.

---

# Failure modes rejected

- `catch network error → mark failed → create a brand-new POST on Retry`;
- generating a new idempotency key per HTTP attempt;
- clearing durable intent identity after timeout before authoritative resolution;
- assuming a timeout means the server did nothing;
- assuming POST is automatically safe to retry;
- reusing one key with a different payload;
- treating an outstanding same-key request as permission to execute concurrently;
- using a visual “Retry” affordance without defining duplicate-execution semantics;
- equating idempotency with conflict resolution;
- equating idempotency with transaction isolation or exactly-once delivery.

---

# Evidence limits / OPEN

This study does **not** establish:
- a standardized final `Idempotency-Key` RFC; draft-07 is expired work in progress;
- production database atomicity between business side effect and idempotency ledger;
- gateway/proxy/load-balancer retry behavior;
- crash between side effect and key-result persistence;
- distributed multi-region idempotency;
- key expiry/retention policy;
- authentication/account scoping;
- replay security/privacy;
- payment/booking/vendor-specific guarantees;
- production browser/mobile storage;
- background job queues;
- exactly-once message processing;
- AT announcements;
- human understanding.

The hardest production boundary remains **atomicity of business effect + idempotency record**. If those can diverge during a crash, a key ledger alone does not prove exactly-once behavior.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Recovery surfaces may need to show exact operation/object details so users can distinguish “still processing”, “recovered previous result”, and “new action”.
- Long/localized text must not force these states into ambiguous truncation.
- No Type policy is defined here.

### Color
- `outcome unknown`, `processing duplicate`, `confirmed replay`, `rejected`, and `payload mismatch` are distinct semantic roles.
- Color can reinforce them but cannot define them or be the only distinguishing channel.

### Layout / Interaction
- Retry UI is only valid after the operation's duplicate semantics are defined.
- Stable intent identity belongs to the interaction/data lifecycle, not merely networking plumbing.
- “Try again” can mean **recover the same intent**, not **create a new intent**.

### Web Design
- W001 now provides the first Web baseline.
- Future Web transfer should test real `fetch`/AbortController/offline/reload/framework mutation behavior and confirm that one UI intent keeps one stable operation identity across retries.
- Validate page-level messaging for unknown outcome separately from ordinary failure.

---

# Evidence level

**PRACTICE + CRITIQUE / actual HTTP/1.1 connection-loss-after-commit + duplicate side-effect reproduction + stable-intent-key revision + fingerprint/concurrent-duplicate adversarial cases.**

**18 / 18 bounded assertions PASS.**

I005 is **not PASS**. Production atomicity, distributed systems, real browser/mobile stack, AT and app-stage human validation remain open.
