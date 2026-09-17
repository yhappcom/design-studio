# CD058 — Batch Dependency Recovery Language System

Evidence purpose: **STAGE 3 PRACTICE / COMPLETE STATE LANGUAGE / LOCALIZATION TRANSFER**.

## RELATED DOMAIN CHECK
- **Type:** use mature fallback while T021 remains provisional.
- **Color:** C052 cannot carry dependency meaning alone.
- **Layout/Interaction:** I039 owns actual dependency/action truth; L043 owns hierarchy.
- **Web:** W052 owns runtime/reconciliation provenance.
- **UX:** human comprehension and recovery performance remain OPEN.

## Semantic model
Do not collapse these states:
- `prerequisiteConfirmed`;
- `prerequisiteOutcomeUnknown`;
- `dependentWaitingForRecheck`;
- `dependentBlockedByPrerequisite`;
- `dependentSkippedByPolicy`;
- `dependentIndependentlyDenied`;
- `dependentKnownFailure`;
- `dependentEligible`;
- `dependentConfirmed`;
- `dependencyPolicyUnavailable`.

`Blocked` is not `failed`; `waiting for recheck` is not `pending execution`; `skipped by policy` is not `cancelled by user`; unknown prerequisite outcome is not known prerequisite failure.

## Action-language rules
Recovery labels must match scope and replay safety. Avoid generic `Retry all` when prerequisite reconciliation is required. Prefer action semantics such as recheck status, retry this operation, or continue eligible operations only when the Interaction/runtime contract actually supports them.

Do not claim that a dependent will run after a prerequisite unless the product contract guarantees that behavior. Do not explain malformed dependency data with invented causal language.

## Localization requirements
- keep operation/dependency IDs and workspace/object names as data parameters;
- avoid sentence fragments whose grammar depends on English word order;
- test plural/select for one/many blocked dependents;
- test pseudo-expansion, long localized prerequisite names and missing-resource fallback;
- preserve state distinctions through locale changes and history/export.

## Closure matrix
Bind CD058 resources to W052 `runId/batchId/operationId/dependencyIds/contextId/objectId/artifactId` and execute prerequisite confirmed, unknown, known failure, independent denial, policy unavailable, reload and static export cases.

## Evidence boundary
No actual Flutter/TMS/ARB round trip, linguistic review, Content Stage 3 PASS, native QA, AT or human comprehension/task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
I039 is semantic authority for execution eligibility; L043 must keep cause/action together; C052 must preserve meaning without hue; W052 supplies runtime evidence.