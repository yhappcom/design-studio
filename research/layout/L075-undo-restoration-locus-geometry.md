# L075 — Undo Restoration Locus Geometry

## Purpose
TRANSFER VALIDATION of I071: measure the spatial consequences of restoring a disappeared object while preserving, or deliberately changing, the current interaction locus.

## RELATED DOMAIN CHECK
I070/I071 define semantic focus policy; C083 owns focus-state rendering; T052 owns rendering constraints; W083 owns served-runtime evidence; CD089 owns recovery semantics. Layout does not choose the focus owner before Interaction declares it.

## Practice model
Compare three post-Undo geometries at baseline and 200% text/zoom: (A) focus remains on Undo/recovery control, (B) focus remains on logical fallback field, (C) explicit product rule returns focus to restored field. For each, record focus rectangle, restored-object rectangle, viewport, scroll offset before/after, sticky/safe-area overlap, wrapping, target visibility and distance to the next intended action.

## Critique
A restored field becoming visible does not justify automatic scroll-to-field. A visually calm layout can still fail if focus identity is wrong; conversely a semantically correct focus policy can create excessive displacement. Geometry is therefore a second acceptance axis after I071 identity/agency.

## Reproducible validation
Run middle/end field hide→Undo, group collapse→recovery, Reset-hide→Undo, and a 200% recomposition inserted between mutation and Undo. Repeat each executable scenario twice. Classify: stable locus; minimal reveal; justified explicit return; excessive displacement; obscured; wrong semantic destination.

WCAG 2.2 Focus Not Obscured (Minimum) is the conformance floor for keyboard focus visibility; Studio acceptance is stricter where professional workflow continuity requires low-disruption continuation.

## Evidence boundary / OPEN
No rendered LogMate L075, independent-engine, physical-device or human workload PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Interaction consumes displacement evidence when choosing between preserve-locus and explicit-return policies. Color must render only the actual focus owner. Web records viewport/scroll rectangles. Content must not imply focus return merely because an object was restored. Type must not be compressed to suppress legitimate recovery wrapping.