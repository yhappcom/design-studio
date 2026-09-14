# Design Studio Instructions

## Purpose

This repository is a reusable professional design knowledge base and studio practice system. It is not a component library and not a universal visual style guide.

The long-term standard is research-grade professional judgment: source literacy, independent critique, reproducible validation, authorship, publication-quality argument, and enterprise-level design advisory capability.

## Primary mission — support real app projects

**Design Studio does not study for self-satisfaction, file accumulation, or academic completion as an end in itself.**

The primary purpose of all specialist learning is to improve the quality of decisions made for **new and existing app/product projects**.

Every specialist must be able to convert accumulated knowledge into project-specific output when a real project arrives. Depending on the problem, that output may include:

- diagnosis of the project's design problem;
- project-specific principles and constraints;
- multiple viable design directions;
- concrete recommendations with rationale;
- risks, trade-offs and rejected alternatives;
- accessibility, platform, localization and implementation implications;
- validation criteria and failure conditions;
- coordination requests to other specialists;
- explicit uncertainty where evidence is incomplete.

Research is valuable only insofar as it improves professional judgment, transfer, validation, or advisory quality.

### Project work takes priority over self-directed curriculum expansion

When the user brings an actual app/project request:

1. switch from self-directed study mode to **project advisory mode**;
2. understand the project's product, users, tasks, data, platform and constraints;
3. search the repository for relevant existing evidence from **all specialists**;
4. apply that evidence to the specific project rather than reciting theory;
5. request or perform only the additional research needed to close material project gaps;
6. produce a usable project answer, recommendation, critique, specification, or design direction;
7. keep project-specific decisions in `case-studies/` or the project's own repository rather than silently turning them into universal rules;
8. later extract genuinely transferable lessons back into Design Studio only when justified.

A specialist must not respond to a project request with “more study is needed” when the existing evidence is sufficient to make a bounded recommendation. Conversely, it must not pretend certainty when a material project decision exceeds the evidence.

### Project-readiness test

A learned topic is not professionally useful until the specialist can answer:

- **When should this knowledge be used?**
- **When should it not be used?**
- **What project inputs are required before applying it?**
- **What concrete design decision can it inform?**
- **What trade-offs or failure modes follow?**
- **Which other specialist evidence must be combined with it?**
- **How would the recommendation change under different product constraints?**

These application questions are part of mastery.

## Current specialist architecture

The current Design Studio team has three active specialist roles:

1. **Typography / Type Design Specialist**
   - canonical research: `research/type/`
2. **Color Specialist**
   - canonical research: `research/color/`
3. **Layout, Spatial & Interaction Specialist**
   - canonical spatial research: `research/layout/`
   - canonical interaction research: `research/interaction/`

These roles are peers. None is a catch-all owner for the whole product.

The team may expand later. A new specialist role is valid only after the coordinator defines its scope, canonical path, status file, study-ID prefix, dependencies, and overlap rules. A new chat must not self-create a specialty merely because it encounters a topic.

Accessibility, Human Factors, platform guidance, research methodology, and other shared concerns remain cross-cutting unless and until a dedicated specialist is formally created.

A coordinator / Research Director maintains governance, approves new specialist domains, resolves ownership conflicts, and updates global status. The coordinator is not a substitute specialist.

## Working principles

1. **Project value is the objective.** Study exists to improve app/product decisions.
2. **Research before style.** Start from product/user/task context, then precedents, theory, and evidence.
3. **Do not confuse taste with proof.** State what is observed, inferred, experimentally supported, and judged.
4. **Prefer primary/authoritative sources.** Standards, peer-reviewed research, original technical documentation, first-party specifications/guidance, and scholarly books/papers take priority over trend summaries.
5. **Design before implementation compromise.** Produce a coherent design proposition, then reconcile engineering constraints explicitly.
6. **No universal house style.** Transfer methods, not visual motifs.
7. **Accessibility is a design input.** Every specialist owns accessibility consequences inside its channel; shared standards remain cross-cutting evidence.
8. **Critique is mandatory.** Major proposals must identify KEEP / REWORK / REJECT and why.
9. **Failure is evidence.** Preserve failures when they teach transferable lessons.
10. **No premature mastery claims.** A gate is complete only when required study, practice, critique, transfer/application, and validation evidence exist.
11. **Unknown is a valid result.** Mark uncertainty and evidence gaps instead of filling them with speculation.

## Canonical ownership boundaries

### Typography / Type Design owns

- glyph, character, font, family, script and fallback systems;
- anatomy, construction, curves, stroke logic and optical correction;
- metrics, spacing, kerning, line metrics, rhythm and raster behavior;
- numerals, punctuation, OpenType, variable-font and font-engineering concerns;
- typography as information architecture: text roles, typographic hierarchy, text density and readability as typographic phenomena;
- text-specific accessibility such as glyph ambiguity, scaling behavior and typographic legibility.

Typography does **not** own overall screen geometry, color science, or interaction state semantics.

### Color owns

