# CD012 — Empty, Loading, Pending, Success, and Recovery Content System

Status: **STAGE 2 PRACTICE — LIFECYCLE SYSTEM + COMPARATIVE PRACTICE / NOT PASSED**  
Date: 2026-09-16

## Question

How should an English-first global product distinguish and connect empty, loading, pending, success, and recovery language across a task lifecycle without collapsing product truth, over-messaging routine states, or creating localization/runtime defects?

CD011 classified failure/warning states by cause, certainty, agency and recovery. CD012 extends that model to non-error lifecycle states.

## RELATED DOMAIN CHECK

### Type
Checked `progress/TYPE_STATUS.md`. Necessary state strings remain operational content and must not be shortened merely to compensate for weak glyphs, wrapping or one-line geometry. Literal identifiers and numerics remain especially sensitive.

### Color
Checked `progress/COLOR_STATUS.md`. Color may reinforce loading, success, unavailable and recovery states, but state identity must survive color removal/transformation. CD012 therefore defines semantic propositions before visual severity/status roles.

### Layout / Interaction
Direct reuse of `research/interaction/I002-latency-pending-optimistic-retry.md`: accepted, pending, progressing, confirmed, failed, canceled and outcome-unknown are distinct behavioral states. Interaction owns whether work is actually pending, cancellable, retryable or complete. Content does not invent those facts.

### Web
Checked `progress/WEB_STATUS.md`, especially W018. W018 independently transferred first-frame, data-visible and task-ready distinctions into Chromium and showed that reserved geometry can reduce async displacement. It also confirms that `pending` and `ready` are runtime-distinct. Web remains responsible for actual browser focus/status/announcement/reflow/network transfer.

### Content
CD001–CD009 Foundation contracts, CD010 forms and CD011 state taxonomy are reused. CD012 is an **EXTENSION + TRANSFER VALIDATION PREPARATION** study, not another summary of generic microcopy advice.

### External authoritative evidence checked
- W3C WCAG 2.1/2.2 status-message guidance: dynamic status can be programmatically conveyed without moving focus.
- Apple `ContentUnavailableView` / `UIContentUnavailableConfiguration`: unavailable content can represent empty, loading, search-no-results and network-related states; label, description and actions are separate composable roles.
- Apple Progress Indicators / Loading guidance: progress indicators are transient and distinguish determinate from indeterminate work; useful content should appear as soon as practical and other work may continue when feasible.
- Microsoft Writing Style guidance: lead with important information and emphasize useful action; localization/accessibility are writing constraints.

These sources support state separation and communication structure. They do **not** prove that any exact CD012 wording is best for users.

Overlap classification: **EXTENSION + PEER TRANSFER + PRODUCTION-TRANSFER PREPARATION**.

---

## 1. Lifecycle model: absence, preparation, commitment, confirmation, recovery

### SYNTHESIS

The useful top-level distinction is not visual component type (`empty view`, `spinner`, `toast`) but product truth:

1. **Empty / absence** — there is currently no content matching the surface's scope.
2. **Loading / preparation** — content or capability is being obtained/prepared; no user commitment is implied.
3. **Pending / unconfirmed commitment** — the product accepted an intent but authoritative completion is not yet known.
4. **Success / confirmed result** — authoritative completion is known.
5. **Recovery** — the current state requires or benefits from an available next action after a block, failure, conflict or interruption.

### STUDIO JUDGMENT

A visual component may be shared across these states, but a semantic key must not be shared merely because English strings look similar.

`Loading records…` and `Saving record…` are not interchangeable: the first describes retrieval/preparation; the second can describe an unconfirmed commitment with duplicate/retry consequences.

---

## 2. Empty is a family of causes, not one message

### STUDIO MODEL

Classify empty surfaces before writing:

