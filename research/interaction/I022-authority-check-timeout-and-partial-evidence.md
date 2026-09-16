# I022 — Authority Check Timeout and Partial Evidence

Date: 2026-09-16
Evidence class: **SYSTEMS PRACTICE / CONTRADICTION REVIEW / PRODUCT TRANSFER OPEN**

## RELATED DOMAIN CHECK
T021 remains independent; C035 visualizes but cannot define certainty; L025/L026 own placement; W034/W035 provide runtime/network provenance; CD040/CD041 own language.

## Problem
I021 separates restored presentation from authoritative freshness, but an authority check can itself time out, return partial fields, or produce revisions from different moments. Treating any successful response as globally current creates a new stale-but-plausible failure.

## State contract
Distinguish at minimum:
- `authorityChecking`;
- `authorityConfirmed(revision, checkedAt)`;
- `authorityUnavailable(lastKnownRevision, lastKnownAt)`;
- `authorityPartial(knownFields, unknownFields, evidenceAt)`;
- `authorityConflict(localRevision, remoteRevision)`;
- `authorityExpired(previousEvidenceAt)` when product policy defines a freshness window.

## Action-safety rule
An action may be enabled only from the subset of authoritative facts its safety preconditions actually require. A partial response must not silently authorize an action whose required field is unknown. Timeout does not convert unknown to failed or unchanged.

## Reconciliation oracle
For each action record: required facts → observed authority evidence → missing/contradictory facts → certainty → enabled/disabled action → recovery path. This creates a machine-checkable dependency rather than a generic online/offline flag.

## Evidence boundary
No production freshness window, timeout duration, idempotency rule or backend contract is invented. Those values remain product-owned evidence requirements.

## HANDOFFS TO OTHER SPECIALISTS
CD041 must preserve partial/unknown distinctions; L026 must keep required uncertainty adjacent to the affected action; C035 must not encode partial authority by color alone; W035 must capture per-request provenance.
