# Cross-Specialist Collaboration Protocol

This document defines how Design Studio specialists cooperate without duplicating research or missing useful findings from peers.

## Current team

- Typography / Type Design Specialist
- Color Specialist
- Layout, Spatial & Interaction Specialist

Future specialists may be added through `coordination/ONBOARDING.md`.

## Core rule

**Before researching, check what the others already know. After researching, tell the others what became useful to them.**

The purpose is not merely to prevent duplicate files. It is to create a cumulative shared research system.

## Start-of-work protocol

Before every substantial study, critique, validation or design block:

1. read `progress/STATUS.md`;
2. read all specialist status files;
3. inspect your own open gaps and dependencies;
4. search other specialists' research for concepts related to the proposed question;
5. identify reusable findings;
6. verify that no specialist is already studying the same primary question;
7. identify any dependency that belongs elsewhere;
8. write `RELATED DOMAIN CHECK` in the planned research note.

## RELATED DOMAIN CHECK template

Every new substantial research note should contain:

```md
## RELATED DOMAIN CHECK

### Type
- Evidence checked:
- Reusable finding:
- Dependency or overlap:

### Color
- Evidence checked:
- Reusable finding:
- Dependency or overlap:

### Layout / Interaction
- Evidence checked:
- Reusable finding:
- Dependency or overlap:

### Other / future specialist / cross-cutting
- Evidence checked:
- Reusable finding:
- Dependency or overlap:

### Duplication decision
- Why this study is genuinely new:
```

A section may say `Not materially relevant` only after the specialist has checked whether relevant evidence exists.

## During-work protocol

When another specialist's evidence becomes relevant:

- cite/link the canonical study;
- do not reproduce the entire source review;
- document only the new consequence inside your domain;
- if the canonical evidence is insufficient, add a dependency rather than silently completing the other specialist's research;
- if a contradiction appears, preserve both positions and escalate it.

## Dependency protocol

A dependency entry in the specialist's own status must state:

- requested specialist/domain;
- exact question;
- why it affects the current work;
- evidence already checked;
- whether the current work is blocked or can continue partially;
- what form of answer/evidence would resolve it.

Do not edit another specialist's status to assign them work.

## Completion protocol

At the end of a substantial study:

1. save the canonical research/evidence;
2. distinguish SOURCE / SYNTHESIS / STUDIO JUDGMENT / OPEN / DEPENDENCY;
3. add `HANDOFFS TO OTHER SPECIALISTS` when relevant;
4. update your own specialist status;
5. list any new incoming/outgoing dependency;
6. note any external-domain finding that changed your conclusion;
7. commit before beginning materially different work when practical.

## HANDOFFS TO OTHER SPECIALISTS template

```md
## HANDOFFS TO OTHER SPECIALISTS

### Type
- Useful finding/context:
- Canonical section to reuse:
- Caution / scope limit:

### Color
- Useful finding/context:
- Canonical section to reuse:
- Caution / scope limit:

### Layout / Interaction
- Useful finding/context:
- Canonical section to reuse:
- Caution / scope limit:
```

Omit only domains for which there is genuinely no useful transfer.

## Examples of proper reuse

### Type → Layout / Interaction

Use font metrics, line wrapping, numeral alignment, localization and scaling evidence to stress spatial systems and action/status labels.

Do not let Layout independently derive font metrics.

### Layout / Interaction → Type

Use real width constraints, state labels, dense-data contexts and responsive conditions to test Type decisions.

Do not let Type independently define navigation or state semantics.

### Color → Layout / Interaction

Use luminance, contrast, gamut, environment and state/focus color evidence in actual interaction contexts.

Do not let Layout derive a parallel color science model.

### Layout / Interaction → Color

Provide state meaning, focus context, surface hierarchy and real interaction flows so Color evaluates the right visual signals.

Do not let Color invent the state machine.

### Type → Color

Provide realistic font sizes, weights, roles, numeral density and localized text contexts for contrast testing.

### Color → Type

Provide measured foreground/background and viewing-condition evidence when typographic legibility claims depend on color.

## Conflict protocol

When specialists reach incompatible conclusions:

1. neither overwrites the other's file;
2. each states its claim and supporting evidence;
3. identify whether the disagreement is factual, methodological, contextual or a design judgment;
4. identify what new evidence could resolve it;
5. coordinator reviews and records the resolution or leaves it explicitly unresolved.

## Concurrency protocol

To reduce Git conflicts:

- each specialist writes only its own canonical paths and status file;
- specialists do not edit global governance/index files;
- specialists do not move or rename files while others may be active;
- new studies use domain prefixes;
- shared structural changes are coordinator work.

## Research-queue principle

Do not maximize the number of simultaneous studies.

Prefer:

1. close an existing evidence gap;
2. answer an incoming dependency that blocks another specialist;
3. validate an existing claim;
4. only then expand into a new topic.

The best next study is the one that most increases the reliability and usefulness of the shared knowledge base, not the one that creates the most files.