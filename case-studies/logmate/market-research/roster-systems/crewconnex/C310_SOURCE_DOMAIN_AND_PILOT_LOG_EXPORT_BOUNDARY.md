# C310 — CrewConnex source-domain separation (2026-10-23)

Status: RESEARCH ONLY; public P2 unchanged; Production Parser OPEN. No private roster content copied.

Current official PDC AirlineSuite Features and Functionalities documentation distinguishes (1) FlightCrew flight legs synchronised from FlightTime/FlightOps; (2) pairings with layover, transportation and flight legs; (3) CrewConnex Roster/Schedule with downloadable formats; and (4) CrewConnex Pilot Log with user-entered off-block, takeoff, landing, block-on and PF/PM allocation. The latter does NOT establish any PF/PM or OOOI columns in the observed Skia/PDC roster PDFs. Audit trail/historic roster protection is NOT a roster PDF publication/revision token.

Primary source: https://www.pdc.com/airline-solution/features-and-functionalities/
Report-family context: https://www.pdc.com/airline-solution/crewconnex/
Two focused public search passes found no lawful anonymized raw Pilot Log export or validated export column mapping. Do not use identifiable published rosters. Pilot Log remains UNSUPPORTED_EXPORT and cannot be substituted for the existing-record-only roster parser.

Fresh re-aggregation of previously committed C194 privacy-safe real-PDF-derived locator manifest (blob 625c4e4367d12189f96cf4ee85cd1f3bae71e035): 62 selected Skia numeric rows; 43 unique curated Preview links, 19 uncurated August; uncurated August 17 page-1 and 2 page-2, Activity TD6=9 TD7=1 TD8=9; 62/62 operational years remain UNVERIFIED. This is manifest recomputation, NOT fresh original PDF decode. Prior company/Skia comparison for uncurated August flight+route-only cardinality: zero=8, one=4, two=5, three=2; zero minute-equal BLH or exactly equal registration among 11 rows with partial candidates. This does not prove an owner Flight is absent. PDC 26 observations and Skia 62 may overlap; 88 is NOT a unique-flight count.

ParserProfile research-2.13-C310: strict report-family detector; source-locator and raw label preservation; no Pilot Log field leakage into roster; nonflight/Sum exclusion before candidate validation; omitted Date/century/crew/revision remain detached; only verified active UID-owned Flight and explicit review may admit source-only BLH/crew evidence; dual CAS, idempotent receipt and backup compatibility required. No FlightRecord creation, canonical Block overwrite, PF/PM/PIC/SIC/date inference, or generic Flight Sync mutation. Nine grouped standalone synthetic policy tests PASS, not Dart/Sembast or production parser acceptance.

C265 correction still pending: 2025 present-empty ntTme=2, instTme=0, toCnt=5, ldCnt=4 (C277/C280 actual OOXML). Fresh-fetch GitHub update was blocked by safety checks. Do not claim remote synchronization. Next: certify Skia 27 missing-own-Date crew/section antecedents and August 19 against independently dated PDC/company/owner Flight, then actual evidence-only Sembast CAS/receipt/rollback/legacy backup tests.
