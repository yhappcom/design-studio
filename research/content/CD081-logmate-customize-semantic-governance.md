# CD081 — LogMate Customize Semantic Governance

Date: 2026-09-18
Mode: **TRANSFER VALIDATION + SYSTEMS PRACTICE**
Stage: 3 PRACTICE / NOT PASSED

## Question
How should Customize language preserve professional logbook meaning when users alter presentation but never redefine underlying record semantics?

## SOURCE
LogMate's current configuration contract establishes a 35-item Known Field catalog, renderer-owned compact headers, four system Field Groups, immediate presentation changes, and strict separation between display-column configuration and Add Flight entry fields. Known Fields cannot be renamed in V1. Hiding a column never deletes its value. Route is a presentation group over distinct Departure and Arrival semantics, not a stored Route value. Type and Registration remain separate. Block, Actual, Instrument Flight Time, IFR Time, Actual Instrument and Simulated Instrument remain distinct semantics.

## SEMANTIC GOVERNANCE MODEL
For every catalog item maintain:

`semantic_id → full semantic name → Customize label → compact ledger header → group membership → value type → total eligibility → localization notes`

The visible string never selects the semantic ID. A localized label may change wording while preserving identity.

Protected distinctions include:
- Hide ≠ delete;
- Reset presentation ≠ erase data;
- Route group ≠ a canonical Route value;
- Type ≠ Registration;
- Block ≠ Actual;
- Instrument Flight Time ≠ IFR Time ≠ Actual Instrument ≠ Simulated Instrument;
- display column ≠ entry field;
- system Field Group ≠ user-created Custom Field.

## PRACTICE — complete content-system stress
Test the same catalog through:
1. Standard first-use with no configuration explanation required;
2. Customize entry and SHOWN/HIDDEN organization;
3. turning a field OFF and later ON;
4. reorder and position feedback;
5. Reset to Standard;
6. unavailable Custom Field creation entry point while disabled;
7. future persistence/offline/sync conflict messaging;
8. localization where compact header and full label need different realizations.

## CONTENT CRITIQUE
`Customize` is appropriate only if the surface clearly communicates presentation control. Terms such as Delete column, Remove data, Save changes, Cancel changes or Template can contradict the actual V1 behavior. Conversely, excessively technical explanations of projection metadata would increase cognitive load. The system should reveal the destructive/non-destructive boundary at the action where confusion is plausible, especially Reset and Hide.

Compact aviation abbreviations (`DEP`, `ARR`, `Reg`, `Inst`, `PIC`, `SIC/FO`, `PF/PM`) are domain-facing labels, not evidence that every locale should mechanically abbreviate the English expansion. Localization needs a per-field compact-label contract and expert/domain review where aviation terminology is regulated or conventional.

## REPRODUCIBLE VALIDATION
A localization/content QA ledger should compare semantic IDs rather than English strings. For each locale and state capture: source ID, full label, compact header, group identity, action wording, accessibility name, visible result after toggle/reorder/reset, and history/persistence message when implemented.

Automated string/key checks can establish structural continuity. They cannot establish pilot comprehension, trust or linguistic quality.

## RELATED DOMAIN CHECK
- **Type:** compact labels are legitimate strings and should stress metrics rather than be shortened ad hoc for geometry.
- **Color:** SHOWN/HIDDEN and state changes must remain understandable without color.
- **Layout/Interaction:** immediate changes and Reset semantics determine wording truth.
- **Web:** browser localization and accessibility-name output are transfer evidence.
- **UX:** professional workflow requires fast recognition of familiar aviation terms without semantic collapse.

## HANDOFFS TO OTHER SPECIALISTS
Interaction must preserve the actual immediate-change/Reset contract. Type receives protected strings for fit tests. Web receives semantic IDs for locale/runtime assertions. Color receives non-color state-language requirements. Layout receives full-label/compact-header dual-string pressure.

## OPEN
Actual multilingual runtime, localization resource architecture for the catalog, professional linguistic review, AT comprehension and representative-pilot task evidence.

## Conclusion
CD081 advances the complete content system from auth-state semantics into professional ledger configuration. Stage 3 remains open until semantic identity survives real localization/runtime and human/domain review.