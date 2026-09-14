# W002 — Page Composition, Flow, Grid, Density & Visual Hierarchy

Status: **PRACTICE / CRITIQUE — controlled Chromium transfer complete; Foundation Web work still open**

Canonical artifacts:

- `research/web/W002-page-composition-flow-grid-density-hierarchy.md`
- `research/web/W002-page-composition-specimen.html`
- `research/web/W002-page-composition-playwright.py`
- `research/web/W002-page-composition-results.json`

## Research question

How should a Web designer choose ordinary flow, Flexbox, Grid, bounded sizing, local overflow, or positioning from the **relationship the product must preserve**, rather than from a preferred CSS technique, a named device breakpoint, or a reference screenshot?

The project goal is to preserve information priority, comparison relationships, readable flow and valid adaptation under variable content.

## RELATED DOMAIN CHECK

### Type

Checked `progress/TYPE_STATUS.md` through T016. T016 proves in a controlled Chromium case that downloadable-font loading/failure can change width, wrapping and downstream geometry. W002 therefore treats exact line breaks as runtime outcomes rather than stable composition primitives. This is **TRANSFER VALIDATION**, not a duplicate Type study.

### Color

Checked `progress/COLOR_STATUS.md`. Color Stage 1 is PASS. W002 does not delegate hierarchy to hue; source order, grouping, spacing and type remain sufficient to expose the information structure before chromatic reinforcement.

### Layout / Interaction

Checked current `progress/LAYOUT_STATUS.md`, now Stage 1 PASS. W002 reuses L002 density/rhythm, L003 Type-dependent reflow and L006 ownership evidence, then transfer-tests them as complete Web page composition rather than isolated spatial mechanisms.

### Web

Checked W001. W001 established relationship-over-coordinate design and a fixed-canvas failure→fluid/intrinsic revision. W002 extends it into a layout-mechanism selection model plus a browser-rendered three-direction exercise.

### Why overlap is useful

This is **TRANSFER VALIDATION** of Type and Layout findings into a Web-specific page system. The value is not another CSS summary; it is a project decision procedure plus measured failure→revision evidence.

---

## SOURCE

Authoritative sources were rechecked on 2026-09-15.

### CSS Grid

W3C CSS publications describe Grid as a two-dimensional grid-based layout system optimized for user-interface design. Grid permits flexible/fixed row and column tracks; Level 2 adds subgrid participation in parent sizing.

### Flexbox

The W3C Flexible Box model organizes layout around a main axis and flexible distribution/alignment. It is therefore a strong fit where the primary relationship is one-dimensional, even when wrapping is allowed.

### Reflow

WCAG 2.x Success Criterion 1.4.10 requires content, with exceptions for parts that require two-dimensional layout for usage or meaning, to be presentable without loss of information/functionality and without two-dimensional scrolling at the equivalent of 320 CSS px width for vertically scrolling content or 256 CSS px height for horizontally scrolling content.

This is an accessibility boundary, **not** a universal instruction to turn every table/chart into a single column or to prohibit all local horizontal scrolling.

### Text resize / zoom boundary

W3C guidance also treats user zoom/text enlargement as a separate accessibility concern. W002's `200% text` case below is a controlled text-growth stress test. It is **not claimed to be browser-UI 400% zoom** or complete WCAG conformance evidence.

---

## SYNTHESIS — relationship first, mechanism second

| Relationship to preserve | Default mechanism | Why | Warning |
| --- | --- | --- | --- |
| Sequential reading/task flow | ordinary document flow | content determines progression and absorbs growth naturally | fixed heights can convert growth into clipping/overlap |
| One-axis action/control group | Flexbox or ordinary flow | alignment/distribution is primarily one-dimensional | wrapping can alter grouping and priority |
| Two-axis comparison/alignment | Grid or semantic table when truly tabular | rows/columns share alignment relationships | CSS Grid must not replace table semantics for tabular data |
| Repeating items with flexible count | Grid `repeat()`/`minmax()` or wrapping Flex | available space can determine count while preserving useful measure | item count is an outcome, not the design goal |
| Full-bleed region + readable content | outer full-width region + bounded inner measure | separates surface extent from readable measure | one universal max-width is rarely appropriate for every region |
| Intrinsically 2-D artifact | local overflow/zoom/pan/recomposition | forced stacking can destroy meaning | keep overflow local; do not make the whole document scroll sideways |
| Overlay/anchored transient UI | positioning/top-layer after ownership is defined | relationship is to an anchor/layer, not normal progression | visual position does not prove focus/pointer/semantic ownership; reuse L006 |

