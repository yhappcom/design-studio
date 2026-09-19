# L093 — LogMate import field-mapping review geometry

Status: **STAGE 3 PRACTICE / spatial transfer — rendered runtime OPEN**

## RELATED DOMAIN CHECK
I089 supplies mapping authority; C101 supplies non-color-only state separation; CD108 supplies source/target semantics; T021/T070 constrain rendering; W102 owns browser transfer. This is **TRANSFER VALIDATION**, not a new interaction state machine.

## SOURCE
W3C form instructions connect labels/instructions and programmatic relationships to WCAG 2.2 SC 1.3.1, 2.4.6, 3.3.2 and 4.1.2. https://www.w3.org/WAI/tutorials/forms/instructions/

## Spatial contract
A mapping row must preserve a perceivable relationship among:
`source field → target field → mapping state/reason → representative sample/unit → available action`.

The design must not depend on left-to-right proximity alone; responsive recomposition may stack these elements while preserving reading and focus order.

## PRACTICE matrix
Use I089's 12-column fixture and measure at baseline and 200%:
- exact mapping;
- ambiguous mapping requiring review;
- unknown/unmapped;
- user-excluded;
- unit ambiguity;
- remap after preview;
- long source header/filename;
- EN/KO realization;
- sticky summary/action region.

Capture bounding boxes for source label, target control, state/reason, sample/unit, error/recovery, focus indicator, sticky region and primary action.

## CRITIQUE / FAIL
- source and target become visually interchangeable;
- status is detached from the field it describes;
- a sticky footer/header fully obscures focused mapping control;
- 200% reflow forces horizontal two-dimensional scanning for a simple field mapping where a stacked relationship can preserve meaning;
- unresolved mapping disappears outside a collapsed region while commit remains apparently ready;
- focus order follows CSS visual rearrangement incorrectly;
- long headers cause truncation that removes the distinguishing portion without an accessible full value.

## Reproducible validation
For each scenario, twice: capture viewport, zoom, DOM/semantic order, rectangles, overlap/obscuration, scroll displacement, focus semantic ID and I089 mapping state. Geometry PASS never implies human comprehension PASS.

## HANDOFFS TO OTHER SPECIALISTS
Color receives state adjacency contexts; Content receives actual available space and order; Web receives geometry assertions; Type receives real full strings but must not compensate before T021 closure.

## Evidence boundary
No rendered LogMate mapping screen, 200% runtime, independent-engine, forced-colors, AT or human PASS is claimed.