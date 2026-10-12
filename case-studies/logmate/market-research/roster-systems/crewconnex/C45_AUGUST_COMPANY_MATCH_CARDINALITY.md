# C45 — August Skia/company partial-key cardinality gate (2026-10-12)

## Read-only provenance
- Product authority: `yhappcom/logmate/AGENTS.md`, `MASTER.md`, `docs/specs/import-contract.md`, `docs/specs/crewconnex-parser-plan.md`; FlightRecord, SourceEvidence, CrewParticipant, LocalDate, FlightIdentifier and tests reviewed.
- Existing private August Skia PDF blob SHA: `29ac040595089188a8353e98f41ba27f92b8650b`; 2026 company XLSX blob SHA: `a716dc090b1692320d819b3c8e1f5aa3095b4c7f`. Both inspected in connector memory only. No source bytes, crew names/IDs, private flight identifiers, route strings or raw rows transferred.
- Distinct source objects: August Skia PDF is not the separate PDC-generator August PDF. Company XLSX is 159 data rows; no additional source independence claimed.

## New aggregate evidence
- Skia ToUnicode: 1,872 decoded Tj text operations, zero unmapped glyphs. Tagged tree: 48 TR overall, including 34 on page 1 (one header + 33 body), nine primary body TR on page 2 (through MCID 310), and five post-Sum auxiliary TR (MCID >= 340). The Sum barrier begins after the primary body at MCID 311.
- The 42 primary body rows contain 22 ASCII three/four-digit Activity candidates; C44 already classified four rows (13, 19, 20, 21). This cycle classified the other **18** against the full 159-row company 2026 workbook using **7C-only numeric-suffix normalization + exact three-letter departure/arrival**.
- Per-roster-row company partial-key candidate multiplicity: **5 with zero, 3 with one, 6 with two, 4 with three**; thus 13/18 have at least one flight+route partial-key overlap, but 10/18 have multiple company candidates.
- Date TD/text: **12/18 explicit yearless date; 6/18 omitted**. Among the nine explicit-date rows with a company partial-key hit, **2 have a month/day overlap under the unproven assumption that the PDF date is in 2026; 7 have no such overlap**. These are conditional cross-checks, not date-verified matches. Four of 18 rows participate in repeated Skia flight+route keys.
- All 18 rows retain Remark text; BLH text is present on 12 and Pairing text on 11. A populated field is not semantic validation.
- C44's four target rows remain separate: their earlier partial-key counts were 0/0/0/1. Do not merge these with the 18-row histogram or count the one overlap as a date-verified match.

## ParserProfile consequence
- A 7C flight-number/route partial key is **candidate discovery only**; even multiplicity one is not a clear match without an independently grounded year/date and validated row/section provenance.
- Preserve zero/one/many candidate cardinality, explicit-vs-omitted date state, repeated roster key, source page/TR/MCID, and review reason. Unknown year, duplicate company candidates, omitted Date, revision ambiguity and nonflight barrier are review-only; never forward-fill date or crew.
- CrewConnex remains existing-record-only crew snapshot/BLH evidence. Zero FlightRecord creation, automatic crew attachment, BLH/Block overwrite, or inferred PIC/SIC/PF/PM/duty semantics. Internal private PDFs are **not public P1**; public grade P2, production parser OPEN.
- This was a read-only independent analysis, not LogMate CI or production parser PASS.

## Next single CrewConnex target
Independently establish the August Skia PDF's export-period/year linkage (or explicitly exhaust it), then rerun date-aware one-to-one matching for the two conditional month/day overlaps and the ten multi-candidate rows, retaining snapshot/revision ambiguity.
