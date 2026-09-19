# L087 — Scroll-Anchor / Focus Geometry

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Related: I083, I082, L086

## Practice
Measure baseline and 200% geometry for focused semantic object, viewport, sticky/overlay surfaces and rows inserted/removed above it. Record scrollOffset delta separately from focus-rectangle delta and projection change.

Scenario bundle: reorder commit, cancel, Undo, Reset, status insertion, source-offscreen rebuild and 200% reflow. Repeat twice in primary and independent engines when executable.

## Geometry contract
Viewport stabilization is not semantic stabilization. A row may keep nearly the same visual y-position because of scroll anchoring while its ordinal changes; a focused semantic object may move visually while focus identity remains correct.

## Failure conditions
- focus restoration targets old ordinal instead of stable ID;
- application and browser scroll corrections compound into a jump/overshoot;
- sticky/overlay content entirely obscures focus after correction;
- 200% reflow causes clipping or unrecoverable displacement;
- geometry evidence cannot distinguish scroll delta from layout delta.

## RELATED DOMAIN CHECK
I083 owns behavioral authority; C095 owns visual state separation; W096 will own served engine evidence; CD102 owns wording truth; T065 remains rendering transfer only.

## Evidence boundary
No rendered product, independent-engine, physical-device or human spatial-orientation PASS is claimed.