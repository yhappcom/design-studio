# L061 — Compact width-budget localization and responsive recomposition protocol

## Purpose
Turn the observed compact overflow into a causal, measurable repair procedure instead of trial-and-error pixel shaving.

## Stage
Stage 3 PRACTICE / NOT PASSED. TRANSFER VALIDATION of the MintTap compact shell.

## Known evidence
Prior runtime evidence detected horizontal overflow at compact baseline and substantially larger overflow under 2× text scaling. Source inspection identified the compact AppBar title cluster (wordmark + spacing + PRODUCT LAB badge) competing with actions/trailing space as a high-probability source. Source inspection alone does not prove it is the failing RenderFlex.

## PRACTICE — width-budget localization
For the exact failing viewport, record the RenderFlex stack and calculate the horizontal budget:

`available width = viewport - safe area - leading - actions - toolbar paddings`

Then measure each title-cluster claimant:
- wordmark intrinsic width;
- fixed gaps;
- badge intrinsic/min width;
- action widths and hit targets;
- any titleSpacing/navigation defaults;
- scaling/localization expansion.

Repeat at baseline and 2× text scaling. The repair target is the competing structure, not the reported overflow magnitude.

## Responsive recomposition candidates
Evaluate in this order, preserving semantics and target geometry:
1. allow flexible allocation where semantics permit;
2. remove non-semantic fixed spacing;
3. move secondary badge/meta content to a second line or alternate compact slot;
4. use Wrap/vertical recomposition when the title cluster cannot coexist horizontally;
5. use breakpoint-specific composition only when intrinsic-content evidence justifies it.

Do not solve by shrinking font, reducing target size, deleting semantic qualifiers, or clipping.

## CRITIQUE
A repair fails if any of the following occurs:
- baseline overflow merely becomes <1 px without structural margin;
- 2× scaling reintroduces overflow/clipping;
- action targets shrink below accepted geometry;
- reading/focus order diverges from visual order;
- badge/qualifier meaning disappears;
- long localization or signed/large currency values break the repaired composition;
- wide/tablet layout regresses.

## Reproducible validation matrix
Required: compact baseline; compact 2× text scale; long localized strings; signed/large KRW/USD; partial/unavailable and estimated/final qualifiers; wide/tablet. Record viewport, scale, locale, scenario ID, build SHA, overflow/assertion log and screenshots.

## Accessibility boundary
WCAG 2.2 is the Web accessibility baseline. Automated geometry can test clipping/reflow/focus visibility conditions but does not establish human comprehension or cognitive workload.

## RELATED DOMAIN CHECK
Type: no kerning/font compression workaround. Content: no semantic deletion. Interaction: preserve targets/focus/activation. Color: preserve visible state surfaces. Web: promote only after same-build widget regression and served-browser evidence.

## Next evidence
The next product run must first capture the exact failing RenderFlex stack. If the AppBar candidate is confirmed, implement structural recomposition and rerun the full matrix; if not, apply this same width-budget procedure to the actual stack.