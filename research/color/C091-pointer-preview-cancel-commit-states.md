# C091 — Pointer preview, cancellation and commit state separation

Status: PRACTICE / RENDERED TRANSFER OPEN

## Question
Can pointer press/preview, valid destination, cancellation, committed move, focus, selection, recovery, no-op and failure remain visually distinct without color becoming the source of transaction truth?

## State model
Keep these axes independent: `focus`, `selection`, `pressed/preview`, `candidate destination`, `valid/invalid destination`, `cancelled`, `committed success`, `boundary no-op`, `recovery eligible`, `failure/superseded`, `hidden/disabled`.

Cancellation is not failure and preview is not success. A ghost/drag preview must not look like a committed row. A pressed Move control must not impersonate keyboard focus. A valid destination cannot rely on hue alone, and forced-colors must retain ownership/eligibility through structure, text, border/shape or other non-color cues.

## Practice
Render I078/L082 scenarios in light, night and forced-colors once executable. Capture before/down-preview/cancel/commit frames plus semantic owner and transaction result. Re-run at 200% and independent engine.

## FAIL conditions
- cancelled preview retains success/recovery styling;
- focus and pressed state collapse into one indistinguishable accent;
- invalid/boundary destination is communicated only by reduced opacity or hue;
- forced-colors removes the distinction between candidate and committed state;
- color suggests a mutation that the I078 transaction ledger says did not occur.

## Evidence boundary
No rendered C091, forced-colors, independent-engine, calibrated-display, observer or human PASS is claimed.