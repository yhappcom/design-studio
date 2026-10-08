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

## 2026-10-09 05:00 KST — PDC-generator L/B time-column non-equivalence

In-memory text-layer audit of the existing private August PDC PDF (49 body bands, 26 numeric Activity candidates): each candidate has distinct raw `STD (L)`, `STD (B)`, `STA (L)`, `STA (B)` cells. Raw STD pairs equal 21/26 and STA pairs equal 21/26. Exactly 16/26 candidates have both pairs equal; 5 differ only in STD, 5 differ only in STA, and none differ in both. Four candidates contain an explicit `+1` time-cell suffix; all four are among the ten candidates with at least one differing pair. After recognizing `+1`, all 26 pairs in both families are syntactically parseable. Nonzero modulo-day clock differences are +60 (1), -60 (3), -120 (1) minutes for each pair family; do **not** infer timezone, time basis, or operational-date correction from these offsets. The labels `(L)`/`(B)` remain uninterpreted. The 2026 company workbook separately exposes `fltDat`, `fltNo`, `stFr`, `stTo`, `bt`. Preserve four raw time fields and explicit rollover marker in detached staging; require matched-leg validation before any semantic mapping. No private flight/crew rows were stored. Public P2 / production OPEN unchanged.


## 2026-10-09 — PDC-generator Local/Base timezone hypothesis checked

Privacy-safe read-only cross-check of the existing August PDC Pdf Generator source: 26 numeric-activity flight candidates; for each, compare STD (L) minus STD (B) against departure-airport UTC offset minus UTC+09:00, and STA (L) minus STA (B) against arrival-airport offset minus UTC+09:00 (minute-of-day modulo 24h). All 52/52 endpoint checks agree; mismatches 0. Offset distribution: 42 at 0 min, six at -60 min, two at -120 min, two at +60 min. The observed airports cover Korea/Japan (+09), Philippines/Bali/China (+08), Vietnam (+07), and Saipan (+10). Four rows carry an explicit +1 suffix; preserve it independently of clock-zone conversion.

Interpretation: (L) is strongly supported as station-local civil time; (B) is strongly supported as UTC+09 base-reference time in THIS source document. This is an observed source-specific inference, not proof of a universal PDC convention or the crew member's exact home-base airport. Airline/base configuration and DST/date-aware conversion must be independently validated for any other profile. Preserve all four source clock cells and any +1 day marker, plus IANA airport-zone provenance; do not silently change canonical operational date or FlightRecord values. CrewConnex remains existing-record-only; public parser sample grade P2 and production parser OPEN.

Timezone references: https://www.timeanddate.com/time/zone/south-korea/incheon ; https://www.timeanddate.com/time/zone/indonesia/denpasar ; https://www.timeanddate.com/time/zone/usa/saipan ; https://www.timeanddate.com/time/zone/%408531735 ; https://www.timeanddate.com/time/zone/china/tsingtao ; https://www.timeanddate.com/time/zone/%401704245 . No roster rows, private names, identifiers or exact routes copied.


## 2026-10-09 06:01 KST — day-aware +1 check

The same August PDC sample has 52/52 station/base endpoint clock checks consistent after applying each source-cell +1 day marker. Four candidate rows contain +1; three mark both arrival cells, and one also marks only the base departure cell. This supports source-relative day-offset preservation, not operational-date correction. No new public P1 sample, non-UTC+09 CrewConnex base fixture or direct PDC acronym definition. Keep separate profile and DST/base-setting negative tests. Public P2; production OPEN.

## 2026-10-09 — paired August Skia/PDC/company antecedent gate

Existing Skia/PDC PDF comparison gives 18 flight+route candidate pairs, eight with both dates omitted. Independent date-aware antecedent tracing (Skia weekday/day/month without year; PDC ddMMMyy) yields six matching month/day, one differing, one blocked by non-flight rows. Within the six provisional matches, five flight+route keys are unique and one repeats in Skia; raw BLH versus Blk Hrs strings agree in two, differ in four. Company 2026 workbook has 159 records, three in August; only one of the six has an exact company date/normalized-flight/route candidate. The other five are unrepresented, not parser errors. No automatic source merge or date correction is authorized.

The Skia text-band extractor sees 42 Activity-bearing bands while the PDF has 43 tagged primary rows; production acceptance requires full tagged-row and section boundary reconciliation. Add synthetic negative fixtures for yearless vs dated token, non-flight barrier, repeated flight/route, absent company counterpart, BLH conflict and missing Activity-bearing row. Public P2; production OPEN. Only aggregate observations retained.
