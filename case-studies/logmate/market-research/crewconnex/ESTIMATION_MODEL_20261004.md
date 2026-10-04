# CrewConnex Pilot Market Estimation Model — 2026-10-04

## Objective

Create a reproducible planning model for the number of **pilots potentially addressable by a LogMate CrewConnex import path** without confusing modeled values with airline-reported headcounts.

The model is intentionally conservative about evidence semantics and intentionally broad about uncertainty.

## Raw vs derived fields

### Raw / observed

Preferred inputs, in order:

1. airline/government-reported pilot headcount;
2. current management statement;
3. union roster where coverage is understood;
4. current active/in-service fleet;
5. total fleet;
6. operation type and aircraft family;
7. total employees, cabin crew, block hours or sectors when useful as a plausibility check.

### Derived

Derived outputs include:

- pilot planning band;
- pilots per active aircraft;
- visible CrewConnex pilot TAM;
- adoption scenarios;
- expected monthly roster-import volume;
- concentration by airline;
- sample/parser priority.

Derived values must always be labeled **MODEL** or **PLANNING BAND**.

## Current direct anchors

### Jeju Air

Observed 2023 pilots: **656**.

2023 fleet size was reported at a similar order of magnitude to the current fleet; Oct-2026 tracking shows 44 total / 42 in service.

2023 pilot-per-aircraft anchor using the 42-aircraft 2023 fleet reference:

```
656 / 42 = 15.62 pilots per aircraft
```

This is a useful LCC/narrowbody reference, not a universal staffing rule.

### Norse Atlantic

Q2-2026 management statement:

- around 300 pilots;
- 580 cabin crew;
- 12 Boeing 787s.

Approximate pilot-per-aircraft anchor:

```
300 / 12 = 25 pilots per aircraft
```

This is a long-haul widebody operating-model anchor.

### SkyUp

Operator states:

- 168 pilots;
- 354 cabin crew;
- 10 Boeing 737s.

Pilot-per-aircraft anchor:

```
168 / 10 = 16.8 pilots per aircraft
```

This is particularly useful for narrowbody ACMI comparison.

### SKY Airline

257 pilots were in the Chile pilot-union roster in March 2025.

This is treated as a **partial/lower-bound population**, not as a group total, because the airline operates across Chile and Peru and union coverage is not proven to equal all group pilots.

## Planning envelopes

These are stress-test ranges, not industry constants.

| Operation type | Initial planning envelope | Reason |
| --- | ---: | --- |
| narrowbody scheduled / ACMI | ~12–20 pilots per active aircraft | brackets Jeju/SkyUp anchors while allowing schedule/base variation |
| regional / turboprop | ~8–14 | shorter sectors and fleet/base structures vary widely |
| widebody long-haul | local anchor ~25 | use direct Norse evidence where applicable |
| cargo | ~8–14 | utilization, night operation and base patterns vary |
| business / managed aviation | case-specific | managed-aircraft scope makes fleet-count multiplication unreliable |
| mixed fixed-wing + helicopter | case-specific | crew licensing and mission mix prevent direct transfer |

The per-airline bands in the dataset apply these envelopes only after considering available direct evidence and scope.

## Current cohort output

19-airline core cohort:

```
pilot_band_low  = 3,034
pilot_band_high = 4,303
midpoint        = (3,034 + 4,303) / 2
                = 3,668.5
```

Use the midpoint only for scenario comparison. It is not a best estimate with statistical confidence.

## Adoption scenarios

If the visible cohort were the full reachable market and LogMate adoption among those pilots were:

| Pilot adoption | Users at low TAM | Users at high TAM |
| ---: | ---: | ---: |
| 1% | ~30 | ~43 |
| 5% | ~152 | ~215 |
| 10% | ~303 | ~430 |
| 20% | ~607 | ~861 |
| 30% | ~910 | ~1,291 |
| 50% | ~1,517 | ~2,152 |

These are scenario mechanics only. No conversion rate is asserted.

## Roster-import volume scenarios

Assumption for a simple operational load model:

```
1 active pilot user × 1 monthly roster import × 12 months
```

Full visible pilot TAM would imply:

```
3,034 × 12 = 36,408 roster-month imports/year
4,303 × 12 = 51,636 roster-month imports/year
```

At 10% adoption:

```
~3,641–5,164 roster-month imports/year
```

At 20% adoption:

```
~7,282–10,327 roster-month imports/year
```

This can later inform parser regression testing, telemetry sizing, import-failure support burden, and sample diversity.

## Cohort concentration

Using the midpoint of each current planning band only for prioritization:

- Jeju Air: ~670 midpoint pilots, about **18%** of the modeled visible cohort.
- SKY Airline: ~330, about **9%**.
- Norse Atlantic: ~300, about **8%**.
- Nouvelair: ~272, about **7%**.
- CemAir: ~220, about **6%**.

The first five therefore represent roughly half of the current modeled pilot opportunity. This is a **prioritization heuristic**, not a market-share claim.

## Korean opportunity

Current visible Korean CrewConnex evidence:

- Jeju Air — direct 2023 pilot count 656; model 620–720.
- Air Seoul — fresh 2026 CrewConnex evidence; pilot count still modeled 90–135.

Combined model:

```
710–855 pilots
```

For external/public copy, prefer direct observations over this modeled aggregate.

## Fleet footprint

The current row-level fleet figures sum to approximately:

```
288 total/tracked aircraft or operational units
271 in-service/operational units
```

Do not calculate a single global pilot-per-aircraft ratio from this sum because:

- Air Alsie has managed-aircraft scope mismatch;
- Arkia includes wet-leased/external registrations;
- Atlantic Airways includes helicopters;
- Emerald is aggregated across two AOCs;
- West Atlantic is deliberately limited to a traceable AOC subset;
- parked-aircraft treatment differs.

## Parser leverage model

A parser's value is not simply the number of airlines.

A useful future score:

```
Parser Priority Score =
  addressable_pilots
  × evidence_confidence
  × sample_availability
  × format_reuse
  ÷ implementation_complexity
```

Suggested qualitative multipliers:

- evidence confidence: A1 1.0, A2 0.85, B 0.60, R 0.25;
- sample availability: actual recent sample 1.0, documented format 0.7, inferred only 0.3;
- format reuse: common CrewConnex CSV/HTML 1.0, minor airline variant 0.8, bespoke path 0.5.

Do not treat these multipliers as statistical probabilities. They are project prioritization weights.

## What to collect next to reduce uncertainty

Highest information-gain work:

1. current pilot count for Air Seoul;
2. direct pilot counts for the larger estimated cohorts: SKY group, Nouvelair, CemAir, Emerald, DAT, Bulgaria Air;
3. exact CrewConnex export formats enabled at Jeju Air and Air Seoul;
4. representative CrewConnex CSV/HTML samples from more than one airline;
5. whether PDC's PDF export produces stable structure across airline configurations;
6. current CrewConnex confirmation for Clic Air and Parata Air;
7. airline-level active crew accounts if publicly disclosed.

## Stop rule

Do not tighten a pilot band merely because a narrower number looks more useful.

Tighten only when:

- a direct current headcount is found;
- a reliable dated workforce split is found;
- a verified operating fleet/base schedule materially constrains the range; or
- a comparable airline with the same aircraft/operating model provides a transferable direct staffing ratio and the transfer assumptions are explicit.