### Decision procedure

Before choosing Grid/Flex/positioning/overflow:

1. Identify the user task and information relationship.
2. Classify it as sequential, one-dimensional, two-dimensional, anchored or intrinsically spatial.
3. Identify content that can grow, localize, load late, fail or be user-substituted.
4. Separate semantic alignment from decorative alignment.
5. Decide what may stack/wrap/reorder and what must remain simultaneously comparable.
6. Decide whether overflow is a failure or intrinsic navigation of a 2-D artifact.
7. Choose the simplest mechanism that preserves those relationships under stress.

---

## Original exercise — three compositions for one information set

Scenario: an investment-tracking web page contains page identity/summary, primary actions, four KPI values, a distribution-history chart, explanatory copy and a transaction table/list.

### Direction A — sequential editorial

- summary/actions in normal flow;
- KPI values wrap;
- chart spans the content column;
- explanation and records follow sequentially.

**KEEP:** progressive reading/comprehension dominates and narrow transfer matters strongly.  
**REWORK:** repeated chart↔record comparison is frequent.  
**REJECT:** core work requires persistent cross-panel comparison.

### Direction B — comparison workspace

- bounded page system;
- summary/actions span the page;
- chart and recent records share coordinated columns while sufficient measure exists;
- below the stress threshold they return to sequential source order instead of shrinking indefinitely.

**KEEP:** simultaneous comparison is task-critical.  
**REWORK:** long labels or text growth destroy useful column measure.  
**REJECT:** side-by-side placement is merely decorative.

### Direction C — dense data with local 2-D preservation

- summary/KPIs remain compact and flexible;
- chart remains responsive;
- genuinely tabular transaction data retains columns inside a bounded scroll region.

**KEEP:** expert cross-row/column comparison matters.  
**REWORK:** local scrolling hides essential context or keyboard/focus behavior becomes poor.  
**REJECT:** records are actually independent items whose labels can recompose without loss.

### Selected default

For a general-purpose tracker, **Direction B** remains the preferred starting point: it supports desktop comparison while retaining semantic sequential recomposition. Direction A is the lower-complexity alternative. Direction C is reserved for data surfaces where two-dimensional comparison is itself part of the task.

This is **STUDIO JUDGMENT**, not human performance evidence.

---

## Density and hierarchy model

W002 rejects both `more whitespace = better design` and `more visible information = better productivity`.

Density should instead respond to task frequency, comparison need, error cost, content variability and input constraints.

Hierarchy layers:

1. page identity/current context;
2. primary task/action;
3. decision data;
4. supporting explanation/metadata;
5. secondary/administrative actions.

Spacing, alignment, grouping, Type and Color reinforce this hierarchy together. None should be the sole semantic channel.

---

# Browser transfer validation

## Method

Engine: Chromium `144.0.7559.96` through Playwright.

Five controlled cases:

1. `1280px`, normal content/text;
2. `768px`, normal content/text;
3. `320px`, normal content/text;
4. `320px`, long bilingual English/Korean content;
5. `320px`, long bilingual content + controlled `200%` text-size stress.

Measured/asserted per case:

- document-level horizontal overflow;
- comparison workspace same-row vs stacked relation;
- local table overflow state;
- semantic `<table>` plus eight header cells retained;
- source/focusable sequence remains `Add transaction → Export history → table scroll region`.

The test does not claim screen-reader quality or browser-UI zoom equivalence.

## Initial failure and critique

The first `320px + 200% text` run produced:

- viewport/client width `320px`;
- document scroll width `420px`;
- unwanted document-level horizontal overflow.

Inspection showed heading/text minimum-content behavior was contributing overflow outside the intentionally scrollable table region.

