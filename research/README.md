# Design Studio Research Index

`research/` is the source-grounded evidence layer of Design Studio. Knowledge is organized by **canonical ownership** so specialists can find, reuse, validate, challenge, and extend one another's findings coherently.

Canonical ownership is not a prohibition on cross-domain learning or repeat research. Overlap is allowed when it has analytical value.

## Current specialist research areas

| Specialist | Canonical path(s) | Primary responsibility |
| --- | --- | --- |
| Typography / Type Design | `research/type/` | font, glyph, metrics, spacing, typography systems, rendering, font engineering |
| Color | `research/color/` | color science, perception, contrast, gamut, color management, palette/system behavior |
| Layout, Spatial & Interaction | `research/layout/`, `research/interaction/` | spatial composition, responsive systems, navigation, state, feedback, task/action behavior |
| Web Design | `research/web/` | real website/web-app structure, page systems, navigation, responsive composition, components, web interaction, browser/device validation |

`research/interaction/` remains separate because temporal/behavioral claims should not be mixed into spatial research files, although both are owned by the same Layout, Spatial & Interaction Specialist.

The Web Design directory is design-led. It owns web-specific application and integration rather than general software engineering. Frontend knowledge is included when it helps prototype, validate, preserve design intent, or make credible production decisions.

Shared/cross-cutting evidence such as accessibility, human factors, research methodology, information visualization or content design may remain outside these directories until a dedicated specialist is formally created.

## Study IDs

Existing legacy study numbers remain stable. New work uses domain prefixes:

- Type `T###`
- Color `C###`
- Layout `L###`
- Interaction `I###`
- Web Design `W###`
- coordinator/shared cross-cutting `X###` when needed

## Mandatory pre-study cross-domain scan

Before opening a substantial new research file, every specialist must:

1. read `progress/STATUS.md`;
2. read all four specialist status files;
3. read its own domain README(s) and relevant canonical studies;
4. search the other specialists' canonical research for related concepts;
5. identify reusable, uncertain, disputed, or test-worthy peer evidence;
6. decide whether the new work is novel, complementary, replicative, adversarial, transfer-oriented, implementation-oriented, or project-specific;
7. identify dependencies or collaboration opportunities;
8. record the scan under `## RELATED DOMAIN CHECK`.

A compliant `RELATED DOMAIN CHECK` covers Type, Color, Layout/Interaction and Web Design evidence, plus other relevant cross-cutting work.

## Overlapping and repeat research

Repeat research is allowed when the repetition itself produces confidence, comparison, transfer evidence, implementation validation, contradiction testing, or a second professional perspective.

Good reasons include:

- replication or calculation check;
- adversarial review of a high-impact claim;
- comparison of standards, theories, methods or datasets;
- transfer validation in another project, device, language, environment or discipline;
- implementation validation in an actual browser/product context;
- contradiction review;
- prerequisite learning;
- project-specific validation;
- second-specialist interpretation.

Avoid repetition whose only result is another summary of the same sources with no new analytical purpose.

## Mutual research awareness

Ownership is not isolation.

### Type ↔ Web

Type provides canonical typography knowledge. Web applies and stress-tests it under real page hierarchy, browser rendering, font loading/fallback, wrapping, localization, zoom and responsive conditions.

### Color ↔ Web

Color provides canonical color knowledge. Web applies and stress-tests it in themes, surfaces, state systems, CSS/browser/device contexts and accessibility settings.

### Layout/Interaction ↔ Web

Layout/Interaction provides canonical spatial and behavioral theory. Web turns it into complete page systems, navigation, components, responsive behavior and actual browser/input interactions.

### Web → all peers

Web hands back real-world confirmations, limitations, contradictions and transfer failures found under browser, content, responsive, accessibility, performance and implementation conditions.

All specialists remain free to independently reproduce or challenge one another's results when useful.

## Handoff rule

Every substantial research note should add `## HANDOFFS TO OTHER SPECIALISTS` when its findings can materially help another domain.

Do not copy source summaries merely for redundancy. Point to canonical evidence and explain what transfers, what was independently verified, and what changed.

## Evidence vocabulary

Use as appropriate:

- `SOURCE`
- `SYNTHESIS`
- `STUDIO JUDGMENT`
- `OPEN`
- `DEPENDENCY`
- `REPLICATION`
- `CONTRADICTION`
- `TRANSFER VALIDATION`

`PASS` is never inferred from folder placement or reading alone.

## New specialist entry

A new specialist first reads current governance and statuses, maps existing overlap and reusable evidence, and proposes a distinct role before a new canonical structure is created.

Overlap with current specialists is not automatically a reason to reject a new specialty. The question is whether the new role contributes a distinct body of expertise, methods, validation or project value.

## Persistence

After each substantial completed learning block:

1. save evidence in the appropriate specialist writable/canonical path;
2. update the owning specialist status file;
3. record dependencies and useful external findings;
4. record deliberate overlap/replication where relevant;
5. record handoffs;
6. commit before beginning materially different work when practical.

The coordinator, not individual specialists, updates `progress/STATUS.md`.
