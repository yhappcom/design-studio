# Roster Systems Revalidation Queue

## Active

1. Verify the NetLine/Crewlink scrambled public PDF sample and capture a stable source reference or lawful repository copy if appropriate.
2. Find a public raw AIMS eCREW CSV or HTM sample.
3. Find a public raw NAVBLUE/RAIDO ICS sample and a representative PDF activity/roster report.
4. Find a public raw FLICA ICS export.
5. **CLOSED / STALE**: the earlier 19-airline migration item is superseded. The current deployment index already has 20 CrewConnex rows; pilot planning bands cover 19. Preserve source/confidence grades; do not duplicate migration.
6. Revalidate current CrewConnex use for Clic Air, Parata Air and Braathens successor entities.
7. Determine whether current Korean PDC customers Air Premia and Eastar Jet use FlightCrew + CrewConnex specifically.
8. CrewConnex Skia printer-PDF: independent ToUnicode decode verifies ordered page-1 core headers Date/Activity/From/To/BLH/Emp.#/CC/Pos. and page-2 Sum in June/July/August (earlier June-absence claim corrected). Primary tagged-table physical locators are structurally supported (June 35+6, July 39+6, August 34+9); exact page-2 Sum-to-tagged-row mapping, semantic continuation and negative detector acceptance remain OPEN. 2026-10-08 tagged synthetic fixture structurally covers MCID reset, primary/aux table, summary barrier, malformed ParentTree and BLH grid drift; real Skia row-to-Sum mapping remains unverified. 2026-10-08 18:04 nested-cell audit: June/July/August first p2 TR has 32/30/31 TD but 78/50/50 MCID leaves; 15/17/15 primary rows contain multi-leaf TD. Add nested-cell regression, preserve cell/leaf provenance, and classify semantic page-edge leg/antecedent using privacy-safe paired corpus before PASS.
9. CrewConnex same-August cross-format: 2026-10-09 geometry-filtered Skia 22 numeric rows/20 distinct flight+route keys and PDC 26/26; 16 shared keys, 14 unique in both, 2 repeated in Skia. Raw BLH vs Blk Hrs equals 8/18 unfiltered key-pairs; **not date/revision-verified**, no semantic equivalence. Resolve date-aware pairing and repeated-key ambiguity; keep separate fail-closed profiles.
10. CrewConnex PDC-generator PDF: 49 content bands, 26 numeric Activity candidates (13 explicit dates, 11 tentative contiguous dates, 2 unsafe post-barrier); 2 independently row-dated company matches with minute-equal Blk Hrs vs bt, plus 1 unverified omitted-Date inheritance hypothesis (not an independent exact-date match). The same-August Skia PDF differs in generation and candidate coverage; require exact date/revision/leg alignment before merging evidence.
11. CrewConnex PDC PDF date-lineage check (2026-10-09): 13 undated numeric candidates; 7 direct, 4 chained, 2 blocked by intervening non-flight/blank rows. Two chained rows repeat Pairing. Eight undated Skia/PDC cross-format pairs still require independent Skia-side validation.
10. CrewConnex PDC-generator local/base time semantics: 2026 August source cross-check shows 52/52 STD/STA(L minus B) deltas equal the respective airport's UTC offset minus UTC+09:00. Strong source-specific local/base evidence, including 52/52 relative-day +1 checks; direct PDC acronym definition and non-UTC+09 base fixture still absent after two focused searches. Require verified crew/base timezone and date-aware IANA/DST +1 handling; if unavailable, preserve four raw clock values and mark normalization unsupported (zero automatic date or FlightRecord mutation).
12. CrewConnex August paired-corpus follow-up (2026-10-09): six provisional same-month/day antecedent pairs; one exact company flight/date/route candidate and five unmatched against only three company August records. Skia 43 tagged rows reconcile as one header plus 42 Activity-bearing body rows (33 page-1, nine page-2). Resolve tagged-cell/section alignment, repeated-key ambiguity, and full-year/revision provenance before matching.
14. Index synchronization debt (2026-10-09): GitHub write safety check blocked `PARSER_SAMPLE_INDEX.csv` and `FIELD_COVERAGE_MATRIX.csv` paired-corpus annotations; refresh and retry. Existing `RESEARCH_LOG.md`, `MASTER_SYSTEM_INDEX.csv`, and geometry note are saved. A queue numbering cleanup attempt was also blocked.

