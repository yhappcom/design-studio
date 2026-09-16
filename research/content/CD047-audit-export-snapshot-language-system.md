# CD047 — Audit Export Snapshot Language System

Evidence purpose: **STAGE 3 SYSTEMS PRACTICE + TRANSFER VALIDATION**.

## RELATED DOMAIN CHECK
I028 defines snapshot/provenance truth; L032 defines static hierarchy; C041 requires non-color semantics; W041 owns runtime export/print execution; Type custom metrics remain provisional.

## Semantic requirement
An exported audit artifact must not sound live merely because the in-app source was live. Content must distinguish:
- `snapshotGeneratedAt` — when the artifact was generated;
- `authorityConfirmedAt` — when current authority was last confirmed, if known;
- `authorityUnavailableAtExport`;
- `historyIncomplete` / `historyUnavailable` / `historyNotLoaded` as distinct states;
- event observed time versus reconciliation time;
- `recheckCurrentState` as a route/action only when the product can actually provide it.

## Content model
Header: object identity + snapshot status + generation-time semantics.
Current section: authoritative consequence or explicit limitation.
History: immutable event semantics from CD046 with operation/event identity.
Footer/metadata: provenance, omitted-data disclosure and recheck path where supported.

## Localization contract
Locale realization may reorder grammar but may not:
- turn snapshot into current/live;
- collapse observed and reconciled timestamps;
- convert unknown actor/source into system attribution;
- translate professional identifiers as ordinary localized numbers;
- hide omitted-history disclosure to preserve layout.

Pseudo-expansion must include long snapshot labels, timestamps, identifiers, intervention reasons and missing-history explanations. Missing resource fallback must preserve semantic ID/certainty rather than substituting a generic success/error string.

## Evidence boundary
Static semantic contract only. No Flutter/TMS/ARB round trip, linguistic review, human comprehension or regulatory-record wording acceptance is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W041 should execute these resources in export/print; L032 must reserve space for provenance; C041 must not rely on color-only state references; I028 remains source of truth for provenance semantics.