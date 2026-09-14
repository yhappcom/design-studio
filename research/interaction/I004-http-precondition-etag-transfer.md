# I004 Extension — Real HTTP ETag / If-Match Conflict Prevention and Recovery

Status: **PRACTICE + CRITIQUE / REAL HTTP PRECONDITION TRANSFER — lost-update reproduction, 412 protection, disjoint rebase, same-field preservation, and delete-vs-edit new-identity flow established; production backend/offline/multi-device/AT/human validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist — Interaction stream  
Parent study: `research/interaction/I004-concurrent-edits-conflict-merge-recovery.md`

Reproducible artifacts:
- `research/interaction/I004-http-precondition-validation.py`
- `research/interaction/I004-http-precondition-results-summary.json`

## Question

I004's original Chromium specimen proved the user-facing state model for concurrent edits, but the canonical OPEN list still included:

> actual ETag / If-Match service integration.

This extension asks:

1. Can the original lost-update failure be reproduced over an actual HTTP origin-server exchange rather than an in-memory UI state machine?
2. Does strong ETag + `If-Match` prevent the stale mutation from being applied?
3. After a 412, can a semantically safe disjoint merge be rebased against the **current** validator rather than blindly retried?
4. Does the same protocol correctly leave same-field conflict unresolved for human/domain logic?
5. Can delete-vs-edit preserve local work under a **new identity** without silently resurrecting the deleted original?

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T007.
- Reusable finding: a technically successful build does not prove correct runtime behavior; T007 showed skipped/malformed variation can survive file generation.
- Transfer opportunity: I004 similarly distinguishes a technically valid HTTP request from a semantically valid write against the current base state.
- Dependency or overlap: no Type behavior is varied here.

### Color
- Evidence checked: `progress/COLOR_STATUS.md` through C009 and I003 state-semantics transfer.
- Reusable finding: local/remote/conflict/deleted/merged states need semantic distinction independent of hue.
- Transfer opportunity: this HTTP study produces authoritative conflict states for later production rendering.
- Dependency or overlap: no Color conclusion is claimed.

### Layout / Interaction
- Evidence checked: parent I004, I002 async/outcome-unknown, I001 draft/focus continuity, current L006 ownership work.
- Reusable finding: Retry is not conflict resolution; drafts and object identity must survive until semantic resolution.
- Transfer opportunity: replace simulated version checks with actual HTTP validators while keeping the original conflict taxonomy.
- Dependency or overlap: direct I004 implementation transfer, not a new I005 topic.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; no substantive W### evidence exists.
- Reusable finding: production API/router/offline/browser integration remains Web-owned.
- Application opportunity: Web should later reproduce against the real project service and user-facing conflict UI.
- Dependency or overlap: this is a real local HTTP origin server, but not production Web/backend PASS.

### Other / cross-cutting
- RFC 9110, HTTP Semantics, Section 13 conditional requests / `If-Match` / `If-None-Match` / 412:
  https://www.rfc-editor.org/rfc/rfc9110.html#name-preconditions

RFC 9110 explicitly identifies conditional state-changing requests as a mechanism to prevent the **lost update** problem. `If-Match` uses strong comparison, and when its condition is false the origin server must not perform the requested method. `If-None-Match: *` can protect create-only requests from accidentally modifying an existing representation.

### Overlap decision
- **HIGHER-FIDELITY TRANSFER VALIDATION + FAILURE REPRODUCTION**.
- Why: the original I004 semantic model exists. This block validates that the model maps onto a real standards-based HTTP mutation contract.

---

# SOURCE / SYNTHESIS BOUNDARY

## SOURCE

RFC 9110 establishes:

- conditional requests can be used on state-changing methods to prevent lost updates;
- `If-Match` uses strong entity-tag comparison;
- a false `If-Match` condition means the requested method must not be performed; a 412 response can communicate this;
- `If-None-Match: *` can prevent a create request from modifying an already existing representation.

## SYNTHESIS

A 412 is not merely “Save failed.” It means the client's write precondition did not match the authoritative resource state. The correct next step depends on **semantic conflict classification**, not automatic retry.

## STUDIO JUDGMENT

