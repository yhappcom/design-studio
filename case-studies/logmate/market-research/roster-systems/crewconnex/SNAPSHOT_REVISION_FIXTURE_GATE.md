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
