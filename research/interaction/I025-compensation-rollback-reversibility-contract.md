# I025 — Compensation, rollback and reversibility contract

Date: 2026-09-16
Evidence purpose: **SYSTEMS PRACTICE / ADVERSARIAL VALIDATION**

## RELATED DOMAIN CHECK
T021 constrains rendering only; C038 owns visual truth; L029 owns spatial continuity; W038 owns runtime/network provenance; CD044 owns semantic explanation. I025 owns actual compensation/reversal behavior.

## Core distinction
Undo, rollback, retry and compensating action are not synonyms.
- **Undo:** user-requested reversal supported by product semantics.
- **Rollback:** system restores a prior authoritative state because a presented/attempted mutation cannot stand.
- **Retry:** a new attempt; unsafe while outcome is unknown unless idempotency/deduplication proves safety.
- **Compensation:** a new authoritative operation that counteracts effects when literal rollback is impossible or inappropriate.

## Deterministic oracle
For each operation preserve `objectId`, `operationId`, `baseRevision`, `presentedRevision`, `authoritativeRevision`, `outcomeCertainty`, `reversalCapability`, `compensationOperationId`, and `stableRetrievalRevision`.

Adversarial sequence:
`rev1 → A dispatch → optimistic presentation → rev2/conflict → late A result → reconciliation → rollback or compensation decision → compensation pending → response loss if injected → reconciliation → stable later retrieval`.

## Safety invariants
1. Optimistic presentation never proves commit.
2. A late success cannot overwrite newer authority without reconciliation.
3. A compensation operation gets its own operation identity and certainty; it cannot borrow certainty from the original operation.
4. Failed compensation and outcome-unknown compensation are distinct.
5. Retry of compensation remains blocked until its own outcome is reconciled or backend contract proves safe repetition.
6. Later retrieval must explain the final authoritative state without requiring the original transient UI to remain available.

## UX integration
Non-human UX review can verify state/action consistency, reversible-path availability, provenance, and recovery reachability. It cannot prove that users understand rollback versus compensation, trust the system, or recover efficiently; those remain HUMAN EVIDENCE OPEN.

## HANDOFFS TO OTHER SPECIALISTS
L029 keeps original action, reversal consequence and recovery local; C038 prevents stale success styling; CD044 names distinctions; W038 executes race/network variants; Type must render identifiers/state strings without changing semantics.