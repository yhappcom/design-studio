# L009 — Integrated Workflow Architecture Capstone

Status: **STAGE 2 PRACTICE / CRITIQUE COMPLETE — integrated product-practice gap materially reduced; Stage 2 closure audit still required**

Evidence intent: **ORIGINAL PRACTICE + COMPARATIVE STUDY + CRITIQUE + PEER-EVIDENCE TRANSFER**

## Question

Can the Layout / Interaction specialist turn its strong mechanism-level evidence into three materially different complete product architectures for the same operational workflow, then defend one direction using explicit criteria without collapsing into component-driven sameness?

This directly answers the gap identified by L008. It is a controlled practice substrate, not a production redesign of LogMate or any live app.

## RELATED DOMAIN CHECK

### Type
Checked current Type status through T021. Reused: semantic role architecture, proportional technical identifiers by default, tabular figures for comparison-critical numerics, and the rule that geometry must survive real font metrics rather than be repaired with indiscriminate monospace. Exact production font transfer remains Type-owned.

### Color
Checked current Color status through C018. Reused C017/C018 semantic-role principle: state meaning is stable while palette strategy may vary; hue is reinforcement rather than the sole carrier. Color Stage 2 is PASS, but physical-display/human evidence remains later work.

### Layout / Interaction
Checked L001–L008 and I001–I006. Reused responsive relationship preservation, layer ownership, route/view/transient-state separation, async/retry/recovery, and preserved-intention rules. L008 explicitly requested an integrated workflow capstone rather than another isolated mechanism study.

### Web
Checked W011–W013. Reused W011's signal-role distinction and icon+visible-label default, and W013's independent Chromium confirmation that route identity, view state, transient task layer and focus restoration require separate contracts. This capstone does not claim browser execution.

### Overlap classification
**INTEGRATED PRACTICE + TRANSFER VALIDATION.** Existing peer mechanisms are intentionally assembled into a complete product-design exercise. No peer canonical ownership is replaced.

---

# 1. Fixed problem substrate

A generic operational logbook workspace is used because it naturally combines dense records, search, editing, settings and recovery. The exercise is domain-neutral enough to transfer later.

## Primary user task
Find a prior record, verify the critical operational fields, correct one field if needed, and return to the same comparison context without losing search/filter state.

## Secondary task
Add a new record, survive interrupted/failed save, and understand whether the record is local, pending, saved or failed without relying on color alone.

## Fixed information objects
- record: date, identifier, origin, destination, duration, role/status;
- query/filter state;
- selected record;
- draft edit/new record;
- save/sync outcome;
- display preferences.

## Required surfaces/states
- browse/list or dashboard;
- search/filter;
- dense comparison table/region;
- add/edit form;
- settings/preferences;
- populated, empty, loading, partial, error and recovery states;
- narrow responsive recomposition;
- labeled/non-text signals;
- explicit navigation/state model.

The data, tasks and state semantics remain constant across all three architecture hypotheses.

---

# 2. Architecture A — Record-Centric Workspace

## Structure
A persistent record table is the primary surface. Search/filter sits directly above it. Selecting a row opens a detail/editor region without destroying table context. Add is a primary labeled action. Settings remain secondary and separate.

`query/filter → table → selected record detail/edit`

## Component policy
Reusable: search field, filter group, status badge/text pair, field controls, save/retry controls.

Page-specific: the dense record table is allowed its own geometry and is not forced into generic cards; detail editing uses a task-specific field grouping rather than reusing table rows as form rows.

## State policy
- loading: table skeleton/placeholder region with explicit status text;
- empty-query: preserve filters and explain no matching records;
- empty-dataset: distinct first-record action;
- partial: available records remain inspectable while degraded source/status is explicit;
- save pending: draft remains visible and editing ownership is explicit;
- save failure: preserve draft + retry/discard choices;
- ambiguous outcome: do not silently duplicate submission.

## Responsive policy
Wide: table + adjacent detail region where space permits.
Narrow: relationship is recomposed into list/table summary → dedicated detail route/layer; query/filter state is preserved on return. Columns are prioritized, not uniformly squeezed.

## KEEP
- shortest path for the primary find/compare/correct task;
- strongest dense-data comparison;
- table context can survive edit;
- page-specific composition avoids false card sameness.

## REWORK
- wide two-region mode requires careful minimum widths;
- narrow transition must explicitly preserve query/filter/scroll context;
- settings discoverability must remain adequate without competing with primary task.

## REJECT WHEN
The product's dominant task becomes aggregate monitoring rather than record retrieval/comparison.

---

# 3. Architecture B — Summary-First Dashboard

## Structure
A summary dashboard leads with aggregate metrics/status and recent activity. Search opens a dedicated record-explorer surface. Editing occurs from explorer/detail. Settings are a dashboard utility destination.

