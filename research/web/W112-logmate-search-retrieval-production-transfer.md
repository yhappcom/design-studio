# W112 — LogMate Search/Retrieval Production Transfer Manifest

Date: 2026-09-20  
Purpose: Stage 3 closure-oriented SEARCH-001 transfer; do not accumulate another isolated Chromium micro-test.

## RELATED DOMAIN CHECK
I099/L103/T081/C112/CD118 checked. W112 observes runtime truth and does not redefine specialist semantics.

## SOURCE
WAI APG documents combobox/listbox interaction semantics when those patterns are used. WCAG 2.2 SC 4.1.3 covers programmatically determinable status messages such as search progress/count/no-results without requiring focus movement; SC 2.4.3 preserves meaningful focus order.

Sources:
- https://www.w3.org/WAI/ARIA/apg/patterns/combobox/
- https://www.w3.org/WAI/ARIA/apg/patterns/listbox/
- https://www.w3.org/WAI/WCAG22/Understanding/status-messages
- https://www.w3.org/WAI/WCAG22/Understanding/focus-order

## Production manifest
For each search transition capture:
- production build/commit, service-worker/app-shell/data version where relevant;
- engine/version and browser/standalone mode;
- canonical query, normalized/submitted query and filter/sort state;
- request ID/version, start/cancel/supersede/response timing and network state;
- result-set ID/order and stable record IDs;
- active/highlighted versus selected/opened result;
- visible + accessibility query/status/result payload;
- focus, scroll and L103 geometry/occlusion;
- actual loaded font/fallback and T081 wrap/truncation;
- C112 semantic state IDs;
- route/history transition and restored/re-run search state under I098/W111;
- error/offline/retry evidence and recovery outcome.

## Scenario family
1. query → results → record → Back/restore;
2. rapid query A→B with A response arriving late: stale A must not replace B;
3. zero results versus network/server error versus offline;
4. clear/refine/filter/sort while preserving record/result identity;
5. record edit/cancel/commit then return;
6. reload/deep entry under actual addressability policy;
7. baseline/narrow/enlarged/text-spacing and actual font fallback;
8. light/night/forced-colors/reduced-motion where applicable.

Run served primary engine twice (`REPLICATION`) then independent engine (`TRANSFER VALIDATION`). Physical iPad/mobile/PWA standalone remains required where keyboard, safe area, browser chrome or install mode materially changes search behavior.

## Failure conditions
Older response overwrites newer query; loading/count/no-results mismatches current request; Back restores wrong query/filter/result; duplicate/untraceable record identity; focus stolen by routine status; custom combobox/listbox semantics diverge from implemented keyboard behavior; visible/a11y payload disagreement; retry obscures unresolved outcome.

## Performance evidence boundary
Synthetic query/interaction timings, Lighthouse, DevTools and CI are **LAB**. LCP/INP/CLS are **FIELD** only when provenance-bearing representative RUM/aggregate data exists. Search latency observed in a production-like run is runtime evidence but not automatically representative field performance.

## STUDIO JUDGMENT
W112 is a closure manifest, not closure evidence. SEARCH-001 remains OPEN until actual LogMate runtime executes it.

## HANDOFFS
Return actual font/wrap to Type, state collisions to Color, focus/geometry/authority failures to Layout/Interaction, and visible/a11y wording mismatches to Content.