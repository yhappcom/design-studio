# Content Design / UX Writing Specialist Status

Operating state: **ACTIVE — STAGE 1 FOUNDATION / CD001–CD003 EXECUTED / CD004 NEXT**  
Governance activation: 2026-09-16  
Primary path: `research/content/`  
Study prefix: `CD###`  
Next new-study ID: `CD004`

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

CD002 extends semantic fidelity from single messages to product-wide concept and terminology architecture.

### Key additions

- user needs are task/outcome based and should not be confused with proposed features;
- “mental model” is not accepted as an intuition shortcut: Design model, system image and user model are distinct, and HCI literature uses the mental-model construct diversely;
- concept and designation are separate, supporting concept-first terminology analysis;
- same concept/function should normally preserve a stable designation;
- different concepts should remain distinct when their action, consequence, recovery, persistence or interpretation differs;
- consistency means stable concept mapping, not mechanically identical strings;
- domain-native expert vocabulary can coexist with plain language when it is genuinely audience-native and task-critical;
- internal implementation terms, common words used with unusual product meanings and product-created neologisms require explicit justification.

### CD002 original practice

A synthetic professional data-import scenario compared one-word simplification, concept-preserving terminology and friendlier generic wording.

- collapsing file/event/result under `Import` was **REJECTED** for concept collision;
- `File / Import / Record / Possible duplicate` was **KEPT as a semantic control**, not proven final user wording;
- `Document / Add data / Item / Match / Fix matches` was **REJECTED / REWORKED** where common words distorted fixed product facts.

### CD002 non-human audit v0.1

Can flag:
- `COLLISION`;
- `DRIFT`;
- `INTERNALISM`;
- `AUDIENCE EVIDENCE NEEDED`;
- `LOCALIZATION REVIEW NEEDED`;
- `HUMAN VALIDATION NEEDED`.

It cannot measure comprehension, recall, preference, trust, task time or error rate.

## CD003 — action labels, command grammar and consequence clarity

Canonical: `research/content/CD003-action-labels-command-grammar-consequence-clarity.md`

CD003 applies CD001/CD002 to commands and control labels.

### Key source-grounded result

Apple, GOV.UK and Microsoft all support action labels that clearly communicate purpose, but GOV.UK provides a particularly useful semantic distinction:
- `Continue` when no save occurs;
- `Save and continue` when data is persisted;
- `Save and come back later` when persistence supports leaving/resuming;
- `Confirm and send` vs `Accept and send` when legal/commitment semantics differ.

This supports a stronger rule than “start buttons with verbs”:

> **Label wording must reflect the real command contract when persistence, commitment, object scope, destructive consequence or temporal outcome changes.**

### Command semantic layers

CD003 separates:
1. command;
2. object/scope;
3. immediate product behavior;
4. commitment/persistence;
5. outcome state;
6. recoverability.

A label need not contain all six, but the interface must not misrepresent them.

### Action-label principles now adopted provisionally

- short conventional labels are acceptable when risk/context ambiguity is low;
- specificity should rise when object, persistence, commitment, destructive scope or external side effect matters;
- `Save`, `Submit`, `Publish`, `Delete`, `Remove`, `Archive`, `Retry` are not interchangeable by default;
- an action label describes what the user initiates/authorizes, not an unconfirmed completed outcome;
- `Retry` is unavailable as a Content choice until Interaction establishes that retry is behaviorally safe;
- destructive meaning must survive without red styling alone;
- visible label and accessible name must preserve the same command identity.

### CD003 original practice

Four controlled command contracts were tested:

1. advance without persistence → `Save and continue` **REJECTED**, `Continue` retained as semantic control;
2. durable draft save + advance → `Save and continue` retained as semantic control;
3. permanent record deletion among multiple scopes → generic `Confirm` **REJECTED**, `Delete record` retained as semantic control;
4. asynchronous export generation → `Export ready` and premature `Download` rejected, `Create export` retained until completion creates a real download action.

The result is not “always use longer labels.” The current Content rule is:

> **Use the smallest amount of language that preserves the distinctions the user is actually authorizing.**

### CD003 non-human command audit v0.1

Can flag:
- `FALSE PERSISTENCE`;
- `FALSE COMPLETION`;
- `OBJECT AMBIGUITY`;
- `CONSEQUENCE HIDING`;
- `UNSAFE RETRY LANGUAGE`;
- `TERM COLLISION`;
- `ACCESSIBLE-NAME DRIFT`;
- `HUMAN VALIDATION NEEDED`.

## Cross-specialist state after CD003

### Type
Semantically necessary terms/labels must become actual Type/layout stress strings; they must not be shortened merely to preserve preferred geometry.

### Color
Destructive/warning state can be reinforced visually but cannot depend on color alone. No Color contradiction introduced.

### Layout / Interaction
Highest-overlap dependency remains active. Interaction owns actual state, persistence, reversibility, retry safety and consequence; Content cannot invent these through wording.

### Web
Future transfer must validate visible label/accessibility-name identity, correct semantic controls, keyboard/focus behavior, pending/disabled/busy states and consequential duplicate activation.

## Evidence boundary

Current Content evidence now includes:
- authoritative/primary source study;
- historical/contemporary HCI conceptual evidence;
- cross-specialist reuse;
- three original structured practice blocks;
- provisional terminology and command audits that can reject semantic falsehoods without pretending to measure human comprehension.

NOT established yet:
- human comprehension;
- task completion effects;
- terminology recall;
- action-label speed/error effects;
- trust/confidence effects;
- actual expert-domain vocabulary recognition;
- Korean command-language behavior;
- Korean↔English terminology equivalence;
- production string-governance behavior;
- live-project improvement.

## Active next queue

1. **CD004 — plain language, scanning, information order and sufficiency trade-offs.** Move beyond “shorter is better” and establish when front-loading, chunking, sentence complexity and necessary detail improve or damage task communication.
2. CD005 — accessible/input-neutral interface language and non-visual reference failures.
3. Add design-history/precedent literacy specific to content design before Foundation closure.
4. Add stronger Korean-language and bilingual evidence.
5. Extend reproducible non-human checks without treating formulas/model critique as human evidence.
6. Run a Stage 1 gap/closure audit only after sufficient original practice exists.
7. Only after Foundation evidence is strong enough, move into Stage 2 surfaces such as forms, errors, onboarding, empty states and voice/tone systems.

## OPEN / dependencies

- information scent, recognition and comprehension evidence;
- plain-language evidence beyond practitioner rules;
- Korean word order/action-label transfer;
- research methods for expert-domain terminology elicitation;
- terminology governance for professional-domain products;
- cross-surface command mapping for mobile/web/notifications/voice;
- later human testing protocol once live projects support it.

## Latest checkpoint

- Specialist approved: **YES**.
- Canonical path/status: **ACTIVE**.
- Five-stage progression: **DEFINED**.
- CD001: **EXECUTED** — language-as-interface semantic contract.
- CD002: **EXECUTED** — user needs, mental-model caution, terminology architecture, original practice, terminology audit v0.1.
- CD003: **EXECUTED** — command semantics, consequence clarity, original practice, action audit v0.1.
- Original practice/critique blocks: **3 EXECUTED**.
- Human validation: **NOT CLAIMED**.
- CD004: **NEXT**.
- Stage 1: **NOT PASSED**.
