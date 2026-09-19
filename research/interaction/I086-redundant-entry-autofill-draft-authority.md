# I086 — Redundant Entry, Autofill, and Draft Authority

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION + CONTRADICTION REVIEW

## RELATED DOMAIN CHECK
Content owns labels/instructions and recovery wording; Web owns browser autofill/runtime evidence; Layout owns field/review geometry; Color owns semantic states; Type owns rendering constraints. Interaction owns the task-state and authority model only.

## SOURCE
WCAG 2.2 SC 3.3.7 Redundant Entry (A) requires information previously entered by or provided to the user in the same process to be auto-populated or available for selection, except when re-entry is essential, needed for security, or no longer valid. SC 1.3.5 Identify Input Purpose (AA) separately requires programmatic identification of supported input purposes. HTML `autocomplete` tokens are browser-facing hints and do not prove application validation or draft truth.

Sources: https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html ; https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html ; https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill

## AUTHORITY MODEL
`previously supplied value ≠ browser autofill candidate ≠ browser-filled DOM/control value ≠ validated application draft ≠ committed configuration ≠ persisted/synced state`.

A repeated field in the same professional workflow must first be classified: same information and still valid; changed/expired; security-sensitive; essential re-entry; or genuinely new information. Only the first class is a Redundant Entry candidate. Autofill availability does not authorize silent commit.

## PRACTICE MATRIX
For a LogMate-like add/edit flow, run: repeated aircraft/registration/crew/context field with valid prior value; prior value now invalid; user overwrites an autofilled value; browser restores a value after Back/Forward; application restores an unvalidated draft; Reset clears the branch; locale EN/KO; 200% reflow. Record stable field ID, provenance (`user`, `browser`, `app-restored`, `selected-existing`), validation state, dirty branch, commit transaction and recovery eligibility.

## CRITIQUE / FAILURE CONDITIONS
FAIL if repeated information is demanded without a valid exception; browser autofill is labelled Saved; restored values bypass validation; provenance changes object identity; Reset leaves hidden restored values; browser autofill styling is used as semantic validation; or security/validity exceptions are invented merely to avoid redesign.

## REPRODUCIBLE VALIDATION
Replicate each executable family twice. Compare drag/non-drag configuration where relevant, Back/Forward/new-document return, 200%, forced colors and independent engine. Human comprehension, actual browser password-manager heuristics, physical-device keyboard/autofill UX and representative-pilot workload remain OPEN until observed.

## HANDOFF
L090 measures repeated-field/review geometry. C099 separates autofill/restored/validated/error state. CD105 defines complete-system language. T068 stress-tests resulting EN/KO strings after T021. W099 records browser/app provenance in served runtime.