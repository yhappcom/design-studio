# C27 — year provenance / duplicate-leg matching gate (synthetic only)

Date: 2026-10-11 15:02 KST. Scope: CrewConnex existing-record-only enrichment and BLH cross-check. **43/43 synthetic cases PASS** (5 CLEAR_MATCH review candidates, 31 AMBIGUOUS_MATCH, 5 UNMATCHED, 1 EXCLUDED_NON_FLIGHT, 1 UNSUPPORTED_LAYOUT). This is a standalone research oracle, **not** LogMate code, a real Skia/PDC detector, a production import test, or a parser-readiness promotion.

## Source and authority

Read-only current LogMate `AGENTS.md`, `MASTER.md`, import and CrewConnex specs, `flight_record.dart`, `crew_participant.dart`, `source_evidence.dart`, `source_evidence_history.dart`, `flight_identifier.dart`, `local_date.dart`, source-evidence test and record-domain spec. Reused existing LogMate 2026-08 Skia/PDC + 2026 company XLSX *metadata* and the Design Studio C24/C25/C26 findings; no private rows or source binaries were copied. C26 measured 22 Skia numeric Activity candidates, 12 explicit yearless dates, 10 omitted dates, two repeated flight+route keys, and two conditional month/day+flight+route company overlaps with minute-equal BLH/bt. These remain **source-to-source observations**, not canonical matches.

## Decision-gate proposal for future ParserProfile / review engine

1. `UNSUPPORTED_LAYOUT` when report-family/detector/required-field validation fails; `EXCLUDED_NON_FLIGHT` for nonflight activities. Both yield zero candidates and zero writes.
2. `AMBIGUOUS_MATCH` when the year is missing without **independently validated** source-period evidence. Filename, PDF CreationDate, inferred company year, or the mere presence of one company match are **not** year authority. Yearless month/day with hypothetical independently validated year was tested as a *conditional* positive; **not validated in the real Skia corpus**.
3. An omitted Date, even beside a dated numeric row, remains ambiguous until a real profile validates same-duty lineage. A nonflight/Remark/Sum/page/source barrier prohibits inheritance; a synthetic antecedent flag does not override this.
4. Require verified airline-specific `7C` normalization (raw retained), full date, complete flight identifier, exact departure and arrival, valid BLH syntax, and a single roster-source observation per version before considering a canonical review candidate. Unsupported carriers/suffixes or missing fields remain unresolved. Do not use BLH as identity proof.
5. One exact canonical date+flight+route record **and no competing ±1-day same-flight/route candidate** is `CLEAR_MATCH` **for review only**. Two canonical records with the same composite key, competing adjacent-day records, duplicated roster keys or unresolved cross-snapshot revision identity remain `AMBIGUOUS_MATCH`. Same-day partial-key conflicts also remain ambiguous.
6. With a complete validated key and no exact, ±1-day or same-day partial-key candidate, `UNMATCHED` means no existing record candidate; it never creates a FlightRecord. A BLH-versus-canonical-Block difference retains the unique review candidate but requires explicit conflict review.
7. Matching is a detached staging classification. Current `SourceEvidence` is record-bound, so **no record-bound evidence or crew snapshot is constructed before owner review/record selection**. No FlightRecord create/update, crew attachment, BLH overwrite, date correction, revision ordering, PIC/SIC/PF/PM inference, or source merge.

## Synthetic regression coverage

43 named scenarios cover: exact unique; yearless with absent, unverified, verified and incorrect independent year; omitted Date with/without an antecedent flag and with nonflight barrier; two/three canonical duplicate keys; exact plus one/two ±1-day alternatives; ±1-day-only; route/flight partial conflicts; complete unmatched and other-year unmatched; duplicate same-snapshot or cross-snapshot source keys; BLH conflict, invalid/missing BLH; missing/invalid route; nonflight and unsupported layout; non-ASCII, 2/5-digit and suffix Activity; unverified/other carrier; invalid dates; `7C0125` and all-zero suffix; unsupported company identifier. Every case asserted **zero canonical mutations and zero record-bound evidence attachments**. A first-run oracle expectation for a malformed company identifier was corrected to ambiguous partial-key conflict; final rerun passed 43/43. All identifiers, routes and records in the oracle are synthetic.

**Boundary:** these are conservative proposed review-gate semantics, not product-approved matching thresholds. Exact duplicate composite keys and confidence thresholds remain OPEN in LogMate import contract. Public CrewConnex corpus grade **P2**; production parser **OPEN**.

## Next single CrewConnex target

Validate **independent operational-year provenance for the real 2026 Skia printer PDF** (print header/export UI versus filename/PDF CreationDate) and whether its omitted-Date same-duty antecedent is explicitly represented. If neither is available, keep all yearless/omitted-date rows review-only and specify a fail-closed year-confirmation UX. Do not revisit a twice-exhausted public revision-token search.
