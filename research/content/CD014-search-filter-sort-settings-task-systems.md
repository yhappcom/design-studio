# CD014 — Search, Filter, Sort, and Settings as Task Systems

Status: **STAGE 2 PRACTICE — DEEP TASK-SYSTEM STUDY / NOT PASSED**  
Date: 2026-09-16

## Question

How should an English-first professional product design search, filter, sort and settings content as explicit transformations of scope, order and persistent behavior rather than as isolated control labels?

CD012 established distinct empty/search-no-result/filter-empty lifecycle truth. CD013 established disclosure timing and expert/novice assistance. CD014 now studies retrieval and configuration as systems whose language must make **scope, active constraints, result transformation, persistence and reset consequences** intelligible.

## RELATED DOMAIN CHECK

### Type
Literal identifiers, dates, flight numbers, registrations, tickers, numeric values and compact filter chips are operational strings. Content must preserve their identity and necessary qualifiers; Type owns glyph/spacing/rendering fitness. Long filter names and localized sort labels become geometry stress, not permission to delete meaning.

### Color
Active filter, selected scope and changed-setting states cannot depend on hue alone. Semantic state must be named/programmatically exposed independently of visual treatment.

### Layout / Interaction
Direct reuse of L009: task-critical filters belong with the task rather than being hidden in Settings; query/filter context must survive inspect/edit/back when that continuity is part of the workflow. Interaction owns whether changes apply immediately, require Apply, persist, reset, or affect other surfaces.

### Web
Search scope, URL/history restoration, keyboard behavior, async result state and native/custom control behavior require runtime transfer. Content defines the semantic contract, not browser implementation proof.

### Content
CD002 terminology, CD003 action grammar, CD004 scanning/order, CD007 localization architecture, CD012 no-results/filter-empty distinction, and CD013 progressive disclosure are reused.

Overlap classification: **INTEGRATED TASK-SYSTEM STUDY + PEER TRANSFER + CONTRADICTION REVIEW + PRODUCTION-TRANSFER PREPARATION**.

## SOURCE

Current Apple search guidance treats search as a scoped interaction and supports suggestions, scopes and tokens. Apple's 2026 search design material explicitly notes that placement can alter perceived search scope. Apple settings guidance treats settings as a dedicated interface for configurable behavior and notes that some infrequently changed settings can live in system Settings. GOV.UK Design System guidance states that filtering/sorting should apply to the whole result set, not merely the visible page, and that defaults should help users reach needed content efficiently. W3C cognitive-accessibility search guidance emphasizes findability and recommends supportive mechanisms such as autocomplete and grouping where appropriate.

These sources support scope clarity, findability and consistent transformation. They do not establish one universal search/filter/settings architecture for professional apps.

---

# 1. Core model — four operations, four different contracts

## SYNTHESIS

- **Search** changes the candidate set by matching a query against a declared or inferable scope.
- **Filter** constrains an existing candidate set by explicit predicates.
- **Sort** changes ordering, not membership.
- **Settings** change persistent or semi-persistent product behavior/preferences beyond one immediate retrieval operation.

### STUDIO JUDGMENT

Do not merge these concepts because they share a toolbar.

A control labeled `Filter` that also changes sort order, data scope and persistent defaults creates a hidden multi-contract operation.

A task-local constraint is not automatically a setting. A persistent preference is not automatically a filter.

---

# 2. Search requires a scope contract

For every search define:

- searchable corpus;
- searchable fields;
- current scope;
- query normalization assumptions;
- exact vs partial matching where materially relevant;
- identifier behavior;
- result ordering/relevance basis where user decisions depend on it;
- zero-result meaning;
- suggestions/history behavior;
- whether query state survives navigation;
- privacy/sensitivity implications of search history.

### Critical professional-domain rule

Identifiers often need different treatment from prose. Flight number, aircraft registration, airport code, ticker and transaction identifier may have punctuation/case/leading-zero semantics that ordinary natural-language search normalization can damage.

Content therefore must not promise `Search everything` unless the implementation genuinely searches the represented scope.

### Search placeholder rule

Placeholder can suggest scope, but must not be the only durable explanation when scope is ambiguous or consequential because placeholder disappears during entry.

Examples of stronger source-English direction when true:
- `Search flights, airports, or registrations`
- `Search by flight number or registration`

These are contracts, not decorative examples. Do not list fields that are not actually searchable.

---

# 3. Query is not filter, even when both reduce results

### SYNTHESIS

Search expresses an information need, often as text or identifier input. Filters expose structured predicates such as date range, aircraft type, role, portfolio or ticker.

### CONTRADICTION TEST

