# CrewConnex evidence, decisions and contradiction register — 2026-11-07

**Authority:** EVIDENCE NAVIGATION ONLY. This register distinguishes source data, research tests, interpretations, user-approved LogMate contracts and unclosed implementation gates; it cannot approve product behavior. No private flight/crew data or identifiers are copied here. Main overviews: [research synthesis](RESEARCH_SYNTHESIS_20261107.md), [profile](PARSER_PROFILE_SPEC_20261107.md), [readiness](IMPLEMENTATION_READINESS_20261107.md).

## 1. Controlled confidence vocabulary

- **P/Market grade:** Use the research-plan's P1–P5 **per format and per sample**, A1/A2/B/R per airline-system deployment; not a probability and not a product PASS.
- **REAL ORIGINAL:** an authorized private source file was fetched/decoded/verified for a bounded claim; does NOT confer public P1 or authenticated Flight identity.
- **REAL-DERIVED MANIFEST:** reproducible metadata extracted earlier from private originals, with no new source decode in the current check.
- **SYNTHETIC:** transformed/generated fixtures or source-shaped tests; counts do not establish independent real samples.
- **STATIC SOURCE REVIEW:** code function, contract or schema inspected; its presence != runtime PASS.
- **PRODUCT CONTRACT:** LogMate MASTER/spec-owned rule (not proposed or newly approved by Design Studio).
- **OPEN / SUPERSEDED / DEBT:** needs acceptance / fact corrected by newer evidence / document or index not yet synchronized.

## 2. Key claim registry

| ID | Asserted result and exact scope | Grade | Primary record | Decision implication |
|---|---|---|---|---|
| E01 | Skia Jun/Jul/Aug original 40/44/42 primary body TR, 18/22/22 numeric-shaped rows (62 total), 310 physical field locators | REAL ORIGINAL (C194) | [C194](crewconnex/C194_INTEGRATED_PHYSICAL_LINEAGE_AND_AUGUST_COMPANY_GATE.md), [manifest](crewconnex/C194_THREE_MONTH_FIELD_LOCATOR_MANIFEST.csv) | Structure/extraction feasibility; no standalone Flight |
| E02 | 43/43 manually curated Preview rows uniquely connected to PDF physical five-field locations (18/22/3); remaining 19 Aug rows outside Preview | REAL ORIGINAL + curated-manual comparison | C194 | Not 43/43 production Import or source-issued PDF receipt |
| E03 | Curated 43 company join/Actual-Block-Night-Instrument minute equality; 37 same roster date / 6 +1 day | REAL-CORPUS BOUNDED COMPARISON | [C110](crewconnex/C110_INTEGRATED_YEAR_AND_MATCH_GATE.md), [system index](MASTER_SYSTEM_INDEX.csv) | No date auto-correction, no universal BLH/Block equivalence |
| E04 | All 2018–2026 nine company XLSX contain 1530 total rows (1520 7C supported, ten not); 2026=159 rows, last observed Aug date Aug 02 | REAL ORIGINAL / verified decode with coverage constraint | [C113](crewconnex/C113_COMPANY_CORPUS_INTEGRATED_GATE.md), C194/C325 in C194 | No valid "missing flight" verdict for post-Aug02 uncurated roster |
| E05 | August 19 non-Preview partial company flight+route multiplicity 0=8/1=4/2=5/3=2, 0 minute-equal BLH-vs-bt and 0 exact ACReg among 11 with candidates | REAL ORIGINAL, PARTIAL-KEY ONLY | C194, [C195](crewconnex/C195_INTEGRATED_AUGUST_DATE_GEOMETRY_ADMISSION_GATE.md) | This is neither authenticated full-date nor same-owner Flight join |
| E06 | Skia own-Date 35/62, absent 27/62; own-Pairing 30/62, absent 32/62; 26 single-leaf, 31 six-leaf, five seven-leaf | REAL-DERIVED / original cell audits | C194, [C457](crewconnex/C457_PRIVACY_SAFE_ASSOCIATION_ACCEPTANCE_FIXTURE.json), [C233](crewconnex/C233_INTEGRATED_PROFILE_AND_SOURCE_ONLY_EVIDENCE_GATE.md) | No crew count, same-duty, name or date inheritance |
| E07 | Among 26 single-leaf rows, physical anchor distance 1:22, 2:2, 3:2; all recorded within same selected page/source | REAL-DERIVED MANIFEST recheck C547 | C233; [research log](RESEARCH_LOG.md) | Four nonadjacent cases defeat naïve previous-row copy |
| E08 | Six selected Skia page-2 candidates: 5 own Date and 1 omitted; no source manifest page-crossing physical crew-anchor | REAL-DERIVED MANIFEST recheck C548 | C233 | Absence of observed cross-page anchor is not cross-page continuation certification |
| E09 | PDC-generator unchanged August original 39,612 bytes/495 text objects/48 Activity/26 numeric/22 nonflight/31 own-Date cells and 31 groups | REAL ORIGINAL C530/C502/C546 | [PDC research profile](crewconnex/PDC_GENERATOR_PROFILE_RESEARCH_V1.json), C233 | Verified one report subtype only |
| E10 | PDC Local/Base raw endpoints 52/52 fit observed station-offset relative UTC+09 interpretation | REAL SOURCE-SPECIFIC CROSS-CHECK | [field matrix](FIELD_COVERAGE_MATRIX.csv), C194/C233 | Base/IANA/DST and auto operational date unverified |
| E11 | C532 actual PDC original inspectPdcPdfStrict -> OBSERVED_FAMILY_DETACHED_HOLD and **55/55 original-dependent adversarial checks** | REAL ORIGINAL + ORIGINAL-DERIVED TESTS; JS research oracle | [queue](REVALIDATION_QUEUE.md), [log](RESEARCH_LOG.md), [C426 script](crewconnex/C426_PDC_NATIVE_PDF_TEXT_ADMISSION.mjs) | Already executed; do not schedule as first test again; not Dart/parser production |
| E12 | C533 **21/21 synthetically generated** date-group relocations rejected in strict research gate | SYNTHETIC | Queue/log; C426 | Distinct from exact C512 21 original-derived mutated PDF replays |
| E13 | C512 **21 source-native coordinate PDF mutations**, independently rejected by position oracle; strict C426 + independent PDF renderer replay **not yet evidenced** | REAL ORIGINAL-DERIVED / different oracle | PDC research profile C512 and queue | This exact integration test remains OPEN |
| E14 | Actual named crew mapping absent; Emp.# is transient lineup only, CrewParticipant requires name | REAL SOURCE + STATIC CODE + PRODUCT CONTRACT | C233; LogMate MASTER/crew_participant.dart | No staff-ID persistent evidence or inferred names |
| E15 | SourceEvidence represents canonical scalar field; SourceEvidenceHistory notice compares normalized scalar, not entire crew snapshot/provenance | STATIC CODE | LogMate source_evidence.dart, source_evidence_history.dart, C233 | No BLH alias to canonical Block; new source-only revision stream needed |
| E16 | Existing record-only CrewConnex; no silent canonical writes; external Import review != Manual Sync LWW | PRODUCT CONTRACT | LogMate MASTER, import-contract and crewconnex-parser-plan | Absolute boundary for research spec and tests |

