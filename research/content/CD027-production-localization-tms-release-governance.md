# CD027 — Production Localization / TMS / Release Governance

Status: **STAGE 3 PRACTICE — PRODUCTION-SYSTEM ARCHITECTURE / NOT PASSED**  
Date: 2026-09-16

## Purpose

Move the Stage 3 content system from semantic-schema validation into a production localization operating model. The question is not "how do we translate strings?" but:

> How does product truth move from authored source content through localization work, runtime resources, QA, release, rollback and later semantic change without losing certainty, consequence, recovery, variable semantics or professional-domain meaning?

This is architecture and governance practice. It does not claim that a specific commercial TMS, locale, translator team or production app has been validated.

## RELATED DOMAIN CHECK

### Type
T022 requires literal airport/registration/flight/time corpora and mixed-script behavior to remain explicit. Localization may change prose and formatting but must not silently transliterate/reformat operational identifiers unless the product/domain contract explicitly allows it.

### Color
C023 reinforces state but does not define it. Translation/release QA must preserve textual state identity when authored colors are transformed or unavailable.

### Layout / Interaction
L014/I009 remain authoritative for runtime state, safe action, certainty and reflow invariants. Localization cannot strengthen `outcome_unknown` to `failed` or invent retry because a translator prefers a shorter sentence.

### Web
W021 is the future rendered transfer surface. CD027 produces release metadata and fixtures that can later be bound to browser/native runtime tests. Browser evidence remains OPEN.

### Content
CD020–CD023 define registries, cross-channel projections and governance. CD025/CD026 add executable semantic lint and versioned transfer checks. CD027 extends those contracts into production localization/release operations rather than creating a parallel translation system.

## SOURCE

Authoritative platform/source findings used for this block:

- Apple localization documentation treats internationalization as preparation of code/UI for localization; String Catalogs manage localizable strings, translations, plurals and device variation; localizable APIs can carry comments/context; exports can include screenshots and XLIFF/localization catalogs for localizers; Apple explicitly recommends native-speaker testing when machine translation is used.
- Unicode CLDR plural rules show that languages do not share English's binary singular/plural model. CLDR plural categories may include `zero`, `one`, `two`, `few`, `many`, `other`, and category assignment is locale-specific and may differ for fractional values.
- CLDR release material also demonstrates that localization data/rules evolve over time; therefore locale realization has versioned dependencies, not timeless rules.

These sources support the architecture direction but do not prescribe this studio's exact workflow.

---

## 1. Localization is a release pipeline, not a translation handoff

### SYNTHESIS

Production localization requires at least these layers:

`authoritative product state/event`
→ `semantic content contract`
→ `source-English realization`
→ `localization package/context`
→ `locale realization`
→ `linguistic review`
→ `structural/semantic validation`
→ `rendered functional QA`
→ `release eligibility`
→ `runtime fallback/rollback`
→ `post-release change propagation`

A translation can be linguistically fluent and still be a product defect if it changes certainty, consequence, object identity, safe action, freshness, or variable meaning.

### STUDIO JUDGMENT

**Localization release status must be attached to a semantic revision, not merely to a string key.**

---

## 2. Canonical ownership model

A production system needs distinct authorities:

- **Interaction/product logic owner** — authoritative state/action/recovery behavior;
- **Content owner** — concept, message family, source-English semantic realization, context, tone ceiling, variable semantics;
- **Localization owner/vendor/TMS process** — locale realization workflow and linguistic status;
- **Engineering** — resource extraction/import, runtime selection, formatting, fallback, build integration;
- **QA** — structural, linguistic, rendered, functional and regression evidence;
- **Release owner** — decides whether locale/build meets declared gate.

### REJECT

- translator decides product state because source is ambiguous;
- engineer edits source wording in code without semantic review;
- content designer marks locale PASS without linguistic competence/evidence;
- one role silently owns state truth, translation, runtime and release approval.

---

## 3. Localization work-unit contract v0.1

Each localizable message family should expose enough context to translate the product meaning rather than only the English sentence.

Recommended fields:

- `message_id`
- `semantic_revision`
- `concept_id`
- `state_id`
- `action_id`
- `certainty`
- `required_semantics`
- `source_text`
- `source_revision`
- `surface_role`
- `channel`
- `user_goal`
- `consequence`
- `recovery_or_safe_action`
- `tone_intent`
- `tone_ceiling`
- `variables[]`
  - name
  - semantic type
  - sample value
  - localizable/literal
  - formatting owner
  - bidi policy where applicable
