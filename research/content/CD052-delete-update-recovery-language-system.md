# CD052 — Delete/Update Recovery Language System

## PURPOSE
Extend CD051 partial-order language to destructive concurrency. The content system must preserve existence, deletion certainty, conflict and recoverability without inventing backend truth.

## SEMANTIC RESOURCE MODEL
Keep distinct resources for: `deleteRequested`, `deletePending`, `deleteOutcomeUnknown`, `deleteUpdateConflict`, `deletedConfirmed`, `restoreAvailable`, `restoreUnavailable`, `restoreRequested`, `restoreOutcomeUnknown`, `restoredConfirmed`, `objectUnavailable`, `retentionUnknown`, `authorityUnavailable`.

`Undo` is permitted only when Interaction/product authority defines true reversal. If recovery is a new mutation, label it as restore/recover according to the product concept. Never promise “You can restore this later” when retention/tombstone evidence is absent.

## MESSAGE CONTENT ORDER
For consequential states communicate: object identity/context → current authoritative existence/consequence → certainty/conflict → safe next action → durable history/recheck path. Do not use generic `Deleted` for pending or outcome-unknown states, and do not call a late update `restored` unless authority confirms restoration.

## LOCALIZATION / ACCESSIBILITY STRESS
Pseudo-expand labels and explanations; preserve object/branch identity; avoid color references; keep deletion/restore verbs input-neutral; distinguish no live records from history unavailable/not loaded; ensure locale changes do not collapse pending, unknown and confirmed. Timestamp/arrival wording must not imply ordering where I033 says branches are incomparable.

## RELATED DOMAIN CHECK
Type T021 remains provisional and must consume unchanged operational strings only after drawing gates. C046 supplies visual-state constraints. I033 owns existence/action truth. L037 owns recovery locality. W046 supplies runtime/fallback/export evidence. Human comprehension and linguistic review remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Interaction must provide authoritative delete/restore semantics before final copy. Web must report missing-resource/fallback and route/history failures. Layout must preserve consequence/recovery wording rather than truncate it to maintain preferred geometry.

## EVIDENCE BOUNDARY
Static semantic system only; no Flutter/TMS/ARB round trip, linguistic review, AT, production-backend integrity or human comprehension/task PASS.