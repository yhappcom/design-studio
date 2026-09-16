# CD010 — Stage 2 Entry Audit + Forms / Validation / Error System Baseline

Status: **STAGE 2 ENTRY — SOURCE STUDY + GAP AUDIT + ORIGINAL FORM-SYSTEM PRACTICE / STAGE 2 NOT PASSED**  
Date: 2026-09-16

## Research question

What genuinely new professional-practice evidence is required after Foundation PASS, and how should Content Design structure form questions, labels, hints, constraints, validation and error/recovery messages as one system rather than a collection of field-level microcopy tricks?

CD009 passed Stage 1. CD010 therefore does not repeat Foundation theory. It audits Stage 2 gaps and begins with forms/validation because this surface combines terminology, user questions, instructions, error prevention, recovery, accessibility, localization and Interaction dependencies.

---

## 1. Stage 2 entry audit

| Stage 2 area | Existing evidence | Current state |
|---|---|---|
| buttons/action labels | strong Foundation evidence in CD003/CD008 | **BRIDGE / MORE SURFACE PRACTICE NEEDED** |
| forms/questions/labels/helper text | only partial Foundation examples | **NEW MAJOR GAP** |
| validation/error/warning/success/confirmation | state semantics exist; no systematic form pattern practice | **NEW MAJOR GAP** |
| loading/pending/offline/recovery | strong Interaction dependency + CD008 wording | **BRIDGE / SYSTEM PRACTICE NEEDED** |
| onboarding | little direct evidence | **OPEN** |
| empty states | little direct evidence | **OPEN** |
| search/filter/settings content | terminology knowledge exists; surface patterns not practiced | **OPEN** |
| voice/tone systems | not yet systematized | **OPEN** |
| localization-ready patterns | strong Foundation architecture | **BRIDGE / REPEATED PATTERN PRACTICE NEEDED** |
| multiple solutions + defended selection | strong method from CD008 | **SUPPORTED FOR ENTRY** |
| design/engineering/research collaboration | boundary discipline established | **SUPPORTED FOR ENTRY; PRODUCTION PRACTICE OPEN** |

Verdict: Stage 2 entry is justified, but Stage 2 is clearly **NOT PASSED**.

Highest-value first gap: **forms + validation + error recovery**.

---

## 2. Sources

### SOURCE — GOV.UK Design System: error messages explain what went wrong and how to fix it

Current GOV.UK Design System guidance distinguishes validation errors from eligibility, permission or service problems. A validation error is appropriate when the user supplied information the service cannot use and can correct. Eligibility/service-state problems should be explained as different product states rather than mislabeled field errors.

GOV.UK also recommends:
- preserving entered values when redisplaying a form;
- placing a specific message near the affected field;
- keeping field and summary error wording consistent;
- using language from the question/label to make the relationship clear;
- avoiding vague messages such as `An error occurred`, `Answer the question` or `This field is required`;
- stating what happened and/or what the user needs to change.

Sources:
- GOV.UK Design System — Error message  
  https://design-system.service.gov.uk/components/error-message/
- GOV.UK Design System — Recover from validation errors  
  https://design-system.service.gov.uk/patterns/validation/
- GOV.UK Design System — Error summary  
  https://design-system.service.gov.uk/components/error-summary/

### SOURCE — W3C/WAI: controls need labels/instructions and detected errors need textual identification

W3C/WAI form guidance requires controls to have labels that identify their purpose and requires instructions where users need format, requirement or other input guidance.

The WAI forms guidance also states:
- placeholder text is not a replacement for a label;
- instructions must remain available rather than disappear as the user types;
- input errors need text descriptions;
- known correction suggestions should be provided when appropriate;
- consequential data/legal/financial actions require stronger prevention/review/correction mechanisms under WCAG.

Sources:
- W3C WAI — Labeling Controls  
  https://www.w3.org/WAI/tutorials/forms/labels/
- W3C WAI — Form Instructions  
  https://www.w3.org/WAI/tutorials/forms/instructions/
- W3C WAI — Validating Input  
  https://www.w3.org/WAI/tutorials/forms/validation/
- WCAG input-assistance criteria indexed by WAI  
  https://www.w3.org/WAI/standards-guidelines/act/rules/

### SOURCE — Apple: validation and field design must fit expected input

