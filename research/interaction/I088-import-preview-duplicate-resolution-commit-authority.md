# I088 — Import preview, duplicate resolution and commit authority

Date: 2026-09-19
State: STAGE 3 PRACTICE — SOURCE/SYNTHESIS/TRANSFER SPEC; runtime and human evidence OPEN

## PURPOSE
Extend I087 from individual mutations to LogMate's high-consequence batch-import workflow. The central risk is collapsing file selection, parse success, duplicate classification, user resolution, preview, commit and persistence into one apparent success state.

## RELATED DOMAIN CHECK
- Type: T021 remains upstream; T069 supplies review/recovery strings. No metric workaround is allowed.
- Color: C100 separates review/commit/recovery states; import needs additional parsed/conflict/excluded axes.
- Layout/Interaction: I063–I087 transaction/focus/recovery invariants remain binding.
- Web: W100 requires served transaction provenance; File/FileList/FileReader add browser-source provenance but do not establish product commit.
- Content: CD106 requires object→consequence→recovery truth; import needs row/batch error and duplicate language.
- UX: human duplicate comprehension, workload and pilot confidence remain OPEN.

## SOURCE
WCAG 2.2 Guideline 3.3 requires users to be helped to avoid and correct mistakes. SC 3.3.1 requires automatically detected input errors to identify the item and describe the error in text. SC 3.3.3 requires a known correction suggestion when an input error is detected, unless that would compromise security or purpose. SC 4.1.3 covers programmatically determinable status messages that report results, waiting/progress or errors without a change of context.

The Web File API exposes user-selected File objects from file input or drag/drop and asynchronous reading through FileReader. File selection/read completion therefore proves only acquisition/read stages, not parser validity, duplicate resolution, import commit or persistence.

## SYNTHESIS — AUTHORITY CHAIN
`file_selected ≠ file_read ≠ source_detected ≠ parsed ≠ normalized ≠ duplicate_classified ≠ user_resolution ≠ preview_accepted ≠ batch_committed ≠ persisted/synced`

A duplicate is not automatically an error. It is a classification requiring a policy/result: exact duplicate excluded, possible duplicate requiring review, replacement/update candidate, or distinct record. Parser rejection, validation error and duplicate classification must not share one generic failure state.

## STUDIO JUDGMENT
1. Preview is a proposed projection, not the database.
2. Batch commit authority requires stable sourceFileId/importBatchId plus stable record identity and explicit resolution policy.
3. Counts must be decomposable: selected/read/parsed/accepted/excluded/error/possible-duplicate/committed. A single “35 imported” number is insufficient when any rows were excluded or unresolved.
4. Row-level correction must preserve batch context; batch-level status must not hide unresolved rows.
5. Cancel before commit must produce no imported records. Undo after commit is a separate inverse transaction and must never be described as cancel.
6. File name/type/size are acquisition metadata, not trustworthy semantic source-system identity by themselves.

## PRACTICE / REPRODUCIBLE VALIDATION MATRIX
Use one deterministic fixture with: 20 valid new records, 3 exact duplicates, 2 possible duplicates, 2 malformed rows, 1 unsupported value and one source-system ambiguity. Run each executable scenario twice with identical fixture hash.

Scenarios: select→read→parse; parser failure; row validation failure with known suggestion; exact-duplicate exclusion; possible-duplicate review keep/skip; preview count reconciliation; cancel before commit; commit; Undo batch; repeated import of same fixture; Back/Forward/reload before and after commit; 200% reflow; forced colors; independent engine.

Record fixture hash, sourceFileId, parser/source-system result, normalized-record IDs, duplicate rule/version, per-row classification, resolution, preview hash, batch transaction/inverse IDs, projection hash, focus/status result and persistence truth separately.

## CRITIQUE / FAILURE CONDITIONS
FAIL if parse success is called import success; duplicate is colored or worded as error without policy basis; preview and committed counts diverge without explanation; a malformed row cannot be identified; known correction is withheld without reason; focus is moved merely to announce progress; cancel mutates data; Undo is offered without a valid inverse; browser file-read success is treated as persistence evidence.

## OPEN
Actual CrewConnex/AIMS/NetLine fixtures, physical iPad/PWA file-picker behavior, screen-reader announcement quality, human duplicate comprehension, representative-pilot workload, persistence/sync and production import implementation remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- Color: separate acquisition/parse/validation/duplicate/resolution/commit/recovery semantics.
- Layout: measure preview table/list, error-summary, row recovery and 200% geometry.
- Web: capture File API and parser/transaction provenance in served primary + independent engines.
- Content: create batch/row message grammar without collapsing duplicate, invalid and excluded states.
- Type: stress counts, filenames, flight identifiers and recovery labels only after drawing gate.
