# Roster Systems Research Log

## 2026-10-04 — baseline

- Opened the broader LogMate roster-system intelligence and parser-corpus research program.
- Reused the existing CrewConnex market baseline rather than duplicating it.
- Seeded system queue: CrewConnex, AIMS eCREW, NAVBLUE/RAIDO, NetLine, CAE Crew Access, FLICA, IBS iFlight, Jeppesen, Sabre, LEON and later systems.
- Seeded parser-corpus leads for NetLine PDF, AIMS CSV/HTM, NAVBLUE ICS/PDF and FLICA ICS.
- Next highest-value target: verify and acquire the public scrambled NetLine/Crewlink PDF sample, then extract its field structure.


## 2026-10-04 23:00 KST — NAVBLUE N-Ops & Crew / N-Crew Planning

- Official NAVBLUE documentation verifies two calendar delivery modes in N-OC: subscription link and direct download, with roster changes synchronized to the external calendar.
- Official N-Crew Planning documentation explicitly identifies Download Schedule output as ICS.
- Official N-OC My Roster documentation verifies Print generates a PDF activity report.
- Documented roster semantics include calendar-month activities, check-in time/station, first activity code/start time, check-in/out, flight or station information, optional crew-on-board and notes.
- Two focused searches found no lawful public raw NAVBLUE ICS/PDF artifact. P1 remains open; do not repeat the same raw-sample query next cycle.
- Parser impact: ICS and PDF are now independently P2-verified export paths; exact ICS properties/PDF text layer remain blocked on P1.
- Next target: FLICA public ICS sample or stronger official export evidence.


## 2026-10-05 00:00 KST — CAE FLICA

- Frontier and JetBlue setup documentation independently confirms the same FLICA user export path: Schedule -> Export -> V2 Calendar (.ics), saved locally and repeated for each published monthly schedule.
- Current Flight Crew View support confirms a user-controlled ICS workflow: authenticate to FLICA in the device browser, export the ICS, then import it into the app. This supports a file-import architecture without authenticated scraping.
- Flight Crew View schedule documentation states BLK is block time downloaded with the schedule; exact ICS property mapping remains unknown.
- Two focused searches found no lawful public raw FLICA V2 Calendar ICS artifact. P1 remains open; do not infer VEVENT properties.
- Parser impact: FLICA remains P3, but V2 Calendar ICS is corroborated across two airlines plus a current downstream importer.
- Next target: CAE Crew Access export formats/public samples.

## 2026-10-05 08:00 KST — AccelAero aeroLINE CREW

- Official aeroLINE CREW App Store release notes verify a user-controlled Electronic Logbook export/download path in PDF and XLS (v5.0, 2025-04-17), with Total Duty Hours, Total Flying Hours and Grand Total statistics.
- Official v5.0.1 notes expose aircraft type + registration, ICAO/IATA airport-code switching, duty/flying-hour displays and checkout timing tied to portal duty start/end; these are field-structure evidence, not assumed exact export headers.
- Official aeroLINE CREW product brochure documents REST API and Google Calendar integration and states approximately 6,000 crew are planned or tracked through the system; because brochure observation date/customer distribution are not established, this is recorded as scale context rather than current pilot TAM.
- Two focused searches found no lawful public raw Electronic Logbook PDF/XLS. P1 remains open; private portal access was not attempted.
- Updated MASTER_SYSTEM_INDEX.csv, PARSER_SAMPLE_INDEX.csv and FIELD_COVERAGE_MATRIX.csv. Parser impact: AccelAero enters at P2 because the vendor-controlled app documentation explicitly verifies offline PDF/XLS exports.
- Next target: SkyCrew / CyberJet public raw roster/export sample or official export-format evidence.


## 2026-10-05 09:00 KST — CyberJet Skycrew / JetSched

