# CrewConnex Airline Data — 2026-10-04

This table is the human-readable companion to `crewconnex_airlines_20261004.csv`.

**Do not read the pilot planning band as a reported headcount.** Direct observations and model outputs are kept separate.

## Core current cohort

| Airline | Country / region | CrewConnex grade | Direct pilot evidence | Pilot planning band | Fleet footprint | In service / operational | Fleet / model note | Sources |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| Air Alsie | Denmark | A2 | — | 30–60 | 8 | 8 | Narrow ownership/tracker scope; managed/operated footprint is broader | S04, S20, S21, S35 |
| Air Seoul | South Korea | A1 | — | 90–135 | 6 | 6 | Fresh Jul-2026 CrewConnex import evidence; all A321 | S05, S18 |
| Air Seychelles | Seychelles | B | historical 81 Seychellois pilots (2018) | 70–100 | 7 | 7 | 5 Twin Otter + 2 A320neo; historical pilot count is anchor only | S04, S12, S19 |
| Arkia | Israel | A2 | — | 100–180 | 10 | 10 | Tracked operational footprint includes external/wet-leased registration | S04, S22, S35 |
| Atlantic Airways | Faroe Islands | A2 | — | 30–60 | 6 units | 6 units | 4 fixed-wing aircraft + 2 helicopters; ~280 total employees in 2026 | S04, S13, S35 |
| Bulgaria Air | Bulgaria | A2 | — | 144–256 | 16 | 15 | Mixed A220/A319/A320/E190 fleet; one parked in Oct-2026 tracker snapshot | S01, S04, S23, S35 |
| DAT | Denmark / group | A2 | — | 136–272 | 20 | ~17 | Mixed ATR/Airbus Danish AOC; group has additional affiliated AOCs | S04, S24, S35 |
| Electra Airways | Bulgaria | A2 | — | 154–220 | 11 | 11 | ACMI/charter; official 10 A320 + 1 A321 | S04, S25, S35 |
| Emerald Airlines | Ireland / UK | A2 | — | 152–266 | 20 group | 19 | Ireland 13 total/12 active + UK 7 active | S04, S26, S27, S35 |
| FlyOne | Moldova | A1 | — | 126–180 | 10 | 9 | Fresh Aug-2026 source explicitly identifies FlyOne portal as CrewConnex | S06, S28, S35 |
| CemAir / FlyCemAir | South Africa | A2 | — | 160–280 | 26 | 20 | Tracker scope is CRJ/Dash fleet; other public fleet sources can differ | S04, S29, S35 |
| Jeju Air | South Korea | A2 | **656 (2023)** | 620–720 | 44 | 42 | 2023 direct pilot count from MOLIT reporting; current fleet remains similar scale | S04, S08, S17, S35 |
| Jettime | Denmark | A2 | — | 130–182 | 13 | 13 | B737-800 charter/ACMI operator | S04, S30; PDC current airline customer surface |
| Norse Atlantic Airways | Norway | A2 | **~300 (Q2 2026)** | 290–310 | 12 | 12 | Direct management statement: ~300 pilots, 580 cabin crew, 12 Dreamliners | S04, S09; PDC current airline customer surface |
| Nouvelair | Tunisia | A1 | — | 224–320 | 19 | 16 | Live CrewConnex login; current tracker shows 16 active + 3 parked | S07, S31 |
| SKY Airline | Chile / Peru | A2 | **257 Chile union roster (2025)** | 280–380 | 36 | 36 | 257 is a Chile union population, not proven total group pilot headcount | S04, S11, S14, S15, S35 |
| SkyUp Airlines | Ukraine / Malta | A2 | **168** | 168 | 10 | 10 | Official ACMI page states 168 pilots, 354 cabin crew and 10 B737s | S04, S10, S35 |
| TUS Airways | Cyprus | A2 | — | 42–60 | 3 | 3 | Official current fleet: 3 A320-family aircraft | S04, S32, S35 |
| West Atlantic | UK / Sweden | A2 | — | 88–154 | 11 traced | 11 traced | Traceable AOC subset: UK 9 + Sweden 2; public group brand describes a larger enterprise fleet | S04, S33, S34, S35 |

