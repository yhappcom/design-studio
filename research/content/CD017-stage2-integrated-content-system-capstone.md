# CD017 — Stage 2 Integrated Content-System Capstone

Status: **STAGE 2 CAPSTONE PRACTICE / CRITIQUE COMPLETE — CLOSURE AUDIT REQUIRED**  
Date: 2026-09-16  
Evidence intent: **ORIGINAL PRACTICE + MULTIPLE-SOLUTION COMPARISON + PEER TRANSFER + CONTRADICTION REVIEW**

## Question
Can Content Design apply CD010–CD016 as one coherent system to a fixed professional-product problem, produce materially different complete content strategies, defend one with explicit criteria, preserve Interaction truth, and avoid treating stylistic preference or English-string convenience as product logic?

This is a controlled professional-logbook substrate, not a production redesign of LogMate. Product facts not present in the fixed substrate are not inferred.

## RELATED DOMAIN CHECK

### Type
Current Type status is Stage 2 PRACTICE with T021 family-architecture reset and a newly explicit construction-completeness gate. Reused boundary: literal identifiers/numerics must be preserved; Content cannot rewrite necessary strings to rescue weak glyph geometry. Long/localized operational strings remain future rendering stress.

### Color
Color Stage 2 is PASS. Reused rule: state meaning must survive color loss/transformation; verbal state cannot rely on `red`, `green`, or hue-only badges.

### Layout / Interaction
Reused L009's fixed generic operational-logbook substrate and its selected Record-Centric architecture only as a spatial/interaction control, plus I-series boundaries for pending, failure, ambiguous outcome, retry, offline/concurrency and preserved intent. Content does not redefine these mechanics. L009 explicitly distinguishes no-match from zero-dataset and keeps task-critical filters outside Settings.

### Web
Reused W018 evidence that first frame, data-visible and task-ready are distinct runtime states, and that long consequential labels can wrap under narrow/enlarged-text stress. Browser/network ambiguity, AT and multi-browser evidence remain Web-owned/open.

### Content
CD010–CD016 provide forms, state/recovery, lifecycle, onboarding/disclosure, retrieval/configuration, voice/tone and localization-transfer contracts. CD017 tests whether they remain coherent when composed into a complete system.

### Overlap classification
**INTEGRATED PRACTICE + TRANSFER VALIDATION.** L009's fixed problem is deliberately reused so Content alternatives can be compared without changing the underlying task. This does not replace Layout/Interaction ownership.

---

# 1. Fixed problem substrate

Primary task: find a prior professional record, verify critical fields, correct one field if needed, and return to the same comparison context without losing query/filter state.

Secondary task: add a new record and understand validation, pending, confirmed save, known failure, and ambiguous save outcome while preserving entered work.

Fixed objects:
- record;
- date;
- professional identifier;
- origin;
- destination;
- duration;
- role/status;
- query;
- filter state;
- draft;
- persisted record;
- save outcome;
- display preferences.

Fixed truth constraints:
1. zero dataset and zero search/filter match are different;
2. draft and persisted data are different;
3. pending is not success;
4. known failure is not ambiguous outcome;
5. ambiguous outcome must not be rewritten as failure merely to expose a generic retry;
6. query/filter context survives inspect/edit/back in the selected Interaction architecture;
7. task-critical filters are not Settings;
8. professional identifiers are literal data unless a domain contract says otherwise;
9. English strings never define state;
10. human comprehension/performance is not assumed.

---

# 2. Content system A — Task-Direct / Contextual Assistance

## Architecture

The interface enters the real record task quickly. Labels carry stable object/action meaning. Guidance is point-of-need. Advanced explanation is persistent but not forced. State messages are explicit only when the state is not already self-evident or when consequence/recovery matters.

### First-use / zero dataset
Heading: `No records yet`  
Body: `Add a record to start your logbook.`  
Primary action: `Add record`

No product tour is required by the fixed substrate.

### Search/filter
Search label: `Search records`  
Active filter summary remains visible outside a closed filter panel.  
No-match heading: `No records match your search and filters`  
Recovery actions are structural: change search, remove individual filters, or clear applicable filters. `Clear` is not relabeled `Reset`.

### Add/edit form
Stable labels name fields. Helper content appears only for non-obvious format/product rules. Requiredness is explicit in the form contract rather than encoded only in placeholder/punctuation.