- Current CyberJet documentation verifies Skycrew crew planning with flight/ground/rest activities, training, schedule communication and activity statements; JetSched Crew Access communicates rosters/changes and aggregated hours to crew.
- Safelog/Dauntless importer documentation verifies two distinct offline XLS inputs: Cyberjet Skycrew Flight Log (.XLS) and Cyberjet Jetsched Schedule (.XLS). This establishes P3 parser evidence and requires separate format-family handling until raw samples prove compatibility.
- Safelog identifies Air Côte d’Ivoire specifically with Cyberjet Skycrew and Wamos Air with Cyberjet Jetsched; deployment remains B pending primary/current airline corroboration.
- CAE/RosterBuster independently lists SkyCrew (CyberJet) as an enterprise roster integration.
- Two focused raw-sample searches found no lawful public Skycrew Flight Log XLS or JetSched Schedule XLS. P1 remains open; no authenticated/private portal access attempted.
- Repository index writes were attempted but blocked by connector safety checks; canonical index synchronization remains pending.
- Parser impact: CyberJet reaches P3 evidence with two concrete XLS parser inputs; exact headers/field mappings remain blocked on P1.
- Next target: TUI Opsman public raw roster/export sample or official export-format evidence.

## 2026-10-07 09:00 KST — CrewConnex corpus inventory

- Re-read the current LogMate product/import/CrewConnex contracts before research; CrewConnex remains existing-record-only enrichment/cross-check evidence.
- Read-only corpus inventory confirms roster PDF references across 2018-2026 and paired company flight-history workbook references across 2018-2026; no private raw rows were copied into Design Studio.
- Anti-duplication: the two differently named 2026 flight-history workbook entries resolve to the same repository blob and must count as one artifact, not two independent samples.
- Existing current parser contract already records TSV detector anchors, continuation-leg behavior, repeated-crew markers, rollover notation, non-flight filtering, and roster-revision variation. Internal reference evidence is not public P1 and does not raise the public sample grade above P2.
- Parser implication: next highest-information gap is privacy-safe detector/profile-generation comparison across the existing historical PDF/TSV corpus, not another generic sample search.
- Next target: compare only non-identifying headers/layout/page-continuation fingerprints across historical and focused 2026 CrewConnex samples to determine immutable ParserProfile boundaries.


## 2026-10-07 10:00 KST — CrewConnex same-period PDF artifact fingerprint

- Re-read current LogMate authority/import/CrewConnex contracts and roster-system plan/indexes before analysis; LogMate remained read-only.
- Privacy-safe repository metadata confirms seven distinct CrewConnex PDF reference artifacts: 2018, 2019, compiled 2020-2026, focused 2026-06, focused 2026-07, and two distinct 2026-08 artifacts.
- The two 2026-08 artifacts are not duplicates: the print sample is blob 29ac040595089188a8353e98f41ba27f92b8650b (552,417 bytes), while the separately named roster PDF is blob 8e7fec30f98458c770053bd7739e60869a87e33b (39,612 bytes). Same-period provenance therefore cannot be treated as proof of one byte/layout generation path; detector/profile equivalence must be demonstrated from privacy-safe text-layer/header/page fingerprints before sharing one ParserProfile.
- The 2020-2026 artifact is a separate 31,201,015-byte blob and must be treated as a corpus container/reference artifact, not evidence that one immutable layout remained stable across 2020-2026.
- Binary PDF text-layer extraction is not available through the current GitHub connector, so no header/layout equivalence claim was made and no private roster rows were copied.
- Attempted MASTER_SYSTEM_INDEX.csv synchronization after fresh fetch, but GitHub write safety checks blocked that write. This log append records the increment; retry master-index synchronization on a later fresh fetch.
- Parser impact: CrewConnex remains public grade P2. Implementation should retain fail-closed profile detection and must not collapse the two 2026-08 artifacts into one profile until detector fingerprints match.
- Next target: obtain privacy-safe text-layer/header/page-structure fingerprints for the two 2026-08 PDFs first, then compare 2018/2019/2020-2026 generations.


## 2026-10-07 16:00 KST — CrewConnex parser/matcher authority separation

