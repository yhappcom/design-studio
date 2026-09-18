# I068 — Reset Post-Mutation Focus & Status Contract

## Purpose
Extend I067 from baseline correctness to continued operability after a bulk Reset. A correct baseline restoration can still fail interaction quality if focus loses semantic identity, becomes obscured, or status feedback misstates the consequence.

## RELATED DOMAIN CHECK
- Type: T021 remains upstream; do not compress strings to rescue geometry.
- Color: C080 keeps focus, dirty/baseline and recovery states orthogonal.
- Layout: L071 requires temporal geometry, not screenshot preference.
- Web: W080 requires served-runtime provenance.
- Content: CD086 distinguishes Reset/Undo/erase and baseline identities.
- Purpose: TRANSFER VALIDATION of I067 across focus/status behavior.

## SOURCE
WCAG 2.2 2.4.3 requires sequential focus order to preserve meaning and operability. WCAG 2.2 2.4.11 requires a focused component not be entirely hidden by author-created content. WCAG 2.2 4.1.3 requires status messages to be programmatically determinable without receiving focus where applicable. W3C supplemental cognitive guidance recommends clear feedback after user actions; this is supportive guidance, not an additional conformance criterion.

## PRACTICE — mutation families
For each declared `baseline_id/version`, execute:
1. focused field survives Reset;
2. focused field becomes hidden under Reset;
3. focus begins on Reset control;
4. already-at-baseline Reset/no-op;
5. Reset → Undo;
6. Reset → navigate away/back.

Record before/after: semantic order, visibility, active semantic ID, focused semantic ID, focus rectangle, viewport/scroll offset, obscuration, recovery availability, status payload, transaction ID.

## CRITIQUE / failure conditions
- FAIL: index is preserved but now identifies a different field.
- FAIL: focus falls to document/body with no deliberate recovery rule.
- FAIL: focus target is entirely obscured by sticky/recovery UI.
- FAIL: no-op Reset creates a false mutation or false success.
- FAIL: status claims Saved/Synced without persistence truth.
- PASS is not claimed from static reasoning.

## Reproducible validation
Run each available path twice. Compare semantic/focus/status signatures. Classify `EXECUTED-PASS`, `EXECUTED-FAIL`, `BLOCKED`, `NOT-EXECUTED`. Extend identical scenarios to 200% text, forced colors and an independent browser engine through Web.

## UX integration
Information architecture: Reset remains display-configuration scope, not flight-data scope. Flow: preserve a predictable recovery locus. Cognitive load: consequence feedback should re-orient without gratuitous focus relocation. Accessibility: focus and status are separate channels. Professional workflow: hidden fields remain data-preserving display choices.

## OPEN
Non-drag reorder implementation, actual Reset/Undo implementation, AT behavior, physical devices, representative-pilot discoverability/workload and persistence/sync semantics.

## HANDOFFS TO OTHER SPECIALISTS
Layout should measure post-Reset geometry; Content should encode changed/no-op/undoable consequence truth; Color should preserve focus/recovery state independence; Web should execute the full mutation matrix; Type should treat new strings as transfer corpus only.