## Aggregated working outputs

### Pilot addressable market

Sum of the planning bands for the 19-airline core cohort:

- **Low:** 3,034 pilots
- **High:** 4,303 pilots
- **Midpoint for scenario work only:** 3,668.5 pilots

This is not a statement that PDC or the airlines collectively employ exactly this many CrewConnex-enabled pilots.

### Fleet footprint

Per-row reported/tracked fleet totals sum to roughly:

- **288 aircraft / operational units**
- roughly **271 in-service / operational units**

This aggregate is useful for scale comparison only. The denominator is heterogeneous and must not be used as an accounting fleet total.

### Korean visible cohort

- Jeju Air: 656 directly observed in 2023; planning band 620–720.
- Air Seoul: no current public pilot count found; planning band 90–135.
- Combined planning band: **710–855 pilots**.
- A conservative evidence statement for public-facing use would be: “CrewConnex is publicly observable at Jeju Air and Air Seoul; Jeju Air alone reported 656 pilots in 2023.” Do **not** publish the 710–855 range as a factual employee count.

## Pilot-band construction notes

The model deliberately avoids one universal pilots-per-aircraft ratio.

- **Known current / recent pilot counts** override generic ratios.
- **Narrowbody scheduled / ACMI** operators are generally stress-tested around a broad 12–20 pilots per active aircraft, then adjusted when operating model or direct anchors suggest otherwise.
- **Regional / turboprop mixed** operations use a broader 8–14 pilot-per-active-aircraft planning envelope.
- **Long-haul widebody** uses Norse's direct ~25 pilots per aircraft as a local anchor, not as a universal industry rate.
- **Cargo** and **business aviation** are modeled separately because rotations, standby patterns, managed-aircraft scope and utilization differ materially.
- Old pilot counts can anchor plausibility but are never silently treated as current.

See `ESTIMATION_MODEL_20261004.md` for formulas and scenario use.

## Evidence ranking implications

### A1

Strongest current public CrewConnex-specific signals:

- Air Seoul — recent 2026 integration release explicitly names CrewConnex.
- FlyOne — recent 2026 roster integration explicitly names FlyOne's CrewConnex portal.
- Nouvelair — live CrewConnex login endpoint.

### A2

For most of the remaining core cohort, two independent signals exist:

1. current CrewConnex-specific compatibility/import evidence; and
2. a current PDC airline relationship/customer listing.

This supports prioritization and sample acquisition, but it still does not prove the exact CrewConnex configuration, version, export formats, or number of enabled crew accounts.

### B

Air Seychelles is kept in the active core because it is an operating airline and current compatibility evidence explicitly names CrewConnex, but a second fresh system-side confirmation has not yet been found.

## Parser-relevant facts

Safelog documents a generic CrewConnex Roster importer for:

- **CSV**
- **HTML**

PDC documents formatted **PDF exports** for schedules/reports at platform level.

Because CrewConnex is configurable per airline, the next research layer should collect actual, user-accessible sample outputs by airline before claiming that a particular airline exposes a particular format.

## Next data fields to acquire

Priority order:

1. direct 2025/2026 pilot headcount;
2. pilot + cabin crew split;
3. actual CrewConnex export/sample formats available to crew;
4. CrewConnex URL/domain and authentication constraints;
5. aircraft types and active vs parked fleet;
6. annual sectors / block hours;
7. crew bases;
8. roster period and timezone behavior;
9. whether crew IDs, registrations, crew names and duty codes appear in exports;
10. pilot-logbook fields that can be mapped without inference.

These fields allow both **market sizing** and **parser complexity sizing** from the same evidence base.
