# CD044 — Rollback, compensation and recovery language system

Date: 2026-09-16
Evidence purpose: **SYSTEMS PRACTICE / CONTENT CLOSURE EXTENSION**

## RELATED DOMAIN CHECK
I025 defines whether the system can undo, rolls back, or creates compensation; L029 owns spatial association; C038 owns visual truth; W038 owns runtime provenance; Type T021 must render these strings without semantic shortening.

## Semantic distinction
Content must not use “Undo”, “Retry”, “Reverted”, “Restored” or “Fixed” interchangeably.
- `undoAvailable`: user can intentionally reverse a confirmed operation.
- `rollbackInProgress`: system is restoring prior authoritative state.
- `compensationRequired`: effects cannot be treated as literal rollback; another operation is required.
- `compensationPending`: compensating operation dispatched, outcome not yet authoritative.
- `compensationOutcomeUnknown`: response lost/ambiguous; check outcome, do not assert failure.
- `restoredConfirmed`: authoritative state confirms restoration.
- `alternateConfirmed`: compensation produced a different but authoritative final state.

## Resource contract
Each message carries object identity, original operation reference where needed, compensation operation reference when present, certainty, consequence, safe action, and history/detail path. Revision/time variables must say what they timestamp; a presentation time cannot masquerade as authoritative confirmation time.

## Prohibited transformations
Localization/tone may not: turn outcome-unknown into failed; turn compensation into literal undo; erase operation identity when concurrent outcomes need disambiguation; imply current authority from cached/presented success; call a blocked retry safe; hide a changed consequence behind generic reassurance.

## Stress set
Pseudo-expansion; long object identifiers; two concurrent original operations; compensation response loss; plural affected records; date/time/duration; missing-resource fallback; later retrieval after the transient correction banner is gone.

## UX closure boundary
Static resources can be reviewed for semantic fidelity but cannot prove comprehension. Actual ARB/ICU/TMS or equivalent production round trip, runtime binding, linguistic review and human task comprehension remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W038 binds semantic IDs to executed run IDs; I025 owns allowed actions; L029 ensures local consequence/recovery association; C038 prevents stale success visual truth; Type must preserve the full operational wording.