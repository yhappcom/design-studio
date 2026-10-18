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

## 2026-10-14 — Profile-scoped missing-period and crew-capability gate (C96)

Read-only source-family verification: three Skia PDFs and one PDC-generator PDF retain distinct generator/tag/ToUnicode fingerprints; this is file-structure evidence only, not a parser PASS. The existing C51 synthetic case 08 (`printed Period absent => unsupported`) is under-specified: missing a period that a particular validated profile requires is an unsupported-layout error, but a structurally recognized Skia document with no independently authenticated four-digit operational year is a **detached year-unverified review candidate**, not automatically an unknown PDF layout. Keep these two cases separate in the next versioned oracle. PDC-generator lacks crew columns: `not provided` is not an empty crew snapshot or evidence of deletion. A changed crew snapshot with identical BLH, A→B→A, and conflicting payload under one fingerprint require independent review/integrity outcomes; scalar `SourceEvidenceHistory` notice is not a crew revision detector. A synthetic standalone 18-case classification oracle passed; no real Flutter parser or owner-ledger match was tested. Existing-record-only, zero automatic attachment/create/overwrite, public P2 and production OPEN remain unchanged.

## 2026-10-16 21:00 KST — C153 evidence-only replay/lifecycle contract

Read-only product cross-check: LogMate MASTER inbound authority, import/CrewConnex contracts, SourceEvidenceHistory, LedgerMutationPlan, SembastLogbookRepository and repository types. Existing CrewConnex corpus rechecked as private reference only; no private payload was transferred to Design Studio. Public parser grade remains P2; production implementation OPEN.

**New decision distinction:** exact receipt replay is not a new evidence admission. The previous C152 synthetic SQLite model checks active Flight revision before replay. A controlled counterexample confirms an already-accepted identical receipt is rejected after a canonical record revision changes, despite the original durable observation and binding remaining. This is a **synthetic-model limitation**, not an observed LogMate bug. Proposed contract: check exact owner/unlocked status and immutable receipt/source integrity first; return original receipt as CURRENT or HISTORICAL depending on live record/revision; never re-activate an old binding, and apply active-Flight/expected-Revision CAS for every NEW approval inside one transaction. A deleted/restored record leaves old binding historical until separately reviewed. New interpretation under another profile version is a separate reviewable observation, not overwrite.

**Direct code-level lifecycle audit:** current Sembast repository defines a separate local replica identity store; it is absent from the explicit account-wipe drop list and the missing-schema-marker known-data check. Fresh initialization calls capability publication, which preserves an existing replica identity. This is source-code behavior requiring product-owner review of account-deletion replica-rotation policy, not proof of a security exploit. It is distinct from future CrewConnex evidence stores, which MUST be explicitly covered by wipe, known-data checks, capability/migration/reopen validation and failure-injection tests. Do not use replica identity as user ownership or roster revision authority.

Suggested evidence-only persistence separation: immutable source observation (file fingerprint + family + physical locator); immutable profile-version interpretation (raw labels, capability, provenance); owner-approved record binding with exact UID and approved record RevisionId; durable unique receipt. Unknown Skia year and ambiguous date/crew antecedents remain detached. PDC subject header is not a crew snapshot. Never mutate canonical FlightRecord, totals, generations, projection, baseline or canonical outbox.

Adversarial research checks: existing C152 SQLite oracle 38/38 PASS; independently reproduced its after-revision replay rejection; a separate fully synthetic C153 state model passed 18/18 lifecycle checks (replay after revision/delete/restore, new approval CAS, receipt/source collision, wrong/locked owner, missing crew capability, ambiguous candidate, wipe, unchanged canonical values). Neither is Dart/Sembast or production parser validation.

**Product acceptance still OPEN:** actual Dart/Sembast evidence-only transaction and per-store schema migration; file-backed reopen; simultaneous writers; same-source conflicting profile reinterpretation; account deletion with local replica policy; real UID-owned Flight candidate cardinality; source-bound Skia operational year/publication proof. Next integrated target: implement and run the evidence-only Sembast test matrix in an authorized product development workspace, or obtain independent same-export Skia year/revision evidence; research automation must not modify LogMate.


## 2026-10-19 — C210 original-binary reconciliation and detached evidence gate

Read-only private 71-page historical Skia PDF and seven original company XLSX files were independently byte-matched to current LogMate Git blobs (8/8). Numeric PDF candidates: 1,164; company supported numeric 7C identifiers: 1,144 of 1,154 original rows. Exploratory source-key candidates: 1,042 unique same-date, 93 unique +/-1-day, 29 unmatched. One of the 1,042 is a page-top, BLH-absent row with no row-local or same-page date; retain as CROSS_PAGE_DATE_CONTEXT_REVIEW. Conservative disjoint result: 1,041 same-date, 93 date-shift review, 29 unmatched, one cross-page hold. These are NOT owner UID FlightRecord joins.

Eight 2020-2023 historical unmatched: three same-date flight/one-endpoint route disagreements, two same-date route/flight-number disagreements, three same flight+route on a different date (nearest 19-461 days); no exact full key within +/-7 days. All 56 same-date PDF BLH vs original company bt discrepancies were independently reconfirmed (49 within 1-5 min; seven larger); PDF Base elapsed equals its own BLH in 56/56, PDF BLH equals company Actual in 0/56. Neither source value has precedence. BLH-absent 31 cases remain missing, not zero or Base-derived. A second PDF engine confirmed 128/128 selected fields on 16 rows across 11 pages.

ParserProfile v1.19 RESEARCH proposal: distinguish own-date, same-page context and cross-page context; preserve raw activity/crew/BLH/clock/provenance and report-family detector; separate company-source cardinality from owner-ledger cardinality; all partial-key/shift/unknown-revision cases detached. Evidence-only binding requires reviewed active UID Flight Revision CAS and separate evidence-head CAS plus immutable receipt; zero FlightRecord creation, canonical Block overwrite, aggregate or ordinary Sync LWW mutation. Synthetic file-backed SQLite 8/8 PASS only; actual Dart/Sembast, backup/wipe and owner-ledger binding OPEN. Public P2 unchanged, Production OPEN. No private rows/IDs retained.
