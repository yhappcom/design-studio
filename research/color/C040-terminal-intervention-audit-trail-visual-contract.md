# C040 — Terminal Intervention + Audit-Trail Visual Contract

Evidence purpose: **SYSTEMS PRACTICE + TRANSFER VALIDATION specification**.

## RELATED DOMAIN CHECK
Type T021 remains non-production; Content CD045 owns terminal language; I026 owns correction-chain termination; L030 owns escalation locality; W039 owns runtime provenance. Color only governs visual encoding and must not redefine terminal truth.

## Problem
C039 establishes that intervention-required outranks stale success. The next product risk is temporal: after the terminal banner disappears, history/audit views can visually flatten attempted, confirmed, not-applied and stopped corrections into equivalent rows. That destroys provenance even when text remains technically present.

## Contract
For each correction-chain history row, preserve independent visual roles for: (1) authoritative terminal state, (2) operation identity, (3) chronology, (4) current-vs-historical emphasis, and (5) focus/selection. Brand emphasis and selection must never masquerade as confirmation.

Adversarial tests must remove authored hue, remove icon/shape, enable forced-colors, move keyboard focus across rows, select a historical row, retain stale success styling, and overlay a sticky control. A terminal intervention row must remain distinguishable through non-color semantics and structure.

Contrast, distinguishability, focus visibility and focus obscuration remain separate verdicts. `forced-color-adjust:none` is not a default escape hatch.

## Gate
C040 is ready for execution against the next shared Web runtime IDs. No Stage 3 PASS, forced-colors PASS, observer PASS or human salience claim is made.

## HANDOFFS TO OTHER SPECIALISTS
L031 should preserve chronology/current-state locality; Interaction should define audit event truth; Content should supply durable event labels; Web should capture computed styles/focus/geometry for the same event IDs.