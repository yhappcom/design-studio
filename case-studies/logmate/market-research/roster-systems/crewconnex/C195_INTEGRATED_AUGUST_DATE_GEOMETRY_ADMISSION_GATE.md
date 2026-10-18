# C195 — Integrated Skia source-lineage, August sparse-Date and evidence-only admission gate

Date: 2026-10-18 KST. Research only. Product repository read-only. No private roster rows, personal/employee identifiers, flight/route values or source binaries reproduced.

## Authority and evidence scope

Fresh-read LogMate `AGENTS.md`, `MASTER.md`, `docs/specs/import-contract.md`, `docs/specs/crewconnex-parser-plan.md`, current SourceEvidence/SourceEvidenceHistory/Sembast code and configuration test. Fresh-read Design Studio research plan, current system/deployment/sample/field indexes, queue, research log, C113, PDF geometry, snapshot-revision fixture gate and C194 report/62-row physical locator manifest. The C194 manifest Git blob SHA-1 is `625c4e4367d12189f96cf4ee85cd1f3bae71e035`; this is a repository blob identity, not raw PDF SHA-256. This run independently recomputed **metadata/cohort results from that existing real-source-derived manifest** and cross-checked previous real-PDF aggregate audits. **No new raw private PDF or company workbook row was decoded this cycle.** No public P1 artifact acquired.

## 1. Cohort-resolved physical geometry

| Skia cohort | Numeric candidates | Activity TD6 | TD7 | TD8 | Page-2 candidates |
|---|---:|---:|---:|---:|---:|
| June curated | 18 | 7 | 2 | 9 | 2 |
| July curated | 22 | 10 | 2 | 10 | 2 |
| August curated | 3 | 1 | 0 | 2 | 0 |
| **August not in curated Preview** | **19** | **9** | **1** | **9** | **2** |
| **Total** | **62** | **27** | **5** | **30** | **6** |

The observed TD6 counts coincide with earlier **independently inspected real PDF** missing-Date totals by month: June 7, July 10, August 10. The previously unresolved C175 cohort bounds (7–10 of 19 uncurated August; 17–20 of 43 curated) are narrowed at the **geometry-signature** level to **9/19** and **18/43**. The nine August uncurated TD6 source rows are page-1 primary TR ordinals **11,14,18,20,21,22,28,30,32**. TR20–22 is a consecutive sparse-Date sequence; no automatic Date or crew inheritance is justified. Both uncurated August page-2 candidate rows (TR35, TR39) are TD8, not TD6. The one uncurated TD7 row must not be silently treated as either full-width or missing Date.

**Important evidence limit:** these are per-row TD-shape observations from C194's source-derived manifest plus earlier aggregate Date audit, **not direct new row-by-row Date-cell text validation**. TD6→missing Date remains a strong sample-specific correspondence, not a general ParserProfile rule. The count 18 also equals the manually blank dates in the curated Preview, but does not establish identical rows or explain the blanks. All 62 Skia source operational years are still explicitly `UNVERIFIED`.

## 2. Independent prior company and cross-format reconciliation

C194's **real-corpus** 2026 company comparison for the 19 uncurated August Skia rows remains: flight+route-only candidate counts **0=8, 1=4, 2=5, 3=2**. The 11 with any partial-key company candidate had **0** minute-equal Skia BLH versus company `bt` candidates and **0** exact registration-string matches. These are neither proof of non-operation nor a basis for BLH/Block equivalence or correction. The privacy-safe locator manifest does **not** contain company per-row match categories, actual Date-cell values, crew snapshots or revision identifiers. Therefore a nine-TD6 × company-candidate cross-tab, date-aware Skia/PDC pairing, and UID-owned FlightRecord cardinality **cannot be computed from this manifest**. The PDC-generator's 26 candidates are a distinct report family, not a substitute source of Skia year or crew context.

## 3. Independent validation and adversarial tests

Re-parsed the C194 CSV separately from its original producer. **11/11 source-derived manifest invariants passed**: 62 rows, unique SHA/page/TR locators, 43 unique Preview rows exactly 2–44, all years UNVERIFIED, five TDs in bounds, five distinct page-local MCIDs per row, increasing TD order, one source SHA per month, six page-2 candidates, and ten August TD6 rows. **10/10 synthetic mutated-manifest cases were rejected**: duplicate physical row, duplicate Preview row, TD overflow, same-row MCID alias, unjustified year promotion, reversed TD order, changed month source SHA, deleted row, changed TD6 geometry and dropped Preview link. These checks validate **research metadata**, not a PDF parser, source Date semantics, Dart/Flutter, Sembast or production readiness.

## 4. ParserProfile v1.04 — implementation decision delta

- **Detector:** keep Skia tagged printer PDF separate from PDC-generator. Validate immutable raw-byte fingerprint, PDF/report family, expected core headers, primary Table/TR/TD ancestry, page-local MCID ownership, per-month observed TD-shape variants, nonflight/auxiliary/Sum barriers. Reject unknown/shifted/partial layouts. TD6/7/8 are diagnostic shapes, not universal field maps.
- **Extraction:** preserve raw Activity/Date/From/To/BLH/ACReg and raw crew/position codes only where physically present; retain original labels and source SHA256+page+primary TR+TD+MCID. Distinguish absent Date from yearless present Date, unavailable crew from changed crew, and printed date from authenticated operational year. Do not forward-fill Date, Pairing or crew through adjacent rows or page boundaries.
- **Candidate matching:** keep source observation → immutable profile interpretation → reconstructed Preview value-key link → company source candidate → active authenticated UID-owned FlightRecord binding as distinct edges. Zero/multiple/unknown-year/unsupported candidates stay detached; even a unique partial key needs owner review. ±1 day is a review comparison, not a correction.
- **Revision and persistence:** no implicit publication ordering from filename/CreationDate. Store approved evidence only after owner/unlocked-state check, exact active FlightRecord RevisionId CAS, durable replay key, conflict/reinterpretation review, atomic rollback and deletion/backup/Sync coverage. SourceEvidenceHistory scalar append is not a detached crew-snapshot receipt.
- **Prohibitions:** CrewConnex cannot create a FlightRecord, overwrite canonical Block or totals, infer duty/PIC/SIC/PF/PM/deadhead, promote nonflight, infer year, or merge PDC Blk Hrs with Skia BLH.

## 5. Checkpoint and outstanding evidence

**New in this cycle:** row-level cohort geometry allocation for all 62 C194 locators, exact nine-row August sparse-Date geometry cohort, consecutive-row and page-2 risk analysis, C175 bound refinement, independent 11 positive and 10 adversarial manifest checks, and cross-validation with C194 company histogram. **Not newly verified:** direct PDF Date-cell content, Skia same-export operational year/period, crew continuation and revision authority, date-aware 19-row Skia/PDC/company joins, active UID ledger cardinality, real Dart/Sembast transactions, public P1 sample. Public evidence **P2 unchanged; Production Parser OPEN**.

Adjacent questions completed now: cohort split, geometry/date aggregate agreement, three-month page distribution, source-locator uniqueness, Preview uniqueness, sparse-Date run, prior company comparison and negative mutations. Remaining high-value semantic questions require raw-source cell/section inspection and authorized product runtime, not additional inference from the privacy-safe manifest.

**Next integrated target:** directly authenticate the nine August TD6 rows' tagged Date-cell/section/crew antecedents and Skia same-export year/period, then cross-check all 19 uncurated rows against PDC and company on verified date+flight+route, and execute authorized UID-owned Sembast CAS/replay/conflict/deletion/backup acceptance.
