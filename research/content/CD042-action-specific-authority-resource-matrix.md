# CD042 — Action-specific authority resource matrix

Date: 2026-09-16
Evidence: **SYSTEMS PRACTICE / LOCALIZATION TRANSFER CONTRACT**

## RELATED DOMAIN CHECK
I023 owns required facts and action enablement; L027 owns locality; C036 owns visual encoding; W036 owns runtime binding/provenance; Type owns rendering. Content names the truth and consequence without changing it.

## Advance from CD041
`partial` is too coarse as user-facing content when different actions depend on different facts. CD042 binds content to the action-specific evidence graph.

For every constrained action maintain:
`semanticId -> object -> actionId -> knownFacts -> unknown/expired/conflictingFacts -> consequence -> safeAction -> variables -> locale -> revision`.

## Required distinctions
- **known but stale**: name the evidence event/time and avoid “current”;
- **unknown**: do not convert to failed, unchanged or absent;
- **expired by policy**: explain that confirmation is too old for this action, not that the underlying object necessarily changed;
- **conflict**: name competing revisions/sources where useful and provide compare/reconcile action;
- **partial**: state the specific unconfirmed fact that blocks the action while allowing independently safe actions to retain normal labels.

## Localization invariants
Translation may change syntax and information order but must not:
- strengthen unknown/partial/expired to confirmed;
- weaken conflict into generic warning;
- imply retry safety without I023 evidence;
- drop variables that identify object, evidence time/revision or affected action when those are required for consequence clarity.

## Executable stress set
Resource/toolchain transfer should include long object identifiers, long localized action labels, plural/select branches, date/time evidence, missing-resource fallback, pseudo-expansion and two actions on the same object with different authority requirements.

## Toolchain boundary
This environment has Python but no `flutter` or `dart` executable, so actual Flutter `gen-l10n`/ARB runtime generation cannot be claimed in this run. Existing static ARB/resource fixtures remain useful inputs, not toolchain PASS evidence.

## HANDOFFS
W036 binds resource IDs to actual rendered action states. L027 verifies local association after expansion. C036 checks non-color survival. Type consumes the unchanged stress strings during later candidate transfer.