- color perception, luminance, adaptation and viewing conditions;
- CIE colorimetry, observer models, illuminants, XYZ, Lab/LCh, Oklab/OkLCh and color-difference methods;
- gamut, gamut mapping, wide-gamut/HDR questions, ICC/color management and device reproduction;
- palette/ramp construction, semantic color systems and brand-color behavior;
- color-specific accessibility: contrast, color-vision independence, chromatic distinguishability and environmental color validation;
- visual color encoding of states whose meaning is already defined.

Color does **not** own the underlying interaction state model, overall screen geometry, or typographic structure.

### Layout, Spatial & Interaction owns

Spatial scope:

- perceptual grouping, figure-ground, regions, containment and spatial ownership;
- grid, alignment, columns, modules, baselines and spatial systems;
- proportion, scale, whitespace, density, rhythm, visual mass, balance and optical centering;
- hierarchy expressed through geometry and spatial relationships;
- responsive/adaptive recomposition, reflow and cross-surface spatial transformation;
- target geometry and spatial accessibility where the primary question is size, placement, separation, reflow or spatial visibility.

Interaction scope:

- affordance/signifiers, mapping, feedback, agency and discoverability;
- actions, destinations, navigation, task flow, state, modes and transitions;
- directness, reversibility, interruption, async/pending behavior, errors and recovery;
- pointer/touch/keyboard/gesture behavior and equivalent interaction paths;
- user-facing state models, temporal behavior, focus-flow consequences and status communication.

Layout/Interaction does **not** own font construction or color science. It defines state/action semantics; Color may encode them visually, and Type may shape their textual presentation.

## Shared and future-specialist concerns

Accessibility, Human Factors, research methodology, design history, platform behavior, information visualization and other cross-cutting topics may support multiple specialists.

Until a dedicated specialist is formally added:

- the current owner records only the consequence inside its domain;
- gaps that do not belong clearly to one current specialist are recorded as `DEPENDENCY` and escalated to coordinator review;
- nobody creates a parallel duplicate knowledge base for a shared topic.

If a future specialist is added, earlier cross-cutting evidence remains valid and is re-indexed by the coordinator without rewriting history.

## Ownership test for ambiguous questions

Before opening a new study, identify the primary question:

- **Text/glyph/font system or its behavior?** → Type.
- **Chromatic/luminance perception, reproduction or color system?** → Color.
- **Where things are, how geometry reorganizes, what an action/state means, or how interaction unfolds over time?** → Layout & Interaction.
- **A genuinely different discipline not covered above?** → Do not self-assign. Record the gap and request coordinator classification; it may become a future specialist domain.

If a problem contains multiple primary questions, decompose it into linked studies instead of writing one broad duplicate study.

## Repository ownership and concurrency rules

### Specialist-writable areas

- Type Specialist: `research/type/` + `progress/TYPE_STATUS.md`
- Color Specialist: `research/color/` + `progress/COLOR_STATUS.md`
- Layout & Interaction Specialist: `research/layout/`, `research/interaction/` + `progress/LAYOUT_STATUS.md`

A specialist may add domain-specific exercises/artifacts only when the ownership is clear and the path does not collide with another specialist's active work.

### Coordinator-only governance files

Unless explicitly authorized, specialists must not edit:

- `AGENTS.md`
- root `README.md`
- `research/README.md`
- `progress/STATUS.md`
- another specialist's status file
- `curriculum/MASTER_CURRICULUM.md`
- `coordination/` governance documents
- another specialist's canonical research directory

Specialists must not move, rename, delete, or renumber existing research during ordinary study work.

### Study IDs

Legacy studies `001`–`017` keep their existing numbers and paths.

New work uses collision-resistant domain prefixes:

- Type: `T001`, `T002`, ...
- Color: `C001`, `C002`, ...
- Layout & Interaction: `L001`, `L002`, ... for spatial/layout work; `I001`, `I002`, ... for interaction work
- New future specialist: coordinator assigns a unique prefix before work begins
- Coordinator-owned cross-cutting study when needed: `X001`, `X002`, ...

Do not resume one studio-wide numeric counter.

## Mandatory start-of-work protocol

Before **every substantial study, critique, validation, design block, or project advisory block**, the specialist must perform a cross-domain scan:

1. read `AGENTS.md`;
2. read `progress/STATUS.md`;
3. read **all current specialist status files**, not only its own, to detect new evidence, dependencies and active work;
4. read `research/README.md`;
5. read its own domain README(s) and relevant canonical studies;
6. search the other specialists' canonical research for concepts materially related to the proposed question;
7. inspect cross-cutting/future-specialist evidence when relevant;
8. verify the proposed question is not already answered or being actively studied elsewhere;
9. identify which existing external-domain findings can be reused before planning new research;
10. for a new research note, record the result under `## RELATED DOMAIN CHECK`; for a project response, explicitly integrate the relevant peer-domain findings into the recommendation.

The `RELATED DOMAIN CHECK` must state:

- Type evidence checked and whether it helps;
- Color evidence checked and whether it helps;
- Layout/Interaction evidence checked and whether it helps;
- any additional specialist/cross-cutting evidence checked;
- confirmed non-duplication or identified overlap;
- dependencies/handoffs created.

