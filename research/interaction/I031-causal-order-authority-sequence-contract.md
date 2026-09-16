# I031 — Causal Order / Authority Sequence Contract

## PURPOSE

Extend I030 so action safety and audit reconstruction survive cases where wall-clock chronology conflicts with authoritative causal order.

## CONTRACT

The system must distinguish `eventTime`, `observedTime`, `receivedTime`, `reconciledTime`, `authorityRevision`, `sequence/orderToken`, and `orderingBasis`. Display time is presentation evidence, never an automatic ordering oracle.

For consequential actions, precedence is: explicit authoritative revision/sequence → validated dependency relation → server/authority ordering contract → timestamp ordering only when the product contract explicitly guarantees comparable clocks. Unknown order remains unknown.

## REQUIRED SCENARIOS

1. client clock +8 min but server revision is older;
2. offline event occurred earlier but uploads after a newer online event;
3. equal formatted timestamps with distinct authoritative sequence;
4. event time absent but revision/order token present;
5. authority revision present but sequence across objects is not comparable;
6. timezone/DST changes display order without changing causal order.

FAIL if UI enables a consequential action because a displayed time merely appears newest.

## RELATED DOMAIN CHECK

Type: T021 temporal strings remain stress corpus, not ordering logic. Color: C044 must not equate recency emphasis with authority. Layout: L035 must keep causal order and time role distinguishable. Web: W044 captures raw provenance and runtime ordering basis. Content: CD050 owns user-facing language for sequence/unknown order.

## HANDOFFS TO OTHER SPECIALISTS

W044 should execute these scenarios with shared object/event IDs and record both display order and authoritative order. Content/Color/Layout should consume the verdict, not derive it independently.

## EVIDENCE BOUNDARY

Deterministic interaction contract only; no production backend ordering guarantee, distributed-system proof, AT, or human comprehension/task evidence.