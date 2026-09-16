# Content Design / UX Writing Specialist Status

Operating state: **ACTIVE — STAGE 1 FOUNDATION / CD001–CD005 EXECUTED / CD006 NEXT**  
Governance activation: 2026-09-16  
Primary path: `research/content/`  
Study prefix: `CD###`  
Next new-study ID: `CD006`

## Current level

Stage 1 — Foundations: **IN STUDY / PRACTICE — NOT PASSED**  
Stage 2 — Intermediate Professional Practice: **NOT STARTED**  
Stage 3 — Advanced / Systems Practice: **NOT STARTED**  
Stage 4 — Production & Authorship: **NOT STARTED**  
Stage 5 — Research & Advisory: **NOT STARTED**

Content Design progresses deliberately from fundamentals to expert/research-advisory practice. No stage may be skipped because later project work appears more immediately useful.

## Canonical role

Content Design owns the user-facing semantic and linguistic interface: terminology, naming, action labels, questions, instructions, state/recovery messaging, voice/tone, plain language, accessibility-oriented language, localization-ready content systems and content governance.

It does not own font/rendering mechanics, visual color encoding, spatial composition, interaction state machines or complete web page/browser architecture. Those remain with Type, Color, Layout/Interaction and Web respectively.

## Stage 1 Foundation target

Foundation begins with principles rather than microcopy recipes:

1. content design vs adjacent disciplines;
2. language as interface material;
3. user needs, user language and mental models;
4. terminology/naming/concept consistency;
5. action-state-consequence semantics;
6. plain language and cognitive load;
7. scanning, information order and front-loading;
8. clarity vs brevity vs necessary detail;
9. accessible and input-neutral wording;
10. source literacy, precedent/history and basic research/critique method;
11. original exercises with explicit KEEP / REWORK / REJECT rationale;
12. cross-specialist reuse and dependency reasoning.

Reading or collecting style-guide rules does not satisfy the Foundation gate.

## CD001 — language as interface

Canonical: `research/content/CD001-language-as-interface-foundations.md`

Key result:

> Content is part of the product contract, not a decorative string layer. Before optimizing tone or brevity, verify semantic fidelity to the real object, state, available action and consequence.

Diagnostic: **Object → State → Action → Consequence**.

A controlled ambiguous network-outcome exercise rejected shorter wording that falsely asserted failure and encouraged unsafe retry. Human comprehension/preference was not claimed.

## CD002 — user needs, mental models, terminology and naming

Canonical: `research/content/CD002-user-needs-mental-models-terminology-naming.md`

Key results:
- user needs are task/outcome based, not proposed features;
- “mental model” is not accepted as an intuition shortcut;
- concept and designation are separate;
- same concept/function should normally preserve a stable designation;
- different concepts remain distinct when action, consequence, persistence, recovery or interpretation differs;
- domain-native expert vocabulary may be preferable to generic simplification when audience/task evidence supports it;
- internal implementation terms and product-created neologisms require explicit justification.

Terminology audit v0.1 flags concept collision, drift, internalism and evidence/localization needs without pretending to measure comprehension.

## CD003 — action labels, command grammar and consequence clarity

Canonical: `research/content/CD003-action-labels-command-grammar-consequence-clarity.md`

Key result:

> **Label wording must reflect the real command contract when persistence, commitment, object scope, destructive consequence or temporal outcome changes.**

CD003 separates command, object/scope, immediate behavior, persistence, outcome state and recoverability.

Current rules include:
- specificity rises when scope/persistence/commitment/destructive consequence matters;
- `Save`, `Submit`, `Publish`, `Delete`, `Remove`, `Archive`, `Retry` are not interchangeable by default;
- an action label describes what the user initiates/authorizes, not an unconfirmed completed outcome;
- `Retry` requires Interaction evidence that retry is behaviorally safe;
- visible and accessible control identity should remain aligned.

Original practice rejected false persistence, hidden deletion scope and premature completion wording.

## CD004 — plain language, scanning, information order and sufficiency

Canonical: `research/content/CD004-plain-language-scanning-information-order-sufficiency.md`

Key results:
- plain language is task-oriented information design, not merely short words/sentences;
- clarity, brevity and sufficiency are distinct variables;
- readability scores are lint signals, not comprehension evidence;
- front-load information that changes the next decision;
- chunk by semantic purpose rather than arbitrary length;
- distinguish required-before-action, point-of-need and background information;
- preserve precise expert-domain vocabulary when genuinely audience-native while simplifying surrounding language/structure.

Current rule:

> **Optimize for minimum sufficient content, not minimum character count.**

Original practice separated brevity-induced omission, sufficient-but-poorly-ordered prose and a minimum-sufficient structured candidate.

Information-sufficiency audit v0.1 flags missing object/state/action/consequence/condition/scope, late task facts, generic headings, internal jargon, false simplification and human/localization evidence needs.

## CD005 — accessible, input-neutral language and non-visual reference

Canonical: `research/content/CD005-accessible-input-neutral-language-nonvisual-reference.md`

CD005 establishes the language-side accessibility contract without claiming that wording alone makes an implementation accessible.

### Key source-grounded results

- instructions must not rely solely on sensory characteristics such as color, shape, size, visual position, orientation or sound;
- color cannot be the only way semantic state/action is communicated;
- input-neutral wording is appropriate when the physical input method is incidental, while modality-specific wording is correct when the modality itself is what is being taught;
- visible control label and accessible/programmatic name should preserve the same command identity;
- input fields require stable labels/instructions where needed;
- status-message wording and programmatic status delivery are separate contracts.