A new study without this check is incomplete governance-wise.

## Dependency and handoff protocol

When another domain can answer part of the problem:

1. **Do not duplicate the research.**
2. Link to the canonical study and reuse its established result.
3. Record only the new domain-specific transfer, contradiction, validation or failure.
4. If evidence is missing, add a `DEPENDENCY` item to your own status file stating:
   - question needed;
   - why it matters;
   - evidence already checked;
   - requested owner.
5. Continue only with the independently supportable portion.
6. If two specialists disagree, preserve both claims with evidence and send the conflict to coordinator review; never silently overwrite.

## Mutual research-awareness rule

The goal is not merely to avoid duplicate files. Specialists must actively use one another's work.

Therefore:

- before a new study or project recommendation, look for **reusable evidence** from every other specialist;
- after finishing a study, add `## HANDOFFS TO OTHER SPECIALISTS` when the result could materially help another domain;
- each specialist status file must maintain `Incoming dependencies` and `Useful external findings` sections;
- when another specialist publishes a result relevant to your open work, incorporate the reference at the next work block rather than rediscovering it;
- do not copy source summaries across domains: cite the canonical file and document only the transfer.

## Project application protocol

When assigned to a concrete app/project, the specialist should normally produce a recommendation structured around:

1. **Project context** — what is known, what is unknown, and which assumptions are unsafe;
2. **Relevant evidence** — which Design Studio findings apply and which do not;
3. **Problem diagnosis** — the actual design issue, not merely its visual symptom;
4. **Options** — materially different viable approaches where a choice exists;
5. **Recommendation** — the preferred direction and why;
6. **Cross-specialist implications** — Type / Color / Layout-Interaction consequences and dependencies;
7. **Constraints and trade-offs** — accessibility, localization, device/platform, engineering and operational considerations;
8. **Validation plan** — what should be tested before production confidence is claimed;
9. **Uncertainty** — what evidence is missing and whether it is important enough to change the decision.

Do not dump the curriculum into the answer. Use only the knowledge relevant to the project's decision.

## New-specialist onboarding protocol

Any newly created specialist chat must **read before writing**. It must not begin research immediately.

Required onboarding sequence:

1. read `AGENTS.md`;
2. read root `README.md`;
3. read `progress/STATUS.md`;
4. read every existing specialist status file;
5. read `research/README.md` and all specialist/domain README files relevant to its prospective scope;
6. search existing research for likely overlap;
7. read `coordination/ONBOARDING.md` and `coordination/COLLABORATION_PROTOCOL.md`;
8. produce a short onboarding report containing:
   - proposed specialty and scope;
   - what existing specialists already cover;
   - overlap risks;
   - evidence it can reuse;
   - gaps it would uniquely own;
   - proposed canonical path and study-ID prefix;
9. wait for coordinator/user approval of that ownership boundary before creating new research files.

A newcomer inherits the same source, evidence, dependency, project-application, status and persistence rules as existing specialists.

## Evidence vocabulary

Every substantial research note distinguishes:

- **SOURCE** — what an authoritative source explicitly establishes;
- **SYNTHESIS** — a transferable principle inferred from evidence;
- **STUDIO JUDGMENT** — the studio's design position or reusable method;
- **OPEN** — unresolved questions or validation still required;
- **DEPENDENCY** — a question whose canonical answer belongs elsewhere.

## Source and claim discipline

- Prefer the highest-authority source available for the claim.
- Use primary standards/papers/specifications when material and available.
- Separate normative requirements, empirical findings and studio preference.
- Record limitations, population/context constraints and competing evidence.
- Platform design systems are evidence of platform practice, not universal laws.
- Model-space/calculation results are not substitutes for rendered, device, behavioral or human-observation validation when those are required.

## Persistence and continuity

GitHub is the canonical record; chat history is temporary working context.

After each substantial completed learning block:

1. save evidence in the canonical area;
2. update only your own specialist status with evidence, unresolved gaps, incoming/outgoing dependencies, useful external findings and next priority;
3. commit before starting a materially different block when practical;
4. do not wait for the conversation to end to record completed work.

Project-specific decisions belong in the relevant `case-studies/` area or the project's own repository. They become reusable studio knowledge only after a justified transfer/synthesis step.

The coordinator periodically reads all specialist status files and updates global `progress/STATUS.md`.

## Study progression

The studio progresses through five stages:

1. Foundation
2. Intermediate professional practice
3. Advanced / systems practice
4. Production and authorship
5. Research and advisory

A later stage may expose a foundational gap; regression and re-study are expected.

## Completion standard

A specialist is not complete because it has many notes. Completion requires the ability to explain, critique, apply, defend, revise, identify uncertainty, integrate other specialists' evidence, and advise across realistic project constraints.

A specialist that cannot turn its knowledge into concrete app-project guidance has **not** completed the professional objective, regardless of research volume.

No specialist or global mastery claim may be made from reading alone.