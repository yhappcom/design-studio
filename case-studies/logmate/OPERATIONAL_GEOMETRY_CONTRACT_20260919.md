# LogMate Operational Geometry Contract — 2026-09-19

Status: **PHASE 4 COMPLETE — PRE-CONCEPT GEOMETRY CONTRACT / PRODUCTION METRICS PARTLY OPEN**

Upstream authority:
- `INTEGRATION_PRINCIPLES_20260919.md`
- `DESIGN_CORRIDOR_20260919.md`
- audited Evidence Map / Contradiction Register
- LogMate MASTER / UI contract / configuration contract / visual restart

Purpose: define which spatial and typographic relationships a new LogMate concept must preserve before aesthetic review. This document does not choose final fonts, palette, radii, exact Home spacing, or final navigation destinations.

---

# 1. Geometry hierarchy

Operational geometry is resolved in this order:

1. semantic identity;
2. local comparison axis / column boundary;
3. text and data metrics;
4. target/focus/recovery geometry;
5. responsive recomposition;
6. decorative alignment.

A lower layer may not move a higher layer merely to improve appearance.

**Stable geometry means stable semantic relationships, not identical absolute coordinates across screens.**

---

# 2. Typography-to-geometry roles

## General UI

Use proportional UI typography as the geometry control for:
- labels;
- section titles;
- actions;
- navigation labels;
- helper/error/recovery copy;
- ordinary product-authored prose.

Exact family/weights remain OPEN unless already fixed by a product contract.

## Operational mono role

Use an exact mature mono family in production for confirmed operational-data roles, including:
- repeated Home Flight identifier;
- repeated Activity Flight identifier where Flight rows exist;
- View Logbook body operational values under the existing contract.

Generic Flutter `fontFamily: 'monospace'` is not the production geometry authority.

## Arbitrary user/source text

Remark and other arbitrary user/source free text:
- may contain any language/script;
- must use a fallback-safe proportional/text role unless independently justified otherwise;
- must not inherit the operational mono contract merely because it appears inside a ledger row;
- must preserve platform text shaping and bidirectional behavior rather than being split into fixed Latin character cells.

Exact overflow/wrap/full-value interaction for Remark remains surface-specific and OPEN where not already specified.

---

# 3. Flight identifier contract

Semantic structure:

`[2-character carrier] [1–4 digit flight number + optional 1-character suffix]`

Geometry:

- carrier zone has a stable start;
- number/suffix zone has a separate stable start;
- mono operational glyph advances stabilize the content inside each zone;
- variable total string length does not move either semantic start;
- the combined Flight string is **not** whole-string centered;
- equal per-character fixed cells are prohibited.

OPEN:
- exact mono family;
- exact carrier-zone width;
- exact inter-zone gap;
- exact value box width per surface.

Validation corpus must include wide/narrow carrier glyphs, 1/2/3/4-digit numbers, suffix/no-suffix and ambiguity-critical glyphs.

---

# 4. Date geometry

Canonical presentation is numeric and locale-ordered through the product DateFormats contract.

Rules:
- do not tune a visual column to textual fixtures such as `Sep 02`;
- preserve one local comparison axis for repeated dates;
- budget against supported numeric ordering/format outputs;
- date presentation and UI language are separate.

OPEN:
- exact per-surface date width;
- exact large-text date adaptation.

H3 remains active until canonical formatter outputs are measured in the actual production type stack.

---

# 5. Duration and cumulative-value geometry

Confirmed formatting:
- ordinary duration: `H+MM`;
- cumulative ledger capacity must support at least `99,999+59`.

Rules:
- comparison values preserve a stable local numeric axis;
- View Logbook duration columns follow their confirmed shared semantic boundaries;
- proportional summary metrics may use tabular figures when the selected family supports them;
- do not disable stable numeric features solely to save width;
- width is budgeted after the production feature/family is active.

No global rule requires every duration everywhere to use monospace.

---

# 6. View Logbook normal-presentation contract

The following are preserved from the confirmed product contract:

- LogMate Standard leaf order:
  `Date | Type | Reg | Flight | DEP | ARR | Block | Night | Inst | Remark`;
- compact ledger is LEFT/START anchored after its outer content padding;
- selected semantic column widths sum to the ledger width;
- the ledger does not stretch columns merely to fill surplus viewport width;
- when selected semantic width exceeds available content width, controlled horizontal scrolling is allowed;
- header, body and totals share the same horizontal offset;
- header/body/totals share the same semantic column boundaries;
- column header remains sticky during vertical ledger scrolling;
- normal header/body/total rhythm is 36 logical px;
- body remains regular mono/code at w400;
- header / Page Total / Previous Total remain w500;
- New Total remains w600;
- totals use the same neutral-background family rather than a special brand fill;
- duration totals align with their corresponding duration columns.

The visual reset may change visual finish inside those contracts. It may not silently delete them.

## Enlarged text

The 36px normal rhythm does **not** prove 200% behavior.

At enlarged text:
- do not shrink text to preserve 36px;
- recompose/expand/scroll according to semantic need;
- preserve column meaning and access to content.

Exact large-text ledger mode remains H2 OPEN.

---

# 7. Home geometry contract

Home retains these semantic families:
- identity/header;
- primary actions;
- Search;
- Current Period;
- Recent;
- Activity;
- Totals.

Current Period remains Block Time.

