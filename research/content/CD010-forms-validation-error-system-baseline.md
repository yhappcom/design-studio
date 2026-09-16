# CD010 — Stage 2 Entry: Forms, Validation, and Error-System Baseline

Status: **STAGE 2 PRACTICE / SOURCE + SYSTEM PRACTICE + CRITIQUE / NOT A PASS CLAIM**  
Date: 2026-09-16

## Question

How should an English-first global professional app design form questions, helper text, validation, and error/recovery content as one coherent system rather than as isolated strings?

This is the first Stage 2 study after CD009 closed Foundation with PASS. The objective is repeated professional-surface application, not more Foundation theory.

## RELATED DOMAIN CHECK

### Type
Current Type status remains Stage 2 practice. T021 has exposed that operational strings must not be silently shortened to conceal drawing/metric defects. Transfer here: form labels, hints and errors are semantic inputs whose required meaning survives Type pressure. Exact rendering remains Type-owned.

### Color
Color Stage 2 is PASS. Transfer: invalid/error state cannot be owned by red alone; text and programmatic semantics must identify the problem. Color can reinforce state.

### Layout / Interaction
Layout/Interaction Stage 2 is PASS. Interaction owns when validation runs, what input is acceptable, whether data is preserved, what recovery is available, and whether a failure is user-correctable or service/system-owned. Content must not relabel a service failure as a field-validation problem.

### Web
Web Stage 2 remains practice with strong native/custom control and accessibility-transfer evidence. Web owns actual label association, described-by relationships, focus movement, live/status delivery, browser validation behavior and runtime testing. Content specifies semantic relationships but does not claim browser/AT proof.

### Existing Content
CD002 supplies concept/terminology identity; CD003 command/consequence fidelity; CD004 minimum-sufficient information; CD005 accessible naming; CD007 localization-ready complete message units; CD008/CD009 integrated judgment and Foundation closure.

Overlap classification: **STAGE-2 APPLICATION + TRANSFER PREPARATION**.

---

## 1. SOURCE — validation should identify a usable-input problem, not every blocked outcome

GOV.UK's current validation pattern distinguishes information the service cannot use from eligibility, permission, capacity, or service problems. It recommends minimizing validation failures by designing questions well and accepting harmless format variation where ambiguity is not introduced.

Sources:
- GOV.UK Design System — Recover from validation errors: https://design-system.service.gov.uk/patterns/validation/
- GOV.UK Design System — Error message: https://design-system.service.gov.uk/components/error-message/

### SYNTHESIS

Before writing an error, classify the failure owner:

1. **missing/invalid/ambiguous user input** — field/form validation;
2. **business-rule eligibility or permission** — explain the rule/outcome, not `invalid input`;
3. **service/system failure** — system/recovery message;
4. **commitment/outcome uncertainty** — Interaction recovery contract, not ordinary form validation.

### STUDIO JUDGMENT

`There is an error` is not a diagnosis. Error content begins with failure classification.

---

## 2. SOURCE — errors need identification and, when known, a correction path

WCAG 2.2 input-assistance requirements establish that automatically detected input errors are identified and described in text (3.3.1); labels/instructions are provided where input is required (3.3.2); and known correction suggestions are provided unless that would undermine security/purpose (3.3.3).

Sources:
- W3C WAI Forms Tutorial — User Notification: https://www.w3.org/WAI/tutorials/forms/notifications/
- W3C ACT/WCAG input assistance index: https://www.w3.org/WAI/standards-guidelines/act/rules/

### SYNTHESIS

A useful field-error contract normally needs:
- **identity** — which field/concept;
- **problem** — missing, impossible, ambiguous, too long, wrong relationship, etc.;
- **repair** — what acceptable correction is known;
- **preservation** — retain prior input unless there is a defensible reason not to;
- **delivery dependency** — how the implementation associates/announces/navigates to it.

Content owns the first three semantically; preservation and delivery require Interaction/Web collaboration.

---

## 3. SOURCE — prevent avoidable errors before polishing error copy

GOV.UK recommends accepting multiple harmless formats, ignoring unwanted formatting characters when doing so is unambiguous, retaining both passing and failing answers after validation, and avoiding premature per-field validation unless research supports it.

W3C similarly recommends forgiving input processing where possible.

Sources:
- https://design-system.service.gov.uk/patterns/validation/
- https://www.w3.org/WAI/tips/developing/

### STUDIO JUDGMENT

Use this order:

`remove unnecessary constraint → improve question/label → add point-of-need instruction → validate → write recovery message`.

Do not compensate for an unnecessarily strict parser with increasingly elaborate error prose.

---

## 4. Form-content architecture

For each field/question, specify separately:

