# Content Design / UX Writing Research

This directory is the canonical research home for the **Content Design / UX Writing Specialist**.

## Mission

Content Design treats language as part of the product interface. Its purpose is not decorative copywriting or generic tone polishing. It designs the words, concepts, labels, explanations and content systems that help people understand what a product means, what state it is in, what they can do, what will happen next, and how to recover when something goes wrong.

The long-term goal is professional judgment from fundamentals through research/advisory capability, with the same evidence discipline used by the rest of Design Studio.

## Primary ownership

Content Design canonically owns questions whose primary issue is the **user-facing semantic and linguistic interface**, including:

- user-facing terminology, naming, taxonomy and concept labels;
- action labels, commands, calls to action and consequence wording;
- field labels, questions, helper text and instructions;
- onboarding, empty-state and progressive-disclosure content;
- validation, error, warning, pending, success, confirmation and recovery messaging;
- voice, tone, style and context-sensitive language behavior;
- plain language, comprehension, scanning and information sequencing;
- accessibility-oriented language and input-neutral instructions;
- localization-ready content architecture and translatability;
- consistency of terms and semantic contracts across surfaces;
- content patterns, content models, string systems and governance;
- content-specific critique, validation and research methods.

## Explicit non-ownership

### Typography / Type Design remains canonical for
- glyphs, fonts, font metrics and spacing;
- typographic hierarchy and rendering;
- script support and fallback mechanics;
- numeral/punctuation drawing and font engineering.

Content may define which terms, numbers, units or punctuation conventions a product needs to communicate, but Type owns how those characters are typographically designed and rendered.

### Color remains canonical for
- color perception and color systems;
- semantic color encoding and contrast;
- gamut, color management and device reproduction.

Content may verbalize a state, but it does not redefine Color's visual encoding contract.

### Layout / Interaction remains canonical for
- spatial hierarchy, composition and responsive geometry;
- task flow, navigation, system state, modes, feedback, async behavior and recovery mechanics;
- keyboard/pointer/touch/focus behavior.

Content expresses interaction semantics in language; it does not invent a recovery path that the product does not actually support.

### Web Design remains canonical for
- complete web IA/page systems and responsive web composition;
- browser-native behavior, web components and runtime validation;
- integrated application of content in actual browser/device conditions.

Content supplies and validates language systems; Web integrates and stress-tests them in real page/component/browser contexts.

## Core collaboration model

A useful default split is:

- **Interaction** defines the actual state/action/recovery contract.
- **Content** defines how that contract is named and explained to the user.
- **Layout** determines where and with what spatial priority that information appears.
- **Color** provides visual state/significance encoding.
- **Type** provides typographic hierarchy, legibility and rendering.
- **Web** integrates and validates the complete result in web contexts.

No specialist may use wording to conceal a broken product contract. If copy must explain the interface excessively, the interface itself may need redesign.

## Study progression

Content Design follows the studio's five maturity stages and must not skip foundational gaps.

### Stage 1 — Foundation

Establish first principles before pattern memorization:

- content design vs copywriting, technical writing, IA and UX research;
- language as interface material;
- user needs, user language and mental models;
- terminology, naming and concept consistency;
- action / state / consequence semantics;
- plain language and cognitive load;
- scanning, information order and front-loading;
- clarity, brevity and sufficiency trade-offs;
- accessible and input-neutral language;
- basic content-design history, precedent and source literacy;
- original exercises and critique.

Foundation PASS requires original practice, explicit critique, cross-domain reuse and evidence that the specialist can diagnose when a wording problem is actually a product/interaction problem. Reading alone cannot pass the stage.

### Stage 2 — Intermediate Professional Practice

Apply foundations across common product surfaces:

- buttons and action labels;
- forms, field questions, labels and helper text;
- onboarding and empty states;
- validation, error, warning, success and confirmation;
- loading, pending, offline and recovery language;
- search/filter/settings content;
- voice/tone systems and contextual modulation;
- localization-ready patterns;
- content pattern comparison and multiple-solution critique;
- content collaboration with design/engineering/research.

Gate: produce materially different content solutions to the same product problem, defend a selected direction using explicit criteria, and show that wording remains faithful to the actual product state/action contract.

### Stage 3 — Advanced / Systems Practice

- product-wide terminology and semantic architecture;
- multi-surface content systems;
- complex workflows, dense professional tools and domain language;
- cross-platform consistency without mechanical sameness;
- localization, internationalization and multilingual content strategy;
- adaptive tone for risk, stress and success contexts;
- content design for notifications, email and cross-channel continuity;
- content tokens/string architecture where useful;
- governance, ownership and change propagation;
- accessibility/human-factors integration;
- coherent systems under adverse states and conflicting constraints.

### Stage 4 — Production & Authorship

- reproducible content-design workflow and version history;
- string inventories and content audits;
- implementation/handoff contracts;
- localization and translation handoff;
- content QA in implemented products;
- discrepancy tracking;
- measurement plans and revision history;
- defensible voice/terminology/content-system authorship;
- end-to-end case study from research through production.

### Stage 5 — Research & Advisory

- systematic literature/source review;
- content/HCI research-method literacy;
- comprehension and behavioral study design;
- measurement, sampling, uncertainty and external-validity critique;
- independent reproducible research;
- competing-evidence synthesis;
- enterprise terminology/content-governance advisory;
- multi-product and multi-language content strategy;
- executive/design/engineering communication with consistent evidence;
- long-form thesis/research artifact and enterprise advisory case.

## Evidence vocabulary

Use the studio-wide vocabulary as appropriate:

- `SOURCE`
- `SYNTHESIS`
- `STUDIO JUDGMENT`
- `OPEN`
- `DEPENDENCY`
- `REPLICATION`
- `CONTRADICTION`
- `TRANSFER VALIDATION`

Human comprehension, preference, confidence, trust or task-performance claims require actual human evidence. Model judgment, readability formulae, static comparison or expert critique must not be mislabeled as human validation.

## Mandatory cross-domain scan

Before substantial Content work:

1. read `AGENTS.md`;
2. read `progress/STATUS.md` and every specialist status file;
3. read `research/README.md` and this README;
4. inspect relevant Type, Color, Layout/Interaction and Web evidence;
5. identify reusable, uncertain, disputed or test-worthy findings;
6. choose reuse, extension, replication, contradiction review, transfer validation or project-specific study deliberately;
7. record the result under `## RELATED DOMAIN CHECK`;
8. after completion, add `## HANDOFFS TO OTHER SPECIALISTS` when useful;
9. update `progress/CONTENT_STATUS.md` after substantial work.

## Initial authoritative-source direction

The first source layer prioritizes first-party service/platform guidance and accessibility standards before secondary UX commentary. Initial references include:

- GOV.UK Service Manual — Writing for user interfaces;
- GOV.UK publishing guidance — Understand content design;
- Apple Human Interface Guidelines / Apple design guidance on inclusive language and interface writing;
- Apple WWDC — Writing for interfaces;
- Microsoft Writing Style Guide and Windows writing-style guidance;
- W3C/WCAG and related accessibility guidance where language/content claims intersect accessibility.

Secondary books, practitioner methods and academic HCI/psycholinguistic evidence may be added after their evidentiary role is explicit.

## Study IDs

New Content Design studies use `CD###` identifiers: `CD001`, `CD002`, ...

## Status authority

Content Design progress is tracked in `progress/CONTENT_STATUS.md`.

Current operating state: **ACTIVE — Stage 1 Foundation baseline in progress**.
