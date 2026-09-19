# CD112 — LogMate Large-Text Ledger Content Integrity

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION — no gate promotion**

## PURPOSE
Define which content may recompose under enlarged-text ledger adaptation and which semantic payload must remain invariant.

## RELATED DOMAIN CHECK
Type T075, Color C106, Interaction I093, Layout L097 and Web W105 checked. Current WCAG 2.2 Reflow/Text Spacing guidance supports adaptation but does not authorize loss of information/function.

## CONTENT INVARIANTS
The following are protected when moving between table, hybrid and detail representations:
- canonical record values;
- field identity;
- professional identifier boundaries;
- state/action/consequence/recovery truth;
- validation/ambiguity distinctions;
- sort/filter meaning;
- source/user text availability.

Placement, grouping, visible labels and disclosure depth may change when the semantic relationship remains programmatically and visually recoverable.

## PRACTICE — ABBREVIATION POLICY
Do not abbreviate merely to preserve compact geometry. A shortened form is acceptable only when it is established professional vocabulary or an explicit product term and does not create ambiguity. Airport identifiers, operational role labels and duration notation remain governed by their actual domain contracts. User/source Remark text is never rewritten for fit.

Ellipsis is a presentation state, not a content state. If used, the complete content must remain available through an in-context mechanism consistent with the interaction contract.

## CROSS-REPRESENTATION STRING SET
Validate the same semantic payload in:
1. column header + cell;
2. compact row + disclosure;
3. labeled detail field;
4. validation/error state;
5. recovery/Undo state;
6. empty/loading/partial state where applicable.

A representation fails if it changes `invalid` into generic `issue`, hides the affected field, drops the object from a destructive action, or claims Saved/Synced without implementation truth.

## CRITIQUE
Large-text pressure often produces premature abbreviation and label removal. This can make a concept look cleaner while increasing inference cost. Semantic economy means removing redundancy, not removing the semantic job. The content system therefore yields space through recomposition/disclosure before meaning reduction.

## SYNTHESIS
Content integrity is the invariant that lets Layout change representation safely. If a compact table and a detail view expose the same product truth with stable terminology and action consequences, they can be different surface realizations of one content system.

## OPEN
- Representative-pilot comprehension of compact vs disclosed labels.
- Linguistic review of final production strings.
- Runtime/AT reading-order evidence.
- Exact product decisions for locale-date presentation and some professional abbreviations.

## HANDOFFS TO OTHER SPECIALISTS
- Layout/Web: recompose before shortening protected strings.
- Type: use the full stress corpus; do not tune metrics to shortened fixtures.
- Interaction: disclosure/detail must preserve action and recovery ownership.