15. CrewConnex Skia August tagged-row structural gate (2026-10-09 08:00 KST): 43 primary TR map to one header and 42 body row baselines (33 page-1 body, nine page-2). 25 body TR have multiline text; 11 omit first-column text. Page-2 Sum MCID 311 follows last primary row MCID 310; auxiliary table excluded. Still OPEN: semantic Date/Activity/crew mapping, page-edge antecedent and June/July equivalent; use redacted/synthetic regression only. This cycle GitHub safety-check blocked writes to crewconnex/PDF_PRINT_GEOMETRY.md, MASTER_SYSTEM_INDEX.csv, PARSER_SAMPLE_INDEX.csv and FIELD_COVERAGE_MATRIX.csv; retry after fresh-fetch. Research log commit 12724c95f6cb242042019d17cb1d1b29bbe9b647.

16. June omitted Pos. TD (2026-10-09): header index 28 is Pos.; eight of 40 June body rows omit this TD, all with nonnumeric Activity; all 18 numeric-Activity rows retain it. June header has additional DH CC, Remarks and Fdp Time tail fields, unlike July/August. Next: classify crew-cell content/blank/sentinel and baseline cardinality in these eight rows; page-2 first body row is among them. Fail closed on unexpected missing Pos. and never forward-fill roles. Geometry note, research log and field matrix write retry after fresh-fetch (GitHub safety checks); master and sample indexes updated.

17. CrewConnex June missing-Pos leaf gate (2026-10-09): eight nonnumeric-Activity body rows omit Pos. but retain text-bearing Emp.# and CC. Seven have one paired leaf; page-2 first body row has 24 paired leaves with matching baselines and no Pos. TD. This is not 24 validated participants. Next: validate sentinel/blank semantics against the existing TSV and require synthetic negative fixture with zero automatic crew/FlightRecord creation. Index/geometry synchronization retry required after fresh-fetch.
18. CrewConnex June pipe antecedent: 16 aligned triplets split into seven numeric-Activity candidates (adjacent dated numeric predecessor, one predecessor Pairing absent) and nine nonnumeric-Activity rows (explicit Date). Verify same-duty/crew consistency and negative fixtures; no blanket reuse. Synchronization of research log, geometry and indexes requires fresh-fetch retry after GitHub safety-check blocks.


## 2026-10-09 16:01 KST — CrewConnex repeat-lineage open gate

June numeric pipe triplets: 7/7 previous dated numeric Activity with explicit crew values; preceding Pairing present 6/7, omitted 1/7. Current Date/Pairing omitted; From/To/BLH populated. Same-duty link unverified. Next: independent Pairing/Roster/DC and section-barrier audit of seven; missing-predecessor-Pairing synthetic fail-closed fixture. Retry any unsynchronized indexes after fresh fetch.


2026-10-09 16:55 KST — CrewConnex: seven numeric continuation candidates have no decoded Roster/DC text in current or preceding row; one lacks preceding Pairing. Next: verify antecedent barrier. Research/index sync pending after blocked writes.


2026-10-09 22:03 KST - CrewConnex publication/revision gate: Existing mobile UI screenshots display an explicit calendar year and a two-month roster period, while Notifications shows acknowledged changes with affected dates. No stable roster revision ID or publication timestamp is visible. The login/profile software-version label and saved-web asset version are NOT roster revisions. Treat yearless printer-PDF dates as unresolved without independently validated context. FIELD_COVERAGE_MATRIX publication_version should be OPEN, not OBSERVED. Next: determine whether the printable PDF header or export workflow carries a stable revision/publication token; otherwise require fingerprinted source snapshot plus manual review. Previous index/log synchronization blocked by GitHub safety checks; retry after fresh fetch.

Vendor follow-up: indexed PDC System Monitor PDF describes before/after roster changes, change actor/time, and CrewConnex acknowledgment timestamp. Direct PDF access returned 404. Current PDC product page confirms notifications/acknowledgments. This is not proof of a revision ID in a CrewConnex PDF export; export-level publication identity remains OPEN. See PDC systemmonitor PDF indexed under 2023/10 and current CrewConnex product page.


