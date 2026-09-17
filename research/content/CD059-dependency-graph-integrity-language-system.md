# CD059 — Dependency Graph Integrity Language System

Evidence purpose: **STAGE 3 PRACTICE / COMPLETE SYSTEM EXTENSION / LOCALIZATION CONTRACT**. Extends CD058 from valid prerequisite/dependent outcomes to graph-integrity states.

## RELATED DOMAIN CHECK
- **Type:** T021 remains provisional; strings use mature fallback.
- **Color:** C053 must not carry graph meaning alone.
- **Layout/Interaction:** I040 defines graph/action truth; L044 defines hierarchy.
- **Web:** W053 owns runtime/resource evidence.
- **Content:** CD058 already separates waiting/blocked/skipped/failed; CD059 prevents graph-level invalidity from collapsing into those member outcomes.
- **UX:** static semantic correctness is not human comprehension evidence.

## Semantic resource model
Keep distinct resources/concepts for:
- `dependencyGraphValidationPending`
- `dependencyPolicyUnavailable`
- `dependencyReferenceMissing`
- `dependencyCycleDetected`
- `dependencyGraphInvalid`
- `dependentBlockedByGraph`
- `prerequisiteOutcomeUnknown`
- `memberIndependentlyDenied`
- `memberIndependentlyFailed`
- `memberConfirmed`
- `graphRecheckRequired`

## Language invariants
- Cycle detected ≠ prerequisite failed.
- Missing prerequisite ≠ deleted prerequisite unless authority proves deletion.
- Policy unavailable ≠ graph invalid.
- Graph invalid ≠ every member failed.
- Blocked by graph ≠ queued for automatic retry.
- Local cancellation/removal ≠ authoritative dependency rewrite.
- Do not tell users to “fix the order” unless production semantics actually expose an order they are authorized and able to change.

## Localization/toolchain stress
Exercise long labels, plural/select where counts are surfaced, pseudo-expansion, missing-resource fallback, locale change during validation, professional IDs as typed variables, RTL-sensitive relationship phrasing where applicable, and history/export wording. State selection must come from product truth, never from English text matching.

## Complete-system continuity
The content chain now covers forms/state/onboarding/retrieval/tone/localization plus complex async/offline/batch/dependency recovery. W053 should materialize graph/member states through actual resources rather than concatenated fragments.

## HANDOFFS TO OTHER SPECIALISTS
I040 supplies truth; L044 supplies information order; C053 supplies redundant visual state; W053 must execute actual resource/runtime transfer; Type must not shorten strings to protect provisional geometry.

## Evidence boundary
No Flutter/TMS/ARB round trip, linguistic review, native functional QA, production dependency integrity, AT or human comprehension/task-performance PASS is claimed.