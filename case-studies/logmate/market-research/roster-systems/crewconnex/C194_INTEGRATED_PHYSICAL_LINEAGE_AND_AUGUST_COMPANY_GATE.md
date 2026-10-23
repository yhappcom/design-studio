# C194 — Three-month Skia physical-field lineage and August company adjudication

Date: 2026-10-18 14:00 KST. **Research evidence only; not a production parser PASS.** LogMate remained strictly read-only. All private PDF/XLSX values were compared only in ephemeral connector memory. This document contains no crew names, employee identifiers, flight numbers, registrations, routes, private source rows or raw files.

## 1. Source and independent method

Re-read current LogMate AGENTS/MASTER/import/CrewConnex contracts and SourceEvidence/SourceEvidenceHistory/CrewParticipant/repository/Sembast tests; re-read Design Studio research plan, indexes, queue, log, C110/C112/C113, PDF geometry and revision gate. Re-fetched the existing June/July/August Skia printer PDFs, the curated Preview XLSX and the 2026 company flightHistory XLSX from the read-only LogMate reference directory. Git blob identities matched earlier C192 raw-byte SHA-256 attestations.

Independently decoded PDF Flate streams and ToUnicode glyphs; reconstructed primary Table → TR → TD → NonStruct → page-local MCID ownership. Parsed Preview sheet 4 and company workbook ZIP/XML and shared strings. Flight-candidate extraction used the observed numeric Activity, two airport cells, ACReg and minute-parseable BLH structure. Approved 7C suffix normalization was used only for comparison. No date/crew inheritance, role inference or operational-date correction was applied.

## 2. Actual three-month source-to-Preview physical lineage

| Month | Primary body TR | Numeric candidates with five physical field locators | Unique curated Preview value-key links | Outside curated Preview |
| --- | ---: | ---: | ---: | ---: |
| June | 40 | 18 | 18 | 0 |
| July | 44 | 22 | 22 | 0 |
| August | 42 | 22 | 3 | 19 |
| **Total** | **126** | **62** | **43** | **19** |

All 62 candidate rows have nonempty **Activity, From, To, BLH, ACReg** TD and page-local MCID locators. The five selected fields have one MCID leaf each, no within-row MCID alias and in-bounds TD ordinals. Source decoding yielded **5,617 Tj operations** (1,824/1,921/1,872), zero unmapped glyphs. The per-month full five-field comparison of normalized flight suffix, route, registration and minute BLH matched **43/43 Preview sheet-4 rows uniquely** (18/22/3). Comparison of the same first four fields was also unique for these 43; this is bounded to the current curated cohort, not a universal key guarantee. The Preview workbook does not natively record PDF physical locators; these associations were **independently reconstructed by matching source values** and are not PDF-issued provenance receipts.

The privacy-safe **62-row manifest** `C194_THREE_MONTH_FIELD_LOCATOR_MANIFEST.csv` was actually committed and read back: Git commit `1b9b3bad0e35d7e1204dfea62fd91be5377d51b5`, manifest blob `625c4e4367d12189f96cf4ee85cd1f3bae71e035`. It records source raw SHA-256, Git blob SHA-1, physical page, primary TR ordinal, selected TD/MCID locators, Preview sheet-row ordinal when linked, and explicit `UNVERIFIED` operational-year state; it contains no source flight/crew values. Independent read-back checked 62 unique physical rows, 43 unique Preview sheet rows 2–44, 19 uncurated, all five field locators in bounds and zero year promotions. Four additional adversarial integrity checks rejected duplicate physical locator, duplicate Preview row, out-of-bounds TD and year-promotion assumptions. These checks validate the research manifest, **not** a Dart parser.

Page distribution: curated June 16/2 (pages 1/2), curated July 20/2, curated August 3/0, uncurated August **17/2**. The 19 are outside this manually curated Preview, **not** proven unoperated, invalid, or unmatched to an owner FlightRecord.

## 3. Independent 2026 company cross-check: August's 19 uncurated rows

Company 2026 workbook contains 159 data rows. Comparing **all 22 August Skia numeric candidates** against company 2026 flight+route keys (no source-year assumption) yields:

| Skia August cohort | Company candidates = 0 | = 1 | = 2 | = 3 |
| --- | ---: | ---: | ---: | ---: |
| Three curated Preview-linked rows | 0 | 0 | 1 | 2 |
| **19 uncurated source rows** | **8** | **4** | **5** | **2** |

Among the 11 uncurated rows with at least one flight+route-only company candidate, **zero** have any candidate with minute-equal source BLH versus company `bt`, and **zero** have any candidate with an exactly equal registration string. The eight zero-candidate rows likewise have no such comparison. By contrast, each of the three curated August rows has exactly one minute-equal `bt` candidate. These are cross-source comparisons without authenticated Skia operational year; **do not conclude that the 19 were not operated, that company data are erroneous, or that BLH and Block are equivalent**. Date, revision and source coverage remain unresolved.

