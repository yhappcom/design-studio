# CD008 — Integrated Foundation Capstone: Professional Record Import and Duplicate Review

Status: **FOUNDATION CAPSTONE — INTEGRATED PRACTICE + CRITIQUE + EXECUTABLE STRUCTURAL AUDIT / NOT A HUMAN PASS CLAIM**  
Date: 2026-09-16

## Research question

Can the Content Design / UX Writing specialist integrate CD001–CD007 into one bounded professional-product workflow, produce materially different content architectures, reject attractive but semantically weak alternatives, defend one direction using explicit criteria, preserve peer-domain ownership boundaries, and create reproducible non-human checks without confusing those checks with user evidence?

This study is the Stage 1 integrated practice gate. It is not a live-product redesign and does not claim user comprehension, preference, task-time, screen-reader, localization-quality or production-platform results.

---

## 1. Fixed problem substrate

The capstone uses a bounded professional record-import workflow already established across Content studies and compatible with the studio's operational-logbook practice substrate.

Fixed product facts:

1. A user selects one or more source files.
2. The parser identifies candidate records.
3. Some records may match existing records, but the match is not certain enough to call them confirmed duplicates.
4. The user reviews possible duplicates before final import.
5. For a possible duplicate pair, the supported resolution choices are:
   - keep the existing record;
   - replace the existing record with the incoming record;
   - keep both records.
6. Final confirmation starts an import operation.
7. Import can be pending, authoritatively confirmed, authoritatively failed, or outcome-unknown.
8. Retry after outcome-unknown is not automatically safe; the prior outcome must be verified before another commit attempt.
9. English is the source language, but the content architecture must remain localization-ready.
10. No semantic distinction may depend only on color, icon, visual position or one input method.

The data/state model remains fixed across all alternatives. Only the content architecture changes.

---

## 2. Foundation requirements carried into the capstone

### CD001 — language is part of the product contract

Every important message must preserve:

`object → state → action → consequence`

The wording layer may not redefine the underlying system state.

### CD002 — concept before designation

The study keeps these concepts separate:

- source file;
- candidate record;
- possible duplicate;
- existing record;
- import operation;
- review decision;
- pending import;
- confirmed import;
- known failure;
- outcome unknown.

`Possible duplicate` is deliberately not collapsed into `duplicate` because certainty differs.

### CD003 — command labels represent the command contract

`Import {count} records` starts the commit. It does not claim that import is already complete.

`Try import again` is permitted only in a known-failure state where Interaction confirms retry safety.

### CD004 — minimum sufficient content

The target is not minimum character count. The target is the smallest amount of content that preserves the distinctions required for the next decision.

### CD005 — accessible/input-neutral language

No required instruction depends on:

- `click` or `tap` when the input method is incidental;
- left/right/above/below location;
- color alone;
- icon shape alone.

Visible action label and accessible name remain identical in the selected control artifact.

### CD006 — source and disciplinary boundaries

This study does not treat Content as owner of:

- parser/deduplication logic;
- retry safety;
- record state transitions;
- responsive geometry;
- font rendering;
- color encoding;
- browser/AT behavior.

Content expresses those contracts and records dependencies.

### CD007 — global English and localization readiness

The selected architecture uses complete semantic messages, semantic string IDs, variable definitions and localizer context. It avoids string concatenation, English pseudo-plurals and position-dependent references.

---

## 3. Three materially different content architectures

The three candidates intentionally solve the same workflow with different content-system strategies.

# Candidate A — Minimal Command Layer

### Strategy

Expose as little language as possible. Assume expert users infer most meaning from table context and visual structure.

Representative strings:

- heading: `Duplicates`
- summary: `12 found`
- row actions: `Keep` / `Replace` / `Both`
- commit: `Import`
- pending: `Working…`
- known failure: `Failed. Retry`
- outcome unknown: `Failed. Retry`

### KEEP

- low visual text volume;
- potentially compact in dense professional interfaces;
- fast to scan when context is already perfectly understood.

### REWORK

Almost every important term needs semantic expansion.

### REJECT for this fixed workflow

1. `Duplicates` overstates certainty.
2. `12 found` does not identify what was found.
3. `Keep` does not identify the object or whether existing/incoming data is preserved.
4. `Replace` is underspecified when two records are visible.
5. `Import` hides scope when the selected set matters.
6. `Working…` hides the actual operation.
7. `Failed. Retry` collapses known failure and outcome-unknown.
8. It encourages localization by isolated fragments rather than semantic propositions.

This candidate demonstrates **brevity-induced semantic debt**.

---

