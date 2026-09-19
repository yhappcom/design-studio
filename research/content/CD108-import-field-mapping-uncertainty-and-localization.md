# CD108 — Import field mapping, uncertainty and localization

Status: **STAGE 3 PRACTICE / production linguistic evidence OPEN**

## RELATED DOMAIN CHECK
I089 owns actual mapping/provenance; L093 owns geometry; C102 owns visual state encoding; W102 owns browser/runtime provenance; T021/T070 own glyph/rendering constraints. This extends CD107 by **TRANSFER VALIDATION** from duplicate resolution to schema meaning.

## SOURCE
W3C guidance requires clear labels/instructions and programmatic relationships for forms; descriptive labels should make control purpose clear. https://www.w3.org/WAI/tutorials/forms/instructions/ and https://www.w3.org/WAI/WCAG22/Techniques/general/G131
RFC 4180 defines common CSV syntax but not domain semantics for column names. https://www.rfc-editor.org/rfc/rfc4180

## Content contract
Keep these concepts distinct:
`source label ≠ target concept ≠ mapping rationale ≠ uncertainty ≠ validation result ≠ import result`.

Recommended content architecture, not frozen copy:
- Source field: preserve literal source header/value where safe.
- Maps to: canonical LogMate field name.
- Why/status: documented mapping / source rule / needs review / unmapped / excluded.
- Consequence: what will happen if accepted.
- Recovery/action: change mapping, exclude, return to review.

Never translate or normalize professional identifiers as if they were prose. Locale realization may translate interface labels, but source headers and typed aviation identifiers need provenance-preserving display.

## PRACTICE corpus
Stress EN/KO with:
- `Block Time`, `Flight Time`, `PIC`, `SIC`, `Night`, `Instrument`, `IFR`, `DEP`, `ARR`;
- unknown headers;
- long source-system labels;
- unit ambiguity (`1:30`, `1.5`, minutes/hours when source contract is unknown);
- exact and possible mapping rationales;
- exclude/change/review actions;
- batch summary with unresolved count.

## CRITIQUE / FAIL
- wording claims semantic certainty from a syntactic match;
- `Mapped` is used when mapping still requires review;
- `Invalid` is used for a valid but unknown/unmapped field;
- translated target terminology overwrites literal source evidence;
- source and target use the same label without role/context, hiding the distinction;
- concise mobile wording deletes consequence/recovery truth;
- English string equality is used as product logic.

## Reproducible validation
Static checks: complete string inventory, typed variables, source-vs-interface localization flags, unresolved-count reconciliation, no color-only references. Runtime checks later: EN/KO at baseline/200%, visible and accessibility payload, focus association, independent engine. Linguistic review and human comprehension remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Type receives exact stress corpus; Layout receives minimum semantic units that may not be dropped; Color receives wording-independent state identities; Web receives localization/provenance flags and runtime assertions.

## Evidence boundary
No professional-linguist, pilot-comprehension, AT, production multilingual or runtime PASS is claimed.