# CD103 — Route/history and draft truth

## Goal
Extend the complete content system through navigation restoration without narrating browser mechanics as user outcomes.

## Protected semantic contracts
- `Back/Forward ≠ Undo/Redo`.
- `scroll restored ≠ focus restored`.
- `form value restored by browser ≠ draft validated`.
- `draft restored ≠ configuration committed`.
- `local commit ≠ Saved/Synced`.
- `pageshow persisted ≠ data freshness confirmed`.
- `route returned ≠ previous action succeeded`.

## Content-system practice
For forms/state/onboarding/retrieval/tone/localization, derive visible and accessibility payloads from current semantic object + branch + validation + transaction/recovery truth. Browser history entry, bfcache lifecycle and scroll restoration are diagnostic provenance unless they change action/recovery.

Test EN/KO candidates for: restored unsaved draft, invalidated restored draft, current committed configuration, unavailable source object, recovery/Reset. Keep literal production wording provisional until runtime fit and linguistic review.

## Critique
FAIL if navigation creates a success message, stale draft is described as current without revalidation, ordinal/index is used as object identity, or concise visible feedback contradicts richer a11y status.

## RELATED DOMAIN CHECK
I084 semantic authority; L088 geometry; C097 state visibility; T066 string transfer; W097 runtime lifecycle evidence.

## Evidence boundary
No production multilingual, AT comprehension, persistence/sync or human task PASS is claimed.

## Sources
- https://html.spec.whatwg.org/multipage/browsing-the-web.html
- https://developer.mozilla.org/en-US/docs/Web/API/Window/pageshow_event
