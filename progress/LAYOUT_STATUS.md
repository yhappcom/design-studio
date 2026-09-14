# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L005`; Interaction `I005`

This file is maintained by the Layout, Spatial & Interaction Specialist. It must not update global `progress/STATUS.md` during ordinary research.

## Operational mission

This specialist studies spatial organization and interaction to improve real app, web and product decisions. Research volume and curriculum speed are not success metrics.

For live projects, accumulated evidence must become project-specific guidance on hierarchy, grouping, density, responsive behavior, navigation, state, feedback, latency, concurrency, recovery, target placement, accessibility, localization, platform/device constraints, implementation trade-offs, validation, uncertainty and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules; Foundation is **not passed**.

Spatial evidence stays under `research/layout/`; temporal/behavioral evidence stays under `research/interaction/`.

## Four-specialist sync

Latest relevant peer state:

- **Type:** through `T005`; numeral/runtime and Latin/Korean fallback evidence are active transfer inputs.
- **Color:** through `C006`; semantic-token transfer now has two-context practice, while C001/C002/C003 remain key Layout/Interaction dependencies.
- **Web:** no substantive `W###` at latest check; `W001` remains next. Do not invent Web evidence.

Web remains the complete page/browser integration partner. Layout/Interaction may independently validate browser behavior in its own domain when useful, without replacing Web canonical ownership.

---

## Canonical evidence

