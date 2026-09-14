# Design Studio Research Index

`research/` is the source-grounded evidence layer of Design Studio. Research is organized by **primary specialist ownership** so that knowledge accumulates coherently and other specialists can find it before starting overlapping work.

## Canonical specialist research areas

| Domain | Canonical path | Primary owner |
| --- | --- | --- |
| Typography / Type Design | `research/type/` | Typography / Type Design Specialist |
| Color | `research/color/` | Color Specialist |
| Layout & Spatial Design | `research/layout/` | Layout & Spatial Design Specialist |
| Interaction Design | `research/interaction/` | Interaction Specialist |

Shared research that does not yet have a dedicated specialist directory may remain at `research/` root. Accessibility is currently cross-cutting and is tracked through its research/evidence plus `progress/STATUS.md`.

## Mandatory pre-study check

Before beginning a new research block, every specialist must:

1. read `progress/STATUS.md` to identify current stage, existing evidence, unresolved gaps, and immediate priorities;
2. identify which specialist owns the primary question;
3. read that domain's `README.md` and relevant existing studies;
4. inspect adjacent domains when the question depends on their knowledge;
5. avoid duplicating established research — link to the canonical study and add only genuinely new evidence, synthesis, contradiction, transfer validation, or failure analysis.

## Cross-domain awareness

Design problems routinely cross specialist boundaries. A specialist must therefore distinguish **ownership** from **dependency**.

Examples:

- Layout may depend on Type for font metrics and text expansion, and on Color for luminance hierarchy.
- Interaction may depend on Layout for spatial grouping, Type for action-label clarity, and Color for state cues.
- Color may depend on Interaction for the semantic meaning of states it visually encodes.
- Type may depend on Layout for realistic context and responsive stress testing.

A dependency does not transfer canonical ownership. Do not copy a conclusion into a second domain as if independently established. Reference the canonical source and document only the domain-specific transfer or contradiction.

## Evidence vocabulary

Every substantial research note should distinguish:

- **SOURCE** — what an authoritative source explicitly establishes;
- **SYNTHESIS** — a transferable principle inferred from evidence;
- **STUDIO JUDGMENT** — the studio's design position or reusable method;
- **OPEN** — unresolved questions or validation still required.

`PASS` is never inferred from folder placement or reading alone. Gate status is controlled by `progress/STATUS.md` and requires the evidence defined in the curriculum.

## Numbering

Study numbers are a **studio-wide chronology**, not per-folder counters. Moving a study into a specialist directory never renumbers it. This preserves links among research, exercises, critiques, status history, and future citations.

## Persistence

After each substantial completed learning block, save the evidence in the canonical domain path and update `progress/STATUS.md` when the learning state, evidence links, open gaps, or next priorities materially change. Do not wait until the end of a chat session.
