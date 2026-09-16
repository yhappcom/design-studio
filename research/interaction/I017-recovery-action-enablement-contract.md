# I017 — Recovery action enablement contract

Evidence type: **SYSTEMS PRACTICE / CRITIQUE**

## RELATED DOMAIN CHECK
I016/W028 establish certainty semantics. CD035 names them. W029 is the runtime transfer. Layout owns action reachability; Content does not decide whether retry is safe.

## Action-enablement matrix
| certainty/state | authoritative commit evidence | primary safe action | retry enabled? |
| --- | --- | --- | --- |
| pending | none yet; request active | wait/cancel only if contract supports cancellation | no |
| outcome unknown | absent | check/reconcile | no by default |
| reconciled confirmed | committed | continue/view record | no duplicate submit |
| known rejection | authoritative non-success/no commit for fixture | correct input or retry if contract permits | conditional |
| reconciled not-found | authoritative fixture has no recorded commit | retry only if product idempotency/dedup contract permits | conditional |
| conflict | competing authoritative versions | compare versions | no destructive overwrite by default |
| offline/stale | authoritative refresh unavailable | view local / reconnect then reconcile | no unsafe submit by default |

## Key critique
W028 proves that identical transport loss cannot determine retry safety. I017 therefore separates **certainty** from **action enablement**. Even a reconciled `not-found` fixture does not establish a production retry rule unless the real backend defines operation identity, idempotency/deduplication and retention semantics.

## Runtime acceptance
W029 may validate that the rendered primary action matches this matrix for the controlled fixture. It cannot promote fixture behavior into a production backend guarantee.

## UX integration
This reduces duplicate-action risk and cognitive branching: the interface should present the next safe action appropriate to certainty rather than expose every technically possible command. Whether users understand or trust that action requires later human evidence.

## HANDOFFS
Content labels the enabled action without overstating certainty; Layout keeps it reachable; Web binds it to actual state; product engineering must provide idempotency/deduplication guarantees before production retry policy closes.