- Re-read current LogMate MASTER, import contract, CrewConnex parser contract, roster-system plan/indexes before analysis; LogMate remained read-only.
- Current CrewConnex contract already establishes the strongest paired-corpus facts available without copying private rows: 2026-06~08 PDF BLH and company Excel `bt` agree in aggregate, while some corresponding legs differ in date; 2026-08 TSV/PDF also show roster-revision differences in time, BLH, registration, crew, or overall pairing.
- These observations do not authorize date correction, BLH overwrite, or automatic attachment. They instead require source-specific provenance and review when CrewConnex evidence conflicts with the existing operational record.
- Parser/matcher boundary is now explicit: ParserProfile may detect/validate/extract a supported roster layout into staging evidence; exact record identity and confidence thresholds remain owned by the general import contract and are still OPEN. Parser success must not be used as match confidence.
- Regression implication: paired-corpus tests need at least (a) aggregate-BLH-equal + leg-date-different, (b) same-period roster revision with changed BLH/registration/crew/pairing, and (c) unsupported/required-anchor-loss zero-candidate cases. All fixtures committed to CI must be redacted/synthetic.
- No new public raw CrewConnex sample was found or required for this cycle; public sample grade remains P2.
- Next target: define the minimum privacy-safe CrewConnex ParserProfile fixture manifest (multi-month, multi-page, two-month boundary, continuation, rollover, crew change, unknown code, revision conflict, unsupported layout) and map each case to pass/review/fail-closed without defining the still-open automatic-match threshold.


## 2026-10-07 19:00 KST — CrewConnex saved-web artifact version fingerprint

- Re-read current LogMate MASTER, import contract, CrewConnex parser contract, research plan/indexes before analysis; LogMate remained read-only.
- Existing corpus contains a saved CrewConnex ASP.NET login artifact alongside the roster PDFs. Its static asset query strings consistently expose `ver22.03.01.000.000` across jQuery/bootstrap/FloatThead/dateFns/moment/daterangepicker/Spinner/Global/Validators/PilotsLog assets.
- The same artifact references separate print, screen, custom-bootstrap, hide-navbar and mobile stylesheets. This is direct corpus evidence that the captured CrewConnex web generation had distinct presentation surfaces; it does not prove that PDF column/layout structure is identical across those surfaces.
- The artifact identifies CrewConnex and PDC branding and contains airline-specific logo/background configuration. Those branding URLs are not parser anchors and must not be required by a generic ParserProfile.
- Privacy boundary: no login values, employee identifiers, roster rows or credentials were copied into Design Studio. Only non-identifying version/presentation/configuration metadata was retained.
- Parser impact: `22.03.01.000.000` is a useful provenance/version fingerprint candidate, but not sufficient alone for `profileId/profileVersion` assignment. Detector acceptance still requires roster-structure anchors. Synthetic regression should include same semantic roster under print/mobile/presentation variation and assert that airline branding/configuration is ignored.
- Next target: determine whether any privacy-safe metadata/text representation in the existing 2026 PDFs exposes a CrewConnex generation/version marker or print-surface fingerprint that can be correlated with `22.03.01.000.000`; otherwise move to paired BLH/date/revision evidence without repeating binary extraction.


## 2026-10-08 09:04 KST — CrewConnex Skia PDF pagination fingerprint

- Re-read LogMate authority and Design Studio plan/indexes; inspected only non-identifying metadata and PDF text-layer geometry from three private 2026-06/07/08 printer-PDF references.
- All three PDFs use Skia/PDF m151, 2 portrait pages, ToUnicode text layers. Page 2 starts near document-space y=1682-1684, and shares the page-1 x-column grid; this supports vertical continuation of one logical table rather than a new document or horizontal tile.
- No verified repeated full table header on page 2; incomplete subset-font decoding prevents exact immutable header anchor acceptance. Source page/row locators and validated antecedent linkage remain required; unknown page/section transitions fail closed.
- The separate one-page August BLK PDF remains a distinct unverified profile; no BLK=BLH inference. Internal corpus does not upgrade public P2 grade.
- GitHub safety checks blocked canonical write; next target: synthetic two-page Skia continuation + page-2 summary boundary source-locator oracle.


## 2026-10-08 13:56 KST — CrewConnex real Skia tagged-row boundary evidence

