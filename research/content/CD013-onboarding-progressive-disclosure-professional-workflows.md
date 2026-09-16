# CD013 — Onboarding and Progressive Disclosure for Professional Workflows

Status: **STAGE 2 PRACTICE — DEEP SYSTEM STUDY + MULTI-SOLUTION CRITIQUE / NOT PASSED**  
Date: 2026-09-16

## Question

How should an English-first global professional product introduce concepts, setup, and advanced capability without forcing experts through tutorials, abandoning novices after a welcome screen, hiding consequential truth, or turning progressive disclosure into feature concealment?

This is intentionally a deep Stage 2 block. The target is not a library of welcome-screen phrases. It is a reusable decision system for **what must be known, when it must be known, where it should appear, whether it may be deferred, how users resume/re-enter, and how expertise changes the path**.

---

## RELATED DOMAIN CHECK

### Type
Checked current Type status. Onboarding/help strings are real operational strings: headings, steps, examples, warnings, identifiers and numeric/domain terminology must survive wrapping, fallback and localization. Type defects do not authorize semantic truncation.

### Color
Checked current Color status. Progress, completion, warning and optional/required distinctions must survive color removal/transformation. Color may reinforce but cannot own onboarding semantics.

### Layout / Interaction
Checked L009 and Interaction evidence. L009's operational logbook substrate distinguishes record lookup, add/edit, search/filter, settings and recovery; it also preserves recognition over recall and warns against hiding task-critical filters in Settings. Interaction owns whether setup is actually required, whether a step can be skipped, what state persists, and how resume/re-entry behaves.

### Web
Checked W018 and current Web status. Progressive readiness demonstrates that visible shell, available data and task readiness can be different milestones. Onboarding content must therefore not declare a product ready merely because an introductory surface has rendered. Browser focus, route restoration, disclosure controls and responsive behavior remain Web-owned validation.

### Content
Reuses CD002 user-needs/mental-model caution, CD003 action consequence, CD004 information order, CD005 accessibility wording, CD007 localization architecture, CD010 form contracts, CD011 state taxonomy and CD012 lifecycle/readiness system.

### External authoritative evidence checked
W3C WAI cognitive-accessibility guidance was checked for: clear purpose and familiar controls; finding important tasks; clear page structure; explicit step-by-step instructions; separation of instructions; orientation within multi-step processes; predictability and consistency. These are supplemental cognitive-accessibility recommendations in several cases, not all normative WCAG success criteria.

Authoritative-source direction from the Content README was retained. The present study does not convert generic platform conventions into universal laws and does not claim exact wording superiority without human evidence.

### Overlap classification
**SYSTEM SYNTHESIS + ACCESSIBILITY TRANSFER + PRODUCT-PRACTICE EXTENSION + CONTRADICTION REVIEW.**

---

# 1. Onboarding is a knowledge-transition system, not a screen sequence

## SYNTHESIS

A useful definition:

> **Onboarding is the managed transition from insufficient product/domain knowledge to sufficient knowledge for the user's next meaningful task.**

It may include first-run setup, contextual instruction, examples, defaults, empty-state guidance, import/setup decisions, permissions, later advanced-feature education, recovery education and re-entry help. It does not have to happen before the product becomes usable.

### STUDIO JUDGMENT

For each proposed onboarding item, identify:

- `user_goal` — what the user is trying to accomplish;
- `knowledge_gap` — what they cannot safely/effectively infer yet;
- `decision_or_action` — what this knowledge changes;
- `latest_safe_moment` — the latest point it can be learned without causing failure/risk;
- `earliest_useful_moment` — the earliest point it has enough context to make sense;
- `requiredness` — required, conditionally required, recommended, optional;
- `persistence` — one-time, until complete, contextual repeat, always available;
- `reentry` — how the user finds it again;
- `evidence` — source/product truth supporting the need.

If an item has no identifiable decision/action consequence, it is a candidate for removal rather than onboarding.

---

# 2. The central timing principle: earliest useful, latest safe

Too-early instruction has weak context and high memory demand. Too-late instruction permits error, confusion or unsafe commitment.

## STUDIO MODEL — instruction timing window

For knowledge item `K`:

`earliest useful moment <= presentation moment <= latest safe moment`

This is a design model, not a measured cognitive equation.

Examples:

- product philosophy: often not required before first task;
- required data-format constraint: before or adjacent to entry, not after validation failure only;
- irreversible consequence: before commitment;
- advanced filtering syntax: when search/filter use creates need, with persistent reference access;
- sync conflict semantics: when conflict can occur or before a consequential reconciliation choice, not in a generic first-run carousel;
- backup/restore consequence: before a user makes a decision whose safety depends on it.

