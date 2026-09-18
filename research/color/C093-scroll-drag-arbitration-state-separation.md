# C093 — Scroll/drag arbitration state separation

Status: STAGE 3 PRACTICE / TRANSFER SPEC
Date: 2026-09-19

## Problem
A touch stream inside a scrollable reorder surface can be pending, scrolling, reorder-previewing, cancelled, committed or recoverable. Color must not fabricate ownership before semantic resolution.

## State axes
Keep independent: focus; selection; pressed/pending; reorder preview; candidate validity; scroll/UA ownership; cancelled/arena-lost; committed move; boundary no-op; recovery eligible; failure/superseded; hidden/disabled.

## Rules
- Pending/pressed is not committed.
- Scroll ownership does not receive success/reorder paint merely because the stream began on a reorder affordance.
- Cancel/arena-loss clears transient preview paint.
- Recovery color appears only from eligible committed history.
- Focus indication remains distinguishable from preview/selection/recovery.
- Forced-colors must preserve meaning through structure/system colors/non-color cues; hue-only distinctions fail.

## Validation matrix
Run I080/L084 families at baseline, 200%, forced-colors and independent engine once product runtime exists. Compare semantic state payload with actual paint owner and visible indicator.

## Evidence boundary
No forced-colors, independent-engine, physical-device or human recognition PASS is claimed.