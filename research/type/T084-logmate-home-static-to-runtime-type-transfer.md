# T084 — LogMate Home static→runtime Type transfer

Date: 2026-09-20
Purpose: **TRANSFER VALIDATION / PROJECT APPLICATION**
Upstream: T021, T083, `case-studies/logmate/HOME_WHITE_CANVAS_DRAFT_01_REVIEW_20260920.md`.

## RELATED DOMAIN CHECK
- Type: T021 drawing gate and T083 acceptance oracle remain authoritative.
- Color: C114 requires semantic salience to survive actual rendering.
- Layout/Interaction: I101/L105 protect semantic relationships rather than static coordinates.
- Web: W114 requires actual resolved-font/runtime provenance.
- Content: CD120 protects canonical strings from fit-driven semantic shortening.
- Reuse: the new Home draft supplies a concrete product fixture; this study does not reopen signature theory.

## SOURCE / PROJECT EVIDENCE
The latest Home draft explicitly assigns proportional UI voice to labels/actions/section titles, operational mono only to confirmed comparison data, and fallback-safe proportional treatment to arbitrary-language Remark. It also forbids geometry dependence on unfinished custom Type.

## PRACTICE — concrete fixture map
Static fixture strings are partitioned before rendering:
- proportional UI: `Current Period`, `Recent Flights`, `Activity`, `Totals`, `Settings`, `Search logbook`, `Add Flight`, `View Logbook`, `7 days`, `28 days`, `90 days`, `Custom`;
- operational comparison candidates: flight identifiers `7C 132`, `7C 1123`, `KE 28`; repeated duration/value fields `42+15`, `318+40`, `1+12`, `1+08`, `1+10`, `6+48`, `1,284+35`, `842+10`, `1,163+55` only where comparison stability is actually required;
- date strings remain representation-sensitive and must not be used to freeze provisional custom metrics.

## CRITIQUE / falsifiers
FAIL if the rendered concept:
1. uses unfinished T021 custom glyphs to establish final Home geometry;
2. applies mono globally for an “aviation” look;
3. shortens canonical labels solely to preserve one-line geometry;
4. uses negative tracking, glyph narrowing or kerning to hide unfinished drawing/general-spacing defects;
5. records only intended CSS/font-family rather than actual resolved family/fallback in runtime evidence.

## Reproducible validation contract
For the first coded Home implementation, capture the same fixture at baseline, enlarged text, WCAG text-spacing override and forced fallback. Record resolved family, size/weight, line boxes, wraps/truncation and the protected comparison geometry. Compare mature proportional baseline with exact mature mono candidate only for confirmed operational roles.

## Gate decision
No T021 drawing or spacing gate changes. This project transfer adds a concrete downstream falsification fixture but cannot authorize kerning or custom-font production use.

## HANDOFFS TO OTHER SPECIALISTS
- Layout/Web: do not freeze rails/columns around provisional T021 metrics.
- Content: preserve canonical strings; hand fit failures back to Type/Layout before rewriting.
- Color: evaluate state salience with actual resolved font/fallback, not design-tool assumptions.

## OPEN
Actual coded Home render, resolved production font stack, enlarged/text-spacing/fallback evidence, native/browser transfer, human recognition.