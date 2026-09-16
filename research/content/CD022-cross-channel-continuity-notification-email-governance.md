# CD022 — Cross-Channel Continuity, Notification/Email Semantics, and Message Governance

Status: **STAGE 3 PRACTICE — SYSTEM TRANSFER / NOT PASSED**  
Date: 2026-09-16

## Question
How should one authoritative product event remain semantically coherent when represented in-app, in a notification, in email, in activity/history, and later in localized implementations—without forcing literal copy sameness or allowing channels to invent stronger certainty, urgency, scope, or recovery than the product state supports?

This extends CD020 semantic architecture and CD021 structured inventory into cross-channel systems. It is not a marketing-email study and does not claim delivery/runtime evidence.

## RELATED DOMAIN CHECK

### Type
T021 closed the unsupported whole-family bespoke route and T022 now studies mature product typography roles. Content therefore preserves literal identifiers, time/duration and operational strings as typed data; channel compression must not rewrite them merely to fit a typographic preference.

### Color
C022 exact pair audit confirms bounded visual state pairs while preserving semantic collisions such as outcome-unknown ≠ warning and known failure ≠ destructive action. Cross-channel Content treats color as reinforcement only; notification/email text must remain meaningful without app palette context.

### Layout / Interaction
L013/I008 establish cross-surface invariants: viewport/surface changes cannot mutate certainty or safe action; outcome-unknown blocks blind retry; recovery restores object + task + certainty context. CD022 deliberately transfers those invariants from viewport recomposition into channel recomposition.

### Web
W021 is now an executable integrated specimen but actual browser execution remains open. It already provides the future in-app/runtime transfer surface for CD021-style expansion/bidi/status. CD022 does not relabel that static/executable artifact as browser evidence.

### Content
CD020 defines stable concepts/state schema. CD021 defines stable message IDs, typed variables and localization stress. CD022 adds channel policy, provenance, governance and change-propagation rules rather than repeating message drafting.

---

## 1. Channel is a projection of product truth, not a new source of truth

### SYNTHESIS

An event should be modeled before any channel copy exists:

`authoritative event/state → semantic message contract → channel eligibility → channel projection → locale realization → rendered/delivered surface`

A push notification, email subject, in-app banner and activity row are not four independent writing opportunities. They are projections with different interruption cost, persistence, available context and action affordances.

### STUDIO RULE

**A channel may omit recoverable context when the destination restores it; it may not strengthen certainty, consequence, urgency or available action.**

Examples:
- in-app `We couldn’t confirm whether the record was saved.` must not become push `Save failed`;
- an offline-local save must not become email `Your record is safely backed up` unless remote backup is actually confirmed;
- a conflict notification must not expose `Replace` if the product requires comparison/reconciliation first.

---

## 2. Channel eligibility precedes channel wording

Before drafting, ask:

- Is this event worth interrupting the user for?
- Does the user need to know outside the app?
- Is the event still actionable when delivered later?
- Can stale delivery create a false state impression?
- Is sensitive content safe on lock screen/email preview?
- Does the channel have a reliable deep destination?
- Is there a preference/permission/policy governing delivery?
- Is there a lower-interruption surface that satisfies the need?

### STUDIO JUDGMENT

Notification design begins with **whether to notify**, not how to phrase the notification.

Routine success should normally remain in-app/history unless a real asynchronous completion or operational dependency justifies external interruption. This is a system policy hypothesis, not a measured user-preference claim.

---

## 3. Cross-channel semantic invariants

For one message family, these fields are invariant unless the underlying event changes:

- `concept_id`
- `event_id` or event class
- `object_type`
- `certainty`
- `persistence_scope`
- `consequence_class`
- `safe_action_set`
- `recovery_class`
- `literal_identifier_policy`
- `sensitivity_class`

These may vary by channel:

- information order;
- detail depth;
- explicit object repetition;
- timestamp prominence;
- destination label;
- subject/title/body decomposition;
- visible recovery detail when destination restores context;
- bounded tone compression.

### CONTRADICTION

Literal copy sameness can be less consistent than semantic adaptation. A toast may rely on visible object context; a push preview cannot. Conversely, copying a verbose in-app recovery paragraph into a push can obscure the one fact required before opening the app.

---

## 4. Channel contract v0.1

Each externally projected message should declare:

- `message_family_id`
- `source_event`
- `source_state`
- `channel`
- `eligibility_rule`
- `suppression_rule`
- `freshness_limit`
- `sensitivity_class`
- `preview_policy`
- `title_intent`
- `body_intent`
- `primary_destination`
- `destination_context_required`
- `allowed_actions`
- `certainty_invariant`
- `scope_invariant`
- `recovery_invariant`
- `typed_variables`
- `localizer_context`
- `accessibility_intent`
- `analytics_question`
- `owner`
- `change_dependency`

The contract separates delivery policy from prose and makes stale/unsafe projections auditable.

---

## 5. Freshness and stale-message semantics

