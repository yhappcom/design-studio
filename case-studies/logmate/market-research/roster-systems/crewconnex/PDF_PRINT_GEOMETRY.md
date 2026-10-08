# CrewConnex printer-PDF geometry — 2026-10-08

Research metadata only. Three existing internal printer PDFs (June, July, August 2026) share a Skia/PDF m151 generator, two portrait pages, compressed text streams and ToUnicode CMaps. Page 2 starts around document-space y=1682–1684 and repeats the first page's x-column grid. This supports vertical continuation of one print table, not a new independent roster. Exact header and row semantics remain unverified.

Parser implication: retain physical page/row source locator, validate antecedent before page continuation, and reject unsupported section/geometry. CrewConnex creates zero FlightRecords. Internal source is not a public P1 sample; public grade remains P2. Do not infer BLK=BLH or crew duty-code meaning.

Next: synthetic two-page continuation fixture with no repeated header, page-2 summary boundary and unsupported-grid negative test.

## 2026-10-08 10:00 KST — synthetic continuation regression checkpoint

Four wholly synthetic, two-page text-layer PDF fixtures were generated and checked: no-header page-2 continuation, page-2 period-total barrier, shifted column grid, and orphan continuation. Expected detached observations: 2, 2, 0, 0 respectively; no FlightRecords or record-bound SourceEvidence before matching. The summary barrier makes the following blank-date leg review-only; the shifted grid is document-level unsupported layout. These ReportLab fixtures are NOT Skia artifacts and do NOT validate the real CrewConnex detector. Page-2 actual header/reading order remains OPEN. GitHub writes of detailed JSON/Markdown fixture oracles were blocked by connector safety checks; retry fresh-fetch next run.
