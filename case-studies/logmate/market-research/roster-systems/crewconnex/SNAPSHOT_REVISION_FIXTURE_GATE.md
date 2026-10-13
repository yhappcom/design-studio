# CrewConnex synthetic snapshot-revision regression gate — 2026-10-10

Status: RESEARCH / NOT IMPLEMENTATION PASS. Entirely synthetic. No source roster, crew names or IDs are reproduced.

Authority: LogMate MASTER.md and docs/specs/import-contract.md plus docs/specs/crewconnex-parser-plan.md. CrewConnex is existing-FlightRecord-only crew snapshot and BLH evidence; never a FlightRecord creator.

## Direct code/test evidence

- `SourceEvidence` holds sourceFileFingerprint, sourceLocator, parserProfileId and parserProfileVersion, but not a roster-publication identity.
- `SourceEvidenceHistory` groups one record, one canonical field and one source system. When two observations have equal normalized values, `requiresUserNotice` is false even if sourceFileFingerprint changes. The existing source-evidence-history test explicitly confirms this behavior.
- `CrewParticipant` has required name, optional raw position/duty code and optional operating/deadhead status. Snapshot identity/order/source linkage/history are OPEN in current MASTER.
- Matching operational date plus complete flight identifier is only a weak review-candidate signal in current MASTER, not duplicate identity or automatic attachment.

## Synthetic fixture contract

Given one already-existing canonical flight (fixture-only ID F-A), use two separate, synthetic CrewConnex snapshots:

- Snapshot A: fingerprint A, source locator A, raw BLH 01:25, participant [CREW_A, raw role X, raw code Q].
- Snapshot B: fingerprint B, source locator B, raw BLH 01:25, participant [CREW_B, raw role Y, raw code R].
- Both snapshots have the same synthetic date, flight number and route; publication/revision identifier is absent. No employee IDs.

Expected assertions:
1. No new FlightRecord, no silent canonical mutation, and no inferred PIC/SIC/PF/PM.
2. Two source observations may preserve identical normalized BLH with distinct fingerprints; scalar notice logic alone does not classify crew revision.
3. Different participant content across fingerprints creates a detached crew-snapshot conflict/review candidate; no automatic replacement, forward-fill, or deletion.
4. The same source fingerprint plus identical snapshot is idempotent as a source observation, subject to future approved import persistence semantics.
5. Unknown publication ID is `unverified`, not an ordering key; PDF CreationDate and software asset version cannot establish newer roster authority.
6. A second case with duplicate same-date/same-flight canonical candidates must remain ambiguous even when BLH agrees.
7. Unknown/unsupported PDF family, non-flight activity or missing required anchor produces zero automatic enrichment.

## Remaining evidence

Existing July/August Skia PDF page-2 date-like text has not been independently attributed to the primary tagged table versus summary/auxiliary sections. GitHub binary-blob reading returned UnicodeDecodeError in this cycle; do not infer a roster year or revision from those tokens. Real redacted PDF fixture and multi-month detector acceptance remain OPEN.

Public parser-corpus grade P2; production parser OPEN. Next CrewConnex target: implement and verify this wholly synthetic two-snapshot conflict oracle without altering LogMate.

## 2026-10-13 — C76 source-key/date candidate gate

A read-only independent decode of 159 company rows in `flightHistory_2026.xlsx` was compared against 43 **manually transcribed** archive import-preview entries (18 June, 22 July, three August). The archive's flight+registration+route key yields 40 unique and three multiple-candidate entries when the date is omitted. When the manually assigned full date is used as a ±1-day **review-candidate comparison**, all 43 yield one company candidate: 37 same-date and six roster-date +1 day. The 43 selected company `bt` values equal the archive's transcribed BLH values. This is an archival preview/source cross-check, **not independent PDF parsing, PDF-year authentication, actual canonical FlightRecord matching, or BLH/Block semantic equivalence**. It cannot authorize automatic attachment or date correction.

**Additional synthetic fixture requirements (not production-tested):** (a) same flight+registration+route on two dates, (b) one date omitted with both candidates retained, (c) a one-day shift offered for review only after source-bound year/date validation, (d) equal BLH on competing candidates does not resolve identity, (e) source file/locator exact repeat idempotence while changed crew with same BLH remains a conflict, (f) canonical ledger with 0/1/>1 candidate records distinct from company-source cardinality. Unknown year, unverified section/crew antecedent and missing publication order remain detached. No standalone FlightRecord creation.