### SYNTHESIS

External channels are temporally dangerous because delivery may lag behind product truth.

A notification generated at state S1 can arrive after the object has reached S2. Therefore a message family needs a freshness policy:

- `snapshot-valid` — the message truth remains historically true even after state changes;
- `current-state-sensitive` — message should be suppressed/replaced if state advances;
- `action-expiring` — action/destination must verify current state before execution;
- `historical-record` — activity/history intentionally reports past state with timestamp.

### Example

`Record needs review` may become stale if reconciliation completes on another device before push delivery. Opening the push should resolve current state, not recreate the old action blindly.

### HANDOFF DEPENDENCY

Interaction/backend owns actual deduplication, freshness and action authorization. Content can specify the semantic risk but cannot implement it.

---

## 6. Notification compression hierarchy

When space/attention is constrained, preserve in this order:

1. state/certainty that changes interpretation;
2. affected object/scope;
3. material consequence;
4. valid next action or destination;
5. supporting explanation;
6. personality.

This extends CD015's functional priority into cross-channel compression.

### REJECT

- dropping `couldn’t confirm` to fit a push;
- replacing specific object identity with generic `Something` where multiple records may exist;
- using urgency words to increase opens;
- using `Retry` as a universal notification action;
- embedding all explanation in a truncated preview.

---

## 7. Email is not merely a long notification

### STUDIO JUDGMENT

Transactional email can support more persistent context, but persistence creates its own risks:

- email may outlive current state;
- forwarded content may expose sensitive data;
- subject lines appear without body context;
- reply behavior may imply support/interaction that does not exist;
- deep links may expire or resolve differently across devices;
- locale/timezone formatting must be explicit;
- legal/operational retention may differ from in-app history.

Therefore email requires a separate projection contract while retaining the same semantic family.

Subject should identify object/event sufficiently for inbox context without claiming more than body/source state.

---

## 8. Activity/history as semantic evidence

Activity/history is not a dumping ground for toast text. It may serve as a durable account of events.

If a history entry represents an event rather than current state, it should preserve:

- what happened;
- object;
- event time;
- actor/source when materially relevant;
- historical certainty at that time;
- later resolution link if the product supports it.

### CONTRADICTION

`Save not confirmed` stored forever with no later resolution can imply unresolved current state even after reconciliation. Historical UI may need event/result linkage rather than isolated strings.

---

## 9. Governance: message IDs are APIs

### SYNTHESIS

Once messages are referenced by application code, analytics, localization catalogs, notifications and tests, message identifiers behave like interface contracts.

A mature change process therefore distinguishes:

- copy-only revision with unchanged semantics;
- locale-only realization revision;
- semantic contract revision;
- state-machine revision;
- variable-schema revision;
- channel-policy revision;
- deprecation/replacement.

### STUDIO RULE

**Do not silently reuse an old message ID for a materially different state or consequence.**

This prevents analytics, translations, tests and downstream channels from inheriting false equivalence.

---

## 10. Change propagation graph

A semantic change may affect:

`domain concept → state/action contract → message family → in-app surfaces → notification/email/history projections → localization context → accessibility status → analytics event interpretation → QA assertions → documentation/support`

Content governance should record dependency edges rather than rely on writers remembering every occurrence.

### Example

If `saved locally` changes to mean `queued for sync` rather than durable device persistence, this is not a copy tweak. It may require Interaction contract review, lifecycle message changes, notification suppression changes, settings/help changes, translator-context revision and analytics reinterpretation.

---

## 11. Ownership model

Suggested system roles, not organization chart mandates:

- **product/Interaction owner** — authoritative state/action/consequence;
- **Content owner** — concept/message family/semantic wording contract;
- **localization owner/process** — locale realization, terminology and linguistic QA;
- **engineering owner** — message invocation, variable typing, fallback/delivery;
- **channel owner** — eligibility/freshness/privacy/destination behavior where separate;
- **QA** — contract and rendered-state verification;
- **research/human factors** — comprehension/trust/task-performance evidence where required.

A RACI spreadsheet alone does not solve governance. Each semantic family needs an identifiable authoritative owner and change path.

---

## 12. Versioning and deprecation

For high-impact message families, record:

- current semantic version/revision;
- introduced date/version;
- superseded IDs;
- reason for semantic change;
- affected states/channels/locales;
- migration requirement;
- compatibility/fallback rule;
- verification evidence.

Version numbers need not be user-visible. The purpose is traceability.

### REJECT

- deleting a key immediately because English copy changed;
- reusing deprecated key names with new meaning;
- leaving old notification templates active after state semantics change;
- changing variable type from literal identifier to localized number without migration review.

---

## 13. Localization governance

Cross-channel localization requires more than one English source string per message family.

Localizer context should include:

- source state and certainty;
- object/domain definition;
- channel/surface;
- character/preview constraints if real;
- variable types and examples;
- literal identifier rules;
- consequence/recovery intent;
- tone bounds;
- screenshot/reference when available;
- related terms that must remain consistent.