- Re-read LogMate authority/import/CrewConnex contracts, relevant domain evidence, and Design Studio plan/indexes. Inspected the three existing private 2026-06/07/08 printer PDFs **read-only** through their PDF object/tag structure; no private content was transferred to Design Studio.
- New evidence: all three contain a tagged primary `/Table` with `/TR`/`/TD` leaves carrying page-local MCIDs. Primary tagged row totals are June 41 (p1 35/p2 6), July 45 (39/6), August 43 (34/9). Exact physical-page transition row pairs are 35→36, 39→40, 34→35 respectively; **no tagged TR spans two pages**. July/August additionally have separate two-cell tagged tables on page 2 (7/5 rows), not yet semantically classified. MCIDs restart on page 2.
- Parser impact: `pageIndex + tableOrdinal + taggedRowOrdinal` can serve as a per-file source locator for these Skia samples, with MCID/geometry as cross-check only. Tagged adjacency does **not** prove same-duty continuation; `Sum` and section boundaries must independently block antecedent reuse. The current `SourceEvidence` is record-bound, so detached staging must precede matching. No FlightRecord creation, no code/PIC/SIC/date inference.
- Corrected stale June `Sum` absence wording in geometry note. Public sample grade P2 unchanged; actual semantic row/antecedent verification and production PDF detector remain OPEN.
- Next: align tagged-row/page locators with redacted geometry and `Sum` boundaries to validate page-2 staging eligibility without exposing actual crew/roster data.


## 2026-10-08 16:57 KST — CrewConnex real Skia tagged Sum boundary

- Re-read current LogMate authority, import/CrewConnex contracts, relevant FlightRecord/evidence/crew domain code, and Design Studio plan/indexes/queue/log. LogMate remained read-only.
- Read-only in-memory ToUnicode/DEFLATE/ParentTree analysis of private 2026-06/07/08 printer PDFs confirms page-2 primary table ends at MCID 256/240/310 and separate `Sum` NonStruct marker follows at MCID 257/241/311. Page-2 primary TR counts are 6/6/9; July/August have post-Sum auxiliary tables with 7/5 TR, June none. No private roster rows or identifiers retained.
- Critical correction: prior synthetic tagged fixture models Sum as a primary TR, unlike actual Skia output. It is a negative/synthetic logic test only, not a real-layout detector oracle. Select primary table and separately tagged summary boundary; exclude later auxiliary tables. MCIDs are sample-local checks, not profile constants.
- Public P2 unchanged; production detector, duty/leg antecedent and DATA-001 reconciliation remain OPEN. Next: classify last page-1 and first page-2 primary rows via privacy-safe paired-corpus metadata to validate continuation decisions.


## 2026-10-09 — CrewConnex PDC PDF (L)/(B) airport-timezone cross-check

- On the existing private August PDC-generator PDF, compared 26 numeric-activity candidate rows at departure and arrival against independently published 2026 station time zones and a UTC+09:00 base hypothesis. **52/52** local-minus-base clock offsets match the corresponding airport-minus-UTC+09 offset; **0 mismatches**. Endpoint offset distribution: zero 42, -60 min six, -120 min two, +60 min two. Four candidates explicitly have a +1 notation.
- Evidence upgrades the *source-specific* (L)=station Local, (B)=Base reference UTC+09 hypothesis from uninterpreted to strongly corroborated. It does **not** establish a universal CrewConnex/PDC acronym contract, individual crew home-base airport, operational-date correction, or equivalent BLH/Blk Hrs semantics. Preserve raw STD/STA(L/B), +1, source locator and date-sensitive IANA offsets; unsupported settings/DST fail closed.
- No identifiable roster rows or crew IDs retained; LogMate read-only. CrewConnex existing-record-only enrichment persists. Public parser corpus grade P2, production parser OPEN.
- Geometry note updated; next target: verify a non-UTC+09 CrewConnex base setting or explicit vendor/airline documentation for (L)/(B), with redacted synthetic DST/base-change negative cases.


## 2026-10-09 06:01 KST — PDC relative-day verification

Existing 26-candidate PDC sample: 52/52 source-local/base time comparisons remain exact after +1 day markers are applied, including one base-only departure +1. No direct vendor definition or non-UTC+09 sample after two focused searches. Production OPEN; public P2 unchanged. Next: cross-format August pairs versus company operational records. No private roster copied.

## 2026-10-09 06:55 KST — CrewConnex paired August company comparison