- `plural_or_select_requirements`
- `character_or_geometry_note` only as implementation context, never as permission to delete meaning
- `screenshot_or_surface_reference`
- `do_not_translate_terms`
- `term_registry_refs`
- `localizer_note`
- `source_owner`
- `locale_status`
- `review_status`
- `qa_status`
- `release_status`

### STUDIO RULE

A character limit is subordinate to required semantics. If the surface cannot carry the proposition, escalate to recomposition/alternate projection instead of authorizing semantic loss.

---

## 4. Status machine for localization work

A binary `translated/not translated` flag is insufficient.

Proposed bounded status model:

`source_draft`
→ `source_semantic_reviewed`
→ `ready_for_localization`
→ `locale_in_progress`
→ `locale_linguistic_reviewed`
→ `locale_structural_validated`
→ `locale_render_qa_pending`
→ `locale_release_candidate`
→ `released`

Exceptional states:
- `source_changed`
- `locale_stale`
- `blocked_context_missing`
- `blocked_domain_review`
- `rejected_semantic_drift`
- `rejected_runtime_defect`
- `rolled_back`
- `deprecated`

### Critical distinction

`translated` does not mean `reviewed`; `reviewed` does not mean `runtime-safe`; `runtime-safe` does not mean `human-comprehension validated`.

---

## 5. Change propagation and staleness

CD026 establishes that semantic identity can remain stable across wording changes but not across incompatible state/certainty/action changes.

Production propagation therefore classifies changes:

### A. Source wording-only
Semantic contract unchanged. Existing translations may remain potentially reusable, but require policy-defined review if wording/context changed materially.

### B. Context-only
No source text change, but surface, audience, screenshot, tone or usage changed. Existing translation cannot automatically be assumed valid.

### C. Variable-schema change
Variable added/removed/type changed. Locale resources become structurally stale until validated.

### D. Semantic-contract change
State/certainty/consequence/action/recovery/required semantics changed. Existing translations must be marked stale/retranslation-required even if the English string barely changed.

### E. Locale-data dependency change
CLDR/runtime formatting behavior or supported locale/script behavior changes. Requires targeted regression rather than source-string churn.

### F. Channel-projection change
Notification/email/history eligibility or freshness/revalidation changes. Channel-specific locale realization and runtime action path require review.

---

## 6. Translation memory is evidence reuse, not semantic authority

### SYNTHESIS

A TMS translation-memory match can reduce repeated work but cannot override the current semantic contract.

Exact English source match does not prove semantic equivalence if:
- state changed;
- surface changed;
- object changed;
- variable meaning changed;
- tone/risk changed;
- action changed;
- professional terminology context changed.

### STUDIO JUDGMENT

TM reuse should be gated by semantic identity/context compatibility, not source-string similarity alone.

Potential statuses:
- `reuse_safe_by_contract`
- `reuse_review_required`
- `reuse_rejected_semantic_change`

This is a governance model, not a claim about a specific TMS feature.

---

## 7. Machine translation / AI translation boundary

Machine/AI translation can be a production input but not automatic proof of release quality.

Required controls for consequential professional content:
- semantic contract/context supplied;
- variables protected;
- do-not-translate identifiers protected;
- terminology constraints supplied;
- locale review appropriate to consequence/risk;
- structural lint;
- rendered/functional QA before release where material.

### Risk-tier proposal

- **Tier 0 — low consequence/static discovery:** automated draft may be acceptable pending ordinary QA policy.
- **Tier 1 — routine task content:** linguistic review + structural validation.
- **Tier 2 — state/recovery/consequence:** domain-aware review + semantic validation + runtime QA.
- **Tier 3 — financial, legal, safety/operational or irreversible consequence:** product/domain authority + qualified linguistic review + functional/runtime release gate; machine output alone cannot authorize release.

This is STUDIO JUDGMENT and must be adapted to actual product/regulatory risk.

---

## 8. Plural/select/message grammar contract

### SOURCE + SYNTHESIS

CLDR demonstrates that plural categories vary by locale and can include more than `one/other`; fractions can also affect category selection. Therefore English-style branching such as `count == 1` is not a global message architecture.

### Contract

