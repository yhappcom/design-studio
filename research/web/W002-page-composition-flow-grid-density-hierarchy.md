# W002 — Page Composition, Flow, Grid, Density & Visual Hierarchy

Status: **PRACTICE / CRITIQUE — source-grounded design exercise; browser harness pending**

## Research question

How should a Web designer choose ordinary flow, Flexbox, Grid, bounded sizing, local overflow, or positioning from the **relationship the product must preserve**, rather than from a preferred CSS technique or a reference screenshot?

The goal is project judgment: preserve information priority, comparison relationships, readable flow and valid adaptation under variable content.

## RELATED DOMAIN CHECK

### Type
Checked `progress/TYPE_STATUS.md` through T016. T016 shows that downloadable-font loading/failure can materially change width, wrapping and downstream geometry. W002 therefore treats exact line breaks as runtime outcomes, not stable composition primitives. This is **TRANSFER VALIDATION planning**, not a duplicate Type study.

### Color
Checked `progress/COLOR_STATUS.md`. Color Stage 1 is PASS, but semantic hierarchy cannot be delegated to hue. W002 keeps spatial/source hierarchy legible before chromatic reinforcement.

### Layout / Interaction
Checked `progress/LAYOUT_STATUS.md`. Layout/Interaction Stage 1 is PASS and includes L002 density/rhythm, L003 Type-dependent reflow and L006 ownership evidence. W002 reuses these as canonical peer evidence and asks the Web-specific question: how should those constraints determine complete page composition and implementation choice?

### Web
Checked W001. W001 established relationship-over-coordinate design and demonstrated a fixed-canvas failure against a fluid/intrinsic revision. W002 extends that baseline from “fixed canvas vs resilient page” into a **layout-mechanism decision model**.

### Why overlap is useful
This is **TRANSFER VALIDATION** of Layout and Type findings into Web page architecture. The value is not another CSS summary; it is a decision procedure for project composition.

---

## SOURCE

### CSS Grid
W3C describes CSS Grid as a two-dimensional grid-based layout system optimized for user-interface design. Grid allows children to participate in flexible or fixed row/column tracks; Level 2 adds subgrid so nested grids can participate in parent sizing.

Source checked 2026-09-15: W3C CSS publications / Grid Layout Levels 1–2.

### Flexbox
The CSS Flexible Box model is fundamentally organized around distributing space along an axis. It is appropriate where the primary relationship is a row or column whose items need flexible sizing, alignment, distribution or wrapping.

Source checked 2026-09-15: W3C CSS publications / Flexible Box Layout.

### Reflow
WCAG 2.x Success Criterion 1.4.10 requires content, with stated exceptions for intrinsically two-dimensional content, to be presentable without loss of information/functionality and without two-dimensional scrolling at the equivalent of 320 CSS px width for vertically scrolling content or 256 CSS px height for horizontally scrolling content.

This is an accessibility requirement boundary, **not** a universal mandate that every component must become a single column or that all horizontal overflow is forbidden.

Source checked 2026-09-15: W3C WAI WCAG Reflow guidance.

---

## SYNTHESIS — relationship first, mechanism second

A page can be decomposed into relationship classes:

| Relationship to preserve | Default design mechanism | Why | Warning |
| --- | --- | --- | --- |
| Sequential reading/task flow | ordinary document flow | lets content determine block progression and naturally absorbs text growth | avoid fixed heights that turn content growth into overlap/clipping |
| One-axis action/control group | Flexbox or ordinary inline/block flow | alignment/distribution is primarily one-dimensional | wrapping may change grouping; verify priority and reading order |
| Two-axis comparison/alignment | Grid or semantic table where data is tabular | columns/rows share alignment relationships | do not use CSS Grid as a substitute for table semantics when the information is actually tabular |
| Repeating cards with flexible count | Grid `repeat()`/`minmax()` or wrapping Flex depending alignment need | lets available space determine count while retaining minimum useful measure | card count is an outcome, not the product goal |
| Full-bleed region with constrained readable content | outer full-width region + inner bounded measure | separates background/surface extent from content measure | do not force all page regions to one universal max-width |
| Intrinsically 2-D artifact | explicit local overflow/zoom/pan/recomposition | preserves meaning that may be destroyed by forced stacking | contain overflow locally; do not make the entire document horizontally scroll |
| Overlay/anchored transient UI | positioning/top-layer mechanism after ownership is defined | relationship is to an anchor/layer, not normal document progression | visual position does not prove focus/pointer/semantic ownership; reuse L006 |

