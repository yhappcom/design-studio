# Design Studio Research Index

`research/` is the source-grounded evidence layer of Design Studio. Knowledge is organized by **canonical ownership** so specialists can reuse one another's findings without duplicating research.

## Current specialist research areas

| Specialist | Canonical path(s) | Primary responsibility |
| --- | --- | --- |
| Typography / Type Design | `research/type/` | font, glyph, metrics, spacing, typography systems, rendering, font engineering |
| Color | `research/color/` | color science, perception, contrast, gamut, color management, palette/system behavior |
| Layout, Spatial & Interaction | `research/layout/`, `research/interaction/` | spatial composition, responsive systems, navigation, state, feedback, task/action behavior |

`research/interaction/` remains a separate evidence directory because temporal/behavioral claims should not be mixed into spatial research files, but it is owned by the same Layout, Spatial & Interaction Specialist.

Shared/cross-cutting evidence such as accessibility or human factors may remain outside these directories until a dedicated specialist is formally created.

The team can expand. A new specialist receives a canonical research path only after coordinator/user approval under `coordination/ONBOARDING.md`.

## Legacy numbered files

Legacy numbered files remaining directly under `research/` for moved domains are **compatibility pointers only** unless they contain genuinely shared evidence. They preserve older references and are not locations for new specialist content.

Existing study numbers `001`–`017` remain stable. New work uses domain prefixes defined in `AGENTS.md`.

## Mandatory pre-study cross-domain scan

Before opening a new research file, every specialist must:

1. read `progress/STATUS.md`;
2. read **all current specialist status files**;
3. read its own domain README(s) and relevant canonical studies;
4. search the other specialists' canonical research for related concepts;
5. identify reusable external-domain evidence;
6. verify the question is not already answered or actively being studied elsewhere;
7. identify dependencies or overlap before writing;
8. record the scan in the study under `## RELATED DOMAIN CHECK`.

A compliant `RELATED DOMAIN CHECK` records whether Type, Color, Layout/Interaction, and any additional relevant specialist/cross-cutting evidence were checked, what can be reused, and what dependency/handoff was created.

## Mutual research awareness

Ownership is not isolation.

Examples:

- Type should use Layout/Interaction evidence for realistic width, density, action-label and state-message contexts.
- Type should use Color evidence when a legibility claim depends on luminance/contrast.
- Color should use Type evidence for realistic text roles, sizes, weights and numeral contexts.
- Color should use Layout/Interaction evidence for real surfaces, state semantics, focus and feedback contexts.
- Layout/Interaction should use Type evidence for text growth, metrics, labels and data alignment.
- Layout/Interaction should use Color evidence for contrast, state/focus color, environmental viewing and gamut/device behavior.

A dependency does not transfer canonical ownership. Reference the canonical source and document only the domain-specific transfer, contradiction, validation or failure that is genuinely new.

## Handoff rule

Every substantial research note should add `## HANDOFFS TO OTHER SPECIALISTS` when its findings can materially help another domain.

Do not copy entire source summaries into the receiving domain. Point to the canonical study and explain what consequence transfers.

## Evidence vocabulary

Every substantial research note should distinguish:

- **SOURCE** — what an authoritative source explicitly establishes;
- **SYNTHESIS** — a transferable principle inferred from evidence;
- **STUDIO JUDGMENT** — the studio's design position or reusable method;
- **OPEN** — unresolved questions or validation still required;
- **DEPENDENCY** — a question whose canonical answer belongs elsewhere.

`PASS` is never inferred from folder placement or reading alone. Gate status is controlled by the relevant specialist status and coordinator-maintained global status.

## New specialist entry

A new specialist chat must not create research immediately. It first follows `coordination/ONBOARDING.md`, reads all current specialist status files, searches for overlap, and submits a proposed scope. The coordinator/user then assigns:

- canonical path;
- status file;
- unique study-ID prefix;
- ownership boundary;
- dependencies and handoff rules.

This prevents a new specialist from recreating knowledge that already exists in Type, Color, Layout/Interaction, or another future domain.

## Persistence

After each substantial completed learning block:

1. save evidence in the canonical path;
2. update the owning specialist status file;
3. record incoming/outgoing dependencies and useful external findings;
4. commit before beginning a materially different block when practical.

The coordinator, not individual specialists, updates `progress/STATUS.md`.