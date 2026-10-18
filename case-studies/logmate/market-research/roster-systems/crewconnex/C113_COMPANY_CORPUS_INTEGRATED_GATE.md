# C113 — CrewConnex paired-corpus and admission decision checkpoint

Date: 2026-10-15 KST. Research only. LogMate was read-only. No personal source rows, crew identifiers, raw rosters or binaries are included.

## New real-source verification

All nine distinct 2018–2026 company flightHistory workbooks were independently decoded from ZIP/XML and shared strings. Data rows by year: 58, 318, 88, 172, 158, 184, 176, 217, 159; total **1,530**. All 1,530 operational date cells use eight-digit YYYYMMDD, are calendar-valid, and have the corresponding workbook year. They are **not Excel date serials**. Every company Block cell is nonblank HH:mm. Company-only full date + approved 7C-normalized flight + route has zero duplicate groups; this is not proof of a unique personal FlightRecord.

Ten flight identifiers are outside the approved 7C numeric-only normalization rule. Source-specific mapping must fail closed rather than silently convert other identifiers.

Across the nine workbooks, 1,036 Night cells explicitly contain 00:00. OOXML cell-aware revalidation (C181/C182) shows twelve **present-but-empty** operational cells, not physically absent cells: `ntTme` 2 (2025), `toCnt` 5 (2025), `ldCnt` 5 (2024: 1; 2025: 4). Recognized takeoff indicators: 443 Y and 1,082 dash; recognized landing indicators: 440 Y and 1,085 dash. These are raw indicators, not numeric counts. Present-empty is not zero, Day, a dash, or an absent XML cell. Preserve cell locator and value-state separately.

The four distinct 2026 CrewConnex PDFs were independently admitted as complete PDF 1.4 byte payloads. Three Skia outputs have 131/137/138 FlateDecode references and 16/17/17 ToUnicode references; the separate PDC-generator PDF has neither. Boundary-aware uncompressed PDF-name scans found zero Encrypt, EmbeddedFiles, JavaScript, OpenAction, AcroForm, XFA, Launch or RichMedia tokens. Naive /AA substring scanning falsely matches Skia font names; exact /AA token scanning finds zero. This is not a comprehensive malicious-PDF clearance.

Earlier real-source results remain: 62 numeric Skia candidates across three months; 43 of 43 manually curated entries uniquely linked to source flight, route, registration and minute-BLH geometry, including 18 omitted-date rows; two independent explicit-date PDC/company matches and one unverified date-inheritance hypothesis. No same-export Skia year, crew identity, publication order or actual owner-ledger match has been established.

## Integrated implementation contract — research ParserProfile v0.36

Use immutable, separately detected Skia printer and PDC-generator PDF profiles. Validate payload, PDF syntax, report-family anchors, header/grid, primary table, page/section/summary barrier and source locators. Use a separate company XLSX profile with explicit YYYYMMDD parsing and lossless missing/zero/indicator states. Reject unsupported carriers, ambiguous source rows, unknown layouts, nonflight activities and unverified date/crew inheritance. Preserve raw BLH/Blk Hrs and clocks; do not equate them with canonical Block.

Maintain independent source-row, company-record and verified UID-owned FlightRecord cardinalities. CrewConnex remains existing-record-only snapshot/BLH evidence. Any future evidence-only commit requires explicit user choice, exact owner check, active-record revision CAS, durable replay idempotence, atomic rollback, revision conflict review and account-deletion coverage. No canonical create, silent overwrite, date correction, duty-role inference, or aggregate mutation.

## Evidence boundary and next target

The new nine-year XLSX audit and four-PDF admission scan are actual read-only corpus checks, not synthetic tests. No Flutter parser, Sembast evidence-only transaction, actual owner-ledger test or new source-bound Skia year proof was performed. Public sample grade P2 and production parser OPEN remain unchanged. Legacy 2018/2019 PDF content retrieval remains blocked despite readable Git metadata.

Next integrated target: authenticate the Skia year/period and the 18 omitted-date section/crew associations; then test actual existing-owner FlightRecord cardinality and evidence-only atomic replay/conflict/deletion.
## 2026-10-18 C181–C182 identity and PDF provenance correction (research only)

Nine distinct company workbooks have 1,530 rows. Every `order1` worksheet cell is present-empty (1,530/1,530). `rowNo` is unique within each annual workbook but has only 832 distinct values across all nine, hence cannot be a global FlightRecord/revision identity. Of 1,520 supported `7C` company rows, date-free flight+route+company `bt`+registration has nine duplicate groups (18 rows); even adding month/day leaves one two-row cross-year collision. The 2026 sample alias is the same Git blob as the 2026 workbook, not a second source. These are company-only identities, not roster-to-ledger matches.

Read-only PDF metadata revalidation on the June and July Skia files found 2 pages each, `Skia/PDF m151`, and PDF CreationDate/ModDate on 2026-08-27 UTC (June: 22:50:08, July: 22:48:59). Creation metadata dates **do not authenticate the operational year or roster revision order**. The separate August PDC-generator file has CreationDate 2026-09-28 without an explicit offset; do not treat the three creation timestamps as one publication/revision chain. No actual UID-owned Flight match, 43-entry physical Preview lineage or Dart/Sembast evidence-only PASS follows. Public P2, production OPEN. All CrewConnex data remains existing-record-only detached enrichment evidence.
