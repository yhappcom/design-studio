# Exercise 001 Critique — Accessibility Geometry Is Composition

Status: PRACTICE / REWORK REQUIRED

Related specimen:
- `product-design/exercises/001-accessibility-geometry.svg`

Research basis:
- `research/004-accessibility-reflow-targets-focus.md`

## Intent

Test whether accessibility can be represented as composition geometry rather than a post-design checklist.

The exercise deliberately separates:

- visible control mark from hit target;
- wide composition from narrow reflow;
- visual hierarchy from fixed spatial arrangement;
- drag gesture from semantic reorder action;
- ordinary responsive content from a justified two-dimensional table exception.

## A — visible mark ≠ target

### KEEP

The wide composition keeps the visible `⋮` mark small while showing a 44px interaction envelope. This correctly demonstrates that premium restraint does not require undersized hit regions.

The specimen also separates two adjacent actions enough to make accidental activation less likely.

### REWORK

The 44px value is a studio exercise choice, not a cross-platform universal law. The reusable lesson is the separation of visible and interactive geometry, plus validation against the relevant platform and accessibility standard.

## B — narrow reflow

### KEEP

The narrow state does not simply scale down the wide state. Supporting metadata wraps, actions move to a dedicated row, and the primary object remains visually dominant.

This demonstrates an important foundation principle:

**responsive composition preserves semantic hierarchy while allowing spatial hierarchy to change.**

### REWORK

The specimen is static and does not yet test:

- 200–400% zoom behavior;
- long localization strings;
- large accessibility text settings;
- keyboard traversal after reordering.

Therefore this is practice evidence, not reflow mastery.

## C — focus and layers

### KEEP

The focus indicator is visible, has dedicated geometry, and remains unobscured by the shown overlay.

This correctly treats focus as a positional information channel.

### REWORK

The SVG does not prove contrast numerically and does not model actual scroll/overlay behavior. A browser/native prototype is required before PASS.

The next exercise must include:

- sticky header covering risk;
- modal/sheet state;
- focus moving into and back out of an overlay;
- at least one failure state where focus becomes obscured, followed by correction.

## D — drag + explicit alternative

### KEEP

The reorder list provides `Move Up`, `Move Down`, and a drag handle. The semantic result — ordering — is not tied exclusively to a drag gesture.

### REWORK

The up/down glyphs need accessible labels and keyboard semantics in an actual implementation. The static drawing proves interaction concept only.

## E — two-dimensional layout exception

### KEEP

The exercise makes the exception local to the dense table rather than using it as justification for the entire screen.

That is consistent with WCAG reflow guidance: some content may require two-dimensional layout for meaning/function while surrounding content can still reflow.

### REWORK

A real table prototype should test:

- sticky column/header behavior;
- cell text zoom/reflow;
- keyboard access across both axes;
- whether a narrow alternative representation can answer common tasks without forcing the full table.

## What this exercise proves

It supports advancement of `Accessibility foundations` from `IN STUDY` to **PRACTICE** because source study now has an original composition artifact and critique.

It also provides initial practice evidence for `Interaction foundations`, specifically:

- target/action separation;
- alternate operation;
- focus as state feedback;
- responsive relocation without semantic loss.

However `Interaction foundations` should move only to **IN STUDY** or early PRACTICE after broader affordance, mapping, consistency, recognition/recall, status, and error-prevention work exists.

## Next required work

1. interactive/browser prototype of target, focus, and reorder behaviors;
2. large-text / 320-equivalent stress test;
3. one explicit failure → correction sequence;
4. affordance/feedback/mapping study beyond accessibility mechanics;
5. keyboard and screen-reader semantics in a production-like prototype.

## Transfer lesson

The strongest transferable finding is:

**accessibility constraints often improve composition when they are treated as structural inputs early — target envelopes create functional negative space, reflow clarifies semantic grouping, and focus creates an explicit state hierarchy.**