`summary → explorer/search → record detail/edit`

## Component policy
Reusable metric tiles and status summaries are allowed only for genuinely repeated aggregate semantics. Records remain a table/list in explorer rather than becoming metric cards.

## State policy
Dashboard has independent summary loading/error from explorer data loading/error. A summary failure must not imply record data is unavailable.

## Responsive policy
Summary tiles reflow; explorer becomes full-width on narrow screens. No attempt is made to preserve a dashboard+table split when it harms comparison.

## KEEP
- strong for users whose first question is “what is the current overall state?”;
- separates aggregate monitoring from record maintenance;
- can surface pending/error state globally.

## REWORK
- primary exercise task gains an extra navigation step;
- summary can become decorative if metrics do not drive decisions;
- duplicate search entry points can create IA ambiguity.

## REJECT WHEN
The dominant workflow is frequent record lookup/correction and aggregate metrics are secondary.

---

# 4. Architecture C — Search/Command-First Workspace

## Structure
A prominent search/command entry is the primary doorway. Results appear as a compact list; selection opens detail/edit. Add and settings are available through explicit labeled commands/actions.

`search/command → result set → record detail/edit`

## Component policy
Search result rows are optimized for recognition, not forced to share full table geometry. The edit form remains semantically grouped. Command affordances retain visible labels for consequential/unfamiliar actions.

## State policy
Search has explicit initial, querying, zero-result, partial-result and error states. Save/recovery semantics remain separate from search state.

## Responsive policy
Transfers cleanly to narrow width because the architecture is sequential. Dense cross-record comparison is available through an explicit “compare results” mode rather than the default result list.

## KEEP
- direct for expert retrieval when identifiers/queries are known;
- low initial visual density;
- naturally responsive sequential flow.

## REWORK
- browse/recognition users pay recall cost;
- dense comparison becomes a secondary mode;
- empty initial state can under-expose available records.

## REJECT WHEN
Users often need to visually scan records before knowing what to search for.

---

# 5. Explicit comparative criteria

Scale: 1 weak → 5 strong for this fixed exercise. Scores are structured studio judgments, not human-performance measurements.

| Criterion | Weight | A Record-centric | B Summary-first | C Search-first |
|---|---:|---:|---:|---:|
| primary-task directness | 5 | 5 | 3 | 4 |
| dense comparison efficiency | 5 | 5 | 4 | 2 |
| recognition over recall | 4 | 5 | 4 | 2 |
| state/recovery visibility | 5 | 5 | 5 | 4 |
| responsive relationship survival | 4 | 4 | 4 | 5 |
| component-semantic fit | 4 | 5 | 4 | 4 |
| localization/text-growth resilience | 3 | 4 | 4 | 4 |
| accessibility structure | 4 | 5 | 4 | 4 |
| implementation/state complexity | 3 | 3 | 3 | 4 |
| future-change flexibility | 3 | 4 | 4 | 4 |

Weighted totals (maximum 200):
- A: **185**
- B: **157**
- C: **145**

The total is only a consistency check. It does not erase criterion conflicts or substitute for human evidence.

## Selected direction — A, provisionally

**KEEP A Record-Centric Workspace** for this fixed problem because the primary task is record lookup/comparison/correction, not aggregate monitoring or known-item command retrieval.

Borrow from B: global pending/error summary when it changes operational decisions.

Borrow from C: fast search/command affordance for expert retrieval, without making it the only doorway.

This is a defended selection under the exercise constraints, not a universal logbook architecture rule.

---

# 6. Complete workflow contract for selected A

## Find / inspect / correct
1. Enter query or filter; results update without destroying source order semantics.
2. Select a record; selection state is distinct from focus and route identity.
3. Inspect detail while comparison context remains recoverable.
4. Enter edit; draft state is separate from persisted record.
5. Save enters explicit pending state.
6. Success commits authoritative value and returns/retains comparison context.
7. Failure preserves draft and offers retry/discard; ambiguous outcome uses stable operation identity rather than blind duplicate submission.

## Add
1. Labeled Add action opens a new-record task surface.
2. Validation prevents known invalid submission but does not erase entered values.
3. Pending save remains visible.
4. Failure preserves local intent.
5. Cancel/discard is explicit and reversible until irreversible boundary.

## Search/filter states
- initial populated;
- active query;
- no match with query preserved;
- data empty with first-record path;
- loading;
- partial/degraded;
- error + retry.

## Settings
Settings contains display/format preferences only when they affect how the workspace is interpreted. Task-critical filters are not hidden in Settings.

---

# 7. Component architecture without sameness

## Reuse because semantics repeat
- semantic button/action primitives;
- text input and validation shell;
- status/pending/error announcement pattern;
- search field;
- filter control group;
- dialog/layer ownership contract where a transient layer is justified.