### Layout / spatial

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`
- `research/layout/L001-figure-ground-balance-optical-centering.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`
- `research/layout/L002-density-validation-specimen.html`
- `research/layout/L002-density-validation-playwright.py`
- `research/layout/L002-density-validation-results-summary.json`
- `research/layout/L002-density-validation-report.md`
- `research/layout/L003-type-fallback-density-reflow-transfer.md`
- `research/layout/L003-type-layout-transfer-playwright.py`
- `research/layout/L003-type-layout-transfer-results-summary.json`
- `research/layout/L004-tabular-numerals-dense-comparison-transfer.md`
- `research/layout/L004-tabular-numerals-playwright.py`
- `research/layout/L004-tabular-numerals-results-summary.json`
- retained grid/responsive/grouping/L001 product-design exercises.

### Interaction

- `research/interaction/007-interaction-agency-feedback-errors.md`
- `research/interaction/015-directness-state-modes-reversibility.md`
- `research/interaction/I001-navigation-history-focus-restoration-interruption.md`
- `research/interaction/I001-navigation-state-validation-specimen.html`
- `research/interaction/I001-navigation-state-validation-playwright.py`
- `research/interaction/I001-navigation-state-validation-report.md`
- `research/interaction/I002-latency-pending-optimistic-retry.md`
- `research/interaction/I002-async-validation-specimen.html`
- `research/interaction/I002-async-validation-playwright.py`
- `research/interaction/I002-async-validation-results-summary.json`
- `research/interaction/I002-async-validation-report.md`
- `research/interaction/I003-forced-colors-state-semantic-resilience.md`
- `research/interaction/I003-forced-colors-validation-playwright.py`
- `research/interaction/I003-forced-colors-results-summary.json`
- `research/interaction/I004-concurrent-edits-conflict-merge-recovery.md`
- `research/interaction/I004-conflict-validation-playwright.py`
- `research/interaction/I004-conflict-results-summary.json`
- retained state-matrix and Study 015 practice/critique evidence.

### Shared accessibility evidence

- `research/004-accessibility-reflow-targets-focus.md`
- retained accessibility geometry practice/critique.

---

## Latest completed block — I004 concurrent edits / conflict / merge / recovery

I004 extends I001/I002 from one user's async lifecycle into **multiple valid concurrent intentions**.

### Source/project model

Evidence and current platform guidance establish that:

- version/precondition metadata can prevent blind lost updates;
- a stale write should not automatically overwrite current authoritative state;
- conflicts should be resolved automatically when the product can do so correctly;
- otherwise local/remote intentions must be preserved for explicit resolution;
- offline reconciliation requires a conflict policy, not only a retry policy.

I004 classifies:

1. no semantic conflict;
2. disjoint mergeable conflict;
3. same-semantic-field conflict;
4. delete vs edit;
5. externally committed/side-effect conflict;
6. ordering/sequence conflict.

### Failure reproduced — lost update

Controlled sequence:

- v1 title `Flight 101`, notes `Routine`;
- remote writer changes title to `Flight 101A` → v2;
- stale writer changes notes to `Weather diversion` but sends a naive whole-record save.

Observed v3:

- notes update survives;
- title reverts to stale `Flight 101`;
- remote writer's valid change is lost.

This confirms why “last response wins” and “save until success” are not acceptable universal interaction policies.

### Re-proof — disjoint merge

With version-aware conflict detection:

- stale save is blocked;
- local draft remains visible;
- controlled domain model recognizes title and notes changes as independent;
- merge rebases the local note change onto current remote title;
- final v3 preserves both `Flight 101A` and `Weather diversion`;
- focus returns to stable Save after resolution.

### Re-proof — same-field conflict

When both writers change title:

- remote v2 remains untouched until a decision;
- local `Flight 101B` remains preserved;
- conflict UI exposes both values;
- blocking conflict receives focus;
- explicit `Use my version` commits against current v2 → v3;
- focus returns to the edited field.

### Re-proof — delete vs edit

When the remote record is deleted while a stale local draft changes notes:

- deletion is classified separately;
- local draft remains intact;
- product does not silently resurrect deleted `r1`;
- `Keep my changes as a new record` creates separate identity `r2` while `r1` remains deleted.

### Controlled result

Playwright: **17/17 assertions PASS**.

Evidence level: **PRACTICE + CRITIQUE / controlled Chromium conflict state-machine evidence**.

Not PASS: real ETag/If-Match service, actual Firestore/backend transactions, multiple devices/tabs, offline/reconnect queues, text/list/ordering CRDT/OT, authorization conflict, AT, localization and human conflict-comprehension evidence remain open.

### Professional conclusion

Conflict UX is not one dialog pattern. The product should use the least burdensome policy that preserves valid intentions and domain invariants:

- auto-merge only when semantic independence is established;
- preserve local work before asking for resolution;
- same-field/coupled-field conflicts require a meaning-aware choice if the system cannot decide safely;
- delete vs edit may require a new identity rather than overwrite/resurrection;
- retry is not conflict resolution.

---

## Previous key blocks

### L004 — tabular numerals → dense Layout transfer

Chromium control fonts showed zero DOM digit/decimal spread under `tabular-nums`, but Inter's tabular figures widened a fixed 88px numeric column enough to cause `3/4` overflows. Intrinsic numeric width removed overflow. State: **PRACTICE / CRITIQUE**.

### I003 — forced-colors state-semantic resilience

Chromium forced-colors emulation reproduced fill/shadow-only state failures; structural/current/text/programmatic cues survived. **14/14 assertions PASS**. State: **PRACTICE / CRITIQUE**.

### L003 — Type fallback → Layout transfer

Four T005-compatible Latin/Korean fallback stacks crossed different wrap thresholds. Semantic-lane recomposition stabilized critical object identity. State: **PRACTICE / CRITIQUE**.

### L002 — whitespace / density / spatial rhythm

**216-condition Chromium validation**: fake compactness through clipping/undersized controls rejected; adaptive density preserves content/targets/grouping while compressing discretionary whitespace. State: **PRACTICE / CRITIQUE**.

### I001 — navigation as state

Back/Up/Close/deep-link/workspace/focus/draft model; **14/14 controlled assertions PASS** after failure → revision → re-proof. State: **CRITIQUE**.

### I002 — latency / pending / retry / cancellation

Separates confirmed/failed/**outcome unknown**, ties Retry/Cancel to data contracts, and preserves recovery focus; **19/19 controlled assertions PASS**. State: **PRACTICE / CRITIQUE**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real-rendering proof; text-growth/cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants; realistic layering; blinded comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | controlled centroid data; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size device proof; blinded comparison; text/RTL transfer |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | L002 rendered cycle complete; human task/broader project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002/L003 localized/enlarged/fallback evidence; actual zoom/cross-browser/device/production page transfer pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | L003 fallback + L004 numeric runtime transfer established; production font loading/exact T004/cross-platform/human evidence pending |
| Dense numeric comparison geometry | PRACTICE / CRITIQUE | L004 proof established; locale/accounting/dynamic update/human comparison evidence pending |
| Interaction agency / feedback / errors | CRITIQUE | broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device/human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |
| Color-channel-independent state semantics | PRACTICE / CRITIQUE | I003 controlled proof complete; real OS/other browsers/AT/production token-component/human evidence pending |
| Concurrent edits / conflict / merge / recovery | **PRACTICE / CRITIQUE** | I004 17-assertion controlled proof complete; real service/offline/multi-device/CRDT-OT/AT/human validation pending |

---

## Peer evidence affecting this role

### Type

Type is through T005. L003/L004 provide Layout-owned browser transfer evidence for fallback and numeric-feature dependencies. Production font/fallback quality remains Type-owned.

### Color

Color is through C006.

Relevant consequences:

- C001/C002/I003: current/focus/status/conflict meaning must survive color replacement;
- C003: data color must not collide with interaction state;
- C006: finance/operational contexts keep action, selection/current, focus and domain status as separate semantic jobs.

I004 adds `local`, `remote`, `conflict`, `deleted elsewhere`, and `merged` as Interaction semantics that Color may encode but must not define.

### Web Design

No substantive `W###` at latest synchronization.

