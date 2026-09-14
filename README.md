# Design Studio

A professional design research and practice repository for building reusable expertise, research-grade judgment, and cross-specialist collaboration.

This repository does **not** define one reusable visual style for every product. Its purpose is to develop a reusable method of thinking, researching, composing, critiquing, validating, collaborating, and advising so that each product can arrive at its own appropriate visual language.

## Studio mandate

Design Studio participates in product work as an independent design discipline.

Default sequence:

**understand → research → frame → compose → prototype → critique → validate → reconcile with engineering → refine → document → transfer**

The long-term target is not only competent execution. Specialists are expected to progress toward publication-quality reasoning and enterprise-level advisory capability.

## Current specialist team

The current team has three active specialist roles:

1. **Typography / Type Design Specialist**
2. **Color Specialist**
3. **Layout, Spatial & Interaction Specialist**

The team can expand. New specialist chats must complete the onboarding protocol before opening a new research area.

Interaction is intentionally owned by the Layout, Spatial & Interaction Specialist. Its evidence remains in a separate `research/interaction/` directory so temporal/behavioral research is not conflated with spatial research.

Accessibility, Human Factors, research methodology and other shared concerns remain cross-cutting unless a dedicated specialist is formally created later.

## Repository structure

- `AGENTS.md` — authoritative governance, ownership, concurrency, handoff and onboarding rules
- `curriculum/` — structured study from foundations through research/advisory capability
- `research/` — source-grounded research indexed by canonical ownership
  - `research/type/` — Typography / Type Design
  - `research/color/` — Color
  - `research/layout/` — Layout / Spatial
  - `research/interaction/` — Interaction, owned by Layout & Interaction specialist
  - `research/README.md` — research-domain index and cross-domain lookup rules
- `methods/` — reusable methods, critique frameworks and gates
- `type-design/` — type-design exercises and production knowledge
- `product-design/` — product/interaction/visual-system exercises
- `case-studies/` — product-specific applications; these do not silently become universal studio rules
- `progress/` — global and specialist learning status
- `coordination/` — onboarding, collaboration and shared specialist operating prompts

## Current status files

- `progress/STATUS.md` — coordinator-maintained global summary
- `progress/TYPE_STATUS.md` — Typography / Type Design
- `progress/COLOR_STATUS.md` — Color
- `progress/LAYOUT_STATUS.md` — Layout, Spatial & Interaction

A specialist updates only its own specialist status during ordinary work. The coordinator updates global status.

## Cross-specialist research rule

Specialist ownership boundaries are **not silos**.

Before starting substantial work, every specialist must read all current specialist status files and search related research from other domains. The purpose is twofold:

1. avoid duplicate or contradictory research;
2. actively reuse evidence that another specialist has already established.

Each new substantial study records a `RELATED DOMAIN CHECK`, and each completed study records `HANDOFFS TO OTHER SPECIALISTS` when the result can help another domain.

Examples:

- Layout/Interaction work involving text growth, labels or numeric alignment uses Type evidence.
- Layout/Interaction work involving state/focus color or environmental contrast uses Color evidence.
- Color work evaluating text contrast uses Type's realistic text roles and metrics.
- Color work encoding states uses Layout/Interaction's state semantics.
- Type work under responsive or dense conditions uses Layout/Interaction's canonical spatial contexts.

Established knowledge is referenced from its canonical file rather than duplicated.

## New specialist onboarding

A newly created specialist chat must **read before writing**. It follows `coordination/ONBOARDING.md`, reviews the current team and research, searches for overlap, then proposes its unique scope.

Only after coordinator/user approval does it receive:

- a canonical path;
- a specialist status file;
- a unique study-ID prefix;
- ownership boundaries;
- dependency/handoff rules.

This allows future expert chats to join without fragmenting the knowledge base.

## Professional standard

A topic is not considered learned because it has been read once. Completion requires evidence appropriate to the topic, including:

1. authoritative-source study;
2. terminology and principle mastery;
3. original practical exercises;
4. critique against explicit criteria;
5. application in more than one context;
6. failure analysis and revision;
7. accessibility/technical/device validation where required;
8. cross-specialist integration;
9. written synthesis that future projects can reuse;
10. at advanced stages, defensible research and advisory reasoning.

The goal is not to accumulate references. The goal is to develop judgment.

## First case study

LogMate is the first major case study because it exposes demanding problems in typography, dense data, mobile/landscape composition, interaction, accessibility and product identity. LogMate-specific decisions remain product-specific; Design Studio extracts only transferable knowledge.