- In-memory read-only comparison of August Skia/PDC PDF and 2026 company workbook: eight both-undated shared flight/route pairs, of which six have matching month/day antecedents, one differs, and one is blocked by non-flight rows. Skia date is yearless; PDC date is ddMMMyy.
- Six provisional same-day pairs: five unique cross-format flight/route keys, one repeated Skia key; BLH vs Blk Hrs raw strings agree in two, differ in four. Company workbook: 159 rows in 2026, three in August. One of the six has an exact company date/normalized-flight/route candidate; five have none, so no parser-failure inference.
- Skia geometry extractor recognized 42 Activity-bearing row bands against 43 tagged primary rows; complete row accounting remains OPEN. All provisional pairs remain review-only; public P2, production OPEN, no FlightRecord creation. No identifying roster data stored.
- Next: classify the Skia tagged row missing from Activity-band extraction and validate its effect on antecedent boundaries.


## 2026-10-09 08:00 KST — CrewConnex August Skia tagged-row baseline reconciliation

- Read-only in-memory Skia PDF audit: 43/43 primary tagged TR map to text baselines. Page 1: one header plus 33 body TR; page 2: nine body TR. This reconciles the previous 43 tagged rows versus 42 body text bands without a missing row.
- Of 42 body TR, 25 span multiple text baselines (22 page 1, three page 2); 11 have no x=18 first-column text (all page 1). First page-2 body row contains 31 TD but 50 MCID leaves over six text baselines. Treat multiline cell content as one tagged row; do not auto-inherit omitted date/pairing.
- Last primary page-2 row MCID 310 precedes independent Sum MCID 311; exclude post-Sum auxiliary table. Sample-specific geometry is not a universal detector. Semantic Date/Activity/crew cell alignment, June/July equivalent and page-edge duty lineage remain OPEN. Public P2 and production OPEN, existing-record-only; no personal data stored.
- GitHub safety-check blocked index and geometry writes; fresh-fetch retry next cycle. Next CrewConnex target: verify semantic Activity/date/crew cell ownership for multiline/blank-first-column rows and page-edge antecedent using the existing paired corpus.

## 2026-10-09 10:00 KST — CrewConnex Skia TD ownership and crew-baseline verification

- Existing August Skia printer PDF, read-only structural analysis: **1,234/1,234** body TD cells in **42 primary TR** map exactly to the 31 header X anchors. **68 omitted TD** belong only to Date (11), Pairing (25), AC/Hotel (17), TL List (8), Qualification (7). Fixed tag ordinal is invalid; X-grid ownership is verified for this artifact.
- Core crew columns 25/26/28: equal leaf counts **and ordered Y baselines 42/42**; 15 rows multiline (1/2/6/7-leaf counts: 27/2/9/4 rows). Optional TL List/Qualification differ; their leaves must not be zipped blindly. Page edge: last p1 row omits Pairing/AC-Hotel (29 TD; one core leaf), first p2 row has 31 TD (six core leaves). No duty/date inheritance or crew semantic equivalence established.
- Private data not copied. ParserProfile requires anchored TD ownership, baseline validation, explicit optional/missing cell handling, `Sum` barrier, provenance and fail-closed staging. CrewConnex remains existing-record-only. Public P2; production OPEN.
- Next target: **June/July Skia** cross-month grid and core crew-baseline replication.

## 2026-10-10 08:58 KST — CrewConnex July Skia ToUnicode full code-space audit

- Read LogMate authority, import/CrewConnex contracts, FlightRecord/CrewParticipant/SourceEvidence domain and tests; reviewed Design Studio plan, indexes, queue, log and existing geometry/CC gate. The private July 2026 Skia PDF was inspected read-only in memory; no raw roster text, glyph values, employee identifiers or PDF bytes were transferred to Design Studio.
- Independently decompressed both page content streams and all 17 referenced ToUnicode CMaps (13 Type3, four Type0). Parsed bfchar and bfrange, then audited all 1,921 hex Tj operations (page 1: 1,522; page 2: 399), totaling 5,664 source glyph codes (4,314 / 1,350). All 5,664 resolve through their active font's CMap; unmapped codes 0, malformed-width tokens 0, duplicate CMap keys 0, invalid UTF-16 destinations 0. No CMap array-ranges were present. This closes the prior limited-decoder four-code concern at the whole-document coverage level, not as a one-to-one code reconciliation.
- Code-space coverage does not establish human-readable glyph correctness, Unicode normalization, or CC mixed Type3/Menlo text-object semantic assembly. Preserve raw glyph-run order, font/MCID/TD provenance and fail closed on ambiguous crew associations. Internal source does not upgrade public P2; production parser remains OPEN and existing-record-only.
- Next CrewConnex target: privacy-safe Unicode-category and text-object-order validation for the 13 July mixed Type3/Menlo CC baselines in 12 tagged TD cells.