### OPEN

Actual translation-memory/terminology tooling, ICU/message-format implementation, screenshot automation, vendor workflow and locale linguistic QA remain Stage 3/4 production-transfer work.

---

## 14. Privacy and preview boundary

### STUDIO JUDGMENT

External surfaces can reveal content when the app is not foregrounded. Therefore the semantic contract needs a sensitivity class independent of wording.

Possible policy classes:
- public-safe;
- contextual/private;
- sensitive — generic preview only;
- prohibited from external preview.

Exact classifications are product/privacy dependencies, not Content-only decisions.

A generic privacy-safe preview must still avoid false semantics. `Action needed` may be acceptable only if opening reliably reveals the actual current action; `Your flight has an error` is not acceptable if the underlying state is merely unconfirmed sync.

---

## 15. Cross-channel audit flags

- `CHANNEL_INVENTS_CERTAINTY`
- `CHANNEL_INVENTS_URGENCY`
- `CHANNEL_INVENTS_ACTION`
- `CHANNEL_LOSES_OBJECT_SCOPE`
- `STALE_EXTERNAL_STATE`
- `STALE_ACTION_EXECUTION`
- `ROUTINE_SUCCESS_INTERRUPTION`
- `PREVIEW_SENSITIVITY_LEAK`
- `SUBJECT_BODY_SEMANTIC_DRIFT`
- `HISTORY_CURRENT_STATE_CONFUSION`
- `MESSAGE_ID_SEMANTIC_REUSE`
- `UNTYPED_CHANNEL_VARIABLE`
- `LOCALIZER_CONTEXT_MISSING`
- `DEPRECATED_TEMPLATE_STILL_ACTIVE`
- `ANALYTICS_MEANING_DRIFT`
- `RECOVERY_DESTINATION_UNVERIFIED`
- `HUMAN_VALIDATION_NEEDED`
- `RUNTIME_DELIVERY_VALIDATION_NEEDED`

---

## 16. Reproducible non-human assertions

For a message-family fixture, a structural audit can assert:

1. every channel variant references one source semantic family;
2. certainty is equal across variants unless source event differs;
3. allowed actions are a subset of authoritative safe actions;
4. external variants declare freshness and sensitivity policies;
5. every variable has a type;
6. professional identifiers are marked literal where required;
7. deprecated IDs are not active invocation targets;
8. channel variants include localizer context;
9. current-state-sensitive messages have a destination revalidation dependency;
10. no notification is generated solely because a copy string exists.

These are architecture checks, not human comprehension evidence.

---

## 17. KEEP / REWORK / REJECT

### KEEP
- one semantic family, multiple channel projections;
- channel eligibility before wording;
- certainty/scope/recovery invariance;
- freshness and sensitivity as first-class metadata;
- typed variables and literal identifiers;
- message IDs treated as governed interfaces;
- explicit change-propagation graph;
- deprecation rather than semantic key recycling.

### REWORK
- exact notification/email eligibility for live MintTap/LogMate;
- privacy classifications;
- production localization tooling;
- notification delivery and stale-state reconciliation;
- analytics taxonomy;
- channel-specific AT behavior;
- human interruption/comprehension/trust evidence.

### REJECT
- independent copy truth per channel;
- push/email as marketingized versions of operational state;
- stronger urgency/certainty for engagement;
- exact same sentence forced across every surface;
- message-key reuse after semantic meaning changes;
- notification actions that bypass current-state verification.

---

## Stage 3 implication

CD022 extends the Stage 3 architecture from product-wide concept/message structure into **cross-channel continuity and governance**. It provides a reproducible policy model for channel eligibility, freshness, sensitivity, semantic invariants, ownership, versioning and change propagation.

Stage 3 remains **PRACTICE / NOT PASSED**. Major evidence gaps now concentrate around executable cross-channel/message-format transfer, production localization workflow, runtime delivery/fallback/accessibility behavior, and a later integrated Stage 3 system capstone/closure audit.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
I008's certainty/safe-action invariants transfer directly to notification/email/history. Interaction/backend must own freshness, stale-action revalidation and actual recovery authorization.

### Web
W021 can later consume `message_family_id`, channel/source-state metadata and verify in-app projection. Browser execution must not be inferred from this document.

### Color
External channels may not carry product palette. State wording therefore remains independently sufficient; C022 aliases are reinforcement, not the cross-channel state source.

### Type
Channel compression must preserve literal identifiers and state qualifiers. T022 can use notification/history strings as additional role-system stress material after exact role needs are established.

## Evidence level

**SYSTEM SYNTHESIS + CROSS-DOMAIN TRANSFER + CONTRADICTION TESTING + GOVERNANCE MODEL + REPRODUCIBLE STRUCTURAL ASSERTIONS. No notification/email delivery, production localization, AT, human interruption/comprehension, or live-project PASS claimed.**