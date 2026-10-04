# LogMate Roster System Intelligence & Parser Corpus Research Plan

Status: **ACTIVE**
Start date: **2026-10-04**
Repository: `yhappcom/design-studio`
Scope owner: LogMate case-study market / parser research
Canonical path: `case-studies/logmate/market-research/roster-systems/`

## 1. Mission

Build a source-grounded intelligence base that answers two questions for LogMate:

1. **Market leverage:** which airline crew/roster systems cover the most airlines and pilots?
2. **Parser readiness:** for which systems can LogMate obtain enough lawful public evidence and sample data to implement reliable import parsers?

The research must go beyond vendor/customer lists. Each system should be studied down to:

- current airline users;
- pilot population;
- fleet size / aircraft types;
- roster/export formats;
- real or anonymized sample availability;
- field structure;
- airline-specific variation;
- parser difficulty;
- estimated pilot coverage if LogMate supports that system.

## 2. Primary system queue

Initial priority order:

1. **PDC FlightCrew / CrewConnex**
2. **AIMS / eCREW**
3. **NAVBLUE N-Ops & Crew / RAIDO**
4. **Lufthansa Systems NetLine Crew / Crewlink**
5. **CAE Crew Access**
6. **CAE FLICA**
7. **IBS iFlight**
8. **Jeppesen Crew Management**
9. **Sabre / AirCentre crew products**
10. **LEON**
11. **CAE Merlot**
12. **ARMS**
13. **AccelAero**
14. **SkyCrew / CyberJet**
15. **TUI Opsman**
16. other systems discovered through evidence

The queue is dynamic. A lower-ranked system may move up when a high-value parser sample or large airline cohort is discovered.

## 3. Hourly research objective

Each hourly run must produce **one measurable increment** and save it to Design Studio.

Preferred increment types, in order:

1. acquire a new public parser sample or direct sample URL;
2. identify and document an export format;
3. map fields from a real sample/manual into LogMate fields;
4. verify a current airline-system relationship;
5. obtain a current pilot headcount;
6. obtain fleet size / active fleet / aircraft types;
7. discover airline-specific system variation;
8. resolve an item in the revalidation queue;
9. update parser-readiness scoring;
10. only when none of the above is possible, discover a new roster system candidate.

A run must not merely restate prior findings.

## 4. Evidence classes

### System-use evidence

- **A1 — direct/current:** live crew portal, current airline/vendor documentation, current integration explicitly naming both airline and system.
- **A2 — corroborated:** two independent current sources, one of which is system-specific.
- **B — probable:** one credible system-specific source but incomplete current corroboration.
- **R — revalidation required:** legacy evidence, predecessor airline, rebrand, PDC/vendor customer relation without module proof, or stale source.

### Parser-corpus evidence

- **P1 — actual public sample file:** downloadable anonymized/scrambled PDF, CSV, HTML/HTM, ICS or other raw export.
- **P2 — official export documentation:** vendor/airline manual clearly defining export file or data structure.
- **P3 — third-party importer documentation:** actual instructions or support material showing how a roster is obtained/imported.
- **P4 — screenshots / visible roster structure only:** usable for field discovery, not enough for parser validation.
- **P5 — inferred:** structure suspected but not directly observed.

Parser implementation priority should heavily favor P1/P2.

## 5. Lawful data acquisition boundary

Allowed:

- public vendor documentation;
- public airline documentation;
- public sample files;
- intentionally anonymized/scrambled roster samples;
- public app support pages;
- public calendar/export instructions;
- public GitHub repositories;
- public manuals and help centers;
- files later supplied voluntarily by LogMate users with appropriate privacy handling.

Not allowed:

- bypassing login/authentication;
- credential sharing or credential harvesting;
- accessing private crew portals without authorization;
- collecting identifiable crew rosters from private sources;
- defeating technical access controls;
- treating leaked private crew data as corpus.

If a potentially useful source crosses this boundary, record its existence only if appropriate and mark it **DO NOT ACQUIRE**.

## 6. Canonical data model

For every roster system, collect where available:

