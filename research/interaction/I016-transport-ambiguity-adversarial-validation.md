# I016 — Transport ambiguity adversarial validation

Date: 2026-09-16
Evidence class: **INDEPENDENT VALIDATION / TRANSFER VALIDATION**

## RELATED DOMAIN CHECK
Type is unrelated to behavior truth except later geometry transfer. Color C029 and Layout L020 consume visible states after classification. Web W027/W028 supplies the executable request boundary. Content CD034 must verbalize the classified truth without converting transport symptoms into unsupported outcome claims.

## Result
W028 executed an adversarial pair with the same client symptom but different authoritative outcomes:

- `drop-before`: connection ended without a response; reconciliation by operation ID returned `not-found`.
- `drop-after`: connection ended without a response after the fixture recorded the commit; reconciliation returned `confirmed`.

The immediate transport layer therefore cannot distinguish these cases. **Outcome unknown** is the correct pre-reconciliation state for both in this fixture. After reconciliation, they diverge.

## Recovery invariant
1. A transport exception is evidence about response delivery, not by itself about commit truth.
2. If commit may have occurred, an unconditional retry is unsafe unless the operation contract is idempotent/deduplicated.
3. Reconcile by stable operation identity before offering a destructive or duplicate-producing retry.
4. A known HTTP rejection with authoritative semantics is materially different from an interrupted response.

## UX integration consequence
The end-to-end contract is now: `transport symptom → certainty classification → authoritative reconciliation → semantic state → permitted recovery action → wording/visual state`. Web must not let generic network error handling bypass Interaction certainty.

## Evidence boundary
This is a controlled local backend fixture, not production backend proof. Idempotency, distributed commit, timeout proxies, service workers, app lifecycle, offline queues and concurrent writes remain OPEN. No human UX evidence is claimed.

## HANDOFFS TO OTHER SPECIALISTS
- Content: preserve outcome-unknown language before reconciliation; do not say “failed” for both drop cases.
- Web: automate the same pair in browser Fetch and retain operation IDs in W026 captures.
- Layout/Color: treat reconciliation as a distinct state transition when auditing focus/action visibility and semantic reinforcement.
