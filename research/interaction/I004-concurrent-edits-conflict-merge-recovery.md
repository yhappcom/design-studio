# I004 — Concurrent Edits, Conflict Detection, Merge, and Recovery

Status: **PRACTICE + CRITIQUE / SOURCE + RUNNING CONFLICT VALIDATION — controlled Chromium evidence established; real service/offline/multi-device/AT/human validation remains OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Canonical path: `research/interaction/`

Reproducible artifacts:

- `research/interaction/I004-conflict-validation-playwright.py`
- `research/interaction/I004-conflict-results-summary.json`

## Question

When two devices/users/processes edit the same object from different base states, how should a product distinguish **safe automatic merge, destructive lost update, same-field semantic conflict, delete-vs-edit conflict, and user-required resolution** while preserving work and avoiding unnecessary conflict dialogs?

I004 extends:

- `research/interaction/015-directness-state-modes-reversibility.md`;
- `research/interaction/I001-navigation-history-focus-restoration-interruption.md`;
- `research/interaction/I002-latency-pending-optimistic-retry.md`.

The central design problem is not “show a conflict modal.” It is deciding **when the system has enough semantic evidence to resolve the conflict safely and when it must preserve multiple intentions for human judgment**.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T005.
- Reusable finding: conflict labels, version values, user/device names, timestamps, and long local/remote values are real semantic text roles that can wrap or reflow.
- Replication / challenge / transfer opportunity: stress conflict-comparison UI with localization, long values, mixed scripts and enlarged text.
- Dependency / overlap: Type owns rendering and text behavior; Interaction owns conflict semantics and recovery.

### Color
- Evidence checked: `progress/COLOR_STATUS.md` through C006; C001/C002/I003 transfer.
- Reusable finding: conflict/current/remote/local/error states cannot depend on hue alone; action/selection/focus/status are distinct semantic roles.
- Replication / challenge / transfer opportunity: later test conflict panels under forced colors and semantic-token substitutions.
- Dependency / overlap: Color owns visual encoding; Interaction owns what “conflict”, “remote”, “local”, “merged”, and “deleted elsewhere” mean.

### Layout / Interaction
- Evidence checked: Studies 015, I001, I002, I003 and current `progress/LAYOUT_STATUS.md`.
- Reusable finding:
  - unsaved work has a lifecycle;
  - ambiguous remote outcome is different from known failure;
  - recovery controls require focus lifecycle;
  - state semantics must exist before styling.
- Replication / challenge / transfer opportunity: extend single-operation async models into multiple concurrent intentions with shared object identity/version.
- Dependency / overlap: primary ownership remains Interaction.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; no substantive `W###` result at study start.
- Reusable finding: Web owns production router/page/service integration, real requests, browser persistence, offline/reconnect and actual multi-device behavior.
- Implementation / application validation opportunity: reproduce I004 against a real API or sync backend using version validators/transactions and production conflict UI.
- Dependency / overlap: current result is a controlled Interaction state machine, not Web/service PASS.

### Other / cross-cutting / future specialist
- Evidence checked:
  - RFC 9110 HTTP conditional requests / `If-Match` and lost-update prevention;
  - Apple `UIDocument` / `NSFileVersion` conflict guidance;
  - Android offline-first conflict-resolution guidance;
  - Firestore transaction/data-contention behavior as one implementation example.
- Reusable finding:
  - version/precondition metadata can prevent blind overwrite;
  - some conflicts can be resolved automatically, while others require preserving multiple versions/intentions;
  - offline reconciliation commonly requires version history/metadata.
- Dependency / overlap: engineering chooses the actual concurrency protocol. Interaction specifies what user-facing states, protections and recovery must exist.

### Overlap decision
- **EXTENSION + INDEPENDENT VALIDATION + FAILURE ANALYSIS + PROJECT-READINESS SYNTHESIS**.
- Why: I002 handled one operation with uncertain outcome; I004 adds multiple legitimate writers and proves why last-write behavior, automatic merge and manual resolution cannot be treated as the same state.

---

# 1. SOURCE — conditional requests exist specifically to prevent lost updates

