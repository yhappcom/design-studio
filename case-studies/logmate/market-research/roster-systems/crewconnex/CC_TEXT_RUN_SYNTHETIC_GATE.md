# CrewConnex CC text-run grouping regression gate — 2026-10-10

Status: research fixture contract only; production parser OPEN. All fixture strings below are synthetic and do not represent a person, employee ID or actual flight.

## Why this gate exists

The read-only July Skia PDF CC column has 130 text objects but only 117 distinct page/Y baselines. Thirteen same-baseline pairs share page, X, Y and MCID. Each pair contains a three-glyph Hangul Type3 text object plus a separate one-character ASCII Menlo text object. The ASCII tokens are not literal `|`. This is a distinct counting unit from the prior 12 affected tagged rows. Separately, 98 of 130 CC text objects have three `Tj` glyph runs within one `BT...ET` object. Neither `Tj` count nor text-object count is a participant count. This document records no original text or identifiers.

## Wholly synthetic cases and expected behavior

| Case | Synthetic CC structure | Expected staging outcome |
| --- | --- | --- |
| C1 | One text object: Type3 glyph runs `가`, `나`, `다` at one Y | Preserve three glyph runs and their order as one *text-object candidate*, not three crew members; full crew identity remains unverified. |
| C2 | Same page/TD/MCID/X/Y: one `가나다` text object and a separate ASCII `Q` object | Preserve two source objects, mark mixed-origin ambiguous; never choose, concatenate, or count as two crew automatically. |
| C3 | Same X/Y, different MCIDs | Keep both locators; do not merge by Y alone; review. |
| C4 | Same MCID but Y differs beyond validated baseline tolerance | Do not merge; require verified row/list alignment. |
| C5 | Same Y but X falls outside anchored CC grid | Unsupported layout; zero automatic enrichment. |
| C6 | A literal `|` as the only CC token, with no verified same-duty antecedent | Review; no crew forward-fill. |
| C7 | `가나다` plus a literal `|` overprinted at the same origin | Mixed-origin ambiguous, not a valid pipe-only sentinel. |
| C8 | Unknown font/ToUnicode mapping or incomplete glyph decode | Fail closed for that crew association; no fabricated name. |
| C9 | Valid-looking CC baseline but missing/misaligned Emp.# or Pos. baseline | Review/unsupported; no participant snapshot attachment. |

Required provenance for detached staging: file fingerprint, generator/profileId/profileVersion, page, primary tagged TR/TD, MCID, source baseline, X grid, text-object ordinal, glyph-run ordinal, font/ToUnicode decode state and unmodified raw token. Never copy actual private roster text into research or CI. If two sources differ in crew snapshot while BLH is equal, preserve both and require explicit reconciliation. No CrewConnex input creates a FlightRecord.

Acceptance: a future redacted/synthetic executable oracle must demonstrate C1–C9 plus multi-page/unknown-layout regressions; this fixture matrix itself is NOT an implementation test PASS. Public sample grade P2 remains unchanged.