The E11 test count is **not 55 independent private exports**. E02 43/43 and E03 43/43 are related curated-cohort checks, not independent universal sensitivity measurements. E06 leaf counts do not identify staff.

## 3. Explicit contradictions and supersession

| Register | Earlier statement | Current adjudication | Status |
|---|---|---|---|
| X01 | C499 claimed 30 printed Date anchors and a leading undated first two Activity rows | C502 independently re-decoded **31** printed Date cells, first Activity own Date present; C546 matched **31/31** original group shapes with current pinned C426 topology | **SUPERSEDED**; retain C499 as historical erroneous evidence, no automatic day inheritance |
| X02 | Some follow-up reports said original PDC strict admission had never run | C532 already ran unchanged original strict path + 55/55 original-dependent checks; C546 was separate 31-group geometry check | **CLOSED** execution-status correction |
| X03 | C533 "21 mutations" was conflated with C512 21 original-derived PDFs | C533 generated synthetic 21; C512 21 original-derived under an independent position oracle; exact C512 strict-C426+renderer replay not run | **OPEN** distinct acceptance task |
| X04 | 26/32/4 single/six/seven leaf distribution stated in C539 | C540 independently corrected to **26/31/5** on the 62-row C194 manifest; C547 anchor distances rechecked | **SUPERSEDED** prior shape count |
| X05 | C200/C339 legacy 2025 XLSX missing-cell inference | C341 direct workbook OOXML found P/Q/R/S cell nodes physically present across 1530 rows with 12 PRESENT_EMPTY states across 8 records; no physically absent cells of that class | **SUPERSEDED** missing-node inference; do not equate empty with zero |
| X06 | "20 CrewConnex airlines" incorrectly interpreted as the whole tracked cohort, or earlier 19 migration task | Current deployment CSV **21 tracked**: 5 A1 + 15 A2 + 1 B; system index **20 A1/A2 confirmed**, 19 planning-band rows | **RESOLVED** denominator; no count CSV edit needed |
| X07 | CrewConnex "public P2" generic statement in some C194/C233 notes | System index highest **P3**; weekly HTML instructions P3; PDC PDF/export sample row P5; UI manual/screenshots P4; any format-specific P2 claim needs exact qualifying official export-schema evidence | **OPEN GRADE RECONCILIATION**, no silent index upgrade or private-to-public P1 |
| X08 | C194 August 19 zero/equal mismatch interpreted as 19 unoperated/unmatched flights | 10 own-Date cases print Aug03–31 but company currently observed only through Aug02; 9 lack own Date; four-digit Skia year/UID/Publication absent | **INVALID INTERPRETATION**; HOLD rather than fail unmatched |
| X09 | An earlier C457 fixture 404 was interpreted as absent | Current repository directory and direct fetch both confirm [C457 JSON](crewconnex/C457_PRIVACY_SAFE_ASSOCIATION_ACCEPTANCE_FIXTURE.json) exists | **RESOLVED PATH/ACCESS**, not runtime test |
| X10 | Later ZIP header inspection described first company XLSX XML decode still needed | C194 had already decoded private company workbook ZIP/XML/shared strings; C544 later 9/9 limited ZIP admission did **not** independently execute CRC/decompression | **RESOLVED DISTINCT SCOPE**; neither implies full independent CRC PASS |

