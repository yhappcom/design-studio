# Content Design / UX Writing Specialist Status

Operating state: **ACTIVE — STAGE 1 PASSED / STAGE 2 PRACTICE / CD010–CD014 EXECUTED**  
Governance activation: 2026-09-16  
Primary path: `research/content/`  
Study prefix: `CD###`  
Next new-study ID: `CD015`

## Current level

Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**  
Stage 3 — Advanced / Systems Practice: **NOT STARTED**  
Stage 4 — Production & Authorship: **NOT STARTED**  
Stage 5 — Research & Advisory: **NOT STARTED**

Authority:
- CD001–CD007 — Foundation source/practice evidence;
- CD008 — integrated Foundation capstone;
- CD009 — Stage 1 closure audit / PASS;
- CD010 — forms/validation/error baseline;
- CD011 — error/warning/service-failure/recovery taxonomy;
- CD012 — empty/loading/pending/success/recovery lifecycle;
- CD013 — onboarding/progressive-disclosure professional-workflow system;
- **CD014 — search/filter/sort/settings task-system study**.

## Product-language direction

English-first source language for global release. Architecture remains localization-ready. Locale-specific work opens only when product/market need or transfer risk justifies it; Korean is not a Stage 2 blocker.

## Stage 1 closure

`research/content/CD009-stage1-foundation-closure-audit.md` remains the bounded authority for Stage 1 PASS. It does not claim human comprehension/task evidence or production localization/runtime evidence.

## Stage 2 evidence through CD013

CD010–CD012 establish form contracts, state taxonomy, and lifecycle content. CD013 adds professional onboarding/progressive disclosure with the critical distinction `domain expertise ≠ product expertise`, decision-relative disclosure timing, skip/resume/re-entry/replay contracts, and three onboarding strategies. These remain practice evidence rather than live-product or human validation.

## CD014 — Search / Filter / Sort / Settings task systems

Canonical: `research/content/CD014-search-filter-sort-settings-task-systems.md`.

### New result

Retrieval/configuration content is now modeled as four different contracts:
- **search** changes membership through query matching within a scope;
- **filter** constrains membership through structured predicates;
- **sort** changes ordering, not membership;
- **settings** change persistent or semi-persistent product behavior/preferences.

The system rejects control-driven collapse such as one generic `Filter` surface silently changing scope, membership, ordering and persistent defaults.

### Search scope

Every search requires an explicit or reliably inferable corpus/scope and a truthful searchable-field contract. Professional identifiers need deliberate normalization rules; ordinary natural-language normalization can damage flight numbers, registrations, airport codes, tickers or transaction IDs. Placeholder examples cannot promise fields the implementation does not search.

### Filter causality

Filters are treated as predicates with named dimensions, values/operators, combination semantics, default state, persistence and clear behavior. Active constraints must remain semantically visible after a filter panel closes. `No flights found` is rejected when the truth is `No flights match the active filters`.

### Sort semantics

Sort labels name the domain field and direction when ambiguity matters. `Newest` is insufficient if multiple dates exist. Algorithmic labels such as `Best` or `Recommended` require an appropriate explainable basis rather than implying objective quality.

### Settings boundary

A setting is a persistent behavior contract with scope, application timing, persistence/sync, reversibility and default source. Task-critical filters must not be moved into Settings merely to simplify layout; this directly transfers L009.

### Reset/default distinctions

`Clear query`, `Clear filters`, `Reset changes`, `Restore defaults`, and deleting a saved preset/view are separate operations. `Reset` is defective when its baseline is unknown. `Default` is defective when the source/value is not intelligible to the user.

### Apply vs immediate

Content must match actual commitment semantics. Immediate changes do not need a false `Apply` stage. Staged edits require saved-vs-draft distinction and explicit commit/discard behavior. `Done` is rejected when it obscures whether filters/settings were actually committed.

### Localization architecture

Retrieval logic lives in semantic metadata, not English concatenation. Dimension key, machine value, localized label, operator, sort field/direction, count/plural formatting and literal-data rules remain separate. Compact English filter chips do not justify deleting semantic dimensions needed by other locales.

### Comparative practice

Three retrieval architectures were compared for a fixed professional-record lookup task:
- A global search + hidden advanced filters — REWORK;
- B persistent query + explicit active-filter summary + explicit sort — provisional KEEP;
- C settings-driven default views with minimal task controls — REJECT as primary retrieval architecture, though saved views may supplement B.

This is studio practice, not a LogMate production decision and not human-performance evidence.

## Cross-specialist transfer

### Type
Compact filters, sort labels, counts, literal identifiers and localization expansion are realistic operational stress strings; semantic dimensions are not removed to hide Type defects.

### Color
Active filters/changed settings must survive color loss and forced-color transformation.

### Layout / Interaction
Interaction owns apply timing, persistence, restoration and synchronization truth. Content preserves task-local versus persistent-setting boundaries.

### Web
Search scope/query/filter/sort state is ready for later URL/history/browser transfer, dynamic-result status, keyboard/focus and direct-entry restoration tests.

## Stage 2 gap map after CD014

| Area | State |
|---|---|
| buttons/action labels | strong Foundation bridge + repeated practice |
| forms/questions/labels/helper text | **PRACTICE — strong** |
| validation/error/warning/recovery | **PRACTICE — strong** |
| empty/loading/pending/success lifecycle | **PRACTICE — strong** |
| onboarding/progressive disclosure | **PRACTICE — strong** |
| search/filter/sort/settings | **PRACTICE — strong after CD014** |
| voice/tone system | **NEXT MAJOR GAP** |
| localization-ready patterns | strong repeated bridge; broader cross-surface transfer still needed |
| complete multiple-solution content system | OPEN for Stage 2 capstone |

## Active next queue

1. **CD015 — voice/tone as controlled modulation of functional content**, not brand adjective lists: risk, urgency, user agency, emotional context, professional-domain neutrality, error/success modulation and global-English constraints.
2. Localization-ready pattern transfer across forms, lifecycle, onboarding and retrieval/configuration surfaces.
3. Integrated Stage 2 capstone: materially different complete content systems for one fixed professional-product problem, explicit criteria, defended selection, critique and handoffs.
4. Stage 2 closure audit only after the explicit gate is evidenced.

## OPEN / dependencies

- actual LogMate/MintTap searchable fields and normalization rules;
- actual saved-view/filter persistence and settings sync semantics;
- multi-device conflict behavior;
- native/web history restoration and AT announcements;
- production localization/message-format and translator workflow;
- human findability, comprehension, recovery and trust evidence;
- telemetry linking zero-results/filter/reset/message states to outcomes.

## Latest checkpoint

- Stage 1: **PASS**.
- CD010–CD012: forms/state/lifecycle systems executed.
- CD013: **DEEP ONBOARDING / PROGRESSIVE DISCLOSURE PRACTICE EXECUTED**.
- CD014: **SEARCH / FILTER / SORT / SETTINGS TASK-SYSTEM PRACTICE EXECUTED**.
- Stage 2: **PRACTICE / NOT PASSED**.
- Human validation: **NOT CLAIMED**.
- Production runtime/localization validation: **NOT CLAIMED**.
- Next Content study: **CD015 — voice/tone controlled modulation system**.
