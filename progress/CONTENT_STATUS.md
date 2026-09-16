# Content Design / UX Writing Specialist Status

Operating state: **ACTIVE — STAGE 1 FOUNDATION / CD001–CD002 EXECUTED / CD003 NEXT**  
Governance activation: 2026-09-16  
Primary path: `research/content/`  
Study prefix: `CD###`  
Next new-study ID: `CD003`

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

## CD001 — executed Foundation evidence

Canonical: `research/content/CD001-language-as-interface-foundations.md`

CD001 established the first Content-specific foundation model from first-party GOV.UK, Apple and Microsoft guidance plus direct reuse of existing Design Studio Interaction evidence.

Key result:

> Content is part of the product contract, not a decorative string layer. Before optimizing tone or brevity, verify semantic fidelity to the real object, state, available action and consequence.

Initial diagnostic model:
- **Object** — what thing/process is this about?
- **State** — what is actually known to be true now?
- **Action** — what can the user actually do now?
- **Consequence** — what will that action change or risk?

This is a diagnostic, not a mandatory sentence template.

A controlled ambiguous network-outcome exercise rejected the shortest candidate because it falsely asserted a known failure and encouraged unsafe retry despite an unknown server outcome. Human comprehension/preference was not claimed.

## CD002 — user needs, mental models, terminology and naming

Canonical: `research/content/CD002-user-needs-mental-models-terminology-naming.md`

CD002 extends semantic fidelity from single messages to product-wide concept and terminology architecture.

### Source/evidence additions

- GOV.UK user-needs guidance: user needs are task/outcome based and should use language users recognize rather than embedding a proposed solution.
- ISO 9241-110: task suitability, self-descriptiveness, user expectations and learnability provide an interaction-level basis for predictable concepts and names.
- Norman conceptual-model framing: design model, system image and user's model are distinct; Content is part of the system image rather than a mechanism for directly controlling a user's mental model.
- Hu & Twidale 2023 HCI scoping review: “mental model” is used diversely across HCI, so the studio must specify what evidence was actually observed rather than using the phrase as an intuition shortcut.
- ISO 704/1087 terminology work: concepts and linguistic designations are distinct, supporting concept-first terminology analysis.
- W3C WCAG 3.2.4/G197 + cognitive-accessibility guidance: repeated functionality should be identified consistently; clear/familiar labels reduce avoidable ambiguity, while human usability claims still require appropriate user evidence.
- Microsoft terminology guidance: familiar words should not be casually assigned unusual product meanings, and specialized terms require audience justification.

### Foundation correction introduced by CD002

Do **not** write “this matches the user's mental model” without evidence describing what users actually know, predict, group, call or expect.

Use a more explicit chain:

`user need → product/domain concept → audience/context evidence → designation → cross-surface consistency → validation`

### Concept-first terminology method

For high-value terms, record:
- concept and boundary;
- audience/context;
- evidence source;
- preferred designation;
- allowed variants;
- prohibited collisions;
- cross-surface locations;
- localization note;
- validation need.

Default studio rules now include:
1. same concept/function → same designation by default;
2. different concepts → different designations when the distinction changes action, state, consequence, ownership, persistence, recovery or interpretation;
3. consistency means stable mapping, not mechanically identical character strings;
4. precise domain-native vocabulary can coexist with plain language when it is genuinely audience-native and task-critical;
5. internal implementation jargon and product-created neologisms require explicit justification rather than automatic exposure.

### Original terminology practice

A synthetic professional data-import scenario compared three terminology systems for distinct concepts such as source file, import run, record, possible duplicate and resolution choice.

- one-word simplification using `Import` for file/event/result was **REJECTED** for concept collision;
- concept-preserving `File / Import / Record / Possible duplicate` was **KEPT as a semantic control**, not as proven final user wording;
- friendlier generic `Document / Add data / Item / Match / Fix matches` was **REJECTED / REWORKED** because common words hid or distorted product semantics.

This demonstrates that vocabulary minimization and common-word substitution are not equivalent to conceptual simplicity.

### Reproducible non-human audit introduced

CD002 introduces a provisional terminology audit that can flag:
- `COLLISION`;
- `DRIFT`;
- `INTERNALISM`;
- `AUDIENCE EVIDENCE NEEDED`;
- `LOCALIZATION REVIEW NEEDED`;
- `HUMAN VALIDATION NEEDED`.

It can verify terminology structure against known product facts but cannot measure comprehension, recall, preference, trust, task time or error rate.

## Cross-specialist state after CD002

### Type
Operational strings and terminology create real glyph, width, abbreviation, punctuation and localization stress. T017 provides a future expert-domain transfer substrate, but CD002 makes no aviation-vocabulary correctness claim.

### Color
Terminology should name semantic state/concept rather than rely on palette-specific references. No new Color contradiction introduced.

### Layout / Interaction
Still the highest-overlap dependency. Interaction owns actual concepts, state/action/recovery consequences; Content must preserve materially meaningful distinctions in naming.

### Web
Future transfer should check repeated-function naming, visible label ↔ accessible name mapping, long/localized terminology and responsive variants in implemented browser components.

## Evidence boundary

Current Content evidence now includes:
- authoritative/primary source study;
- historical and contemporary HCI conceptual evidence;
- cross-specialist reuse;
- two original structured practice exercises;
- provisional reproducible non-human semantic/terminology checks.

NOT established yet:
- human comprehension;
- task completion effects;
- terminology recall;
- trust/confidence effects;
- actual expert-domain vocabulary recognition;
- Korean↔English terminology equivalence;
- localization quality;
- screen-reader user outcomes;
- production string-governance behavior;
- live-project improvement.

These require later appropriate evidence and must not be inferred from source agreement or expert critique.

## Active next queue

1. **CD003 — action labels, command grammar and consequence clarity:** distinguish command, object, state and outcome language and test when labels must expose consequence/risk.
2. CD004 — plain language, scanning, information sequencing and sufficiency trade-offs.
3. CD005 — accessible/input-neutral interface language and non-visual reference failures.
4. Add design-history/precedent literacy specific to content design before Foundation closure.
5. Add stronger Korean-language and bilingual terminology evidence.
6. Continue developing reproducible non-human content checks that validate semantic structure without pretending to measure comprehension.
7. Run a Stage 1 gap/closure audit only after sufficient original practice exists.
8. Only after Foundation evidence is strong enough, move into Stage 2 surfaces such as forms, errors, onboarding, empty states and voice/tone systems.

## OPEN / dependencies

- research methods for eliciting expert-domain vocabulary without preference-only testing;
- stronger evidence on information scent, recognition and comprehension;
- Korean-language plain-language and bilingual terminology evidence;
- terminology governance for professional-domain products;
- partial synonymy, abbreviations and locale-specific non-equivalence;
- best boundaries among Content, UX Research and IA methods such as card sorting/tree testing/concept mapping;
- later human testing protocol once a live app/project can support it.

## Latest checkpoint

- Specialist approved: **YES**.
- Canonical path/status: **ACTIVE**.
- Five-stage progression: **DEFINED**.
- CD001: **EXECUTED** — language-as-interface semantic contract.
- CD002: **EXECUTED** — user needs, mental-model caution, concept/designation terminology architecture, original practice and non-human audit v0.1.
- Original practice/critique blocks: **2 EXECUTED**.
- Human validation: **NOT CLAIMED**.
- CD003: **NEXT**.
- Stage 1: **NOT PASSED**.
