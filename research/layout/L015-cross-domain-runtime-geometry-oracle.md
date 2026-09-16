# L015 — Cross-domain runtime geometry oracle

Classification: **TRANSFER VALIDATION DESIGN + UX INTEGRATION**

## Purpose
Consolidate L014’s assertions into a small set of cross-domain geometry failures that can be consumed directly by W021 without creating a separate UX owner.

## RELATED DOMAIN CHECK
T022 keeps product metrics flexible. C023/C024 requires actual adjacency. I009 owns certainty/safe action. W021 owns browser integration. CD027/CD028 requires critical semantics to survive localization. Human usability remains deferred.

## Invariants across phone / tablet-EFB / desktop
The same task must preserve:
- record identity;
- certainty state adjacent enough to the affected object to avoid attribution ambiguity;
- authorized safe action;
- recovery context;
- operational literals;
- meaningful source/reading/focus order.

Composition, density, panel count and navigation exposure may change.

## Failure oracle
A rendered state fails spatial transfer if any of these occurs:
1. status becomes visually attributable to the wrong record;
2. sticky/transient UI fully obscures focused or recovery-critical content;
3. +40% pseudo expansion removes or clips certainty/safe-action semantics;
4. 200% text/zoom forces ordinary two-axis task navigation where recomposition is feasible;
5. RTL visual reordering changes semantic/source task order or detaches LTR identifiers;
6. a breakpoint changes available safe action rather than only its presentation;
7. numeric alignment requires fixed width before Type proves the metric/feature contract;
8. a theme/state banner changes adjacency such that Color’s assumed pair is no longer the rendered pair.

## UX integration interpretation
This is expert/system evidence about coherence, not proof of discoverability, workload or task success. Those human outcomes remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- Web: instrument these eight failures in W021.
- Color: use actual adjacency from failures 2/8.
- Type: return metrics before numeric width freeze.
- Content: treat failures 3/5 as semantic-release blockers when critical meaning is lost.

## Gate result
**RUNTIME GEOMETRY ORACLE READY; BROWSER/NATIVE EXECUTION OPEN.**