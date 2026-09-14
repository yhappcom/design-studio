# Cross-Specialist Collaboration Protocol

This document defines how Design Studio specialists cooperate without wasting effort or missing useful findings from peers.

## Current team

- Typography / Type Design Specialist
- Color Specialist
- Layout, Spatial & Interaction Specialist

Future specialists may be added through `coordination/ONBOARDING.md`.

## Core rule

**Before researching, check what the others already know. After researching, tell the others what became useful to them.**

The purpose is not to eliminate all overlap. The purpose is to make overlap intentional, useful, and traceable.

## Start-of-work protocol

Before every substantial study, critique, validation or design block:

1. read `progress/STATUS.md`;
2. read all specialist status files;
3. inspect your own open gaps and dependencies;
4. search other specialists' research for concepts related to the proposed question;
5. identify reusable findings;
6. identify existing work that may deserve replication, challenge, method comparison, or transfer validation;
7. identify any dependency or collaboration opportunity;
8. write `RELATED DOMAIN CHECK` in the planned research note.

## RELATED DOMAIN CHECK template

Every new substantial research note should contain:

```md
## RELATED DOMAIN CHECK

### Type
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

### Other / future specialist / cross-cutting
- Evidence checked:
- Reusable finding:
- Dependency or overlap:

### Overlap decision
- Reuse only / deliberate repetition / extension / contradiction review / method comparison / project-specific transfer:
- Why:
```

A section may say `Not materially relevant` only after the specialist has checked whether relevant evidence exists.

## When repeat research is appropriate

Overlapping or repeated research is legitimate when it serves at least one of these purposes:

- independent replication;
- calculation or method check;
- adversarial review;
- contradiction investigation;
- transfer validation in another context;
- comparison of standards, theories, tools or datasets;
- learning a prerequisite deeply enough to use another specialist's findings correctly;
- project-specific validation;
- obtaining a second-specialist interpretation of the same evidence.

The problem is not duplication itself. The problem is **unexamined duplication with no additional analytical value**.

## During-work protocol

When another specialist's evidence becomes relevant:

- cite/link the canonical study;
- choose whether to reuse, reproduce, challenge, or extend it;
- state that choice explicitly;
- if independently repeating it, explain the reason and keep the new record in your own writable area unless joint work is authorized;
- document any confirmation, contradiction, limitation, transfer failure, or new consequence;
- hand useful results back to the peer specialist.

A specialist is not required to stop merely because another domain has studied the topic already.

## Dependency protocol

A dependency entry in the specialist's own status should state:

- requested specialist/domain;
- exact question;
- why it affects the current work;
- evidence already checked;
- whether the current work is blocked or can continue partially;
- whether independent investigation is also planned;
- what form of answer/evidence would resolve it.

Do not edit another specialist's status to assign them work.

## Completion protocol

At the end of a substantial study:

1. save the research/evidence in the appropriate writable/canonical area;
2. distinguish SOURCE / SYNTHESIS / STUDIO JUDGMENT / OPEN / DEPENDENCY;
3. label REPLICATION / CONTRADICTION / TRANSFER VALIDATION when applicable;
4. add `HANDOFFS TO OTHER SPECIALISTS` when relevant;
5. update your own specialist status;
6. list any new incoming/outgoing dependency;
7. note any external-domain finding that changed your conclusion;
8. note deliberate overlap and what it added;
9. commit before beginning materially different work when practical.

## HANDOFFS TO OTHER SPECIALISTS template

```md
## HANDOFFS TO OTHER SPECIALISTS

### Type
- Useful finding/context:
- Canonical section to reuse or verify:
- Confirmation / contradiction / transfer note:
- Caution / scope limit:

### Color
- Useful finding/context:
- Canonical section to reuse or verify:
- Confirmation / contradiction / transfer note:
- Caution / scope limit:

### Layout / Interaction
- Useful finding/context:
- Canonical section to reuse or verify:
- Confirmation / contradiction / transfer note:
- Caution / scope limit:
```

Omit only domains for which there is genuinely no useful transfer.

## Examples of proper collaboration

### Type ↔ Layout / Interaction

Use Layout/Interaction evidence for realistic width, density, state-label and responsive contexts. Type may independently test those constraints when needed to understand typographic failure behavior. Layout may reproduce type-growth cases when the geometry itself is under test. Canonical ownership remains explicit.

### Color ↔ Layout / Interaction

Layout/Interaction provides state meaning, focus context and surface hierarchy. Color provides luminance, contrast, gamut and environmental evidence. Either side may independently reproduce a high-impact test when validation quality requires it.

### Type ↔ Color

Type provides realistic font sizes, weights, roles and numeral density. Color provides measured foreground/background and viewing-condition evidence. Either specialist may reproduce a peer calculation or rendering when the decision risk justifies independent confirmation.

## Conflict protocol

When specialists reach incompatible conclusions:

1. neither overwrites the other's file;
2. each states its claim and supporting evidence;
3. identify whether the disagreement is factual, methodological, contextual or a design judgment;
4. reproduce or extend the disputed work when useful;
5. identify what new evidence could resolve it;
6. coordinator reviews and records the resolution or leaves it explicitly unresolved.

## Concurrency protocol

To reduce Git conflicts without restricting intellectual scope:

- each specialist writes only its own canonical paths and status file during ordinary work;
- cross-domain replication is stored in the investigating specialist's own writable area and explicitly linked to peer canonical evidence;
- specialists do not edit global governance/index files unless authorized;
- specialists do not move or rename files while others may be active;
- new studies use domain prefixes;
- shared structural changes are coordinator work.

## Research-queue principle

Do not maximize the number of simultaneous studies merely to create activity.

Choose work by expected value. Strong reasons to study next include:

1. a live project need;
2. an important unresolved Foundation or validation gap;
3. a dependency that blocks another specialist;
4. a high-impact peer finding that deserves independent verification or challenge;
5. a cross-domain transfer question;
6. a genuinely new topic that expands professional capability.

The best next study is the one that most increases the reliability, breadth, transferability, or project usefulness of the shared knowledge base.