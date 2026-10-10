# C24 synthetic PDC detector gate — 2026-10-11

64/64 PASS: 16 detached-review cases, 48 unsupported-layout cases. Header Blk Hrs x492 and right-aligned body x511 are deliberately distinct. No actual PDF parser or LogMate CI ran. Zero record creation, crew attachment, BLH overwrite or date inheritance. Public P2; production OPEN.

Next: real second PDC-generator report-family/header/body/footer validation.

Fixture scope: synthetic 14 ordered header anchors, 49 row bands (26 numeric: eight 3-digit and eighteen 4-digit; 22 nonnumeric; one remark-only), 598x842 page, footer outside body. Wrong generator/report family, shifted or missing headers, invalid body field/locator, nonnumeric route/Pairing/clocks, malformed remark and footer contamination fail closed. Coordinate tolerances are synthetic, not production-calibrated.

Sync debt: writes to `crewconnex/PDF_PRINT_GEOMETRY.md`, `RESEARCH_LOG.md`, `MASTER_SYSTEM_INDEX.csv`, `FIELD_COVERAGE_MATRIX.csv`, `REVALIDATION_QUEUE.md` were blocked with `This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.` Retry after fresh fetch. `PARSER_SAMPLE_INDEX.csv` commit `7dda0d8cefd9214bef04063a3e390340db0c8237` verified. LogMate unchanged.
