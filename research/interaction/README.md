# Interaction Research

This directory is the canonical home for **Interaction research owned by the Layout, Spatial & Interaction Specialist**.

It remains separate from `research/layout/` because temporal/behavioral claims should not be conflated with spatial composition claims, even though one specialist owns both streams.

## Primary scope

Research belongs here when its primary question concerns:

- affordance/signifiers, mapping, feedback, agency, familiarity and discoverability;
- actions, destinations, system state, modes, directness and reversibility;
- navigation, task flows, async/pending behavior, latency, errors, recovery and interruption;
- keyboard/pointer/touch/gesture behavior and equivalent interaction paths;
- user-facing state models and temporal behavior;
- interaction accessibility, focus-flow consequences, status communication and assistive-technology consequences where the primary issue is behavioral.

Spatial composition, grouping, grid, density and responsive geometry remain in `research/layout/`.

## Boundary with other disciplines

- **Typography / Type Design** owns glyph/font systems, type metrics and typographic structure. Interaction owns the meaning and behavior of action labels/states, while Type owns their textual/type presentation.
- **Color** owns color systems, perception, contrast and reproduction. Interaction defines state semantics; Color may encode those semantics visually.
- **Layout / Spatial** is the same specialist role but a separate evidence stream. Interaction research should reference spatial evidence instead of duplicating it.

## Mandatory cross-domain scan

Before new Interaction work:

1. read `progress/STATUS.md` and all specialist status files;
2. read `research/layout/README.md`, this README and relevant interaction/layout studies;
3. search Type and Color research for dependencies;
4. check whether the question is already covered elsewhere;
5. record a `RELATED DOMAIN CHECK` in the new study.

After completion, add `HANDOFFS TO OTHER SPECIALISTS` when the interaction result creates useful contexts or constraints for Type or Color.

## Current studies

- `007-interaction-agency-feedback-errors.md`
- `015-directness-state-modes-reversibility.md`

Existing study numbers remain stable. New Interaction studies use `I###` IDs under the Layout, Spatial & Interaction Specialist.

## Status authority

Interaction progress is tracked in `progress/LAYOUT_STATUS.md`, not in a separate fourth specialist status file.