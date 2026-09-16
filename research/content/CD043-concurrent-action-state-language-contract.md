# CD043 — Concurrent-action state language contract

Date: 2026-09-16
Purpose: **COMPLETE CONTENT SYSTEM / CONCURRENCY TRANSFER**

## RELATED DOMAIN CHECK
I024 owns changing action truth; L028 owns locality; C037 owns visual precedence; W037 owns runtime provenance; Type must render strings without changing semantics.

## Content problem
When one action is pending and another becomes blocked by newer authority, a single page-level “Updating…” or “Something changed” message is insufficient. Each affected action needs language tied to its own evidence and consequence without flooding the interface.

## Resource model
Each concurrent-action resource records:
`objectId, actionId, operationId?, semanticId, authorityRevision, certainty, consequence, safeAction, variables, locale, revision`.

Minimum semantic states:
- actionPending;
- actionBlockedNewerData;
- actionBlockedConflict;
- actionOutcomeUnknown;
- actionConfirmed;
- actionReconciledNotApplied.

## Writing invariants
- Pending is not success or failure.
- Newer data is not called an error when it is a legitimate authoritative revision.
- A late response is not described as current until reconciliation establishes that fact.
- Two actions with different authority dependencies may require different messages.
- Prefer local explanation near the affected action; use a page-level summary only as an additional orientation layer.
- Localization may reorder syntax but may not remove operation/object identity needed to disambiguate concurrent outcomes or strengthen uncertainty.

## Stress matrix
Test two simultaneous actions, long object identifiers, long localized consequence text, pseudo-expansion, plural/select where applicable, missing-resource fallback and resumption after interruption. Record semantic resource revision alongside W037 run ID.

## Evidence boundary
This contract is static content-system evidence until passed through actual localization tooling and runtime binding. Linguistic quality, comprehension and workload remain OPEN.