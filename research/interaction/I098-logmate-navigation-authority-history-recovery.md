# I098 — LogMate Navigation Authority, History, and Recovery

Date: 2026-09-20  
Purpose: `TRANSFER VALIDATION` / project-specific Stage 3 systems practice.  
Scope: close the analytical part of the long-open NAV-001 blocker without pretending that a runtime implementation or human validation exists.

## RELATED DOMAIN CHECK

- Type: T079 and the open T021 drawing gate; navigation labels must use mature fallback and must not be shortened to rescue geometry.
- Color: C110; current destination, focus, pending/error and selection are distinct semantic axes.
- Layout/Interaction: I095 cross-surface transfer, I096 runtime authority, I097 reorder equivalence; reuse their identity/state/recovery separation.
- Web: W108–W110; route/history/runtime provenance and independent-engine transfer remain required.
- Content: CD114–CD116; canonical terminology and actual state/action/consequence must survive surface changes.
- UX: cross-cutting only; no new ownership structure is created.

## SOURCE

1. W3C WCAG 2.2 remains the accessibility baseline. Repeated navigation mechanisms must preserve relative order unless the user initiates a change (SC 3.2.3).
2. WAI navigation guidance uses a navigation landmark and `aria-current="page"` to expose the current destination; current-state semantics are not merely decorative highlighting.
3. MDN History API: `pushState()` adds a session-history entry; Back/Forward activate history entries and dispatch `popstate`; initial SPA state may require explicit state reconstruction. History traversal is asynchronous.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation.html
- https://www.w3.org/WAI/tutorials/menus/structure/
- https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/
- https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API
- https://developer.mozilla.org/en-US/docs/Web/API/Window/popstate_event

## SYNTHESIS — navigation authority chain

`canonical destination ≠ visible nav item ≠ current-destination indicator ≠ focused control ≠ history entry ≠ restored route state ≠ task draft state`.

A bottom dock, side rail, in-content link, browser Back, deep link and notification entry may all reach the same canonical destination. None of those entry mechanisms owns the destination's product truth.

## PRACTICE — LogMate route family

Use a stable fixture containing at least:
- Home summary;
- View Logbook / ledger;
- Add Flight;
- Activity or equivalent history surface;
- Settings/Customize where implemented;
- record detail/edit as a nested destination.

For each route record: canonical route ID, URL/route representation where applicable, visible label, current-state semantic, entry source, focus restoration target, scroll restoration policy, dirty-draft policy, and Back/Forward expectation.

## CRITIQUE / failure conditions

FAIL if any of the following occurs:
- current destination is inferred from color alone;
- focused nav item is treated as current destination when it is not;
- repeated primary navigation changes order merely because a surface changes;
- Back exits a task when the product contract requires returning to an internal prior state, or traps the user by manufacturing redundant history entries;
- reload/deep link cannot reconstruct a canonical destination that is represented in the URL/router contract;
- route return silently discards a dirty draft or presents a stale success state;
- a Home-specific Bottom Dock is promoted to app-wide truth without cross-surface evidence;
- responsive recomposition changes destination wording/identity rather than only presentation.

## Reproducible validation contract

Execute, when implementation exists:
1. cold-load each addressable destination;
2. navigate Home → ledger → record → edit → cancel and repeat with commit;
3. use browser Back/Forward after each transition;
4. reload at Home, ledger, record detail and dirty-draft boundaries;
5. enter a nested route directly where supported;
6. repeat at narrow/reflow/enlarged/text-spacing states;
7. repeat primary engine twice, then independent engine;
8. capture route/history state, current-destination semantics, focus, scroll, visible+a11y payload, dirty/persisted state and actual loaded font.

## UX integration

Information architecture: destinations are defined by user task/object scope, not by available screen real estate.  
Discoverability: persistent primary navigation can improve orientation but this is not a human discoverability PASS.  
Cognitive load: avoid simultaneous competing current-location signals; human workload remains OPEN.  
Accessibility: current destination, focus and selected content remain separate states; WCAG 2.2 is the baseline.  
Professional workflow: route transitions must preserve record identity, draft/persistence truth and recovery.

## STUDIO JUDGMENT

NAV-001 is now analytically specified enough for implementation. It is **not closed**. Closure requires actual LogMate routes and history behavior, cross-engine evidence, responsive/accessibility transfer, and physical-device evidence where browser/PWA behavior matters.

## HANDOFFS TO OTHER SPECIALISTS

- Type: validate real nav labels and current-state strings without provisional T021 metrics.
- Color: encode current destination without merging focus/selection/error.
- Layout: preserve primary order and route orientation across recomposition.
- Web: own runtime history/deep-link/reload evidence.
- Content: keep destination naming stable while allowing surface-specific concise realization.

## OPEN

Actual app-wide primary destination set; Bottom Dock adoption beyond Home; deep-link policy; dirty-draft route interception; screen-reader behavior; physical iPad/iPhone/Android/PWA behavior; representative-pilot wayfinding and workload.