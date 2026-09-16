# Content Design / UX Writing Specialist Status

Operating state: **ACTIVE — STAGE 1 PASS / STAGE 2 PASS / STAGE 3 PRACTICE — CD027/CD028 PRODUCTION LOCALIZATION GOVERNANCE + EXECUTABLE RELEASE GATE**  
Governance sync: 2026-09-16  
Primary path: `research/content/`  
Active studies: `CD027`, `CD028`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

Authority: CD018 Stage 2 closure; CD019 entry; CD020 semantic schema; CD021 inventory/localization stress; CD022 cross-channel continuity; CD023 governance/schema; CD024 executable test contract; CD025 single-snapshot lint/mutation evidence; CD026 versioned semantic transfer; **CD027 production localization/TMS/release governance; CD028 executable release-manifest gate**.

## Latest evidence

### CD027 — production localization system
Localization is now modeled as a release pipeline rather than a translation handoff:

`authoritative product state/event → semantic content contract → source-English realization → localization package/context → locale realization → linguistic review → structural/semantic validation → rendered functional QA → release eligibility → fallback/rollback → change propagation`.

The study defines ownership boundaries, localization work-unit metadata, multi-state localization workflow, semantic staleness classes, translation-memory reuse limits, machine/AI translation risk tiers, plural/select architecture, formatting ownership, fallback policy, layered QA, release manifests, rollback and terminology propagation.

Key rule: **localization release status attaches to a semantic revision, not merely a string key**. Translation completion percentage is inventory information, not release authority.

### CD028 — executable release governance
A bounded synthetic locale release manifest and deterministic Python gate were created. The clean manifest returns zero errors. Eight controlled mutations are correctly rejected:
- stale semantic revision;
- Tier 2 critical message using an unapproved source-English fallback;
- missing required plural category;
- consequential render QA pending;
- consequential functional QA pending;
- linguistic review pending;
- rollback semantic revision missing;
- QA approval missing.

This separates two machines:
1. semantic integrity gate — CD025/CD026;
2. release evidence gate — CD028.

The gate does not claim that synthetic `passed` QA fields are real rendered or linguistic evidence.

## Source-grounded internationalization result
Authoritative Apple localization guidance supports externalized/localizable resources, translator context/comments, screenshots/export workflows, plurals and locale-aware value formatting. Unicode CLDR confirms that plural categories are locale-specific and may include more than English `one/other`, with fractional behavior varying by locale. English binary plural branching is therefore not accepted as global message architecture.

## Cross-domain state
- **Interaction I009** remains authoritative for lifecycle certainty/safe action; Content risk/release policy cannot redefine actual behavior.
- **Layout L014** owns rendered preservation under reflow/zoom/RTL; critical semantics cannot be deleted to satisfy translated geometry.
- **Web W021** remains browser-execution blocked here; future W021 evidence should populate real render/functional QA artifacts keyed to message ID + semantic revision.
- **Type T022** receives operational literals plus locale-formatted counts/time/durations as mixed-script and variable-width stress material.
- **Color C023** reinforces but does not define state; locale release cannot rely on hue-only identity.

## Active queue
1. Execute a real resource-format transfer exercise: bounded source inventory → XLIFF/String-Catalog-class or Flutter ARB-class package → import/reconciliation checks, using a synthetic locale if no qualified locale reviewer is available.
2. Add CLDR-backed plural/select/date-time/duration execution where an executable environment supports authoritative locale data; distinguish formatting correctness from linguistic review.
3. Build terminology/glossary change-propagation exercise across source messages and locale package.
4. Package CD025/CD026/CD028 fixtures for W021 binding when browser execution is available.
5. Audit Stage 3 only after actual resource-transfer/reconciliation evidence and remaining systems integration are sufficient.

## OPEN
- actual TMS vendor/API workflow;
- real XLIFF/String Catalog/ARB import-export cycle;
- actual CLDR-backed plural/select/date/time/duration execution;
- locale-specific linguistic review;
- actual +30–40% rendered expansion;
- actual bidi shaping/order;
- browser/native runtime state binding;
- real route/network ambiguity;
- notification delivery;
- screen-reader/AT;
- human comprehension, trust, recovery and task performance;
- real production rollback.

## Evidence boundary
**EXECUTED:** CD025 six structural mutations; CD026 seven semantic-transfer mutations; CD028 clean release manifest + eight release-gate mutations.  
**SYSTEM ARCHITECTURE:** CD027 production localization/TMS/release model.  
**NOT CLAIMED:** real locale linguistic quality, actual translator/TMS, rendered localization, browser/native functional QA, AT, backend/network truth or human evidence.

Stage 3 remains **PRACTICE / NOT PASSED**. Next Content block should execute a bounded real resource-format localization transfer/reconciliation cycle rather than add more generic localization policy.
