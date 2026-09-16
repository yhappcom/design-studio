# CD048 — Snapshot-to-Live Recheck Language System

Evidence purpose: **STAGE 3 PRACTICE / SEMANTIC TRANSFER CONTRACT** paired with I029/L033/W042.

## RELATED DOMAIN CHECK
I029 owns actual recheck outcomes; L033 owns spatial ordering; C042 owns visual cue survival; W042 owns runtime provenance; Type must accept unchanged operational strings only after its current gates.

## Semantic distinction
A static artifact needs language that says what was known when it was generated and a separate live recheck vocabulary. Translation may reorder grammar but cannot strengthen certainty.

Canonical outcome concepts:
- `snapshotGeneratedAt`: artifact creation time, never authority time;
- `snapshotAuthorityConfirmedAt`: last authority confirmation represented by the artifact;
- `recheckCurrentConfirmed`: live authority confirms current state;
- `recheckChangedSinceSnapshot`: live state differs from artifact snapshot;
- `recheckAuthorityUnavailable`: current truth cannot be checked now;
- `recheckObjectUnavailable`: object cannot be retrieved; do not imply deletion unless known;
- `recheckAccessNotAuthorized`: access cannot be granted; do not imply object absence;
- `recheckInProgress`: authority check underway, not success.

## Content ordering
For changed state: identify object → say snapshot is older → state what is current → state consequence → expose only currently safe action → provide history. For unavailable authority: identify object → preserve snapshot timestamp → say current state could not be checked → offer non-mutating recovery/recheck path.

## Localization invariants
Localization must not translate `snapshot` as current/live, `unavailable` as failed/deleted, or `changed` as conflict unless the Interaction contract establishes conflict. Timestamp labels must preserve whether they mean generated, observed, authority-confirmed or reconciled time. Long IDs and timestamps may wrap; semantics may not be deleted for fit.

## Executable vectors
The production localization round trip must cover pseudo-expansion, plural/select where applicable, long object/event IDs, timezone-qualified timestamps, missing resource/fallback, locale change between export and recheck, and snapshot/current wording on the same surface. Record resource revision and generated-build identity.

## OPEN
No Flutter/TMS/ARB production round trip is executed here. Linguistic review and human comprehension/task evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W042 must record resource revision/locale with the runtime artifact. L033 must preserve semantic ordering under reflow. C042 verifies that the meaning survives loss of color. I029 remains authoritative for state/action truth.