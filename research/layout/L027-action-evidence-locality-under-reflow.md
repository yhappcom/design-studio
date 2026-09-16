# L027 — Action/evidence locality under reflow

Date: 2026-09-16
Evidence: **SYSTEMS PRACTICE / TRANSFER PROTOCOL**

## RELATED DOMAIN CHECK
I023 owns the fact dependency graph; C036 owns cue composition; W035/W036 owns browser provenance; CD041/CD042 owns wording; Type metrics remain provisional until T021 drawing critique.

## Problem
A logically correct partial-authority model can become spatially misleading after responsive recomposition. If the uncertainty explanation moves away from the action it constrains, users may read a blocked mutation as a generic page problem or miss why one action is available while another is not.

## Spatial invariant
For each action group preserve the reading/interaction sequence:
`object identity -> action-critical evidence state -> consequence/blocked reason -> action -> recovery/detail`.

The invariant is semantic adjacency, not a fixed pixel distance. It must survive wide layout, 320 CSS px reflow, actual 200% zoom, long localized strings, sticky layers and reduced visual viewport where executable.

## Geometry record
Per shared run ID record rectangles and DOM/reading order for object label, evidence-state text, affected action, recovery action, focus indicator and authored overlays. Flag:
- evidence/action association broken by column collapse;
- blocked reason visually attached to the wrong action;
- global banner substituted for local uncertainty;
- focus moved under sticky content;
- action separated from its consequence by unrelated content;
- horizontal overflow hiding state or recovery.

## Critique rule
A layout does not PASS merely because every node is visible. The action-critical evidence and its consequence must remain attributable to the correct object/action after recomposition. Human comprehension and workload remain OPEN.

## HANDOFFS
I023 supplies which facts constrain which actions. C036 verifies visual state survival. CD042 supplies localization stress strings. W036 records actual browser geometry. Type provides final metrics only after T021 drawing/general-spacing gates.