| Empty class | Product truth | Content job | Candidate action |
|---|---|---|---|
| first-use empty | user has not created/imported content yet | explain what belongs here and how to begin | create/import when available |
| user-cleared empty | content was intentionally removed/cleared | confirm current absence only if useful | create/restore if supported |
| filter empty | data exists outside current filter | identify active constraint | clear/change filter |
| search no-results | query returned no match | name query/result relationship | revise/clear search |
| permission empty | content may exist but is inaccessible | explain access boundary | request access / switch scope |
| unavailable/offline | content cannot currently be obtained | state availability problem, not absence | reconnect/use cached data |
| truly complete/zero state | zero is the meaningful result | present zero as information, not an error | often none |

### CONTRADICTION

`No records yet` is false or misleading for filter-empty, permission-empty and unavailable states. A generic empty component can therefore conceal materially different causes.

### Comparative practice

Fixed surface: flight records list.

- First use: `No flight records yet` + `Add a flight or import records to start your logbook.`
- Filter empty: `No flights match these filters` + action to change/clear filters.
- Search no-results: `No flights found for “KE123”` + revise/clear search.
- Offline/unavailable: do **not** say `No flights`; state that records cannot currently be loaded if that is the truth.

Exact LogMate actions remain project dependencies rather than assumed product facts.

---

## 3. Loading describes preparation; pending describes commitment

### SOURCE / PEER TRANSFER

Apple distinguishes determinate and indeterminate progress and treats progress indicators as transient representations of ongoing operations. Interaction I002 separately distinguishes local acceptance, pending, progressing and confirmed states.

### SYNTHESIS

Content must answer different questions:

- Loading: **What is being prepared or retrieved?**
- Pending: **What user intent has been accepted but is not yet confirmed?**

### STUDIO JUDGMENT

Prefer object/action-specific status when the delay is material enough to communicate:
- `Loading flight records…`
- `Importing 128 records…` when count/progress is authoritative.
- `Saving record…` only when the save is actually pending.

Do not fabricate percent complete or `Almost done` from elapsed time alone.

Do not turn every brief background fetch into prose. Content presence should be proportional to task blockage, duration, consequence and need for status.

---

## 4. Progressive readiness requires semantic milestones

### TRANSFER VALIDATION

W018 measured first frame, data visibility and task readiness as distinct milestones in a deterministic Chromium specimen. CD012 transfers that finding into a content requirement:

> Do not label a surface `Ready`, `Loaded`, or equivalent merely because something rendered.

If partial content is visible while controls or authoritative data are still unavailable, language and affordances must match the actual readiness level.

### STUDIO JUDGMENT

Possible content states include:
- shell visible, no status text needed;
- `Loading records…` while records are unavailable;
- partial/cached content with explicit freshness status when materially relevant;
- `Syncing changes…` for unconfirmed synchronization;
- ready state with no celebratory announcement when readiness is self-evident.

`Ready` is not a default success message. It is a claim about capability.

---

## 5. Success is confirmation, not celebration

### SYNTHESIS

Success content should communicate a result only when the result is not already sufficiently evident or when confirmation materially reduces uncertainty.

### STUDIO JUDGMENT — success ladder

1. **Self-evident state change** — often no additional success copy.
2. **Brief confirmation** — `Record saved.` when commitment certainty matters.
3. **Confirmation + consequence** — explain what changed when non-obvious.
4. **Confirmation + next action** — only when a legitimate next task exists.
5. **High-salience completion** — reserve stronger treatment for meaningful milestones, not routine saves.

### REJECT

- `Success!` without naming what succeeded;
- celebratory language for routine background operations;
- success before authoritative confirmation when the contract is pessimistic/pending;
- success copy that hides a partial result.

---

## 6. Recovery content is an action contract

Recovery is not synonymous with `Try again`.

### STUDIO MODEL

Recovery may be:
- edit/correct;
- clear/change scope;
- resume;
- reconnect;
- verify authoritative state;
- reconcile conflict;
- request access;
- choose an alternative;
- undo;
- safely retry;
- contact support/escalate when no self-service path exists.

