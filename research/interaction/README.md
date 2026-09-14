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

## Relationship with other disciplines

- **Typography / Type Design** is the canonical owner for glyph/font systems, type metrics and typographic structure.
- **Color** is the canonical owner for color systems, perception, contrast and reproduction.
- **Layout / Spatial** is the same specialist role but a separate evidence stream.

These boundaries define canonical ownership, not limits on what Interaction may study. Interaction may directly investigate Type, Color, Accessibility, Human Factors or other adjacent material for realistic behavior validation, independent replication, method comparison, contradiction review, transfer testing, prerequisite learning or project-specific work.

Interaction defines state/action semantics, while Color may encode them and Type may shape their textual presentation. The Interaction specialist may still study those adjacent channels deeply enough to validate the complete behavior.

## Mandatory cross-domain scan

Before new Interaction work:

1. read `progress/STATUS.md` and all specialist status files;
2. read `research/layout/README.md`, this README and relevant interaction/layout studies;
3. search Type and Color research for related evidence;
4. identify what can be reused, independently verified, challenged or extended;
5. identify dependencies and collaboration opportunities;
6. record a `RELATED DOMAIN CHECK` in the new study.

Existing work elsewhere is not an automatic reason to stop. Decide whether to reuse it or intentionally repeat/extend it, and document why.

After completion, add `HANDOFFS TO OTHER SPECIALISTS` when the interaction result creates useful contexts or constraints for Type or Color.

## Current studies

- `007-interaction-agency-feedback-errors.md`
- `015-directness-state-modes-reversibility.md`

Existing study numbers remain stable. New Interaction studies use `I###` IDs under the Layout, Spatial & Interaction Specialist.

## Status authority

Interaction progress is tracked in `progress/LAYOUT_STATUS.md`, not in a separate fourth specialist status file.

Current operating state: **ACTIVE — research may resume immediately**.