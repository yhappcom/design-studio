# I015 — W027 Recovery Oracle

Evidence type: SYSTEMS PRACTICE / TRANSFER VALIDATION / OPEN

## RELATED DOMAIN CHECK
W027 supplies transport/runtime events. L020 owns spatial reachability. C029 owns visual focus/state evidence. CD033 owns wording. T023 owns typography. I015 remains authority for state/action/recovery semantics.

## Runtime oracle
Classify each operation using observable authoritative evidence, not the browser exception alone:

- no dispatch: safe to initiate;
- dispatched + authoritative success: confirmed; do not duplicate;
- dispatched + authoritative rejection/non-commit: known failure; retry may be offered if operation policy allows;
- dispatched + transport ended without authoritative commit evidence: outcome unknown; reconcile before unsafe retry;
- reconciliation confirms committed: confirmed;
- reconciliation confirms absent/non-commit: known failure/retry eligible;
- reconciliation unavailable: remain outcome unknown.

Reconnect is transport restoration, not proof of commit or non-commit. Idempotency keys can make retries safer only when the backend contract actually guarantees their semantics; the UI must not infer such a guarantee from a client-generated operation ID.

## W027 assertions
The harness must never convert a fetch exception directly into `known failure`. `Check outcome` is the primary safe action for outcome-unknown. A future backend fixture must expose explicit committed/non-committed reconciliation states before I015 can claim runtime validation.

## Current result
**ORACLE SPECIFIED AGAINST EXECUTABLE HARNESS / BACKEND VALIDATION OPEN.** No backend or idempotency guarantee is fabricated.

## HANDOFFS TO OTHER SPECIALISTS
CD033 maps each oracle state to message IDs; W027 records observed transitions; L020 ensures recovery remains reachable; C029 ensures state is not color-only; UX integration audits whether the workflow preserves user control without claiming human comprehension.