For quantity-sensitive messages, store:
- semantic variable type (`count`, `duration`, etc.);
- whether cardinal/ordinal/range semantics apply;
- locale-aware category selection owner;
- complete message variants or a message-format representation that permits grammar to vary around the variable;
- tests for representative category values including fractions where relevant.

### REJECT

- `1 item / N items` hard-coded as universal;
- `1 flight(s)`;
- concatenating localized number + English-derived noun fragment;
- assuming category `one` means traditional grammatical singular in every language;
- treating all decimals as `other` without locale evidence.

---

## 9. Formatting ownership

Typed variables separate semantic value from display realization.

| Type | Semantic owner | Locale realization owner | Critical rule |
|---|---|---|---|
| operational identifier | product/domain | usually literal policy | never silently numeric-format |
| count | product | locale formatter/message system | plural/select category locale-dependent |
| datetime | product instant/local-time semantics | locale formatter | timezone/context must remain defined |
| duration | product duration | locale formatter/message system | unit width/plural may vary |
| currency | product amount + currency | locale formatter | symbol alone must not change currency identity |
| percentage | product numeric meaning | locale formatter | preserve basis/meaning |
| user-entered text | user/data | display/bidi policy | do not translate user data |

---

## 10. Fallback policy

Fallback is a product decision, not a harmless technical default.

Possible policies by message risk:
- approved parent-locale fallback;
- approved source-English fallback;
- block locale release for missing critical message;
- suppress nonessential channel projection;
- use platform-native localized content when authoritative and semantically compatible.

### Critical rule

A fallback must not silently remove required semantics or strengthen certainty. CD026 structural fallback checks remain applicable.

### Release implication

A locale may be partially complete for low-risk surfaces while being **not releasable** if a Tier 2/3 critical state lacks an approved realization/fallback.

---

## 11. QA stack

No single QA pass covers localization quality.

### Q0 — source semantic review
Is the English source itself correct, plain, globally readable and semantically complete?

### Q1 — structural validation
Keys, variables, types, literals, plural/select completeness, forbidden concatenation, semantic revision compatibility.

### Q2 — linguistic review
Naturalness, grammar, terminology, tone intent, locale appropriateness. Requires qualified linguistic evidence; Content specialist cannot simulate it.

### Q3 — rendered localization QA
Clipping, wrapping, hierarchy, bidi, mixed-script identifiers, text expansion, control geometry, state adjacency.

### Q4 — functional localization QA
Correct message for actual runtime state, correct variable values/formatting, fallback behavior, deep links/actions, persistence and channel freshness.

### Q5 — accessibility QA
Programmatic names/status, reading/announcement behavior, text alternatives and locale-specific AT behavior where applicable.

### Q6 — human/domain validation
Comprehension, terminology acceptance, task performance, trust/workload where the product risk justifies it.

Passing Q1 does not imply Q2–Q6.

---

## 12. Release gate model

A locale release candidate should have an explicit manifest rather than a vague "translation complete" percentage.

Manifest dimensions:
- semantic revision coverage;
- critical-message coverage by risk tier;
- missing/fallback inventory;
- variable/plural/select structural status;
- linguistic-review status;
- rendered QA status by target surface/platform;
- functional QA status;
- unresolved defects and severity;
- approved exceptions;
- rollback target;
- responsible approvers.

### STUDIO RULE

**Completion percentage is inventory information, not release authority.**

95% translated may be unreleasable if the missing 5% contains outcome-unknown recovery or destructive confirmation; 80% may be acceptable for a deliberately scoped beta locale if all exposed critical flows are covered and unsupported surfaces are not exposed.

---

## 13. Rollback and emergency correction

Localization defects need rollback semantics.

Possible defect classes:
- linguistic awkwardness — normal correction;
- terminology inconsistency — targeted correction + glossary propagation;
- semantic drift — urgent locale correction/release block;
- wrong action/consequence — high-severity rollback/block;
- malformed variable/runtime crash — engineering rollback/block;
- unsafe fallback — locale/surface disable or corrected fallback;
- stale notification action — runtime action revalidation, not copy-only fix.

### Rule

Rollback must identify both **content revision** and **semantic contract revision**. Reverting only the visible string can be wrong if product behavior changed simultaneously.

---

## 14. Terminology governance in production

Terminology registry entries should carry:
- concept ID;
- preferred source term;
- definition;
- forbidden/legacy synonyms;
- domain authority/source;
- grammatical notes where known;
- literal/localizable classification;
- locale equivalents with review status;
- affected message families;
- owner;
- deprecation/migration history.

