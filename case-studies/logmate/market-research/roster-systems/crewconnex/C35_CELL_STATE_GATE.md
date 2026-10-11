# C35 — Skia PDF cell-state evidence (2026-10-11)

Read-only structural and text-layer analysis of the existing June and July PDF references. No source values retained.

| Metric | June | July |
|---|---:|---:|
| Body rows | 40 | 44 |
| Emp./CC cells | 40 / 40 | 44 / 44 |
| Pos. cells | 32 | 44 |
| Emp./CC rendered lines | 121 / 121 | 118 / 118 |
| Pos. rendered lines | 90 | 118 |
| Literal pipe triplets | 16 | 16 |
| Pos. literal hyphen lines | 0 | 20 |
| Three-column baseline alignment | 32/32 | 44/44 |

June page-2 first row: 24 Emp./CC lines and absent Pos. cell. July page-2 first row: six aligned lines in all three columns. Distinguish absent cells, whitespace, pipe, hyphen and other text. No participant inference, record creation or automatic reconciliation. Public P2; production OPEN.

Next: August 31-column Skia cell-state replication.

## Additional validation and unresolved decisions

ToUnicode/MCID audit: June 1,824 and July 1,921 decoded text operations, with no unmapped glyphs or unowned text objects; 1,555 primary tagged MCID leaves per month. Emp./CC decoded line states (other text / pipe / whitespace): June 103/16/2 each; July 99/16/3 each. Pos. (other text / pipe / hyphen / whitespace): June 72/16/0/2; July 79/16/20/3. These are rendered text-line counts, **not participant counts**. Exact pipe and hyphen meaning, repeated-value ancestry, participant identity and operating status remain unverified. This is internal source evidence, not a public raw P1 sample or production-parser PASS.

## Synchronization debt

2026-10-11: `FIELD_COVERAGE_MATRIX.csv` updated successfully. Writes to `MASTER_SYSTEM_INDEX.csv`, `PARSER_SAMPLE_INDEX.csv`, `REVALIDATION_QUEUE.md`, `RESEARCH_LOG.md`, and `crewconnex/PDF_PRINT_GEOMETRY.md` were blocked. Each returned exactly: `This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.` Retry after fresh fetch on a later run; do not treat this document as replacing the canonical indexes.
