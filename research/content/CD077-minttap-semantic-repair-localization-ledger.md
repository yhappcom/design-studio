# CD077 — MintTap Semantic Repair & Localization Ledger

Date: 2026-09-18
Purpose: **TRANSFER VALIDATION / SYSTEMS PRACTICE**
Stage: Stage 3 PRACTICE.

## QUESTION
How can MintTap repair compact geometry and recovery states without silently changing financial meaning, and how should the actual Dart localization pipeline be validated afterward?

## PROTECTED SEMANTICS
The following distinctions are invariants unless product truth explicitly changes:
- distribution ≠ profit;
- partial/unavailable ≠ zero;
- estimated ≠ final;
- gross ≠ net;
- tax refund/additional tax sign remains explicit;
- pending ≠ known failure;
- ambiguous outcome ≠ known success/failure;
- verify/reconcile ≠ ordinary retry.

## PRACTICE — repair string ledger
Every changed user-facing string receives one class:

1. `REFLOW_ONLY` — same string/meaning, layout changes.
2. `MEANING_EQUIVALENT_ABBREVIATION` — shorter realization with documented equivalence.
3. `TERMINOLOGY_SUBSTITUTION` — concept label changed; requires cross-surface audit.
4. `SEMANTIC_DELETION` — required distinction removed; reject unless product truth changed.
5. `STATE_CONSEQUENCE_CHANGE` — wording now asserts different state/action/consequence; Interaction dependency required.

No abbreviation is accepted solely because it makes the AppBar or card fit.

## LOCALIZATION EXECUTION LEDGER
For each stress scenario trace:

`source key/API truth → typed variables → locale/fallback → number/currency/date formatting → visible UI → accessible value → recovery/history/export`

Corpus:
- long portfolio names;
- signed/large KRW and USD;
- estimated/final ROC;
- partial/unavailable data;
- positive distribution + negative total return;
- gross/net;
- tax refund/additional-tax consequences;
- pending/known failure/ambiguous/verify/reconcile/retry.

Record locale, source key, variables/types, rendered string, truncation/wrap, accessible string/state and downstream history/export realization.

## CRITIQUE
Synthetic English fixtures can reveal geometry pressure but cannot establish localization closure. Likewise, successful translation rendering does not prove linguistic quality or human comprehension. Those require appropriate linguistic/human review.

## ACCESSIBILITY / PLATFORM CONNECTION
Flutter's text scaling normally follows user/platform settings, so localization stress must be combined with enlarged-text conditions rather than tested only at default scale.

- https://api.flutter.dev/flutter/widgets/Text/textScaler.html
- https://docs.flutter.dev/ui/accessibility/ui-design-and-styling

## RELATED DOMAIN CHECK
- Type: T040 owns rendering/fallback causality; Content does not prescribe kerning.
- Color: C071 requires non-color semantic cues for state distinctions.
- Layout: L062 must recompose around necessary language before requesting shortening.
- Interaction: I058 supplies actual state/action/recovery truth.
- Web: W071 executes real locale strings in served runtime and returns fit/semantics failures.
- UX: automated string/state continuity is not human comprehension, trust or workload evidence.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives protected strings and abbreviation classifications. Interaction receives any wording that appears to alter state/consequence. Web receives the finite localization corpus. Type receives only reproduced fallback/rendering defects.

## EVIDENCE BOUNDARY
No actual MintTap locale round-trip is executed here. No linguistic-review, AT-comprehension or representative-human task PASS is claimed.
