# CD107 — Import preview, duplicate resolution and recovery content system

Date: 2026-09-19
State: STAGE 3 PRACTICE — COMPLETE-SYSTEM EXTENSION; linguistic/human evidence OPEN

## RELATED DOMAIN CHECK
Uses I088 as state/action source truth, L092 for batch/row geometry, C101 for non-color-dependent semantics, W101 for browser/runtime provenance and T021/T069 for downstream rendering constraints. Forms/state/onboarding/retrieval/tone/localization remain one system.

## SOURCE
WCAG 2.2 SC 3.3.1 requires detected input errors to identify the item and describe the error in text. SC 3.3.3 requires known correction suggestions where appropriate. SC 4.1.3 requires qualifying status messages to be programmatically determinable without requiring focus.

## CONTENT MODEL
Protected distinctions:
`file selected ≠ read ≠ parsed ≠ validated ≠ duplicate classified ≠ resolved ≠ previewed ≠ imported ≠ Saved/Synced`.
`exact duplicate ≠ possible duplicate ≠ invalid row ≠ excluded row`.
`Cancel before commit ≠ Undo after commit`.

Batch content must expose counts that reconcile with row truth: ready to import, exact duplicates excluded, possible duplicates requiring review, invalid rows requiring correction/exclusion. Row content names the record/object, problem/classification, consequence and available recovery. Progress/status copy must not steal focus merely to announce routine progress.

## PRACTICE
Create runtime payload slots rather than frozen prose: `source_file`, `record_identity`, `classification`, `reason`, `suggested_correction`, `selected_resolution`, `batch_counts`, `commit_result`, `undo_availability`, `persistence_truth`. Stress English/Korean, long filenames, flight number/registration/DEP/ARR, dates and ambiguous duplicate candidates.

## CRITIQUE / FAILURE
FAIL: “Import complete” after parse only; “Error” for every duplicate; unexplained count mismatch; generic “Something went wrong” where row and known correction exist; “Saved” without persistence evidence; “Undo” after inverse expiry; color-referential instructions; inaccessible status that requires focus movement solely for announcement.

## OPEN
Final EN/KO wording, professional linguistic review, screen-reader comprehension, actual pilot interpretation of duplicate choices and task-performance evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Interaction owns classification and available resolutions. Web must verify visible/accessibility payload parity. Layout must keep batch and row consequences associated at 200%. Type must stress full semantic strings rather than abbreviating them for fit.
