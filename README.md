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

The team can expand. New specialist chats complete the onboarding protocol before opening a new canonical research area.

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

Specialist ownership boundaries are **not silos and not learning restrictions**.

Before starting substantial work, every specialist reads all current specialist status files and searches related research from other domains. The goals are to:

1. reuse strong evidence already available;
2. identify uncertainty or contradictions;
3. decide whether independent replication or challenge is useful;
4. avoid accidental repetition with no analytical value;
5. create better cross-domain project judgments.

Each new substantial study records a `RELATED DOMAIN CHECK`, and each completed study records `HANDOFFS TO OTHER SPECIALISTS` when the result can help another domain.

Overlap is permitted and may be desirable when it provides replication, second-check confidence, transfer validation, method comparison, contradiction review, prerequisite learning, or project-specific evidence.

Examples:

- Layout/Interaction work involving text growth, labels or numeric alignment may reuse or independently stress-test Type evidence.
- Layout/Interaction work involving state/focus color or environmental contrast may reuse or independently verify Color evidence.
- Color work evaluating text contrast uses realistic Type roles and may reproduce typography conditions where needed.
- Color work encoding states uses Layout/Interaction state semantics and may study those semantics deeply enough to validate the color system.
- Type work under responsive or dense conditions uses Layout/Interaction contexts and may independently reproduce spatial constraints for typographic testing.

Canonical ownership tells the studio where authoritative knowledge is maintained. It does not forbid another specialist from learning, reproducing, challenging, or extending that knowledge.

## New specialist onboarding

A newly created specialist chat must **read before creating a new canonical structure**. It follows `coordination/ONBOARDING.md`, reviews the current team and research, maps overlap and collaboration opportunities, then proposes its role.

Only after coordinator/user approval does it receive:

- a canonical path;
- a specialist status file;
- a unique study-ID prefix;
- ownership boundaries;
- overlap/dependency/handoff rules.

The new specialist may still learn, critique, and analyze overlapping topics during onboarding. Approval governs canonical structure, not intellectual scope.

## Professional standard

A topic is not considered learned because it has been read once. Completion requires evidence appropriate to the topic, including:

1. authoritative-source study;
2. terminology and principle mastery;
3. original practical exercises;
4. critique against explicit criteria;
5. application in more than one context;
6. failure analysis and revision;
7. accessibility/technical/device validation where required;
8. cross-specialist integration and, when useful, independent verification;
9. written synthesis that future projects can reuse;
10. at advanced stages, defensible research and advisory reasoning.

The goal is not to accumulate references. The goal is to develop judgment that improves real product decisions.

## Operating state

All three current specialists are **ACTIVE** and may resume self-directed research immediately. Live app/product project work takes priority over nonessential curriculum expansion.

## First case study

LogMate is the first major case study because it exposes demanding problems in typography, dense data, mobile/landscape composition, interaction, accessibility and product identity. LogMate-specific decisions remain product-specific; Design Studio extracts only transferable knowledge.