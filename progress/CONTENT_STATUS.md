# Content Design / UX Writing Specialist Status

Operating state: **ACTIVE — STAGE 1 FOUNDATION / CD001–CD004 EXECUTED / CD005 NEXT**  
Governance activation: 2026-09-16  
Primary path: `research/content/`  
Study prefix: `CD###`  
Next new-study ID: `CD005`

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

Initial diagnostic:
- **Object**
- **State**
- **Action**
- **Consequence**

A controlled ambiguous network-outcome exercise rejected a shorter but semantically false failure/retry message. Human comprehension/preference was not claimed.

## CD002 — user needs, mental models, terminology and naming

Canonical: `research/content/CD002-user-needs-mental-models-terminology-naming.md`

Key additions:
- user needs are task/outcome based and should not be confused with proposed features;
- “mental model” is not accepted as an intuition shortcut: Design model, system image and user model are distinct;
- concept and designation are separate, supporting concept-first terminology analysis;
- same concept/function should normally preserve a stable designation;
- different concepts should remain distinct when their action, consequence, recovery, persistence or interpretation differs;
- domain-native expert vocabulary can coexist with plain language when genuinely audience-native and task-critical;
- internal implementation terms and product-created neologisms require explicit justification.

Original practice rejected concept collision and false simplification in a professional data-import vocabulary system.

Terminology audit v0.1 can flag `COLLISION`, `DRIFT`, `INTERNALISM`, audience/localization/human-evidence needs, but cannot measure comprehension or performance.

## CD003 — action labels, command grammar and consequence clarity

Canonical: `research/content/CD003-action-labels-command-grammar-consequence-clarity.md`

Key result:

> **Label wording must reflect the real command contract when persistence, commitment, object scope, destructive consequence or temporal outcome changes.**

CD003 separates command, object/scope, immediate behavior, persistence, outcome state and recoverability.

Provisional rules:
- specificity rises when object/persistence/commitment/destructive scope/external side effect matters;
- `Save`, `Submit`, `Publish`, `Delete`, `Remove`, `Archive`, `Retry` are not interchangeable by default;
- action labels describe what the user initiates/authorizes, not an unconfirmed completed outcome;
- `Retry` requires Interaction evidence that retry is behaviorally safe;
- visible and accessible names must preserve the same command identity.

Original practice executed four controlled command contracts and rejected false persistence, hidden deletion scope and premature completion wording.

Command audit v0.1 can flag `FALSE PERSISTENCE`, `FALSE COMPLETION`, `OBJECT AMBIGUITY`, `CONSEQUENCE HIDING`, `UNSAFE RETRY LANGUAGE`, `TERM COLLISION`, `ACCESSIBLE-NAME DRIFT` and human-validation needs.

## CD004 — plain language, scanning, information order and sufficiency

Canonical: `research/content/CD004-plain-language-scanning-information-order-sufficiency.md`

CD004 moves beyond the shortcut “shorter is better.”

### Key source/evidence additions

- ISO 24495-1 provides an international plain-language frame that goes beyond sentence length and vocabulary simplification;
- GOV.UK supports user-language, front-loading, scanning and removing unnecessary words while warning that an over-explained interface may itself need redesign;
- W3C cognitive-accessibility guidance supports clear words, short logical chunks, descriptive headings and separated instructions, while remaining supplemental rather than a universal word-count law;
- controlled health-communication studies show that plain-language revisions can improve comprehension but effects vary by content/audience;
- readability-formula research shows word/sentence length and grade scores are incomplete proxies for actual comprehension.

### Foundation correction introduced by CD004

Content now separates:
- **clarity** — ambiguity/interpretability;
- **brevity** — amount of language;
- **sufficiency** — whether enough task-relevant information is present.

Current rule:

> **Optimize for minimum sufficient content, not minimum character count.**

CD004 also classifies information as:
- required-before-action;
- helpful-at-point-of-need;
- background/explanatory.

Required-before-action information must not be hidden merely to reduce density.

### Original practice

