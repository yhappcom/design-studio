# W006 — Complete Task Surfaces: State, Validation, Recovery, and Data-View Contracts

Status: **PRACTICE / CRITIQUE — FOUNDATION INTEGRATION / TRANSFER VALIDATION**  
Owner: Web Design Specialist  
Canonical path: `research/web/`

## Question

How should a Web specialist design complete task surfaces — forms, search/filter, settings, tables, dashboards and list/detail views — so that the page remains understandable and recoverable across initial, loading, empty, partial, validation, pending, error, retry, outcome-unknown and confirmed states?

The objective is not a pattern catalogue. The objective is a project-ready method for deciding **what the page is currently claiming, what remains usable, what the user can safely do next, and which state owns the recovery path**.

## RELATED DOMAIN CHECK

### Type
Checked `progress/TYPE_STATUS.md` through T016. T016 establishes that preferred-loaded, fallback-visible and preferred-failed typography can produce materially different geometry. W006 therefore treats long labels, validation text, status text, table cells and recovery actions as variable-content geometry. Exact production-font transfer remains OPEN.

### Color
Checked `progress/COLOR_STATUS.md` through C015 Stage 1 PASS. Color may reinforce validation, warning, pending and success, but cannot be the sole carrier of state. W006 keeps state semantics in text/structure/action before Color assignment.

### Layout / Interaction
Checked `progress/LAYOUT_STATUS.md` and `research/interaction/I002-latency-pending-optimistic-retry.md`. I002's accepted/pending/progress/confirmed/failed/canceled/outcome-unknown distinctions are canonical Interaction evidence. W006 is **TRANSFER VALIDATION + WEB-SPECIFIC INTEGRATION**: it places those distinctions inside complete Web task surfaces rather than redefining them. I004/I005 conflict/idempotency evidence remains relevant to consequential retries.

### Web
Checked W001–W005. W002 supplies page-composition stress; W003 relationship ownership; W004 resource/direct-entry model; W005 semantic primitive and independent-state model. W006 integrates them into end-to-end task surfaces.

### Overlap decision
**TRANSFER VALIDATION + INTEGRATION.** Repetition is deliberate because isolated Interaction state semantics are insufficient evidence that a complete Web page preserves hierarchy, unaffected work, resource identity, validation and recovery simultaneously.

---

## SOURCE

Current WHATWG HTML establishes native form submission and constraint-validation behavior. A disabled form control is barred from constraint validation; disabled controls prevent user-interaction click dispatch, and implicit form submission can activate the default submit button when applicable. This means native form behavior is part of the Web design contract, not an implementation afterthought.

Current W3C WAI Forms guidance recommends clear required-field identification, useful input validation, understandable error feedback, and overall submission feedback. It distinguishes inline feedback from overall task feedback and recommends telling users whether submission succeeded or errors occurred.

Authoritative sources checked 2026-09-15:
- WHATWG HTML — forms, form-control infrastructure and button behavior: https://html.spec.whatwg.org/
- W3C WAI Forms Tutorial — Validating Input: https://www.w3.org/WAI/tutorials/forms/validation/
- W3C WAI Forms Tutorial — User Notification: https://www.w3.org/WAI/tutorials/forms/notifications/

Reading these sources does not establish browser/AT PASS.

---

# 1. Complete-surface model

## SYNTHESIS

A task surface should be modeled as:

`resource/task identity`
`→ current authoritative or cached content`
`→ user intent/input`
`→ validation state`
`→ operation state`
`→ result/data-view state`
`→ recovery/continuation action`
`→ navigation/history consequence`

These dimensions should not be flattened into one page enum such as `loading | error | success`.

A realistic page can be simultaneously:
- showing confirmed existing data;
- filtering locally;
- refreshing one region;
- validating an edited field;
- holding another save operation in pending state;
- showing a recoverable error in a secondary panel.

## STUDIO JUDGMENT

Prefer **state ownership at the smallest truthful task boundary**. A local refresh should not blank an otherwise valid page. A form-field error should not convert the entire route into an error page. Conversely, a route whose resource cannot be authorized or resolved should not masquerade as a local widget error.

---

# 2. Data-view states are semantically different

For tables, lists, dashboards and search results, distinguish at minimum:

| State | Meaning | Default design consequence |
| --- | --- | --- |
| Initial unresolved | no usable result known yet | communicate acquisition without pretending emptiness |
| Loading with prior content | known content exists, refresh unresolved | preserve useful content when safe; mark freshness/work state |
| Empty valid result | query/resource resolved to zero items | explain zero state and relevant next action |
| Filtered zero result | data may exist, current criteria yield none | preserve filter context; offer criterion recovery, not onboarding copy |
| Partial result | some content valid, completeness unresolved/limited | identify incompleteness and affected scope |
| Stale/offline cached | content exists but freshness cannot be confirmed | preserve provenance/freshness and actions that are actually safe |
| Failed acquisition | requested result not obtained | retain query/context; recovery should not erase user work |
| Unauthorized/not found | resource-level access/identity failure | route-level treatment; do not present as generic empty state |

### Failure mode

`[]` is not sufficient product semantics. It can represent a genuinely empty account, a filter with no matches, a failed request accidentally normalized to empty, or an unauthorized resource hidden by the backend. These require different explanations and next actions.

---

# 3. Form and settings contract

A consequential form should preserve these separations:

1. **Instruction** — what valid completion requires.
2. **Input** — current editable value.
3. **Local validity** — format/range/required constraints known locally.
4. **Remote/business validity** — uniqueness, authorization, workflow or server rule that may only be known remotely.
5. **Accepted intent** — user activated submission and local preconditions passed.
6. **Pending** — authoritative result not yet confirmed.
7. **Confirmed** — authoritative success known.
8. **Failed with known non-commit** — safe correction/retry path can be offered.
9. **Outcome unknown** — transport/UI does not know whether the side effect committed; do not label this as ordinary failure or blindly duplicate the action.

## STUDIO JUDGMENT

Do not disable the submit action merely to hide incomplete validation if discoverability of requirements is important. Native `disabled`, discoverable unavailable, validation-on-submit and progressive validation are different choices. W005 owns the primitive distinction; W006 chooses among them according to task risk and correction cost.

When errors exist:
- preserve entered values unless there is a security/privacy reason not to;
- identify the field/task problem specifically;
- provide overall feedback when submission as a whole failed;
- move or restore attention deliberately when the error is outside the current viewport/context;
- do not rely on red borders alone.

---

# 4. Search and filter contract

Search/filter surfaces have two identities:

`criteria state` and `result state`.

Criteria that users need to share, bookmark, reload or traverse should be evaluated under W004's addressability/history model rather than kept transient by default.

Three viable strategies:

### A. Immediate query
Best when requests are cheap, reversible, results update quickly and every criterion change is meaningful.

KEEP when continuous comparison is the task.  
REWORK when request cost or result churn causes instability.  
REJECT when changes trigger consequential side effects.

### B. Explicit Apply
Best when several criteria form one meaningful query, requests are expensive, or users need to stage changes before recomputation.

KEEP when staged criteria are understandable.  
REWORK if users cannot tell applied from unapplied values.  
REJECT when it adds needless confirmation to a trivial local filter.

### C. Hybrid
Immediate local refinements plus explicit remote/expensive query boundaries.

KEEP when the boundary maps to a real task/data distinction.  
REJECT when it merely reflects implementation architecture users cannot understand.

### Invariant
A zero-result response must retain enough visible criteria context to explain *why* the result is zero and how to recover.

---

# 5. Tables, dashboards and list/detail

## SYNTHESIS

Dense data surfaces are not one giant component. Separate:
- query/filter ownership;
- summary/KPI ownership;
- collection ownership;
- selection ownership;
- detail ownership;
- mutation ownership;
- freshness/sync ownership.

This allows partial failure without destroying unrelated valid work.

### STUDIO JUDGMENT

For a dashboard with six panels, `Promise.all → one full-page error` is usually a poor design contract unless all six results are genuinely atomic for the task. Prefer truthful region-level failure when independent regions remain useful, while still exposing page-level status if the combined interpretation is incomplete.

For list/detail, preserve selection identity independently from visual position. Resorting/filtering must not silently make a different item appear selected merely because it occupies the same row index.

For tables, preserve tabular relationships when simultaneous row/column comparison is the task; local horizontal overflow can be preferable to destructive stacking. This reuses W002 rather than asserting that every table must fit without horizontal movement.

---

# 6. Pending, retry and outcome-unknown transfer

## TRANSFER VALIDATION from I002/I004/I005

Web surfaces must distinguish:

`intent accepted → request/operation pending → authoritative confirmation`

from:

`intent accepted → transport ambiguity → outcome unknown`.

### Known failure
If the server definitively rejects before commit, correction/retry can be framed as failure recovery.

### Outcome unknown
If the response is lost after the server may have committed, the UI must not claim "Save failed" as a fact. Recovery should first use operation identity/current authoritative state when the product/API supports it.

### STUDIO JUDGMENT

A retry button is not merely a visual component. Its safety is a contract involving operation semantics, stable intent identity and backend guarantees. Web Design should expose only recovery actions whose semantics are defensible.

---

# 7. Three complete-surface directions

Consider a portfolio holdings workspace with search/filter, table, edit drawer and refresh.

## Direction A — Global blocking transaction surface
- one page-level loading state;
- edits block the page until confirmation;
- any fetch failure becomes full-page error.

**KEEP** only where the entire page is truly one atomic, short, high-consequence transaction.  
**REWORK** when read-only context remains useful during a mutation.  
**REJECT** for independent dashboard/list regions because it destroys valid context.

## Direction B — Region-owned progressive workspace
- confirmed content remains visible;
- refresh/pending/error owned by affected region;
- edit state remains attached to the selected resource;
- filter/query state remains visible and recoverable.

**KEEP** for most data workspaces where tasks continue around local latency.  
**REWORK** if cross-region values must be interpreted atomically.  
**REJECT** if partial data could create a dangerous false whole.

## Direction C — Snapshot-first offline-tolerant workspace
- last-confirmed snapshot is primary;
- freshness/provenance is explicit;
- local edits may queue under Interaction's durable-intent contract;
- unavailable remote-only actions remain distinct from queued-safe actions.

**KEEP** where intermittent connectivity is a product requirement.  
**REWORK** when users cannot judge stale-data consequence.  
**REJECT** for operations that legally/operationally require immediate authoritative confirmation.

### Preferred Foundation default
**Direction B**, unless product requirements establish atomicity or offline-first constraints. It preserves truthful state ownership without forcing advanced synchronization architecture onto every project.

---

# 8. Project-readiness checklist

Before recommending a task surface, answer:

- What is the stable resource/task identity?
- Which content is authoritative, cached, partial or stale?
- What can remain usable while one operation is pending?
- Which state belongs to the route, region, control or operation?
- Is zero data genuinely empty, filtered-zero, unauthorized, or failed acquisition?
- Which validation is local vs remote/business validation?
- Can the operation be safely retried? What proves that?
- What does direct entry/reload/back-forward do to criteria and selection?
- Which criteria belong in the URL?
- What happens to user input after validation/server/network failure?
- How are success/error/status changes communicated without color alone?
- Does long Korean/English status/recovery text break geometry?
- Does the table/list preserve comparison and selection identity under reflow/filter/sort?
- What is the narrowest truthful loading/error boundary?

---

## OPEN

- Browser specimen combining search/filter/table/edit and local/global state ownership.
- Native constraint-validation vs custom error-summary behavior under keyboard and browser UI.
- `aria-live`/status-message and screen-reader transfer; no AT PASS claimed.
- Actual browser zoom and long bilingual validation/recovery text.
- Forced-colors transfer for validation/pending/error/selection.
- W004 history/direct-entry integration for query/filter state.
- Real fetch abort/offline/response-loss harness and I005 stable-intent transfer.
- Firefox/Safari/physical mobile.
- Complete real-project exercise and human task validation at app/project stage.

## Evidence level

**SOURCE + SYNTHESIS + PRACTICE / CRITIQUE + TRANSFER VALIDATION.** This study establishes a complete-surface decision model and materially different design directions. It does not claim browser, assistive-technology, production API or human PASS.

## HANDOFFS TO OTHER SPECIALISTS

### Type
W006 makes status/error/recovery copy part of live page geometry. Future Type→Web transfer should include long bilingual validation and outcome-unknown text, not only steady-state labels.

### Color
W006 supplies concrete page-level semantics — empty, filtered-zero, stale, partial, pending, known failure, outcome unknown, confirmed — for Color to reinforce without collapsing distinctions or relying on hue alone.

### Layout / Interaction
W006 confirms the usefulness of I002/I004/I005 distinctions in complete Web surfaces. It does not change their canonical semantics. A future browser harness should test whether region-owned state and recovery preserve focus, context and safe retry behavior.
