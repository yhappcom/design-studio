# CD011 — Error, Warning, Service Failure, and Recovery Taxonomy

Status: **STAGE 2 PRACTICE — CROSS-STATE TAXONOMY + COMPARATIVE PRACTICE / NOT PASSED**  
Date: 2026-09-16

## Question

How should an English-first global product keep validation errors, warnings, conflicts, service failures, pending states, authoritative failures, and outcome-unknown states semantically distinct while still presenting a coherent content system?

CD010 established the form contract. CD011 extends it across product states so `error` does not become a catch-all content category.

## RELATED DOMAIN CHECK

### Type
Operational state strings are required semantic test material. Type may expose wrapping/density defects but does not authorize deletion of state distinctions.

### Color
Severity/state may be visually reinforced, but warning/error/failure identity must survive color loss or transformation.

### Layout / Interaction
Direct reuse of `I002-latency-pending-optimistic-retry.md`: accepted, pending, confirmed, failed, canceled and outcome-unknown are different behavioral states; retry safety depends on actual operation semantics/idempotency. Content preserves rather than invents these distinctions.

### Web
W015–W017 establish that runtime state, focus, accessible naming and non-color signaling need executable transfer. CD011 supplies the semantic taxonomy for later browser/native implementation testing.

### Content
CD001/CD003/CD008 established state/action/consequence fidelity; CD010 separated user-correctable validation from service/system problems.

Overlap classification: **EXTENSION + INTERACTION-TO-CONTENT TRANSFER**.

---

## 1. Core taxonomy

| State class | Product truth | Content job | Typical recovery |
|---|---|---|---|
| validation error | entered information cannot be used and user can correct it | identify concept + specific repair | edit input |
| warning | action is available but has material risk/consequence worth surfacing before commitment | name consequence without falsely blocking | continue/cancel/change |
| business-rule block | product rule prevents requested action | explain rule and available next step | change condition / alternate path |
| permission block | user lacks authority | identify access limitation without blaming input | request access / alternate owner |
| conflict | current intent conflicts with another authoritative/local state | identify competing states and decision needed | reconcile/choose/review |
| pending | operation accepted but not yet confirmed | communicate ongoing unconfirmed state | wait/cancel only if actually supported |
| authoritative failure | product knows operation did not complete | state non-completion + preserved intent + safe recovery | retry/edit/alternate path if safe |
| outcome unknown | product cannot prove whether operation committed | state uncertainty; prevent duplicate side effect | verify/reconcile before retry |
| service unavailable | system cannot currently provide capability | distinguish service problem from user input | wait/alternate path/status |
| success/confirmed | authoritative completion is known | state result/consequence proportionally | next task/undo if supported |

### STUDIO JUDGMENT

The taxonomy is based on **cause + certainty + agency + recovery**, not visual severity.

A red banner and a red field border can represent different semantic classes; sharing a color does not make them the same message pattern.

---

## 2. Warning is not a softer error

A warning appears before or around an action that remains available but carries a material consequence or risk. If the product has already prohibited the action, the state is a block, not merely a warning.

Content questions:
1. What will happen if the user proceeds?
2. Is the consequence reversible?
3. What scope is affected?
4. Is the warning based on known fact, probability, or uncertainty?
5. What alternatives exist?

Reject vague intensity language such as `Are you sure?` when the actual consequence can be named.

Example direction:
- weak: `Are you sure you want to continue?`
- stronger when true: `Delete 12 imported records? This removes them from this logbook. You can’t undo this action.`

The exact destructive-action behavior remains Interaction/product truth.

---

## 3. Failure certainty determines language

### Known failure

If the authoritative system confirms non-completion, language may state that the action did not complete.

Example architecture:
- result: `The record wasn’t saved.`
- preservation: `Your entries are still here.`
- action: `Try again` only when Interaction confirms repetition is safe.

### Unknown outcome

If response loss/timeout means commitment is unknown, do not say `failed`.

Example architecture:
- `We couldn’t confirm whether the record was saved.`
- recovery should check authoritative state before allowing a duplicate side effect.

This is a direct Content transfer of I002, not an independent network-semantics claim.

---

## 4. Service problem is not user error

GOV.UK's validation guidance explicitly separates user-correctable validation from service/capacity/eligibility problems. CD011 generalizes the diagnostic:

`Can the user repair this by changing the supplied information?`

If no, do not attach blame-like field copy merely because the failure appeared after form submission.

Examples to reject:
- `Invalid request` when the service is unavailable;
- `Check your information` when the server returned an unrelated failure;
- `Try again` when repeated submission could duplicate a committed action.

---

## 5. Comparative practice — one save operation, four truths

Fixed action: user selects `Save record`.

### Truth A — local validation failure
Registration is missing.

Content: `Enter the aircraft registration.`

Recovery: edit field; retain other entries.

### Truth B — authoritative remote failure
Server confirms save was rejected and no record was created.

Content architecture: `The record wasn’t saved. Your entries are still here.` Safe retry only if Interaction confirms it.

### Truth C — outcome unknown
Request left the client; response was lost; commit status cannot be established.

Content architecture: `We couldn’t confirm whether the record was saved.` Recovery: check/reconcile first.