2026-10-09 23:01 KST — CrewConnex export identity / report-family gate: four existing Skia/PDC PDFs inspected at byte-level; PDF Info exposes generator/title/timestamps but no roster publication/revision ID; no XMP packets. This is metadata-only, NOT a decoded page-header absence claim. Official PDC lists distinct Roster, Day Schedule PDF and Master Schedule PDF surfaces. Require explicit report-family detector and publication token search in decoded page header/export UI; reject unknown report PDFs, never infer revision from CreationDate. A publicly indexed roster with apparent identifying crew data was rejected as DO NOT ACQUIRE; no source content retained. Next: inspect printed header/period and export UI, then define no-token fingerprinted-snapshot review policy.

## 2026-10-10 05:03 KST — CrewConnex July CC-fragment follow-up

July Skia 1,240/1,240 body TD map uniquely to 30 X anchors across 44 primary body rows; core crew columns 25/26/28 are present in all rows. Raw leaf counts differ in 12 rows due to 1–2 extra CC fragments at existing Y baselines; grouped unique baseline sets align 44/44. This does not validate participant count/identity or same-duty inheritance. Next: determine whether CC duplicate-baseline fragments are same-line subdivisions or distinct semantic tokens and encode lossless grouping/ambiguous negative fixtures. P2 / production OPEN / existing-record-only.


## 2026-10-10 — CrewConnex CC mixed-origin follow-up

July CC content stream: 13 duplicate page/Y baselines with same X and MCID combine a three-glyph Type3 text block and a one-character ASCII text block; ASCII is not `|`. This refines the previous 12 affected-row count (different unit). Treat same-origin mixed text as ambiguous, not additional crew or a repeat marker. Next: synthetic same-MCID mixed-script versus literal-pipe negative oracle and source-locator gate. P2; production OPEN. Other index/log writes require fresh-fetch retry.

## 2026-10-10 07:02 KST — CrewConnex CC synthetic oracle execution

C1–C9 and three additional synthetic provenance negatives executed: 12/12 PASS in standalone Python, zero participant/FlightRecord creation. This is NOT production parser PASS. OPEN: GitHub source upload, real Skia detector validation, calibrated Y/X tolerances, Type3+ASCII same-origin semantic interpretation, and multi-month fixture integration. Next target: July CC font/ToUnicode text-object ordinal + tagged cell provenance without exporting private tokens.

## 2026-10-11 03:00 KST — PDC nonnumeric negative-detector gate

Read-only August PDC 49-band source: 22 nonnumeric Activity bands (18 route, six Pairing, all four clock fields, zero Blk Hrs) plus one remark-only; four nonnumeric arrival clocks fail strict HHMM range and additional rows carry +3/-1 offsets. Next: synthetic C22 detector negative fixtures and report-family/section boundary acceptance; no automatic FlightRecord or crew attachment. Public P2; production OPEN. Prior sync debt still pending.

## 2026-10-11 11:58 KST — CrewConnex export revision-token gap

Two focused lawful public searches found no verifiable CrewConnex printer-PDF `Revision`/`Issued` label-to-value mapping or export-level publication token. Existing private July/August Skia labels occur after `Sum` in `NonStruct` (prior read-only audit), not validated roster metadata. PDC confirms notification acknowledgments and separately configurable report families; these are not PDF revision identities. Roster Helper's 2026 FlyOne CrewConnex integration independently reports notifications, acknowledgments and locally managed revision history, but neither developer guide nor app release proves that PDF exports carry a stable revision ID. FlyOne deployment is third-party B pending direct corroboration; no raw sample acquired. Reject any public roster containing crew identifiers (DO NOT ACQUIRE). Next CrewConnex gate: privacy-safe multi-month paired-corpus exact-date/flight/route ambiguity classification; continue treating source fingerprint as snapshot identity only, not recency ordering. Pending index synchronization remains unresolved after GitHub safety-check rejection.

## 2026-10-11 20:00 KST — C32 CrewConnex tagged-header ownership

