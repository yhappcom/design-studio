# I019 — Interruption / Resumption Cognitive-State Contract

Date: 2026-09-16
Evidence: **SYSTEMS PRACTICE / UX INTEGRATION / HUMAN EVIDENCE OPEN**

## RELATED DOMAIN CHECK
- **Type:** identifiers/times must remain discriminable after resumption; T021 is not production-ready.
- **Color:** C032 audits whether resumed state remains identifiable without hue.
- **Layout:** L022 owns where resumption context and recovery controls remain reachable under reflow.
- **Web:** W031/W032 owns route/history/session runtime transfer.
- **Content:** CD037 owns wording and durable semantic IDs; it must not invent certainty after interruption.

## Why this follows I018
I018 defines the complete professional-record workflow. The next UX risk is not another state label; it is **loss of task context across interruption**. Professional workflows are vulnerable when a user returns and cannot tell what object, operation, certainty or recovery step was active.

## Minimum resumption state
After route traversal, reload, temporary disconnect or later return, the product should be able to reconstruct or explicitly declare unavailable:
- object/record identity;
- last authoritative persisted state;
- local draft/pending mutation identity where applicable;
- certainty level: known / pending / outcome-unknown / reconciled;
- last safe action and whether it remains valid;
- conflict presence;
- time/source of last authoritative observation where material.

## Invariants
1. **No phantom continuity:** UI must not visually imply a pending operation is still live when the runtime has lost its identity.
2. **No certainty inflation:** interruption cannot turn outcome-unknown into failure or success without authoritative evidence.
3. **No hidden object switch:** resumption must not silently apply recovery to a different record after navigation/filter changes.
4. **Durable recovery:** if recovery requires reconciliation, the operation ID or equivalent correlation key must survive the relevant interruption boundary.
5. **History coherence:** later retrieval must agree with the reconciled authoritative outcome or surface a conflict.
6. **Safe abandonment:** users must be able to leave a non-destructive ambiguous state without accidentally dispatching a duplicate consequential action.

## Non-human UX checks
A deterministic fixture can verify object IDs, operation IDs, state transitions, route/history restoration, enabled actions and persistence. It can expose contradictions in cognitive state representation.

It cannot establish remembered context, perceived workload, confidence, discoverability, interruption cost or pilot task performance. Those remain HUMAN EVIDENCE OPEN.

## Failure ledger
Record: interruption boundary → persisted identifiers → restored semantic state → enabled actions → content ID → route/location → authoritative check → discrepancy. A missing correlation key is a product-contract defect, not a writing problem.

## HANDOFFS TO OTHER SPECIALISTS
- **Web:** create runtime cases for back/forward, reload and response loss using shared operation IDs.
- **Content:** provide resumption/reconciliation strings without certainty inflation.
- **Color/Layout:** preserve state identity and recovery reachability under alternate modes/reflow.
