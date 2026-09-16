# W034 — Restoration / cache / authority transfer

Evidence: **SOURCE → SYSTEMS PRACTICE / BROWSER TRANSFER OPEN**

## RELATED DOMAIN CHECK
T021 keeps mature font metrics in use; C034 defines forced-colors transfer; I021 defines authority/freshness truth; L025 defines staleness/conflict spatial priority; CD039 owns resumption/retrieval wording.

## Why W034
W033 defined a product-like resumption fixture, but browser restoration can preserve a plausible presentation without proving that data is current. Web must therefore distinguish browser/navigation restoration from product authority reconciliation.

## Browser/runtime matrix
For each scenario — normal reload, navigate away/back, history traversal, restoration from a browser cache mechanism where observable, offline return, later deep link — capture:
- engine + OS + commit SHA;
- navigation/restoration type and relevant lifecycle events;
- object/operation ID;
- local/presented revision;
- authoritative revision/check result;
- semantic certainty/action ID;
- viewport + visualViewport;
- locale;
- forced-colors state;
- focus target and geometry;
- raw network/reconciliation trace.

A route/history success is not an authority-check PASS. A restored DOM is not current-state evidence.

## Accessibility transfer
WCAG 2.2 remains the baseline. Focus Visible and Focus Not Obscured are tested separately from semantic state survival; stronger Focus Appearance observations are recorded separately from AA closure. Forced-colors uses actual engine/user-color behavior rather than a screenshot recolor simulation.

## Performance boundary
Restoration paths can alter experienced performance, but W034 does not promote synthetic timings to field Core Web Vitals. LCP/INP/CLS field claims require actual field/RUM population context. Lab/restoration timing remains diagnostic only.

## Stage-3 value
An executed W034 artifact would close a more consequential Web gap than another isolated Chromium component test because it joins route/history, cache/restoration, real authority reconciliation, responsive geometry, accessibility modes, localization and independent-engine provenance around one professional workflow.

## Evidence boundary
No new browser run is claimed in this repository-only cycle. Chromium plus an independent engine are required before cross-browser claims; Safari claims require Safari. AT and physical mobile remain separate.

## HANDOFFS TO OTHER SPECIALISTS
I021 consumes restoration-vs-authority evidence. L025 consumes rectangles/reachability. C034 consumes forced-colors computed/rendered evidence. CD039 consumes semantic ID/revision/locale binding. Type remains on mature fallback until T021.