### CONTRADICTION REVIEW

`Tell users everything up front` fails because much information lacks context and must be remembered until later.

`Never explain; make UI self-evident` also fails because professional-domain concepts, unusual constraints and consequential system behavior can be irreducibly non-obvious.

The target is **timed sufficiency**, not zero instruction or maximal instruction.

---

# 3. Progressive disclosure is information prioritization, not hiding

## SYNTHESIS

Progressive disclosure should reduce simultaneous decision burden while preserving discoverability and consequence clarity.

Classify information/action into four disclosure classes:

| Class | Meaning | Default treatment |
|---|---|---|
| immediate | needed to understand/perform the current primary task | visible now |
| consequence-critical | needed before an action can create material consequence | visible before commitment; never hidden merely for cleanliness |
| contextual | useful only under a condition, exception or advanced path | reveal when condition/path becomes relevant |
| reference | infrequently needed explanatory depth | persistent help/reference access |

### Critical rule

**Progressive disclosure must not defer truth beyond the decision it governs.**

A disclosure strategy is defective if the user can commit to a consequential action before seeing information necessary to understand that consequence.

### REJECT

- hiding required constraints in tooltips;
- burying task-critical filters/settings because the main surface looks cleaner;
- putting destructive consequences behind `Learn more` after the destructive action;
- using `Advanced` as a dumping ground for poorly prioritized product concepts;
- assuming an expert will discover an unlabeled gesture or obscure icon.

---

# 4. Required onboarding and optional education are different contracts

## STUDIO MODEL

### A. Required setup
Only when the product cannot truthfully perform the intended task without a prerequisite or legally/operationally necessary decision.

Required content must explain:
- why the input/decision is needed when not self-evident;
- what is required now;
- consequence of the choice;
- whether it can be changed later;
- what happens to entered work if interrupted.

### B. Conditionally required setup
Triggered by a chosen feature, data source, permission, environment or workflow.

Do not make all users complete it merely because some users will need it.

### C. Recommended configuration
May improve the product but is not required for truthful basic operation. Marking it as mandatory is coercive architecture.

### D. Optional education
Tips, tours, advanced shortcuts and feature discovery. It should be dismissible and re-findable unless there is a defensible safety/operational reason otherwise.

### Audit question

`What breaks if the user skips this?`

If the answer is only `they may not know this feature exists`, it is generally not required setup.

---

# 5. Novice and expert paths: shared truth, different assistance

Professional products often serve users with domain expertise but uneven product expertise. A pilot may understand flight-time concepts while being new to LogMate; an experienced MintTap investor may understand ROC but not the app's exact tax-adjustment model.

## STUDIO JUDGMENT

Do not equate:
- domain novice with product novice;
- product expert with domain expert;
- frequent user with complete knowledge;
- first launch with first meaningful use.

### Assistance ladder

1. **Recognizable primary task** — product purpose/action visible without tutorial dependency.
2. **Point-of-need label/helper** — supports normal unfamiliarity.
3. **Example or short explanation** — for non-obvious format/concept.
4. **Expandable contextual detail** — for exceptions or deeper rationale.
5. **Reference documentation** — for infrequent complex knowledge.
6. **Guided flow** — only where sequence/dependency itself needs assistance.

Experts should usually be able to proceed through levels 1–2 without being forced through 3–6. Novices must still have a discoverable path downward into greater support.

This produces **adaptive depth without changing product truth**.

---

# 6. Skip is not enough: resume, re-entry and replay

A `Skip` button alone does not make onboarding user-controlled.

For any dismissible/deferred learning flow define:

- whether progress is saved;
- whether partially entered configuration is saved;
- where the user resumes;
- whether dismissal is permanent or session-scoped;
- where the information can be found later;
- whether the product can re-surface it contextually after a relevant failure/need;
- whether replay resets data or only education state.

### STUDIO JUDGMENT

A user who skipped because they were busy is not evidence that the information is permanently irrelevant.

Conversely, repeatedly resurfacing dismissed education can become obstruction. Re-presentation needs a new contextual reason, material product change, or explicit user request.

---

# 7. Orientation in multi-step professional workflows

W3C cognitive-accessibility guidance supports clear steps, explicit instructions and orientation in multi-step processes, including completed/current/pending steps and important choices.

## SYNTHESIS

A step indicator is useful only when it represents meaningful task structure. Do not fabricate `Step 1 of 5` when branches make five meaningless or when the number changes unpredictably.

For each multi-step flow specify:

- current purpose;
- completed decisions;
- current decision/action;
- what remains at an appropriate level;
- whether back navigation is safe;
- whether changing an earlier choice invalidates later work;
- save/resume semantics;
- exit consequence.

### Content rule

Step titles should name the decision/object, not generic process verbs.

Prefer conceptual labels such as `Choose data source`, `Review imported records`, `Resolve duplicates` over `Next step`, `Details`, `Continue setup` when those labels truthfully describe the work.

---

# 8. Instructions: prevention before repair

W3C supplemental guidance recommends clear step-by-step instructions, located before/near the activity, and notes that needed instructions should not appear only after an error.

## STUDIO JUDGMENT

Instruction priority:

1. prevent high-frequency/high-cost errors;
2. state non-obvious constraints at point of need;
3. use examples when format recognition is easier than abstract explanation;
4. defer rare exceptions without making them undiscoverable;
5. retain specific validation/recovery after error.

This connects directly to CD010: helper text and validation are complementary, not substitutes.

### Failure mode

A form that teaches every rule only after rejection technically has error messages but has failed onboarding at the point of need.

---

# 9. Feature tours are a bounded tool, not the default architecture

## STUDIO JUDGMENT

A feature tour is justified when:
- spatial relationships themselves matter;
- a materially new workflow cannot be recognized from normal interface structure;
- a changed feature could cause meaningful confusion;
- the user can act on the information immediately or soon.

A tour is weak when:
- it explains ordinary controls already labeled clearly;
- it fronts loads many unrelated features;
- it requires memorization before context;
- it blocks the first useful task;
- it cannot be replayed/referenced;
- it is being used to compensate for poor information architecture.

### Contradiction test

A six-screen carousel can produce more onboarding content while producing less task readiness. Quantity of explanation is not the success metric.

---

# 10. Professional-domain terminology: teach the product delta

CD002 established mental-model caution. CD013 extends this for expert products.

### Principle

Do not reteach established professional-domain concepts unless the product uses them differently, requires a specific interpretation, or evidence shows a comprehension gap.

Teach the **delta** between domain expectation and product behavior:

- what the product calls the concept;
- how it stores/calculates/interprets it;
- any scope or assumption that differs from professional convention;
- where the source of truth comes from;
- what the user can change;
- what consequence follows.

### Example substrate — not production claims

For a logbook import workflow, explaining `CSV means comma-separated values` to an airline pilot may be less important than explaining **which imported fields LogMate will map, which it will not infer, how duplicates are classified, and what Replace Existing actually changes**.

The exact LogMate contract remains a live-project dependency.

---

# 11. Comparative architecture practice — same setup problem, three strategies

Fixed hypothetical professional task: user has existing operational records and wants to begin using a logbook product.

The product may allow manual entry and import. Exact LogMate behavior is not asserted.

## Direction A — front-loaded guided setup

Sequence: welcome → choose source → configure → learn main concepts → import/add → workspace.

**Strengths:** explicit orientation; prerequisites can be collected coherently; progress can be visible.

**Risks:** experts are blocked; optional education can masquerade as setup; concepts arrive before context; abandonment before first value.

**KEEP WHEN:** prerequisites truly block useful operation and dependency order is real.

**REJECT AS DEFAULT WHEN:** most steps are educational rather than operationally required.

## Direction B — workspace-first contextual onboarding

User enters a usable workspace quickly. First-use empty state exposes `Add` / `Import`; contextual help appears when each path is chosen; advanced explanation remains referenceable.

**Strengths:** fastest path to real task; expert bypass; learning has context; naturally re-enterable.

**Risks:** weak IA can hide capability; users may miss global concepts needed before choosing a path; contextual tips can become fragmented.

**KEEP WHEN:** useful work can begin without global setup and task entry points are recognizable.

## Direction C — adaptive checkpoint model

Minimal initial question(s) establish the user's immediate goal or prerequisite. Product then enters the relevant task with contextual assistance; consequential checkpoints inject required explanation before commitment; optional learning stays available separately.

**Strengths:** balances directness with prerequisite truth; avoids teaching irrelevant paths; supports heterogeneous expert users.

**Risks:** branching logic can become opaque; wrong early classification can constrain the user; personalization can create inconsistent help if not reversible.

**KEEP WHEN:** a small number of early answers materially changes required setup/help.

### STUDIO SELECTION FOR THIS FIXED EXERCISE

**Direction C with a strong B bias** is the provisional studio direction: minimize initial classification, enter the real workspace/task early, then use consequence-aware checkpoints and persistent contextual help. Do not construct a questionnaire merely to appear adaptive.

This selection is a studio judgment for the fixed hypothetical substrate, not a universal onboarding recommendation and not a LogMate production decision.

