# CD051 — Concurrent Branch / Merge Language System

## PURPOSE
Extend CD050 so language preserves partial-order truth when two valid branches are concurrent and cannot honestly be called earlier/latest.

## SEMANTIC RESOURCES
Keep distinct concepts/resources for: `concurrentChanges`, `orderingUnknown`, `mergeRequired`, `mergeInProgress`, `mergeConflict`, `mergeOutcomeUnknown`, `mergeConfirmed`, `branchSuperseded`, `authorityUnavailable`, and `currentAfterMerge`.

Avoid “latest version” when the product only knows that one event has a larger client timestamp or arrived later. Prefer wording that states the comparison basis when material: “Changes from two sources need review”, “These changes cannot be ordered automatically”, or equivalent localized semantics. Do not call a branch “older” unless the authoritative ordering contract supports that claim.

Merge copy must state consequence and safe next action. A lost merge response is not “merge failed”; it is outcome unknown until recheck/reconciliation. Historical branch wording remains historical after merge and is not retroactively rewritten into a false total order.

## LOCALIZATION CONTRACT
Translation may reorder grammar and date/time presentation but must preserve branch identity, incomparability, uncertainty, merge consequence and action identity. Pseudo-expansion must cover branch labels + provenance + consequence + recovery together. Missing-resource fallback must not collapse `concurrentChanges` into generic error/success.

## RELATED DOMAIN CHECK
- I032 supplies actual comparability/action truth.
- L036 supplies information hierarchy and reflow constraints.
- C045 ensures meaning survives without color.
- W045 supplies actual runtime/resource provenance.
- Type receives unchanged operational strings after T021 gates.

## HANDOFFS TO OTHER SPECIALISTS
W045 should record resource IDs/revision/locale beside branch and merge IDs. Layout must accommodate full uncertainty/recovery language. Color must not replace these distinctions with hue-only labels.

## EVIDENCE BOUNDARY
Semantic/localization contract only. No Flutter/TMS/ARB round trip, linguistic review, AT, or human comprehension/task-performance PASS.