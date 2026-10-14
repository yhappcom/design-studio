# C110 — CrewConnex source-bound year and company matching gate

Date: 2026-10-15 KST. RESEARCH ONLY; no production parser or Flutter acceptance. LogMate is read-only. This note contains aggregate evidence and no raw private roster, employee identifiers, personal flight keys, or crew names.

## Actual private corpus verification

Read-only binary retrieval using base64 of three Skia printer PDFs succeeded. Their 406 compressed streams were independently inflated (June 131, July 137, August 138), and their embedded ToUnicode maps decoded all 5,617 text objects (June 1,824; July 1,921; August 1,872) with zero unmapped glyphs. This resolves the earlier UTF-8 binary retrieval obstacle for this run; it does not prove semantic row parsing.

Within decoded text objects and same-MCID groups, literal 2026 is absent from all three primary tables. June has no 2026 token; July has one on page 2 at MCID 283 (after Sum MCID 241); August has one on page 2 at MCID 349 (after Sum MCID 311). The previously verified tagged ancestry places the two tokens outside the primary Table. The post-Sum token is not an authenticated operational-year or roster-publication field. A user interface screenshot showing 2026 also lacks demonstrated same-export binding. Do not infer the year from filename, PDF CreationDate, post-Sum content, or matching company rows.

The independent one-page PDC-generator PDF has 49 body bands and 26 numeric Activity candidates, 13 with their own printed date. A fresh read-only comparison against 159 company 2026 workbook rows produced flight+route candidate multiplicities 0:8, 1:8, 2:6, 3:4. Exactly two numeric PDC candidates have independently explicit matching date+normalized 7C flight+route, and both have minute-equal source Blk Hrs and company bt. A third previously reported overlap depends on a missing-date inheritance hypothesis and is NOT a third explicit-date match. This validates only source-to-source comparison, not a user FlightRecord identity or BLH/Block semantic equivalence.

## Implementation decision — ParserProfile research delta

1. Keep Skia and PDC-generator separate immutable report-family profiles, with required anchors, per-page table/row/cell or coordinate locators, raw field state, source fingerprint, and fail-closed unknown-layout detection.
2. Treat an otherwise structurally recognized Skia PDF with no authenticated year as `YEAR_UNVERIFIED_DETACHED`, distinct from `UNSUPPORTED_LAYOUT`. A post-Sum year token must not satisfy the year requirement.
3. Preserve explicit, omitted, inferred-for-review-only, and unsupported dates as separate states. No adjacency, printed weekday, +1 marker, company date or file metadata automatically repairs a missing operational date.
4. Compare company-source 0/1/many candidates independently from actual owner FlightRecord 0/1/many candidates. A unique company hit is not attachment authorization.
5. Preserve raw BLH, Blk Hrs, source clocks, and optional C/I/C/O without assuming canonical Block, Duty or operating/deadhead semantics. PDC-generator has no participant columns; absence is not crew deletion.
6. For a future owner-approved evidence-only commit, require exact UID/unlocked state, existing-record CAS, idempotent fingerprint+locator+payload, changed-crew/same-BLH conflict review, atomic rollback, and account-deletion store inclusion. Never create FlightRecord from CrewConnex.

## Verification boundary and next gate

Real PDF decoding and PDC/company XLSX comparison were executed; no real Skia row-to-43 manually curated preview binding, verified participant semantics, actual owner-ledger match, Flutter parser, or Sembast integration test was executed. Synthetic tests from earlier cycles remain synthetic and are not upgraded here. Public corpus grade P2; production parser OPEN.

Next integrated gate: prove privacy-safe Skia page/TR/TD/MCID to manually curated 43-row lineage using independently bound year/period where available, then resolve duplicate/omitted-date, crew revision, owner-ledger cardinality and evidence-only persistence. If source-bound year cannot be established, keep detached manual review and stop short of automatic matching.