RFC 9110 defines HTTP conditional requests and states that conditions such as `If-Match` can be applied to state-changing methods to prevent the **lost update** problem, where one client accidentally overwrites another client's parallel work.

Authoritative source:

- https://www.rfc-editor.org/rfc/rfc9110.html#name-preconditions

`If-Match` uses a previously observed validator; if it no longer matches, the server must not blindly perform the method and can return `412 Precondition Failed`.

### SYNTHESIS

A client that saved successfully once is not entitled to overwrite a later remote version merely because its local draft is valid.

The interaction model needs at least:

- base version/validator;
- local draft;
- current authoritative version;
- changed-field/operation intent where available;
- conflict classification;
- resolution policy.

### STUDIO JUDGMENT

A generic “Save failed” message is too weak for a version conflict. The user needs to know whether:

- their work is preserved;
- someone/something else changed the object;
- the system can merge safely;
- a decision is required;
- saving one version will discard another intention.

---

# 2. SOURCE — platform guidance supports automatic resolution when correct, user resolution when not

Apple's current `UIDocument` guidance states that cloud documents can enter a conflict state and that apps should resolve the conflict automatically when they can do so correctly; otherwise they should notify the user and allow resolution among conflicting or merged versions.

Authoritative sources:

- https://developer.apple.com/documentation/uikit/uidocument
- https://developer.apple.com/documentation/foundation/nsfileversion

### SYNTHESIS

Showing every low-level version conflict to users is not a mark of safety. It can externalize implementation complexity unnecessarily.

### STUDIO JUDGMENT

Use this order:

1. **prevent blind overwrite**;
2. **auto-resolve only when the product can establish semantic safety**;
3. **preserve all unresolved intentions**;
4. **ask the user only for the semantic choice the system cannot make**;
5. **make the consequence of each resolution explicit**.

---

# 3. SOURCE — offline conflict resolution requires an explicit policy, not just retry

Current Android offline-first guidance states that local and network state may diverge and need reconciliation when connectivity returns. It notes that conflict resolution often requires versioning/history metadata and that different applications can use different strategies; last-write-wins is described as a common mobile approach, not a universal semantic guarantee.

Source:

- https://developer.android.com/topic/architecture/data-layer/offline-first

Firestore documentation provides one concrete implementation example: transactions track the documents they read and retry when concurrent modification occurs, rather than blindly committing a stale calculation.

Source:

- https://firebase.google.com/docs/firestore/manage-data/transactions

### SYNTHESIS

`Retry` and `conflict resolution` are different operations.

Retry repeats an operation under a known-safe contract. Conflict resolution decides what the operation **should mean after the base state has changed**.

### STUDIO JUDGMENT

Do not automatically retry a stale whole-record write until it succeeds. That can transform a detected conflict into a silent lost update.

---

# 4. Conflict taxonomy for Design Studio

## A. No semantic conflict

The authoritative state has not changed relative to the draft's base version.

Action: save normally.

## B. Disjoint mergeable conflict

Remote and local changes affect independent fields/operations and the domain confirms the changes commute or can be combined without changing meaning.

Potential action: automatic merge, followed by validation against the new authoritative version.

Do not infer safety from different JSON paths alone. Two fields can be semantically coupled.

## C. Same-semantic-field conflict

Both sides changed the same meaningful value or two coupled values.

Potential action: preserve both and request a resolution if no domain-specific merge rule exists.

## D. Delete vs edit

The remote object was deleted while another client still has a draft based on the old identity.

Potential actions depend on product semantics:

- discard local draft;
- restore/recreate with explicit consequence;
- keep local work as a **new identity**;
- escalate if deletion has regulatory/authorization meaning.

Never silently resurrect a deleted object merely because stale data later reconnects.

## E. Side-effect / externally committed conflict

Examples: payments, submitted records, sent messages, finalized approvals.

The correct resolution may be a new compensating action rather than editing history.

## F. Ordering conflict

Both sides reorder/prioritize items. Field-level diffs can look separate while sequence meaning conflicts.

Needs an operation/sequence-aware merge model rather than whole-record LWW.