Web should reproduce L002/L003/L004/I001/I002/I003/I004 under production page systems, font loading, localization, real router/service/API, offline/reconnect, target browser/device/OS accessibility modes and AT.

---

## Active next queue

Choose by expected project value, not file count.

1. **L002 human task validation when participants are available** — known-item search, comparison and action selection; performance separate from preference/workload.
2. **Color → Layout density/salience transfer** — consume/coordinate with C007 when available; hold L002/L004 geometry constant while varying luminance/chroma/emphasis.
3. **L001 stronger validation** — controlled border-ownership/centroid/optical-centering raster evidence and blinded observation where possible.
4. **I004 higher-fidelity transfer** — real ETag/If-Match or transaction backend, offline/reconnect, multiple devices/tabs, delete/finalization semantics and AT when a suitable environment exists.
5. **L004 extension only if useful** — exact T004 research font or production `@font-face`, locale/accounting formats, dynamic update and real zoom/DPR.
6. **I003 higher-fidelity transfer** — real OS high-contrast/AT/production tokens when environment exists.
7. Consume future `W###` evidence and independently reproduce high-risk findings where useful.
8. Open `L005` or `I005` only for a genuinely new high-value question after current validation gaps are considered.

---

## Open research-quality gaps

- human search/comparison/action evidence for density/fallback/numeric layouts;
- human conflict-resolution comprehension/error evidence;
- controlled human observation for grouping, figure-ground, balance and optical centering;
- actual browser zoom rather than synthetic scaling;
- production font loading/fallback and exact T004 browser transfer;
- geometry-fixed Color density/salience transfer;
- real OS forced-color/high-contrast environments;
- real multi-device/offline conflict and sync reconciliation;
- CRDT/OT/list/text/order conflict behavior where relevant;
- real router/history and service/network evidence;
- screen-reader/AT validation of navigation, state, status, conflict, busy/progress and dense table semantics;
- interruption/resumption evidence on representative tasks;
- stronger future Web integration.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- L004 confirms browser-level tabular alignment while exposing numeric-column width cost.
- I004 adds local/remote value comparison, version/user metadata and preserved drafts as localization/wrapping stress contexts.
- Scope limit: Layout/Interaction does not define font internals or production fallback stacks.

### Color

- I003 confirms C001's color-channel-loss failure mechanism.
- I004 adds conflict/local/remote/deleted/merged semantic states; they must remain understandable without color alone.
- L002/L004 supply fixed dense-data geometry for future C007-style salience transfer.
- Scope limit: no new Color threshold is claimed.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- enable approved numeric features before finalizing numeric tracks;
- viewport width alone is insufficient near Type/fallback thresholds;
- timeout, failure and outcome-unknown are distinct;
- retry is not conflict resolution;
- auto-merge only when semantic independence is established;
- preserve local draft across conflict;
- same-field and delete-vs-edit need distinct recovery;
- object identity matters when preserving work after deletion;
- disappearing recovery controls need explicit focus lifecycle;
- critical state meaning must survive authored color-channel loss.

### Web Design

Reusable transfer evidence:

- L002: **216-condition density/reflow matrix**;
- L003: mixed-script fallback / wrap-threshold / semantic-lane transfer;
- L004: browser tabular-numeral / decimal / intrinsic-width transfer;
- I001: **14-assertion navigation/state matrix**;
- I002: **19-assertion latency/retry/cancellation matrix**;
- I003: **14-assertion forced-colors matrix**;
- I004: **17-assertion concurrent-edit/conflict matrix**.

Web should reproduce these with production fonts/tokens/pages, actual zoom/localization, real router/API/offline/multi-device behavior, target browser/device matrix, OS accessibility modes and AT.

---

## Latest checkpoint

- `L002`: density validation → **PRACTICE / CRITIQUE**.
- `L003`: T005 fallback→Layout transfer → **PRACTICE / CRITIQUE**.
- `L004`: browser `tnum`/decimal/intrinsic-width transfer → **PRACTICE / CRITIQUE**.
- `I001`: navigation/state validation → **CRITIQUE**.
- `I002`: async/retry/cancel validation → **PRACTICE / CRITIQUE**.
- `I003`: forced-colors semantic resilience → **PRACTICE / CRITIQUE**.
- `I004`: concurrent edit/conflict/merge/recovery → **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L005`; Interaction `I005`.
- No PASS promotion claimed. Highest-value remaining work is human evidence plus production Color/Web/Type/service/AT transfer rather than research volume.
