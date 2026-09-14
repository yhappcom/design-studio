# I002 Validation Report — Pending, Outcome Unknown, Retry Safety, and Cancellation

Status: **PRACTICE + CRITIQUE / FAILURE → REVISION → RE-PROOF COMPLETE FOR THE CONTROLLED SPECIMEN**  
Owner: Layout, Spatial & Interaction Specialist  
Canonical research being validated: `research/interaction/I002-latency-pending-optimistic-retry.md`

Reproducible artifacts:

- `research/interaction/I002-async-validation-specimen.html`
- `research/interaction/I002-async-validation-playwright.py`
- `research/interaction/I002-async-validation-results-summary.json`

This report records executable state-contract evidence. It does **not** promote I002 to PASS because real HTTP/API behavior, actual server idempotency/deduplication, browser request cancellation, offline/reconnect, assistive technology, cross-browser/device behavior, localization and human task evidence remain open.

---

## Objective

Test whether I002's latency model can prevent common async interaction failures rather than merely describe them.

Three materially different operation classes are represented:

1. **optimistic reversible favorite** — immediate local change, pending save, known failure, rollback, safe user retry;
2. **high-consequence transfer** — one remote commit, lost response, ambiguous outcome, status reconciliation before any retry;
3. **long-running export** — determinate progress and a Cancel action that must actually stop the simulated underlying work.

The controlled specimen also tests repeated activation, `aria-busy`, focus preservation, recovery-control focus restoration and separation between live status and interactive recovery actions.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `progress/TYPE_STATUS.md` through T004;
  - current Type handoffs for status/action text, fallback, localization and compact rendering.
- Reusable finding:
  - pending/error/retry/status labels are real semantic text roles and can fail under fallback, wrapping, localization and enlargement.
- Replication / challenge / transfer opportunity:
  - rerun this specimen with long Korean labels, mixed-script fallback and enlarged text.
- Dependency / overlap:
  - Interaction owns state semantics and focus/recovery; Type owns font, metrics and rendered text behavior.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md` through C003;
  - C001 forced-color resilience and C002 semantic role architecture.
- Reusable finding:
  - pending, error, confirmed and focus states must not depend on one literal color channel;
  - semantic roles should precede token/color assignment.
- Replication / challenge / transfer opportunity:
  - run unknown/failure/pending/confirmed states under forced colors, light/dark and semantic-token substitutions.
- Dependency / overlap:
  - this controlled specimen uses text/state structure first and does not claim Color validation.

### Layout / Interaction
- Evidence checked:
  - Studies 007 and 015;
  - I001 source and running validation;
  - I002 source study;
  - current `progress/LAYOUT_STATUS.md`.
- Reusable finding:
  - local optimistic state, remote pending state and authoritative confirmation are distinct;
  - status and recovery action are separate channels;
  - navigation/focus/data-lifecycle policy must survive async transitions.
- Replication / challenge / transfer opportunity:
  - this report directly tests these distinctions in running code.
- Dependency / overlap:
  - primary ownership remains Interaction.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web Design owns complete real browser/network/page-system integration.
- Implementation/application validation opportunity:
  - real `fetch`, AbortController, network timeout, offline/reconnect, request IDs/idempotency keys where supported by the actual service, duplicate submissions, reload/navigation and assistive technology.
- Dependency / overlap:
  - no substantive `W###` evidence was available; current result is Interaction-owned controlled validation, not Web canonical proof.

### Other / cross-cutting / future specialist
- Evidence checked:
  - RFC 9110 idempotency semantics;
  - WAI/WCAG status-message and ARIA busy/progress semantics;
  - response-time/progress literature synthesized in I002.
- Reusable finding:
  - ambiguous communication failure is not necessarily authoritative operation failure;
  - retry safety depends on operation semantics and data contracts.
- Dependency / overlap:
  - actual API idempotency and transaction reconciliation require engineering/service evidence in a live project.

### Overlap decision
- **PRACTICE + INDEPENDENT VALIDATION + FAILURE ANALYSIS + TRANSFER PREPARATION**.
- Why:
  - I002's source framework required running proof showing that its state distinctions actually catch implementation/design defects.

---

# 1. Baseline failure cycle

The first implementation intentionally used three common but weak patterns.

## F1 — native `disabled` caused focus loss during pending

Baseline optimistic favorite behavior:

- user activated Favorite;
- the button became natively disabled during save;
- the focused control lost focus.

### Why this matters

Disabling duplicate activation can be correct, but removing the active element from keyboard focus behavior without a replacement focus policy can interrupt orientation.

### Revision

For this controlled case:

- preserve the control in the focus order;
- expose `aria-disabled="true"` while pending;
- guard the activation handler against repeated requests;
- use `aria-busy` on the containing operation region.

### Scope limit

