# L009 — Integrated Workflow Architecture Capstone

Status: **STAGE 2 PRACTICE / CRITIQUE COMPLETE — integrated product-practice gap materially reduced; Stage 2 closure audit still required**

Evidence intent: **ORIGINAL PRACTICE + COMPARATIVE STUDY + CRITIQUE + PEER-EVIDENCE TRANSFER**

## Question
Can the Layout / Interaction specialist turn its strong mechanism-level evidence into three materially different complete product architectures for the same operational workflow, then defend one direction using explicit criteria without collapsing into component-driven sameness?

This directly answers L008. It is a controlled practice substrate, not a production redesign of LogMate or any live app.

## RELATED DOMAIN CHECK
### Type
Checked current Type status through T021. Reused semantic role architecture, proportional technical identifiers by default, tabular figures for comparison-critical numerics, and the rule that geometry must survive real font metrics. Exact production font transfer remains Type-owned.

### Color
Checked current Color status through C018. Reused C017/C018 semantic-role principle: state meaning is stable while palette strategy may vary; hue is reinforcement rather than the sole carrier. Color Stage 2 is PASS; physical-display/human evidence remains later work.

### Layout / Interaction
Checked L001–L008 and I001–I006. Reused responsive relationship preservation, layer ownership, route/view/transient-state separation, async/retry/recovery, and preserved-intention rules. L008 explicitly requested an integrated workflow capstone rather than another isolated mechanism study.

### Web
Checked W011–W013. Reused W011's signal-role distinction and icon+visible-label default, and W013's independent Chromium confirmation that route identity, view state, transient task layer and focus restoration require separate contracts. This capstone does not claim browser execution.

### Overlap classification
**INTEGRATED PRACTICE + TRANSFER VALIDATION.** Existing peer mechanisms are intentionally assembled into a complete product-design exercise. No peer canonical ownership is replaced.

---

# 1. Fixed problem substrate
A generic operational logbook workspace is used because it naturally combines dense records, search, editing, settings and recovery.

Primary task: find a prior record, verify critical operational fields, correct one field if needed, and return to the same comparison context without losing search/filter state.

Secondary task: add a new record, survive interrupted/failed save, and understand local/pending/saved/failed state without relying on color alone.

Fixed objects: record (date, identifier, origin, destination, duration, role/status), query/filter state, selected record, draft, save/sync outcome, display preferences.

Required surfaces/states: browse/list or dashboard, search/filter, dense comparison region, add/edit form, settings, populated/empty/loading/partial/error/recovery, narrow recomposition, labeled/non-text signals, explicit navigation/state model.

The data, tasks and state semantics remain constant across all three hypotheses.

---

# 2. Architecture A — Record-Centric Workspace
Persistent record table is primary. Search/filter sits directly above it. Selecting a row opens detail/editor without destroying table context. Add is a labeled primary action; Settings remains secondary.

`query/filter → table → selected record detail/edit`

Reusable components: search field, filter group, status pair, field controls, save/retry controls. Page-specific: dense table keeps its own geometry; form grouping is not forced to mimic rows.

State policy: loading has explicit status; no-match preserves query; zero-dataset has a distinct first-record action; partial data remains inspectable with degradation explicit; pending keeps draft visible; failure preserves draft + retry/discard; ambiguous outcome does not silently duplicate submission.

Responsive: wide may use table + adjacent detail. Narrow recomposes to summary/list → dedicated detail while preserving query/filter context; columns are prioritized rather than uniformly squeezed.

**KEEP:** shortest primary path; strongest comparison; context can survive edit; avoids false card sameness.

**REWORK:** wide minimum widths; narrow restoration of query/filter/scroll; Settings discoverability.

**REJECT WHEN:** aggregate monitoring becomes the dominant task.

---

# 3. Architecture B — Summary-First Dashboard
Aggregate metrics/status and recent activity lead. Search opens a record explorer; editing occurs from explorer/detail. Settings is a utility destination.

`summary → explorer/search → record detail/edit`

Metric tiles are reusable only for repeated aggregate semantics. Records remain a table/list rather than becoming cards. Summary loading/error is independent from explorer loading/error.

Responsive: summary tiles reflow; explorer becomes full width on narrow screens.

**KEEP:** good when the first question is overall state; separates monitoring from maintenance; can surface global pending/error.

**REWORK:** extra navigation for the fixed primary task; risk of decorative metrics; duplicate search entry ambiguity.

**REJECT WHEN:** frequent record lookup/correction dominates.

---

# 4. Architecture C — Search/Command-First Workspace
Prominent search/command entry is primary. Results form a compact list; selection opens detail/edit. Add and Settings remain explicit labeled actions.

`search/command → result set → record detail/edit`

Results optimize recognition rather than copying table geometry. Search has initial/querying/zero-result/partial/error states; save state remains separate.

Responsive: sequential flow transfers naturally to narrow width. Dense cross-record comparison becomes an explicit secondary mode.

**KEEP:** direct for expert known-item retrieval; low initial density; strong narrow transfer.

**REWORK:** browse users pay recall cost; comparison becomes secondary; initial state can under-expose data.

**REJECT WHEN:** users often need to scan before knowing what to search for.

---

