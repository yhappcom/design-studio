# L058 — Compact Recomposition Repair Contract

Evidence class: **SOURCE + SYNTHESIS + TRANSFER VALIDATION PLAN**

## QUESTION
After L057 found 9.3 px baseline and 47 px enlarged-text horizontal overflow at 390×844, what repair preserves semantic content and Type integrity while making the compact composition robust?

## SOURCE
W3C WCAG 2.2 remains the studio accessibility baseline. WCAG 1.4.4 requires text resize to 200%; 1.4.10 requires reflow without loss of information/functionality under its normative conditions. WAI also explicitly describes larger text and small viewports as conditions where content should reflow rather than lose information.

## PRACTICE — repair order
1. Localize the exact overflowing RenderFlex/group before changing dimensions.
2. Preserve Content truth-bearing strings and Type metrics.
3. Remove avoidable fixed-width competition first.
4. Permit nonessential identity/status chrome to move to a second line/region before truncating task content.
5. Replace a single rigid horizontal group with bounded Wrap/Flex/vertical recomposition when the available width crosses the content-fit threshold.
6. Preserve reading order, semantic adjacency and target geometry after recomposition.
7. Re-run both 390×844 baseline and 2.0-scale stress; a baseline-only fix is insufficient.

## CRITIQUE
A 9.3 px baseline overflow proves the composition has no reserve even before accessibility stress. A repair that merely absorbs 9.3 px is fragile because L057 already demonstrates a much larger 47 px pressure at 2.0 scale. Shrinking typography, tightening tracking/kerning, deleting qualifiers, or clipping are rejected because they move a Layout defect into Type or Content.

## REPRODUCIBLE VALIDATION
For the same build/scenario identity record: viewport, text scale, locale/currency fixture, exact offending widget path, overflow count/extent, screenshot, protected-group reading order, target bounds, and Flutter exceptions. Acceptance requires zero unintended horizontal overflow in both compact scenarios and no semantic loss introduced by the repair.

## RELATED DOMAIN CHECK
- Type: T035 classifies current failure as composition pressure; T021 drawing→spacing→kerning remains protected.
- Color: C066 requires visible semantic/feedback surfaces after recomposition.
- Interaction: I053 requires Material feedback and workflow continuity.
- Web: W066 owns runtime identity and browser transfer after widget smoke.
- Content: CD072 forbids deleting financial semantics to make geometry fit.

## HANDOFFS TO OTHER SPECIALISTS
Type should classify post-repair wrapping/raster effects only after L058 passes geometry. Interaction must verify focus/target/order after structural recomposition. Web should preserve identical scenarios for regression comparison. Content must review any proposed abbreviation as a semantic change, not a layout implementation detail.

## OPEN
Exact source widget localization and repaired runtime evidence remain open. Human usability, AT and physical-device evidence are not inferred.