This is not a universal rule that `aria-disabled` should replace native `disabled`. If a control should truly be unavailable and focus retention is not required, native disabled semantics may be preferable. The project must decide whether the user's current locus should remain inspectable/action-addressable during pending.

---

## F2 — lost response was treated as failure and exposed Retry

Baseline high-consequence transfer:

- the simulated server committed once;
- the response was lost;
- the UI labeled the result as failure;
- Retry was exposed.

If the retry had actually repeated the commit, the product could have created a duplicate side effect.

### Revision

Introduce an explicit state:

**`outcome = unknown`**

Then:

- preserve an operation identifier;
- do not expose unsafe Retry;
- expose `Check status`;
- reconcile against authoritative state;
- only then show Confirmed or a known failure/recovery path.

### Professional implication

A timeout/error from the transport layer is not sufficient evidence for a product message saying the operation failed.

---

## F3 — Cancel changed UI but did not stop work

Baseline export:

- Cancel changed visible status to `Canceled`;
- the underlying interval continued;
- later, the same operation changed to `Export complete.`

### Revision

Cancellation now:

- clears the active work timer;
- increments an operation generation so stale updates are ignored;
- clears busy state;
- preserves the last completed progress value;
- reports `Export canceled.`.

### Professional implication

`Cancel` must describe what the product can actually cancel. If only the dialog can close while work continues, use a different contract such as `Hide`, `Dismiss`, or `Continue in background`.

---

# 2. Second-order focus failure after the first revision

The first corrected specimen passed the major state assertions, but review of the active element exposed another defect.

## F4 — disappearing recovery controls dropped focus to `body`

Examples:

- Retry Save succeeded and the Retry button disappeared;
- Check Status confirmed the transfer and the Check button disappeared;
- Cancel Export stopped the export and the Cancel button disappeared.

In each case, hiding the currently focused transient control without a destination could leave focus on the document body.

### Revision

Define a post-recovery focus contract:

- Retry completion → original Favorite control;
- Check status completion → stable Transfer control;
- Cancel export → Start Export control;
- automatic export completion also restores focus if the now-removed Cancel control happened to own focus.

### SYNTHESIS

A temporary recovery action has a lifecycle:

**appears → receives focus/activation → resolves → disappears → focus must have a logical destination**.

This extends I001's modal/route focus-restoration principle into inline async recovery controls.

---

# 3. Final state model in the specimen

## Optimistic reversible favorite

`idle → optimistic/pending → known failure/rollback → retry pending → confirmed`

Properties:

- local value changes immediately;
- first simulated save fails;
- rollback is explicit;
- Retry is safe in this controlled contract;
- repeated pending activation is ignored;
- focused origin remains stable;
- successful Retry returns focus to the durable Favorite control.

## High-consequence transfer

`idle → pending → server committed / response lost → outcome unknown → checking → confirmed`

Properties:

- one operation ID is generated;
- repeated submission while pending/unknown is blocked;
- server commit count stays at one;
- Retry remains hidden while outcome is unknown;
- Check status reconciles authoritative state;
- focus returns to a stable transfer control after Check disappears.

## Long-running export

`idle → progressing → canceled` in the tested path.

Properties:

- determinate native progress element;
- actual progress increments;
- `aria-busy` reflects operation state;
- Cancel stops the underlying simulated operation;
- stale updates are invalidated;
- focus returns to Start Export when Cancel disappears.

---

# 4. Final re-proof

The final Playwright harness produced **19 / 19 PASS** assertions:

1. optimistic immediate visual;
2. pending preserves focus;
3. `aria-busy` while saving;
4. duplicate favorite ignored;
5. failed optimistic action rolled back;
6. retry-safe favorite succeeds;
7. Retry completion restores focus;
8. duplicate transfer guarded;
9. lost response becomes outcome unknown;
10. unsafe Retry is not exposed;
11. Check status is exposed;
12. operation ID exists;
13. reconciliation confirms;
14. reconciliation restores focus;
15. no duplicate commit after reconciliation;
16. export is determinate and busy;
17. Cancel actually stops operation;
18. Cancel restores focus;
19. status regions do not steal focus.

### Evidence class

**PRACTICE + CRITIQUE / controlled Chromium JavaScript state-machine evidence.**

This is stronger than a static flow diagram but weaker than a real production/network test.

---

# 5. Project-facing conclusions

## 5.1 Pending should preserve semantic orientation

Preventing duplicate activation and preserving focus are separate decisions.

Do not use disabling as an automatic implementation reflex. Decide:

- must the control remain focusable/inspectable during pending?
- is repeated activation ignored, queued, merged, or invalid?
- what programmatic state communicates pending/unavailable behavior?

## 5.2 Failure and outcome uncertainty are different UX states

Known failure can justify Retry when repeating is safe.

Outcome unknown often requires verification first.

This distinction is especially important for:

- financial transfer/payment;
- order/booking creation;
- destructive remote commands;
- invitations/messages with external side effects;
- irreversible submissions.

## 5.3 Operation identity belongs in the recovery model

A high-consequence action may need a stable operation/request/transaction identity that can be queried later.

The Interaction Specialist need not prescribe the backend identifier implementation, but the product recommendation must identify the dependency when correct recovery requires it.

## 5.4 Cancel must distinguish stopping work from leaving the view

Use different labels/contracts for:

- cancel underlying operation;
- stop waiting;
- dismiss surface;
- continue in background;
- undo after completion.

## 5.5 Recovery controls need focus restoration

Focus restoration is not limited to modal dialogs and page navigation.

Inline controls that disappear after resolving a pending/error state require the same reasoning.

---

# 6. KEEP / REWORK / REJECT

## KEEP

- explicit pending/confirmed/failed/unknown distinctions;
- optimistic update only for the low-consequence reversible case;
- `aria-busy` on operation regions;
- non-interactive live status separated from recovery actions;
- operation identity for the ambiguous high-consequence case;
- verify-before-retry when duplicate commitment could be harmful;
- real cancel semantics for the export;
- post-recovery focus destinations.

## REWORK in production

- replace simulated timers with actual request/service state;
- determine whether `aria-disabled` vs native `disabled` is correct per control and input model;
- define real API idempotency/deduplication and operation-status contracts;
- validate announcement verbosity with screen readers;
- define navigation/reload behavior for pending operations;
- define offline/reconnect and cross-device reconciliation where applicable.

## REJECT

- timeout = failure by default;
- unsafe blind Retry for ambiguous non-idempotent operations;
- Cancel that only changes the label while work continues;
- disabling focused controls without considering focus lifecycle;
- hiding the focused Retry/Check/Cancel control without a post-resolution destination;
- interactive recovery controls embedded inside a live status region;
- color-only distinction among pending/error/unknown/success states.

---

# 7. Scope limits and OPEN

Not established by this block:

- real HTTP transport behavior;
- actual server-side idempotency or transaction isolation;
- actual idempotency-key implementation;
- AbortController/request-cancellation semantics;
- offline/reconnect/queued writes;
- browser refresh/process death restoration;
- cross-browser/device behavior;
- screen reader announcement quality/frequency;
- real network latency distributions;
- human preference or task performance;
- localization/fallback stress;
- actual Web framework/router/data-layer integration.

Therefore I002 remains **PRACTICE + CRITIQUE**, not PASS.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - async state introduces a family of high-value labels: Saving, Pending, Checking status, Failed, Outcome unknown, Retry, Canceled, Confirmed.
- Canonical section:
  - Sections 3–5.
- Confirmation / contradiction / transfer note:
  - these states should be used as long-label/localization/fallback stress contexts rather than generic lorem ipsum.
- Scope limit:
  - this study does not determine font metrics or hierarchy tokens.

### Color
- Useful finding/context:
  - `failed` and `outcome unknown` are semantically different; pending/confirmed/error/unknown should not be collapsed into one generic accent/warning role.
- Canonical section:
  - Sections 1–3 and KEEP/REJECT.
- Confirmation / contradiction / transfer note:
  - supplies explicit Interaction semantics for C002 role architecture and C001 forced-color testing.
- Scope limit:
  - no palette/contrast/device validation occurred.

### Layout / Interaction
- Useful finding/context:
  - disappearing inline recovery controls require focus restoration just like modal/navigation transitions;
  - retry policy belongs to the state/data contract, not merely button styling.
- Canonical section:
  - F2, F4, Sections 3–5.
- Confirmation / contradiction / transfer note:
  - extends Study 015 and I001 with executable latency/recovery evidence.
- Scope limit:
  - production network semantics remain external dependencies.

### Web Design
- Useful finding/context:
  - reusable three-operation specimen and 19-assertion transfer matrix covering optimistic rollback, duplicate guarding, ambiguous outcome reconciliation, progress/cancel and focus lifecycle.
- Web application / validation consequence:
  - reproduce with real `fetch`, request abort, network failure, offline/reconnect, real API idempotency/reconciliation, framework state and screen readers.
- Confirmation / contradiction / transfer note:
  - current result is controlled Interaction evidence; Web should return real browser/network limitations or contradictions.
- Scope limit:
  - no substantive W### evidence existed at this checkpoint.

---

# Next evidence step

Highest-value next I002 work is not another simulated timer variant.

It is one of:

1. real Web/browser network validation with a controlled local/test endpoint;
2. assistive-technology validation of busy/progress/status/recovery announcements;
3. project-specific API contract validation where duplicate commitment and outcome reconciliation matter.

Until then, Design Studio can use the I002 model to diagnose and specify async flows, but should label recommendations that depend on real service semantics as conditional.
