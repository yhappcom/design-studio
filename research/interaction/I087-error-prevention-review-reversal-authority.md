# I087 — Error Prevention, Review, and Reversal Authority

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION + CONTRADICTION REVIEW

## RELATED DOMAIN CHECK
Type T068 keeps provisional drawing out of product geometry; Color C099 separates autofill/validation state; Layout L090 owns form/review geometry; Web W099 owns served browser provenance; Content CD105 owns form language. Interaction owns the actual submission, mutation, reversal and recovery contract. No separate UX canonical owner exists, so end-to-end UX is treated as cross-cutting evidence.

## SOURCE
WCAG 2.2 SC 3.3.4 Error Prevention (Legal, Financial, Data) requires, for covered submissions that create legal/financial commitments, modify/delete user-controllable stored data, or submit test responses, at least one of: reversible submission; input checking with correction opportunity; or review/confirm/correct before finalization. WCAG 2.2 SC 3.3.6 Error Prevention (All) extends the same three alternatives to all information submission at Level AAA. W3C technique G168 describes confirmation as one sufficient technique for irreversible actions, but techniques are not themselves normative requirements.

Sources: https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html ; https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-all.html ; https://www.w3.org/WAI/WCAG21/Techniques/general/G168

## AUTHORITY MODEL
`edited draft ≠ validated draft ≠ review representation ≠ confirmation intent ≠ committed mutation ≠ reversible checkpoint ≠ undo success ≠ persisted/synced state`.

A confirmation dialog is not automatically the safest design. Reversibility can reduce interruption when the inverse is truthful and durable; review-before-commit is preferable when consequences are broad or the inverse is incomplete. Destructive or history-sensitive professional records require explicit classification of consequence and reversibility before choosing a pattern.

## PRACTICE MATRIX
For LogMate-like professional records, exercise: edit a reversible display preference; delete a user-entered flight record; replace imported data; Reset customized fields; commit a multi-field edit after review; attempt an invalid mutation; Undo within and beyond an allowed recovery window; navigate away and return. Record stable object ID, draft hash, validation result, review payload hash, action/consequence class, commit transaction, inverse/recovery eligibility, focus restoration and projection hash.

## CRITIQUE / FAILURE CONDITIONS
FAIL if confirmation is added reflexively to every mutation; destructive wording hides the object or scope; review payload differs from the committed payload without disclosure; Undo is offered when no reliable inverse exists; a failed inverse is reported as restored; irreversible mutation is committed before the user can inspect the material consequence; or browser/framework lifecycle is mistaken for persistence truth.

## REPRODUCIBLE VALIDATION
Replicate each executable family twice. Compare reversible/no-confirm, review-before-commit, explicit destructive confirmation, cancel, failed validation, Undo, Reset, Back/Forward, 200%, forced colors and independent engine. Human comprehension of consequence, error rate, interruption cost, trust, AT behavior, physical-device behavior and representative-pilot workflow remain OPEN until observed.

## HANDOFFS TO OTHER SPECIALISTS
L091 measures review/confirmation/recovery geometry and focus continuity. C100 separates destructive, invalid, committed and recovery states. CD106 defines object→consequence→recovery language. T069 stress-tests review/destructive/recovery strings after T021. W100 captures served commit/inverse/projection provenance and must not call lab/runtime evidence persistence or human PASS.