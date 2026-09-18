# L085 — Edge-autoscroll and reflow geometry

Status: STAGE 3 PRACTICE / GEOMETRY TRANSFER SPEC
Date: 2026-09-19

## Purpose
Measure whether edge-autoscroll remains spatially legible and semantically stable under long-list, 200% reflow, sticky and safe-area conditions without treating visible motion as proof of user intent.

## METHOD
For I081 families record at baseline and 200%: viewport and scroll-container rectangles; top/bottom edge zones; drag boundary; source/proxy/candidate/focus rectangles; sticky surfaces and safe-area intersections; scrollOffset(t); pointer coordinate; candidate semantic ID. Repeat each executable family twice.

## ACCEPTANCE
A stationary pointer may see rows move because the viewport scrolls, but geometry alone must not silently redefine commit authority. Edge zones must not be fully obscured by sticky controls or unsafe areas. Reflow must not cause clipping, unreachable destinations or focus obscuration. WCAG 2.2 SC 2.5.8 target-size compliance is recorded by the exact PASS clause rather than assumed from visual size. Non-drag controls remain independently measurable.

## CRITIQUE
FAIL when autoscroll makes candidate identity visually ambiguous; a sticky region creates an invisible hot edge; 200% causes the active control/focus to be obscured; a spatial fix requires shortening semantically necessary content; or geometry is used to infer transaction success.

## RELATED DOMAIN CHECK
Type T062: strings/metrics are inputs, not adjustable escape hatches. Color C093: state visibility must survive geometry changes. Interaction I081 owns semantic authority. Web W093 owns served runtime provenance. Content CD099 owns result wording. This is TRANSFER VALIDATION of I081 into spatial evidence.

## OPEN
No physical-device, independent-browser, AT or human motor-performance PASS.