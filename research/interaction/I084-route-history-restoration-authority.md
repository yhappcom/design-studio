# I084 — Route/history restoration authority

## Purpose
Stage-3 systems practice after I083. Separate browser session-history restoration from application navigation, semantic focus, draft/configuration state and persistence truth.

## SOURCE
- WHATWG HTML session history defines traversal and persisted user state; history traversal may restore scroll/form state independently of application semantic intent.
- `History.scrollRestoration` exposes `auto` vs `manual`; it is not a focus- or transaction-restoration API.
- `pageshow` exposes whether a document is restored from a persisted page state (`PageTransitionEvent.persisted`).
- Flutter restoration APIs restore registered application state only when restoration is configured; framework capability is not LogMate product evidence.

## PRACTICE contract
Keep these identities independent:
`history entry ≠ route identity ≠ semantic object ≠ focused object ≠ draft/configuration branch ≠ persisted/synced state`.

Protected invariants:
1. Back/forward traversal must not be interpreted as Undo/Redo of a reorder transaction.
2. Browser-restored scroll/form state must not create `Saved`/`Synced` truth.
3. Focus restoration resolves from the active semantic route/object, never from stale ordinal/widget identity.
4. A bfcache/pageshow restoration is document lifecycle evidence, not proof that application state was revalidated.
5. Reload/new-document restoration and same-document history traversal are separate scenario families.

## CRITIQUE / failure taxonomy
FAIL if history traversal resurrects stale reorder preview/candidate, changes branch without explicit product rule, restores focus to an invalid/hidden object, duplicates a committed mutation, or announces persistence from browser-restored state alone.

## Reproducible verification
Use one stable 35-item Customize dataset and stable semantic IDs. For each family run twice: commit→navigate away→Back; uncommitted draft→navigate away→Back; Undo/Reset→Back/Forward; 200% reflow before traversal; route return after source becomes unavailable. Record history entry/route ID, pageshow persisted flag where available, scroll offset, semantic focus ID, branch/projection hash, transaction IDs and visible/a11y result.

## RELATED DOMAIN CHECK / handoff
- Layout L088 owns viewport/focus/overlay geometry.
- Content CD103 owns restoration/draft wording truth.
- Color C097 owns restored/current/stale visual-state separation.
- Type T066 supplies strings only; T021 drawing gate remains upstream.
- Web W097 owns served browser-history provenance and independent-engine transfer.

## Evidence boundary
This is SOURCE→PRACTICE/CRITIQUE specification. No LogMate route/history runtime, bfcache parity, persistence, AT or human PASS is claimed.

## Sources
- https://html.spec.whatwg.org/multipage/browsing-the-web.html
- https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration
- https://developer.mozilla.org/en-US/docs/Web/API/Window/pageshow_event
- https://api.flutter.dev/flutter/widgets/RestorationManager-class.html
