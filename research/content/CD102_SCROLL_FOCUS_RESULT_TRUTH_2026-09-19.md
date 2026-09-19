# CD102 — Scroll / Focus Result Truth

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Related: I083/L087/W096

## Protected semantic distinctions
`viewport moved ≠ object moved`
`scroll restored ≠ focus restored`
`focus restored ≠ reorder restored`
`ordinal changed ≠ object identity changed`
`visible position stabilized ≠ transaction succeeded`
`local commit ≠ Saved/Synced`

Visible and accessibility feedback must resolve from semantic object + transaction result + focus result, not scrollOffset, anchor adjustment, widget index or geometry alone.

## Complete-system transfer
Apply these distinctions to forms/state/onboarding/retrieval/tone/localization: reorder help must not promise positional stability the runtime cannot guarantee; recovery copy must identify the affected object/action rather than narrate browser mechanics. Actual EN/KO literals remain OPEN until runtime fit and linguistic review.

## Critique
Reject messages that infer success from viewport stabilization, say an item was restored when only scroll position returned, or expose `scroll anchoring` as user-facing jargon without an action/recovery reason.

## RELATED DOMAIN CHECK
Type T064/T065 rendering constraints; Color C096 focus-state cues; I083 semantic authority; L087 geometry; W096 browser evidence. CD101 result/focus truth is extended, not replaced.

## Evidence boundary
No multilingual production, AT comprehension, linguistic review or representative-human PASS is claimed.