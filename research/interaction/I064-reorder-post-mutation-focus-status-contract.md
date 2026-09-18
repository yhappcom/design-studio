# I064 — Reorder Post-Mutation Focus & Status Contract

Date: 2026-09-18
State: PRACTICE / TRANSFER VALIDATION

## Question
I063 established outcome equivalence across drag, non-drag pointer and keyboard reorder paths. The next gap is temporal: after an item moves, does the user retain an intelligible interaction locus and receive truthful confirmation without an unexpected focus jump?

## SOURCE
WCAG 2.2 remains the accessibility baseline. SC 2.5.7 requires a single-pointer non-drag alternative for dragging functionality unless dragging is essential. SC 2.4.7 requires visible keyboard focus; SC 2.4.11 requires focused components not be entirely obscured by author-created content. W3C supplemental cognitive guidance also recommends that controls/content not move unexpectedly unless movement is user initiated.

Sources:
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p01-unexpected-movement/

## PRACTICE — post-mutation state oracle
For initial semantic order S and requested move M, record:
1. focused semantic item before action;
2. resulting semantic order S′;
3. focused semantic item after action;
4. visible focus geometry and obstruction;
5. available next actions at the new boundary position;
6. status/announcement payload;
7. whether scrolling changed and why;
8. whether another item accidentally acquired focus.

Acceptance position: the moved semantic item should ordinarily remain the interaction locus after a discrete Move earlier/later command. A DOM/list-index change must not silently transfer focus to the item that inherited the old index. If implementation constraints require another policy, it must be explicit, repeatable and task-defensible.

Boundary attempts are separate states. Requesting Move earlier on the first item or Move later on the last item must not mutate order, fabricate success, or silently wrap.

## CRITIQUE
A reorder control can satisfy I063 final-order equivalence yet remain operationally poor if every mutation returns focus to the list start, loses focus, hides the focused control behind a sticky region, or provides no perceivable confirmation. Conversely, an announcement such as “Moved” is insufficient if it omits the object or new relational position.

## REPRODUCIBLE VALIDATION
Run each vector twice for drag, non-drag pointer and keyboard where applicable:
- middle item → earlier;
- middle item → later;
- first item → earlier boundary;
- last item → later boundary;
- move across a group boundary where allowed;
- hidden-neighbor condition;
- 200% text/zoom with scrolling required.

Record semantic IDs, not English labels, as the state oracle. Human comprehension of announcements remains OPEN.

## RELATED DOMAIN CHECK
- Type: T045 protects full action/status strings; no typographic compression is authorized.
- Color: C076 separates focus, boundary-disabled and visibility states.
- Layout: L067 compares reorder-control architectures under density/target pressure.
- Web: W076 requires focus/accessibility-name/runtime evidence per scenario.
- Content: CD082 owns action/status wording and semantic IDs.

This is an extension of I063, not a repetition: I063 proves outcome equivalence; I064 tests continuity after mutation.

## HANDOFFS TO OTHER SPECIALISTS
Layout should preserve a stable visible interaction locus after movement. Color must keep post-move focus distinguishable from selection/visibility. Content should specify object + consequence/position semantics without using text as state. Web should capture active element/accessibility identity before and after mutation.

## OPEN
Actual non-drag reorder implementation; browser/AT announcement behavior; touch/physical-device behavior; representative-pilot discoverability and workload.