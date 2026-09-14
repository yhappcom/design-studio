# I004 / I002 Extension — Ambiguous Outcome, Idempotent Retry, and Duplicate-Delivery Protection

Status: **PRACTICE + CRITIQUE / REAL HTTP AMBIGUOUS-RESULT TRANSFER — applied-but-response-lost failure, own-success 412 ambiguity, duplicate POST reproduction, and application-level dedupe established; production API/database/payment/idempotency infrastructure remains OPEN**

Owner: Layout, Spatial & Interaction Specialist — Interaction stream  
Parents:
- `research/interaction/I002-latency-pending-optimistic-retry.md`
- `research/interaction/I004-concurrent-edits-conflict-merge-recovery.md`
- `research/interaction/I004-http-precondition-etag-transfer.md`
- `research/interaction/I004-offline-outbox-reconnect-transfer.md`

Reproducible artifacts:
- `research/interaction/I004-ambiguous-outcome-idempotency-validation.py`
- `research/interaction/I004-ambiguous-outcome-idempotency-results.json`

## Question

What should an offline/queued client do when the server **applied a state-changing request but the response was lost**?

This is neither a known failure nor a normal version conflict. The client has incomplete knowledge:

`request sent → server may have applied → connection closes before response → client cannot know outcome from transport alone`.

The study asks whether an idempotent PUT can confirm already-achieved state, whether stale If-Match can misclassify the client's own prior success, whether blind POST retry duplicates side effects, and whether an application operation identity can make the intended POST semantics idempotent.

## RELATED DOMAIN CHECK

### Typography / Type
- No new Type mechanism is tested.
- Recovery/status copy must distinguish `outcome unknown`, `confirmed`, and `conflict` precisely; localization must preserve those distinctions.

### Color
- I003/C001/C011 remain relevant: `outcome unknown`, `failure`, `conflict`, and `confirmed` are different semantic states and cannot be encoded by color alone.

### Layout / Interaction
- I002 already established `outcome unknown ≠ failure` and that Retry requires an operation/data contract.
- I004 established version conflicts and durable offline outboxes.
- This extension links them: after an ambiguous result, a queued retry can confirm prior success, create a duplicate side effect, or misclassify the situation as conflict depending on operation semantics.

### Web Design
- No W### evidence exists yet.
- Future production transfer should validate fetch/network-abort behavior, framework retry middleware, service-worker queues, proxy/CDN/API-gateway behavior and UI status.

### Other / standards
- RFC 9110 §9.2.2 defines PUT, DELETE and safe methods as idempotent and explains that idempotent requests can be retried after communication failure before the response is read.
- RFC 9110 says clients should not automatically retry non-idempotent methods unless they know request semantics are actually idempotent or can determine the original request was not applied.
- The IETF HTTPAPI `Idempotency-Key` draft is not treated as a current standard here; the listed draft expired in 2025. The lab uses application-specific `X-Operation-Id` only to model a product/API deduplication contract.

Sources:
- https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2
- https://datatracker.ietf.org/group/httpapi/documents/

### Overlap decision
- **I002↔I004 CROSS-TRANSFER + FAILURE REPRODUCTION**.

---

# Controlled failure environment

Real HTTP/1.1 local origin. The server deliberately receives a request, applies mutation/side effect, then closes the TCP connection **without sending a response**.

The client observes `RemoteDisconnected` and classifies the transport result as `outcome_unknown`. Server state is inspected separately.

Final matrix: **15 / 15 assertions PASS**.

# Scenario 1 — conditional PUT succeeded, response lost, retry becomes 412

Initial record: r1 v1, ETag `"r1-v1"`.

Client sends desired notes `Weather diversion` with `PUT If-Match: "r1-v1"`. Server applies it to v2 and closes before any response. Client knows only `outcome_unknown`.

A later GET proves the first PUT succeeded. However, naïve retry with the original validator receives **412**, because current ETag is now `"r1-v2"`.

### Finding

A 412 after an ambiguous result does **not automatically prove another actor caused a conflict**. It can mean the client's own first request succeeded, changed the validator, and only its response was lost.

### Product consequence

Do not show manual conflict UI merely because an ambiguous-result retry receives 412. First determine whether the intended state/operation may already have been achieved.

# Scenario 2 — idempotent PUT confirmation without duplicate effect

A revised endpoint, when the old `If-Match` fails, checks whether the current representation already equals the requested desired representation.

