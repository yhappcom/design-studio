# I002 — Latency, Pending State, Optimistic UI, Retry, and Outcome Uncertainty

Status: **FOUNDATION STUDY / PROJECT-DECISION FRAMEWORK — running failure/retry specimen and real network/platform validation still required before PASS.**

Owner: Layout, Spatial & Interaction Specialist  
Canonical path: `research/interaction/`

## Question

How should a product communicate and recover from latency so that users can distinguish **accepted, pending, progressing, confirmed, failed, canceled, and outcome-unknown** operations without using spinners, optimistic updates, timeouts, or retries as generic visual tricks?

This study extends:

- `research/interaction/007-interaction-agency-feedback-errors.md`;
- `research/interaction/015-directness-state-modes-reversibility.md`;
- `research/interaction/I001-navigation-history-focus-restoration-interruption.md`.

The project objective is practical: for any slow or asynchronous action, Design Studio should be able to recommend whether to update immediately, show pending state, show determinate/indeterminate progress, allow cancellation, retry automatically, require explicit recovery, or first verify whether the original operation actually committed.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `progress/TYPE_STATUS.md` through T004;
  - existing Type findings on hierarchy, compact labels, status/action text, fallback and reflow.
- Reusable finding:
  - status, progress, error and recovery labels must survive fallback, localization and enlargement;
  - small compact labels are not typographically neutral.
- Replication / challenge / transfer opportunity:
  - later test pending/error/retry labels under long Korean/Latin localization and fallback.