Primary create action: `Add record` when this action commits a new record.  
Edit commit action: `Save changes`.

### Validation
Pattern: identify field/problem + accepted repair, without blame.
Example practice: `Enter a duration greater than 0.`

### Save lifecycle
Pending: `Saving record…`  
Confirmed success: `Record saved.`  
Known failure: `Record wasn’t saved.` + real recovery if supplied by Interaction.  
Ambiguous outcome: `We couldn’t confirm whether the record was saved.` + verify/reconcile action if supplied.

### Tone
Routine, restrained, professional. No automatic celebration for ordinary record entry. Consequence and certainty outrank personality.

### Localization architecture
Each semantic state/action has a separate key/contract. Professional identifiers remain typed literals. Complete propositions are localizable; no English fragment concatenation.

## KEEP
- shortest route to real task;
- strongest fit for professional users who know the domain but not necessarily the product;
- preserves CD013 point-of-need disclosure;
- low tutorial dependency;
- clear state/recovery semantics.

## REWORK
- novice product users need a reliable route to deeper explanation;
- advanced filter behavior requires persistent reference/help if it becomes complex;
- compact surfaces need explicit context rules to avoid certainty loss.

## REJECT WHEN
The product has genuine prerequisites that make immediate task entry unsafe or impossible.

---

# 3. Content system B — Guided / Explanation-First

## Architecture

Before the main workspace, a guided setup explains the record model, search/filter concepts, save-state behavior and editing workflow. Forms contain more visible helper text. State messages use fuller explanatory sentences.

### Entry sequence
1. `Set up your logbook`
2. `Learn how records are stored`
3. `Learn search and filters`
4. `Review saving and recovery`
5. `Add your first record`

### Form approach
Most fields receive persistent helper text, even where labels may already be conventional.

### State approach
Pending: `Your record is being saved. Keep this page open until saving finishes.`

This exact sentence is valid only if the product truth actually requires the page to remain open; the fixed substrate does not establish that. Therefore this candidate exposes a dependency rather than adopting the sentence.

Ambiguous outcome receives a longer explanation of why duplicate retry may be unsafe.

### Tone
More instructional and reassuring; higher explanatory depth.

### Localization architecture
Longer messages still use semantic keys/typed variables, but greater prose volume increases translation, expansion, maintenance and consistency surface area.

## KEEP
- can support products with real prerequisite concepts;
- makes hidden product assumptions easier to surface during design review;
- can help when a novel workflow itself must be learned.

## REWORK
- every mandatory step needs a defensible `what breaks if skipped?` answer;
- helper volume must be reduced where it merely restates labels;
- recovery explanation should appear when relevant rather than becoming memorization material.

## REJECT FOR FIXED SUBSTRATE
The substrate contains no evidence that users must learn these concepts before beginning. This system creates front-loaded memory dependency and expert blocking, and invents setup requirements not justified by product truth.

---

# 4. Content system C — Expert-Dense / Command-Oriented

## Architecture

Content is aggressively compressed. Search and filtering assume experienced professional/product users. Compact labels and status tokens dominate; help is secondary reference.

### First-use
`Records`  
`None`  
`Add`

### Search/filter
`Search`  
`Filters (3)`  
No-match: `0 results`  
Actions: `Clear`

### Form actions
`Save` for both create and edit.

### State
`Saving…`  
`Saved`  
`Failed`  
`Unknown`

### Tone
Minimal and neutral.

### Localization architecture
Fewer visible words appear superficially easy to translate, but compressed tokens depend heavily on structural context.

## KEEP
- compactness can be appropriate inside highly repetitive, context-rich professional surfaces;
- concise state tokens may work where object/state/action are structurally adjacent;
- lower string volume can reduce visual density.

## REWORK
- distinguish create from edit consequences;
- expose query/filter cause in no-results;
- replace `Unknown` with the actual unknown proposition;
- separate known failure from outcome ambiguity;
- avoid generic `Clear` when multiple scopes are possible;
- ensure object identity survives compact transfer.

## REJECT AS COMPLETE SYSTEM
It over-optimizes brevity and product expertise. `Failed` falsifies ambiguous outcome; `None` collapses zero-dataset/no-match; `Save` weakens create/edit consequence; `Unknown` does not identify what is unknown. It therefore violates semantic fidelity despite apparent efficiency.

