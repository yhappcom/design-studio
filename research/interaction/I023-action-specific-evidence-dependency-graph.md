# I023 — Action-specific evidence dependency graph

Date: 2026-09-16
Evidence: **SYSTEMS PRACTICE / ADVERSARIAL VALIDATION MODEL**

## RELATED DOMAIN CHECK
L026 owns spatial association, C036 visual composition, W035 transport/runtime provenance, CD041 wording, Type rendering. Interaction owns whether an action is logically authorized by known facts.

## Advance from I022
I022 established that partial authority cannot authorize an action whose prerequisite is unknown. I023 makes this executable as a dependency graph rather than a screen-level state label.

For each action define:
`actionId -> requiredFacts[] -> evidenceSource -> freshness/policy -> certainty -> enabled/blocked -> recoveryAction`.

Example research fixture:
- `viewHistory` requires object identity only;
- `reconcile` requires operation identity + reachable authority endpoint;
- `retryMutation` requires authoritative not-committed evidence **and** documented idempotency/deduplication policy;
- `overwriteConflict` requires current authoritative revision + explicit conflict consequence.

## Adversarial cases
1. Response contains 4/5 fields but omits the one required by the action.
2. Required fact exists but its evidence is expired by product policy.
3. Two sources disagree on revision.
4. Route restoration has object ID but no operation correlation ID.
5. Authority endpoint is reachable but returns partial evidence.
6. A safe read action and unsafe mutation coexist on the same partial object.

A screen-level `partial` badge is insufficient. Each action is evaluated independently. Safe read actions may remain available while mutations stay blocked.

## Deterministic verdict
PASS requires every enabled action to have a complete evidence path for all required facts. Missing/expired/conflicting prerequisites must produce a blocked or explicitly downgraded action plus a truthful recovery path. This is logic evidence, not proof that users notice or understand the distinction.

## HANDOFFS
L027 should keep blocked reason/recovery adjacent to the affected action. CD042 should preserve fact-specific uncertainty in resources. W036 should serialize the dependency verdict with raw authority evidence. C036 checks that enabled/blocked/partial states do not collapse visually.