## 2026-10-10 13:56 KST — CrewConnex June/August CC Unicode and TD multi-baseline

- Read-only existing Skia PDFs: June 7/7, August 12/12 CC Type3+Menlo pairs map to Hangul syllables ×3 + uppercase Latin ×1, with 0 unmapped targeted glyphs. Same page-local MCID and tagged TD ownership 7/7 and 12/12. No private text/identifiers retained.
- June 7 pairs in 6 TD (five single, one double baseline; gap 28); August 12 pairs in 8 TD (four single, four double; gaps 14/14/14/28 document-text units). One tagged TD can contain multiple distinct rendered-token candidates; this does not prove participant identity/count.
- Parser: preserve per-glyph font/order, per-baseline and TD/MCID provenance; require Emp.# and Pos. alignment before enrichment. No FlightRecord creation, no code/credit/date inference. Public P2; production OPEN.
- Next: run privacy-safe synthetic C13–C16 multi-baseline/column-alignment gate; reconcile indexes after fresh fetch if blocked.

## 2026-10-10 16:02 KST — CrewConnex real six/seven-line CC cell alignment

- Re-read LogMate authority/import/CrewConnex and FlightRecord/CrewParticipant/SourceEvidence code; Design Studio plan/index/queue/log. Existing private June/August Skia PDF blobs inspected read-only through decompressed content streams and tagged TD→NonStruct→MCID structure. No private names, employee IDs, roster rows or raw PDF copied to Design Studio.
- June: 7 mixed CC baseline pairs in 6 tagged TD cells, **all six cells have six total Y-baselines**. August: 12 mixed pairs in 8 tagged TD cells, five with six total baselines and three with seven; two cells on page 2. Across all 14 affected rows, complete Emp.#/CC/Pos. distinct baseline sets align 14/14; their tagged TDs remain distinct, and 19/19 mixed fragment pairs share a page-local MCID.
- Adjacent full CC baselines differ by 14–15 source units; previously reported 28-unit spacing between mixed-only pairs skips intervening non-mixed baselines. Do not infer a blank crew line, participant identity/count, operating status or automatic attachment from MCID/baseline alignment.
- Existing C13–C16 synthetic tests do not cover real six/seven-line density. Add C17/C18 positive/negative synthetic coverage and verify source-to-FlightRecord matching separately. Public grade P2 unchanged; production parser OPEN; CrewConnex existing-record-only crew snapshot/BLH evidence. Next: C17/C18 executable six/seven-line alignment and missing-middle-line negative gate.


## 2026-10-11 00:58 KST — CrewConnex C21 synthetic candidate/barrier gate

- Re-read LogMate authority/import/CrewConnex contracts and current FlightRecord/SourceEvidence code/tests; reviewed Design Studio plan, indexes, queue, log and existing private-corpus metadata. LogMate read-only; no private data copied.
- Executed wholly synthetic C21 numeric-Activity and Pairing/date-lineage oracle: **30/30 PASS** after fixing an initial negative-index bug in the research harness (not LogMate). ASCII 3/4-digit syntax is candidate-only; 2/5-digit, alphanumeric, Unicode digit and suffix are unsupported/review. Pairing does not bridge nonnumeric/Remark/section/page/source barriers or establish operational date. No date/crew/Pairing inheritance; 0 FlightRecords, 0 snapshot attachments, 0 BLH overwrites.
- Existing August PDC corpus count (8 three-digit + 18 four-digit candidates) is reused, not re-verified in this run. No real PDF detector or LogMate CI was run. Public P2 / production OPEN.
- Next: independent content-band/header-boundary validation of the eight three-digit PDC Activity candidates, then profile-specific detector acceptance.

