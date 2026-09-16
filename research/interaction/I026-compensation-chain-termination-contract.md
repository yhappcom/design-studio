# I026 — Compensation chain termination contract

Date: 2026-09-16
Evidence class: **SYSTEMS PRACTICE / adversarial workflow contract**

## RELATED DOMAIN CHECK
Type must preserve operation/revision identifiers; Color must not leave stale-success or stale-compensation emphasis; Layout must preserve causal locality; Web owns runtime ordering/provenance; Content owns distinct correction language.

## Problem
I025 makes compensation a first-class operation. A new risk follows: compensation itself can conflict, time out, or trigger another correction. A product can accidentally create an unbounded `operation → compensation → compensation-of-compensation` loop while repeatedly presenting locally plausible recovery UI.

## Contract
Every correction chain has a stable `correctionChainId` and monotonically ordered operation identities. For each new corrective operation record:
- target authoritative revision;
- facts it intends to restore/change;
- predecessor operation;
- whether it is idempotent/replay-safe by documented backend contract;
- terminal success condition;
- escalation condition.

Automatic compensation must stop when any of these occurs: authoritative target changed beyond the correction precondition; the correction outcome is unknown; the maximum product-defined automatic correction budget is reached; a semantic conflict requires user/professional judgment; or backend replay/idempotency safety is undocumented.

At termination the UI must not silently spawn another mutation. It moves to a stable reconciled state or an explicit intervention-required state with durable history.

## Adversarial sequence
`op A optimistic success → conflict → comp B → B response loss → reconcile B not-applied → authority changed again → automatic comp C forbidden → intervention-required → later retrieval preserves A/B history and current authority`.

## Deterministic verdicts
PASS requires no unbounded automatic correction loop, no mutation while predecessor certainty is outcome-unknown, no late predecessor response overwriting newer authority, and a durable terminal/escalated state.

## HANDOFFS TO OTHER SPECIALISTS
L030 should preserve chain identity and intervention locality. CD045 should distinguish correction pending/unknown/terminated/intervention-required. W039 should execute bounded chain ordering. C039 should ensure stale optimistic/correction success cannot dominate the terminal conflict state.

## Evidence boundary
No production backend, human comprehension, workload, trust, AT, or physical-device PASS is claimed.