### System identity
- vendor
- product
- previous/current product names
- crew-facing app/portal name
- system version or generation
- official product URL

### Airline deployment
- airline
- country
- AOC / group scope
- evidence grade
- evidence date
- source URL
- deployment notes

### Market scale
- pilot count observed
- pilot count date
- pilot count scope
- pilot planning band low/high
- cabin crew count when available
- fleet total
- active fleet
- aircraft families
- crew bases
- annual sectors / block hours when available

### Parser inputs
- PDF
- CSV
- XLS/XLSX
- HTML/HTM
- ICS/iCalendar
- API
- calendar subscription URL
- email attachment
- web-only view
- other

For each format:
- export path/instructions;
- sample availability;
- sample URL;
- anonymization status;
- date range;
- page/file structure;
- encoding;
- timezone representation;
- locale/date formatting;
- identifiers;
- known airline customization.

### Field inventory
At minimum look for:

- date
- duty type
- flight number
- departure
- arrival
- STD
- STA
- report/check-in
- release/check-out
- block time
- flight time
- aircraft type
- registration
- role / rank
- PIC/SIC indicators
- crew names / IDs
- deadhead / positioning
- standby
- training
- leave / off
- remarks
- roster publication/version timestamp
- timezone
- period totals

### LogMate mapping
Classify each source field as:

- **DIRECT** — directly maps to a LogMate field;
- **DERIVED** — can be calculated without guesswork;
- **OPTIONAL** — useful but not essential;
- **UNMAPPED** — no current LogMate field;
- **UNSAFE TO INFER** — must not be generated from ambiguous source data.

## 7. Parser readiness score

Maintain a qualitative and numerical project-priority score.

Suggested working model:

```
Parser Priority =
  pilot_coverage
  × evidence_confidence
  × sample_quality
  × format_reuse
  × field_completeness
  ÷ implementation_complexity
```

Working weights are prioritization aids, not probabilities:

### evidence_confidence
- A1 = 1.00
- A2 = 0.85
- B = 0.60
- R = 0.25

### sample_quality
- P1 = 1.00
- P2 = 0.80
- P3 = 0.60
- P4 = 0.35
- P5 = 0.15

### format_reuse
- common vendor format across multiple airlines = 1.00
- minor airline variation = 0.80
- significant per-airline customization = 0.55
- one-off airline-specific path = 0.35

Do not present the resulting score as a statistical likelihood.

## 8. Hourly run procedure

Every run must:

1. Read this plan first.
2. Read the current master index and latest research notes.
3. Check the queue for unresolved high-value gaps.
4. Search for new evidence.
5. Prefer primary sources; corroborate important third-party findings.
6. Download or record a public sample when lawful and useful.
7. Record exact provenance and date.
8. Extract new structured facts.
9. Update the relevant system file and master index.
10. Record uncertainty and contradictions.
11. Select the next highest-information-gain target.
12. Commit changes to `yhappcom/design-studio` only.

## 9. Anti-duplication / stop rules

A run must not repeat the same searches without a new hypothesis.

Stop researching a target for the current cycle when:

- two search passes produce no new evidence;
- only circular third-party references remain;
- evidence requires private portal access;
- the available public evidence is already sufficient for the current parser-readiness grade.

When blocked, mark the gap and advance to the next target.

Do not spend multiple hourly runs polishing prose while higher-value missing data remains.

## 10. Storage structure

Canonical root:

`case-studies/logmate/market-research/roster-systems/`

Files:

- `RESEARCH_PLAN_20261004.md` — this document.
- `MASTER_SYSTEM_INDEX.csv` — one row per roster system.
- `MASTER_AIRLINE_DEPLOYMENTS.csv` — one row per airline/system deployment.
- `PARSER_SAMPLE_INDEX.csv` — one row per discovered sample/export artifact.
- `FIELD_COVERAGE_MATRIX.csv` — system/format → LogMate field coverage.
- `RESEARCH_LOG.md` — timestamped concise record of each hourly increment.
- `REVALIDATION_QUEUE.md` — unresolved / stale / successor cases.

