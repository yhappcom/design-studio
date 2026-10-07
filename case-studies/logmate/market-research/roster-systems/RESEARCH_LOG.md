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