Apple's current Text Fields guidance recommends matching field presentation to expected input and validating fields when the allowed value requires it.

Source:
- Apple HIG — Text fields  
  https://developer.apple.com/design/human-interface-guidelines/text-fields

### Evidence caution

GOV.UK's exact implementation pattern — such as page-level error summary behavior or when its service standard validates — is strong service-design precedent, not a universal mobile/native law.

W3C success criteria provide accessibility requirements, but a technically conforming label/error implementation still does not prove human comprehension.

---

## 3. Form content is a contract, not five independent strings

For each meaningful field/question, CD010 introduces this provisional content contract:

1. **Concept/purpose** — what product fact is being collected and why?
2. **Question/label** — what stable name or question identifies the input?
3. **Accepted input** — what values/formats can the product actually use?
4. **Required/optional state** — must a value be supplied for this task?
5. **Hint/instruction** — what must be known before input that is not obvious from the label?
6. **Example** — only when an example clarifies the expected format without becoming the sole instruction.
7. **Validation trigger** — when does the product decide an answer is unusable?
8. **Error category** — missing, ambiguous, impossible, unsupported format, out-of-range, conflict, etc.
9. **Error message** — what specifically needs correction?
10. **Preservation/recovery** — what entered value remains and what can the user change?
11. **Programmatic relationship** — label/instruction/error/status delivery belongs to implementation but Content must specify the semantic relationships.
12. **Localization context** — concept, variables, format rules and constraints must be understandable outside English source context.

This is a Content specification model, not a UI layout prescription.

---

## 4. Question / label / hint / placeholder / error are different roles

### Question or label

Identifies what input means.

Examples:
- `Aircraft registration`
- `Block time`

The stable label should survive after the user enters a value.

### Hint / instruction

Provides information needed before answering that the label does not already communicate.

Example:
- `Enter time as HH:MM or decimal hours.`

This example is a controlled professional-form specimen, not a universal LogMate production decision.

### Placeholder

May illustrate input but must not carry the only label/instruction because it disappears during editing and is not a reliable label substitute.

### Error

Appears after the product identifies a specific unusable input. It should reference the affected concept and the actual correction condition.

### Status

Reports system processing/completion state. A form field validation error and an asynchronous submission status are separate semantic roles.

---

## 5. Prevent avoidable errors before writing better error messages

### SOURCE TRANSFER — GOV.UK

Validation guidance emphasizes accepting harmless input variation where possible instead of creating unnecessary correction work.

### SYNTHESIS

Before writing an error message, ask:

1. Can the parser safely normalize the input?
2. Can the control constrain impossible choices?
3. Can a format requirement be explained before entry?
4. Is the field actually necessary?
5. Is the product rejecting a value for an internal implementation convenience rather than a user/domain requirement?

### STUDIO JUDGMENT

Content Design should treat repeated avoidable errors as a product/form-design signal, not merely as an opportunity to improve copy.

A polished error is not success if the product could have accepted or prevented the condition safely.

---

## 6. Validation error vs product/service state

### Validation error

Use when:
- the user provided missing, impossible, unsupported or too-ambiguous input;
- changing the answer can resolve the problem.

Examples:
- missing required identifier;
- impossible date value;
- time format the parser cannot interpret;
- mutually incompatible choices.

### Not a validation error

Do not present as field blame when:
- server/service is unavailable;
- permission is missing;
- user is ineligible;
- authoritative data conflicts externally;
- submission outcome is unknown;
- the product cannot currently complete the operation for a system reason.

These require state/recovery design with Interaction.

### Foundation transfer

This extends CD001/CD003:

> Error wording must not rewrite a service/system state into a user-input failure merely because the message appears near a form.

---

## 7. Error-message model

CD010 introduces a provisional error diagnostic:

`affected concept → observed problem/constraint → correction path`

Not every error needs all three written as separate clauses, but the user must be able to identify what needs changing.

### Weak

`Invalid value`

Failures:
- no concept;
- no reason;
- no repair path;
- uses internal validation language.

### Better for missing input

`Enter aircraft registration`

### Better for unsupported format

`Enter block time as HH:MM or decimal hours`

### Better for bounded value

`Block time must be greater than 0`

These are semantic specimens. Exact domain constraints must come from the product/domain contract.

---

## 8. Validation timing is an Interaction + research question