A controlled import-state message compared:
- compressed but insufficient wording — **REJECT**;
- complete but poorly ordered bureaucratic wording — **REWORK**;
- front-loaded, scoped, minimum-sufficient content — **KEEP AS SEMANTIC/INFORMATION-ORDER CONTROL**.

No human comprehension/finding claim is made.

### Information-sufficiency audit v0.1

Can flag:
- `MISSING OBJECT / STATE / ACTION / CONSEQUENCE / CONDITION / SCOPE`;
- `LATE TASK FACT`;
- `GENERIC HEADING`;
- `MULTI-TOPIC CHUNK`;
- `FRAGMENTED RELATIONSHIP`;
- `INTERNAL JARGON`;
- `UNEXPLAINED UNCOMMON TERM`;
- `FALSE SIMPLIFICATION`;
- `REDUNDANT PREFACE`;
- readability/audience/human/localization validation needs.

It cannot prove scan pattern, comprehension, reading speed, trust, preference or task performance.

## Cross-specialist state after CD004

### Type
Semantically necessary headings, conditions and warnings become real Type stress content. Wrapping/geometry pressure is not permission to delete necessary meaning. Current Type live-project work remains Stage 2 PRACTICE with LogMate identity priority.

### Color
Visual salience can reinforce information priority, but meaning/findability cannot depend on authored hue alone.

### Layout / Interaction
Content now distinguishes required-before-action vs point-of-need vs background information. Layout owns spatial realization; Interaction owns whether information is prerequisite to a safe/valid action.

### Web
W017’s preservation of visible labels under enlargement aligns with CD004. Future Web transfer should stress minimum-sufficient content under narrow width, zoom/enlargement, localization and runtime states.

## Evidence boundary

Current Content evidence includes:
- authoritative/primary source study;
- HCI/conceptual evidence;
- controlled empirical evidence from adjacent communication domains;
- cross-specialist reuse;
- four original structured practice blocks;
- provisional terminology, command and information-sufficiency audits.

NOT established yet:
- human comprehension/findability/task completion;
- terminology recall;
- action-label speed/error effects;
- trust/confidence effects;
- actual expert-domain vocabulary recognition;
- Korean information-order/action-language behavior;
- Korean↔English equivalence;
- screen-reader/AT user outcomes;
- production string-governance behavior;
- live-project improvement.

## Active next queue

1. **CD005 — accessible/input-neutral language and non-visual reference failures.** Establish how wording survives screen-reader, keyboard, pointer/touch, forced-colors, magnification and modality changes without claiming AT user evidence.
2. Add design-history/precedent literacy specific to Content Design before Foundation closure.
3. Add stronger Korean-language/bilingual evidence, including information order and professional-domain terminology.
4. Extend reproducible non-human checks without treating formulas/model critique as human evidence.
5. Run Stage 1 gap/closure audit only after the remaining Foundation evidence is present.
6. Only after Foundation closure should Stage 2 surface-pattern work begin (forms, errors, onboarding, empty states, voice/tone systems).

## OPEN / dependencies

- input-neutral and non-visual language foundations;
- Korean word order/action-label transfer;
- expert-domain abbreviation/terminology elicitation;
- terminology governance for professional-domain products;
- appropriate human methods separating findability, comprehension, recall and actionability;
- progressive-disclosure validation where omission cost is asymmetric;
- cross-surface command/content mapping for mobile/web/notifications/voice;
- later human testing protocol once live projects support it.

## Latest checkpoint

- Specialist approved: **YES**.
- Canonical path/status: **ACTIVE**.
- Five-stage progression: **DEFINED**.
- CD001: **EXECUTED** — language-as-interface semantic contract.
- CD002: **EXECUTED** — user needs, mental-model caution, terminology architecture.
- CD003: **EXECUTED** — command semantics and consequence clarity.
- CD004: **EXECUTED** — plain language, scanning, information order and minimum-sufficient content.
- Original practice/critique blocks: **4 EXECUTED**.
- Human validation: **NOT CLAIMED**.
- CD005: **NEXT**.
- Stage 1: **NOT PASSED**.