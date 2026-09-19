# LogMate Home Candidate 04 — Coordinator Gate — 2026-09-20

Status: **OWNER-REVIEW ELIGIBLE / STATIC CONCEPT ONLY / RUNTIME OPEN**

## Isolation

Generation inputs:
- structural restore point `f992d62a98193629d19346a022a64deef824570c`;
- canonical `MASTER.md`, `ui-contract.md`, DateFormats and current product fixtures;
- owner-wide directions;
- current assets;
- Design Studio Integration Principles / Design Corridor / Operational Geometry Contract / Signature Code Study.

Excluded:
- Candidate 01 render/rationale/composition;
- rejected Candidate 02 and Candidate 03 render/rationale/composition;
- Round-1 A/B/C visual geometry.

Result: **ISOLATION PASS**.

## Implementation / render provenance

Flutter branch:
`design/home-candidate-04-code-20260920`

Initial implementation:
`ca5f95ba32d499db4b41a8800400aaef20f5341f`

Corrected implementation:
`c696e5a6d473949f1a9c7f8c88c31dceb7cb7030`

Canonical-literal test update:
`80100bc0d58ecec15748823a9bbf8b331c9d0068`

GitHub Actions run:
`35474977405`

The Actions run failed before runner steps began. No Flutter analyze/test/golden PASS is claimed.

A deterministic 390x844 review render was produced by mirroring the implemented geometry/tokens into a static render harness. It is static visual evidence only.

## Candidate thesis

**Route Journal**

Home gives the most visual weight to the user's recent flight routes rather than to dashboard containers or aggregate tiles.

Hierarchy:
1. identity;
2. Search;
3. equal Add flight / View logbook primary actions;
4. compact Current Period / Block Time band;
5. Recent route journal as the main operational field;
6. Activity horizontal analysis band;
7. Totals horizontal summary band.

Key expression:
- DEP → ARR is the dominant repeated object;
- Date / Flight / Block remain quieter metadata;
- operational mono stays bounded to repeated flight data;
- summary metrics remain proportional tabular;
- no card stack;
- no bottom navigation;
- no aviation decoration;
- no invented product copy.

## R1 specialist blockers and corrections

R1 blockers:
1. Current Period did not visibly identify Block Time.
2. Add flight received unsupported brand-priority over View logbook.
3. draft literals used Recent Flights / Add Flight / View Logbook instead of current canonical Recent / Add flight / View logbook.

Corrections:
- explicit Block Time label added;
- primary actions equalized to neutral visual hierarchy;
- canonical literals restored.

## Independent R2 specialist results

- Type: PASS FOR OWNER AESTHETIC REVIEW.
- Color: PASS FOR OWNER AESTHETIC REVIEW.
- Layout / Spatial: PASS FOR OWNER AESTHETIC REVIEW.
- Interaction: PASS FOR OWNER AESTHETIC REVIEW.
- Content: PASS FOR OWNER AESTHETIC REVIEW.
- Web / Runtime: PASS FOR OWNER AESTHETIC REVIEW ONLY / RUNTIME PASS PROHIBITED.

No remaining `CHANGES REQUIRED` blocker exists for static owner review.

## Remaining OPEN

Not blockers for static aesthetic review:
- exact production type families/fallback;
- actual Flutter golden/runtime;
- narrow/enlarged/text-spacing;
- coded dark/night/forced colors;
- route/focus/SEARCH-001 runtime;
- accessibility tree/AT;
- physical device/PWA/browser transfer;
- representative-pilot usability and brand perception.

## Verdict

**OWNER-REVIEW ELIGIBLE.**

This does not mean:
- preferred direction;
- production baseline;
- production-ready UI;
- Masterpiece;
- superiority over sealed Candidate 01.

Candidate 01 remains sealed until after Candidate 04 owner review.
