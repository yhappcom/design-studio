# W091 — Served pointer cancellation and commit-event manifest

Status: PRACTICE / SERVED TRANSFER OPEN

## Goal
Prove I078 in the actual product/runtime instead of accumulating isolated Chromium gesture tests.

## Runtime manifest
For each scenario record build/commit, route, browser/engine/version, OS, viewport, zoom/text scale, theme/forced-colors, pointer type, semantic object/action ID, pointer down/up/cancel sequence, Flutter recognizer/action result when observable, candidate destination, commit event, tx/branch/inverse IDs, projection hash before/after, focus owner, visible/a11y status, recovery eligibility, target/focus/preview rectangles, scroll/obscuration and runtime exceptions.

## Scenario matrix
1. native/Flutter Move control down-inside → leave target → up-outside;
2. normal up-inside activation;
3. drag abort at origin/approved abort area;
4. valid drag drop;
5. pointercancel/gesture-arena loss where reproducible;
6. cancellation followed by keyboard and explicit non-drag pointer move;
7. boundary no-op, Undo and Reset interaction.

Each family runs twice with the same scenario ID lineage. Promotion ladder: actual product implementation → production Web build → served primary engine → independent engine → 200% → forced-colors. Browser/framework documentation is SOURCE, not runtime PASS.

WCAG 2.2 SC 2.5.2 is the Level A cancellation floor; SC 2.5.7 remains the AA non-drag alternative requirement and SC 2.5.8 the AA target-size floor. These are separate acceptance axes.

## Performance evidence boundary
Lighthouse, DevTools and CI synthetic results remain LAB. LCP/INP/CLS become FIELD evidence only with provenance-bearing aggregate/RUM from the served product population.

## Blockers
The repository does not yet provide executable non-drag reorder/product runtime evidence for this family. Until implementation exists, no browser, pointer-device, screen-reader, physical-device or human PASS is claimed.