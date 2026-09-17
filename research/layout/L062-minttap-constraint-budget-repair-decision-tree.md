# L062 — MintTap Constraint-Budget Repair Decision Tree

Date: 2026-09-18
Purpose: **TRANSFER VALIDATION / REPAIR PRACTICE**
Stage: Stage 3 PRACTICE.

## QUESTION
How should the known compact overflow be repaired without pixel shaving, Type compression or semantic deletion?

## SOURCE
W3C Reflow requires content to remain usable without loss of information/functionality under constrained presentation, with exceptions only where two-dimensional layout is essential.

- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/#1410-reflow-aa

Flutter's accessibility guidance requires layouts to accommodate increased font sizes and recommends testing small screens at the largest font setting.

- https://docs.flutter.dev/ui/accessibility/ui-design-and-styling

## PRACTICE — measurable constraint budget
Before changing structure, capture the exact failing RenderFlex and calculate:

`usable_width = viewport - safe_area - leading - actions - toolbar_padding`

Then measure every title claimant independently: wordmark, secondary badge/metadata, gaps, action reservations and any hidden minimum constraints. Repeat at baseline and enlarged text.

### Repair decision tree
1. **Wrong claimant identified?** Stop and localize the actual failing RenderFlex.
2. **Non-semantic fixed spacing consumes reserve?** Remove/reduce only that spacing and rerun.
3. **Secondary metadata competes with primary identity/action?** Recompose metadata to a second line/region or conditional disclosure without deleting its meaning.
4. **Primary text needs flexible allocation?** Use bounded Flexible/Expanded behavior with explicit overflow policy; verify semantics/read order.
5. **Content still cannot fit?** Move to Wrap/vertical recomposition or evidence-based breakpoint.
6. **Only solution is font compression or semantic deletion?** Reject and hand back to Type/Content.

## ACCEPTANCE MATRIX
Same build identity must cover:
- compact baseline;
- compact enlarged text;
- long localized/portfolio strings;
- large signed KRW/USD values;
- partial/unavailable and estimated/final states;
- 1024×768 workflow;
- focus/target geometry after recomposition.

For each scenario record overflow, clipping, horizontal scroll, semantic order, focus order, target geometry and changed claimant widths.

## CRITIQUE
A repair that turns 9.3 px overflow into 0 px only at one fixture is not closure. The 47 px enlarged-text failure shows the system must be recomposed under changed intrinsic content size. Breakpoints should emerge from content/constraint failure, not device folklore.

## RELATED DOMAIN CHECK
- Type: T040 prohibits font/kerning width compensation without Type-owned evidence.
- Color: C071 requires state surfaces/focus to remain visible after recomposition.
- Layout/Interaction: L061 measurement protocol reused; I057 recovery must remain reachable.
- Web: W070 requires same-build widget smoke before browser promotion.
- Content: CD076 protected semantics must survive layout repair.
- UX: spatial pass does not prove discoverability/workload/usability.

## HANDOFFS TO OTHER SPECIALISTS
Web receives exact breakpoint/constraint evidence rather than device labels. Content receives any proposed abbreviation for semantic classification. Interaction receives changed focus/target geometry for behavioral regression.

## EVIDENCE BOUNDARY
This is an executable decision tree, not evidence that the product repair has been implemented. Existing EXECUTED-FAIL remains authoritative until a new run supersedes it.