All 3,870 primary TD cells across three existing Skia PDFs carry empty Headers and unit spans; no primary TH/Scope. Auxiliary TH exists in July/August. The 96/126 shortened body rows cannot be aligned to primary header by TD ordinal. Next: June/July physical grid ownership and absent-vs-blank TD, especially page-2 first row. Public P2 / production OPEN. Synchronize C31 and indexes after fresh-fetch if blocked.

## 2026-10-11 23:56 KST — CrewConnex August crew-column verification

Real August Skia: 42/42 rows have Emp.#, CC, Pos. TDs and aligned rendered baselines; 1,234/1,234 body TDs uniquely map to 31 header anchors. All three columns have 17 pipe and four whitespace-only lines; Pos. also five hyphen lines. Page-2 first row has six aligned non-placeholder lines per column. No crew inference. Next: synthetic missing/shifted Pos., mixed-font, placeholder, and page-edge negative gate. Public P2; production OPEN.

19. CrewConnex C39 (2026-10-12): Of 34 omitted-Date TD rows across June/July/August, 27 have ASCII 3/4-digit Activity (7/10/10), seven are nonnumeric (3/3/1). Numeric predecessors: 22 dated numeric, four undated numeric, one nonnumeric; zero cross-page, zero Pairing TD, 27 BLH text. Verify section/Remark/Sum barriers and full-date evidence; never infer date or crew from adjacency. Public P2; production OPEN. Retry prior index synchronization.

20. CrewConnex C44 (2026-10-12): actual August Skia page-1 row13 has omitted Date/Pairing after dated nonnumeric row12; rows19→20→21 form a three-row omitted-Date/Pairing numeric chain after dated row18. Company 2026 workbook has 159 data records; target rows 13/19/20/21 have flight+route partial-key hits 0/0/0/1, with no independently validated full-date match. Detached review only; public P2, production OPEN. Next: audit other 18 August numeric rows by company partial-key cardinality and independent date evidence. Synchronize C44 and indexes after fresh-fetch if blocked.

21. CrewConnex C45 (2026-10-12): Read-only August Skia/company XLSX 18-row follow-up, excluding C44 rows 13/19/20/21. Company flight+route candidate multiplicity 0:5, 1:3, 2:6, 3:4; 12 explicit yearless dates, six omitted; two month/day overlaps only if PDF year is assumed 2026. Tagged 42 primary body rows separated from five post-Sum auxiliary TR. Public P2, production OPEN. Next: independently verify same-export year/period or record explicit absence, then date-aware one-to-one review. No auto binding.


## 2026-10-17 C164 — CrewConnex semantic-namespace and local-acquisition review

- The 19-operator migration queue item is stale: current deployment index has 20 CrewConnex rows, with pilot bounds on 19; master index count was updated by commit 41f76f8. Do not claim all 20 are current direct A1.
- CrewConnex BLH and PDC Blk Hrs are distinct raw roster observations, not canonical Block values; equality in paired company samples is cross-check evidence only. Existing scalar SourceEvidence cannot hold detached or withheld crew snapshots. Need evidence-only store/transaction without fake Flight mutation.
- Public P2 roster-schema classification remains under audit. RosterBuster weekly HTML/frame-source and Safelog CSV/HTML are P3 third-party format leads, not P1 samples or approved LogMate credential/hosted-upload flows.
- Same-export Skia operational year/crew antecedent/publication order and real UID-owned Sembast approval remain OPEN. C164 synthetic oracle is not production PASS.


## 2026-10-17 C169 — CrewConnex source-denominator and evidence-only API gate

Aggregate revalidation of existing real-source C110/C112/C44/C45 (no new PDF decode): 62 Skia numeric candidates = June 18 + July 22 + August 22. Curated 43 PDF-linked preview entries = 18 + 22 + 3; remaining 19 are August **not represented in curated preview**, not proven unmatched. C44/C45 combined August company-2026 flight+route-only cardinality for 22 source candidates: 0=8, 1=4, 2=6, 3=4. Ten ambiguous partial keys and eight with no partial hit; even four unique keys lack source-bound full date/year, UID and revision. Six +1 and 18 missing Date figures apply to 43 preview-linked entries, not all 62. Separate PDC-generator cohort must not be conflated.

