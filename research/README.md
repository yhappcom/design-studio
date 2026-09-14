# Design Studio Research Index

`research/` is the source-grounded evidence layer of Design Studio. Knowledge is organized by **canonical ownership** so specialists can find, reuse, validate, challenge, and extend one another's findings coherently.

Canonical ownership is not a prohibition on cross-domain learning or repeat research. Overlap is allowed when it has analytical value.

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
5. identify reusable, uncertain, disputed, or test-worthy peer-domain evidence;
6. determine whether the new work is novel, complementary, replicative, adversarial, transfer-oriented, or project-specific;
7. identify dependencies or overlap before writing;
8. record the scan in the study under `## RELATED DOMAIN CHECK`.

A compliant `RELATED DOMAIN CHECK` records what each domain contributed and whether overlap will be reused or intentionally repeated.

## Overlapping and repeat research

**Repeat research is allowed.** It is useful when the repetition itself produces confidence, comparison, transfer evidence, contradiction testing, or a second professional perspective.

Good reasons include:

- independent replication or calculation check;
- adversarial review of a high-impact claim;
- comparison of standards, theories, methods, or datasets;
- transfer validation in another project, device, language, environment, or discipline;
- contradiction review;
- prerequisite learning needed to correctly apply another specialist's work;
- project-specific validation;
- second-specialist interpretation where professional judgment differs.

Avoid repetition whose only result is another summary of the same sources with no new analytical purpose.

When intentionally overlapping existing research, label the purpose, for example:

- `REPLICATION`
- `INDEPENDENT VALIDATION`
- `TRANSFER VALIDATION`
- `CONTRADICTION REVIEW`
- `METHOD COMPARISON`
- `PROJECT-SPECIFIC RESEARCH`

The peer specialist's canonical study remains referenced even when the work is repeated independently.

## Mutual research awareness

Ownership is not isolation.

Examples:

- Type should use or test Layout/Interaction evidence for realistic width, density, action-label and state-message contexts.
- Type should use or independently verify Color evidence when a legibility claim depends on luminance/contrast.
- Color should use Type evidence for realistic text roles, sizes, weights and numeral contexts.
- Color should use or challenge Layout/Interaction evidence for real surfaces, state semantics, focus and feedback contexts.
- Layout/Interaction should use Type evidence for text growth, metrics, labels and data alignment.
- Layout/Interaction should use Color evidence for contrast, state/focus color, environmental viewing and gamut/device behavior.

A cross-domain study may reuse, reproduce, challenge, or extend another domain's work. What matters is that the relationship to the canonical evidence is explicit.

## Handoff rule

Every substantial research note should add `## HANDOFFS TO OTHER SPECIALISTS` when its findings can materially help another domain.

Do not copy entire source summaries merely for redundancy. Point to the canonical study and explain what transfers, or explain why independent repetition produced a new confirmation, limitation, contradiction, or method comparison.

## Evidence vocabulary

Every substantial research note should distinguish:

- **SOURCE** — what an authoritative source explicitly establishes;
- **SYNTHESIS** — a transferable principle inferred from evidence;
- **STUDIO JUDGMENT** — the studio's design position or reusable method;
- **OPEN** — unresolved questions or validation still required;
- **DEPENDENCY** — a question whose useful expertise may come from elsewhere;
- **REPLICATION** — deliberate reproduction/check of existing work, when applicable;
- **CONTRADICTION** — evidence conflicting with existing work, when applicable;
- **TRANSFER VALIDATION** — test of whether a finding holds in another context, when applicable.

`PASS` is never inferred from folder placement or reading alone. Gate status is controlled by the relevant specialist status and coordinator-maintained global status.

## New specialist entry

A new specialist chat first follows `coordination/ONBOARDING.md`, reads all current specialist status files, and maps existing overlap before a new canonical structure is created.

Overlap with current specialists is not automatically a reason to reject a new specialty. The question is whether the new role contributes a distinct body of expertise, methods, validation, or project value that justifies its own canonical ownership.

The coordinator/user then assigns:

- canonical path;
- status file;
- unique study-ID prefix;
- ownership boundary;
- overlap, dependency and handoff rules.

## Persistence

After each substantial completed learning block:

1. save evidence in the appropriate specialist writable/canonical path;
2. update the owning specialist status file;
3. record incoming/outgoing dependencies, useful external findings, and deliberate overlap/replication where relevant;
4. commit before beginning a materially different block when practical.

The coordinator, not individual specialists, updates `progress/STATUS.md`.