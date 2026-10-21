# C265 — Integrated source-locator provenance and evidence-only acceptance gate
2026-10-21 12:55 KST. Research only. LogMate read-only. No private raw roster, names, employee IDs, flights or crew contents copied.

## Source-derived independent audit
Fresh-read C194 privacy-safe manifest: 62 Skia candidates (June 18, July 22, August 22), 310 selected Activity/From/To/BLH/ACReg physical field locators. This is independent recomputation from a real-PDF-derived manifest, **not** a fresh original PDF decode or canonical owner-Flight match.

| Key, omitting other identity components | Unique/310 | Collision groups | Affected fields |
| --- | ---: | ---: | ---: |
| page + MCID (no source) | 286 | 23 | 47 |
| page + primary TR + TD (no source) | 249 | 57 | 118 |
| source SHA + page + field + TD (no TR) | 70 | 40 | 280 |
| source SHA + page + primary TR + TD | 310 | 0 | 0 |
| source SHA + page + MCID | 310 | 0 | 0 |

The 23 cross-source page+MCID collision groups span June/July 9, July/August 10, June/August 3 and all three 1. Source+MCID also happens to be collision-free in this selected subset, **not** proof that page can be omitted for general multi-leaf crew TDs or page-local MCID reset. Immutable provenance must preserve source-byte SHA-256, report family/profile, page, primary Table/TR, TD, MCID, and cell/leaf order. This extends C264's within-source 280/310 result with a quantified multi-month collision gate.

## Direct current LogMate code and contract check
Read AGENTS.md, MASTER.md, import-contract.md, crewconnex-parser-plan.md, approved Manual Delta Sync, SourceEvidence, SourceEvidenceHistory, CrewParticipant, LogbookRepository, LedgerMutationPlan, Sembast repository, current capability codec, and Sembast draft-save, rollback and migration tests. Current codec **version 16**, legacy page-policy v15; real v15→v16 migration tests exist. Draft Save receipt checks exact request fingerprint but its first Save invokes canonical _commitLedgerMutation, writing Flight revision/outbox, advancing ledger data generation and publishing aggregate checkpoints. It is **not** a CrewConnex evidence-only method. Scalar SourceEvidence/notice and mandatory-name CrewParticipant cannot authenticate detached BLH/crew snapshots or manufacture a name from Emp.#. Generic Flight LWW excludes external Import SourceEvidence. The .lbk trust and evidence-only persistence APIs are not implemented.

## ParserProfile v1.27 research contract (NOT approved implementation)
1. **Source observation:** retain source SHA-256, immutable family/profile, physical locator, raw label and explicit missing/blank/unknown states. A PDF timestamp or four-digit cell token cannot authenticate Skia operational year/publication.
2. **Trusted parser stage:** issue VerifiedSourceStage only from independently validated source-bound period/year, detector, nonflight/Sum barriers, required flight fields, BLH and crew-continuation checks. Otherwise detached review; never accept a caller-supplied verified boolean.
3. **Owner approval:** bind exact trusted stage digest, verified unlocked Firebase UID, unique active Flight ID, expected FlightRevision and EvidenceHead, explicit review and receipt ID. Full date+7C flight+route is candidate filtering, not proof of UID ownership.
4. **Atomic source-only commit:** re-read trusted stage/approval, verify full request fingerprint, active UID-owned Flight, dual CAS and receipt collision; atomically append observation/head/receipt. No canonical Flight/Block, record revision, generic outbox, data generation, structure, page projection, aggregate, baseline or Custom change. All writes roll back on failure.
5. **Replay/revision/lifecycle:** identical receipt is read-only historical replay; changed fingerprint/locator/crew/BLH/UID/Flight is collision. Same BLH/new crew is a distinct snapshot requiring review. Delete/alias/restore cannot silently reactivate evidence. Imported backup stages/approvals/receipts are quarantined pending verified owner/epoch/source trust; no raw source PDF backup or automatic generic Flight LWW. Register new stores in capability migration, known-data, wipe, reopen and backup.

## Real Dart/Sembast acceptance specification (NOT EXECUTED)
Use a separately authorized LogMate implementation task, not this research workspace. Existing memory database, openForTesting, rollback snapshots and v15→v16 tests are harness patterns; add a dedicated source-only API and failure probe.

| Group | Negative/positive scenarios |
| --- | --- |
| Source | wrong Skia/PDC family; yearless/omitted Date without independent authority; nonflight/after-Sum; malformed BLH; unverified crew |
| Owner/match | locked/wrong UID; missing/deleted Flight; zero or ambiguous full-key candidates; stale Flight Revision |
| Proof | forged stage; altered SHA/profile/page/TR/TD/MCID/crew/BLH/approval |
| Concurrency | two approvals with one EvidenceHead; stale Flight CAS; identical receipt replay vs changed-payload collision |
| Revision | same BLH changed crew; changed BLH; A→B→A; same normalized value/new fingerprint |
| Lifecycle | delete/restore/alias; wrong-owner replay; account wipe; restored-stage quarantine |
| Atomicity | failure after observation/head/receipt writes rolls back every evidence store |
| Reopen/backup | file reopen; migration; old/forged .lbk; fresh replica identity |
| Invariants | before/after canonical active/deleted, revisions, outbox, structure, generations, projection, aggregate, baseline and Custom bytes equal |

**Evidence/readiness:** Actual manifest recomputation and static current-code review only; no new PDF/XLSX original-byte parsing, Dart/Sembast execution, or production parser. C260 real 2025 workbook correction is ntTme=0, instTme=2, toCnt=4, ldCnt=5; reversed older notes are stale. Public P2 unchanged, Production Parser OPEN. No deployment/sample/field grade change, so master CSVs are not edited. Adjacent CrewConnex questions completed this cycle: cross-month collision, current capability, Draft receipt ordering, canonical side effects, external-Sync/backup trust and acceptance matrix.

**One next integrated target:** certify Skia 2026-06/07/08 same-export year/period/publication and 27 undated rows' crew antecedents; date-aware adjudicate 19 uncurated August rows against company full keys; execute UID-owned source-only Sembast lifecycle tests once separately authorized implementation exists.
