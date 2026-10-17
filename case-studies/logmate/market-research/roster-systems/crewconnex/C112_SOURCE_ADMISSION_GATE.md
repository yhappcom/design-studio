# C112 — CrewConnex input admission and lineage gate

Date: 2026-10-15 KST. Research evidence only; no product implementation validation.

## Actual read-only source inspection

The existing LogMate source directory contains two distinct CrewConnex PDF layout families: Skia printer reports (June, July, August 2026 reference artifacts) and a PDC-generator report. Their binary signatures are PDF 1.4. The paired company workbook and manually curated preview are ZIP-based XLSX files. One misleadingly named `.aspx` reference is an HTML/ASP.NET sign-in form rather than a PDF or roster table; it is **not** a parser sample and must not be used for authentication or protected data retrieval. The two 2026 company workbook aliases share one Git blob identity, so they count as one source.

The previously independently decoded three-month Skia PDFs yielded 62 numeric flight candidates. The manually curated preview's 43 entries linked uniquely to PDF flight/route/registration/minute-BLH rows (June 18, July 22, August 3). Of those linked source rows, 25 display yearless dates and 18 omit dates. Without the approved 7C leading-zero normalization, eight links are missed. Four July preview rows are ambiguous on flight+route alone. This is source-row lineage, **not** verified operational year, participant identity, actual owner FlightRecord identity, or production parser accuracy.

A separate PDC-generator/company comparison has two independently row-dated full-key matches; one additional apparent overlap requires unverified date inheritance. No automatic correction or attachment is authorized.

## Versioned ParserProfile decision delta

1. Run a byte-content/MIME admission gate before extension-based dispatch. HTML forms and unsupported/mismatched content fail closed; no network login or credentials.
2. For PDF input, require independent report-family generator, header/grid, primary table, page/section and summary-barrier acceptance. Skia and PDC-generator must remain separate immutable profiles.
3. Preserve source fingerprint, raw values, field absence, page/row/cell locator, parser version and review reason. An absent source year is detached review, not a fabricated 2026 date.
4. Compare source-row, company-row and actual UID-owned ledger candidate cardinalities independently. Only explicit user-approved, exact existing-record evidence-only persistence may proceed after owner/revision/idempotency gates.
5. Reject nonflight, unknown report family, ambiguous duplicates, unverified date inheritance and participant-list mismatch without any FlightRecord creation, Block overwrite, or crew inference.

## Remaining blockers

No same-export Skia operational-year authority; 18 omitted-date row section/crew lineage unresolved; no real owner-ledger match or Flutter/Sembast evidence-only integration. Synthetic classifier checks are not production parser PASS. Public sample grade P2; production parser OPEN.

Next integrated target: independently bind Skia source year and omitted-date section/crew provenance, then test actual existing-ledger cardinality and evidence-only atomic replay/conflict/deletion.

## 2026-10-17 C171 — date-state denominator and non-transitive lineage gate

Cross-reconciled existing actual-source audits C39/C44/C45/C110/C112 and three-month tagged-table counts, not a fresh binary decode. Of 62 Skia numeric Activity candidates, **27 lack a Date TD** (June 7/18, July 10/22, August 10/22), while **35 have a Date TD** but still lack authenticated same-export four-digit operational year. The 27 missing-Date numeric candidates have 22 preceding dated-numeric rows, four preceding undated-numeric rows, and one preceding nonnumeric row; these are structural antecedent categories, NOT authorized date/crew inheritance. Seven further absent-Date TD rows are nonnumeric, giving 34/126 absent-Date body rows. The separate PDC-generator cohort has 13/26 numeric candidates with omitted own-date values: seven direct antecedent, four chained, two barrier-blocked; its year-bearing date anchors do not authenticate the Skia year. The manually curated preview's 18 omitted-Date observations belong to a different 43-entry subset and cannot be subtracted from 27/62.

**Lineage graph (distinct joins):** 43/43 curated preview entries were previously value-key associated to Skia flight/route/registration/minute-BLH observations (18/18 June, 22/22 July, 3/22 August), but a value-key association is not a per-entry source-file SHA + page/TR/TD/MCID proof of export authority. Separately, curated date + 7C-normalized flight + route joins 43/43 to company 2026 rows. These two edges are **not transitive** into 43 authenticated full-date PDF-to-company joins or 43 UID-owned FlightRecord matches. August's other 19 numeric rows are uncurated, not proven unmatched. No automatic attachment is authorized; no independent Skia operational year, revision ordering, crew continuity or owner-ledger CAS test has been established.

**ParserProfile v0.85 research delta:** preserve distinct DATE_TD_ABSENT, DATE_TD_PRESENT_YEARLESS, DATE_VALUE_EMPTY, YEAR_UNVERIFIED, NONFLIGHT_BARRIER, and SOURCE_AUTHORITY_UNVERIFIED states. Date adjacency is evidence for review only. Maintain separate source-row, curated-reference, company-row and owner-Flight cardinalities; require exact file fingerprint + physical locator + user approval + owner UID/revision CAS for new evidence-only binding. The same family-specific fail-closed policy applies to PDC, without importing its year/clock/Pairing semantics into Skia. Standalone privacy-safe aggregate oracle C171 verified linked invariants and rejected three corrupted antecedent aggregates; not actual parser or Sembast tests. Official PDC page currently confirms PDF reporting, Day Schedule and Master Schedule exports, not an immutable CrewConnex printer PDF field schema. Public P2 is capability-scoped; production OPEN.