The next concept is **not** required to preserve the prior candidate's exact track ratios, card geometry, radii, spacing or section styling.

## Repeated operational rows

When Home shows repeated flight rows:
- Date / Flight / DEP / ARR operational values use the confirmed stable operational treatment;
- Flight retains internal zoning;
- comparable row values keep local axes;
- section redesign may move the entire region but must not reintroduce row-to-row jitter.

## Bottom-navigation region

The next Home concept should include a bottom-navigation region as an owner-preferred composition default.

Geometry requirements:
- it must not overlap or obscure scrollable Home content;
- safe-area/inset behavior must be accommodated in implementation;
- the content layout must remain viable if final NAV-001 later changes destinations or app-wide persistence;
- the nav region itself is not an operational-data comparison axis.

OPEN:
- destination count;
- destination identity;
- exact height;
- icon/label treatment;
- persistent vs route-specific use outside Home.

---

# 8. Activity geometry contract

Semantic periods:
- 7 days;
- 28 days;
- 90 days;
- Custom.

Current concept work may use those labels directly without repeated `Last`.

Rules:
- selected/unselected state must remain distinguishable without relying solely on color;
- period labels belong to one comparison/control family;
- future shared-prefix treatment such as a single `Last` may be explored later if it improves economy without changing semantics;
- Activity Detail repeated Flight rows inherit the operational Flight treatment when present.

No exact segment width or visual tab grammar is fixed by this contract.

---

# 9. Add Flight geometry contract

Preserve the confirmed task semantics while replacing the superseded stock card/Material visual treatment.

Confirmed interaction geometry already in product authority:
- ordinary Add Flight input visual height: 40 logical px;
- Takeoffs/Landings counter: 48 logical px;
- `Show/Hide details` and `Add crew member`: minimum 44 logical px touch targets;
- Departure/Arrival remain a two-column read-only display pair that opens dedicated airport search.

Rules:
- forms reflow normally; they do not inherit the dense-ledger horizontal-scroll exception;
- hidden optional fields retain their data/controller state according to the product contract;
- validation/recovery geometry must remain visible even in a low-chrome treatment.

Exact new visual surface composition remains open for later concept work.

---

# 10. Target, focus and state geometry

Visible glyph/icon size and interactive target size are separate.

Any future concept must:
- preserve usable target geometry;
- show focus position;
- keep invalid/ambiguous/recovery ownership local to the relevant control or transaction;
- ensure state remains understandable when authored colors are removed;
- preserve semantic equivalence across supported input methods.

Drag/reorder is not complete geometry until the required non-drag single-pointer alternative exists.

---

# 11. Responsive and scale rules

## Normal responsive behavior

May change:
- region widths;
- wrapping;
- section composition;
- number of simultaneous columns outside fixed product contracts;
- local grouping realization.

Must preserve:
- semantic order;
- comparison axes within the active region;
- focus/target/recovery ownership;
- protected professional terminology.

## Enlarged text / text spacing

Preferred response order:
1. allocate more space;
2. wrap where semantics allow;
3. recompose region;
4. expose controlled scrolling where two-dimensional meaning requires it;
5. only use established governed abbreviation where already valid.

Do not:
- shrink below the intended accessible size;
- apply negative tracking;
- invent abbreviation;
- force all text into operational mono.

---

# 12. Operational stress matrix

Before a whole-screen concept can pass geometry review, stress at minimum:

| Family | Required stress |
|---|---|
| Flight | wide/narrow carriers; 1–4 digits; suffix/no suffix; ambiguity glyphs |
| Date | all supported canonical numeric locale orderings |
| Airport/Route | realistic long/wide code combinations and route relationships |
| Registration | realistic short/long operational registrations from supported data |
| Duration | short and long H+MM values |
| Cumulative | at least 99,999+59 |
| Remark | long Latin, Korean/CJK and other Unicode/script text; mixed user/source content |
| UI copy | canonical English labels, warning/recovery strings |
| Scale | baseline + enlarged text/text spacing |
| State | focus, selected, invalid/ambiguous, recovery, reduced motion/forced colors as applicable |

The arbitrary-language Remark stress is not a multilingual product-UI requirement.

---

# 13. Geometry failure conditions

A concept fails this gate if it:

- reintroduces visible Flight/date/route/duration jitter;
- uses whole-string Flight centering;
- restores fixed per-character cells;
- freezes global coordinates to solve a local comparison problem;
- crushes ledger columns to avoid legitimate horizontal scrolling;
- shortens professional strings merely to fit;
- treats Remark as fixed-width English-only content;
- allows bottom navigation to obscure Home content;
- sacrifices focus/target/recovery geometry for visual cleanliness;
- claims 200% or native/PWA success without runtime evidence.

---

# 14. OPEN items retained

- H1 exact production mono family/weights/fallback;
- H2 large-text dense-ledger adaptation;
- H3 locale-date width budget;
- H4 cross-surface signature transfer evidence;
- H5 runtime evidence;
- H6 final NAV-001 semantics;
- H7 SEARCH-001;
- exact Home spatial metrics;
- exact production type scale outside confirmed contracts.

---

# 15. Gate result

**Operational Geometry Contract: COMPLETE for pre-concept use.**

It provides enough invariants to reject unstable visual concepts without pretending the remaining production metrics are known.

Next allowed phase:
`Signature Code Study`

Still prohibited:
- new UI concept drawing before the Signature Code Study is complete.