### Truth D — confirmed success
Authoritative record ID returned.

Content architecture: `Record saved.` Additional explanation only if the result changes something non-obvious.

### CONTRADICTION TEST

A single generic pattern — `Something went wrong. Try again.` — fails B/C distinction and can create unsafe duplicate submission in C. Therefore a unified visual component must not imply a unified semantic message contract.

---

## 6. Content-state contract v0.1

For every consequential state message specify:

- `state_class`
- `object`
- `known_fact`
- `uncertainty`
- `user_agency`
- `consequence`
- `preserved_intent_or_data`
- `available_recovery`
- `retry_safety`
- `dismissal_meaning`
- `persistence_duration`
- `visible_name/status relationship`
- `localizer_context`

### Failure rule

If `retry_safety = unknown`, Content must not independently emit a retry command.

If `uncertainty = outcome_unknown`, wording must not claim authoritative failure or success.

---

## 7. Global-English/localization constraints

- use complete state propositions, not fragments assembled around status tokens;
- avoid idioms such as `Oops`, `hit a snag`, or culture-specific reassurance as the only explanation;
- keep product/domain objects explicit when the message may appear out of context;
- separate semantic keys for `warning`, `failure`, `unknown outcome`, and `validation` even if English surface wording overlaps;
- localizer notes must identify whether a message is pre-action warning, post-action failure, or uncertain outcome;
- variables must identify object/count/scope, not rely on English word order;
- do not compress a high-consequence warning solely to keep a one-line component.

---

## 8. Tone modulation follows risk, not brand theatrics

Functional truth precedes personality.

Provisional rule:
- low-risk recoverable validation: direct, neutral, repair-focused;
- consequential warning: explicit scope/consequence, low ambiguity;
- system failure: acknowledge blocked task and recovery without blaming user;
- outcome unknown: calibrated uncertainty, no false reassurance;
- success: proportional confirmation, avoid celebratory noise for routine operations.

This is a bridge to later voice/tone study, not a complete voice system.

---

## 9. Audit v0.1

Flag:
- `STATE_CLASS_COLLAPSE`
- `FALSE_FAILURE`
- `FALSE_SUCCESS`
- `WARNING_WITHOUT_CONSEQUENCE`
- `USER_BLAME_FOR_SERVICE_FAILURE`
- `GENERIC_ERROR_NO_REPAIR`
- `UNSAFE_RETRY`
- `DISMISSAL_AMBIGUITY`
- `PRESERVED_DATA_UNSTATED_WHEN_MATERIAL`
- `COLOR_ONLY_SEVERITY`
- `FRAGMENTED_LOCALIZATION_MESSAGE`
- `MISSING_LOCALIZER_STATE_CONTEXT`
- `RUNTIME_DELIVERY_VALIDATION_NEEDED`
- `HUMAN_VALIDATION_NEEDED`

The audit detects semantic-system defects; it does not measure comprehension, stress, trust or task recovery.

---

## 10. KEEP / REWORK / REJECT

### KEEP
- taxonomy by cause/certainty/agency/recovery;
- explicit distinction between known failure and unknown outcome;
- warning consequence before generic confirmation language;
- preserved-intent/data information when it changes recovery decisions;
- state-specific localization context.

### REWORK
- exact persistence/dismissal behavior by platform;
- warning thresholds for professional domains;
- conflict wording for offline/multi-device LogMate synchronization;
- severity/tone system after more surface practice.

### REJECT
- one generic `error` content pattern;
- `Something went wrong. Try again.` as a universal fallback;
- `Are you sure?` without consequence/scope;
- `invalid` for service/permission/business-rule problems;
- celebratory success noise for routine operations;
- retry commands unsupported by Interaction truth.

---

## Stage 2 implication

CD011 closes the immediate taxonomy gap identified by CD010 and provides a reusable cross-state contract. Stage 2 remains **PRACTICE / NOT PASSED** because empty/loading/pending/success systems, onboarding/progressive disclosure, search/filter/settings, voice/tone, localization pattern transfer and an integrated Stage 2 capstone remain incomplete.

## OPEN

- offline and multi-device conflict language using actual LogMate sync semantics;
- warning thresholds and confirmation requirements for high-consequence domain actions;
- actual status persistence/dismissal behavior;
- human comprehension/trust/recovery evidence;
- browser/native AT delivery;
- production telemetry linking message states to recovery outcomes.

## HANDOFFS TO OTHER SPECIALISTS

### Interaction
CD011 preserves I002's outcome-unknown/retry-safety contract. Future LogMate sync/conflict content requires exact Interaction state-machine truth before wording.

### Web
Use `state_class` and `known_fact/uncertainty/recovery` as semantic inputs for runtime status/error/warning components; test focus, announcements, persistence and reflow independently.

### Color
Map visual severity only after semantic state class is known; verify state identity survives color removal.

### Type
Use high-consequence warnings and recovery strings as realistic expansion/wrapping stress cases rather than shortening them by default.

## Evidence level

**PEER-EVIDENCE TRANSFER + SOURCE-GROUNDED TAXONOMY + COMPARATIVE STATE PRACTICE + CONTRADICTION TEST + KEEP/REWORK/REJECT. No human or runtime PASS claimed.**