A second issue was in the test expectation, not the design: at `768px`, the table's inner available width (`674px`) is already below the table's intrinsic minimum (`~729px`), so **local** horizontal overflow is expected there. Treating 768px local overflow as a failure would contradict the stated semantic rule that genuine 2-D data may scroll locally.

## Revision

The specimen was revised with:

- `overflow-wrap:anywhere` on headings/paragraphs to provide an emergency break path under extreme text growth;
- `min-width:0` on relevant Grid/Flex children so intrinsic minimums do not silently force ancestor expansion;
- corrected test expectation that the semantic table may enter local overflow before the page's comparison workspace stacks.

This does not mean arbitrary word breaking is always desirable in production. It is a bounded resilience choice for this specimen; production copy/language rules require review.

## Final measured result

Final run: **25/25 assertions true across 5/5 cases**.

Key measurements:

- `1280px`: document `1280/1280`, no horizontal overflow; comparison workspace remains two columns (`~697px + 336px`); table fits without local overflow.
- `768px`: document `768/768`, no horizontal overflow; workspace still two columns (`~362px + 288px`); table uses local overflow (`729px` content inside `674px` region).
- `320px`: document `320/320`, no horizontal overflow; workspace stacks to one `254px` column; table remains local overflow (`729px` inside `254px`).
- `320px + long bilingual`: no document overflow; one-column workspace and local table overflow preserved.
- `320px + long bilingual + 200% text`: after revision, document returns to `320/320`; table expands internally to `~1330px` but remains inside the `254px` local scroll region.

The focusable source sequence remained stable in all cases.

## What this establishes

Within this bounded Chromium specimen:

- page-level reflow and component-local 2-D overflow can coexist;
- a table may begin local overflow at a wider width than the breakpoint used by a separate comparison workspace because **their relationship constraints differ**;
- viewport width alone did not reveal the text-growth failure;
- intrinsic minimum sizing and break opportunities are design-relevant, not merely implementation trivia;
- source order remained stable while visual composition changed from simultaneous comparison to sequential stacking.

## What it does not establish

No claim of:

- WCAG conformance;
- actual desktop/mobile browser UI 400% zoom behavior;
- screen-reader usability;
- full keyboard operation of a production table;
- real preferred/fallback webfont behavior in this W002 specimen;
- Firefox/Safari parity;
- physical iOS/Android parity;
- human comprehension or performance superiority.

---

## Project-readiness contract

Before approving a Web composition, record:

- primary task and comparison requirement;
- semantic/source order;
- relationship class of each major region;
- chosen mechanism and rejected alternatives;
- minimum useful measure or observed stress condition rather than device-name breakpoints;
- what may wrap/stack/reorder and what must remain aligned;
- local-overflow exceptions and semantic justification;
- long/localized content behavior;
- font loading/fallback risk where Type affects geometry;
- zoom/reflow validation plan;
- focus/keyboard implications where placement differs from source order;
- browser/device evidence level actually obtained.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type

W002 confirms the project-level consequence of T016 without re-running T016: robust page composition needs slack/recomposition beyond one exact font realization. The new 200% text-growth failure also shows that text geometry can expose page overflow even when narrow-viewport tests pass.

### Color

The specimen preserves hierarchy structurally before chromatic reinforcement. Later Web Color transfer should test whether themes/states retain or flatten the same hierarchy.

### Layout / Interaction

W002 transfers L002/L003/L006 into a complete page and returns measured evidence: document reflow, component-local table overflow, source/focus order, and different stress thresholds for different relationship classes. This supports the principle that responsive behavior should follow relationship failure, not a single global breakpoint.

---

## OPEN

- actual browser-UI zoom/reflow validation distinct from the controlled 200% text-size stress;
- preferred/fallback downloadable-font transfer inside the W002 page;
- Firefox/Safari/physical mobile replication;
- richer keyboard/focus validation for interactive tables and responsive visual placement;
- screen-reader/AT validation;
- image/media/aspect-ratio stress;
- human comprehension/comparison evidence, deferred until project-stage validation.

## Evidence level

**PRACTICE / CRITIQUE — authoritative standards + peer-evidence TRANSFER VALIDATION + three materially different design directions + failure→revision browser practice + Chromium 144 five-condition matrix with 25/25 bounded assertions. NOT PASS for Web Foundation as a whole.**
