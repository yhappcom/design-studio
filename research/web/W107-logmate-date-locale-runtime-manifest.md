# W107 — LogMate Date Locale / Width Runtime Manifest

Status: **STAGE 3 PRACTICE / PRODUCT TRANSFER — no gate promotion**

## PURPOSE
Turn H3 into observable production-browser evidence rather than a static width assumption.

## RELATED DOMAIN CHECK
T076, C107, I094/L098 and CD113 checked. W106 production-evidence ladder is reused.

## SOURCE
HTML `input[type=date]` exposes a normalized `yyyy-mm-dd` value while visible presentation can follow browser locale/OS UI. `Intl.DateTimeFormat` provides language-sensitive application formatting. Native control appearance can vary by browser/platform.

## RUNTIME MATRIX
For each actual LogMate date surface capture:
- canonical date value/record ID;
- control type and authored-vs-native presentation;
- requested and resolved locale when application formatting is used;
- visible string where script-accessible, plus screenshot geometry;
- actual loaded font/fallback/features;
- date-zone and adjacent operational geometry;
- focus/validation/selection state and accessibility payload;
- baseline, enlarged text, WCAG text-spacing override;
- served primary engine then independent engine; physical iPad/mobile where native UI matters.

Run executable families twice for REPLICATION. Browser-native picker chrome that is not script-observable is documented as platform evidence, not invented DOM evidence.

## FAILURE CONDITIONS
Canonical value changes merely because presentation changes; stale formatted display after edit/route return; authored format silently depends on runtime default locale where product policy requires determinism; date width obscures required adjacent content/action; native and authored states claim different validation/commit truth.

## PERFORMANCE BOUNDARY
Lighthouse/DevTools/CI remain LAB. No LCP/INP/CLS FIELD claim without provenance-bearing representative RUM/aggregate.

## OPEN
Actual production implementation and route/network/font state; independent-engine and physical-device execution; screen reader/human evidence.

## HANDOFFS TO OTHER SPECIALISTS
- Type/Layout: return measured widths and fallback-driven geometry changes.
- Interaction/Content: return any mismatch between canonical date, visible representation and validation/commit semantics.
- Color: return native/forced-colors state limitations.