### DEPENDENCY

Interaction/product logic must provide the real recovery set. Content can prioritize and name available recovery but cannot manufacture it.

### Critical rule

If the product cannot establish whether a consequential action committed, recovery must follow CD011/I002 outcome-unknown rules: verify/reconcile before exposing a potentially duplicative retry.

---

## 7. State-message architecture v0.2

Extend CD011's state contract with lifecycle fields:

- `state_class`
- `scope_or_object`
- `cause_if_known_and_useful`
- `known_fact`
- `readiness_level`
- `commitment_certainty`
- `progress_basis` (`none`, `indeterminate`, `determinate`, `stage`)
- `freshness_or_cache_state` when material
- `user_agency`
- `primary_recovery_or_next_action`
- `secondary_recovery`
- `retry_safety`
- `dismissal_meaning`
- `persistence_duration`
- `announcement_priority`
- `localizer_context`
- `variables_and_plural_requirements`

### STUDIO JUDGMENT

The content system should encode semantics as metadata rather than infer them from English copy. `empty.search`, `empty.filter`, `empty.first_use`, `pending.save`, and `success.save` should remain distinguishable even if some locales eventually produce superficially similar strings.

---

## 8. English-first global/localization constraints

### SOURCE-ENGLISH RULES

- Write complete semantic propositions before optimizing brevity.
- Keep the object/action explicit where the message may appear outside immediate context.
- Avoid idiomatic waiting language (`Hang tight`, `Just a sec`) as the only status explanation.
- Avoid English grammar as logic: do not concatenate `No` + noun, verb stems + tense fragments, or adjective status tokens into sentences.
- Treat counts with locale-aware plural/message formatting; do not assume English singular/plural morphology transfers.
- Keep query/filter values as variables with localizer context, not embedded English punctuation assumptions.
- Do not promise time (`This will only take a moment`) unless the product has evidence/contract for that promise.
- Distinguish `loading`, `pending`, `syncing`, `offline`, `stale`, `failed`, and `unknown outcome` in semantic keys.

### TRANSFER VALIDATION PLAN

Later production/localization work should test at least:
- long expansion and narrow widths;
- plural/count behavior;
- variable reordering;
- RTL/bidirectional identifiers where relevant;
- date/number/unit formatting;
- translator context completeness;
- string-key state integrity across native/web surfaces.

Korean is not a Foundation or Stage 2 blocker; it can be one later transfer locale when a product/market need justifies it.

---

## 9. Accessibility/runtime boundary

### SOURCE

WCAG status-message guidance establishes that important dynamic status can be programmatically determined and presented by assistive technology without necessarily receiving focus.

### SYNTHESIS

Visible wording, announcement behavior and focus movement are separate design decisions.

### DEPENDENCY

Content supplies the message and intended priority; Web/native implementation owns actual live-region/status semantics, focus behavior, persistence and timing. CD012 does not claim screen-reader behavior from static copy.

Routine loading/success should not automatically steal focus. A recovery UI that requires interaction may need a different structural/focus treatment from a passive status message.

---

## 10. Comparative system practice — one records surface through six states

Fixed domain object: flight records. Exact backend semantics remain hypothetical practice, not LogMate production truth.

### A — first use
`No flight records yet.`  
Purpose: true absence. Action only if create/import is actually available.

### B — loading existing records
`Loading flight records…`  
Purpose: retrieval/preparation, not absence.

### C — filter returns zero
`No flights match these filters.`  
Purpose: scoped zero; recovery changes scope.

### D — save pending
`Saving record…`  
Purpose: accepted intent, unconfirmed commitment. No duplicate action unless contract permits.

### E — save confirmed
`Record saved.`  
Purpose: authoritative confirmation; no extra celebration.

### F — save outcome unknown
`We couldn’t confirm whether the record was saved.`  
Purpose: uncertainty; verify/reconcile before retry.