- Dependency / overlap:
  - Type owns typographic structure; Interaction owns what the state means and when it should be communicated.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md` through C003;
  - C001 forced-color resilience and C002 semantic role architecture.
- Reusable finding:
  - pending/error/success meaning must not depend on literal color;
  - interaction state should be semantically defined before Color assigns visual roles.
- Replication / challenge / transfer opportunity:
  - test pending/unknown/failure/retry states under forced colors and theme substitution.
- Dependency / overlap:
  - Color reinforces state; Interaction defines state semantics and recovery.

### Layout / Interaction
- Evidence checked:
  - Studies 007, 015, I001 and the I001 running validation report;
  - `progress/LAYOUT_STATUS.md`.
- Reusable finding:
  - optimistic local state, pending remote state and confirmed commitment are different states;
  - status communication and recovery action should not be collapsed;
  - data lifecycle determines reversibility and navigation policy.
- Replication / challenge / transfer opportunity:
  - I002 extends the existing commitment model into latency, timeout, ambiguous outcome and duplicate-submission control.
- Dependency / overlap:
  - direct extension of Interaction canonical evidence.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web owns complete browser/network/page-system application and should later validate real fetch/router/native-control behavior.
- Implementation/application validation opportunity:
  - actual request aborts, offline/online transitions, browser resubmission, duplicate activation, real status announcements and network retries.
- Dependency / overlap:
  - no substantive W### study was available at I002 start; this study defines the Interaction-side contract, not Web implementation proof.

### Other / cross-cutting / future specialist
- Evidence checked:
  - Shneiderman 1984 response-time review;
  - Myers 1985 progress-indicator study;
  - Harrison et al. 2007 progress-bar perception study;
  - Apple current Loading / Progress Indicators / Feedback guidance;
  - WCAG 2.2 status-message guidance and WAI-ARIA status/progress/busy semantics;
  - RFC 9110 HTTP idempotency semantics.
- Reusable finding:
  - delay perception and acceptable feedback depend on task/context;
  - progress should communicate real process state;
  - retry safety depends on operation semantics, not merely on whether the UI still shows a button.
- Dependency / overlap:
  - performance engineering and API semantics are implementation domains, but their contracts materially constrain Interaction recovery.

### Overlap decision
- **EXTENSION + METHOD COMPARISON + PROJECT-READINESS SYNTHESIS + TRANSFER PREPARATION**.
- Why:
  - Study 015 identified pending/confirmed as separate states but did not yet provide a complete latency/retry decision model. I002 closes that project-readiness gap without pretending that one timing threshold fits all products.

---

# 1. SOURCE — response time is task-dependent, not one universal threshold

Shneiderman's 1984 review of response time and display rate summarizes experimental work showing that response time affects productivity, expectations, error rate, command patterns and user attitudes. The review reports that frequent users often prefer sub-second response for many tasks, but also emphasizes task differences and notes that both very slow and very fast pacing can affect errors.

Primary source:

- Shneiderman B. *Response Time and Display Rate in Human Performance with Computers*. ACM Computing Surveys. 1984;16(3):265–285. DOI: 10.1145/2514.2517
- https://www.cs.umd.edu/~ben/papers/Shneiderman1984Response.pdf

### SYNTHESIS

Do not turn classic response-time literature into a universal `100 ms / 1 s / 10 s` product law.

Useful transfer:

> The amount and type of feedback should depend on the task, user expectation, consequence, variability and whether the operation blocks further work.

### STUDIO JUDGMENT

Before choosing a loading treatment, classify:

- frequency of the action;
- whether it is direct manipulation, navigation, submission, background sync, export, payment, upload, search, or computation;
- whether the user can safely continue doing other work;
- whether duration is predictable;
- whether the result is reversible;
- whether completion has external side effects.

---

# 2. SOURCE — progress indicators can materially improve waiting interaction

Myers' CHI 1985 work examined percent-done progress indicators and reported practical/experimental evidence that they improve the interface experience for tasks that require waiting.

Primary source:

- Myers BA. *The Importance of Percent-Done Progress Indicators for Computer-Human Interfaces*. CHI 1985. DOI: 10.1145/317456.317459

Apple's current Progress Indicators guidance distinguishes:

- determinate progress when progress/duration can be meaningfully quantified;
- indeterminate activity when it cannot.

It also recommends accurate advancement, moving indicators, switching from indeterminate to determinate when reliable information becomes available, and supporting cancellation when interruption is safe.

Source:

- https://developer.apple.com/design/human-interface-guidelines/progress-indicators

### SYNTHESIS

Progress UI is evidence about **work state**, not decoration for elapsed time.

### STUDIO JUDGMENT

Use a determinate indicator only when its numerator/denominator or equivalent progress estimate has a defensible relationship to completion.

Do not display fake `70%` merely because 70% feels reassuring.

If the process consists of unequal stages, a stage indicator may be more honest than a false continuous percentage.

---

# 3. SOURCE — progress behavior changes perceived duration

Harrison, Amento, Kuznetsov, and Bell experimentally studied progress-bar temporal behavior and found that non-linear progress patterns can alter perceived duration even when actual duration is unchanged.

Primary source:

- Harrison C, Amento B, Kuznetsov S, Bell R. *Rethinking the Progress Bar*. UIST 2007. DOI: 10.1145/1294211.1294231
- https://chrisharrison.net/index.php/Research/ProgressBars

### SYNTHESIS

The shape of progress over time affects user perception.

### STUDIO JUDGMENT

Do **not** interpret this as permission to deceive users by fabricating progress.

Apple's current guidance explicitly warns against highly misleading advancement patterns such as reaching near completion quickly and then appearing stalled.

The studio therefore treats progress pacing as a communication-design problem constrained by truthfulness.

---

# 4. SOURCE — show useful content/status rather than blank waiting

Apple's current Loading guidance recommends showing something as soon as possible, allowing other activity while content loads when feasible, and clearly communicating ongoing work when loading is long enough to become noticeable.

Source:

- https://developer.apple.com/design/human-interface-guidelines/loading

### SYNTHESIS

The first design question is not “which spinner?” but:

> What useful state can the product expose while the final result is unavailable?

Possibilities:

- existing cached content;
- skeleton/placeholder that preserves page structure;
- partial results with explicit incompleteness;
- local optimistic value with pending marker;
- last-synced value plus refresh state;
- background continuation with a completion notification;
- determinate progress;
- indeterminate activity where no estimate is honest.

### Failure mode

Blocking the entire surface because one secondary region is loading can unnecessarily convert local latency into global latency.

---

# 5. Acceptance, pending, progress, and completion are separate states

## STUDIO MODEL

For a consequential asynchronous action, model at least:

1. **Idle** — no request in flight.
2. **Accepted locally** — input passed local validation and the UI accepted the intent.
3. **Pending** — remote/process outcome is not yet confirmed.
4. **Progressing** — optional measurable or observable substate.
5. **Confirmed** — authoritative completion is known.
6. **Failed** — authoritative failure is known.
7. **Canceled** — the requested work was successfully halted or locally abandoned under a defined policy.
8. **Outcome unknown** — the client stopped waiting or lost communication, but cannot prove whether the external operation committed.

### SYNTHESIS

`Outcome unknown` is different from `Failed`.

A network timeout, process death or lost response may happen **after** the server/external system committed the work.

### STUDIO JUDGMENT

Any workflow with expensive duplicate side effects must have an explicit outcome-unknown policy.

Examples:

- payment;
- purchase/order creation;
- tax filing;
- invitation/email send;
- account deletion;
- booking;
- irreversible remote command.

Do not show “Failed — Retry” automatically if repeating the action could duplicate the side effect.

---

# 6. SOURCE — automatic retry safety depends on idempotency

RFC 9110 defines an idempotent request method as one for which multiple identical requests have the same intended effect as one request. It states that a client should not automatically retry a non-idempotent request unless it has a means to know the request semantics are effectively idempotent or to know the original request was not applied.

Primary source:

- RFC 9110, HTTP Semantics, Section 9.2.2 Idempotent Methods
- https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods

### SYNTHESIS

Retry policy is part of the product/API contract.

### STUDIO JUDGMENT — three retry classes

#### A. Safe automatic retry

Use only when the operation contract makes repeated attempts safe.

Examples may include:

- idempotent retrieval/update semantics;
- application-level idempotency key or deduplication contract;
- known-not-processed request.

#### B. User-initiated retry after known failure

Appropriate when failure is authoritative and repeating the action is safe or clearly explained.

#### C. Verify before retry

Required when the outcome is ambiguous and duplicate commitment would be harmful.

Possible recovery:

- check operation status;
- refresh authoritative data;
- query transaction/order ID;
- reconcile local and remote state;
- ask user to wait/check rather than resubmit.

### Failure mode

A visually enabled Retry button can be technically easy to implement while semantically unsafe.

---

# 7. Optimistic UI is a commitment strategy, not a speed effect

An optimistic UI shows the intended result before authoritative confirmation.

### STUDIO JUDGMENT — optimistic update is a candidate when

- expected success rate is high;
- consequence is low or moderate;
- the action is reversible or compensable;
- conflict probability is manageable;
- temporary divergence from server truth is understandable;
- rollback/reconciliation can be explained;
- the user benefits from immediate continuity.

Examples can include:

- local preference toggle;
- low-consequence like/bookmark/favorite;
- reorder with robust rollback/conflict policy;
- local draft edit queued for sync.

### Do not default to optimistic success when

- money or legal commitment occurs;
- scarce inventory/booking confirmation is uncertain;
- permission/authorization may fail;
- irreversible external side effects occur;
- conflicting multi-user edits are likely;
- showing success before confirmation could cause a user to leave or act on false information.

### Required optimistic states

If optimism is used, define:

- optimistic/local value;
- pending evidence;
- authoritative success convergence;
- rollback or conflict state;
- retry/reconciliation behavior;
- navigation behavior while pending.

The user should not have to infer from a silent rollback that the action failed.

---

# 8. Duplicate submission prevention is not merely disabling a button

### STUDIO JUDGMENT

Repeated activation policy should answer:

- Is a second activation ignored, queued, merged, canceled, or treated as another operation?
- Does the button become disabled because duplication is unsafe, or only because the implementation is not ready?
- Can unrelated work continue?
- If the user navigates away, does the request continue?
- What happens after reconnect/reload?
- Is there an operation identifier that can be checked later?

### Failure modes

- disable the whole page for one local save;
- leave a purchase/submit button active with no duplicate-protection contract;
- disable the only control but provide no pending/status evidence;
- re-enable after a local timeout even though remote commitment is unknown;
- silently issue multiple requests while rendering one spinner.

---

# 9. Cancellation has two meanings

A `Cancel` control may mean:

1. stop waiting / dismiss this UI;
2. actually stop the underlying operation.

These are not equivalent.

### STUDIO JUDGMENT

Label and feedback must match the real contract.

If the operation cannot be stopped after submission, a UI action should not imply that it can.

Possible labels/contracts:

- `Hide` / `Continue in background`;
- `Stop upload`;
- `Cancel export`;
- `Dismiss`;
- `Undo` after completion.

If cancellation can lose completed work, communicate the consequence proportionally.

---

# 10. Accessible status must not steal focus by default

WCAG's Status Messages requirement addresses important dynamic changes that should be programmatically determinable without necessarily moving focus.

WAI techniques document `role="status"` / polite live-region patterns, and WAI-ARIA defines `progressbar` plus `aria-busy` semantics for regions undergoing updates.

Sources:

- https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
- https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA22.html
- https://www.w3.org/TR/wai-aria-1.2/

### SYNTHESIS

Pending/completion feedback has two separate questions:

1. what should be visible;
2. what should be announced/programmatically exposed.

### STUDIO JUDGMENT

Routine pending/success should usually preserve the user's working focus.

Move focus only when the resulting context or recovery interaction genuinely requires it.

Do not put interactive recovery controls inside a status/live region merely because they appear next to the message; I001's running validation already exposed this structural error.

---

# 11. Latency design matrix

For each operation document:

| Dimension | Question |
| --- | --- |
| Intent | What is the user trying to accomplish? |
| Local acceptance | Can the UI immediately validate/accept the intent? |
| Authoritative owner | Which system decides success? |
| Consequence | What happens if success is shown too early? |
| Reversibility | Can the effect be undone/compensated? |
| Expected duration | Stable, variable, unknown? |
| Progress measurability | Is determinate progress truthful? |
| Parallel work | Can the user keep working? |
| Duplicate semantics | What does repeated activation mean? |
| Idempotency/reconciliation | Can a retry safely repeat the operation? |
| Timeout semantics | Does timeout mean failed or only unknown? |
| Cancellation | Can underlying work actually stop? |
| Recovery | Retry, rollback, check status, edit, reconcile, contact support? |
| Accessibility | Visible status, live status, focus behavior? |
| Navigation | What survives if the user leaves/returns? |

---

# 12. Project-facing decision patterns

## Pattern A — immediate confirmed local action

Use when no meaningful async commitment exists.

Feedback:

- immediate state change;
- no spinner.

## Pattern B — pessimistic pending commit

Use when authoritative confirmation matters before showing success.

Feedback:

- accepted/pending state;
- disable or guard duplicate commitment as required;
- confirmed or failed result;
- recovery.

## Pattern C — optimistic reversible update

Use when immediate continuity is valuable and rollback/reconciliation is acceptable.

Feedback:

- optimistic value;
- subtle but perceivable pending state when material;
- convergence on success;
- explicit rollback/conflict/error on failure.

## Pattern D — long determinate process

Use when progress is meaningfully measurable.

Feedback:

- determinate progress;
- remaining-stage context if useful;
- pause/cancel only when real;
- background continuation if appropriate.

## Pattern E — long indeterminate process

Use when duration/progress cannot be estimated honestly.

Feedback:

- activity/pending state;
- meaningful description where needed;
- escape/background option if feasible;
- stalled/failure recovery.

## Pattern F — ambiguous remote outcome

Use when response is lost but commit may have occurred.

Feedback:

- `Checking status…` or equivalent;
- do not label as failed prematurely;
- verify authoritative state;
- retry only after safety is established.

---

# 13. Project Readiness Test

Before approving an async interaction, the specialist must be able to answer:

- What exact state is shown immediately after activation?
- Does that state mean accepted, pending, or completed?
- Who is authoritative for success?
- Can the user continue other work?
- Is progress measurable honestly?
- What does repeated activation do?
- Is retry safe? Why?
- What if the client times out after the server commits?
- Can cancellation stop the work or only close the UI?
- What state survives navigation/reload/interruption?
- How is failure distinguished from outcome uncertainty?
- How is status communicated without unnecessary focus movement?
- What Color/Type/Web evidence is required for final production validation?

If these answers are missing, a spinner does not make the interaction complete.

---

# 14. Failure modes

Reject or rework when:

- optimistic success is shown for a high-consequence operation without rollback/reconciliation;
- timeout is treated as authoritative failure without evidence;
- automatic retry can duplicate a non-idempotent side effect;
- determinate progress is fabricated from elapsed time rather than work completed;
- an indeterminate indicator spins forever with no stalled/recovery policy;
- progress reaches near-complete and remains stalled because stages were modeled dishonestly;
- the whole application is blocked for a local asynchronous region;
- the submit control is disabled with no status evidence;
- duplicate activations issue multiple commits without an explicit policy;
- `Cancel` only closes a dialog while the irreversible operation continues, without saying so;
- background completion is possible but the user is forced to watch a spinner;
- routine status steals keyboard focus;
- recovery action is embedded inside a live status region without a deliberate accessibility reason;
- pending/error/success are distinguished only by color.

---

# 15. Practice gate

Before I002 can move beyond source/project framework, create a running specimen with at least three materially different operation classes:

1. **optimistic reversible action** — immediate local change, pending, success/failure rollback;
2. **non-idempotent/high-consequence commit** — pessimistic pending, timeout/outcome-unknown, verify-before-retry;
3. **long-running operation** — determinate or indeterminate progress plus truthful cancellation/background behavior.

The specimen must include:

- repeated activation test;
- explicit operation IDs or equivalent where needed;
- one lost-response/ambiguous-outcome path;
- one retry-safe path;
- one retry-unsafe path;
- visible and programmatic status separation;
- keyboard/focus behavior;
- failure → revision → re-proof;
- KEEP / REWORK / REJECT critique.

---

# OPEN

1. Build the I002 running specimen and test repeated activation, lost response and outcome reconciliation.
2. Validate real request cancellation/AbortController semantics separately from UI dismissal in a Web context.
3. Test screen-reader announcement frequency for progress updates; do not infer ideal announcement cadence from visual update rate.
4. Study offline-first queued writes and multi-device conflict resolution as a later Interaction/system topic.
5. Study latency under collaborative/multi-user state where server rejection/conflict is routine rather than exceptional.
6. Compare user task performance under optimistic vs pessimistic strategies only with actual human testing; do not infer performance from code-path speed.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - accepted/pending/confirmed/failed/outcome-unknown/retry labels are semantic text roles that must survive localization, fallback and enlargement.
- Canonical section:
  - State model and latency design matrix.
- Confirmation / contradiction / transfer note:
  - extends Type's status/action-text contexts into latency-specific roles.
- Scope limit:
  - Interaction does not specify font metrics or text rendering.

### Color
- Useful finding/context:
  - pending, confirmed, failed and outcome-unknown are distinct semantics and should not be collapsed into one warning/accent hue.
- Canonical section:
  - State model and failure modes.
- Confirmation / contradiction / transfer note:
  - supplies state semantics for C002 role architecture and C001 forced-color resilience.
- Scope limit:
  - no palette or contrast decision is made here.

### Layout / Interaction
- Useful finding/context:
  - timeout is not necessarily failure; retry safety depends on operation semantics; cancellation may mean dismissing UI or stopping work.
- Canonical section:
  - Sections 5–9.
- Confirmation / contradiction / transfer note:
  - extends Study 015's commitment model and I001's recovery/navigation model into latency and ambiguous outcome.
- Scope limit:
  - running proof still required.

### Web Design
- Useful finding/context:
  - concrete state/retry/cancellation contracts for real browser/network implementation.
- Web application / validation consequence:
  - reproduce with real requests, aborts, offline/reconnect, duplicate submissions, idempotency/reconciliation, live regions and browser navigation.
- Confirmation / contradiction / transfer note:
  - Interaction-side project contract established; actual Web implementation remains open.
- Scope limit:
  - no W### browser/network evidence is claimed.
