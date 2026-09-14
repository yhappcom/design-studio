# Cross-Specialist Collaboration Protocol

This document defines how Design Studio specialists cooperate without wasting effort or missing useful findings from peers.

## Current team

- Typography / Type Design Specialist
- Color Specialist
- Layout, Spatial & Interaction Specialist
- Web Design Specialist

Future specialists may be added through the onboarding process.

## Core rule

**Before researching, check what the others already know. After researching, tell the others what became useful to them.**

The purpose is not to eliminate all overlap. The purpose is to make overlap intentional, useful and traceable.

## Start-of-work protocol

Before every substantial study, critique, validation, design or project block:

1. read `progress/STATUS.md`;
2. read all four specialist status files;
3. inspect your own open gaps and dependencies;
4. search peer research for concepts related to the proposed question;
5. identify reusable findings;
6. identify existing work that may deserve replication, challenge, method comparison, transfer validation or implementation validation;
7. identify dependency/collaboration opportunities;
8. write `RELATED DOMAIN CHECK` in the planned research note.

## RELATED DOMAIN CHECK template

```md
## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
- Reusable finding:
- Replication / challenge / transfer opportunity:
- Dependency or overlap:

### Color
- Evidence checked:
- Reusable finding:
- Replication / challenge / transfer opportunity:
- Dependency or overlap:

### Layout / Interaction
- Evidence checked:
- Reusable finding:
- Replication / challenge / transfer opportunity:
- Dependency or overlap:

### Web Design
- Evidence checked:
- Reusable finding:
- Implementation/application validation opportunity:
- Dependency or overlap:

### Other / cross-cutting / future specialist
- Evidence checked:
- Reusable finding:
- Dependency or overlap:

### Overlap decision
- Reuse / deliberate repetition / extension / contradiction review / method comparison / transfer validation / project-specific study:
- Why:
```

A section may say `Not materially relevant` only after checking whether relevant evidence exists.

## Repeat research

Overlapping or repeated research is legitimate when it serves at least one of these purposes:

- independent replication;
- calculation or method check;
- adversarial review;
- contradiction investigation;
- transfer validation;
- implementation validation;
- comparison of standards, theories, tools or datasets;
- prerequisite learning;
- project-specific validation;
- second-specialist interpretation.

The problem is not duplication itself. The problem is unexamined duplication with no additional analytical value.

## Web Design's collaboration role

Web Design is not a final implementation handoff.

It designs actual websites and web apps and acts as a strong integration/validation layer.

### Type → Web

Web uses Type research for typography hierarchy, metrics, numerals, localization, fallback and rendering, then applies it in actual page systems and browser conditions.

### Web → Type

Web hands back browser/font-loading/fallback/wrapping/zoom/localization findings that confirm or challenge Type assumptions.

### Color → Web

Web uses Color research for palettes, semantic states, themes, contrast, gamut and viewing conditions in actual web surfaces.

### Web → Color

Web hands back theme/browser/device/forced-colors/system-setting findings that confirm, limit or challenge Color assumptions.

### Layout/Interaction → Web

Web uses spatial hierarchy, responsive logic, navigation, states, feedback and recovery research to design complete page/component systems.

### Web → Layout/Interaction

Web hands back findings from intrinsic sizing, responsive reflow, native controls, focus/keyboard/pointer/touch, browser history, loading/network and real content behavior.

## During-work protocol

When another specialist's evidence becomes relevant:

- cite/link the canonical study;
- choose whether to reuse, reproduce, challenge or extend it;
- state that choice explicitly;
- if independently repeating it, explain the reason and keep the record in your own writable area unless joint work is authorized;
- document confirmation, contradiction, limitation, transfer failure or new consequence;
- hand useful results back to the peer specialist.

A specialist is not required to stop because another domain has studied the topic already.

## Dependency protocol

A dependency entry should state:

- requested specialist/domain;
- exact question;
- why it affects current work;
- evidence already checked;
- whether current work is blocked or can continue partially;
- whether independent investigation is also planned;
- what answer/evidence would resolve it.

Do not edit another specialist's status to assign them work.

## Completion protocol

At the end of a substantial study:

1. save the research/evidence in the appropriate writable/canonical area;
2. distinguish SOURCE / SYNTHESIS / STUDIO JUDGMENT / OPEN / DEPENDENCY;
3. label REPLICATION / CONTRADICTION / TRANSFER VALIDATION when applicable;
4. add `HANDOFFS TO OTHER SPECIALISTS` when relevant;
5. update your own specialist status;
6. list new incoming/outgoing dependencies;
7. note peer findings that changed your conclusion;
8. note deliberate overlap and what it added;
9. commit before beginning materially different work when practical.

## HANDOFFS TO OTHER SPECIALISTS template

```md
## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
- Canonical section:
- Confirmation / contradiction / transfer note:
- Scope limit:

### Color
- Useful finding/context:
- Canonical section:
- Confirmation / contradiction / transfer note:
- Scope limit:

### Layout / Interaction
- Useful finding/context:
- Canonical section:
- Confirmation / contradiction / transfer note:
- Scope limit:

### Web Design
- Useful finding/context:
- Web application / validation consequence:
- Confirmation / contradiction / transfer note:
- Scope limit:
```

## Conflict protocol

When specialists reach incompatible conclusions:

1. neither overwrites the other's file;
2. each states its claim and evidence;
3. classify the disagreement as factual, methodological, contextual or design judgment;
4. reproduce/extend disputed work when useful;
5. identify evidence that could resolve it;
6. coordinator records a resolution or leaves the conflict explicitly unresolved.

## Concurrency protocol

To reduce Git conflicts without restricting intellectual scope:

- each specialist writes only its own canonical paths and status during ordinary work;
- cross-domain replication is stored in the investigating specialist's writable area and linked to peer evidence;
- specialists do not edit global governance/index files unless authorized;
- specialists do not move or rename files while others may be active;
- new studies use domain prefixes;
- shared structural changes are coordinator work.

## Research-queue principle

Choose work by expected value, not activity volume.

Strong reasons to study next include:

1. a live project need;
2. an important unresolved Foundation/validation gap;
3. a dependency that blocks another specialist;
4. a high-impact peer finding that deserves independent verification;
5. a cross-domain transfer or implementation question;
6. a genuinely new topic that expands professional capability.

The best next study is the one that most increases reliability, breadth, transferability, implementation confidence or project usefulness.
