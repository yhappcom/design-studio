# Exercise 007 Critique — Responsive Grid Transfer

Status: CRITIQUE COMPLETE / additional multilingual and large-text evidence still required for foundation PASS.

Related artifact: `product-design/exercises/007-grid-responsive-transfer.svg`

Research basis: `research/006-grid-composition-hierarchy.md`

## Question

Can the strongest structure from Exercise 003 survive a narrow format and an unrelated content category without being reduced to proportional scaling?

## Wide → narrow archive test

### KEEP
- dominant total retains the primary left datum;
- latest-item duration retains a stable right edge, preserving comparison potential;
- major section order remains context → primary total → support → latest;
- whitespace continues to separate semantic groups.

### REWORK
- three support columns cannot survive at 330 px without damaging label legibility;
- support facts therefore recompose as a 2 + 1 group;
- latest metadata becomes two lines rather than one compressed line.

### REJECT
- scaling the desktop grid proportionally;
- preserving column count for its own sake;
- shrinking type to save the original coordinates.

The intentionally compressed control fails because labels collide, groups lose separation, and the latest-record line becomes a dense unparsed string. This is a geometry failure, not a font-selection failure.

## Semantic vs disposable alignment

Semantic alignments:
- primary content left edge;
- right edge for the duration/value when comparison benefits from it;
- section starts that encode reading order.

Disposable at the breakpoint:
- exact support-column count;
- exact inter-column positions;
- one-line metadata composition.

This distinction is the core transferable finding: a responsive grid preserves relationships, not coordinates.

## Second context — editorial article

The method was transferred to a low-density editorial article with title, dek, metadata, and a key finding. The content does not reuse the archive's visual pattern, but it uses the same reasoning procedure:

1. identify the title/reading sequence;
2. identify alignments that encode relationships;
3. collapse columns when width changes;
4. preserve semantic grouping through space and type roles.

The editorial narrow version loses the side-by-side key-finding relation because that relation is not essential at the small width. It preserves the title, metadata, divider, and finding order.

## Failure analysis

The failed compressed control is useful evidence. It shows why a grid should not be treated as a fixed coordinate template. Its failure modes are:
- crowded labels;
- reduced scan chunking;
- ambiguous grouping;
- pressure to reduce text size;
- false visual continuity with the wide layout.

## Cross-context conclusion

The transferable method is:

**define semantic edges → define reading order → identify disposable columns → recompose at the breakpoint → critique lost relationships.**

This is not evidence for asymmetry as a universal style. The archive and editorial examples differ in density and task, yet the method remains valid.

## Remaining evidence before PASS

- repeat with long/multilingual labels;
- test enlarged text in the narrow format;
- verify at least one interactive or real-browser implementation where actual font metrics and wrapping can be observed.

## Status implication

Evidence is now sufficient to move `Composition / visual grammar` and `Grid / alignment systems` from **PRACTICE** to **CRITIQUE**, but not to PASS.