## Do not force reuse where semantics differ
- dense record table ≠ form field list;
- no-results state ≠ empty-dataset onboarding;
- global sync status ≠ per-record save status;
- dashboard aggregate ≠ record card;
- settings row ≠ record row.

**STUDIO JUDGMENT:** component reuse follows repeated semantic/behavioral contracts. Visual resemblance alone is insufficient reason to collapse structures into one component.

---

# 8. Iconography / non-text signal contract

Transferred from W011:
- consequential/unfamiliar actions retain visible labels;
- icon + visible label is the default action pairing where the icon adds scan value;
- icon-only is bounded to conventional disclosure/overflow or strongly repeated contexts;
- status/error meaning survives hue and icon loss through text/programmatic semantics;
- target geometry belongs to the control, not the glyph path.

No human icon-recognition claim is made.

---

# 9. Reproducible non-human assertions

The accompanying JSON records the fixed task model, criteria, weights, architecture scores and weighted totals. Recalculation must produce A=185, B=157, C=145 and preserve A as the selected direction.

Structural assertions for a later rendered prototype:
1. query/filter state survives record inspect/edit/back;
2. zero-result and zero-dataset states are distinct;
3. draft and persisted values are distinguishable during edit/pending/failure;
4. save failure preserves draft;
5. ambiguous outcome does not authorize blind duplicate submission;
6. narrow recomposition preserves access to comparison context;
7. table columns prioritize/recompose rather than uniformly compress;
8. task-critical filters are not moved into settings;
9. semantic status survives hue removal;
10. consequential actions retain explicit names;
11. component reuse follows semantic equivalence rather than card/list visual sameness;
12. focus, selected record, route/view state and transient layer state remain independently representable.

These are specification-level assertions. This run does **not** claim browser/native execution or human task-performance validation.

---

# 10. Critique

## KEEP
- fixed tasks/information across all alternatives;
- materially different architecture hypotheses rather than cosmetic variants;
- explicit criteria tied to the primary question;
- peer evidence reused at ownership boundaries;
- selected architecture contains deliberate page-specific composition.

## REWORK
- render/prototype the selected architecture and at least one rejected control under narrow/enlarged/localized stress;
- validate real focus/keyboard/async behavior in an executable medium;
- test whether table→detail context restoration survives an actual router/framework;
- use live-project data only during project-specific transfer, not as retroactive proof of this generic exercise.

## REJECT
- treating the weighted total as empirical UX evidence;
- declaring A universally superior;
- simulating human recognition, workload, scan speed or preference;
- using generic cards to make all surfaces visually uniform;
- hiding primary filters/settings distinctions merely to reduce component count.

---

# 11. Stage 2 implication

L008 identified five integrated gaps. L009 materially addresses all five in one controlled capstone:
- task analysis → complete workflow: **DIRECT PRACTICE**;
- form/search/settings/empty/error/loading/recovery: **INTEGRATED PRACTICE**;
- component architecture without sameness: **DIRECT PRACTICE**;
- iconography/non-text semantics: **PEER TRANSFER + INTEGRATION**;
- product-scale alternatives + defended selection: **DIRECT THREE-SOLUTION PRACTICE**.

This is strong Stage 2 gate evidence, but **Stage 2 is not marked PASS in this file**. A separate closure audit must re-read the exact Master Curriculum and decide whether accumulated L/I evidence plus L009 satisfies the gate without smuggling Stage 3/4 requirements downward.

## OPEN
- executable rendered capstone transfer;
- real router/browser/native behavior;
- actual font/localization geometry;
- physical-device/input parity;
- AT/screen-reader evidence;
- human task performance, recognition, workload and preference — deferred to app-development validation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type
Selected A depends on dense table typography and tabular numeric behavior but does not prescribe a font. Exact selected Type assets should later stress column geometry and text growth.

### Color
Selected A requires semantic pending/error/selected/focus roles to remain stable independent of palette. C017 direction C can be transfer-tested later without changing the workflow semantics.

### Web
A is ready for independent Web transfer: real responsive table→detail recomposition, router state restoration, native controls, forced colors and async failure should be tested rather than assumed.

### Layout / Interaction
Next highest-value action is a **Stage 2 closure audit**, not another isolated mechanism study. If the gate passes, later executable/product transfer remains valuable evidence but belongs to the appropriate later-stage or live-project requirement.

## Evidence level

**ORIGINAL THREE-ARCHITECTURE PRACTICE + INTEGRATED STATE/COMPONENT SYSTEM + EXPLICIT SELECTION + KEEP/REWORK/REJECT CRITIQUE + CROSS-SPECIALIST TRANSFER.**

No human, AT, physical-device, or production-platform PASS is claimed.