---

# 5. Controlled running validation

The Chromium specimen simulates:

- one authoritative record with `version`;
- a client draft loaded from a specific base version;
- remote edits/deletion;
- naive whole-record last write;
- version-aware conditional save;
- disjoint field merge;
- same-field conflict UI;
- delete-vs-edit recovery;
- local draft preservation;
- focus restoration after conflict resolution.

This is a state-contract specimen, not a database implementation.

---

# 6. Failure reproduced — naive whole-record save loses another writer's work

Controlled sequence:

1. base v1: title `Flight 101`, notes `Routine`;
2. writer A changes title to `Flight 101A` → authoritative v2;
3. stale writer B still holds v1 and changes notes to `Weather diversion`;
4. naive whole-record save from B writes the stale title plus new notes.

Observed authoritative v3:

- title reverted to `Flight 101`;
- notes became `Weather diversion`.

Writer A's title change is lost.

### REJECTION

Reject blind whole-record last-write behavior for user-authored records when losing another valid edit is materially harmful.

LWW can still be acceptable for some low-value/ephemeral semantics, but the product must justify the loss model.

---

# 7. Re-proof A — disjoint changes can merge without a conflict dialog when semantic independence is established

Controlled version-aware sequence:

1. B edits notes from base v1;
2. A has already changed title on authoritative v2;
3. B's stale save is rejected as a conflict;
4. system compares local changes with remote changes;
5. because the controlled fields are declared independent, the UI exposes automatic merge rather than overwrite choices;
6. merge rebases B's note change on current v2 and commits v3.

Final state:

- title `Flight 101A` preserved;
- notes `Weather diversion` preserved.

The local draft remains visible until resolution; after successful merge, focus returns to a stable Save control.

### Scope limit

This experiment knows that `title` and `notes` are independent. Real products must not auto-merge merely because two paths differ. Domain invariants can couple fields.

---

# 8. Re-proof B — same-field conflict preserves both intentions before writing

Controlled sequence:

- authoritative title changed remotely to `Flight 101A`;
- local stale draft changed title to `Flight 101B`;
- conditional save detects the conflict.

Validated behavior:

- authoritative v2 is not modified;
- local `Flight 101B` remains intact;
- conflict UI exposes both remote and local values;
- conflict region receives focus because the save is blocked by a required decision;
- after explicit `Use my version`, commit occurs against current v2 and becomes v3;
- focus returns to the edited field.

### STUDIO JUDGMENT

Manual conflict resolution should show the **meaningful difference**, not dump raw JSON/version IDs unless those details are actually useful.

The user should know:

- what they changed;
- what changed remotely;
- what will be kept/discarded;
- whether the decision is reversible;
- whether other fields are already merged safely.

---

# 9. Re-proof C — delete vs edit is not a normal overwrite conflict

Controlled sequence:

- remote side deletes the record;
- local stale client has an unsaved note.

Validated behavior:

- deletion is identified explicitly;
- local draft remains preserved;
- system does not silently recreate the deleted original;
- `Keep my changes as a new record` creates a separate identity `r2` while original `r1` remains deleted;
- focus returns to the retained draft context.

### STUDIO JUDGMENT

Object identity is part of conflict semantics.

“Keep my work” does not always mean “overwrite or resurrect the same object.”

This is especially important when deletion has business, security, retention or workflow meaning.

---

# 10. Final controlled result

Playwright assertions: **17/17 PASS**.

Covered:

- naive lost-update reproduction;
- stale-save conflict detection;
- local draft preservation;
- disjoint merge path;
- remote+local preservation after merge;
- post-merge focus restoration;
- same-field no-auto-write;
- both-version visibility;
- blocking conflict focus;
- explicit resolution commit;
- post-resolution focus;
- delete-vs-edit classification;
- keep-copy path with separate identity.

Evidence level: **PRACTICE + CRITIQUE / controlled Chromium state-machine evidence**.

---

# 11. Project decision framework

Before choosing a conflict strategy, ask:

1. What is the conflict unit — whole record, field, list operation, text range, transaction, external side effect?
2. Is there a reliable base version/validator?
3. Can two edits commute semantically?
4. Can the system prove a merge is safe?
5. How valuable is each side's unsaved work?
6. Does deletion/finalization change object identity or legal/workflow state?
7. Can a losing version be recovered later?
8. Is the user online, offline, interrupted or on another device?
9. Is another user/device identity meaningful to resolution?
10. Does the user need to resolve now, or can the conflict be deferred safely?

## Strategy options

### Automatic merge
Use when domain semantics establish that changes can coexist safely.

### Last write wins
Use only when losing the older value is an accepted product rule and ordering metadata is trustworthy enough for that purpose.

### Manual choose/merge
Use when both intentions are valid but incompatible and the user understands the semantic distinction better than the system.

### Preserve as new object/version
Use when work must be saved but overwriting/resurrecting the original identity would be wrong.

### Compensating action
Use when an external effect is already committed and history should not be rewritten.

---

# 12. Failure modes

Reject designs that:

- overwrite stale data silently;
- call every conflict a generic network error;
- auto-retry stale writes until they win;
- discard the local draft before resolution;
- ask users to resolve conflicts the system can deterministically merge;
- auto-merge semantically coupled fields merely because JSON paths differ;
- silently resurrect remotely deleted items;
- show only timestamps when timestamps do not explain the semantic difference;
- hide which version will be discarded;
- move focus to disappearing conflict controls without a restoration contract;
- use color alone to distinguish local/remote/conflict state.

---

# 13. Evidence classification

## SOURCE

- RFC 9110: conditional preconditions can prevent lost updates.
- Apple document/version APIs: conflicts exist as version states; resolve automatically when correct, otherwise preserve/expose versions for user choice.
- Android offline-first: offline divergence requires conflict resolution/versioning policy; LWW is one strategy, not a universal product truth.
- Firestore: concurrent transactional changes can trigger retry rather than blindly applying stale calculations.

## SYNTHESIS

Conflict UX depends on **semantic mergeability**, not simply technical concurrency.

## STUDIO JUDGMENT

Use the least burdensome strategy that preserves all materially valid intentions and domain invariants.

## OPEN

- actual ETag/If-Match service integration;
- Firestore/backend transaction transfer;
- offline queue/reconnect with multiple devices;
- text/list/ordering CRDT or OT behavior;
- richer field coupling and validation invariants;
- authorization/ownership conflicts;
- long-running conflict deferral;
- screen reader/AT conflict-announcement behavior;
- localization and long-value comparison UI;
- real user conflict comprehension/error rate;
- production Web/mobile implementation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: conflict-resolution surfaces need to compare local/remote values, user/device/version metadata, and preserve drafts under long content.
- Canonical section: I004 Sections 8–11.
- Confirmation / contradiction / transfer note: supplies realistic localization/enlargement stress cases where wrapping can alter comparison clarity.
- Scope limit: Interaction does not define font/fallback strategy.

### Color
- Useful finding/context: local/remote/conflict/deleted/merged are distinct semantic states; color must not be their sole difference.
- Canonical section: I004 taxonomy and failure modes.
- Confirmation / contradiction / transfer note: extends I003/C002 — semantic state exists before visual token assignment.
- Scope limit: no palette/contrast result is claimed.

### Layout / Interaction
- Useful finding/context: preserve draft + base/current version + semantic change scope; auto-merge only when domain independence is established; same-field/delete conflicts require different recovery paths.
- Canonical section: I004 Sections 4–11.
- Confirmation / contradiction / transfer note: extends I001/I002 from one user's async lifecycle to multiple concurrent intentions.
- Scope limit: distributed-system algorithm correctness remains engineering evidence.

### Web Design
- Useful finding/context: reusable conflict-state matrix and 17-assertion controlled specimen.
- Web application / validation consequence: reproduce with real API validators/transactions, offline/reconnect, multiple tabs/devices, framework forms, router interruption, and AT.
- Confirmation / contradiction / transfer note: return which conflict classes the production data model can safely auto-merge versus which need user resolution.
- Scope limit: current specimen is local Chromium simulation, not service integration.