---

# 12. Onboarding content contract v0.1

For each onboarding/disclosure unit record:

- `content_id`
- `user_goal`
- `knowledge_gap`
- `domain_or_product_knowledge`
- `decision_affected`
- `risk_if_unknown`
- `earliest_useful_moment`
- `latest_safe_moment`
- `requiredness`
- `trigger`
- `surface`
- `primary_message`
- `example_or_detail`
- `action`
- `skip_allowed`
- `dismissal_scope`
- `completion_condition`
- `resume_state`
- `reentry_location`
- `replay_behavior`
- `localizer_context`
- `accessibility_notes`
- `analytics_question` (what evidence would justify revision; not surveillance by default)

### Structural invariant

If `risk_if_unknown` is material and `latest_safe_moment` is before commitment, the content cannot be placed only in optional post-commit help.

If `requiredness = optional`, blocking task completion requires separate justification.

---

# 13. Localization-ready onboarding

Onboarding is especially vulnerable to localization defects because it combines headings, instructions, examples, step counts, buttons and dynamic state.

Rules:

- do not encode sequence in English sentence fragments spread across UI regions;
- do not assume `Next` describes the next consequence adequately;
- keep step titles semantically meaningful and independently translatable;
- examples must be marked as examples, not mistaken for required literal format;
- screenshots/illustrations containing text require localization strategy or avoidance;
- allow text expansion without hiding critical controls/information;
- avoid idioms/metaphors as the only explanation of a professional concept;
- variables and counts need explicit translator context;
- do not assume Western left-to-right spatial phrases (`on the right`, `above`) are stable instructional semantics when structure can change responsively;
- preserve product/domain terminology mappings in a glossary/string system.

### STUDIO JUDGMENT

A localized onboarding flow must preserve **decision order and consequence**, not English word order.

---

# 14. Accessibility and cognitive-load boundary

W3C WAI cognitive guidance emphasizes clear purpose, familiar controls, clear structure, important-task findability, separated instructions and orientation. It also warns against changes that make navigation unpredictable.

### Transfer into Content

- name the current purpose;
- separate steps/instructions;
- expose important actions without requiring hover/discovery tricks;
- keep repeated labels consistent;
- provide enough orientation to resume after interruption;
- do not rely on memory of an earlier tutorial for current task completion;
- do not make critical help accessible only through a transient coach mark;
- preserve a persistent reference path for complex professional concepts.

### Evidence boundary

These principles are evidence-grounded design constraints. CD013 does not claim reduced cognitive load, better completion, or superior comprehension in actual users without human testing.

---

# 15. Failure taxonomy for onboarding/progressive disclosure

Audit flags:

- `FRONT_LOADED_MEMORY_DEPENDENCY` — information taught long before use and unavailable at point of need;
- `TUTORIAL_DEPENDENT_UI` — normal operation depends on remembering a prior tour;
- `OPTIONAL_AS_MANDATORY` — optional education/config blocks task without justification;
- `REQUIRED_AS_OPTIONAL` — consequence-critical knowledge can be bypassed before commitment;
- `DISCLOSURE_AFTER_DECISION` — required truth appears only after the governed decision;
- `FEATURE_CONCEALMENT` — important task/action is technically present but not reasonably discoverable;
- `EXPERT_BLOCKING` — knowledgeable users cannot proceed despite no unmet prerequisite;
- `NOVICE_ABANDONMENT` — no discoverable deeper support path;
- `SKIP_WITHOUT_REENTRY` — dismissed learning cannot be found again;
- `REPEATED_NAGGING` — dismissed education resurfaces without new reason;
- `FALSE_PROGRESS` — step/progress indicator misrepresents branching or completion;
- `GENERIC_STEP_LABEL` — process labels do not identify actual decision/object;
- `DOMAIN_RETEACHING` — content explains familiar domain basics while omitting product-specific delta;
- `HELP_AS_IA_PATCH` — education compensates for structurally hidden task architecture;
- `TRANSIENT_CRITICAL_HELP` — critical instruction exists only in ephemeral overlay/tip;
- `LOCALIZATION_SEQUENCE_COUPLING` — English grammar/spatial order carries product logic;
- `RUNTIME_REENTRY_UNVERIFIED`;
- `HUMAN_VALIDATION_NEEDED`.

---

# 16. Reproducible non-human audit assertions

A future static/runtime audit can check:

1. every required setup item has a product prerequisite/risk justification;
2. every optional item is bypassable without corrupting task state;
3. every consequence-critical item appears no later than its governed commitment;
4. every dismissible educational unit has a re-entry path unless intentionally ephemeral and justified;
5. multi-step labels identify decisions/objects rather than only `Step N`;
6. current step and saved/resume semantics are defined;
7. no critical instruction depends solely on hover, color, icon or a transient overlay;
8. expert path can reach primary task without consuming optional education;
9. novice path can reach deeper explanation without leaving the task context unnecessarily;
10. terminology is consistent with canonical product/domain mapping;
11. localization does not depend on English concatenation or fixed spatial phrasing;
12. onboarding completion is not equated with product/task readiness unless that is actually true.

These assertions test architecture/content contracts, not human success.

---

# 17. KEEP / REWORK / REJECT

## KEEP
- onboarding as knowledge transition rather than first-run screens;
- earliest-useful/latest-safe timing window;
- immediate/consequence-critical/contextual/reference disclosure classes;
- required/conditional/recommended/optional distinction;
- novice/expert assistance ladder;
- skip + resume + re-entry + replay contract;
- teaching product delta rather than indiscriminately reteaching domain basics;
- consequence-aware checkpoints;
- persistent point-of-need/reference access.

## REWORK / project-specific validation
- exact first-run architecture for LogMate/MintTap;
- whether any prerequisite belongs before workspace entry;
- exact import/setup branching;
- permission education timing;
- analytics/telemetry and privacy boundaries;
- platform-native help/replay conventions;
- human comprehension and completion tests.

## REJECT
- mandatory welcome carousel by default;
- feature-tour volume as onboarding quality;
- `Skip` without re-entry;
- `Next` as sufficient consequence label for consequential decisions;
- hiding required constraints under `Learn more`;
- forcing experts through explanations with no unmet prerequisite;
- teaching every advanced feature before first useful task;
- using onboarding to patch poor IA;
- claiming cognitive-load reduction without human evidence.

---

# 18. Project-readiness questions

Before recommending onboarding for a live product, Content must be able to answer:

1. What can a user truthfully accomplish with zero onboarding?
2. Which prerequisites are real system/domain prerequisites versus product preference?
3. What does the user already know from their professional domain?
4. What product-specific delta must be taught?
5. What can safely wait until point of need?
6. What must be known before a consequential commitment?
7. What can an expert bypass?
8. How does a novice request more depth?
9. How do skip, interruption, resume and replay work?
10. Where does persistent reference help live?
11. How does the design survive localization, narrow layouts and accessibility modes?
12. What evidence would show the onboarding is helping rather than obstructing?

If these cannot be answered, copywriting a welcome flow is premature.

---

## Stage 2 implication

CD013 materially closes the onboarding/progressive-disclosure gap in the Stage 2 map at the **system/practice** level. It adds multiple-solution comparison, explicit provisional selection, contradiction review, audit flags and project-readiness criteria.

Stage 2 remains **PRACTICE / NOT PASSED**. Major remaining surface/system gaps include search/filter/settings content, voice/tone modulation, repeated localization-ready transfer, and an integrated Stage 2 capstone/closure audit. Human comprehension/task evidence and production runtime behavior remain outside the present claim.

## OPEN / dependencies

- actual LogMate and MintTap first-run/prerequisite contracts;
- exact import/manual-entry/setup architecture in live products;
- permission and data-safety consequences;
- actual resume/re-entry persistence implementation;
- platform-specific accessibility/focus behavior for disclosures/tours;
- localized production transfer;
- human evidence: skip reasons, time-to-first-meaningful-task, recall vs point-of-need success, abandonment, re-entry findability, expert obstruction, novice comprehension.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Use `earliest useful / latest safe`, requiredness and re-entry fields when defining disclosure/step state. Interaction must own skip/resume persistence and whether earlier choices invalidate later work.

### Web
Transfer-test disclosure controls, route/resume/replay, keyboard/focus, narrow/enlarged text, direct entry to contextual help and persistent reference access. Do not assume coach-mark visibility equals accessibility.

### Type
Use real multi-step headings, consequence text, examples and professional identifiers as wrapping/fallback/localization stress. Do not shorten semantic requirements to maintain preferred geometry.

### Color
Required/optional/current/completed/warning meaning must survive color removal. Color can reinforce progress but not define it alone.

## Evidence level

**AUTHORITATIVE ACCESSIBILITY SOURCE CHECK + CROSS-DOMAIN TRANSFER + DEEP SYSTEM SYNTHESIS + THREE-ARCHITECTURE COMPARATIVE PRACTICE + CONTRADICTION REVIEW + REPRODUCIBLE AUDIT MODEL + PROJECT-READINESS FRAMEWORK. No human, production runtime, localized-product or live-project PASS claimed.**