# 5. Explicit comparative criteria
Scale: 1 weak → 5 strong for this fixed exercise. Scores are structured studio judgments, not human-performance measurements.

| Criterion | Weight | A | B | C |
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

Weighted totals (maximum 200): A **184**, B **157**, C **146**.

The total is only a consistency check; it does not erase criterion conflicts or substitute for human evidence. A first manual tally incorrectly recorded A=185/C=145; recalculation against the stored criterion matrix corrected the arithmetic before status promotion. Preserving this correction is part of the critique trail.

## Selected direction — A, provisionally
**KEEP A Record-Centric Workspace** because the fixed primary task is lookup/comparison/correction, not aggregate monitoring or known-item command retrieval.

Borrow from B: global pending/error summary when operationally useful. Borrow from C: fast search/command affordance for expert retrieval without making it the only doorway.

This is not a universal logbook rule.

---

# 6. Selected workflow contract
Find/inspect/correct: query/filter → select record → inspect while context remains recoverable → edit draft separate from persisted record → explicit pending → success commits authoritative value or failure preserves draft + retry/discard. Ambiguous outcome uses stable operation identity rather than blind duplicate submission.

Add: labeled Add → validation without erasing input → pending visible → failure preserves local intent → cancel/discard explicit until irreversible boundary.

Search/filter states: initial populated, active query, no match with query preserved, zero dataset with first-record path, loading, partial/degraded, error+retry.

Settings contains display/format preferences only when they affect interpretation. Task-critical filters are not hidden in Settings.

---

# 7. Component architecture without sameness
Reuse because semantics repeat: semantic actions, input/validation shell, status/pending/error announcement pattern, search, filter group, layer-ownership contract.

Do not force reuse where semantics differ: dense table ≠ form list; no-results ≠ zero-dataset onboarding; global sync ≠ per-record save; dashboard aggregate ≠ record card; Settings row ≠ record row.

**STUDIO JUDGMENT:** component reuse follows repeated semantic/behavioral contracts. Visual resemblance alone is insufficient.

---

# 8. Iconography / non-text contract
Transferred from W011: consequential/unfamiliar actions retain visible labels; icon+visible-label is default when icon adds scan value; icon-only is bounded to conventional/repeated contexts; status/error survives hue/icon loss through text/programmatic semantics; target geometry belongs to the control, not glyph path. No human icon-recognition claim is made.

---

# 9. Reproducible non-human assertions
The companion JSON stores the criterion matrix. Recalculation must produce A=184, B=157, C=146 and preserve A as selected.

Later rendered prototype assertions:
1. query/filter survives inspect/edit/back;
2. zero-result and zero-dataset differ;
3. draft and persisted values remain distinguishable;
4. failure preserves draft;
5. ambiguous outcome forbids blind duplicate submission;
6. narrow recomposition preserves comparison-context access;
7. columns prioritize/recompose rather than uniformly compress;
8. task-critical filters remain outside Settings;
9. status survives hue removal;
10. consequential actions retain explicit names;
11. component reuse follows semantic equivalence;
12. focus, selection, route/view and transient-layer state remain separable.

These are specification-level assertions, not browser/native or human proof.

---

# 10. Critique
**KEEP:** fixed tasks across alternatives; materially different architectures; explicit criteria; peer evidence at ownership boundaries; justified page-specific composition.

**REWORK:** render selected architecture plus one rejected control under narrow/enlarged/localized stress; execute focus/keyboard/async behavior; test router context restoration; transfer to live-project data only as project-specific evidence.

**REJECT:** treating weighted total as empirical UX evidence; universalizing A; simulating human recognition/workload/scan/preference; generic-card sameness; hiding task-critical distinctions to reduce component count.

---

# 11. Stage 2 implication
L009 materially addresses all five L008 gaps: task analysis→workflow, integrated form/search/settings/states, component architecture without sameness, iconography/non-text peer transfer, and product-scale alternatives with defended selection.

This is strong Stage 2 gate evidence, but **Stage 2 is not marked PASS here**. A separate closure audit must re-read the exact Master Curriculum and avoid smuggling Stage 3/4 requirements downward.

## OPEN
Executable rendered transfer; real router/browser/native behavior; actual font/localization geometry; physical-device/input parity; AT/screen-reader evidence; human task performance/recognition/workload/preference deferred to app-development validation.

## HANDOFFS TO OTHER SPECIALISTS
### Type
A depends on dense-table typography/tabular numeric behavior but prescribes no font. Exact Type assets should later stress geometry/text growth.

### Color
Pending/error/selected/focus meanings remain stable independent of palette. C017 direction C can transfer later without changing workflow semantics.

### Web
A is ready for independent Web transfer: responsive table→detail recomposition, router restoration, native controls, forced colors and async failure should be tested rather than assumed.

### Layout / Interaction
Next action is a **Stage 2 closure audit**, not another isolated mechanism study.

## Evidence level
**ORIGINAL THREE-ARCHITECTURE PRACTICE + INTEGRATED STATE/COMPONENT SYSTEM + EXPLICIT SELECTION + KEEP/REWORK/REJECT CRITIQUE + CROSS-SPECIALIST TRANSFER.** No human, AT, physical-device, or production-platform PASS is claimed.
