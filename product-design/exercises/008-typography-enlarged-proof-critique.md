# Exercise 008 Critique — Typography IA Enlarged-Text Proof

Status: CRITIQUE COMPLETE / real platform text-scaling validation still required for foundation PASS.

Related artifact: `product-design/exercises/008-typography-enlarged-proof.svg`

Research basis: `research/009-typography-as-information-architecture.md`

Primary-source baseline:
- Apple, Scaling Fonts Automatically: https://developer.apple.com/documentation/uikit/scaling-fonts-automatically
- Apple HIG, Lists and tables: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables
- WCAG 2.2 Understanding 1.4.10 Reflow: https://www.w3.org/WAI/WCAG22/Understanding/reflow.html

## Test

The same expense content is rendered as:
1. a normal reference;
2. a deliberately failed enlarged version that scales roles while preserving the original table geometry;
3. a revised enlarged composition that changes hierarchy and row geometry.

## Failure observed

The failed enlarged version preserves too much of the normal layout. This causes:
- the primary value to consume excessive vertical space;
- support facts to wrap into an awkward mixed line;
- fixed table slots to become fragile;
- row identity, metadata, and amount to compete horizontally;
- pressure to compress or truncate content.

The important failure is structural: larger text exposes that the original horizontal allocation was conditional on available width and font metrics.

## Revision

### KEEP
- primary amount remains the first major financial answer;
- action remains a separate control role;
- merchant and amount stay visually associated;
- amounts retain a stable comparative edge where feasible.

### REWORK
- display-size differentiation is reduced so the primary value does not monopolize the viewport;
- budget facts become separate readable lines;
- the dense table becomes stacked rows;
- date/category metadata moves under the merchant instead of occupying fixed columns.

### REJECT
- preserving the original table geometry as an identity requirement;
- shrinking text to rescue the desktop arrangement;
- truncating merchant identity before changing composition.

## Second-context transfer

The appointment-summary transfer demonstrates that typographic roles are semantic, not token names. Date/time is the primary operational value, while location and preparation stay visually close because they are action-critical. They must not be demoted simply because another product labeled similar text as metadata.

## Cross-context conclusion

The transferable method is:

**define semantic roles → enlarge text → observe broken relationships → reduce unnecessary scale contrast → change geometry → verify associations again.**

A typography system is robust when semantic relationships survive role scaling, not when the original coordinates survive.

## Remaining evidence before PASS

- implement with a real scalable system font and platform text-scaling mechanism;
- test multiple accessibility sizes and actual wrapping;
- verify no horizontal scrolling is required for the intended content region where WCAG reflow applies;
- repeat with a longer merchant name and longer localized appointment labels.

## Status implication

`Typography as information architecture` remains **CRITIQUE**. The required failure → revision cycle now exists, but device/platform validation is still missing.