### CONTRADICTION TEST

A component system with only `loading / empty / error / success` cannot faithfully represent C, D and F. The content architecture therefore requires semantic state classes richer than common visual variant names.

---

## 11. Audit v0.2

Flag:
- `EMPTY_CAUSE_COLLAPSE`
- `FALSE_ABSENCE`
- `LOADING_PENDING_COLLAPSE`
- `FALSE_READINESS`
- `FALSE_PROGRESS_PRECISION`
- `UNSUPPORTED_TIME_PROMISE`
- `PREMATURE_SUCCESS`
- `SUCCESS_WITHOUT_OBJECT`
- `RECOVERY_WITHOUT_REAL_ACTION`
- `UNSAFE_RETRY`
- `STALE_DATA_UNDISCLOSED_WHEN_MATERIAL`
- `ENGLISH_GRAMMAR_AS_LOGIC`
- `FRAGMENTED_LOCALIZATION_MESSAGE`
- `MISSING_LOCALIZER_STATE_CONTEXT`
- `STATUS_FOCUS_COUPLING_UNVERIFIED`
- `HUMAN_VALIDATION_NEEDED`
- `RUNTIME_TRANSFER_NEEDED`

This audit detects semantic/content-system defects. It does not establish human comprehension, perceived speed, trust, preference or task performance.

---

## 12. KEEP / REWORK / REJECT

### KEEP
- lifecycle taxonomy based on product truth rather than visual component;
- empty-state cause taxonomy;
- loading vs pending separation;
- progressive-readiness distinction;
- proportional success ladder;
- recovery as an Interaction-backed action contract;
- semantic keys/metadata independent of English surface form.

### REWORK
- exact stale/cached/offline language using real product data architecture;
- persistence and announcement priority by platform;
- multi-device sync/conflict lifecycle once LogMate state semantics are available;
- production localization schema and message-format implementation.

### REJECT
- `No data` as universal empty copy;
- `Something went wrong` as universal recovery state;
- `Success!` as universal completion;
- `Almost done` without evidence;
- treating spinner visibility as proof of pending commitment;
- one `empty/error/loading/success` enum when product truth requires more states.

---

## Stage 2 implication

CD012 closes the largest immediate gap after CD011: empty/loading/pending/success/recovery are now one lifecycle system rather than isolated microcopy patterns. Stage 2 remains **PRACTICE / NOT PASSED**. Onboarding/progressive disclosure, search/filter/settings as broader task systems, voice/tone, repeated localization-ready transfer, and an integrated Stage 2 capstone remain incomplete.

## OPEN

- real LogMate/MintTap data freshness, sync, offline and recovery contracts;
- actual native/web status persistence and announcement behavior;
- production localization message format and translator workflow;
- human comprehension, recovery success, perceived latency and trust evidence;
- telemetry linking state class to abandonment/retry/recovery outcomes.

## HANDOFFS TO OTHER SPECIALISTS

### Interaction
CD012 preserves I002's loading/pending/confirmed/outcome-unknown boundaries. Future sync/offline content needs exact product state-machine truth.

### Web
Use CD012 lifecycle classes as semantic inputs for browser transfer. Test actual status announcements, focus preservation, stale/cached states, responsive string fit and real network ambiguity independently.

### Type
Use empty/recovery/pending strings, counts and literal identifiers as operational wrapping/fallback stress. Do not shorten required semantics to hide Type defects.

### Color
Map visual state only after lifecycle class is known. Empty, loading, pending and success must remain distinguishable without color-only meaning.

## Evidence level

**AUTHORITATIVE-SOURCE CHECK + PEER-EVIDENCE TRANSFER + SYSTEM SYNTHESIS + COMPARATIVE PRACTICE + CONTRADICTION TEST + TRANSFER-VALIDATION PLAN. No human, screen-reader, production localization, or live-project PASS claimed.**
