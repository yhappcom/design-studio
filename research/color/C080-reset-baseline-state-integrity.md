# C080 — Reset Baseline State Integrity

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION** of C078–C079 for I067 Reset provenance.

## RELATED DOMAIN CHECK
I067 defines baseline state; L071 defines geometry; CD086 verbalizes consequence; T049 protects strings; W080 owns rendered browser evidence.

## State matrix
Treat these axes independently: `dirty/at-baseline`, `Reset enabled/disabled`, `focus/pressed`, `recovery available/unavailable`, `visibility shown/hidden`, `selection/insertion`, and future-only `local/persisted/synced`.

Required contradictions include:
- at-baseline + focused Reset;
- modified + Reset available + focused row;
- Reset applied + Undo available;
- Reset no-op + no new recovery transaction;
- hidden field + baseline restoration;
- future only: locally reset + persistence failure/ambiguous.

## Acceptance
Evidence chain remains `semantic state → token → paint owner → visible surface → non-color cue → accessible meaning`. Disabled/no-op must not collapse into hidden; Reset/recovery must not reuse financial success/error semantics; focus remains perceivable across state change and forced-colors transformation.

## WCAG boundary
WCAG 2.2 is the current W3C baseline. Color-only meaning remains unacceptable where state must survive nonvisual/forced-color access. Actual forced-colors and independent-engine evidence is required; token inspection is not PASS.

## OPEN
No rendered C080, forced-colors, independent-engine, calibrated-display, observer or human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Layout must preserve non-color state cues after recomposition; Content supplies explicit baseline semantics; Web captures computed/visible state; Interaction owns enabledness and transaction truth; Type owns text rendering.