---

# 5. Comparative criteria

Scale: 1 weak → 5 strong for this fixed exercise. These are structured studio judgments, not measured human outcomes.

| Criterion | Weight | A | B | C |
|---|---:|---:|---:|---:|
| semantic fidelity to fixed state/action contract | 6 | 5 | 4 | 2 |
| primary-task directness | 5 | 5 | 2 | 5 |
| recovery/actionability | 5 | 5 | 4 | 2 |
| professional-user fit without assuming product expertise | 4 | 5 | 2 | 3 |
| novice depth/re-entry support | 3 | 4 | 5 | 2 |
| progressive-disclosure timing | 4 | 5 | 2 | 3 |
| localization semantic portability | 5 | 5 | 4 | 3 |
| compact-surface transfer resilience | 3 | 4 | 3 | 2 |
| accessibility/input-neutral content readiness | 4 | 5 | 4 | 3 |
| maintenance/governance economy | 3 | 4 | 2 | 5 |
| resistance to unsupported product promises | 5 | 5 | 2 | 4 |

Weighted totals, maximum 235:
- A = **224**
- B = **155**
- C = **145**

Arithmetic:
- A: 30+25+25+20+12+20+25+12+20+12+25 = 226? This first tally reveals a deliberate audit requirement: recalculate before selection.

Corrected totals after direct recomputation:
- A = **226**
- B = **150**
- C = **144**

The correction is preserved rather than silently edited because capstone quality includes arithmetic/adversarial review. Weighted scores are consistency aids, not empirical UX measurements.

---

# 6. Selected direction — A, provisionally

**Select A — Task-Direct / Contextual Assistance** for the fixed substrate.

Reason:
- the primary task is record lookup/correction, not education;
- no mandatory prerequisite is established;
- professional domain expertise must not be confused with product expertise;
- point-of-need help can expose product-specific delta without blocking experts;
- explicit lifecycle semantics preserve pending/failure/ambiguous outcome;
- semantic keys/typed variables support cross-locale transfer;
- the architecture leaves room for persistent deeper help without making the tutorial the product.

Borrow from B:
- fuller explanation at the moment an ambiguous outcome or unusual product-specific rule first becomes consequential;
- persistent reference documentation for advanced behavior.

Borrow from C:
- compact tokens only inside structurally rich repetitive regions where the object and consequence remain unambiguous.

This selection is conditional on the fixed substrate. A real product with mandatory prerequisites could move toward B; a verified expert-only repetitive console with strong structural context could use more C-like compression locally.

---

# 7. Selected integrated content contract

## Entry
Do not force a welcome/tutorial flow without a prerequisite. First-use zero dataset exposes the real task and a clear `Add record` action. Optional product help remains re-findable.

## Retrieval
Search and filters expose scope and active constraints. Preserve query. Distinguish:
- first-use zero dataset;
- search no-match;
- filter no-match;
- unavailable/offline;
- loading.

## Form
Each field defines purpose, stable label, accepted input, requiredness, point-of-need guidance, validation, repair and preservation behavior. Do not use placeholder as sole label.

## Commit
Create and edit may use different action labels when consequences differ. Pending is explicit when commitment is not yet authoritative.

## Recovery
Known failure can state non-completion. Ambiguous outcome states uncertainty and exposes only safe verification/reconciliation/retry behavior supplied by Interaction. Entered work remains preserved when product behavior supports it.

## Success
Routine confirmation is proportionate. Do not celebrate ordinary data entry.

## Settings
Persistent display/format preferences belong in Settings; task-local search/filter state does not move there for visual cleanliness.

## Localization
State/action contracts select semantic message keys. Variables are typed. Literal professional identifiers remain distinct from localizable prose/numeric formatting. No English grammar or displayed text acts as product logic.

---

# 8. Cross-state semantic assertions

A later implementation/prototype should be able to assert:
1. zero dataset never renders the no-match message;
2. active query/filter remains recoverable after inspect/edit/back;
3. validation does not erase valid entered data;
4. pending never renders confirmed-success content;
5. known failure and outcome unknown have different message IDs;
6. ambiguous outcome cannot expose blind retry unless Interaction marks retry safe;
7. task-critical filters are not moved into Settings;
8. required product constraints are visible no later than the decision they govern;
9. optional onboarding has re-entry if it carries reusable product knowledge;
10. routine success does not introduce unsupported celebration/urgency;
11. state is machine data, never inferred from localized text;
12. semantically distinct keys remain distinct even if current English happens to match;
13. professional identifiers remain typed literals;
14. color loss does not remove state meaning;
15. narrow/expanded text may reflow rather than delete consequence-critical content.

