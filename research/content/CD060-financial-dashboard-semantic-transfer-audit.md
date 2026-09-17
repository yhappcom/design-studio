# CD060 — Financial-dashboard semantic transfer audit

Evidence purpose: **TRANSFER VALIDATION**

## RELATED DOMAIN CHECK
T022 financial-string corpus; C054 outcome-vs-income semantics; L045/I041 hierarchy/review gate; W054 reproducible artifact package.

## Transfer finding
Financial dashboards require wording that separates portfolio value, invested capital, total performance, cumulative distributions, payback/recovery, ROC and tax adjustment. High distributions and positive recovery do not semantically imply positive total performance. Gross, net, estimated and final are not interchangeable qualifiers.

## STUDIO JUDGMENT
Labels must expose the metric and its status/qualification before tone optimization. Avoid unsupported simplifications such as `return` when the value is distributions only, `profit` for cash received, or `final` for estimated ROC/tax. Where a calculation basis materially changes interpretation, surface the basis near the value or through discoverable supporting content.

## Localization stress corpus
KRW/USD, long translated metric names, signed percentages, tax/ROC qualifiers, dates, zero/negative values, missing estimate, unavailable rate and stale-data states. Necessary wording must not be shortened solely to preserve a compact card.

## OPEN
No Flutter ARB/gen-l10n/TMS round trip; no Korean/English linguistic review; no human comprehension evidence.

## HANDOFFS
Type must accommodate full strings; Layout must reflow rather than truncate truth; Color cannot substitute for qualifiers; Web/native artifacts should bind locale/resource revision.