Professional terms should not be "simplified" solely for consumer tone. Product-created terminology, however, must be challenged if users are expected to learn unnecessary concepts.

---

## 15. Production anti-patterns

Flag:
- `TRANSLATION_COMPLETE_EQUALS_RELEASE_READY`
- `TM_MATCH_EQUALS_SEMANTIC_MATCH`
- `SOURCE_STRING_AS_IDENTITY`
- `SEMANTIC_CHANGE_WITHOUT_LOCALE_STALENESS`
- `VARIABLE_SCHEMA_CHANGE_WITHOUT_REVIEW`
- `MISSING_LOCALIZER_CONTEXT`
- `CRITICAL_MESSAGE_UNAPPROVED_FALLBACK`
- `ENGLISH_BINARY_PLURAL_BRANCH`
- `UNPROTECTED_OPERATIONAL_LITERAL`
- `MACHINE_TRANSLATION_AUTO_RELEASE`
- `LINGUISTIC_REVIEW_CLAIM_WITHOUT_REVIEWER`
- `RUNTIME_QA_INFERRED_FROM_CATALOG`
- `PERCENT_COMPLETE_AS_GATE`
- `ROLLBACK_STRING_WITHOUT_CONTRACT_REVISION`
- `CHANNEL_ACTION_WITHOUT_FRESHNESS_REVALIDATION`

---

## 16. Bounded release exercise

Hypothetical locale `xx` for the professional-record system:

- 100 routine labels translated;
- all routine labels structurally valid;
- `record.save.outcome_unknown` missing;
- source-English fallback exists;
- locale policy forbids English fallback for Tier 2 recovery states;
- locale completion dashboard says 99%.

### Verdict

**NOT RELEASE-ELIGIBLE for the affected flow.**

Reason: the missing 1% is consequence/recovery-critical and no approved fallback exists. Translation percentage is irrelevant to that semantic risk.

Second case:
- a notification translation says equivalent of `Save failed` while authoritative state is `outcome_unknown`.

### Verdict

**REJECTED_SEMANTIC_DRIFT.** Shorter wording cannot strengthen certainty.

Third case:
- source wording changes from `Verify the record before trying again` to a clearer English sentence but state/action/required semantics and variable schema remain unchanged.

### Verdict

Message ID may remain stable, but locale reuse is policy-dependent; translator context/source revision changes and review may still be required.

---

## 17. Stage 3 implication

CD027 closes a major conceptual systems gap: localization is now integrated with semantic versioning, ownership, translation context, TMS-style reuse, plural/select architecture, QA layers, release gating, fallback, rollback and terminology propagation.

It does **not** close Stage 3 because no real TMS/export-import cycle, real locale linguistic review, rendered/browser/native localization QA, or production release manifest has been executed.

The next useful block is not more generic localization theory. It should produce a **bounded production localization package + release manifest + executable gate checker** using the CD025/CD026 inventory, then adversarially test stale semantic revisions, critical missing locale entries, unapproved fallback, incomplete plural/select coverage and release rollback metadata.

## OPEN

- actual TMS vendor/API workflow;
- XLIFF/String Catalog/ARB/Flutter resource transfer on a live product;
- real CLDR-backed message formatting execution;
- locale-specific linguistic review;
- actual RTL/bidi rendering;
- rendered expansion/reflow;
- browser/native runtime state binding;
- screen-reader/AT localization behavior;
- human/domain comprehension evidence;
- production release/rollback exercise.

## HANDOFFS TO OTHER SPECIALISTS

### Interaction
Expose stable state/action/certainty IDs and mark semantic changes so locale staleness can be computed rather than inferred from English text.

### Web
W021 can consume release fixtures to verify actual localized state selection, fallback, pseudo/RTL rendering and actionable notification/deep-link behavior when browser execution becomes available.

### Type
Use production locale fixtures with operational literals + locale-formatted counts/time/durations as mixed-script/width stress corpora.

### Layout
Critical semantics cannot be deleted to satisfy translated geometry; L014 should treat locale expansion as recomposition input.

### Color
Release QA must verify that translated state identity remains understandable without authored hue.

## Evidence boundary

**SYSTEM ARCHITECTURE + SOURCE-GROUNDED SYNTHESIS + BOUNDED RELEASE CRITIQUE.** No commercial TMS, actual translator, locale linguistic PASS, rendered localization, production build, AT or human PASS claimed.
