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
