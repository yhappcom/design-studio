# I034 Retention Expiry / Recoverability Authority Contract

Evidence mode: SYSTEMS PRACTICE / TRANSFER VALIDATION.

## Purpose
Extend I033 from deletion/restore truth to bounded recoverability. The interface must not derive recovery availability from a client countdown, cached policy, wall clock or mere presence of a Restore control.

## RELATED DOMAIN CHECK
C047 consumes the recoverability verdict visually. L038 owns spatial continuity across expiry. W047 will own browser/runtime evidence. CD053 owns language. T021 remains provisional and cannot alter state truth.

## Authority model
Track objectId, deletionEventId, authorityRevision, retentionPolicyRevision, recoverableUntil when authoritative, clockSource, lastAuthorityCheck, recoveryCapability and certainty.

Recovery capability is one of recoverable-confirmed, unavailable-confirmed, outcome-unknown, policy-unknown or authority-unavailable. A local timer may reduce confidence and force a recheck; it cannot promote a state to unavailable-confirmed.

## Deterministic scenario
r1 live → delete confirmed under policy p1 → recoverable confirmed until boundary E → client sleeps/offline across E → user returns → local clock says E passed → consequential Restore remains blocked pending authority recheck → authority reports either recoverable, unavailable, or unavailable-to-check → UI exposes only actions valid for that verdict → reload/history preserves the evidence chain.

Variants: clock skew; policy p1→p2; authority response loss; restore requested just before E but response arrives after E; duplicate restore; object independently recreated with a new identity.

## Safety rules
Do not equate countdown zero, disabled control, cached policy, wall-clock order or object absence with confirmed irreversibility. Do not label a new recreation as Restore unless product authority defines identity continuity.

## Evidence boundary
This is deterministic analysis, not production backend evidence or human comprehension/task evidence.

## HANDOFFS TO OTHER SPECIALISTS
C047 must visualize certainty rather than elapsed local time. L038 keeps evidence and safe action local. W047 records authority/policy revisions and boundary timing. CD053 names uncertainty without promising recovery.