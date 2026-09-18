# CD083 — Reorder Position Feedback Language

Date: 2026-09-18
State: STAGE 3 PRACTICE / CONTENT-SYSTEM TRANSFER

## Problem
CD082 defined action language. I064 adds a consequence-language requirement: after a discrete reorder mutation, the interface needs enough semantic feedback to identify what moved and what changed without making English text the state machine.

## SOURCE
WCAG 2.2 is the accessibility baseline; W3C guidance emphasizes operability through different inputs and visible/unobscured focus. W3C supplemental cognitive guidance advises against unexpected movement not initiated by the user. These sources do not prescribe one reorder sentence; wording remains a Content design decision constrained by truthful product state.

Sources:
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p01-unexpected-movement/

## Semantic contract
State payload, not rendered English, should provide:
- `field_semantic_id`;
- `move_result` = moved | boundary_no_change | rejected;
- `new_index` and `total_visible` where meaningful;
- optional `relative_neighbor_semantic_id`;
- group context when movement changes/approaches a group boundary.

Locale realization may then choose a compact equivalent such as object + new position, or object + relational consequence. The product must not infer state by parsing “Moved”, “Up”, or translated strings.

## PRACTICE corpus
Stress with aviation labels from CD081/CD082: DEP, ARR, Aircraft Type, Registration, Block, Actual, PIC, SIC/FO, PICUS, SPIC, Instrument Flight Time, Actual Instrument, Simulated Instrument, T/O, L/D. Include first/last boundaries, hidden neighbors, group boundaries, and 35 visible fields.

Compare three semantic strategies without declaring human preference:
A. absolute position: object + “position n of N”;
B. relational: object + “before/after [neighbor]”;
C. hybrid: concise visible feedback plus richer accessibility/status payload.

## CRITIQUE
“Moved” is too weak because the object/consequence is absent. “Moved up” is visually directional and may become brittle under alternate writing/layout directions. “Position 7 of 35” is precise but can be verbose and cognitively noisy after repeated operations. Neighbor-relative language may be professionally meaningful but depends on stable, correctly localized field names. The correct production strategy therefore requires runtime and later human/AT evidence.

## Localization gate
Keep semantic IDs and numeric variables typed. Do not concatenate fragments whose grammatical order is assumed to transfer. Test long translations, reordered grammar, plural/number formatting where applicable, and bidirectional/layout-direction conditions before production PASS.

## RELATED DOMAIN CHECK
Type T045 owns rendering pressure. Color C076 owns visible focus/boundary cues. Layout L068 owns mutation geometry. Interaction I064 owns actual move/focus state. Web W076 owns runtime accessibility-name/status evidence.

## HANDOFFS TO OTHER SPECIALISTS
Interaction should expose structured move-result payloads. Web should verify rendered/accessibility feedback derives from those payloads. Layout must reserve for truthful feedback rather than forcing semantic deletion. Type should test the selected localized corpus only after wording is semantically defensible.

## OPEN
No multilingual production run, linguistic review, screen-reader announcement validation or representative-pilot comprehension evidence exists yet.