### Decision rule

Do not ask “Should this page use Grid or Flexbox?” first.

Ask:

1. What information/task relationship must survive?
2. Is that relationship sequential, one-dimensional, two-dimensional, anchored, or intrinsically spatial?
3. Which content can grow, wrap, localize, disappear, load late, or fail?
4. Which alignments are semantic and which are merely decorative?
5. What may recompose, and what must remain simultaneously comparable?
6. Is overflow a failure, or is local two-dimensional navigation intrinsic to the content?
7. Only then choose flow/Flex/Grid/positioning/overflow and constraints.

---

## Original exercise — three page compositions for the same product content

Scenario: an investment-tracking web page contains a title/summary, primary action, four KPI values, a distribution-history chart, explanatory copy and a transaction list.

The exercise deliberately produces multiple viable compositions instead of one “best” layout.

### Direction A — sequential editorial

- summary and action in normal flow;
- KPI values in a wrapping group;
- chart full content-column width;
- explanation follows chart;
- transaction list follows explanation.

**KEEP when:** comprehension and progressive reading dominate; mobile/narrow transfer is high priority.

**REWORK when:** users need simultaneous chart/list comparison.

**REJECT when:** core task requires persistent cross-panel comparison and repeated scanning between data regions.

### Direction B — comparison workspace

- bounded page grid;
- summary/action span page width;
- chart and transaction region occupy coordinated columns when space supports simultaneous comparison;
- below the stress threshold, the regions return to sequential source order rather than shrinking indefinitely.

**KEEP when:** comparison between chart and records is a primary task and sufficient inline space exists.

**REWORK when:** localized labels or text scaling cause either column to lose useful measure.

**REJECT when:** the side-by-side relationship is decorative rather than task-critical.

### Direction C — data-dense desktop with local 2-D preservation

- summary compact;
- KPI strip remains one-axis and may wrap;
- chart remains responsive;
- genuinely tabular transaction data preserves column relationships inside a local scroll region instead of converting every row into cards.

**KEEP when:** expert users need column comparison and the table meaning is genuinely two-dimensional.

**REWORK when:** the local scroll container hides essential row/column context or keyboard/focus behavior is poor.

**REJECT when:** the content is actually a list of independent records whose labels can recompose without loss.

### Selected default

For a general-purpose tracker, **Direction B** is the preferred starting point because it preserves a strong desktop comparison mode while permitting semantic sequential recomposition. Direction A is the lower-complexity fallback. Direction C is reserved for data surfaces where two-dimensional comparison is itself part of the task.

This selection is a **STUDIO JUDGMENT**, not an empirical user-performance result.

---

## Density and hierarchy model

W002 rejects two shortcuts:

- `more whitespace = better design`;
- `more visible information = better productivity`.

Instead, density is allocated by task frequency, comparison need, error cost, content variability and input constraints.

### Hierarchy layers

1. **Page identity / current context** — where am I and what object/time range am I viewing?
2. **Primary task/action** — what is the highest-value next action?
3. **Decision data** — what values or states change the user's decision?
4. **Supporting explanation/metadata** — what resolves ambiguity?
5. **Secondary/administrative actions** — available without competing with the primary path.

Spacing, alignment, grouping, type and color should reinforce this hierarchy together. None is a sole semantic channel.

### Rhythm rule

