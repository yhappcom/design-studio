# I107 — Cross-Concept Failure-Injection Authority Fixture

## PURPOSE
Advance I106 from invariant review to an executable authority fixture that can falsify Candidate 05/07 implementations.

## RELATED DOMAIN CHECK
T089, C120, L110, W119 and CD125 checked. This work intentionally repeats shared workflows as TRANSFER VALIDATION under failure and interruption rather than baseline presentation.

## PRACTICE / CRITIQUE
Use identical logical fixtures in both candidates:
1. Month change: request -> pending if applicable -> authoritative period/projection -> restore.
2. Recent Flight: open record -> mutate if available -> Back -> correct restored projection.
3. Add Flight: invalid -> correct -> submit -> failure/unknown -> safe Retry/recovery -> authoritative result.
4. View Logbook: route -> Back/Forward -> focus and context restoration.
5. Activity range: proposal -> selection -> projection; stale projection must not masquerade as current.

Inject interruption/failure at every boundary where the implementation can distinguish requested, pending, unknown and authoritative states. A visible control is not proof of enabled action; visual completion is not proof of persistence/sync.

Failure conditions include duplicate mutation after blind Retry, stale projection winning over newer authority, lost focus/context after Back, candidate-specific semantics for the same product action, and invented Search behavior. Search remains shell until SEARCH-001 exists.

## EVIDENCE BOUNDARY
No runtime execution, AT, discoverability, workload, trust or representative-pilot evidence is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Content maps each authority state to language; Color maps state salience; Layout preserves owner/recovery relationships; Web executes and records provenance; Type stress-tests resulting strings without semantic abbreviation.
