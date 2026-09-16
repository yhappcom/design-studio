# CD046 — Durable Audit History Language System

Evidence purpose: **SYSTEMS PRACTICE + LOCALIZATION CONTRACT**.

## RELATED DOMAIN CHECK
I027 owns durable event truth; L031 owns current/history hierarchy; C040 owns visual encoding; W040 owns runtime reconstruction; Type remains provisional and cannot justify shortening required identifiers.

## Problem
Transient recovery copy can be truthful yet later history can become misleading if it rewrites uncertainty after the fact or collapses multiple operations into one generic status.

## Semantic contract
Durable event resources preserve event-time truth and operation identity. Required distinctions include: operation requested, outcome unknown, authoritative reconciliation confirmed, authoritative reconciliation not-applied, conflict detected, compensation requested, automation stopped because authority changed, automation stopped because replay safety is unknown, intervention required, and later manual resolution when product truth supports it.

A later confirmed outcome may be linked as a reconciliation event; it must not retroactively rename the earlier observation. `No history`, `history unavailable`, and `history not yet loaded` remain distinct.

Timestamp labels must identify semantics where ambiguity matters (for example requested, observed, reconciled), rather than presenting an unlabeled time that implies commit time. Unknown actor/source is not guessed.

## Localization stress
Pseudo-expansion and locale realization must preserve correction-chain/operation/event identity, uncertainty strength, chronology semantics and safe-action consequence. Long identifiers may wrap or disclose progressively but cannot be silently truncated when the full value is needed for professional verification. Static resource design is not localization round-trip evidence.

## Gate
CD046 extends the complete content system into durable audit/retrieval. Actual Flutter/TMS/ARB execution, linguistic review and human comprehension remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W040 binds semantic resource revision + locale to event IDs; L031 validates expansion; C040 verifies non-color survival; I027 verifies that language never rewrites product history; Type receives unchanged stress strings after T021 drawing repair.