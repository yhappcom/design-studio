# W043 — Temporal Provenance and Timezone Runtime Transfer Contract

Status: **STAGE 3 PRACTICE / RUNTIME TARGET READY — EXECUTION OPEN**

## RELATED DOMAIN CHECK
I030 owns time/ordering truth; L034 owns chronology geometry; C043 owns visual cue degradation; CD049 owns timestamp semantics/localization; Type T021 remains behind repair/rerender/general spacing. This study extends W042 rather than opening another isolated browser micro-test.

Purpose: **PRODUCT TRANSFER + RUNTIME CLOSURE EXTENSION**.

## Current-source check
- WHATWG HTML defines `<time datetime>` as a machine-readable representation and distinguishes local from global date/time forms: https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-time-element
- Unicode CLDR date/time patterns are locale-dependent and include timezone formatting; user 12/24-hour preferences may differ from locale defaults: https://cldr.unicode.org/translation/date-time/date-time-patterns
- WCAG 2.2 remains the accessibility baseline: https://www.w3.org/TR/WCAG22/

These sources define platform/formatting constraints; they do not define the product's authoritative event ordering.

## Runtime scenario

Extend the W042 chain:

`history reconstruction → r1 snapshot export → authority r2 → artifact open in locale/zone A → live recheck in locale/zone B → changed/current/unavailable resolution → history inspection`

Add clock cases:

- client wall clock intentionally offset from authority time;
- locale changes while underlying instant/revision stays constant;
- timezone changes across DST/offset boundary;
- offline-created event uploads later;
- authority revision exists without trustworthy domain-event time.

## Provenance schema
Each captured timestamp carries:

`semanticRole | rawInstantOrNull | clockSource | authorityRevision | locale | timezone | formattedText | machineReadableValue | orderingBasis | certainty`

Do not use formatted text as a database key, ordering key or state selector.

## Browser evidence
For each engine/run capture:

- browser/engine/version and commit SHA;
- object/event/artifact/run IDs;
- raw authority revision and clock source;
- locale, timezone and 12/24-hour preference when controllable;
- rendered timestamp text and machine-readable value;
- DOM/accessible reading order for role/value pairs;
- computed styles plus C043 degradation condition;
- L034 geometry and page-break positions;
- recheck action state before/after authority response.

Cross-browser claims require Chromium plus an independent engine; Safari claims require Safari execution.

## Acceptance rules
PASS for this study requires executed artifacts showing that locale/zone/clock changes alter presentation without silently altering authoritative state, chronology basis or action safety. Reload/deep-link/print/export must reconstruct from durable data, not component memory.

## Performance boundary
Export/recheck duration, script timing and synthetic navigation timing are lab/functional diagnostics. LCP/INP/CLS become field evidence only with actual field/RUM population context.

## Evidence boundary
No W043 runtime artifact exists yet. No cross-browser, Safari, AT, physical-device/print, field Core Web Vitals or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
I030 receives ordering/runtime contradictions. L034 receives geometry/read-order failures. CD049 receives locale/zone semantic failures. C043 receives computed visual-state failures. Type receives timestamp-string transfer only after T021 gates close.