All 22 August source candidates' first-cell text-format audit found 12 printed weekday/day/month dates and 10 omitted Date values; the specific split within the 19 uncurated subset still needs source-row-level confirmation. No date was forward-filled.

## 4. ParserProfile v1.03 research delta and failure modes

1. Separate immutable Skia and PDC-generator report-family detectors; require source byte fingerprint, validated header/table ancestry, page-scoped MCID ownership, field geometry and nonflight/auxiliary/Sum exclusion. Numeric/route/registration/BLH selection here is a research classifier, **not** a production-approved detector.
2. Use physical `sourceSHA256 + page + primary TR + TD + MCID` as observation provenance; keep source field value, normalized comparison value and owner-approved binding distinct. Do not confuse Git blob SHA-1 with raw-byte SHA-256.
3. Normalize approved 7C flight suffix and BLH to minutes **for candidate comparison only**; retain raw source labels/values and original formatting. Preserve missing Date, yearless Date, unknown revision, raw crew codes and nonflight barriers without inference.
4. The Preview value-key association, company source comparison and authenticated active UID-owned FlightRecord are **three distinct edges**. No transitive automatic full-date or owner-Flight binding, even for 43/43 unique value-key links.
5. CrewConnex remains **existing-record-only** detached crew snapshot/BLH evidence. No standalone FlightRecord creation, canonical Block overwrite, PIC/SIC/PF/PM/duty inference or date correction. Future evidence-only persistence requires owner UID/unlocked state, active Flight RevisionId CAS, receipt idempotence, conflict review, atomic rollback, deletion/backup and explicit Sync handling.

## 5. Evidence grade, remaining blockers and synchronization

**Actual evidence:** real PDF glyph/table/cell decoding, 62 physical field locators, 43 unique curated value-key-to-locator links, 19 uncurated source rows, and August 19-versus-company partial-key/BLH/registration cross-check. **Synthetic/integrity evidence:** research-manifest invariants and mutated-key negative checks only. No real Dart/Sembast evidence-only API or Flutter parser was executed. Public sample grade remains **P2** (private corpus does not become public P1); **Production Parser OPEN**.

The manifest creation succeeded. Fresh-fetch attempts to update `crewconnex/C112_SOURCE_ADMISSION_GATE.md`, `crewconnex/PDF_PRINT_GEOMETRY.md`, `RESEARCH_LOG.md`, `FIELD_COVERAGE_MATRIX.csv`, `PARSER_SAMPLE_INDEX.csv`, `MASTER_SYSTEM_INDEX.csv` and `REVALIDATION_QUEUE.md` were each blocked with `This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.` No change to these existing files is claimed. Earlier C158–C193 unsynchronized findings remain distinct from the saved C194 manifest/report. `MASTER_AIRLINE_DEPLOYMENTS.csv` requires no change; no deployment evidence was added. The queue's obsolete 19-operator migration item should be marked closed: current deployment index has 20 rows, of which 19 have pilot planning bands.

**Adjacent CrewConnex questions completed in this run:** full 3-month tagged field extraction; 43 per-entry Preview-to-physical value-key lineage; per-page distribution and field-MCID uniqueness; company 2026 partial-key cardinality for the 19 previously uncurated August rows; minute-BLH and registration comparison; manifest read-back and adversarial integrity checks. Further advancement requires independent same-export Skia year/period, per-row omitted-Date/crew antecedent and revision authority, then actual UID-owned Sembast evidence-only acceptance.

**One next integrated high-value target:** authenticate Skia same-export operational year/period and resolve the 19 August uncurated rows' Date/crew/section/revision against PDC and company dates, then run actual evidence-only owner-UID Sembast CAS/replay/deletion/backup tests in an authorized execution environment without modifying LogMate from this research workspace.

## 2026-10-24 C324 source-row confirmation of August Date/crew shapes

The earlier statement that the 19-row Date split still required source-row confirmation is superseded **for physical own-Date presence only**. Independent re-decode of the same private August PDF and direct Table→TR→TD→NonStruct→MCID inspection matched **22/22** C194 candidate Activity MCIDs and **22/22** TD counts. The 19 non-Preview candidates are **10 own-Date / 9 omitted-Date**; the three curated candidates are **2/1**. All nine non-Preview omitted-Date candidates have five literal pipe-only TD cells. The single omitted-Date non-pipe exception is Preview-linked in this 22-row candidate cohort. Full-month printed weekday/day labels are 31/31 calendar-consistent with 2026; not 31 independently validated flight dates. Source-century, date/crew antecedent, roster publication, company extraction coverage and owner UID matches remain unresolved. No new date-aware company or UID joins, and no private source values were persisted. Detailed C324 method and safe-failure contract: [C110](C110_INTEGRATED_YEAR_AND_MATCH_GATE.md#c324--independent-full-month-weekday-and-august-physical-row-admission-audit-2026-10-24-kst).
