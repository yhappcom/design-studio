# CD028 — Executable Localization Release Gate

Status: **STAGE 3 PRACTICE — EXECUTABLE PRODUCTION-GOVERNANCE TRANSFER / NOT PASSED**  
Date: 2026-09-16

## Purpose

Convert CD027's production localization governance into a bounded machine-checkable release manifest and adversarial gate. This is not a real locale release; it tests whether the proposed governance can reject specific structurally unsafe release states.

## RELATED DOMAIN CHECK

- **Type T022:** operational literals remain separate from locale-formatted values; actual rendering remains OPEN.
- **Color C023:** release gate does not treat color as semantic authority.
- **Layout L014 / Interaction I009:** Tier 2 recovery state requires rendered and functional QA because certainty/safe action must survive runtime transfer.
- **Web W021:** future browser execution can replace placeholder `passed` fixture states with actual evidence artifacts.
- **Content CD025/CD026/CD027:** stable IDs, semantic revisions, typed variables, fallback policy and release-risk tiers are reused directly.

## Fixture

`CD028-localization-release-manifest.json` models a bounded hypothetical locale `xx` with:
- source semantic revision;
- risk-tier policy;
- approved fallback matrix;
- per-message semantic revision;
- linguistic/structural/render/functional QA states;
- plural/select coverage;
- rollback metadata;
- content/localization/QA/release approvals.

The locale is intentionally synthetic. No linguistic quality is claimed.

## Executable gate

`CD028-localization-release-gate.py` checks:
1. semantic revision freshness;
2. fallback authorization by risk tier;
3. required linguistic review;
4. structural validation;
5. render QA for consequential tiers;
6. functional QA for consequential tiers;
7. plural/select category completeness;
8. rollback metadata completeness;
9. required release approvals.

## Execution result

The clean manifest returned **0 errors / PASS**.

Eight adversarial mutations were then executed and all eight expected failures were detected:

| Mutation | Expected code | Result |
|---|---|---|
| stale semantic revision | `STALE_SEMANTIC_REVISION` | PASS |
| Tier 2 message missing with unapproved English fallback | `CRITICAL_OR_UNAPPROVED_FALLBACK` | PASS |
| required plural category removed | `PLURAL_SELECT_COVERAGE_INCOMPLETE` | PASS |
| Tier 2 rendered QA pending | `RENDER_QA_INCOMPLETE` | PASS |
| Tier 2 functional QA pending | `FUNCTIONAL_QA_INCOMPLETE` | PASS |
| required linguistic review pending | `LINGUISTIC_REVIEW_INCOMPLETE` | PASS |
| rollback semantic revision removed | `ROLLBACK_METADATA_INCOMPLETE` | PASS |
| QA approval removed | `RELEASE_APPROVAL_INCOMPLETE` | PASS |

## REPLICATION / CONTRADICTION

This repeats the mutation-testing method from CD025/CD026 for a different layer: release governance rather than message schema. The repetition is deliberate because a policy document that cannot reject unsafe release fixtures is weaker than an executable gate.

No contradiction with I009/L014 was found at the structural level. However, the manifest's `render_qa: passed` and `functional_qa: passed` are synthetic fixture inputs, **not actual Web/native evidence**. They exist only to exercise the gate logic. Real release evidence must replace them.

## Important result

A production localization system needs two distinct machines:

1. **semantic integrity gate** — is this locale resource compatible with the product/content contract?
2. **release evidence gate** — has the required level of review/QA/rollback evidence been supplied for this risk tier?

CD025/CD026 primarily address machine 1. CD028 begins machine 2.

A translation-completion percentage belongs to neither machine as authority.

## OPEN

- real CLDR-backed plural/select execution rather than declared categories;
- actual locale catalogs;
- actual translator/reviewer identities and workflow;
- TMS export/import or XLIFF/ARB/String Catalog cycle;
- actual rendered QA artifacts;
- browser/native functional state binding;
- rollback of a real build/resource bundle;
- AT and human/domain evidence.

## HANDOFFS TO OTHER SPECIALISTS

### Web
W021 can eventually emit actual `render_qa`/`functional_qa` evidence keyed by message ID + semantic revision instead of manually declared fixture values.

### Layout / Interaction
Define severity/risk mapping for actual product states; CD028's Tier 0–3 policy is a studio exercise, not a substitute for product risk classification.

### Type
Use locale release fixtures as future expansion/mixed-script corpus, especially count/date/duration plus operational literals.

### Color
No state may pass release solely because color distinguishes it; non-color semantics remain required.

## Evidence boundary

**EXECUTED:** clean manifest structural PASS + eight adversarial release-gate detections.  
**NOT CLAIMED:** real locale translation, real linguistic review, actual rendered/functional QA, actual TMS, real rollback, browser/native, AT or human evidence.

Stage 3 remains **PRACTICE / NOT PASSED**.
