# I004 Extension — Offline Authorization Change, Finalization, Account Switch, and Compensating Recovery

Status: **PRACTICE + CRITIQUE / REAL HTTP POLICY-STATE TRANSFER — permission revocation, finalization, reauthorization+stale revalidation, actor-bound outbox, and compensating amendment recovery established; production auth/workflow/backend validation remains OPEN**

Owner: Layout, Spatial & Interaction Specialist — Interaction stream

Parents:
- `I004-concurrent-edits-conflict-merge-recovery.md`
- `I004-http-precondition-etag-transfer.md`
- `I004-offline-outbox-reconnect-transfer.md`
- `I004-ambiguous-outcome-idempotency-transfer.md`
- `I004-multi-operation-queue-semantics.md`

Reproducible artifacts:
- `research/interaction/I004-offline-authorization-finalization-validation.py`
- `research/interaction/I004-offline-authorization-finalization-results.json`

## Question

A queued offline mutation can become invalid even when its data intent is still internally coherent.

This study asks what should happen when, before reconnect:

- the actor loses permission;
- the record becomes finalized/locked;
- permission later returns but authoritative data has changed;
- the app switches accounts while another account's intent remains in the outbox.

These are not ordinary same-field conflicts.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Latest Type status checked through T015.
- Actor names, status explanations, local drafts and recovery instructions are semantic text; exact content identity must survive localization/normalization.
- No Type policy is claimed.

### Color
- Latest Color status checked through C014.
- `permission blocked`, `finalized`, `stale`, `account mismatch`, `conflict`, and `recovered as amendment` are distinct states; Color cannot be their sole channel.

### Layout / Interaction
- I001 continuity/restoration, I002 async outcome states, and all I004 extensions checked.
- This study adds policy/workflow state as dimensions separate from representation version.

### Web Design
- W001 is available.
- Future Web transfer should reproduce account-switch/logout, router/remount, local-store partitioning and real auth middleware behavior.

### Other / standards
Source checked:
- RFC 9110 HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110.html

Relevant facts:
- 403 means the server understood a request but refuses to fulfill it.
- RFC 9110 says HTTP preconditions are evaluated **after normal request checks succeed**; failures detectable before significant request processing take precedence over conditional evaluation.
- `If-Match` prevents stale mutation but does not define authorization or domain workflow policy.

The lab uses 409 for `record_finalized`. That is an **application API choice**, not claimed as the universal HTTP status for finalization.

### Overlap decision
**I004 EXTENSION + POLICY-STATE FAILURE REPRODUCTION + RECOVERY PRACTICE**.

---

# Controlled environment

- real local HTTP/1.1 origin;
- per-request lab actor identity (`X-Actor`);
- mutable server authorization state;
- mutable record workflow state;
- strong ETags;
- durable SQLite outbox containing the actor who created the intent.

Final result: **18 / 18 assertions PASS**.

---

# 1. Permission revoked while offline

Client A reads r1 at v1, then queues an offline note edit.

While A is offline, edit permission is revoked. The record representation itself remains v1, so the queued ETag would still match.

On reconnect:

- server returns **403** from the normal authorization check;
- the method is not applied;
- the original record remains unchanged;
- local payload remains durable;
- queue moves to `blocked_permission`.

## Finding

**A matching ETag does not imply permission to mutate.**

Version validity and authorization validity are orthogonal.

## Rejected behavior

Do not label this as:
- generic network failure;
- version conflict;
- safe-to-retry-until-success.

---

# 2. Record finalized while offline

A queues a correction from draft v1.

While offline, the server finalizes the record and increments its version.

The lab API checks finalization as a normal domain request check and returns:

- `409`
- reason `record_finalized`
- recovery hint `create_amendment`

This occurs before stale `If-Match` evaluation in the lab.

The original finalized record is not modified.

Recovery then uses an explicit **new amendment object** referencing the finalized record.

Final result:
- original remains finalized and unchanged;
- local work is preserved as amendment `a1`;
- queue moves to `recovered_as_amendment`.

## Finding

**Finalization can change the legal/workflow meaning of mutation, not only the current field values.**