If a query `737` matches flight number, aircraft type, notes and registration while an Aircraft filter selects only aircraft type, displaying both merely as `737` destroys the distinction between **match rule** and **constraint**.

### STUDIO JUDGMENT

Active constraints should preserve their semantic dimension:
- `Aircraft: 737-8`
- `Role: PIC`
- `Date: Jan–Mar 2026`

Compact visual chips may shorten only when surrounding structure keeps the dimension unambiguous.

---

# 4. Filter content is a predicate system

For each filter document:

- dimension name;
- available values/range;
- inclusion/exclusion semantics;
- AND/OR relationship across selections;
- default state;
- active-state representation;
- result count behavior if available;
- clear-this-filter action;
- clear-all behavior;
- persistence across navigation/session;
- whether hidden filters remain active;
- no-match recovery.

### Critical rule — hidden active state

A filter drawer may close, but its constraints must not become semantically invisible. If results are restricted, users need enough evidence to understand why.

`No flights found` is defective when the actual truth is `No flights match the active filters`.

### Count rule

A count such as `12 results` describes the current transformed set only if computation is authoritative. Do not use stale counts as confirmation of current constraints.

---

# 5. Sort is ordering, not relevance magic

Sort labels should name the ordering criterion and, when needed, direction.

Weak:
- `Newest` when the relevant date could be purchase date, flight date, import date or update date.

Stronger when true:
- `Flight date — newest first`
- `Updated — newest first`
- `Distribution amount — highest first`

### STUDIO JUDGMENT

Professional products should expose the domain field behind an ordering when ambiguity could change interpretation.

`Recommended`, `Best`, `Relevant` and similar algorithmic labels require an explainable basis appropriate to product risk. Content must not imply objective quality when the system only applies a heuristic ranking.

### SOURCE TRANSFER

GOV.UK guidance that sorting/filtering applies to the whole list supports a key semantic invariant: pagination or viewport boundaries must not change the declared meaning of the sort.

---

# 6. Search + filter + sort composition

The result set can be modeled as:

`corpus → scope → query match → structured predicates → ordering → presentation`

This is not an implementation prescription; it is a content diagnostic.

For any results surface, Content should be able to answer:

1. What universe is being searched?
2. What query is active?
3. What structured constraints are active?
4. What ordering is active?
5. How many results are represented, if known?
6. Which operation will change membership versus order?
7. What survives if the user opens a result and returns?

If these answers cannot be recovered from product state, wording alone cannot repair the architecture.

---

# 7. No-results is causal, not generic

Reuse CD012 but deepen the retrieval causes:

- query produced no matches;
- filters produced no matches;
- query + filters jointly produced no matches;
- selected scope contains no records;
- corpus unavailable/offline;
- permission excludes content;
- search/index is incomplete or still building;
- result is genuinely zero.

### Recovery hierarchy

Offer only valid recovery:
- clear query;
- remove one or all filters;
- broaden scope;
- correct identifier;
- wait for indexing only when that is true;
- reconnect;
- request access.

Do not default to `Try another search` if structured filters are the actual cause.

---

# 8. Clear, Reset, Restore defaults, and Remove are different actions

### STUDIO MODEL

- **Clear query** — remove entered search expression.
- **Clear filters** — remove current task constraints.
- **Reset changes** — return controls to a defined pre-edit state; exact baseline must be specified.
- **Restore defaults** — replace current preferences with product-defined defaults.
- **Remove saved view/preset** — delete a stored configuration object.

### CONTRADICTION

`Reset` without naming the baseline is semantically incomplete. It may mean current-session values, last-saved values, recommended defaults, factory defaults, or clearing all data.

For consequential configuration, prefer object + destination state where space allows: `Restore default display settings` rather than unexplained `Reset`.

---

# 9. Settings are persistent behavior contracts

A setting should define:

- object/behavior controlled;
- current value/state;
- effect of changing it;
- scope (this view / portfolio / device / account / all devices);
- application timing (immediate / next use / restart / future records only);
- persistence;
- synchronization behavior if relevant;
- dependency/conflict with other settings;
- reversibility;
- default source;
- localizer context.

### STUDIO JUDGMENT

A setting label should usually describe the stable concept, not merely one current action.

For a switch, the label must make the ON state interpretable without relying on nearby prose such as `Enable` where the controlled behavior remains unnamed.

### Task-local vs persistent boundary

Put a control in Settings because it governs persistent product behavior, not because the main workflow is visually crowded.

This directly transfers L009's finding that task-critical filters must not be hidden in Settings merely for layout cleanliness.

---

# 10. Defaults are product decisions expressed through content

A default is not neutral. It determines the initial behavior users may never change.

For each default ask:

- who/what selected it;
- whether it is safe for new users;
- whether it preserves existing data/meaning;
- whether it varies by locale/device/account;
- whether migration changes it;
- whether `Default` is meaningful to the user or only to implementation.

### STUDIO JUDGMENT

Do not label an option `Default` when the user cannot know what value that means. Prefer the actual value or `System setting` / `Device setting` when that is the true source.

---

# 11. Apply vs immediate application

Content must reflect the interaction contract.

### Immediate filters/settings
Changes take effect as controls change. An `Apply` action would falsely imply staged commitment unless there is a real draft state.

### Staged filters/settings
Changes remain provisional until `Apply`/`Save`. Then Content must distinguish:
- saved/current values;
- edited draft values;
- discard/cancel consequence;
- unsaved-change navigation behavior.

### STUDIO JUDGMENT

Do not use `Done` when the important semantic act is `Apply filters` or `Save settings` and completion would otherwise be ambiguous.

`Done` can close a surface without saying whether state was committed.

---

# 12. Saved searches, saved filters, presets, and views

These are objects, not merely remembered controls.

Define whether the saved object contains:
- query;
- filters;
- sort;
- visible columns/layout;
- date relative/absolute semantics;
- scope;
- notification/subscription behavior.

A name such as `My flights` is insufficient metadata if the underlying predicate can later surprise the user.

Relative date presets (`Last 30 days`) must remain relative if that is the contract; saving today's resolved absolute dates would be a different object.

Rename/delete/overwrite semantics should name the saved object and consequence.

---

# 13. Professional-domain precision

Professional users often use compressed domain vocabulary efficiently. Plain language does not mean replacing correct expert terms with novice paraphrases.

Apply CD013's `domain expertise ≠ product expertise` distinction:
- preserve standardized/domain-recognized terminology when it is the correct concept;
- explain product-specific behavior, scope or transformation;
- do not reteach the profession inside every filter;
- do not assume professional expertise implies knowledge of product-specific defaults or persistence.

Examples:
- `PIC`, `SIC`, `IFR` may be valid domain labels in a pilot product when target users know them;
- whether selecting `PIC` means `role = PIC`, `PIC time > 0`, or another rule is a product predicate and must be defined correctly.

---

# 14. English-first / localization-ready architecture

Do not encode retrieval logic in English strings.

Semantic model should separate:
- dimension key;
- localized dimension label;
- machine value;
- localized value label;
- operator;
- formatted display;
- result count/plural message;
- sort field;
- sort direction.

Avoid concatenation such as:
`"Sort by " + field + " " + direction`
or
`count + " results for " + query`.

Use locale-aware message formatting and allow word-order reorganization.

Literal identifiers should be marked as data, not translated. Dates/numbers/units should use product-defined locale/aviation/financial formatting rules rather than accidental English formatting.

Filter chip geometry must tolerate translation expansion; semantic dimensions must not be removed merely to preserve compact English chips.

---

# 15. Accessibility and nonvisual state

Visible active constraints, selected sort and changed settings need programmatic equivalents. Color or chip fill alone cannot communicate active state.

Search scope must be discoverable without depending solely on spatial placement. Apple's 2026 search guidance explicitly notes that placement influences perceived scope; Content therefore treats scope wording/structure as a safeguard when layout alone could be ambiguous.

Dynamic result counts/no-results are candidate status information, but actual announcement frequency, live-region behavior and focus remain Web/native implementation questions. Avoid announcing every keystroke/result-count change so aggressively that the interface becomes unusable; runtime/AT validation is required.

---

# 16. Comparative practice — professional records explorer

Fixed task: find prior operational records, inspect one, return to the same retrieval context.

## Architecture A — one global search + hidden advanced filters

Advantages: visually simple; fast for known identifiers.

Risks: scope ambiguity; hidden active constraints; structured professional retrieval becomes discovery-heavy.

Verdict: **REWORK**. Useful only if the corpus is genuinely simple or filters remain visibly represented after the panel closes.

## Architecture B — persistent query + explicit filter summary + explicit sort

Search field states its scope; active filters remain summarized; sort names domain field/direction; no-results identifies whether query/filter constraints caused zero matches; retrieval state survives detail/back.

Verdict: **KEEP as provisional practice direction** for the fixed expert lookup/comparison task.

## Architecture C — settings-driven default views with minimal task controls

Advantages: repeat users can open directly into preferred configuration.

Risks: hides task-local constraints in persistent configuration; current result cause becomes difficult to inspect; novice product users may not know why records are absent.

Verdict: **REJECT as primary retrieval architecture**. Saved views/preferences can supplement B but should not replace visible task state.

This is studio practice, not a LogMate production decision and not human-performance evidence.

---

# 17. Content contract v0.4

For retrieval/configuration controls record:

- `control_class`: search | filter | sort | setting | saved_view
- `concept`
- `scope`
- `machine_key`
- `display_label`
- `value_semantics`
- `operator_semantics`
- `default_value`
- `default_source`
- `active_state`
- `application_timing`
- `persistence_scope`
- `navigation_restoration`
- `sync_scope`
- `clear_semantics`
- `reset_baseline`
- `result_effect`: membership | ordering | presentation | persistent_behavior
- `zero_result_cause`
- `recovery`
- `literal_data_rules`
- `localizer_context`
- `announcement_intent`

This metadata is the semantic source; English copy is one rendering.

---

# 18. Audit v0.4

Flag:
- `SEARCH_SCOPE_AMBIGUOUS`
- `SEARCH_PROMISE_EXCEEDS_INDEX`
- `IDENTIFIER_NORMALIZATION_RISK`
- `QUERY_FILTER_COLLAPSE`
- `FILTER_DIMENSION_HIDDEN`
- `HIDDEN_ACTIVE_CONSTRAINT`
- `SORT_FIELD_AMBIGUOUS`
- `SORT_MEMBERSHIP_CONFUSION`
- `NO_RESULTS_CAUSE_COLLAPSE`
- `RESET_BASELINE_AMBIGUOUS`
- `DEFAULT_SOURCE_AMBIGUOUS`
- `TASK_CONTROL_HIDDEN_IN_SETTINGS`
- `SETTING_SCOPE_UNSTATED`
- `SETTING_APPLICATION_TIMING_UNSTATED`
- `DONE_COMMITMENT_AMBIGUOUS`
- `SAVED_VIEW_OBJECT_UNDEFINED`
- `ENGLISH_CONCATENATION_LOGIC`
- `LOCALIZATION_GEOMETRY_RISK`
- `COLOR_ONLY_ACTIVE_STATE`
- `RUNTIME_RESTORATION_UNVERIFIED`
- `AT_ANNOUNCEMENT_UNVERIFIED`
- `HUMAN_FINDABILITY_UNVERIFIED`

---

# 19. KEEP / REWORK / REJECT

## KEEP
- search/filter/sort/settings as separate semantic contracts;
- explicit search scope;
- visible active constraints;
- domain-specific sort field naming;
- causal no-results language;
- clear/reset/default distinctions;
- settings scope + application timing;
- task-local controls outside Settings;
- semantic metadata independent of English grammar.

## REWORK
- exact search normalization for each live product/domain;
- saved-view semantics;
- default-setting migration and multi-device synchronization;
- live result-count announcements;
- compact mobile filter representation without hidden state.

## REJECT
- universal `Search` with unknowable scope;
- `Filter` as an unnamed bundle of search/sort/settings behavior;
- `Reset` without a baseline;
- `Default` without a known source/value;
- `Done` where save/apply commitment matters;
- hiding active constraints after a filter panel closes;
- moving task-critical controls to Settings merely to simplify layout;
- using English string concatenation as retrieval logic.

---

# 20. Stage 2 implication

CD014 closes the broad search/filter/sort/settings task-system gap identified after CD013. It adds a reusable semantic model and a comparative architecture exercise rather than a label catalog.

Stage 2 remains **PRACTICE / NOT PASSED**. Remaining major gaps are voice/tone as a risk/state modulation system, repeated localization-ready pattern transfer across surfaces, and an integrated Stage 2 capstone that produces materially different complete content-system solutions under one fixed product problem and defends a selection.

## OPEN

- actual LogMate searchable fields, identifier normalization, saved views and filter persistence;
- actual MintTap search/filter/sort semantics;
- multi-device setting synchronization and conflict behavior;
- browser/native query-history restoration;
- real AT announcement behavior;
- human findability, recognition, filter comprehension and recovery performance;
- telemetry for zero-results, filter abandonment and reset behavior.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Preserve visible retrieval causality and distinguish task-local constraints from persistent settings. Interaction must define apply/persistence/restoration/sync truth.

### Web
Transfer scope/query/filter/sort state into real URL/history/browser behavior where appropriate; test native controls, keyboard, focus, dynamic result status and direct-entry restoration.

### Type
Stress compact filter/sort labels, counts, domain identifiers and localization expansion without deleting semantic dimensions.

### Color
Ensure active constraints/changed settings survive hue loss and forced-color transformation.

## Evidence level

**CURRENT AUTHORITATIVE-SOURCE CHECK + PEER TRANSFER + DEEP SYSTEM SYNTHESIS + CONTRADICTION TESTS + THREE-ARCHITECTURE PRACTICE + LOCALIZATION/ACCESSIBILITY CONTRACT. No live-product, human, AT, or production runtime PASS claimed.**