## 4. Current open decisions / evidence source to acquire

| Key | Decision required | Exact acceptable closing evidence | Current |
|---|---|---|---|
| O01 | Skia four-digit operational year and subject-to-Firebase UID proof | Same-export source header/period and owner-authenticated identity; historical file names and PDFs' CreationDate insufficient | OPEN |
| O02 | Publication/revision identity and same-value crew snapshot change | Verified publication token or formally reviewed unknown-publication immutable fingerprint policy and re-import notice | OPEN |
| O03 | 19 uncurated August exact company+Flight association | Actual Aug03–31 company coverage or explicit coverage HOLD, authenticated source year, full key, unique active same UID Flight | OPEN |
| O04 | Verified crew names, privacy-safe identity | Independent eligible name mapping and policy; never persist Emp.# or hashes | OPEN |
| O05 | Independent standards PDF parser/render cross-check | C512 exact 21 originals-derived PDF mutations through C426 plus renderer and 3-month Skia page/Sum independent checks | OPEN |
| O06 | Product evidence-only persistence | Actual source-only schema + revision double-CAS, receipt, atomic rollback/retry, zero canonical writes, deletion/backup/UID restore in native Sembast | OPEN |
| O07 | Public raw CrewConnex sample/version/airline portability | Lawfully anonymized actual matching PDF/TSV sample, independent parser validation, exact format grade | OPEN |
| O08 | C194 historical CSV/index update debt | Reconstruct exact substantive unsynced delta from named evidence; fresh fetch, compare, apply only non-no-op changes | DEBT |

## 5. Index reconciliation policy

- [MASTER_SYSTEM_INDEX.csv](MASTER_SYSTEM_INDEX.csv): CrewConnex 20 is A1+A2 and 3,034–4,303 pilot **planning** band for 19 rows; do not change to 21 without explicit field-semantic change. Best P3 concerns public third-party format guidance, not the actual PDF.
- [MASTER_AIRLINE_DEPLOYMENTS.csv](MASTER_AIRLINE_DEPLOYMENTS.csv): 21 current tracked, B unconfirmed in A1/A2 tally, no new airline verified by this consolidation.
- [PARSER_SAMPLE_INDEX.csv](PARSER_SAMPLE_INDEX.csv): source per format, especially private vs public; no P1 CrewConnex raw sample verified.
- [FIELD_COVERAGE_MATRIX.csv](FIELD_COVERAGE_MATRIX.csv): field observable does not equal mapped-to-canonical; BLH, raw crew IDs/codes and year are explicitly limited.
- [REVALIDATION_QUEUE.md](REVALIDATION_QUEUE.md): next run should use O01–O08 and C512/C532/C533 distinction. Avoid repeated ZIP/date/Date-group arithmetic.

**C194 synchronization debt** remains historical. Some blocked writes may have been superseded by later research, and the exact safe payload is not fully reconstructable from the current summary. Do not fabricate missing diffs or force a no-op write. Preserve debt and refresh before an actual material update.

## RELATED DOMAIN CHECK

Reviewed Design Studio AGENTS, global/specialist statuses and research index. Type/Color are not material to corpus confidence; Interaction/Web/Content can transfer the state taxonomy into review flow, offline unsupported-profile behavior and user-facing uncertain-vs-failed source terminology.

## HANDOFFS TO OTHER SPECIALISTS

Engineering: use O01–O06 as acceptance gate IDs, not C-number document count. Interaction and Content: failure, source-uncertain, match-ambiguous, changed revision and explicit approval must remain distinct user-visible semantics. Web/PWA: document upload-free on-device parsing, parser-version mismatch and offline update limitations. Marketing: never market CrewConnex, any system or airline as shipped/verified parser solely from this research evidence.
