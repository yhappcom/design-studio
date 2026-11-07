# CrewConnex implementation readiness & integrated execution gate — 2026-11-07

**Current gate: OPEN / NOT IMPLEMENTATION-DECISION-READY / NOT DEPLOYABLE.** This is a Design Studio research handoff; it does not authorize writes to LogMate or new product policy. LogMate [MASTER](https://github.com/yhappcom/logmate/blob/main/MASTER.md), [Import](https://github.com/yhappcom/logmate/blob/main/docs/specs/import-contract.md) and [CrewConnex](https://github.com/yhappcom/logmate/blob/main/docs/specs/crewconnex-parser-plan.md) contracts remain authoritative. Related consolidated files: [synthesis](RESEARCH_SYNTHESIS_20261107.md), [ParserProfile](PARSER_PROFILE_SPEC_20261107.md), [evidence register](EVIDENCE_DECISION_REGISTER_20261107.md).

## 2026-11-07 product-authority correction and static gate proof

**Do not impose a universal Publication-token gate as a product decision.** C360 and current LogMate MASTER/import/CrewConnex contracts do not explicitly approve this as a universal requirement. G2 requires a resolved **source revision policy**: verified Publication when available, otherwise HOLD_POLICY_PUBLICATION until owner explicitly approves an unknown-publication/fingerprint/review policy. Unknown publication never authorizes silent overwrite or date/crew inference. Distinguish this policy decision from the still-unverified source 4-digit year and Firebase UID/active-Flight binding.

**Direct source inspection at current HEAD, static only:** `sembast_logbook_repository.dart` _lbkStoreRegistry contains **30** named stores (lines 239–273), _syncLbkStoreRegistry adds **7** (lines 274–283); exportWholeLedgerBackup iterates all **37** (lines 470–500). SourceEvidenceHistory.requiresUserNotice only checks normalized scalar when both typed candidates exist; equal BLH cannot prove unchanged crew snapshot. CrewParticipant requires nonempty name; PDF raw staff/role codes do not establish it. These are concrete design constraints, **not** a newly executed native deletion/backup leak or runtime test. Require future source-only store to appear in validated store/owner/wipe/backup/restore policy with zero canonical mutation.

## 2026-11-07 14:xx — backup format and restore compatibility gate

**New static-source-specific implementation finding (not runtime PASS):** At LogMate current `sembast_logbook_repository.dart` blob `f2b8b0eb681f5d960532dac5c87b29cf85a459b8`, `exportWholeLedgerBackup` (lines 448–500) snapshots the **37-store** `_syncLbkStoreRegistry` and embeds exact ordered `storeRegistry` names/key types/counts plus `sourceCapability` and digest in a whole-ledger `.lbk` container. `_validateLbkContainer` (lines 6176+) switches on only **two** recognized backup format versions (legacy 30-store and sync-aware 37-store), requires exact registry length/order/name/key type/count, and requires the version's exact capability. `restoreWholeLedgerBackup` (lines 519–585) restores only into fresh staging, preserves destination replica ID, locks owner and resets imported Sync trust. `_requireEmptyLbkDestination` (lines 6413+) enumerates current nonempty stores; `_validateRestoredLbkReferences` (lines 6484+) checks ledger/aggregate but **has no CrewConnex evidence store to validate**.

**Derived consequence:** Merely adding a CrewConnex source-only evidence/receipt store to the current 37-store registry would change its exact shape. Without an explicitly versioned `.lbk` format/capability migration and backward-compatible decoder, old sync-aware backups would be rejected by the new strict registry, or new evidence could be omitted if a developer left the registry unchanged. Neither outcome is acceptable by default. This is a **forward-design incompatibility risk**, not an observed failure or data leak. It must be closed before production source-only persistence.

**Acceptance addition G3/G4 (not executed):** Define a new versioned evidence-store/receipt schema and `.lbk` backup-format migration policy; preserve restore support for old 30-store and 37-store containers; require new backup to include all approved source-only evidence and **exclude raw employee IDs/PDF**. Validate exact store inventory, key types, owner UID, checksum, source capability, duplicate keys, receipt/source head reference consistency, and stale/unknown version rejection. Exercise (a) old v1/v2 backup -> new code staging restore, (b) new backup -> new code round-trip, (c) new backup -> old code unsupported with no partial state, (d) one missing/extra/misordered evidence store, (e) wrong UID, (f) same BLH but changed crew fingerprint, (g) fault injected after stores written, (h) wrong-owner/delete/reopen, (i) reset Sync trust and destination replica identity. The source-only data's intended inclusion in Sync/backup and retention **requires explicit owner policy**, not a research-invented mandate. Existing source code validates strict current backup shape; no actual new-store code, migration, or Dart test is claimed.

**Independent adjacent-value assessment:** This check closes a previously underspecified **migration/test-design decision**, but not a production G3/G4 gate. Original C512 binary + independent renderer remains unavailable in the GitHub text connector; native CrewConnex evidence-only storage tests require a separately authorized LogMate Work. Company 2026 Aug coverage cannot be extended by interpreting the existing Aug02-ending workbook. No private bytes were copied; master CSV market/sample grades unchanged.

## 1. Completed evidence does NOT imply production readiness

| Dimension | Evidence already recorded | Unresolved gate |
|---|---|---|
| Private Skia source | June/July/Aug original Flate/ToUnicode parse, 62 candidates/310 physical selected field locators; 43 curated unique Preview-source links; 19 August outside Preview | Verified 4-digit operational year, source subject, Publication/revision and full active owner Flight match |
| Company comparator | 2018–2026 nine XLSX decoded in prior research; 2026 = 159 rows and observed Aug end Aug02; 43 curated source comparisons | Company Aug03–31 coverage or explicit unresolved policy, independent same-export year/UID evidence |
| PDC source | One original PDF 48 Activity, 26 numeric, 22 nonflight, 31 Date groups; C532 original strict detached HOLD plus 55/55 original-dependent checks | Exact C512 21 original-derived mutations into C426 strict function + independent standard PDF render/paint |
| Synthetic/manifest tests | Multiple metadata, layout, and negative-fixture passes (C195, C533 etc.) | No synthetic result qualifies as new real source, multi-airline portability or Dart runtime PASS |
| Product domain | SourceEvidence scalar, SourceEvidenceHistory append-only domain, CrewParticipant minimal type and UID-owned existing ledger/revision CAS framework | No CrewConnex source-only BLH/crew snapshot store, verified name binding, separate evidence head/receipt/double CAS, native runtime tests |
| Product import | MASTER identifies production Import coordinator, review storage/UI and export/re-import as OPEN | Need authorized LogMate implementation Work and real build/device acceptance |

User-verified company current values are authoritative. CrewConnex creates **zero** FlightRecords or canonical Block/total updates; unknown Date, code, crew, publication, operating status or owner must remain unresolved.

## 2. Binding gates and closure evidence

| Gate | Required action / success predicate | Existing evidence level | Status |
|---|---|---|---|
| G0 — Input family and source scope | Immutable Skia/PDC/TSV detectors, provenance fingerprints and raw field locator; unsupported layout and nonflight => zero flights and zero attachments | C194 original, C426 one-original strict research, TSV contract | PARTIAL / OPEN |
| G1 — Cross-validator independence | Re-execute **exact** C512 original-derived 21 PDFs in same strict C426 code path plus independently rendered PDF and field geometry; Skia 3-month multi-page/Sum/nonflight/MCID checks | C512 position-only original-derived oracle, C533 synthetic 21, C532 baseline+55 completed | OPEN |
| G2 — Authenticated association | Same-export 4-digit year, subject-to-Firebase UID, revision/Publication or explicit unknown revision disposition, airline/flight/date/route, unique active same UID Flight; company period coverage | C194 43 preview links and incomplete August comparator | OPEN |
| G3 — Data schema & atomic persistence | Source-only BLH+crew snapshot separate from canonical Block/Flight, immutable observation/revision and EvidenceHead+FlightRevision CAS + owner decision+receipt; fault rollback | Current SourceEvidence scalar code, C233 analysis; no runtime implementation | OPEN |
| G4 — Owner lifecycle / privacy | Same-UID replay, concurrent stale heads, deleted/aliased Flight, wrong owner, restore/new UID, backup/Sync/retention; no staff IDs or private raw source ever durably persisted | Static code review only for CrewConnex path | OPEN |
| G5 — End-to-end product experience | File selection, authenticated preflight, pending/review/conflict/error/recovery, proof that no existing record/totals mutate unexpectedly; native & supported PWA + offline old profile, accessibility | Product plans only | OPEN |
| G6 — Lawful transfer / airline variation | Anonymized lawfully shareable real PDF/TSV for additional format/version, source-target acceptance and regression; no scraped portal or credential feed | Private source + weekly HTML instructions P3; no public CrewConnex raw P1 | OPEN |

**Product release requires all applicable gates**, explicit owner approval of any unresolved policy, real same-build acceptance and release-specific checks. G1 and G3 can progress with bounded test harness independently of G2, but **G2 cannot be bypassed** to commit a real observed crew snapshot to an owner ledger.

## 3. Integrated high-information-gain execution package

**Priority A — exact independent PDF validation, no repetitive baseline:** Obtain current C426 source (already in Design Studio), C512 original-derived mutation recipe, unchanged authorized PDC binary **read-only** from LogMate. Reconstruct 21 mutations transiently and test unchanged original + all exact 21 in *the same strict parser path* with independent PDF renderer, inspect page/paint/text alignment and error dispositions; include malformed physical stream, misleading overlays, out-of-group C/I-C/O placement and nonflight-positive exceptions. Record only test scopes, fixture hashes/abstracted failure reasons, not PDF bytes or private strings. C532 baseline + 55/55 need not be reintroduced as a previously unexecuted task.

**Priority B — authentication/coverage:** On 3-month Skia and PDC original source, independently identify report subtype, printed time period vs operational year/century, source subject/carrier and Publication. If not printed/verified, document SOURCE_AUTHORITY_UNRESOLVED and require an owner-confirmed separate binding design rather than guessing from PDF name, weekdays, local/base time or company row. Seek coverage-complete 2026 company August dates or explicitly HOLD all 19 uncurated comparisons until source coverage permits; compare Date + approved flight + route and duration only with full provenance/revision, tally 0/1/many and unresolved distinctly. No private roster values leave LogMate.

**Priority C — atomic evidence-only implementation acceptance:** In separately authorized LogMate Work / isolated Dart test checkout, design receipt/state for an authenticated existing owner Flight without changing canonical record/current totals. Test two revisions (active FlightRevision and EvidenceHead), user-approved source-only snapshot, same source replay, changed-crew same BLH, wrong UID, closed/deleted Flight, duplicate candidate, concurrent transactions, fault injection after each intended write, reopen, restore and backup export. Prove **no FlightRecord CREATE, canonical Flight UPDATE, total/checkpoint/outbox mutation** on HOLD/FAIL or evidence-only success; on conflict or crash no partial receipt/evidence. This is a **future acceptance packet**, not current tests run or authorization to change LogMate.

**Priority D — operational UX and regression:** Before shipping, file-selection and versioning under native iOS/Android and Tablet/EFB PWA; unknown layout/revision/error copy and accessible recovery; exact source fingerprint/photo privacy policy; old profile after offline release; no PWA raw file upload. Draw directly from real implementation, not screenshot-only research.

Packages A/B/C should be coordinated where tooling and permissions permit; they are one connected readiness push, not one microscopic question per hourly trigger. If original source year/owner evidence cannot be acquired in a lawful cycle, document the specific blocker and complete the independent tests possible under G1/G3 instead.

## 4. Proposed runtime test assertions

| Scenario | Expected state/effect |
|---|---|
| Parser detects unsupported report, nonflight, malicious/malformed locator, summary row | FAIL_DOCUMENT/exclude; **Flight writes=0, evidence writes=0** |
| Valid source but missing 4-digit year, subject UID, publication or current Flight match | DETACHED_HOLD; **Flight writes=0, source association=0** |
| 0 or 2+ company/Flight candidates, company beyond Aug02, source same-day ambiguity | REVIEW/HOLD, no auto reconcile or date correction |
| Existing verified Flight, owner explicit approve of source-only snapshot | Only allowed observation/revision/receipt changed transactionally, never canonical Block or totals |
| Receipt same exact request replay | Idempotent result, no repeated writes/notification; revalidate owner/active Flight as required |
| Same normalized BLH, changed fingerprint, publication, crew or raw role | New source revision noticed and resolved; not hidden by scalar equality |
| Stale FlightRevision or EvidenceHead; wrong owner, deleted Flight, UID change | Conflict/reject, all evidence/current/receipt unchanged |
| Crash between intended writes; DB file close/reopen | Whole transaction rollback or exactly-once persisted receipt; no half-committed view |
| Account deletion; different UID logs into same device; backup restore | Prior owner evidence/employee identifiers cannot leak; store wipe/known-data/backup/Sync coverage audited |
| Cross-family Skia/PDC/TSV document with matching raw numeric Activity | No fallback parse by column-count or code alone; separate immutable profile/version admission |

For any actual test result, record code SHA, fixture origin (REAL ORIGINAL vs REAL-DERIVED vs SYNTHETIC), execution command, environment, pass/fail/hold counts, expected vs observed state, affected durable stores, and limitations. A documentation-only assertion has no PASS status.

## 5. Readiness decisions that must be explicit

1. **Source-only storage contract:** namespace and immutable observation/receipt identity distinct from canonical SourceEvidence scalar; lifecycle/retention/owner bounds and Sync projection.
2. **Revision/Publication fallback:** if export lacks a stable token, whether repeated file fingerprint plus explicit user confirmation is acceptable, and what changes cause a notice. No automatic inferred publication order.
3. **Crew identity:** name-bearing verified source mapping or a privacy-safe unresolved snapshot model; staff ID and staff rank remain prohibited durable fields.
4. **Matching policy:** full-key uniqueness, UID ownership, active Flight, ±1 day candidate review, missing Date and incomplete company coverage handling; no automatic date correction.
5. **Parser support claim:** exact supported family/profile/version, PDC 14-column vs Skia tagged, TSV optional; third-party HTML or calendar UI cannot be advertised as supported Import.

These decisions are research proposals subject to LogMate owner/MASTER/spec approval; Design Studio must not silently elevate them.

## 6. Stop rule and scheduling guidance

For recurring roster research, after each run ask: "Did this close a named G0–G6 gate with newly reproducible evidence?" If not, record precise blocker; advance to another adjacent high-value CrewConnex gate. Do not re-count 62/43/31, repeat the already-executed C532 baseline, treat C533 synthetic 21 as exact C512, or spend an entire hour retrying C194 index safety blocks. Keep [revalidation queue](REVALIDATION_QUEUE.md) keyed to these gates.

Historical C194 index-sync debt remains OPEN; meaningful unsynced deltas must be reconstructed from source with fresh fetch, not fabricated. Current four master CSVs do not require no-op changes in the absence of new market/sample/field-grade evidence.

## RELATED DOMAIN CHECK

Design Studio Type/Color status and current Layout/Interaction/Web/Content status reviewed. Type/Color are not the primary acceptance gate for private PDF parsing. Layout/Interaction owns user decision and safe failure, Content owns uncertainty/action/recovery semantics, Web owns PWA file/offline profile compatibility. No visual/human/device test was performed in this consolidation.

## HANDOFFS TO OTHER SPECIALISTS

**Engineering/LogMate:** implement/validate only after a separately authorized Work, retaining existing-record-only and owner authority. **Interaction/Content:** define exact review/unsupported/conflict/changed-evidence statuses before public copy. **Web/PWA:** validate old-profile offline and no-source-upload behavior in served build. **Market/Marketing:** current evidence does not authorize "CrewConnex supported" release claims.
