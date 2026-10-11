# C38 — CrewConnex Skia tagged-field presence (2026-10-12)

Read-only structural audit of existing June/July/August 2026 Skia PDF references. No private source content retained.

| Metric | June | July | August |
|---|---:|---:|---:|
| Header columns | 34 | 30 | 31 |
| Body rows | 40 | 44 | 42 |
| Date TD present | 30 | 31 | 31 |
| Activity TD present | 40 | 44 | 42 |
| BLH TD present | 40 | 44 | 42 |
| Page-1/page-2 body rows | 34/6 | 38/6 | 33/9 |

Across 126 body rows, Date is structurally absent in 34; Activity and BLH TD are present in all 126. All 3,775 body TDs were mapped to header text-matrix X positions without an unmatched or duplicated assignment. Page-2 first body row has Date/Activity/BLH TD in each month; presence does not prove the date value or authorize forward-fill. June page-2 first body row lacks other columns (18, 28).

This is physical tagged-cell ownership evidence, not verified date semantics, BLH equivalence, roster-year provenance, duty ancestry, or a production parser. Keep all unresolved candidates detached; CrewConnex may only enrich/cross-check an existing FlightRecord after separate matching and review. No FlightRecord creation, automatic crew association, or BLH overwrite. Public sample grade P2; production parser OPEN.

Next target: resolve missing Date TD in flight-like rows against explicit antecedent/barrier and page/section provenance, using redacted synthetic fixtures only for tests.
