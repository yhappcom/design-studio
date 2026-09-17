# I059 — Material Ownership Failure Localization

## PURPOSE
**TRANSFER VALIDATION / CONTRADICTION REVIEW.** Localize the repeated MintTap ListTile feedback-layer assertion to its actual paint-owner boundary before changing interaction behavior.

## RELATED DOMAIN CHECK
Type T040/T041 must not absorb interaction defects; Color C071 treats TOKEN_PASS/RENDER_FAIL as failure; Layout L063 localizes spatial/ancestor ownership; Web W071 preserves runtime identity; Content CD077 preserves labels/consequences.

## EXECUTED EVIDENCE
Run `35255971379` produced repeated Flutter assertions stating that ListTile background/ink splashes may be invisible because a background-colored `DecoratedBox` sits between ListTile and the nearest Material. The framework explicitly recommended either giving ListTile its own Material or removing the intermediate background decoration. The failing diagnostics include Settings destinations and other ListTile instances, so this is a shared containment/paint-owner defect rather than evidence that tap actions should be removed.

## PRACTICE
For every affected ListTile family, record ancestor chain `ListTile → intermediate decorated surface → nearest Material`, then choose the smallest structural repair that preserves:
- onTap/action semantics;
- idle/focus/pressed/selected visibility;
- target geometry;
- keyboard/focus traversal where applicable;
- section containment and visual grouping.

## CRITIQUE
A repair that silences the assertion by deleting `onTap`, splash, focus or selected state is FAIL. A repair that changes semantic state truth to fit the paint model is FAIL. Material ownership is implementation structure supporting the interaction contract, not a reason to weaken it.

## VALIDATION
Re-run the 1024×768 major-destination traversal. PASS requires zero framework paint-ownership assertions plus observable activation and state feedback. Pending/known-failure and ambiguous/reconcile families remain a subsequent I058 gate.

## OPEN
No repaired runtime PASS, keyboard/browser/AT/physical-device or human usability PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Color validates visible state redundancy after repair; Layout checks containment geometry; Web promotes only the repaired same-build run; Content verifies labels and consequences remain unchanged.