Sequence:
1. first PUT applies v1→v2;
2. response is lost;
3. retry carries old validator;
4. server sees mismatch but also sees requested state is already current;
5. returns 200 with outcome `already-applied`;
6. record remains v2 rather than creating another mutation/version.

### Rule

Where the product/server can reliably establish **the same intended effect is already present**, an ambiguous result can be converted from `unknown` to `confirmed` without a new side effect.

This is not a universal ETag rule; domain evidence is required.

# Scenario 3 — blind retry of non-idempotent POST duplicates side effect

Lab side effect: create a transfer.

First POST creates `t1` and loses its response. Client sees `outcome_unknown`. Blind retry creates `t2`.

Observed count: `1 → 2`.

### Rule

**Unknown is not permission to repeat a non-idempotent side effect.**

Payments, sends, submissions, bookings and approvals need an API/product retry contract rather than generic network-error retry.

# Scenario 4 — application operation identity prevents duplicate POST

Lab contract uses `X-Operation-Id: transfer-op-123`; this is intentionally **not claimed as a standardized HTTP field**.

Server contract:
- first unseen operation ID + payload applies the effect and records the result;
- same operation ID + same payload returns the original result without reapplying;
- same operation ID + different payload is rejected.

Controlled result:
1. first keyed POST creates `t1` and response is lost;
2. retry sends same operation identity/payload;
3. server returns original `t1` with `replayed` outcome;
4. transfer count remains 1;
5. same ID with different amount is rejected with 409.

### Rule

An operation identity identifies **one semantic intent**, not a reusable retry token for arbitrary payloads. Persist it with the durable outbox until authoritative outcome is known.

---

# Updated I002/I004 state model

After a state-changing request leaves the client, distinguish:
1. **not sent**;
2. **sending**;
3. **known rejected / failed before application**;
4. **outcome unknown** — transport did not establish whether application occurred;
5. **confirmed applied**;
6. **confirmed already applied / replayed result**;
7. **actual external conflict**;
8. **duplicate-prevention mismatch** — operation identity reused inconsistently.

Do not collapse 3, 4 and 7 into one generic “Save failed”.

# Retry decision contract

Before automatic retry, ask:
- Is the HTTP method idempotent for this intended effect?
- Is the API implementation compatible with that intended idempotency?
- Is the operation conditional on a validator the first request may itself have changed?
- Can server/client determine whether desired effect is already present?
- For non-idempotent action, is there a durable semantic operation identity/deduplication contract?
- Is that identity bound to the exact intent/payload?
- Could the first request have triggered an external side effect that cannot simply be inspected or rolled back?

# Failure modes rejected

- displaying `failed` immediately when response connection drops after request transmission;
- automatically replaying every queued POST after reconnect;
- interpreting every 412 after an ambiguous result as another user's conflict;
- generating a fresh operation ID on each retry of the same semantic intent;
- accepting the same operation ID with a different payload;
- clearing an outbox item before outcome confirmation;
- retry middleware that ignores endpoint/method/domain semantics;
- relying on UI disablement to prevent network-level duplicate delivery.

# Evidence limits / OPEN

Not established:
- production reverse proxies/API gateways/load balancers;
- database transaction + dedupe-ledger atomicity;
- crashes between side-effect commit and dedupe-record commit;
- payment-provider/booking/message external APIs;
- distributed multi-region replication;
- operation-ID retention/expiry policy;
- retry storms/backoff/rate limits;
- service-worker/background-sync retries;
- actual app local-database integration;
- security/authorization replay rules;
- user-facing comprehension/AT behavior.

## HANDOFFS TO OTHER SPECIALISTS

### Color
- `outcome unknown`, `actual failure`, `actual conflict`, `confirmed`, and `already applied` are distinct semantic states. Do not collapse them into one status color.

### Typography / Type
- “Failed”, “Not yet confirmed”, and “Changed elsewhere” are not interchangeable strings. Localization must preserve the distinction.

### Layout / Interaction
- Retry policy belongs to the operation contract, not a generic button/network layer.
- Persist semantic operation identity with queued intent when non-idempotent retry safety depends on it.
- A 412 after outcome-unknown needs own-success detection before conflict escalation.

### Web Design
- Audit production fetch/client libraries for automatic retries.
- Test response loss after server application, not only connection failure before request send.
- Verify operation IDs survive reload/offline queues and are not regenerated per retry.

# Evidence level

**PRACTICE + CRITIQUE / real HTTP applied-then-response-lost failure + idempotent PUT confirmation + duplicate POST reproduction + application-level dedupe re-proof.**

No production PASS.