## 2026-10-11 17:03 KST — CrewConnex UI-year / cross-surface provenance gate

- Re-read LogMate authority/import/CrewConnex contracts and FlightRecord/SourceEvidence/CrewParticipant/LocalDate code; Design Studio plan, indexes, queue and log. Existing private UI references inspected read-only, no personal data copied.
- IMG_1908/1909 show the same `1 Aug 2026–30 Sep 2026` roster period and horizontally scrolled `Start/Finish(L/B)` plus `BH` columns. IMG_1918 shows WebCal/WebCals/HTTPS calendar link options, not a public raw ICS. Four existing Skia/PDC PDF Info titles were checked: none contain a four-digit year. A UI period year is NOT evidence of a specific PDF's operational year absent a same-export link.
- CrewConnex remains existing-record-only crew snapshot/BLH evidence; public P2 and production OPEN. No FlightRecord, date, crew or block-time changes. Next: same-export printed-header year/period or provenance-token verification; absent evidence, detached review only.


## 2026-10-11 21:58 KST — CrewConnex C34 omitted-cell placeholder synthetic gate

- Re-read LogMate authority/import/CrewConnex contracts and FlightRecord/CrewParticipant/SourceEvidence code/tests; Design Studio plan, indexes, queue, log and existing June/July Skia C33 geometry evidence. GitHub private binary fetch failed with UnicodeDecodeError; no new raw PDF decode or public sample acquired.
- Ran standalone synthetic C34 oracle **42/42 PASS** (39 classification cases, 3 distinct-cell-state checks). Absent TD, present blank, literal sentinel and literal value remain separate; June 24-leaf/no-Pos page-edge negative and July complete-page-edge detached review both pass. Zero FlightRecords, snapshots, BLH overwrites or inferred crew. Not a production parser or LogMate CI PASS.
- Public P2, production OPEN. Next CrewConnex target: real June/July Pos./Emp.#/CC decoded lexical-state counts and page-edge provenance, aggregate-only.

## 2026-10-12 07:00 KST — CrewConnex C43 real August missing-Date Remark verification

- Read current LogMate authority/import/parser contracts, domain code and Design Studio plan/indexes/queue/log first. Reused the existing private August Skia PDF in memory only. Decoded 1,654 text objects across two pages (1,274/380), with no unmapped glyphs; 42 body Activity rows (22 numeric, 20 nonnumeric).
- All ten page-1 numeric Activity rows with omitted Date TD have two text-bearing Remark objects each at the August-specific x=305.28125 and no same-row Pairing text. Predecessors: seven dated numeric, two undated numeric, one dated nonnumeric. Three-month Remark-presence coverage now 27/27; semantics, year, section/duty linkage and company matching remain unverified. No private roster content copied.
- Public P2 unchanged; production parser OPEN; existing-record-only crew snapshot/BLH evidence. No date inheritance, FlightRecord creation, automatic crew attachment or Block overwrite. Next: August nonnumeric-barrier and two chained rows against independently grounded same-export year/section and PDC/company evidence.


## 2026-10-12 18:55 KST — C55 Skia page-2 Sum ancestry / post-summary gate

- Re-read current LogMate authority, import/CrewConnex contracts and relevant FlightRecord, CrewParticipant, SourceEvidence/History code/tests; Design Studio plan/indexes/queue/log; reused the three existing private 2026-06/07/08 Skia PDFs read-only. No private roster rows, names, IDs or binary copied to Design Studio.
- Direct PDF object-tree audit: page-2 primary last-row max MCID is June 256, July 240, August 310; independently identified post-primary `Sum` NonStruct leaves are the immediate next page-2 MCIDs 257, 241, 311, respectively. Their ancestor chains reach Document without traversing the primary Table. The last primary row has 32/34/29 page-2 leaf MCIDs respectively.
- Post-Sum page-2 tagged leaves: June 9 (257–265), July 45, August 39. **June has nine post-Sum NonStruct leaves despite having no auxiliary Table.** July 14 and August 10 post-Sum leaves are inside separate auxiliary Tables; no post-Sum leaf is inside the primary Table. MCID values are artifact-local fingerprints, not universal constants or a replacement for semantic `Sum` detection.
- Parser rule: require independently validated primary Table/header, physical page and row provenance, and a separate `Sum`/section barrier; reject all post-Sum content even when it is un-tabled (June). Unknown/missing/conflicting marker or table ancestry must fail closed, never create a FlightRecord or infer date, crew, BLH or revision. Text-layer-to-`Sum` glyph identity was reused from the prior decoded audit, not independently re-decoded this cycle.
- Public P2 / production parser OPEN. No deployment changes. Next target: synthetic regression for June un-tabled post-Sum content, July/Aug auxiliary-table intrusion, marker missing/reordered and page-local MCID reset; then actual detector validation.

