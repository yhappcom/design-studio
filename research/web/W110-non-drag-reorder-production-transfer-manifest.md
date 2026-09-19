# W110 — Non-drag reorder production transfer manifest

## PURPOSE
Move the long-standing non-drag reorder blocker from abstract requirement to an executable production-transfer plan. Avoid another isolated Chromium micro-test.

## RELATED DOMAIN CHECK
T079, C110, I097, L101, CD116 and W109 checked. W110 integrates; it does not replace peer ownership.

## SOURCE BASELINE
WCAG 2.2 SC 2.5.7 requires a non-drag single-pointer path for author-implemented drag functionality unless an exception applies. W3C G219 explicitly illustrates stepwise arrow controls and destination selection. Keyboard support is evaluated separately and is not by itself a 2.5.7 substitute. SC 2.5.8 separately constrains pointer target size/spacing.

## PRODUCTION SCENARIOS
Use stable 7-item fixture IDs and execute both candidates if implementation cost permits:
A. stepwise up/down;
B. explicit destination selection.

Runs:
1. first→middle, middle→adjacent, last→middle;
2. repeated moves;
3. boundary unavailable actions;
4. Undo;
5. save/persistence failure→retry;
6. route away/back and reload;
7. drag path versus non-drag path resulting-order equivalence.

## MANIFEST
Capture per run:
- production build/hash and route;
- engine/version/input modality;
- item IDs/order before/proposed/after/recovered;
- action and target rectangles;
- focus owner and accessibility name/state/status payload;
- actual font family/features and wrap/truncation;
- rendered semantic state IDs/treatments;
- transaction/inverse/persistence evidence;
- viewport, scroll/sticky regions;
- enlarged text, WCAG text spacing, narrow reflow;
- light/night/forced-colors where applicable.

Execute primary served engine REPLICATION twice, then independent engine. Physical touch device and screen reader remain separate evidence levels.

## PASS CONDITIONS
- same underlying reorder result is achievable by click/tap without dragging;
- no hover-only dependency;
- focus/item identity remains coherent after movement;
- target geometry satisfies SC 2.5.8 or a documented valid exception;
- visible/accessibility status represents actual transaction truth;
- Undo/persistence/route-return preserve canonical order semantics;
- drag and non-drag paths converge on the same canonical order for equivalent intent.

## PERFORMANCE EVIDENCE
Interaction timing from local traces may be LAB diagnostic evidence only. Lighthouse/DevTools/CI/synthetic traces are not FIELD LCP/INP/CLS. Field claims require provenance-bearing representative RUM/aggregate.

## HUMAN EVIDENCE BOUNDARY
No discoverability, preference, workload, error-rate, AT comprehension or representative-pilot PASS is inferred from browser execution.

## HANDOFFS
Return actual font/wrap failures to Type, state-treatment failures to Color, geometry/focus failures to Layout/Interaction, semantic/status mismatches to Content.

## OPEN
Actual LogMate implementation and execution; independent engine; physical iPad/mobile; screen reader; representative human evidence.