| Layer | Purpose | Example |
|---|---|---|
| concept ID | stable product meaning | `flight.registration` |
| visible label/question | what information is requested | `Aircraft registration` |
| requiredness | whether omission blocks progression | required |
| helper/hint | information needed before entry | `Use the registration shown in your flight record.` |
| accepted semantic domain | actual allowed values/relationships | registration identifier known to record |
| formatting policy | normalization vs rejection | trim surrounding spaces; preserve meaningful hyphen |
| validation state | specific failure class | missing / unrecognized / conflict |
| error message | problem + repair | `Enter the aircraft registration.` |
| recovery | what remains possible | edit value; keep other fields |
| localization context | translator/domain notes | aviation identifier; do not translate identifier value |

### STUDIO JUDGMENT

Helper text and error text are not interchangeable.

- **Helper text** prevents foreseeable uncertainty before failure.
- **Error text** explains an observed failure and repair.

Do not repeat every rule twice. Put stable entry guidance before input; reserve errors for the specific failed condition.

---

## 5. Error taxonomy v0.1

### A. Missing required value
Pattern: `Enter {field concept}.`

Use when the only failure is absence and the requested concept is already clear.

### B. Format/shape problem
Pattern: `{Field} must ...` or `Enter {field} in ... format` only when format is genuinely required.

First ask whether normalization can remove the constraint.

### C. Range/relationship problem
Describe the violated relationship, not `invalid`.

Example: `Arrival time must be after departure time.`

This assumes the product contract actually requires same-record chronological ordering; domain exceptions must be modeled rather than copy-hidden.

### D. Ambiguous/unrecognized professional identifier
State what could not be matched and what evidence the user can inspect/correct.

Avoid pretending that `unrecognized` means objectively nonexistent.

### E. Cross-field conflict
Name both concepts when necessary to repair the relationship.

### F. Permission/eligibility/business-rule block
Not a field error by default. Explain the actual rule/outcome and available next action.

### G. System/service failure
Not a field error. Preserve entered data where possible and provide the actual recovery contract.

### H. Outcome unknown after submission
Not `Submission failed`. Reuse Interaction's outcome-unknown contract and verify before unsafe resubmission.

---

## 6. Three materially different form-content strategies

Fixed exercise: add one professional flight record containing date, flight number, registration, departure, arrival and block time. The system can normalize harmless whitespace; some identifiers may be unknown to the local dataset; save may fail authoritatively or become outcome-unknown.

### Candidate A — Rule-heavy upfront

Every field carries format/rule prose before entry; errors restate all rules.

Example registration hint:
`Required. Enter 2–10 uppercase letters, numbers, or hyphens. Do not enter spaces.`

**KEEP:** useful only where multiple non-obvious constraints truly cannot be removed and pre-entry knowledge prevents expensive failure.

**REWORK:** move implementation-derived syntax out of user language when normalization/domain semantics can handle it.

**REJECT as default:** high duplication; teaches parser syntax rather than task concepts; localization burden rises; may overconstrain legitimate global identifiers.

### Candidate B — Minimal labels + generic errors

Labels only; generic messages such as `Required`, `Invalid format`, `Try again`.

**KEEP:** low visual text volume.

**REJECT:** weak concept identity out of context; no repair guidance; `Try again` may be unsafe after ambiguous submission; generic `invalid` collapses distinct failure causes.

### Candidate C — Concept-first progressive assistance

Stable domain labels; point-of-need hint only where ambiguity is foreseeable; forgiving normalization; specific errors only after a known failed condition; service/outcome failures separated from field validation.

Examples:
- label: `Aircraft registration`
- hint when needed: `Use the registration shown in your flight record.`
- missing: `Enter the aircraft registration.`
- unmatched local reference: `We couldn't match this registration to the current aircraft list. Check the registration or continue if the record is correct.` **only if Interaction/product rules actually allow that continuation**
- authoritative save failure: `The record wasn't saved. Your entries are still here.` + safe recovery action defined by Interaction
- outcome unknown: `We couldn't confirm whether the record was saved.` + verification path; no blind `Retry`

**KEEP provisionally.** It minimizes unnecessary instruction while preserving specific repair semantics and failure ownership.

### Selection

Candidate C is retained as the Stage 2 baseline. This is a **STUDIO JUDGMENT**, not human-performance evidence.

---

## 7. English-first global constraints

Form architecture must not encode English grammar or US-only assumptions into data rules.

Required checks:
- do not infer allowed characters from ASCII-only English expectations;
- do not hard-code date/number/unit presentation into semantic values;
- keep complete error propositions rather than concatenated fragments;
- give translators context for professional abbreviations and identifiers;
- separate identical English strings when concepts differ;
- expect translated labels/errors to expand and reflow;
- never shorten necessary repair information solely to preserve one-line geometry.

### CONTRADICTION REVIEW

A common UI heuristic says errors should always be extremely short. CD004/CD007 and this study reject that as an absolute rule. The target is **minimum sufficient repair information**, not minimum characters.

---

## 8. Validation timing is not a Content-owned universal rule

GOV.UK generally defers validation until progression/submission and warns that premature validation can create problems, while allowing research-supported exceptions such as character limits.

### STUDIO JUDGMENT

Content must specify messages for states that Interaction decides can actually occur. It must not independently prescribe `validate on blur`, `validate while typing`, or `validate only on submit` as universal behavior.

