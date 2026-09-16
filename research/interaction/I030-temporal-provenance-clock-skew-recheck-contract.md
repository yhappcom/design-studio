# I030 — Temporal Provenance, Clock Skew and Recheck Contract

Status: **STAGE 3 PRACTICE / SYSTEMS EXTENSION**

## RELATED DOMAIN CHECK
Type T021 must eventually render dense timestamp/ID strings without ambiguity. C043 reinforces but does not define temporal truth. L034 owns spatial chronology. W043 will own browser/runtime provenance. CD049 owns user-facing time semantics. UX human comprehension remains OPEN.

Purpose: **CONTRADICTION REVIEW + TRANSFER VALIDATION** of I027–I029. A snapshot/recheck workflow can be semantically correct yet still mislead if it sorts or labels evidence by an inappropriate clock.

## Core distinction
Do not collapse these into one `timestamp`:

- domain event time;
- client-observed time;
- server/authority-observed time;
- reconciliation time;
- snapshot generation time;
- live recheck completion time.

Wall-clock order is not automatically causal order. Client clocks may be skewed; offline events may upload later; two systems may have different clock sources.

## Interaction contract

1. Action safety is derived from authoritative revision/evidence dependencies, not from whichever displayed timestamp is newest.
2. A live recheck is non-mutating unless the product separately exposes a mutation.
3. If clock provenance is insufficient, the UI may state that freshness cannot be established; it must not infer currentness from local device time.
4. History preserves recorded event identity and provenance even if later reconciliation supplies a better authority time.
5. Sorting must declare its basis when event time and observed/reconciled time can diverge materially.
6. Relative labels such as “just now” never replace the durable absolute/provenance value required for audit reconstruction.

## Deterministic scenarios

A. client clock +8 minutes, authority revision unchanged;  
B. offline event created earlier but uploaded after a newer server event;  
C. snapshot generated after authority confirmation but before authority revision changes;  
D. live recheck completes after timeout/retry and confirms unchanged revision;  
E. authority supplies revision but no trustworthy event time;  
F. locale or timezone changes between export and later recheck.

For each scenario record: object ID, event/operation ID, revision, clock source, raw instant if known, displayed locale/zone, ordering basis, certainty, available action and recovery.

## Failures

- enabling a consequential action because a client-local timestamp appears recent;
- rewriting historical event time with reconciliation time;
- sorting by display-formatted strings;
- hiding clock-source uncertainty behind a relative-time label;
- treating timezone change as data change;
- treating a later snapshot-generation time as later authoritative state.

## Evidence boundary
This is deterministic interaction analysis. It does not establish production clock synchronization, backend event ordering, user comprehension, workload or trust.

## HANDOFFS TO OTHER SPECIALISTS
L034 must preserve chronology basis and current consequence. CD049 must label time roles. W043 must capture raw instant/revision/zone/clock source separately. C043 must not make recency a semantic priority. Type must stress dense timestamps after drawing repair.
