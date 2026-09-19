# CD105 — Redundant Entry, Autofill, and Form Content System

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION

## RELATED DOMAIN CHECK
I086 owns provenance/validation truth; L090 owns geometry; C099 owns visual states; Web owns browser evidence; Type owns rendering. Content does not redefine browser autofill or application commit semantics.

## CONTENT CONTRACT
`previously supplied ≠ still valid`; `autofilled ≠ validated`; `browser restored ≠ app restored`; `restored draft ≠ committed`; `committed ≠ Saved/Synced`; `re-entry requested ≠ re-entry essential`.

For same-process information, prefer auto-population or selection when WCAG 2.2 SC 3.3.7 applies. If re-entry is required, content must reflect a real validity/security/essential exception rather than inventing friction. Supported personal-data fields use programmatically appropriate input-purpose semantics where SC 1.3.5 applies.

Sources: https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html ; https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html

## COMPLETE SYSTEM TRANSFER
Forms: label, hint, validation and recovery share one field identity. State: restored/dirty/invalid/committed remain distinct. Onboarding: explain reuse only if needed for task success. Retrieval: restored values remain inspectable/changeable. Tone: neutral for restored values; warning only for actual consequence. Localization: EN/KO preserves object/action/consequence and 200% expansion. Accessibility: visible and programmatic payloads may differ in verbosity but not truth.

## PRACTICE MATRIX
Exercise repeated aircraft/registration/crew/context data, invalidated prior value, browser fill, app-restored draft, user overwrite, Reset, Back/Forward and review-before-commit. Produce concise visible feedback plus richer accessibility payload only when state change warrants it.

## FAILURE CONDITIONS
Saved/success wording for autofill; 'required again' without justified exception; error wording for intentional overwrite; ordinal-only identity; hidden provenance that changes recovery eligibility; instructions that depend on color or spatial location; localization shortened by dropping consequence.

## VALIDATION BOUNDARY
Actual EN/KO runtime fit, linguistic review, AT comprehension and representative-pilot task evidence remain OPEN.

## HANDOFF
T068 stress-tests strings after T021. C099 protects semantic states. L090 protects inspection/recovery geometry. W099 returns actual browser/app provenance.