GOV.UK generally validates after the user tries to continue, while recognizing bounded exceptions such as character counts where earlier feedback can prevent wasted effort.

CD010 does not universalize that implementation rule.

### STUDIO JUDGMENT

Classify validation timing:

- **pre-entry constraint** — instruction/control prevents impossible input;
- **during-entry assistance** — only when immediate feedback is genuinely useful and accessible;
- **on field completion** — context-dependent;
- **on step submit/continue** — appropriate for many form checks;
- **server/authoritative validation** — required when only authoritative systems know the answer.

Content owns the messages/instructions for the chosen timing. Interaction owns the behavioral trigger. User Research should validate contentious timing decisions when stakes/complexity justify it.

---

## 9. Preserve entered information through recoverable validation

A correction loop should normally preserve usable information rather than erase the form and force re-entry.

Content consequence:
- error messages should refer to the value/field the user can still see and edit;
- don't design recovery copy around a form that silently discards valid answers unless loss is technically unavoidable and explicitly handled;
- repeated re-entry burden may indicate an Interaction/implementation defect.

This transfers directly from GOV.UK validation precedent and the studio's broader preserved-intention/recovery work.

---

## 10. Original practice — three form-content systems

Controlled substrate: a professional operational-record form with fields such as identifier/registration and duration. Exact final product terminology/constraints remain subject to live project/domain evidence.

### Candidate A — Placeholder-Led Compact Form

Pattern:
- field has no stable visible label;
- placeholder carries example/meaning;
- validation appears while typing;
- errors use generic `Invalid` / `Required`;
- red outline is the main error signal.

Example:

`[N12345]`  
error: `Invalid`

#### KEEP
- visually compact;
- low initial text density.

#### REJECT
- placeholder becomes an unstable label;
- generic error does not identify correction;
- meaning degrades once text is entered;
- color risks carrying too much state meaning;
- premature validation can interrupt input without evidence;
- localization context is weak.

Verdict: **REJECT**.

---

### Candidate B — Rule-Heavy Instruction Form

Pattern:
- visible labels;
- long rules paragraph before the form;
- every field repeats allowed formats and conditions;
- error messages restate full policy.

Example:

`Block time`

`Block time must be entered using hours and minutes separated by a colon or as a decimal number of hours, must be greater than zero, and must not contain alphabetic characters.`

#### KEEP
- semantically explicit;
- lower risk of hidden rule.

#### REWORK
- separates instructions from the exact field moment;
- repeats rules whether relevant or not;
- high reading/localization/layout burden;
- can obscure the primary question.

Verdict: **REWORK / NOT DEFAULT**.

---

### Candidate C — Stable Label + Point-of-Need Constraint + Specific Recovery

Pattern:
- stable visible label/question;
- concise hint only for information needed before entry;
- example separated from concept label;
- validation waits for an appropriate Interaction trigger;
- existing values remain visible;
- specific error describes the repair condition;
- error meaning survives without color;
- source string/localizer context is explicit.

Example control:

Label:
`Block time`

Hint:
`Enter HH:MM or decimal hours.`

Missing error:
`Enter block time`

Unsupported-format error:
`Enter block time as HH:MM or decimal hours`

Bounded-value error, only if the domain contract requires it:
`Block time must be greater than 0`

#### KEEP
- roles do not collapse;
- constraint is available before correction is needed;
- recovery message is specific;
- visible label persists;
- localization units are complete;
- does not assume color/input method.

#### REWORK
- exact accepted formats and constraints must come from product/domain truth;
- actual control/input type and validation timing need Interaction/platform validation;
- actual expert wording needs domain/user evidence.

Verdict: **KEEP AS STAGE 2 BASELINE CONTROL**.

---

## 11. Forms/content audit v0.1

For each field/question, check:

### Purpose / necessity
- `UNJUSTIFIED FIELD`
- `INTERNAL-DATA REQUEST`
- `CONCEPT COLLISION`

### Label/question
- `MISSING STABLE LABEL`
- `AMBIGUOUS QUESTION`
- `INTERNAL TERMINOLOGY`
- `LABEL/ACCESSIBLE-NAME DRIFT`

### Instruction
- `RULE ONLY IN PLACEHOLDER`
- `LATE REQUIRED CONSTRAINT`
- `DUPLICATED RULE`
- `EXAMPLE WITHOUT RULE`
- `SENSORY/INPUT LOCK`

