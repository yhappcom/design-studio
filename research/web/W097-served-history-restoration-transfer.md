# W097 — Served history/restoration transfer

## Goal
Close a browser/product-transfer gap rather than add an isolated Chromium micro-test.

## Promotion ladder
Actual LogMate implementation → production Web build → served primary engine → independent engine → 200% → forced-colors. Same scenario IDs and stable 35-item data across engines; replicate each family twice.

## Manifest
Record build/commit, route/history-entry identity, navigation type where observable, `pageshow.persisted`, `history.scrollRestoration`, viewport and scrollOffset(t), semantic focus/object IDs, branch/projection hash, transaction/inverse IDs, draft/validation state, visible+a11y status, and L088 focus/sticky/recovery geometry.

## Scenario families
1. committed reorder → leave route → Back/Forward;
2. uncommitted draft → leave → Back;
3. Undo/Reset → history traversal;
4. 200% reflow before/after traversal;
5. semantic source becomes unavailable while away;
6. restored document vs fresh/reloaded document where observable;
7. non-drag reorder equivalent once implemented.

## Critique
FAIL if history traversal duplicates/undoes a mutation without product rule, stale preview/branch survives, restored browser state is labeled persisted/synced, or focus/geometry points to an invalid semantic object. Engine disagreement remains OPEN until reproduced and attributed.

## Performance evidence
Lighthouse, DevTools and CI synthetic remain LAB. Only provenance-bearing RUM/aggregate can support FIELD LCP/INP/CLS claims; history/bfcache behavior must not be inferred from lab Core Web Vitals.

## RELATED DOMAIN CHECK
I084 authority; L088 geometry; C097 visual states; CD103 semantic copy; T066 rendering corpus.

## Evidence boundary
No production served history/bfcache parity, independent-engine, field Core Web Vitals, AT, physical-device or human UX PASS is claimed.

## Sources
- https://html.spec.whatwg.org/multipage/browsing-the-web.html
- https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration
- https://developer.mozilla.org/en-US/docs/Web/API/Window/pageshow_event
- https://api.flutter.dev/flutter/widgets/RestorationManager-class.html
