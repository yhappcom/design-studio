# L099 — Cross-surface geometry transfer ledger

Date: 2026-09-20
Status: Stage 3 PRACTICE / TRANSFER VALIDATION DESIGN

## Question
What geometry must remain stable for LogMate to feel and behave coherently across Home, View Logbook, Activity, Add Flight, import/review, and recovery surfaces?

## Result
Stable geometry means stable semantic relationships, not a shared page template.

### Protected relationships
- object identity adjacent to its primary operational values;
- comparison fields aligned locally where simultaneous comparison is required;
- state/action/recovery attached to the object they affect;
- focus remains visible and associated with the active object;
- sticky regions never obscure focus or recovery;
- responsive recomposition preserves reading/action order;
- large-text/date-width adaptation may change coordinates while preserving these relationships.

### Explicit non-requirements
Do not require identical card widths, gutters, row heights, dock offsets, heading positions, or global x-axes across unrelated surfaces. Copying Home geometry into a ledger/form is not signature transfer.

## Stress ledger
Validate baseline, narrow/reflow, enlarged text, WCAG text-spacing, long source/user strings, date-width variants, validation/recovery states, and forced-colors. Record bounding rectangles for object label, operational value group, state, primary/secondary action, focus, recovery, sticky regions, viewport, and scroll container.

## Falsification
FAIL if a protected relationship changes meaning; if recomposition separates consequence from action/recovery; if focus is obscured; if truncation becomes irreversible; or if a visual alignment survives only by shrinking type/content below the established contract.

## Gate consequence
No Stage 3 promotion. Implemented multi-surface evidence in primary and independent engines remains missing.