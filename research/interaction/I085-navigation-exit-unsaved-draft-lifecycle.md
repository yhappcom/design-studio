# I085 — Navigation Exit, Unsaved Draft, and Lifecycle Authority

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION + CONTRADICTION REVIEW

## QUESTION
When a LogMate PWA user has an uncommitted Customize draft, which layer owns the truth of leaving, warning, restoration, and data-loss risk across in-app navigation, browser navigation, backgrounding, tab/process termination, and bfcache?

## SOURCE
- WCAG 2.2 remains the accessibility baseline; status-message semantics remain distinct from focus-taking dialogs.
- MDN `beforeunload`: dialogs require sticky activation, use browser-specified generic text, are not reliably fired on mobile, and Firefox excludes pages with `beforeunload` listeners from bfcache. MDN recommends registering it only while unsaved changes actually exist.
- MDN `visibilitychange` / `pagehide`: visibility change is a better lifecycle signal for application-state preservation; `pagehide` is bfcache-compatible but still not guaranteed on mobile.
- `unload` is unsuitable as a correctness boundary and can damage bfcache/runtime behavior.

Sources:
- https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event
- https://developer.mozilla.org/en-US/docs/Web/API/Window/pagehide_event
- https://developer.mozilla.org/en-US/docs/Web/API/Window/unload_event
- https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html

## RELATED DOMAIN CHECK
- Type: T066 supplies restoration/recovery strings but T021 drawing remains upstream; no geometry problem may be hidden with kerning.
- Color: C097 separates browser lifecycle from semantic success/error; I085 requires an explicit dirty/at-risk state without implying persistence.
- Layout/Interaction: I084 separates history/route/draft/persistence; I085 extends authority to attempted exit and lifecycle loss.
- Web: W097 owns served history/restoration provenance; I085 requires cross-engine exit/lifecycle evidence rather than browser capability claims.
- Content: CD103 separates restored draft from validated/committed state; I085 requires warning language to derive from dirty-state truth, not from lifecycle events.

## MODEL
Keep these facts independent:

`draft_dirty` ≠ `exit_attempted` ≠ `warning_available` ≠ `warning_shown` ≠ `navigation_committed` ≠ `draft_checkpointed` ≠ `draft_restored` ≠ `configuration_committed` ≠ `persisted/synced`.

A `beforeunload` callback is neither a save transaction nor proof that the user saw a warning. `visibilitychange:hidden` is a lifecycle observation, not proof that the user intended to leave. A bfcache return may preserve live memory without validating application freshness.

## PRACTICE / SCENARIO FAMILIES
Use the same 35-item Customize draft and stable object IDs. Replicate each family twice when runtime exists:
1. clean draft → in-app route leave;
2. dirty draft → in-app route leave → stay/discard where product implements it;
3. dirty draft → browser Back/Forward;
4. dirty draft → reload/tab close attempt with and without prior activation;
5. dirty draft → background/app switch → return;
6. dirty draft → background then process termination (physical-device evidence required; do not simulate as PASS);
7. dirty draft → bfcache return vs new-document return;
8. dirty draft at 200% and with non-drag reorder path once implemented;
9. Undo/Reset returning dirty state to clean, then leave.

Record route/history ID, document lifecycle, visibility/pagehide/pageshow where observable, dirty/checkpoint/validation flags, branch/projection hash, semantic focus, warning mechanism, user decision, and resulting draft/configuration truth.

## CRITIQUE / FAILURE CONDITIONS
FAIL if:
- warning registration is permanent rather than dirty-state scoped;
- absence of `beforeunload` is interpreted as safe save;
- lifecycle event is labeled Save/Sync without a persistence transaction;
- Back is silently converted into Undo;
- browser generic warning text is treated as controllable product copy;
- bfcache restoration is treated as freshness validation;
- mobile process termination is claimed covered by unload-style events;
- warning/focus behavior creates a false WCAG status-message claim.

## REPRODUCIBLE VALIDATION
For served primary and independent engines, capture scenario ID, build/route, browser/version, activation state, lifecycle event trace, history entry, dirty/checkpoint flags, projection hash, focus before/after, warning shown/not shown, and final route/draft state. Repeat each executable family twice. Physical process-kill, AT and representative-human evidence remain OPEN until real devices/users exist.

## UX INTEGRATION
Information architecture must distinguish editing from committed configuration. Leaving should not invent persistence. Recovery must preserve stable object identity and explain only actionable product truth. Warning frequency, user comprehension, interruption cost and pilot workflow suitability require human evidence.

## HANDOFFS TO OTHER SPECIALISTS
- Layout: measure warning/return/focus geometry and 200% behavior.
- Color: encode dirty/at-risk only if meaning survives forced colors and does not masquerade as saved/error.
- Content: define concise visible and accessible dirty-exit/recovery payloads without promising save.
- Web: validate actual lifecycle/activation/bfcache behavior cross-engine.
- Type: stress required EN/KO labels only after T021 drawing gate permits.