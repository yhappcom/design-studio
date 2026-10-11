# C31 — CrewConnex three-month tagged-cell cardinality gate

Date: 2026-10-11. Evidence: read-only structural inspection of existing June/July/August 2026 Skia PDF references. No source text or personal data retained.

| Month | Header TD | Body TR | Body TR shorter than header | Body TD distribution | Page-1/2 body TR | First page-2 TD/MCID |
|---|---:|---:|---:|---|---|---|
| June | 34 | 40 | 31 | 31:1, 32:26, 33:4, 34:9 | 34/6 | 32/78 |
| July | 30 | 44 | 34 | 25:1, 26:1, 27:10, 28:19, 29:3, 30:10 | 38/6 | 30/50 |
| August | 31 | 42 | 31 | 27:3, 28:4, 29:20, 30:4, 31:11 | 33/9 | 31/50 |

Across 126 body TR, 96 have fewer TD than the header. Across three primary tables, 3,870 TD parent links and 4,632 page-local MCID leaves had zero detected parent/page/duplicate-MCID violations; no TR spans pages. Each primary table has a direct non-TR page-break MCR child.

These are tag-structure results, not proof of Date/Activity/BLH or crew semantics. ParserProfile must map columns by validated header and geometry, preserve page/TR/TD/MCID provenance, reject ambiguous rows and non-flight activities, and never create FlightRecords. Public sample grade P2; production parser OPEN.

Next: June/July Date/Activity/BLH and Emp.#/CC/Pos. ownership on shortened and page-edge rows. Canonical index/log synchronization is pending due to GitHub write safety rejection.


## Synchronization debt

2026-10-11 18:56 KST: attempted updates to `crewconnex/PDF_PRINT_GEOMETRY.md`, `MASTER_SYSTEM_INDEX.csv`, `PARSER_SAMPLE_INDEX.csv`, `FIELD_COVERAGE_MATRIX.csv`, `REVALIDATION_QUEUE.md`, and `RESEARCH_LOG.md` under the canonical roster-systems root. Each returned exactly: `This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.` No update was committed to those six files. Re-fetch each file and retry on the next cycle; prior C25–C30 debt remains separately open. `MASTER_AIRLINE_DEPLOYMENTS.csv` was unchanged because no airline-deployment evidence was added.
