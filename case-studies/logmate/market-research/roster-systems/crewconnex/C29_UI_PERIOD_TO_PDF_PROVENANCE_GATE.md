# C29 — UI period year versus saved printer-PDF provenance

Date: 2026-10-11 17:03 KST. Read-only internal reference audit; **not** a production parser validation.

## Newly inspected source observations

- `yhappcom/logmate/reference/ui/external-apps/crewconnex-app/IMG_1908.PNG` and `IMG_1909.PNG`: same CrewConnex **Roster** view with explicit period `1. Aug 2026 - 30. Sep 2026`. Horizontal scroll reveals separate `Start(L)`, `Finish(L)`, `Start(B)`, `Finish(B)`, and `BH` headers. These are UI source labels, not automatically equivalent to printer-PDF `STD/STA(L/B)`, `BLH` or PDC-generator `Blk Hrs`.
- `IMG_1918.PNG`: **Calendar Integration** offers `WebCal Link`, `WebCals Link` and `Https Link`. This confirms link-type UI affordances, **not** an acquired ICS file, public raw sample, authenticated API access, or a supported LogMate import format.
- Fresh read-only byte audit of 2026-06/07/08 Skia printer PDFs and separate August PDC-generator PDF: their PDF Info `/Title` values do not contain a four-digit year. This does **not** prove absence of a printed page-header year. Existing C28 decoded page-1 text found no validated operational-year anchor and noted a post-`Sum` year token in July/August.

## Source-binding decision gate (OPEN)

A year explicitly shown on a CrewConnex UI roster is **not** an independently verified operational-year authority for an arbitrary saved PDF. Require a demonstrable same-export/source-document link and validated PDF period/header or export provenance before attaching that year to yearless PDF rows. Do not use screenshot capture time, filename, PDF CreationDate, nearby company records, post-Sum `Issued` text, or matching flight/route as year authority. Preserve raw source label, page/row, generator/profile and fingerprint. Unknown-year candidates remain detached review; no FlightRecord creation, auto-attachment, BLH overwrite, date correction, crew-code interpretation, or revision-order inference.

Public corpus grade **P2** unchanged. Production parser **OPEN**. No private source rows, crew identifiers, screenshots or binaries copied to Design Studio.

## Index synchronization debt

`RESEARCH_LOG.md` was saved and read back (commit `cad556a9a79c052cacd6c64762968626e386fe1a`). Fresh-fetched writes to these paths failed, leaving them unchanged:

- `MASTER_SYSTEM_INDEX.csv`
- `PARSER_SAMPLE_INDEX.csv`
- `FIELD_COVERAGE_MATRIX.csv`
- `REVALIDATION_QUEUE.md`
- `crewconnex/PDF_PRINT_GEOMETRY.md`

For all five: `This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.` A follow-up `RESEARCH_LOG.md` error-annotation update was blocked with the same error. `MASTER_AIRLINE_DEPLOYMENTS.csv` not applicable. Retry after fresh fetch; do not disable research.

**Next single target:** find a lawful, source-bound same-export Skia PDF header or UI export workflow identifier tying an explicit roster period year to the exact PDF. If absent, finalize unknown-year review-only profile behavior.