For some domains the correct recovery is a new compensating/append-only action, not overwrite or resurrection.

---

# 3. Permission restored does not erase stale-data risk

A's queued write is first blocked by permission loss.

Later:
- permission is restored;
- another actor B has changed the record.

Blindly replaying A's original v1 validator now receives **412**.

Revised flow:

`permission restored → retry original precondition → stale detected → fetch current → semantic compare → disjoint rebase → conditional write against current validator`

Final record preserved:
- B's remote title;
- A's offline note.

## Finding

Authorization recovery and concurrency recovery are separate steps.

**“You may edit again” does not mean “your old write is safe to apply unchanged.”**

---

# 4. Account switch can replay the wrong person's intent

A queues a private offline draft.

Before sync, active account changes to B.

## Naive behavior reproduced

The drainer ignores the queued actor and simply uses the current B credential.

Because B also has edit permission, the server accepts the mutation. A's offline intent is applied under B's active authorization context.

This is technically valid HTTP but wrong product ownership.

## Revised behavior

The durable outbox stores `actor=A`.

Before any network mutation:

`queued_actor != active_actor`

therefore queue becomes:

`blocked_account_mismatch`

No request is sent and the server remains unchanged.

## Rule

**Semantic operation identity includes actor/account ownership when that identity matters to authorization, privacy, audit, attribution, or user expectation.**

A queue must not silently inherit whichever credential happens to be active when background sync wakes up.

---

# Updated validity model

A queued mutation can be replayable only if relevant dimensions still hold:

`intent payload`
`object identity`
`historical base/version`
`current authoritative state`
`operation identity`
`actor/account identity`
`current authorization`
`workflow mutability/finalization`
`dependencies`
`external side-effect state`

These dimensions should not be collapsed into one `sync error`.

---

# Suggested states

Add, where product semantics require:

- `blocked_permission`
- `blocked_account_mismatch`
- `blocked_finalized`
- `reauthorization_required`
- `stale_after_reauthorization`
- `recovered_as_amendment`
- `discarded_by_policy`

These exist alongside:
- queued;
- network pending;
- outcome unknown;
- conflict;
- confirmed;
- blocked dependency;
- deleted remotely;
- already applied.

---

# Failure modes rejected

- treating 403 as retryable network failure;
- treating finalization as an ordinary version conflict only;
- force-saving a finalized object because the user authored the edit earlier;
- replaying queued work with whichever account is currently active;
- erasing the queued actor identity on logout/account switch;
- assuming restored permission makes an old base current;
- discarding local work merely because the original mutation is no longer legal;
- mutating finalized history where the domain requires amendment/compensation;
- using one generic red “sync error” for authorization, finalization, version conflict, and account mismatch.

---

# Evidence limits / OPEN

Not established:
- OAuth/session refresh/token expiry;
- production RBAC/ABAC policy engines;
- server-side audit and attribution;
- multi-tenant account partitioning;
- encryption/key destruction on logout;
- finalized regulatory records;
- payments/approvals/booking side effects;
- real auth middleware/proxies;
- atomic authorization+transaction checks in a production DB;
- offline policy snapshots;
- admin override/escalation workflows;
- production mobile/web local-store partitioning;
- AT/user comprehension.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Status copy must distinguish permission loss, finalization, stale data, and account mismatch.
- Local drafts may require exact preserved text when recovery moves work into an amendment/new record.

### Color
- Authorization and workflow blocks are semantic states separate from ordinary conflict/error.
- Do not encode these distinctions by hue alone.

### Layout / Interaction
- Add **actor identity / authorization validity / workflow mutability** to queued-operation validity checks.
- A valid historical edit can become an invalid future mutation without becoming meaningless work.
- Recovery can change the operation type: edit → amendment / compensating action.

### Web Design
- Test production logout/account switch with IndexedDB/localStorage/Cache/service-worker queues.
- Verify queued work is correctly partitioned, blocked, migrated or deleted according to product security policy.
- Validate real router/remount/auth refresh and focus/status behavior.

---

# Evidence level

**PRACTICE + CRITIQUE / real HTTP authorization + workflow-state + durable actor-bound outbox transfer.**

No production PASS.
