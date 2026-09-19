# W111 — LogMate Navigation/History Production Transfer Manifest

Date: 2026-09-20  
Purpose: Web Stage 3 closure-oriented transfer for NAV-001; avoid another isolated Chromium micro-test.

## RELATED DOMAIN CHECK
T080, C111, I098/L102, CD117, W108–W110 checked. W111 integrates their contracts in actual browser/runtime evidence and does not redefine their canonical claims.

## SOURCE
MDN documents session-history traversal through `back/forward/go`, `pushState`/`replaceState`, and `popstate`; `pushState()` itself does not emit `popstate`. Browser history traversal is asynchronous. WAI guidance exposes current-page semantics with `aria-current="page"` and navigation landmarks.

Sources:
- https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API
- https://developer.mozilla.org/en-US/docs/Web/API/Window/popstate_event
- https://developer.mozilla.org/en-US/docs/Web/API/History/pushState
- https://www.w3.org/WAI/tutorials/menus/structure/

## Production manifest
For each route transition capture:
- production build/commit and service-worker/app-shell version where applicable;
- engine/version and display mode (browser/standalone where applicable);
- canonical route/destination ID and visible URL/router representation;
- entry mechanism: nav, in-content link, direct/deep link, Back, Forward, reload;
- history state before/after and transition class (push/replace/traverse/reload);
- current-page semantic and navigation landmark payload;
- focus target, scroll restoration and L102 target/occlusion geometry;
- actual loaded font/fallback and T080 wrap/truncation;
- C111 semantic state IDs/rendering;
- CD117 visible + accessibility strings;
- dirty draft, committed/persisted state and recovery result where relevant.

## Scenario family
1. cold Home → Logbook → record detail → edit → cancel → Back/Forward;
2. repeat with commit and route return;
3. direct entry to addressable nested destination then Back;
4. reload each addressable route;
5. dirty draft + attempted navigation under the actual product contract;
6. offline/degraded route entry and reconnect when PWA/runtime supports it;
7. narrow/reflow/enlarged/text-spacing and actual font fallback;
8. light/night/forced-colors/reduced-motion where applicable.

Run served primary engine twice (`REPLICATION`), then independent engine (`TRANSFER VALIDATION`). Physical iPad/mobile/PWA standalone remains required where browser chrome, safe area or install mode materially changes behavior.

## Failure conditions
Stale current-page state; duplicate history entries producing trap-like Back behavior; URL/content disagreement; unreconstructable reload/deep link; focus/scroll loss that obscures task context; silent dirty-draft loss; responsive navigation identity/order drift; mismatch between visible and accessibility current state.

## Performance evidence boundary
Navigation timing or synthetic interaction traces from Lighthouse/DevTools/CI are **LAB**. LCP/INP/CLS become **FIELD** evidence only with provenance-bearing representative RUM/aggregate data. W111 does not upgrade lab evidence by naming it production transfer.

## STUDIO JUDGMENT
W111 is a closure manifest, not closure evidence. NAV-001 remains OPEN until actual LogMate runtime exists and the manifest is executed.

## HANDOFFS TO OTHER SPECIALISTS
Return actual font/wrap to Type, rendered state collisions to Color, geometry/history/focus failures to Layout/Interaction, and visible/a11y wording discrepancies to Content.

## OPEN
Actual route implementation, independent engine, physical device/PWA standalone, screen reader, representative-human wayfinding, field Core Web Vitals.