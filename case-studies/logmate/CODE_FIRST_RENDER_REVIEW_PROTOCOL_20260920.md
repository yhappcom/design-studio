# LogMate Candidate Generation & Review Protocol — 2026-09-20

Status: **OWNER-CONFIRMED / SUPERSEDES EARLIER CANDIDATE-02 PROCESS**

## Core rule

A saved candidate is **not** a design baseline. It is a sealed comparison artifact.

Candidate 01 was preserved so later, genuinely independent directions can be compared against it. It must not influence the generation of those directions.

Candidate 02 is rejected/discarded and must not influence any future generation.

## Generation isolation

Before a new candidate is generated:
- start from `checkpoint/home-structural-baseline-20260919 @ f992d62a98193629d19346a022a64deef824570c`;
- do not inspect prior candidate renders;
- do not reuse prior candidate composition, rationale, spacing, hierarchy or signature details;
- do not ask “how can Candidate 01 be made different?”;
- build from product truth + owner direction + Design Studio foundations + assets + platform/accessibility constraints only.

## Required sequence

`restore point -> isolated code concept -> implementation completion -> code render/golden -> independent specialist reviews -> contradiction resolution -> coordinator synthesis -> owner-review eligibility -> owner review -> optional comparison with sealed Candidate 01`

## Independent specialist review requirement

The actual completed render must be reviewed independently by the relevant specialists:
- Typography / Type Design;
- Color;
- Layout / Spatial;
- Interaction;
- Web/runtime where applicable;
- Content Design.

A coordinator may summarize those opinions only after they exist.

A coordinator applying old specialist principles to a render is **not** equivalent to post-render specialist review.

## Owner visibility gate

Do not present a candidate to the owner merely because:
- code exists;
- a render exists;
- a coordinator critique exists.

Owner review eligibility requires:
1. implementation is sufficiently complete for the concept;
2. code-origin render evidence exists;
3. independent post-render specialist reviews exist;
4. material conflicts are resolved or explicitly OPEN;
5. coordinator synthesis confirms the candidate is coherent enough to review.

Only then is the candidate shown to the owner.

## Rejection handling

If the owner rejects a candidate:
- remove it from the active comparison set;
- keep implementation/history only as archival evidence if useful;
- do not reuse it as a starting point, intermediate step or inspiration source.

## Current candidate roles

### Candidate 01
**SEALED COMPARISON ARTIFACT**
- retained;
- not baseline;
- not preferred direction;
- not generation input;
- reopened only after a new candidate passes the complete pre-owner gate.

### Candidate 02
**REJECTED / DISCARDED**
- not active candidate;
- not generation input;
- not comparison input.

## Evidence correction

The previous `HOME_CANDIDATE_02_POST_RENDER_REVIEW_20260920.md` was a coordinator synthesis against existing specialist criteria. It was not independent specialist post-render review and therefore was insufficient for owner-review promotion.


## Visual-concept-only freeze

Current owner direction: the next LogMate Home candidates are **visual identity concepts on a frozen product structure**, not layout/data alternatives.

Hold constant across candidates:
- same Home information families and order;
- same data fixtures;
- same product semantics;
- same destination/action set;
- same operational comparison geometry.

Variation must come from:
- type character/role expression;
- color atmosphere;
- surface/rule/boundary language;
- control and icon treatment;
- visual density/spacing finish;
- brand-accent behavior;
- state/motion expression.

A candidate that achieves distinctness mainly by reorganizing the Home, changing section priority, moving actions, or changing the data model is out of scope for this phase and must be rejected before owner review.
