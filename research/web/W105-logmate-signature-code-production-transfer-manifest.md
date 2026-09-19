# W105 — LogMate Signature-Code Production Transfer Manifest

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION PLAN — no runtime PASS**

## PURPOSE
Prevent concept approval from being mistaken for browser/product transfer. W105 converts SC-A–SC-D into observable production evidence requirements.

## RELATED DOMAIN CHECK
T074, C105, I092/L096, CD111, W104 and the coordinator Signature Code/Operational Geometry contracts checked.

## PROMOTION LADDER
For each candidate concept and applicable surface:
1. explicit invariant and fixture;
2. implemented LogMate surface;
3. production Web build;
4. served primary engine;
5. independent engine;
6. 200% / enlarged text and text spacing;
7. applicable light/night/forced-colors/reduced-motion;
8. real route, network and font-loading/fallback state;
9. physical mobile/iPad when input, safe-area, file-picker or lifecycle behavior matters.

A static screenshot can reject a concept but cannot complete this ladder.

## SHARED FIXTURE
Record concept ID, surface, viewport, DPR, engine/version, font-load state, theme/accessibility mode, fixture hash and route/state. Capture:
- semantic object IDs and state;
- key element rectangles and scroll offsets;
- computed font family/features for operational roles;
- visible + accessibility payload;
- focus owner;
- transaction/recovery state where applicable;
- screenshots as supporting evidence, not sole provenance.

## SIGNATURE-SPECIFIC OBSERVABLES
### SC-A Calibrated Axis
Measure local semantic starts/ends/baselines across repeated rows and after fallback/reflow. Reject visible comparison jitter even if the screenshot appears stylistically coherent.

### SC-B Operational Dual Voice
Verify actual loaded proportional/mono/fallback roles and Unicode/source-text fallback. Generic `monospace` is not exact production authority.

### SC-C Quiet Functional Boundary
Verify focus, selected, invalid, ambiguous and recovery ownership under authored-color loss and forced-colors.

### SC-D Measured Transition/Recovery
Verify reduced-motion behavior, stable end state, truthful inverse availability and focus/context restoration. Motion is never sole evidence.

## PERFORMANCE EVIDENCE BOUNDARY
Lighthouse, DevTools traces and CI synthetic measurements remain **LAB** evidence. LCP/INP/CLS become **FIELD** evidence only when provenance-bearing representative RUM/aggregate exists. Concept smoothness or local synthetic scores do not satisfy field performance evidence.

## HARD BLOCKERS
No Stage 3 closure is claimed until actual implementations exist for meaningful cross-surface transfer. Non-drag single-pointer reorder, H1–H7, independent-engine/device evidence and human/AT evidence remain open as applicable.

## SYNTHESIS
The signature stack becomes product authorship only after it survives fallback, reflow, alternate state systems and real browser/runtime conditions. Visual consistency alone is insufficient.

## HANDOFFS TO OTHER SPECIALISTS
Return measured font/fallback failures to Type, state-salience failures to Color, geometry/focus failures to Layout/Interaction, and semantic/accessibility payload failures to Content.