# Candidate B — Explanation-Heavy Guided Layer

### Strategy

Explain the workflow extensively so no important distinction is left implicit.

Representative structure:

- long introductory paragraph explaining parser uncertainty;
- each possible duplicate pair includes a multi-sentence explanation of the three choices;
- confirmation page restates selected files, parsed records, duplicate decisions and import behavior;
- pending and error states include detailed explanation before the next action.

Example heading and explanation:

`Review records that might already exist`

`The importer found records that appear similar to records already in your logbook. A match does not necessarily mean the records are the same. For each item, choose whether to keep the existing record, replace it with the incoming record, or keep both records before continuing.`

### KEEP

- high semantic fidelity;
- preserves uncertainty;
- gives a new user substantial context;
- makes hidden product assumptions explicit.

### REWORK

- separate durable explanation from immediate decision copy;
- move repeated choice definitions into point-of-need help where appropriate;
- shorten without removing uncertainty/scope.

### REJECT as the default architecture

The primary problem is **over-explanation**, not inaccuracy.

The user must repeatedly parse prose whose semantic payload is stable across rows. The content competes with the actual comparison task. Long source sentences also increase localization and layout burden.

This candidate demonstrates that **sufficiency can become excess**.

---

# Candidate C — State-and-Decision Architecture

### Strategy

Expose the real state and the next decision at each step. Keep repeated concepts stable, move detail to the point where it changes a decision, and separate command, pending, success, failure and outcome-unknown messages.

Selected control strings are stored in:

- `research/content/CD008-message-contract.json`

Core examples:

### Review state

Heading:

`Review possible duplicates`

Instruction:

`We found {count} records that may match existing records. Review them before import.`

Resolution choices:

- `Keep existing`
- `Replace existing`
- `Keep both`

### Commit

`Import {count} records`

This names the command and scope without claiming completion.

### Pending

`Importing {count} records…`

### Confirmed

`{count} records imported`

### Known failure

Status:

`Import failed.`

Recovery action, only when Interaction confirms retry safety:

`Try import again`

### Outcome unknown

Status:

`We couldn’t confirm whether the import finished.`

Next step:

`Check imported records before starting another import.`

### KEEP

- uncertainty is explicit where it matters;
- terminology is stable across states;
- actions represent actual command scope;
- command and completion are separated;
- known failure and outcome unknown stay distinct;
- required information appears near the decision it governs;
- visible and accessible action identity can remain aligned;
- semantic messages can localize as complete units.

### REWORK

- exact phrasing still requires product/audience testing;
- real expert-domain terminology needs live user/domain evidence;
- actual layout and narrow-width behavior require Layout/Web transfer;
- actual status announcement behavior requires implementation validation.

### CONDITIONAL LIMIT

If later research shows the audience already treats a shorter domain-native label as unambiguous, selected labels may be compacted without collapsing concept boundaries. That would be a later evidence-based revision, not a Foundation assumption.

---

## 4. Comparative criteria

Scores are **structured studio judgments**, not user-performance measurements.

Scale: 1 weak → 5 strong for this fixed exercise.

| Criterion | Weight | A Minimal | B Explanation-heavy | C State/decision |
|---|---:|---:|---:|---:|
| semantic fidelity | 5 | 2 | 5 | 5 |
| concept consistency | 4 | 2 | 4 | 5 |
| action/consequence clarity | 5 | 1 | 4 | 5 |
| minimum-sufficient information | 4 | 2 | 2 | 5 |
| accessibility/input-neutrality | 4 | 3 | 4 | 5 |
| localization readiness | 4 | 1 | 3 | 5 |
| expert-domain precision | 3 | 2 | 4 | 4 |
| cross-domain implementation fit | 3 | 3 | 3 | 4 |

Maximum weighted total: **160**.

- A Minimal Command: **62**
- B Explanation-heavy: **118**
- C State-and-Decision: **154**

The calculation is reproduced by `CD008-audit.py`.

### Selection

**Candidate C is retained as the Foundation control architecture for this fixed problem.**

This selection is not based on taste or character count. C preserves the interaction contract while minimizing avoidable explanatory load and keeping the strings structurally localizable.

The score does not prove that users will prefer C or complete tasks faster with it.

---

## 5. Machine-readable selected contract

`CD008-message-contract.json` records each high-value string with:

- stable semantic ID;
- role;
- concept;
- state;
- source-English text;
- scope;
- consequence;
- localizer context;
- accessible-name relationship;
- named variables.

This demonstrates that Content Design can move from prose advice to a bounded inspectable content contract.

Important distinction:

> the JSON is a **Content specification**, not a production localization schema or final app string format.

Production framework/string-catalog integration belongs to later stages and platform-specific implementation.

---

## 6. Reproducible non-human audit

Canonical files:

- `CD008-message-contract.json`
- `CD008-audit.py`
- `CD008-audit-results.json`

The audit checks only bounded structural conditions:

1. required content-contract metadata exists;
2. IDs are unique;
3. action visible label and accessible name do not drift;
4. selected English strings do not use `(s)` pseudo-plural syntax;
5. required wording does not depend on common color words;
6. required wording does not depend on left/right/above/below references;
7. input-independent actions do not use `click`/`tap` language;
8. outcome-unknown messages do not expose direct retry wording;
9. variables used in source text have definitions;
10. comparative-score arithmetic is reproducible.

Executed result:

- structural findings: **0**;
- candidate totals: **62 / 118 / 154**;
- selected structured-studio candidate: **C**;
- process exit: **0**.

### Evidence boundary

This executable audit proves only that the selected artifact satisfies the encoded structural rules and arithmetic.

It does **not** prove:

- comprehension;
- findability;
- correct expert terminology recognition;
- task success;
- task time;
- error rate;
- trust;
- preference;
- screen-reader announcement quality;
- translation quality;
- cultural appropriateness;
- real narrow-layout fit;
- production integration.

---

## 7. Combined CD001–CD007 audit

### CD001 semantic fidelity

PASS for the bounded specification:

- possible duplicate ≠ confirmed duplicate;
- pending ≠ confirmed;
- known failure ≠ outcome unknown;
- command ≠ completion.

Human understanding: OPEN.

### CD002 terminology architecture

PASS for bounded internal consistency:

- `record`, `possible duplicate`, `existing`, `import` retain stable concept mapping;
- different resolution actions use different designations;
- internal implementation terms are not exposed.

Expert audience vocabulary recognition: OPEN.

### CD003 action labels

PASS for bounded command-contract fidelity:

- commit action names object/scope;
- completion is not pre-announced;
- retry is conditional on Interaction safety;
- outcome-unknown has verification-first language.

Behavioral retry implementation: DEPENDENCY / OPEN.

### CD004 minimum-sufficient information

Candidate A fails by omission. Candidate B fails by excess. Candidate C is the bounded control because it preserves required decision facts with lower explanatory load.

Human scan/comprehension advantage: OPEN.

### CD005 accessibility/input-neutral language

The selected contract avoids required color/location/input-method references and aligns visible/accessibility action names in the bounded artifact.

Actual AT, keyboard, touch, magnification and low-vision outcomes: OPEN.

### CD006 ownership/source literacy

The capstone explicitly escalates rather than copy-fixing these peer-owned questions:

- deduplication certainty;
- retry safety;
- asynchronous state truth;
- typography defects;
- layout fit;
- browser/AT delivery.

### CD007 localization readiness

The selected contract uses:

- complete message units;
- semantic IDs;
- explicit variables;
- localizer context;
- no pseudo-plural syntax;
- no English-fragment concatenation in the content specification;
- no position-dependent semantics.

Locale-specific quality: OPEN.

---

## 8. RELATED DOMAIN CHECK

### Type

Current Type status: T021 bounded operational build is executable and reaches 36/36 bounded cmap coverage, but the coherent-family **drawing gate is FAIL / REWORK**.

Content consequence:

- do not shorten or rename necessary workflow strings to compensate for a Type drawing defect;
- actual selected strings become future Type/geometry stress inputs;
- no custom Type candidate is promoted by this study.

Relationship: **DIRECT DEPENDENCY + CONTRADICTION-RESILIENT HANDOFF**.

### Color

Color Stage 2 is PASS and already establishes that semantic state must survive palette transformation.

Content consequence:

- pending/failure/unknown/confirmed states have explicit textual identity;
- wording does not refer to color as the primary identifier.

Relationship: **REUSE**.

### Layout / Interaction

L009 supplies an integrated professional logbook workflow precedent. I002 supplies the authoritative distinction among accepted, pending, confirmed, failed and outcome-unknown plus the rule that retry safety depends on operation semantics.

Content consequence:

- `Try import again` is conditional on known-safe retry;
- no direct retry exists in outcome-unknown;
- Content does not redefine deduplication or operation identity.

Relationship: **DIRECT REUSE + INTEGRATED TRANSFER**.

### Web

W017 shows that visible labels, programmatic names, disclosure state and icon appearance are separate implementation contracts and that bounded Chromium validation does not equal screen-reader or cross-browser evidence.

Content consequence:

- the selected message contract is ready for later Web transfer;
- actual status announcements, reflow, zoom, localization, RTL and AT behavior remain Web/implementation validation work.

Relationship: **FUTURE TRANSFER VALIDATION**.

### Existing Content

CD001–CD007 are integrated rather than repeated independently. This capstone is **INTEGRATED PRACTICE + REPLICATION OF STRUCTURAL AUDITS + CROSS-DOMAIN TRANSFER**.

---

## 9. Failure modes exposed by the capstone

### 9.1 Shorter can be less truthful

`Duplicates` and `Failed. Retry` are shorter than the selected architecture but collapse uncertainty and operation state.

### 9.2 More explanation can be worse information design

Candidate B preserves more facts but forces repeated reading and moves stable background explanation into the decision path.

### 9.3 Copy can expose a product-contract defect

If product engineering cannot distinguish known failure from outcome unknown, Content cannot solve that with more polished wording.

### 9.4 Localization can expose hidden English assumptions

Fragmented strings and pseudo-plurals are not merely translator inconvenience; they reveal that English grammar has leaked into product architecture.

### 9.5 Accessibility language cannot repair behavior

A correct label is not proof that focus, status announcement, keyboard activation or screen-reader output is correct.

### 9.6 Layout pressure cannot redefine semantics

If `Review possible duplicates` does not fit a chosen component width, the first response is not to relabel uncertain records as `Duplicates`.

---

## 10. Project-readiness answers

### When should this knowledge be used?

Use the integrated method for consequential workflows where terminology, action scope, asynchronous state, recovery, accessibility and localization interact.

### When should it not be used mechanically?

Do not apply the full artifact/metadata burden to trivial low-risk strings where the distinction adds no decision value.

### Required inputs

- actual objects/concepts;
- state machine;
- available actions;
- persistence/commitment behavior;
- failure/unknown/retry semantics;
- audience/domain terminology evidence;
- supported platforms/localization plan.

### Concrete decisions it can change

- terminology;
- action labels;
- state-message separation;
- information order;
- whether helper text is necessary;
- whether a string may be reused;
- whether translation units need distinct keys/context;
- whether a problem must be escalated to Interaction/Layout/Web/Type.

### Main failure modes

- concept collision;
- false completion;
- unsafe retry language;
- insufficient scope;
- explanation overload;
- sensory/input lock;
- localization-hostile fragments;
- geometry-driven semantic truncation;
- expert critique mislabeled as user evidence.

### Validation path

1. non-human semantic/structural audit;
2. implementation transfer in platform/browser/native UI;
3. localization/RTL/string-growth transfer where relevant;
4. domain-expert terminology review;
5. human comprehension/task testing when the live project is ready.

---

## 11. HANDOFFS TO OTHER SPECIALISTS

### Type

Use the selected CD008 strings as a future real-content corpus. Do not shorten them solely to make an unstable custom family look better. Current T021 drawing defects remain Type-owned.

### Color

The four commit outcomes — pending, confirmed, known failure, outcome unknown — now have explicit verbal identity that Color can reinforce without owning the meaning.

### Layout / Interaction

The Content architecture depends on preserving visible comparison context, review state and retry policy. Any later Interaction change to dedupe certainty or retry safety requires the affected strings to be re-audited.

### Web

Transfer `CD008-message-contract.json` into an actual page/component specimen later. Validate:

- semantic HTML/control type;
- label/name mapping;
- dynamic status delivery;
- narrow reflow;
- zoom/text enlargement;
- string growth;
- language metadata/RTL;
- keyboard/focus behavior;
- real asynchronous transition behavior.

### User Research / Human Factors

Later live-product testing should separate at least:

- terminology recognition;
- state comprehension;
- action-consequence prediction;
- duplicate-resolution accuracy;
- recovery decision quality;
- task time/error rate.

Do not reduce these to one generic preference test.

---

## 12. Capstone verdict

CD008 demonstrates that the Foundation principles can be integrated into one professional-product content system rather than repeated as isolated writing rules.

Evidence now includes:

- a fixed workflow substrate;
- three materially different content architectures;
- explicit KEEP / REWORK / REJECT critique;
- defended selection using fixed criteria;
- machine-readable selected message contract;
- executable structural lint;
- reproducible arithmetic;
- peer-domain dependencies and handoffs;
- explicit human/implementation/localization evidence limits.

CD008 therefore materially closes the **integrated Foundation authorship** gap.

It does **not** itself declare Stage 1 PASS. The next correct action is CD009 — a separate closure audit against the exact Foundation requirements and evidence boundary.
