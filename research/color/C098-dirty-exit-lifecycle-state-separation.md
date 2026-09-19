# C098 — Dirty Exit and Lifecycle State Separation

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: CROSS-DOMAIN TRANSFER VALIDATION

## RELATED DOMAIN CHECK
Transfers I085/L089 into Color while preserving C091–C097 state separation; uses CD103 semantic truth, W097 runtime provenance and T066 strings.

## SEMANTIC AXES
Do not collapse: focus, selection, dirty/uncommitted, warning/at-risk, committed, cancel/stay, discard, recovery, unavailable/stale, saved/synced.

Lifecycle facts such as hidden, pagehide, pageshow, bfcache and beforeunload have no success/error color semantics by themselves.

## PRACTICE / CRITIQUE
Validate light/night/forced-colors and independent engine when runtime exists. Check that:
- dirty is not styled as failure unless product truth is actually failure;
- discard is not styled as success merely because navigation completed;
- bfcache return cannot resurrect stale success/preview color;
- clean after Undo/Reset removes dirty semantics;
- meaning survives without color and in forced colors;
- focus remains distinguishable from dirty/warning styling.

## FAILURE CONDITIONS
Color-only dirty meaning; stale state attached to recycled ordinal slot; lifecycle event painted as Saved; warning styling masking focus; forced-colors collapse of dirty/focus/recovery.

## EVIDENCE BOUNDARY
No rendered C098, forced-colors, independent-engine/device, calibrated-display, observer or human PASS is claimed.