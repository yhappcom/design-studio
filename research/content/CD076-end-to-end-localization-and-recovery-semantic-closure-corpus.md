# CD076 — End-to-end localization and recovery semantic closure corpus

## Purpose
Unify forms, state, retrieval/history, tone and localization into a finite product-transfer corpus that can be executed after the spatial/Material repair.

## Stage
Stage 3 PRACTICE / NOT PASSED.

## Protected semantic invariants
- distribution ≠ profit;
- partial/unavailable ≠ zero;
- estimated ≠ final;
- gross ≠ net;
- refund/additional-tax sign and consequence remain explicit;
- ambiguous outcome ≠ known success or known failure.

## Corpus families
### Financial display
Long portfolio/ticker context; signed and large KRW/USD; positive income + negative total return; zero vs unavailable; estimated/final ROC; partial/complete data; gross/net tax basis.

### Forms
Label, helper, validation, correction, submit, pending and confirmation must preserve the same field meaning. Error text must identify what can be corrected without silently changing units/currency/date semantics.

### Recovery
Maintain separate scripts/state labels for known failure and ambiguous outcome. Ambiguous consequential actions require verification/reconciliation before retry where duplication is possible.

### Retrieval/history
The same event must retain amount, sign, basis, date, status and qualifier meaning in detail, history, export/share surfaces and restored state.

### Localization
Trace `source key/API meaning → typed variables → locale/fallback → number/currency/date formatting → visible UI → accessible name/value → recovery/history/export`.

## Repair-time copy classification
Every changed string is one of:
- REFLOW_ONLY
- MEANING_EQUIVALENT_ABBREVIATION
- TERMINOLOGY_SUBSTITUTION
- SEMANTIC_DELETION
- STATE_CONSEQUENCE_CHANGE

Only the first two can normally be accepted as fit-oriented changes without a separate semantic review. The latter three require explicit Content critique and cross-domain handoff.

## Reproducible validation
Use the same build/scenario IDs as Layout/Interaction/Web. Record locale, source key, rendered string, typed variables, fallback path, visible truncation/wrap, accessible label/value, resulting state and history/export realization.

## Evidence boundary
Synthetic English fixtures are useful for geometry but do not close product localization. Linguistic quality, AT comprehension and representative-human task comprehension remain OPEN until observed.

## RELATED DOMAIN CHECK
Type checks rendering/fallback; Color checks state redundancy; Layout checks fit/reflow; Interaction checks consequence/recovery; Web checks served runtime and browser transfer.

## Next evidence
Once the compact/Material smoke is repaired, execute this corpus through MintTap's actual Dart localization pipeline before claiming Content Stage 3 closure.