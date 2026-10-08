# CrewConnex printer-PDF geometry — 2026-10-08

Research metadata only. Three existing internal printer PDFs (June, July, August 2026) share a Skia/PDF m151 generator, two portrait pages, compressed text streams and ToUnicode CMaps. Page 2 starts around document-space y=1682–1684 and repeats the first page's x-column grid. This supports vertical continuation of one print table, not a new independent roster. Exact header and row semantics remain unverified.

Parser implication: retain physical page/row source locator, validate antecedent before page continuation, and reject unsupported section/geometry. CrewConnex creates zero FlightRecords. Internal source is not a public P1 sample; public grade remains P2. Do not infer BLK=BLH or crew duty-code meaning.

Next: synthetic two-page continuation fixture with no repeated header, page-2 summary boundary and unsupported-grid negative test.

## 2026-10-08 10:00 KST — synthetic continuation regression checkpoint

Four wholly synthetic, two-page text-layer PDF fixtures were generated and checked: no-header page-2 continuation, page-2 period-total barrier, shifted column grid, and orphan continuation. Expected detached observations: 2, 2, 0, 0 respectively; no FlightRecords or record-bound SourceEvidence before matching. The summary barrier makes the following blank-date leg review-only; the shifted grid is document-level unsupported layout. These ReportLab fixtures are NOT Skia artifacts and do NOT validate the real CrewConnex detector. Page-2 actual header/reading order remains OPEN. GitHub writes of detailed JSON/Markdown fixture oracles were blocked by connector safety checks; retry fresh-fetch next run.

## Real Skia comparison — 2026-10-08 10:56 KST

The June/July/August printer PDFs have first-page header bands but no repeated header on page 2. July and August page 2 contain a `Sum` section; June page 2 does not. The `From` header X coordinate is 363.05/357.02/357.02 across the three months. Header geometry therefore varies, and exact ToUnicode label decoding still requires independent validation. This is structural evidence, not a production parser PASS.

## 2026-10-08 20:03 KST — producer and export-time fingerprint

Read-only PDF metadata audit (no crew or flight-row content):

| 2026 artifact | Producer | PDF CreationDate | Pages | StructTreeRoot / MCID | ToUnicode refs |
|---|---|---|---:|---|---:|
| June printer PDF | Skia/PDF m151 | 2026-08-27 22:50:08 UTC | 2 | yes / yes | 16 |
| July printer PDF | Skia/PDF m151 | 2026-08-27 22:48:59 UTC | 2 | yes / yes | 17 |
| August printer PDF | Skia/PDF m151 | 2026-08-09 04:48:38 UTC | 2 | yes / yes | 17 |
| Separate August PDF | PDC Pdf Generator 1.0 | 2026-09-28 15:49:07 (timezone unspecified) | 1 | no / no | 0 |

Skia page MediaBox: about 594.96 x 841.92; separate PDC generator page: 598 x 842. PDC generator Creator is PDC Crew. Absence of ToUnicode references does not establish image-only content. CreationDate is generation metadata, **not** roster effective date, source revision ID, or operational date. Month order is not PDF-generation order. The two August outputs must remain separate fail-closed ParserProfile candidates until their headers/field semantics are independently verified. BLK is not automatically BLH. The June page-2 Sum-absence claim in the older section above is superseded by the independently verified presence of Sum in all three Skia printer PDFs.

## 2026-10-09 00:55 KST — same-August dual-generator geometry-key comparison

Read-only in-memory text-layer decoding of the two distinct August references (Skia printer PDF and PDC Pdf Generator PDF), with no raw rows, identifiers or crew data exported. Geometry-filtered numeric Activity candidates: Skia 22 rows / 20 distinct flight+route keys; PDC 26 rows / 26 distinct keys. Exact raw flight+From+To intersection: 16 distinct keys; 14 occur once in each output, while 2 are repeated in Skia, producing 18 unfiltered candidate pairs. The raw time strings in the Skia BLH and PDC Blk Hrs positions agree in 8 of these 18 *unfiltered* pairs and differ in 10. These are not date/revision-verified same-leg pairs, so the 8/18 ratio is NOT an agreement rate or proof that BLH and Blk Hrs have identical semantics. The two PDFs have different generation paths/timestamps. Numeric Activity filtering is a limited geometry diagnostic, not a complete production detector.

Cross-format source locator must retain generator/profile, file fingerprint, physical page and row, raw date and activity, route, and time label. Do not auto-merge the two exports, forward-fill dates across non-flight barriers, correct operational dates, or create FlightRecords. Next: date-aware pairing of the 14 unique-key candidates and resolution of the 2 repeated-key cases; check BLH/Blk Hrs only after exact source-date/leg/revision alignment.

## 2026-10-09 04:00 KST — cross-format antecedent validation

Eight both-undated August flight+route candidate comparisons were examined independently across Skia and PDC PDF text layers. Seven have reachable dated flight antecedents in each format; one encounters a non-flight barrier in both. Of seven antecedent candidates, six agree on month/day and one disagrees. Two comparisons involve a repeated Skia key. The source date formats differ: weekday/day/month versus day/month/two-digit year. Raw BLH/Blk Hrs strings agree in two of eight unfiltered pairs; no field equivalence or same-leg identity is established. All cases remain review-only; the barrier must block date inheritance. No source rows or identifying crew data were retained. Public P2 and production OPEN remain unchanged.