Use the protocol in this order:

`read current representation + validator → edit from known base → conditional mutation → if stale, preserve draft + fetch/receive current state → classify mergeability → resolve/rebase against new validator`

Do not use:

`stale mutation → retry until it wins`

for user-authored state where loss matters.

---

# CONTROLLED HTTP ENVIRONMENT

A real local HTTP/1.1 origin server was implemented with Python `ThreadingHTTPServer`.

Resource representation:

```json
{
  "id": "r1",
  "title": "Flight 101",
  "notes": "Routine",
  "version": 1
}
```

Strong validators are emitted as:

`"r1-v1"`, `"r1-v2"`, ...

Supported controlled methods:

- `GET /records/{id}` → representation + `ETag`;
- `PUT /records/{id}` with optional `If-Match`;
- `DELETE /records/{id}` with optional `If-Match`;
- create-new-identity `PUT` with `If-None-Match: *`.

This is a standards-shaped lab origin server, not a production persistence/database system.

Final matrix: **16 / 16 assertions PASS**.

---

# A. FAILURE REPRODUCTION — NAIVE STALE WHOLE-RECORD PUT

## Sequence

1. Client A GETs r1 v1 → ETag `"r1-v1"`.
2. Client B independently GETs the same v1 / same ETag.
3. A updates title to `Flight 101A` with `If-Match: "r1-v1"`.
4. Server accepts and advances to `"r1-v2"`.
5. B still holds stale title `Flight 101`, changes only notes to `Weather diversion`.
6. B sends a naive whole-record `PUT` **without a precondition**.

Observed authoritative result:

```text
v3
Title: Flight 101
Notes: Weather diversion
```

A's title edit was lost.

### Interaction consequence

The original I004 lost-update failure is not an artifact of the JavaScript specimen. The failure reproduces across a real HTTP mutation boundary whenever a stale whole-record update is accepted blindly.

---

# B. IF-MATCH REJECTS THE STALE WRITE BEFORE MUTATION

The scenario is reset.

A again advances v1 → v2.

B now sends its stale whole-record update with:

`If-Match: "r1-v1"`

Observed:

- response: **412 Precondition Failed**;
- authoritative representation remains v2;
- title remains `Flight 101A`;
- notes remain `Routine`;
- no stale mutation is applied.

The controlled API also returns current `ETag: "r1-v2"` and current representation metadata in the 412 response body. That response-body design is study-specific; RFC 9110 does not require this exact payload.

### Interaction consequence

Preconditions convert a silent data-loss state into a **detectable conflict state**. They do not by themselves decide what the correct merged content should be.

---

# C. DISJOINT MERGE REBASES AGAINST THE CURRENT VALIDATOR

The controlled domain declares `title` and `notes` semantically independent for this scenario.

After B's 412:

1. current authoritative v2 is retained;
2. local notes draft remains `Weather diversion`;
3. merged payload uses current remote title `Flight 101A` + local notes;
4. merged PUT uses **current** `If-Match: "r1-v2"`, not stale v1;
5. server accepts and advances to v3.

Final:

```text
Title: Flight 101A
Notes: Weather diversion
ETag: "r1-v3"
```

### Rule

Even when the system can auto-merge safely, resolution is a **new conditional write against the latest validated base**. Do not remove the conflict and then send an unconditional overwrite.

---

# D. SAME-FIELD CONFLICT — PRECONDITION DETECTS, PRODUCT SEMANTICS DECIDE

Controlled sequence:

- remote title becomes `Flight 101A` on v2;
- stale local draft contains `Flight 101B` from v1;
- stale conditional PUT returns 412.

Observed:

- authoritative state remains `Flight 101A` / v2;
- local client draft `Flight 101B` remains separately preserved;
- no automatic second PUT occurs.

### Rule

`If-Match` can answer:

> “Is this still the state you edited from?”

It cannot answer:

> “Which of two incompatible user intentions should win?”

That remains domain/interaction policy.

---

# E. DELETE VS EDIT — DO NOT RESURRECT THE ORIGINAL IDENTITY

Controlled sequence:

1. stale client holds r1 v1 and unsaved local notes;
2. another writer conditionally deletes r1 using current `If-Match`;
3. stale client attempts PUT r1 with old `If-Match: "r1-v1"`.

Observed:

- stale edit returns **412**;
- r1 remains absent / GET returns 404;
- the stale mutation does not silently recreate r1.

The product then chooses the controlled I004 recovery:

> preserve my changes as a **new object**.

A create-only PUT to `/records/r2` uses:

`If-None-Match: *`

Observed:

- first create succeeds: **201**, r2 version 1;
- a second create attempt against the same r2 with `If-None-Match: *` returns **412**;
- r2's preserved content is not overwritten.

### Interaction consequence

Object identity remains part of conflict semantics. “Keep my work” can mean “create a new object,” not “resurrect or overwrite the deleted original.”

---

# FINAL ASSERTION MATRIX — 16 / 16 PASS

Covered:

- two readers observe the same strong initial ETag;
- current conditional mutation advances the validator;
- naive stale write reproduces lost update;
- stale `If-Match` write returns 412;
- 412 leaves authoritative state unchanged;
- controlled API exposes current validator after conflict;
- disjoint merge rebases against the new validator;
- merged result preserves both independent intentions;
- same-field stale mutation is blocked;
- local conflicting draft remains preserved;
- precondition detection does not choose a winner;
- conditional delete succeeds;
- stale edit after delete cannot resurrect original identity;
- preserved work creates a new identity via `If-None-Match: *`;
- duplicate create is blocked by the same create precondition.

---

# PROJECT-READY CONTRACT

For HTTP-backed collaborative/user-authored resources, define:

1. **validator source** — ETag/version/revision token and whether strong comparison is required;
2. **base state** — which representation the user's draft was derived from;
3. **conditional write policy** — which mutations require a precondition;
4. **412 state** — draft preservation, current-state acquisition and user-facing message;
5. **merge classifier** — no conflict / safe disjoint merge / same-semantic conflict / delete-vs-edit / side effect / ordering conflict;
6. **rebase rule** — any resolved mutation is written against the newest current validator;
7. **identity rule** — when recovery creates a new object instead of modifying the old identity;
8. **retry rule** — retry only after semantics are resolved, not merely because transport can retry;
9. **focus/status lifecycle** — conflict surface, recovery controls and post-resolution destination;
10. **offline/multi-device extension** — how validators and local drafts survive queueing/reconnect.

---

# EVIDENCE LIMITS / OPEN

This extension does not establish:

- database transaction isolation;
- multi-process persistence beyond this in-memory lab server;
- proxies/caches/CDNs or distributed ETag generation;
- production authentication/authorization;
- real offline queue/reconnect;
- actual simultaneous physical devices;
- Firestore/SQL/REST production service behavior;
- CRDT/OT/text/list conflict handling;
- real Web UI integration;
- assistive technology conflict announcements;
- human conflict-resolution comprehension/error rate.

No PASS promotion is justified.

---

# HANDOFFS TO OTHER SPECIALISTS

## Typography / Type
- Conflict UI now has a real protocol state (`412`, current/local versions, validators) suitable for localization/long-value stress.
- Scope limit: no Type decision.

## Color
- `current`, `local draft`, `stale`, `conflict`, `deleted`, `merged` remain different semantic jobs; HTTP status/validator semantics must not collapse to color-only encoding.
- Scope limit: no Color threshold.

## Layout / Interaction
- I004's taxonomy now survives an actual HTTP precondition boundary.
- `Retry` remains distinct from `Resolve + rebase + conditional write`.
- 412 is a conflict-detection event, not a generic failure state.

## Web Design
- Future W### integration can reuse this real HTTP harness to build a production-like conflict UI.
- Test actual fetch/client state, offline storage, service workers, router transitions, focus/status semantics and the project's real backend.
- Scope limit: lab origin server only.

---

# Project-readiness conclusion

The actionable contract is:

> **Prevent stale mutation at the service boundary, preserve the local intention, classify the semantic conflict, then resolve/rebase against the newest authoritative validator.**

That is stronger than either “last write wins” or “show a conflict dialog whenever the version changed.”
