# I089 — LogMate import schema mapping provenance and ambiguity

Status: **STAGE 3 PRACTICE / TRANSFER DESIGN — runtime OPEN**

## Question
After I088 separates file→parser→duplicate→preview→transaction, what prevents source-field mapping from silently changing the meaning of professional flight records?

## RELATED DOMAIN CHECK
- Type: T021 remains the drawing gate; T070 supplies import strings. Mapping UI must use mature fallback and must not compress provisional glyphs.
- Color: C101 separates classification/resolution states; mapping confidence/ambiguity must not be collapsed into error/success color.
- Layout/Interaction: I088/L092 provide batch authority and geometry; I089 extends the authority chain before normalization.
- Web: W101 separates file-read/parser/transaction provenance; W102 must preserve raw header/value→mapping-rule→normalized-field provenance.
- Content: CD107 separates parsed/validated/classified/imported; CD108 must name source field, target meaning and unresolved ambiguity without inventing certainty.

Purpose of overlap: **TRANSFER VALIDATION** from generic import preview to professional schema mapping.

## SOURCE
1. WCAG 2.2 is the studio accessibility baseline; W3C recommends use of the latest WCAG 2 version. https://www.w3.org/WAI/standards-guidelines/wcag/
2. W3C form guidance ties clear instructions and labels to SC 1.3.1, 2.4.6, 3.3.2 and 4.1.2; mapping controls therefore require understandable labels/relationships, not color or column position alone. https://www.w3.org/WAI/tutorials/forms/instructions/
3. RFC 4180 documents common CSV syntax and explicitly notes that CSV has varied interpretations; the optional `header` parameter may be absent, requiring implementations to decide whether a header exists. It does **not** define aviation semantics for a header such as `Time`, `Block`, `PIC`, or `Role`. https://www.rfc-editor.org/rfc/rfc4180

## SYNTHESIS — authority chain
`raw file bytes → decoded rows → source/header detection → source-field identity → proposed target mapping → mapping confidence/provenance → user resolution where ambiguous → normalized field → record validation → duplicate classification → preview → commit`

None of these arrows is identity.

### Critical professional rule
A syntactically valid column is not a semantically known column. LogMate must not infer domain equivalence merely because values look compatible.

Examples that remain **OPEN/UNMAPPED unless the source contract proves them**:
- `Block` → `Flight Time`;
- `Block` → `PIC`;
- `Captain` → logged `PIC` time;
- `Night` → instrument/IFR;
- `From/To` → DEP/ARR if the source uses a different concept;
- decimal-looking duration → hours without source/unit evidence.

This deliberately preserves the earlier CrewConnex rule: missing professional meaning is not manufactured during import.

## PRACTICE — deterministic mapping fixture
Use one 12-column source with:
- 5 exact documented mappings;
- 2 aliases with source-specific mapping rules;
- 2 syntactically valid but semantically ambiguous fields;
- 1 unknown field;
- 1 unit-ambiguous duration;
- 1 source field intentionally excluded by user.

For each field record:
`sourceSystem, sourceVersion, rawHeader, rawSampleHash, parserVersion, mappingRuleId/version, proposedTarget, confidenceClass, userResolution, normalizedTarget, unitTransform, exclusionReason`.

Confidence classes are product semantics, not probabilities unless an actual calibrated probabilistic model exists:
- `documented_exact`;
- `source_rule_alias`;
- `ambiguous_needs_review`;
- `unknown_unmapped`;
- `user_excluded`.

## CRITIQUE / failure conditions
FAIL if any of the following occurs:
- normalization happens before mapping provenance is inspectable;
- ambiguous mapping is silently auto-accepted;
- a label or color implies confidence not supported by the source contract;
- source header and normalized target cannot be traced after preview;
- user changes mapping but stale normalized values remain;
- remapping one field does not invalidate dependent validation/duplicate/preview results;
- exclusion is represented as parse failure;
- source-system detection alone is treated as proof of every field meaning.

## Reproducible validation
Run each executable family twice with the same fixture hash:
1. exact documented mapping;
2. ambiguous mapping left unresolved;
3. ambiguous mapping resolved by user;
4. target remapped after preview generation;
5. source unit changed/declared;
6. field excluded;
7. Back/Forward/reload before commit;
8. 200% reflow;
9. independent engine and forced colors when served runtime exists.

Assert that mapping changes invalidate all downstream artifacts whose inputs changed: normalized-record hash, validation result, duplicate result, preview hash and proposed transaction.

## UX integration
Information architecture should expose **Source → Maps to → Status/why → sample/value consequence → action**. Progressive disclosure may hide technical provenance by default, but must not hide unresolved semantic ambiguity needed for safe action.

Non-human analysis can verify traceability, state transitions, geometry and accessible relationships. It cannot prove that pilots understand mapping labels, confidence, or consequences; comprehension/workload remain **OPEN** until human validation.

## HANDOFFS TO OTHER SPECIALISTS
- Color: encode mapping status without equating ambiguity with error.
- Layout: preserve source/target/status/action relationships at 200% and narrow widths.
- Content: define source-vs-target language and uncertainty/recovery semantics.
- Web: capture mapping-rule/version and invalidation provenance in served runtime.
- Type: stress raw headers, filenames, identifiers and EN/KO labels only after T021 drawing/spacing gates permit.

## Evidence boundary
No parser-source contract, real LogMate mapping runtime, cross-browser/device, AT, or human comprehension PASS is claimed.