# W077 — Reorder Mutation Browser Closure

Date: 2026-09-18
State: STAGE 3 PRACTICE / RUNTIME CLOSURE SPECIFICATION

## Purpose
W076 defines scenario provenance for reorder equivalence. I064/L068 expose a missing browser-level question: after DOM/widget order mutates, does semantic identity, active focus, scroll position, visible focus, target geometry and status feedback remain coherent in the served product?

## SOURCE
WCAG 2.2 is the studio baseline. Relevant criteria include Keyboard, Focus Visible, Focus Not Obscured (Minimum), Dragging Movements and Target Size (Minimum). W3C's WCAG 2.2 summary explicitly describes a non-drag pointer alternative for drag operations and 24×24 CSS px target-size minimum with defined exceptions.

Sources:
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

## Browser manifest extension
For every I064 mutation add to W076:
- build/commit and route;
- engine/version;
- viewport, DPR, zoom/text scale;
- semantic ID order before/after;
- active element/semantic identity before/after;
- focused target rectangle before/after;
- scroll offset before/after;
- overlap/obscuration result;
- accessible name/role/state for reorder controls;
- status feedback payload/text;
- console/runtime exceptions;
- result = EXECUTED-PASS | EXECUTED-FAIL | NOT-EXECUTED | BLOCKED.

## Closure ladder
1. widget/runtime semantic oracle;
2. production Web build;
3. served primary browser;
4. independent engine;
5. 200% text/zoom + light/night/forced-colors;
6. network/persistence scenarios only when those product capabilities exist;
7. screen-reader/human evidence remains a separate level.

No lower rung is promoted to a higher-rung PASS.

## CRITIQUE
A test that checks only final list order misses a class of real browser failures: active focus can stay on a recycled index rather than the moved semantic item; scroll anchoring can jump; sticky UI can obscure the new focus position; accessibility names can refer to stale positions; status text can announce a result inconsistent with the actual DOM/order. W077 makes those failures first-class.

## PERFORMANCE BOUNDARY
Reorder interaction may later affect responsiveness, but local event duration or synthetic tooling is LAB evidence. LCP/INP/CLS are FIELD only when provenance-bearing field aggregate/RUM evidence exists. Do not infer field INP from a single automation trace.

## RELATED DOMAIN CHECK
Type T046: resolved font/fallback and wrapped feedback. Color C077: visible focus/state after mutation. Layout L068: geometry/scroll stability. Interaction I064: behavioral oracle. Content CD083: structured move-result and locale realization.

## HANDOFFS TO OTHER SPECIALISTS
Return any browser contradiction to the owning domain: stale focus identity → Interaction; clipping/scroll jump → Layout; invisible/merged focus → Color; fallback/wrap defect → Type; stale/false status → Content.

## OPEN
Non-drag control is not yet implemented; independent-engine/forced-colors/screen-reader/physical-device/field Core Web Vitals/human UX remain OPEN.