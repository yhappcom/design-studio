# CD113 — LogMate Date Representation Content Contract

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION — no gate promotion**

## PURPOSE
Resolve the Content side of H3 while preserving LogMate's English-first product language and localization-ready architecture.

## RELATED DOMAIN CHECK
T076, C107, I094/L098 and W107 checked. CD112 content invariants remain authoritative.

## CONTENT CONTRACT
`canonical date identity ≠ storage/value syntax ≠ user-visible date representation ≠ native browser presentation ≠ validation message ≠ commit/persistence result`.

Product-authored English UI does not imply that browser-native date controls render one fixed ordering. Conversely, locale-aware rendering does not authorize changing professional meaning or product state.

## PRACTICE
Maintain a date representation inventory by semantic role: editable date field, compact ledger date, detail/review date, filter/range date, source/import date. For each role record whether representation is product-authored or browser-native, whether ordering is fixed by product policy or runtime locale, and how the complete date is recovered if compact presentation truncates.

Do not use ambiguous shorthand merely to save width. Do not label a browser-localized presentation as if it were the canonical stored syntax. Error/recovery text names the affected field/date, not its incidental pixel format.

## CRITIQUE
The same date can be represented differently without semantic inconsistency; literal-string sameness is not the goal. The failure is when users cannot reliably identify the date, ordering becomes ambiguous in context, or different surfaces imply different record truth.

## SYNTHESIS
Date content architecture is role-based: one canonical identity, explicitly governed surface realizations, and no layout-driven semantic mutation.

## OPEN
Final product date-display policy, any user-configurable format, representative-pilot comprehension, linguistic review, AT evidence.

## HANDOFFS TO OTHER SPECIALISTS
- Type/Layout: receive the full permitted strings, not shortened convenience fixtures.
- Interaction: keep display change separate from mutation.
- Web: verify native vs authored presentation and resolved locale in runtime.