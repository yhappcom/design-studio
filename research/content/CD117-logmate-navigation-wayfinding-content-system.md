# CD117 — LogMate Navigation and Wayfinding Content System

Date: 2026-09-20  
Purpose: Stage 3 cross-surface content-system transfer for NAV-001.

## RELATED DOMAIN CHECK
T080, C111, I098/L102 and Web runtime/history evidence requirements checked. Content does not invent destinations, route state or recovery behavior.

## SYNTHESIS
A navigation label names a destination/task scope; it does not describe current focus, transient selection, save state or browser history. Cross-surface consistency means stable destination identity, not mechanically identical surrounding sentences.

## PRACTICE — content jobs
For every canonical primary destination maintain:
- stable destination ID;
- canonical English product label;
- optional page heading realization;
- current-page accessible semantic supplied by implementation rather than duplicative prose where appropriate;
- nested-detail parent/return wording;
- dirty-draft exit/recovery message only when Interaction exposes that state;
- empty/offline/error text owned by the destination rather than the navigation label.

Stress `Home`, `Logbook`, `Add Flight`, `Activity`, `Settings/Customize` only as candidate fixture labels until implementation confirms the actual IA.

## CRITIQUE
Reject wording that changes destination identity to fit a narrow dock, uses directional geometry (`the blue tab`, `left menu`) as the only instruction, calls focus/selection the current page, promises draft preservation without runtime evidence, or changes terminology between Home/ledger/form for stylistic variety.

Product-authored LogMate UI remains English-only at present. Source/user Unicode and locale-sensitive date/number behavior remain separate stress inputs.

## Reproducible validation
Use I098 route scenarios. Compare visible label, heading, accessible current-state payload, parent/return wording and dirty-draft recovery across direct entry, nested entry, Back/Forward, reload, narrow/reflow and enlarged/text-spacing states.

## HUMAN EVIDENCE BOUNDARY
Expert consistency review is not wayfinding comprehension, discoverability, memory or workload evidence. Representative-pilot validation remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Type receives full unshortened labels; Layout receives non-negotiable semantic identities; Color must not be referenced as sole locator; Web validates visible/a11y payload and history-dependent wording.

## OPEN
Actual production IA and labels, production voice approval, linguistic review, screen-reader comprehension, representative-pilot wayfinding.