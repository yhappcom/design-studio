# I095 — Cross-surface workflow signature transfer

Date: 2026-09-20
Status: Stage 3 PRACTICE / TRANSFER VALIDATION DESIGN

## Purpose
Test whether LogMate signature survives end-to-end professional workflows rather than merely producing visually related screens.

## Authority chain
record/task identity → available action → intent → state transition → feedback → recovery → route return → persisted/synced truth.

The chain must remain legible across Home→ledger retrieval/edit, Home→Add Flight→validation/commit, import→mapping→preview→commit/Undo, and Customize→reorder→save/restore.

## Signature invariants
- SC-A: local semantic calibration survives route changes; identical coordinates are unnecessary.
- SC-B: information roles survive representation changes.
- SC-C: functional boundaries appear when consequence/state requires them; chrome is not added for sameness.
- SC-D: transition and recovery communicate state change but never substitute for transaction truth.

## Falsification
FAIL if route change changes object identity, action meaning, focus ownership, validation semantics, recovery availability, or persisted-state truth merely to preserve a visual pattern. FAIL if Bottom Dock is treated as proof of app-wide navigation semantics, or if Home Search behavior is inferred from Add Flight airport lookup. NAV-001 and SEARCH-001 remain open.

Drag-based reorder remains incomplete until an equivalent non-drag single-pointer mechanism is implemented where WCAG 2.2 SC 2.5.7 applies.

## Reproducible scenarios
1. Home recent item → View Logbook record → edit → cancel/commit → route return.
2. Home/Add Flight → invalid field → correction → review/commit → Undo where supported.
3. Import → mapping ambiguity → resolve → preview → commit → batch Undo.
4. Customize → reorder using each supported input path → save → return/reload.

Capture semantic object ID, route/history identity, focused object, action/state, feedback payload, recovery target, transaction/inverse ID, and final projection hash.

## Human boundary
Discoverability, cognitive load, confidence, interruption cost, and representative-pilot workflow performance remain HUMAN evidence and are not inferred from deterministic traces.