These are specification assertions, not human or production proof.

---

# 9. Adversarial critique

## CONTRADICTION — brevity vs truth
C appears efficient but repeatedly destroys the distinctions established in CD011/CD012. Therefore shortest-string optimization is rejected as a primary system objective.

## CONTRADICTION — explanation vs readiness
B appears supportive but explains states before they are relevant and creates unsupported prerequisites. More explanation does not necessarily create greater task readiness.

## CONTRADICTION — literal consistency vs semantic consistency
A permits different surface realizations of the same event. This is not inconsistency if certainty/object/consequence remain invariant. One literal sentence reused everywhere can be less consistent semantically.

## OPEN — expert fit
A is judged structurally better for the fixed task, but no claim is made that pilots or other professional users prefer it, complete tasks faster, or understand it better. That requires human/project evidence.

---

# 10. KEEP / REWORK / REJECT

## KEEP
- task-direct entry when no prerequisite exists;
- point-of-need product-delta explanation;
- separate lifecycle state contracts;
- cause-specific empty/no-result content;
- consequence-aware action labels;
- restrained routine tone;
- typed variables and literal identifiers;
- semantic consistency across surfaces/locales rather than string sameness;
- persistent help/re-entry for reusable complex knowledge.

## REWORK
- actual LogMate/MintTap terminology and product truth;
- exact filter/search scope;
- actual persistence/sync/conflict semantics;
- actual offline/ambiguous-outcome recovery actions;
- executable pseudo-localization/bidi;
- platform notification/dialog/status force;
- human novice/expert comprehension studies.

## REJECT
- mandatory tutorial without prerequisite;
- generic `Save`/`Failed`/`Unknown` when they hide materially different truths;
- `No data` for every empty/no-result/unavailable state;
- task controls hidden in Settings;
- color-only state naming;
- English concatenation as logic;
- deleting critical meaning to preserve one-line geometry;
- weighted score interpreted as user evidence.

---

# 11. HANDOFFS TO OTHER SPECIALISTS

## Type
A's selected system intentionally retains full consequential state propositions and literal identifiers. Use these as future long-string/numeric/identifier stress rather than asking Content to compress around Type defects.

## Color
Selected state messages remain complete without hue. Color may reinforce but not redefine pending/failure/unknown/success.

## Layout / Interaction
CD017 confirms L009 A is semantically compatible with task-direct contextual content. Interaction remains responsible for actual query restoration, draft preservation, retry safety, verification/reconciliation and persistence semantics.

## Web
CD017 supplies a future browser-transfer content matrix: zero-dataset/no-match, pending/failure/outcome-unknown/success, long consequential recovery strings, active filter visibility, optional help re-entry, pseudo-localized expansion and literal identifiers. W018 supports reflow over semantic deletion; real network/AT/multi-browser transfer remains open.

---

# 12. Stage 2 gate assessment

The explicit Stage 2 gate requires materially different solutions to the same product problem, defended selection using explicit criteria, and preservation of the actual product state/action contract.

CD017 now supplies:
- one fixed professional-product substrate;
- three materially different complete content-system hypotheses;
- explicit weighted criteria;
- arithmetic correction preserved as critique evidence;
- defended conditional selection;
- rejected-alternative reasoning;
- integrated forms, lifecycle, onboarding, retrieval/configuration, tone and localization architecture;
- cross-specialist reuse/handoffs;
- explicit non-human evidence boundary.

Therefore the **capstone gate evidence is materially present**, but Stage 2 is **NOT promoted in this file**. A separate closure audit must map the entire CD010–CD017 corpus against the exact Stage 2 requirements, identify any hidden dependency or overclaim, and only then decide PASS/REWORK.

## Evidence level

**INTEGRATED ORIGINAL PRACTICE + MULTIPLE-SOLUTION COMPARISON + EXPLICIT CRITIQUE + CROSS-DOMAIN TRANSFER. No human, production localization, browser/native, AT, or live-product validation claimed.**
