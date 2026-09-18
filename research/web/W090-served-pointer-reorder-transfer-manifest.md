# W090 — Served pointer reorder transfer manifest

Status: Stage 3 PRACTICE / PRODUCT RUNTIME OPEN

## Closure target
Stop accumulating isolated browser micro-tests. I077 must be validated in the actual product build with equivalent drag and single-pointer movement paths.

## Scenario manifest
For every run record build/commit, browser+version, OS/input modality, viewport/text scale, forced-colors state, semantic object/action IDs, invocation path (drag vs single-pointer alternative), source/destination, transaction/branch/inverse IDs, projection hash before/after, focus owner, visible+a11y status, target/focus rectangles, scroll/obscuration and runtime exceptions.

Families: adjacent, multi-position, boundary no-op, first↔last, hidden/system-group boundary, repeated move, move→Undo, move→Reset. Run each twice for REPLICATION.

## Promotion ladder
actual product implementation → production Web build → served primary engine → independent engine → 200% → forced-colors. A Chromium-only harness is LAB evidence, not stage closure.

## Performance evidence
Lighthouse/DevTools/CI synthetic results remain LAB. LCP/INP/CLS become FIELD evidence only with provenance-bearing real-user/aggregate telemetry tied to an identifiable deployment/population/window. Do not relabel lab surrogates as field metrics.

## Accessibility baseline
Use WCAG 2.2, especially SC 2.5.7 Dragging Movements and SC 2.5.8 Target Size (Minimum), while preserving stronger Studio workflow criteria from Interaction/Layout/Content.