Product-code audit confirms record/field-bound scalar SourceEvidence and append-only scalar notice are not crew snapshot revision storage, while LedgerMutationPlan requires canonical mutation and current repository lacks evidence-only API. Proposed v0.83 source observation/interpretation/approved binding/receipt separation; owner UID+active Flight+RevisionId CAS, privacy-withheld/not-provided distinctions, historical replay and wipe. Standalone synthetic nine-group oracle PASS, not Dart/Sembast. Next: authenticate same-export Skia year/period, resolve August 19 and six +1/18 missing-date source/crew antecedents, then test actual owner-ledger evidence-only atomic storage. Public P2 format scope and P3 weekly HTML remain unverified for exact parser schema. C158-C168 failed writes to C112/sample/field/log remain sync debt; refresh and retry without repeating blocked writes. Production OPEN.

## 2026-10-20 15:01 KST — C243 corrected company-source audit

- Original nine company XLSX files independently verified: 1530 rows; 1520 supported 7C; full-date composite duplicates 0; yearless collisions 7 groups/14 rows. 2026 company June/July/August 18/22/3 is not Skia year/revision proof.
- **SUPERSEDED by C277/C280 original-OOXML revalidation (2026-10-22):** 2025 physically present-empty: `ntTme=2`, `instTme=0`, `toCnt=5`, `ldCnt=4`; no non-H:MM nonempty Night/Instrument values in 2025. Nine-year duration comparisons: Instrument Flight Time > Actual once (2019); Night > Block zero and Actual > Block zero. These are diagnostics, not authority for time correction. Preserve C243 as historical erroneous claim only.
- Current deployment index already has 20 CrewConnex entries; old 19-row migration task is stale. Production parser OPEN. Outstanding: Skia year, crew continuation, publication and real UID-owned Sembast source-only transaction acceptance.

## 2026-10-20 C245 — PDC nonflight detector and source-type gate

Actual one-page PDC PDF: 49 body bands = 26 numeric-Activity candidates + 22 nonnumeric + 1 blank; route+four-clocks alone falsely accepts 18 nonnumeric rows. Of 13 undated numeric candidates, 7 directly follow a dated numeric row, 4 are chained, 1 follows nonflight and 1 follows blank Activity; none authorizes date inheritance. The misnamed internal .aspx is login HTML, not a roster/PDF sample. No public P1 or actual Dart/Sembast PASS. Revalidate source year and crew lineage, then test owner-UID evidence-only atomic persistence. Earlier 2025 Excel reversed-null assertion is superseded by C277/C280: physically present-empty `ntTme=2`, `instTme=0`, `toCnt=5`, `ldCnt=4`.

## 2026-10-23 C317 — Crew structure / nonflight exception and correction checkpoint

- **C315 structural claim corrected and saved:** page-2 direct `/Type /MCR` was miscounted as an empty TR. Actual primary TRs 41/45/43, zero empty TRs, three MCR nodes and 12 auxiliary TRs; typed traversal validates 62/62 candidate rows and 310/310 selected field locators. The C315 file now explicitly marks the historical mixed-child counts as superseded.
- **New real-original structural gate:** among 27 numeric Skia candidates without their own Date, 26 have 1/1/1 Emp.#/CC/Pos. MCID leaf counts, but August primary TR #14 (body #13, page 1; outside curated Preview) has 6/6/6 despite absent Date/Pairing and an earlier source-text-confirmed nonflight predecessor. Dated 35 candidates have 6/6/6 or 7/7/7. These are MCID leaves, not people or proof of repeated crew. **Never infer Date/crew from leaf count or adjacency.** Validate raw text, baseline grouping, barrier and independently authenticated period before binding.
- **Sync debt closed:** C200/C265 2025 XLSX empty-cell claims corrected against saved C277/C280: `ntTme=2`, `instTme=0`, `toCnt=5`, `ldCnt=4`. No new original-workbook decode in C317.
- **Remaining blocker:** source-bound Skia operational year/publication, row-level crew-text semantics for the 27 omitted-Date candidates, 19 August non-Preview full-date+UID Flight cardinality, and actual evidence-only Dart/Sembast CAS/receipt/reopen/legacy-backup acceptance. Public P2 / Production OPEN. Six research-only synthetic policy tests PASS, not product tests.