Use repeated spacing relationships to reveal grouping, but allow intentional breaks when a new semantic region begins. A spacing scale is a production aid; it does not replace optical or semantic judgment.

---

## Failure → revision patterns

### Failure 1 — fixed equal columns
A 50/50 split is retained because the reference image looked balanced.

**Revision:** size tracks from task/content constraints. A dense comparison region may need more measure than explanatory copy; at a stress threshold, recompose rather than continue proportional shrinkage.

### Failure 2 — breakpoint by device label
“Tablet = 768px” becomes the reason for a layout switch.

**Revision:** place the switch where the actual content relationship fails: label collision, unusable measure, action wrapping that destroys priority, or comparison columns becoming ineffective.

### Failure 3 — cards as universal responsive solution
A table is converted into independent cards merely to eliminate horizontal scrolling.

**Revision:** first classify whether cross-row/column comparison is semantically important. Preserve genuine two-dimensional data relationships with appropriate table semantics and bounded local overflow/recomposition.

### Failure 4 — visual reordering breaks logical order
Grid placement produces a visually attractive order different from source/focus sequence.

**Revision:** make source order express the meaningful reading/task order; use visual placement only where it does not create contradictory navigation or interpretation.

### Failure 5 — preferred-font-only composition
A heading/action row is tuned to one font and one language.

**Revision:** treat font loading/fallback and long Korean/English strings as composition states; leave geometric slack or define a valid recomposition rule.

---

## Project-readiness contract

Before approving a Web page composition, record:

- primary user task and comparison requirement;
- semantic/source order;
- relationship class for each major region;
- chosen layout mechanism and rejected alternatives;
- minimum useful measure or stress condition, not just named-device breakpoints;
- what can wrap/reorder/stack and what must remain aligned;
- local-overflow exceptions and why they are semantically justified;
- long/localized content behavior;
- font-loading/fallback risk where Type affects geometry;
- zoom/reflow validation plan;
- keyboard/focus implications where visual placement differs from DOM order;
- browser/device evidence level actually obtained.

---

## CRITIQUE

W002 improves the Web baseline because it turns W001's broad relationship-over-coordinate principle into a page-level selection framework and produces three materially different solutions to one realistic content problem.

However, this block intentionally stops short of browser PASS. No new executable browser harness was run in this commit. Therefore claims about exact Grid/Flex intrinsic sizing, actual zoom, Korean/English wrapping thresholds, focus order, local table overflow and cross-browser behavior remain OPEN.

The next practice block should render the three directions with controlled long English/Korean strings and test at least:

- ordinary narrow viewport;
- actual browser zoom/reflow rather than viewport-only proxy;
- preferred/fallback font states where executable;
- source/focus order versus visual placement;
- local overflow containment;
- a table that remains tabular rather than becoming card-shaped by default.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type
W002 consumes T016's result as a composition constraint: preferred-font geometry is not the only valid runtime state. Future Web browser practice should return measured wrap/reflow failures using exact delivered fonts.

### Color
W002 keeps hierarchy structurally legible before chromatic reinforcement. Later page-theme work should test whether Color increases or accidentally flattens the established hierarchy.

### Layout / Interaction
W002 transfers L002/L003/L006 into a complete-page decision model. Future browser practice should hand back evidence on reflow thresholds, local overflow, DOM/visual order and layer ownership rather than re-deriving the spatial principles abstractly.

---

## OPEN

- executable W002 browser specimen/harness/results;
- actual browser zoom and text enlargement;
- long Korean/English stress corpus;
- exact delivered webfont loading/fallback transfer;
- Firefox/Safari/physical mobile transfer;
- keyboard/focus order under responsive placement;
- local-overflow table behavior and accessibility;
- image/media/aspect-ratio stress;
- human comprehension/comparison evidence, deferred until a project requires it.

## Evidence level

**PRACTICE / CRITIQUE — authoritative Web standards + peer-evidence transfer + original three-direction page-composition exercise + KEEP/REWORK/REJECT rationale. No browser PASS claimed.**