# CrewConnex Airline Market Research

Snapshot date: **2026-10-04**

Purpose: maintain a source-grounded working dataset for LogMate on publicly observable airlines using, or strongly associated with, **PDC CrewConnex**, with emphasis on pilot addressable market size, fleet footprint, parser leverage, and evidence gaps.

## Status

This is an **initial research snapshot**, not a PDC-authoritative customer register.

PDC states that CrewConnex is not standalone and requires **PDC FlightCrew**. PDC also states that its airline scheduling software is used by 49 international airlines, but that does **not** mean all 49 use CrewConnex. The current PDC customer list likewise cannot be treated as a CrewConnex customer list.

The core cohort here therefore requires CrewConnex-specific public evidence, with a confidence grade:

- **A1 — direct/fresh CrewConnex evidence:** current CrewConnex portal or a recent integration explicitly naming the airline and CrewConnex.
- **A2 — corroborated:** CrewConnex-specific import evidence plus a current PDC relationship/customer listing.
- **B — probable/current candidate:** CrewConnex-specific import evidence and an active airline, but no second current system-side corroboration yet.
- **R — revalidation:** legacy CrewConnex evidence, successor/rebrand/current PDC relationship, or other signal that is insufficient to call current CrewConnex use.

## Current headline

Core publicly observable cohort: **19 active airlines**

Initial pilot planning band: **~3,034–4,303 pilots**

Reported fleet footprint across the same cohort: **~288 aircraft/operational units**, of which roughly **271 are currently in service/operational in the cited snapshots**.

These fleet totals are **not accounting-grade totals**. Scope differs by airline: some sources count parked aircraft, group subsidiaries, managed aircraft, helicopters, or wet-leased aircraft. Use the per-airline scope field before doing downstream calculations.

### Korea

- **Jeju Air**: 656 pilots in 2023 was reported from Korean Ministry of Land, Infrastructure and Transport data; current fleet snapshots remain similar in scale.
- **Air Seoul**: current CrewConnex use is unusually well evidenced by a July 2026 CrewLine release; a current public pilot headcount has not yet been found.
- Korean CrewConnex-visible pilot planning band: approximately **710–855 pilots**. This is a model, not a headcount.

## Why this matters to LogMate

1. A CrewConnex import path is not a one-airline feature. Public evidence already points to a cross-regional cohort spanning Korea, Europe, Africa, the Middle East and South America.
2. Safelog currently documents a generic **CrewConnex Roster** importer for **CSV and HTML**, in addition to airline-specific automatic CrewConnex imports.
3. PDC itself documents schedule/report **PDF export** capability, but CrewConnex is configurable per airline. Availability of a format at platform level does not prove that every airline exposes it to every crew member.
4. Therefore the preferred LogMate architecture remains: **common CrewConnex canonical parser/model + format adapters + airline-specific normalization only where evidence requires it**.
5. The current visible cohort alone suggests a pilot TAM on the order of **3k–4.3k**, before undiscovered/currently unverified CrewConnex customers are counted.

## Files

- [AIRLINE_DATA_20261004.md](./AIRLINE_DATA_20261004.md) — readable airline-by-airline snapshot.
- [crewconnex_airlines_20261004.csv](./crewconnex_airlines_20261004.csv) — machine-readable working dataset.
- [ESTIMATION_MODEL_20261004.md](./ESTIMATION_MODEL_20261004.md) — rules, formulas, uncertainty and scenario outputs.
- [SOURCES_20261004.md](./SOURCES_20261004.md) — source register and evidence notes.
- [REVALIDATION_QUEUE_20261004.md](./REVALIDATION_QUEUE_20261004.md) — successor, legacy and PDC-only candidates requiring CrewConnex-specific revalidation.

## Important evidence boundaries

- Pilot estimates are **planning bands**, not claimed employee counts.
- A PDC logo/customer listing confirms a PDC relationship, not necessarily FlightCrew or CrewConnex.
- Safelog's current compatibility page is strong evidence that a CrewConnex integration existed/exists, but it retains some legacy airline names; it is therefore not sufficient by itself for A1.
- Fleet counts from tracking databases can differ from operator/accounting fleet definitions.
- No private airline systems, credentials, or restricted crew portals were accessed.

## RELATED DOMAIN CHECK

- **Typography / Type:** current status reviewed; not materially relevant to airline market-size evidence.
- **Color:** current status reviewed; not materially relevant.
- **Layout / Interaction:** current status reviewed. This dataset can later affect import-source prioritization and provider selection flows, but it does not define those interaction contracts.
- **Web Design:** current status reviewed. Any public LogMate support/compatibility page should expose only evidence-appropriate claims and should not present estimated pilot counts as facts.
- **Content Design / UX Writing:** current status reviewed. Critical transfer is semantic labeling: **confirmed/direct**, **corroborated**, **probable**, **revalidation**, and **estimated** must remain distinct.

## HANDOFFS TO OTHER SPECIALISTS / PROJECT WORK

- **LogMate product/parser work:** use the cohort and format evidence to prioritize CrewConnex parser coverage and sample acquisition.
- **Web/Content:** if airline compatibility is later published, use only verified current support and avoid implying an airline partnership.
- **Marketing/strategy:** pilot bands may be used for opportunity sizing only with the uncertainty labels preserved.
- **Evidence governance:** refresh this snapshot whenever a new airline-side CrewConnex portal, import sample, current pilot headcount, or fleet change is found.

## Primary platform sources

- PDC CrewConnex: https://www.pdc.com/airline-solution/crewconnex/
- PDC airline solution/current customer surface: https://www.pdc.com/airline-solution/
- PDC airline scheduling footprint: https://www.pdc.com/solution/planning-for-airlines/
- Safelog supported imports: https://www.safelogweb.com/FAQ/default.aspx
