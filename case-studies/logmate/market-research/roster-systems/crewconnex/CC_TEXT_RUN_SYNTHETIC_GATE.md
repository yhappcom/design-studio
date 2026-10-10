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


## 2026-10-10 15:01 KST — C13–C16 executed synthetic multi-baseline gate

C13–C16 wholly synthetic multi-baseline oracle: 15/15 PASS. Two/three independent CC baselines at 14 or 28 synthetic units stage separate unlinked display candidates; missing/shifted/duplicate Emp./Pos. baselines, wrong page, non-CC mixed objects, shifted CC grid, split MCID, swapped font order and near-overlap fail closed. Distinct MCIDs BETWEEN baselines are permitted; Type3/Type0 fragments WITHIN a baseline must share tagged TD+MCID. All cases: 0 participants, 0 snapshot attachments, 0 FlightRecords. Synthetic epsilon=0.05 and CC X=824.5 are not production-calibrated; no actual Skia detector or LogMate CI was run. P2/public and production OPEN; existing-record-only.

| Case | Structural condition | Detached decision |
| --- | --- | --- |
| C13 | Same tagged CC TD, two/three distinct Y baselines, gap 14 synthetic units | Stage 2/3 **separate** display candidates; no identity or attachment |
| C14 | Same TD, two baselines, gap 28 | Stage 2 separate candidates, never concatenate baselines |
| C15 | Emp./CC/Pos. cardinality, Y, page or row disagreement | REVIEW; zero participant/snapshot creation |
| C16 | Mixed-font fragments in non-CC column, CC X-grid drift, or absent CC | Ignore non-CC as crew; unsupported/review for invalid CC |

Additional negative checks: MCID split within one baseline, glyph order swap, duplicate/overlapping baselines. Crucial distinction: **MCID equality is required within one mixed-origin baseline pair, not between separate baselines of the same TD**. Page-local MCIDs may differ per baseline. The executable research oracle ran 15 tests locally; its synthetic tolerances and generator assumptions are **not** production ParserProfile rules. Existing C1–C9 fixture contract remains in force. Next: validate Emp.#/CC/Pos. baseline cardinality and source-tag ownership for real June/August multi-baseline TD cells without storing personal data.
