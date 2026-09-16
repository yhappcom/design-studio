# Content Design / UX Writing Specialist Status

Operating state: **ACTIVE — STAGE 1 FOUNDATION / CD001–CD007 EXECUTED / CD008 NEXT**  
Governance activation: 2026-09-16  
Primary path: `research/content/`  
Study prefix: `CD###`  
Next new-study ID: `CD008`

## Current level

Stage 1 — Foundations: **IN STUDY / PRACTICE — NOT PASSED**  
Stage 2 — Intermediate Professional Practice: **NOT STARTED**  
Stage 3 — Advanced / Systems Practice: **NOT STARTED**  
Stage 4 — Production & Authorship: **NOT STARTED**  
Stage 5 — Research & Advisory: **NOT STARTED**

Content Design progresses deliberately from fundamentals to expert/research-advisory practice. No stage may be skipped because later project work appears more immediately useful.

## Product-language direction

Design Studio products are currently treated as:

- **English-first source language**;
- **global-release products**;
- localization-ready from the beginning;
- additional languages selected later by product/market need rather than by the specialist curriculum itself.

Korean is therefore a possible later transfer case, not a primary Foundation focus or PASS blocker.

## Canonical role

Content Design owns the user-facing semantic and linguistic interface: terminology, naming, action labels, questions, instructions, state/recovery messaging, voice/tone, plain language, accessibility-oriented language, localization-ready content systems and content governance.

It does not own font/rendering mechanics, visual color encoding, spatial composition, interaction state machines, User Research methodology, complete service architecture or complete web runtime architecture. Those remain peer/cross-cutting domains.

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
11. English-first global content and localization-ready architecture;
12. original exercises with explicit KEEP / REWORK / REJECT rationale;
13. cross-specialist reuse and dependency reasoning.

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

Information-sufficiency audit v0.1 checks semantic completeness/order without claiming scan/comprehension outcomes.

## CD005 — accessible, input-neutral language and non-visual reference

Canonical: `research/content/CD005-accessible-input-neutral-language-nonvisual-reference.md`

Key results:
- instructions must not rely only on color, shape, position, size, orientation or sound;
- input-neutral wording is appropriate when physical input is incidental;
- modality-specific wording is appropriate when the modality itself is the subject;
- visible label and programmatic name should preserve the same command identity;
- status wording and status delivery are separate contracts;
- hidden accessibility text must not create a second terminology system.

Preferred reference order:

**semantic label/name → role/object → state → optional sensory/location cue**

Accessibility-language audit v0.1 flags modality/sensory/label-name dependencies without claiming AT-user outcomes.

## CD006 — history, disciplinary boundaries and source literacy

Canonical: `research/content/CD006-history-disciplinary-boundaries-source-literacy.md`

Key results:
- current evidence does not support a single-inventor/single-origin story for Content Design or UX Writing;
- the field draws from editorial practice, technical communication, information architecture, content strategy, service design, HCI/usability/user research and modern interface writing;
- a visible wording symptom may actually be an IA, Interaction, Service or technical-architecture problem;
- source type must match claim type: origin, current role boundary, method, platform behavior or human outcome.

Current studio rule:

> **Diagnose the primary problem before claiming ownership merely because words appear on the surface.**

Historical-source audit v0.1 flags origin overclaim, title/practice confusion, one-organization generalization, practitioner guidance presented as empirical evidence and other provenance failures.

## CD007 — global English and localization-ready content architecture

Canonical: `research/content/CD007-global-english-localization-ready-content.md`

CD007 replaces the earlier Korean-specific Foundation plan with the actual product constraint: English-first apps intended for global release.

### Key source-grounded results

- W3C distinguishes internationalization from localization; global readiness must be designed before translation;
- source English can be clear yet architecturally hostile to localization if grammar is assembled from fragments, formatting is hard-coded, or context is hidden;
- Unicode CLDR demonstrates that plural, unit, number, date/time and regional conventions vary by locale;
- Apple’s current localization workflow treats plural variants, string catalogs, localizer context and per-locale testing as first-class requirements;
- Microsoft global-writing guidance supports avoiding gratuitous idioms, culture-specific references and ambiguous modifier stacks for global content;
- right-to-left transfer strengthens CD005’s rule that position/direction cannot own semantic identity.

### Current rule

> **Preserve the semantic contract across locales; allow the linguistic realization to change.**

English is the canonical source language, but the content architecture must not encode English grammar as product logic.

### Localization-readiness model

High-value strings should preserve:
- concept identity;
- state/action/consequence fidelity;
- complete message units rather than concatenated fragments;
- variable meaning/context;
- localizer notes where ambiguity exists;
- semantic key separation when identical English words have different meanings;
- locale-sensitive number/date/currency/unit behavior;
- layout independence from English string length/direction.

Localization-readiness audit v0.1 flags:
- idiom/culture dependency;
- ambiguous referent/part of speech;
- string concatenation;
- pseudo-plurals such as `(s)`;
- semantic key collision;
- missing variable/localizer context;
- hard-coded locale formatting;
- fixed-width/direction dependencies;
- locale-expert/runtime/human-validation needs.

It cannot prove translation quality, cultural appropriateness or user comprehension.

## Cross-specialist state after CD007

### Type
Localized strings become real glyph/width/fallback test corpora. Geometry pressure is not permission to delete necessary semantics. Script/font support remains Type-owned.

### Color
Localized wording must not introduce color-only state references; semantic meaning must survive alternate themes and forced colors.

### Layout / Interaction
Interaction state/action/recovery truth remains invariant across locales. Layout must permit reflow/recomposition rather than forcing English-length assumptions.

### Web
Web is the runtime transfer partner for language/direction metadata, localized reflow, zoom, browser accessibility and RTL behavior.

### User Research / Human Factors
Actual comprehension/findability/task-performance claims in English or any locale require appropriate human evidence.

## Evidence boundary

Current Content evidence includes:
- authoritative/primary source study;
- historical/professional precedent analysis;
- contemporary HCI/technical-communication evidence;
- controlled empirical evidence from adjacent communication domains;
- direct cross-specialist reuse/transfer;
- seven original structured practice/critique blocks;
- terminology, command, information-sufficiency, accessibility-language, source-provenance and localization-readiness audits.

NOT established yet:
- human comprehension/findability/task completion;
- terminology recall or action-label speed/error effects;
- actual expert-domain vocabulary recognition;
- quality/cultural appropriateness in any specific target locale;
- actual screen-reader/voice/magnification/disabled-user outcomes;
- production string-governance behavior;
- live-project improvement.

## Active next queue

1. **CD008 — integrated Foundation capstone.** Apply CD001–CD007 to one bounded English-first professional-product workflow; produce materially different content architectures; preserve Interaction/Type/Web dependencies; run the existing non-human audits together; explicitly expose what still needs human evidence.
2. **CD009 — Stage 1 closure audit** only if CD008 demonstrates integrated judgment rather than rule recitation.
3. Begin Stage 2 forms/errors/onboarding/empty states/voice-tone work only after Foundation PASS.
4. Specific locale studies, including Korean, should be opened later only when product/market need or transfer risk justifies them.

## OPEN / dependencies

- integrated Foundation authorship across a complete workflow;
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
- CD006: **EXECUTED** — history, disciplinary boundaries and source-provenance method.
- CD007: **EXECUTED** — English-first global content and localization-ready architecture.
- Original practice/critique blocks: **7 EXECUTED**.
- Human validation: **NOT CLAIMED**.
- CD008: **NEXT**.
- Stage 1: **NOT PASSED**.
