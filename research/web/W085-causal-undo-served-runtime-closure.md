# W085 — Causal Undo Served-Runtime Closure

Date: 2026-09-18
Stage: Stage 3 PRACTICE
Purpose: PRODUCT TRANSFER / INDEPENDENT VALIDATION of I072, L076, C085, CD091 and T054 constraints.

## RELATED DOMAIN CHECK
I072 supplies causal transaction/focus truth; L076 supplies geometry measurements; C085 separates restored/current-focus/recovery paint; CD091 supplies semantic payloads; T054 prohibits premature Type compensation.

## SOURCE
WCAG 2.2 is the current W3C baseline used by Studio. SC 2.4.3 requires focus order preserving meaning/operability; SC 2.4.11 is the AA Focus Not Obscured floor; SC 4.1.3 covers status messages. APG button guidance is useful pattern guidance but not browser/AT product proof.

Sources:
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://www.w3.org/WAI/ARIA/apg/patterns/button/

## CLOSURE MANIFEST
For each I072 scenario capture in one record:
- product build/commit and route;
- browser engine/version;
- viewport, zoom/text scale, theme/forced-colors;
- transaction_id/inverse_of and eligibility;
- changed/restored semantic object IDs;
- intervening action ID and semantic owner;
- current browser/Flutter focus semantic owner;
- accessibility name/role/state/status payload where observable;
- semantic order/projection membership;
- focus/restored/recovery rectangles;
- scroll offsets and obscuration;
- visible feedback;
- console/runtime exceptions.

## EXECUTION LADDER
1. actual product/widget behavior;
2. production Web build;
3. served primary engine;
4. same scenario in independent engine;
5. 200% text/zoom;
6. light/night/forced-colors.

Do not promote a higher rung from lower-rung evidence. Run each available causal family twice. Mark `NOT-EXECUTED` or `BLOCKED` explicitly rather than inferring PASS.

## CRITIQUE
Final configuration equality is insufficient: a stale inverse may restore state while overriding a later action or stealing focus. Visible focus is insufficient if it belongs to the wrong semantic object. Static accessibility markup is insufficient if runtime status/focus differs.

Persistence/offline/Sync scenarios remain dormant until implementation truth exists. Non-drag single-pointer reorder remains a major Stage-closure blocker for SC 2.5.7-related product transfer.

## PERFORMANCE EVIDENCE
Lighthouse, DevTools and CI traces remain LAB/synthetic. Only provenance-bearing RUM/aggregate data may support FIELD LCP/INP/CLS claims; no field Core Web Vitals claim is made here.

## HUMAN EVIDENCE BOUNDARY
Screen-reader, physical-device, discoverability, workload and representative-pilot evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Return runtime contradictions to the owning domain rather than fixing them silently in Web. Preserve shared scenario IDs so evidence can be compared across Interaction, Layout, Color and Content.