## 2026-10-12 21:00 KST — C57 PDC-to-company explicit-date reconciliation

- Re-read LogMate authority/contracts/domain code and Design Studio plan/index/queue; inspected existing private August PDC-generator PDF and 2026 company XLSX read-only in connector memory, emitting aggregate metadata only. PDC has 49 printed bands / 31 ruled groups (all group starts dated), 26 numeric Activity candidates (13 explicit dates, 13 omitted); 11 omitted-date numeric rows belong to numeric-start groups, two to nonnumeric-start groups. Group continuity does not establish operational date.
- Against 159 company rows (only three in August), exact 7C-normalized flight+route partial-key multiplicity across all 26 PDC numeric candidates: zero=8, one=8, two=6, three=4. Thus 18/26 have a partial hit, including ten ambiguous multi-hits; partial-key uniqueness alone is not a match.
- Only **2/13 explicitly dated** PDC numeric rows independently match company full date+flight+route, both with minute-equal PDC Blk Hrs and company bt. A third company August record corresponds to PDC band 2 with **omitted Date**, adjacent to band 1 in the same ruled group and sharing the preceding printed date only as an unapproved hypothesis; its Blk Hrs also equals bt. These are three distinct company records. Earlier '3 company matches' must NOT be read as three independently source-dated matches.
- Parser decision: preserve explicit/omitted date state, ruled-group locator and full-year partial-key cardinality; two full-date matches remain review candidates, one date-omitted row remains detached review. No FlightRecord creation, date inheritance, automatic crew attachment, Block overwrite or publication-revision inference. Public P2; production OPEN. Next: three-month Skia/PDC actual date/section + company matching with independent year evidence and snapshot conflict review.

## 2026-10-12 23:58 KST — CrewConnex C60 global structural match and printed-weekday gate

- Read LogMate current authority/import/parser contracts and relevant domain code, then Design Studio plan/indexes/queue/log and CrewConnex research. Reused private June/July Skia PDFs and 2026 company workbook read-only; retained only aggregate metadata.
- Independent PDF text-layer/tagged-cell extraction: 40 June and 44 July primary body rows; 18/22 numeric Activity candidates, 11/12 explicitly dated and 7/10 omitted. June 1,301/1,301 and July 1,240/1,240 text-bearing body TDs mapped exactly to their month-specific header X anchors; zero unmapped glyph events.
- Independent company XLSX ZIP/XML replication: 159 records in 2026, including June 18 and July 22. The source fltDat cells are YYYYMMDD strings. Both roster and company have 18 June and 22 July distinct flight+route+minute-BLH/bt triples. Combining this with the previous C59 one-equal-candidate-per-roster-row observation proves a within-assumed-month global structural bijection of 40/40; this is not independently authenticated full-date identity or automatic attachment authority.
- All 23 printed weekday/day/month dates are calendar-consistent with 2026, but the same 23 date/weekday constraints admit nine candidate years from 1990–2050: 1992, 1998, 2009, 2015, 2020, 2026, 2037, 2043, 2048. Source export year remains unverified; 17 omitted dates and six one-day differences remain review-only.
- Standalone synthetic decision oracle 10/10 PASS, not LogMate production parser CI. Public P2 and production OPEN; zero automatic FlightRecord creation, date correction, crew binding or Block overwrite. Next: source-bound year/period authority and 23 row-level date/section/revision adjudications.
