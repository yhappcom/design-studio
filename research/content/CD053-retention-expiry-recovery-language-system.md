# CD053 Retention Expiry / Recovery Language System

Evidence mode: SYSTEMS PRACTICE / TRANSFER VALIDATION.

## Purpose
Extend CD052 so language does not turn a displayed retention countdown or cached policy into a promise of recoverability or confirmed irreversibility.

## RELATED DOMAIN CHECK
I034 owns actual recovery capability and safe action. L038 owns hierarchy/locality. C047 owns visual state. W047 owns runtime evidence. T021 tests unchanged operational strings and remains provisional.

## Semantic resources
Keep distinct concepts/resources for: recoveryAvailableConfirmed, recoveryBoundaryKnown, recoveryBoundaryApproaching, recoveryRecheckRequired, recoveryAvailabilityUnknown, recoveryUnavailableConfirmed, retentionPolicyUnknown, authorityUnavailable, recoveryRequested, recoveryOutcomeUnknown, recoveryConfirmed, and historyOfPriorDeletion.

A displayed date such as “Available until …” is allowed only when product authority defines the boundary and its semantics. If authority cannot currently verify recovery after a boundary, say that availability cannot be confirmed; do not silently change to “Expired” or “Deleted permanently.”

## Wording constraints
- Do not use Undo for a new consequential recovery mutation unless Interaction/product authority proves true reversal.
- Do not promise a fixed recovery period from cached/local configuration.
- Do not infer permanent loss from a client countdown reaching zero.
- Distinguish cannot verify from unavailable confirmed.
- Preserve object identity and whether a later object is restored or newly recreated.

## Localization tests
Round-trip the resources through the actual product toolchain with pseudo-expansion, long date/time formats, locale/timezone change, missing-resource fallback, RTL-ready review, offline return and history/export. Translation may reorder grammar but must not strengthen certainty.

## Evidence boundary
No actual Flutter/TMS/ARB round trip, linguistic review, AT or human comprehension/task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W047 must capture resource revision and rendered wording at both sides of the boundary. C047 must keep non-color semantics visible. L038 must accommodate expanded consequence/evidence/action wording. Type should render identifiers unchanged after T021 repair.