### Foundation model

Preferred reference order:

**semantic label/name → role/object → state → optional sensory/location cue**

Current rule:

> **Use input-neutral language for input-independent tasks; use modality-specific language when modality-specific behavior is genuinely the subject.**

Content now explicitly separates:
- control/object name;
- description;
- instruction;
- status;
- error/recovery message.

Hidden accessibility text must not create a second terminology system or expose internal vocabulary.

### Original practice

- `Click the blue button on the right` — **REJECT** for pointer/color/location lock;
- `Select Review duplicates` — **KEEP AS SEMANTIC CONTROL**;
- generic wording for a genuinely touch-specific gesture — **REJECT / INSUFFICIENT**;
- touch-specific gesture instruction — **KEEP FOR THAT MODALITY-SPECIFIC CONTEXT**;
- visible `Import 121 records` vs hidden `Commit batch` — **REJECT** for label/name drift and internal-name leakage.

### Accessibility-language audit v0.1

Can flag:
- `SENSORY-ONLY REFERENCE`;
- `LOCATION-LOCK`;
- `COLOR-LOCK`;
- `ICON-ONLY SEMANTICS`;
- `INPUT-METHOD LOCK`;
- `FALSE INPUT NEUTRALITY`;
- `LABEL-NAME DRIFT`;
- `INTERNAL NAME LEAK`;
- `NAME-DESCRIPTION COLLAPSE`;
- `MISSING INPUT LABEL`;
- `LATE REQUIRED RULE`;
- `STATUS DELIVERY DEPENDENCY`;
- `COLOR-ONLY ERROR`;
- browser/AT/voice/keyboard/touch/forced-colors/zoom/localization validation needs.

It cannot prove screen-reader announcement quality, speech recognition success, keyboard/touch operability, low-vision findability, cognitive accessibility outcomes or disabled-user task performance.

## Cross-specialist state after CD005

### Type
Necessary labels/instructions/status messages remain actual rendering stress content. Enlargement/wrapping pressure is not permission to delete visible semantic identity.

### Color
Content removes color from sole semantic ownership. Color can reinforce state, but wording/state identity must survive alternate themes and forced colors.

### Layout / Interaction
Responsive position is not a stable semantic identifier. Interaction owns actual modality/state/focus/recovery behavior; Content chooses input-neutral or modality-specific wording from that contract.

### Web
W017 directly supports CD005’s separation of icon appearance, semantic name, visible label and runtime accessibility behavior. Future Web transfer should validate label/name, status delivery, field labeling and zoom/reflow under actual browser conditions. W017 remains bounded Chromium evidence, not AT-user evidence.

## Evidence boundary

Current Content evidence includes:
- authoritative/primary source study;
- historical/contemporary HCI conceptual evidence;
- controlled empirical evidence from adjacent communication domains;
- direct cross-specialist reuse/transfer;
- five original structured practice blocks;
- terminology, command, information-sufficiency and accessibility-language audits.

NOT established yet:
- human comprehension/findability/task completion;
- terminology recall;
- action-label speed/error effects;
- trust/confidence effects;
- actual expert-domain vocabulary recognition;
- Korean information-order/action-language/input-neutral terminology behavior;
- Korean↔English semantic equivalence;
- actual screen-reader/voice/magnification/disabled-user outcomes;
- production string-governance behavior;
- live-project improvement.

## Active next queue

1. **CD006 — Content Design / UX Writing history, disciplinary boundaries and precedent/source literacy.** Map the field’s lineage through editorial practice, technical communication, information architecture, content strategy, service design and HCI; distinguish documented history from modern job-title branding; clarify what methods/ownership Content Design inherits and what remains adjacent-domain work.
2. **CD007 — Korean-language / bilingual Foundation transfer.** Study Korean plain-language, information-order, action-label and professional-domain terminology evidence without literal English-rule translation.
3. Execute an integrated Foundation exercise that applies CD001–CD005 together to one bounded product workflow and preserves peer-domain dependencies.
4. Extend reproducible checks only where they validate known semantic structure; do not convert formulas/model output into human evidence.
5. Run the Stage 1 gap/closure audit only after history/source literacy, Korean transfer and integrated practice are credible.
6. Begin Stage 2 forms/errors/onboarding/empty states/voice-tone work only after Foundation PASS.

## OPEN / dependencies

- documented Content Design / UX Writing history and disciplinary lineage;
- stronger Korean-language authoritative/empirical evidence;
- Korean input-neutral/action-label conventions;
- expert-domain abbreviation and terminology elicitation;
- terminology governance for professional-domain products;
- appropriate human methods separating findability, comprehension, recall and actionability;
- progressive-disclosure validation where omission cost is asymmetric;
- accessible-description/status-delivery collaboration with Web/Interaction;
- later human testing protocol once live projects support it.

## Latest checkpoint

- Specialist approved: **YES**.
- Canonical path/status: **ACTIVE**.
- Five-stage progression: **DEFINED**.
- CD001: **EXECUTED** — language-as-interface semantic contract.
- CD002: **EXECUTED** — user needs, mental-model caution and terminology architecture.
- CD003: **EXECUTED** — command semantics and consequence clarity.
- CD004: **EXECUTED** — plain language, scanning, information order and minimum-sufficient content.
- CD005: **EXECUTED** — accessible/input-neutral language and non-visual reference.
- Original practice/critique blocks: **5 EXECUTED**.
- Human validation: **NOT CLAIMED**.
- CD006: **NEXT**.
- Stage 1: **NOT PASSED**.