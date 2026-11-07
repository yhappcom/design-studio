# LogMate roster-systems research synthesis — 2026-11-07

**Status:** CONSOLIDATED RESEARCH; NOT PRODUCT APPROVAL; CrewConnex Production Parser **OPEN**.  
**Scope:** PDC FlightCrew/CrewConnex first; comparative roster-market intelligence second.  
**Authority:** LogMate [MASTER](https://github.com/yhappcom/logmate/blob/main/MASTER.md), [Import contract](https://github.com/yhappcom/logmate/blob/main/docs/specs/import-contract.md), [CrewConnex parser plan](https://github.com/yhappcom/logmate/blob/main/docs/specs/crewconnex-parser-plan.md) control product decisions. This Design Studio synthesis is an evidence-navigation layer, not a substitute or a new product mandate.

## Read in this order

1. This synthesis for supported scope and the current outcome.
2. [ParserProfile specification](PARSER_PROFILE_SPEC_20261107.md) for concrete research-stage extraction/admission design.
3. [Evidence & decision register](EVIDENCE_DECISION_REGISTER_20261107.md) for the source, correction and supersession status of every consequential claim.
4. [Implementation readiness](IMPLEMENTATION_READINESS_20261107.md) for unclosed acceptance gates and the next integrated execution package.
5. [Research plan](RESEARCH_PLAN_20261004.md), [revalidation queue](REVALIDATION_QUEUE.md), and [research log](RESEARCH_LOG.md) for continuity; older C-number studies remain immutable historical evidence rather than competing current summaries.

## Executive decision

CrewConnex is viable as an **optional existing-FlightRecord-only source of crew snapshot and BLH evidence/cross-check**, not as a creator of flights or a canonical Block updater. Significant real private source analysis and research-oracle testing exist. No production import coordinator, approved general-purpose CrewConnex ParserProfile, authenticated source-to-owner join, or native evidence-only atomic persistence acceptance has been demonstrated. Thus **no production-ready parser is claimed**.

## Actual private-corpus results (do not copy the source)

| Corpus/evidence | Grounded finding | Limit |
|---|---|---|
| 2026 June/July/August Skia printer PDF | 40/44/42 primary body rows; 18/22/22 numeric flight-shaped candidates = **62**; each candidate has Activity, From, To, BLH and ACReg physical locator (**310** selected field locators) | Flight-shaped is not a certified operated flight; all 62 same-export operational years marked UNVERIFIED |
| Source PDF -> manually curated Preview XLSX | **43/43 unique value-key links**, June 18, July 22, August 3; **19 August rows outside Preview** | Value matching reconstructs source position; not a PDF-issued identity receipt or real LogMate UID Flight match |
| Skia Date/Pairing | Own Date **35**, absent **27**; own Pairing **30**, absent **32** | Missing fields are not permission for date, Pairing or crew forward-fill |
| Skia crew cell geometry | Single-leaf **26**, six-leaf **31**, seven-leaf **5**; among 26 single-leaf physical anchors: TR distances 1=22, 2=2, 3=2 | Leaf != number of named people. 4 nonadjacent anchors disprove universal previous-row fill; physical reference != authenticated crew continuation |
| Page-2 Skia selected numeric rows | **6** across three months; own-Date 5/6; selected manifest has zero page-crossing crew physical anchors | Does not establish a safe cross-page inheritance rule |
| PDC-generator original August PDF | One **39,612-byte** original, 14 columns, **495** text operators, **48** Activity rows (26 numeric-shaped/22 nonflight), **31** printed Date cells / 31 structural date groups | One different PDF family; 31 corrects superseded 30-Date claim; no per-leg crew identity |
| PDC local/base clocks | **52/52** numeric endpoint station-offset comparisons align to one UTC+09 base interpretation in observed source | Source-specific explanatory evidence only, not universal timezone definition or authority to alter an operational date |
| 2018–2026 company flightHistory XLSX | **9** workbooks, **1530** rows, 1520 supported 7C normalization and 10 unsupported; 2026 **159** rows | Structural ZIP inspections and prior worksheet XML decoding have different verification scopes |

C194 directly decompressed the three private Skia PDFs and decoded page/ToUnicode/table/MCID and 2026 workbook XML, not merely ZIP headers. Its 62-row privacy-safe locator manifest is separately versioned and saved as [C194 manifest](crewconnex/C194_THREE_MONTH_FIELD_LOCATOR_MANIFEST.csv). No employee names, flight values or roster pages are reproduced here.

### Real cross-source comparisons

- Curated **43/43** records had unique Preview/company date + approved 7C flight + route joins and minute-equal corresponding company Actual, Block, Night and Instrument values; roster date comparisons were **37 equal and 6 +1 day**. These are bounded source comparisons, not source-year/UID authentication and not a CrewConnex BLH == company Block rule.
- For **19** August Skia rows outside curated Preview, company-2026 flight+route-only candidate multiplicity was **0:8, 1:4, 2:5, 3:2**. Of the 11 with partial-key candidates, **zero** had minute-equal BLH/company bt and **zero** an exactly equal registration candidate. These comparisons are exploratory, not evidence of unoperated or failed flights.
- The company-2026 workbook's **last observed August date is Aug 02**. The ten uncurated August Skia rows with their own printed dates show **Aug 03–31**, while nine have no own Date. The comparison set therefore has a **temporal coverage gap**; do not label the 19 as definitively unmatched.
- A few PDC/Skia coincident flight+route/day candidates show non-equal durations. Without export-century/Publication/owner/revision, they are not certified equivalent records or a basis for correction.

## Market intelligence

The current [airline deployment index](MASTER_AIRLINE_DEPLOYMENTS.csv) records **21 CrewConnex candidate airlines**: **A1 five, A2 fifteen, B one**. Consequently [system index](MASTER_SYSTEM_INDEX.csv) **airline_count_confirmed=20** is consistent when it counts only A1/A2, not all tracked rows. A pilot planning range of **3,034–4,303** covers **19** airline rows, excludes Air Premia and Eastar Jet, and is not a census of actual users/pilots. Avoid promoting estimated TAM to direct employee counts.

CrewConnex remains highest product-specific priority because private authorized examples exist. Comparative market leads: NetLine/Crewlink has **P1 public scrambled PDF**; NAVBLUE official ICS/PDF export evidence **P2**; AIMS eCREW roster CSV vs Pilot LogBook CSV are distinct **P3** source families; FLICA ICS **P3**; Leon PDF/Excel/CSV and AccelAero XLS/PDF evidence require format-specific revalidation. P1 availability for another system does not imply CrewConnex P1 support.

For CrewConnex: the system index highest public grade **P3** corresponds to weekly HTML third-party acquisition instructions, not the Skia/PDC printer PDF format. PDC official PDF-export row in [sample index](PARSER_SAMPLE_INDEX.csv) remains **P5**, private actual PDF is not public P1, and the 2023 app guide is a UI manual, not a raw roster/export schema. Earlier generic P2 claims are **not accepted as an exact-print-layout grade without source-specific proof**.

## What is now known versus unproven

**SOURCE VERIFIED:** private Skia/PDC layouts and bounded extraction, 43 curated source links, company temporal-coverage limit, PDC original 31 Date objects, one-original strict-oracle execution.  
**SOURCE-DERIVED METADATA ONLY:** Skia source locator/anchor distances, row and page topology, preview selection manifest.  
**SYNTHETIC ONLY:** some mutation/profile/date-group passes; not independent original files or Dart.  
**OPEN:** source-year/Publication/subject binding, source revision authority, unique active same-UID FlightRecord match, name mapping, full coverage August comparator, independent standards renderer, actual evidence-only Sembast CAS/replay/rollback/reopen/wipe/backup.

The research corpus must retain original raw labels and support negative conclusions. Unknown means HOLD or unsupported; it never means infer a flight, date, PIC/SIC, PF/PM, operating/deadhead status or canonical Block.

## Evidence and governance links

- Actual three-month physical source lineage and company gate: [C194](crewconnex/C194_INTEGRATED_PHYSICAL_LINEAGE_AND_AUGUST_COMPANY_GATE.md); specific August geometry: [C195](crewconnex/C195_INTEGRATED_AUGUST_DATE_GEOMETRY_ADMISSION_GATE.md).
- Cross-family and evidence-only domain constraints, including later corrections: [C233](crewconnex/C233_INTEGRATED_PROFILE_AND_SOURCE_ONLY_EVIDENCE_GATE.md).
- Strict PDC research script: [C426](crewconnex/C426_PDC_NATIVE_PDF_TEXT_ADMISSION.mjs); structured profile evidence: [PDC research profile](crewconnex/PDC_GENERATOR_PROFILE_RESEARCH_V1.json).
- C532/C533 execution-state correction: [revalidation queue](REVALIDATION_QUEUE.md), [research log](RESEARCH_LOG.md).
- No private source PDF/XLSX, employee ID, personal crew row, auth secret or raw personnel data was transferred to Design Studio by this consolidation.

## RELATED DOMAIN CHECK

Reviewed Design Studio AGENTS and current Type, Color, Layout/Interaction, Web and Content specialist status plus research index. Type/Color are not material to byte-level acquisition; Layout/Interaction owns review/HOLD/rollback UI semantics; Web owns native/PWA delivery/unsupported format surface; Content owns correct wording for source-observed, unsupported, ambiguous and user-confirmed outcomes. No UI acceptance or accessibility PASS is inferred.

## HANDOFFS TO OTHER SPECIALISTS

- **LogMate engineering/product:** research-only ParserProfile and evidence-only transaction acceptance; LogMate MASTER/specs remain authority, no implementation approval issued here.
- **Interaction/Content:** distinguish DETACHED_HOLD, FAIL_DOCUMENT, possible match, explicit user-approved association, changed source and conflict; no misleading "imported flight" success state.
- **Web/PWA:** document versioned offline profile behavior and inability to guarantee instant parser updates to offline devices; defer runtime acceptance to real build/device testing.
