# CD115 — Runtime status and recovery language

Date: 2026-09-20
Status: Stage 3 PRACTICE / H5 COMPLETE-SYSTEM TRANSFER

## Purpose
Extend CD114 across offline, retry, stale, reload/update and persistence ambiguity without inventing certainty the system cannot prove.

## RELATED DOMAIN CHECK
Checked T078, C109, I096/L100 and W109. Interaction remains authority for state/action/recovery; Web supplies runtime evidence. Content names those truths.

## Semantic distinctions
Keep separate: Offline, Working offline, Saving, Save failed, Retry available, Retry in progress, Saved locally, Synced, Stale/refresh needed, Unknown outcome, Restored draft and Undo available/expired. Do not expose distinctions the implementation cannot actually determine.

## Content contract
Every runtime message should answer only the jobs required by context: affected object/scope, current state, consequence if material, available action, and recovery/result. Routine status should not demand acknowledgement merely to be noticed. Unknown outcome must not be rewritten as failure or success.

## Reproducible fixture
Use one flight-record fixture through local edit, persistence failure, retry, offline route return, reconnect, stale refresh, interrupted import commit, reload and recovery. Compare visible status, accessible status payload, action label, object reference, consequence/recovery and whether focus changes.

## Critique
FAIL on 'Saved' for a local draft when persistence is unknown; 'Synced' before acknowledgement; generic 'Something went wrong' where a safe recovery is known; 'Retry' when blind repetition can duplicate a mutation; success copy that survives a later failure; or color-only references.

## Human boundary
Comprehension, trust, interruption cost and representative-pilot preference remain HUMAN evidence. Expert consistency review does not close them.

## HANDOFFS TO OTHER SPECIALISTS
Type must render complete necessary messages under fallback; Layout keeps message/action attributable; Color preserves semantic distinctions; Web verifies programmatic status and actual runtime truth.