### Validation
- `AVOIDABLE REJECTION`
- `PREMATURE VALIDATION NEEDS EVIDENCE`
- `CLIENT/SERVER RULE CONFLICT DEPENDENCY`
- `USER-CORRECTABLE VS SERVICE-STATE CONFUSION`

### Error
- `GENERIC ERROR`
- `MISSING AFFECTED CONCEPT`
- `NO CORRECTION PATH`
- `USER BLAME`
- `INTERNAL ERROR CODE/JARGON`
- `COLOR-ONLY ERROR`

### Recovery
- `INPUT LOSS`
- `UNSAFE RETRY`
- `STATE COLLAPSE`

### Localization / implementation
- `FRAGMENTED MESSAGE`
- `MISSING VARIABLE/LOCALIZER CONTEXT`
- `HARD-CODED FORMAT`
- `RUNTIME LABEL/ERROR ASSOCIATION NEEDED`
- `AT/HUMAN VALIDATION NEEDED`

The audit can identify structural/content risks. It cannot prove task completion or human comprehension.

---

## 12. RELATED DOMAIN CHECK

### Type

Current T021 custom candidate fails its drawing gate. Form labels/hints/errors should not be shortened to disguise font deficiencies. Form strings become future text-growth/rendering stress inputs.

Relationship: **DEPENDENCY + FUTURE TRANSFER**.

### Color

Error state cannot be communicated by red alone. Color reinforces validation state after the semantic error contract is established.

Relationship: **DIRECT REUSE**.

### Layout / Interaction

Interaction owns:
- validation timing;
- focus movement;
- preservation of input/draft;
- whether a field/control prevents impossible states;
- server/client validation behavior;
- submission/retry/recovery.

Content owns:
- question/label language;
- constraint explanation;
- field-specific error language;
- error-state terminology;
- ordering of instructions/recovery information.

Relationship: **DIRECT DEPENDENCY**.

### Web

Web must later transfer this baseline into actual native controls/HTML relationships, error association, focus/error-summary behavior, zoom/reflow, browser validation policy and AT behavior.

GOV.UK's error-summary implementation is a useful web precedent but is not declared mandatory for every mobile/native form.

Relationship: **FUTURE TRANSFER VALIDATION**.

### Existing Content

CD010 extends rather than repeats Foundation:
- CD002 supplies concept/terminology;
- CD004 supplies minimum-sufficient information;
- CD005 supplies input-neutral/accessibility language;
- CD007 supplies localization-ready architecture;
- CD008 supplies integrated audit discipline.

Overlap classification: **STAGE-2 EXTENSION + PATTERN BASELINE + TRANSFER PREPARATION**.

---

## 13. Evidence boundary

CD010 establishes:
- Stage 2 gap map;
- form-content role separation;
- validation-error vs service-state distinction;
- error-prevention-before-error-copy principle;
- provisional form field content contract;
- provisional form/error audit;
- three competing form-content systems with critique;
- Candidate C as baseline control.

CD010 does NOT establish:
- best validation timing for all tasks;
- universal required/optional marker convention;
- production mobile/web form implementation;
- actual screen-reader behavior;
- actual domain-user recognition of terms;
- measured recovery rate;
- measured form completion/error rate;
- production localization quality.

---

## 14. Stage 2 implication

Stage 2 is now **PRACTICE / NOT PASSED**.

Highest-value next Content work should continue in larger blocks rather than micro-studies:

1. deepen forms into multi-field validation, review/confirmation and consequential edits;
2. integrate error + warning + service failure + outcome-unknown patterns without collapsing them;
3. then cover empty/loading/pending/success systems and onboarding/progressive disclosure;
4. build voice/tone only after state/functional language remains stable;
5. preserve global-English/localization readiness throughout;
6. later produce materially different complete Stage 2 content systems and run a closure audit.

Recommended next study: **CD011 — Error / Warning / Service Failure / Recovery State Taxonomy and Comparative Practice**.

## Latest checkpoint

- Stage 1: **PASS**.
- CD010 Stage 2 entry audit: **EXECUTED**.
- Forms/validation/error baseline: **EXECUTED**.
- Stage 2: **PRACTICE / NOT PASSED**.
- Human validation: **NOT CLAIMED**.
- Next Content ID: **CD011**.
