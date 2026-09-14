# Design Studio Instructions

## Purpose

This repository is a reusable professional design knowledge base and studio practice system. It is not a component library and not a universal visual style guide.

## Working principles

1. **Research before style.** Start from product/user/task context, then precedents, theory, and evidence.
2. **Do not confuse taste with proof.** State what is observed, what is inferred, and what is a design judgment.
3. **Prefer primary/authoritative sources.** Academic programs, standards, platform guidance, original type-design documentation, books/papers, and first-party technical specifications take priority over trend summaries.
4. **Design before implementation compromise.** Produce the strongest coherent design proposition first. Engineering feasibility is then reconciled explicitly.
5. **No universal house style.** Transfer methods, not visual motifs. Every product may require a different visual language.
6. **Typography is structural.** Type, spacing, hierarchy, and numeric behavior are part of information architecture.
7. **Accessibility is a design input.** It is not a final compliance pass.
8. **Critique is mandatory.** Every major proposal must identify what is KEEP / REWORK / REJECT and why.
9. **Failure is evidence.** Preserve rejected experiments when they teach a transferable lesson.
10. **No premature mastery claims.** A curriculum gate is complete only when study, practice, critique, and application evidence all exist.

## Knowledge separation

- `research/` contains source-grounded research and must preserve source framing.
- `methods/` contains synthesized reusable methods and clearly identified design judgments.
- `case-studies/` contains product-specific decisions and experiments.
- Product-specific decisions must never silently become universal studio rules.

### Canonical specialist research ownership

Source-grounded research is organized by primary specialist ownership:

- `research/type/` — Typography / Type Design Specialist
- `research/color/` — Color Specialist
- `research/layout/` — Layout & Spatial Design Specialist
- `research/interaction/` — Interaction Specialist

`research/README.md` is the canonical domain index. A study number is studio-wide chronology and does not reset or change when a file moves into a specialist directory.

### Mandatory cross-domain awareness

Before beginning any substantial research, critique, or product-design block:

1. read `progress/STATUS.md` to identify current evidence, unresolved gaps, and immediate priorities;
2. identify the primary specialist owner of the question;
3. read `research/README.md`, that specialist directory's `README.md`, and the relevant existing studies;
4. inspect adjacent specialist domains whenever the decision depends on their evidence;
5. reference the canonical study instead of duplicating established knowledge;
6. add a new file only for genuinely new evidence, synthesis, contradiction, transfer validation, practice, or failure analysis.

Cross-domain dependencies are expected. For example:

- Layout must consult Type when font metrics, text growth, numerals, or typographic hierarchy affect geometry;
- Layout and Interaction must consult Color when luminance, contrast, state color, or gamut behavior affects a design decision;
- Interaction must consult Layout when grouping, target placement, or spatial context affects action understanding;
- Color must consult Interaction when a color is being used to encode a state or action;
- Type must consult Layout when typographic choices are evaluated inside responsive or dense interfaces.

**Ownership does not imply isolation.** A specialist must know relevant conclusions from the other specialist domains before making a dependent judgment.

When an adjacent domain's evidence is incomplete, mark that dependency explicitly rather than filling the gap with speculation.

## Persistence and continuity

GitHub is the canonical record of Design Studio learning. Chat history is a temporary working context and must not be treated as the persistence boundary.

After every substantial study, practice, critique, validation, or other completed learning block:

1. save the resulting research, exercise, critique, or other evidence in the appropriate repository location;
2. update `progress/STATUS.md` whenever the learning state, evidence links, unresolved gaps, or immediate next priorities have materially changed;
3. commit the changes before beginning a materially different learning block when practical;
4. do not wait for the conversation to end before recording progress.

A chat session may end or be replaced at any time. Future sessions must resume from the repository state and relevant evidence rather than assuming access to prior chat history.

Do not record unfinished speculation as established knowledge merely to create a checkpoint. If a learning block is incomplete, preserve only clearly identified work-in-progress evidence when it is useful and mark its status accordingly.

## Study progression

The studio progresses through four stages:

1. Foundation
2. Intermediate professional practice
3. Advanced / systems practice
4. Production and authorship

A later stage may reveal gaps in an earlier stage; regression for re-study is expected.

## Completion standard

The Design Studio learning program is complete only when the curriculum completion matrix is satisfied with evidence. Even after completion, the repository remains a living professional practice archive.