Timing decision inputs include:
- cost of late discovery;
- whether the user has completed the thought/value;
- stability of validation knowledge;
- accessibility/runtime delivery;
- risk of distracting or falsely accusing the user mid-entry.

---

## 9. Error summary vs local error — semantic relationship

GOV.UK uses both a page-level error summary and matching local errors for its service context. This is strong precedent, not a universal native-app mandate.

Source:
- https://design-system.service.gov.uk/components/error-summary/

### TRANSFER JUDGMENT

For complex multi-field forms, the Content system should support:
- one canonical error proposition per failure;
- reuse in local and summary contexts when both exist;
- enough concept identity that the summary makes sense out of field context.

Whether a native/mobile product needs a page-level summary is a Layout/Interaction/platform decision requiring transfer validation.

---

## 10. Forms/content audit v0.1

For each field and submission state, check:

### Question quality
- `CONCEPT_CLEAR`
- `USER_CAN_KNOW_ANSWER`
- `NECESSITY_JUSTIFIED`
- `DOMAIN_TERM_STABLE`
- `HELP_BEFORE_ERROR_WHEN_NEEDED`

### Constraint quality
- `CONSTRAINT_NECESSARY`
- `NORMALIZATION_POSSIBLE`
- `GLOBAL_CHARACTER_ASSUMPTION`
- `LOCALE_FORMAT_SEPARATED`

### Error quality
- `FAILURE_OWNER_CORRECT`
- `FIELD/CONCEPT_IDENTIFIED`
- `SPECIFIC_FAILURE_CLASS`
- `KNOWN_REPAIR_STATED`
- `NO_BLAME/JARGON`
- `NO_FALSE_FAILURE`
- `NO_UNSAFE_RETRY`

### Recovery/system
- `INPUT_PRESERVED`
- `OTHER_VALID_INPUT_PRESERVED`
- `RECOVERY_EXISTS`
- `AMBIGUOUS_OUTCOME_SEPARATE`

### Localization/accessibility handoff
- `COMPLETE_MESSAGE_UNIT`
- `LOCALIZER_CONTEXT`
- `VISIBLE_PROGRAMMATIC_IDENTITY_ALIGNED`
- `RUNTIME_ASSOCIATION_TEST_NEEDED`
- `REFLOW_TEST_NEEDED`

This audit identifies structural/content-system debt. It does not establish comprehension, task success, AT behavior, or locale quality.

---

## 11. Critique

### KEEP
- classify failure owner before writing;
- prevent avoidable errors by relaxing unnecessary format constraints;
- concept-first labels;
- point-of-need help rather than universal instruction walls;
- specific repair messages;
- preserve input;
- separate field validation, business-rule blocks, service failures and outcome uncertainty;
- complete localization-ready message units.

### REWORK
- exact platform-specific error-summary/focus strategy;
- professional identifier policy using real LogMate domain evidence;
- cross-field date/time rules, especially flights crossing midnight/time zones;
- whether unmatched registrations can be accepted;
- actual normalization policy per imported/manual field.

### REJECT
- generic `Invalid`/`Required` as the whole message;
- blaming language;
- parser syntax presented as domain truth;
- clearing the form after errors;
- red-only error meaning;
- blind `Try again` after outcome uncertainty;
- shortening semantic repair information to satisfy preferred geometry.

---

## 12. Stage 2 implication

CD010 establishes a reusable forms/validation/error baseline and a three-strategy comparative practice with a defended provisional selection. It is meaningful Stage 2 evidence but **does not pass Stage 2**.

Next highest-value work should apply the same state/failure taxonomy to **empty/loading/pending/success/recovery systems**, then onboarding/progressive disclosure and voice/tone modulation before a later integrated Stage 2 capstone.

## OPEN

- real professional-domain form constraints from live LogMate/MintTap implementations;
- human evidence for label comprehension and repair success;
- actual browser/native focus and error-announcement behavior;
- screen-reader/voice/magnification outcomes;
- locale-specific translation quality;
- production string/instrumentation workflow;
- measurement of repeated error incidence and recovery.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Use CD010 failure taxonomy when defining validation timing, preservation, business-rule blocks and outcome-unknown recovery. Content cannot finalize `continue despite unmatched identifier` without Interaction/product truth.

### Web
CD010 provides canonical semantic error propositions and label/hint/error relationships for later browser transfer. Web should validate association, focus, error summary/local-error behavior, native validation conflicts, reflow and accessibility runtime behavior.

### Type
Use real CD010 labels/hints/errors as operational text-growth stress inputs; do not request semantic truncation as the first geometry fix.

### Color
Error identity must survive removal/transformation of authored hue; Color may reinforce severity/state after semantic classification.

## Evidence level

**AUTHORITATIVE SOURCE STUDY + STAGE-2 SYSTEM SYNTHESIS + THREE-STRATEGY PRACTICE + KEEP/REWORK/REJECT + CROSS-SPECIALIST TRANSFER PREPARATION. No human or production-runtime PASS is claimed.**