Per-system folders:

```
roster-systems/
  crewconnex/
  aims-ecrew/
  navblue/
  netline/
  cae-crew-access/
  flica/
  ibs-iflight/
  jeppesen/
  sabre/
  leon/
  merlot/
  arms/
  ...
```

Each system folder should contain:

- `README.md`
- `AIRLINES.csv`
- `FORMATS.md`
- `FIELDS.md`
- `SOURCES.md`
- `SAMPLE_INDEX.csv`
- `REVALIDATION.md` when needed

Actual sample binaries should be stored only when public, lawful, useful, and repository size/licensing/privacy make storage appropriate. Otherwise store the stable source URL and metadata instead of copying the file.

## 11. Existing CrewConnex research

Existing baseline:

`case-studies/logmate/market-research/crewconnex/`

Current snapshot already includes:

- 19-airline core cohort;
- pilot planning band roughly 3,034–4,303;
- fleet footprint research;
- source register;
- estimation model;
- revalidation queue.

Do not duplicate this work. Migrate/reuse its evidence into the broader master indexes and extend only where new evidence appears.

## 12. Initial parser-corpus leads already identified

### CrewConnex
- generic CSV / HTML import evidence;
- PDC PDF/report export capability;
- airline-specific current deployment evidence.

### AIMS eCREW
- roster CSV export;
- pilot logbook CSV;
- HTM/HTML export path.

### NAVBLUE / RAIDO
- ICS/calendar download or subscription;
- roster/activity PDF reporting;
- official roster field documentation.

### NetLine / Crewlink
- public scrambled/anonymized sample roster PDF reported by third-party support documentation.

### FLICA
- ICS calendar export path documented in airline/crew support material.

These are starting leads, not parser-complete evidence.

## 13. Required outputs for each mature system

A system is considered **research-mature for implementation decision** only when the following are available or explicitly exhausted:

- current airline list with confidence labels;
- pilot TAM estimate with direct vs modeled values separated;
- fleet context;
- at least one known export/input path;
- sample grade P1–P5;
- field inventory;
- LogMate mapping coverage;
- known airline variations;
- parser difficulty;
- unresolved risks;
- next implementation evidence required.

## 14. Decision outputs

The dataset should eventually allow these questions to be answered quantitatively:

- Which parser covers the most pilots?
- Which parser covers the most airlines?
- Which parser has the best pilots-per-development-effort ratio?
- Which systems can be supported from stable files rather than authenticated scraping?
- Which systems expose standard vendor formats across multiple airlines?
- Where are Korean airline opportunities?
- Which parser should LogMate build first, second, and third?
- What proportion of addressable pilots is covered after N parsers?

## 15. Reporting policy

Hourly runs should not generate long narrative reports.

Each run should append a concise record to `RESEARCH_LOG.md`:

- timestamp;
- target system / airline;
- new evidence found;
- files/indexes updated;
- confidence change;
- parser implication;
- next target.

Major synthesis should happen only when a system reaches a materially new maturity state or when requested by the owner.

## 16. Repository boundary

- Read/write: `yhappcom/design-studio`
- LogMate production repository: **read-only unless separately instructed**
- Do not modify LogMate application code as part of this research automation.

## 17. RELATED DOMAIN CHECK

Current Design Studio global and specialist status files were reviewed before opening this cross-cutting research plan.

- Typography: not materially involved in market/corpus acquisition.
- Color: not materially involved.
- Layout/Interaction: downstream relevance to import flows and source selection; does not own evidence acquisition.
- Web: downstream relevance to compatibility/support surfaces and public claims.
- Content: evidence-state terminology must remain precise; confirmed, probable, revalidation, observed and estimated must not be collapsed.

This work is cross-cutting project research rather than a new specialist discipline.

## 18. Success criterion

Success is not the number of documents created.

Success is a dataset and parser corpus strong enough that LogMate can choose implementation order based on **verified airline coverage, pilot reach, sample quality and parser feasibility**, with every important claim traceable to evidence.
