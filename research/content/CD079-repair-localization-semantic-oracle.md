# CD079 — Repair & Localization Semantic Oracle

Date: 2026-09-18
Stage: 3 PRACTICE
Purpose: semantic oracle for repair regression and later localization transfer

## Problem
A layout repair can appear green by shortening or collapsing meaning. CD078 already requires stable scenario identity; CD079 defines the semantic oracle that decides whether a repair/localization output still represents the same product truth.

## Oracle dimensions
For every finite-corpus case record source truth, typed variables, visible string, accessible name/value where available, recovery message/action, and history/export representation.

Protected distinctions:
- distribution vs profit;
- partial/unavailable vs numeric zero;
- estimated vs final;
- gross vs net;
- refund/additional-tax sign and consequence;
- pending vs known failure vs ambiguous outcome;
- verify/reconcile vs retry;
- currency/date/number unit and sign.

## PRACTICE
Before L064/I060 repair, snapshot the exact semantic scenario payload and visible strings. After repair classify every content change as:
- `REFLOW_ONLY`;
- `MEANING_EQUIVALENT_ABBREVIATION`;
- `TERMINOLOGY_SUBSTITUTION`;
- `SEMANTIC_DELETION`;
- `STATE_CONSEQUENCE_CHANGE`.

Only the first two can be accepted without renewed semantic review, and abbreviation still requires locale/translatability review. Geometry obtained through semantic deletion/state collapse is a Content FAIL even if the widget test is green.

After smoke repair, run the corpus through the actual MintTap Dart localization/formatting path. Trace source/API truth → typed variables → locale/fallback → number/currency/date formatting → visible/accessibility output → recovery/history/export. Synthetic English fixture remains geometry evidence only.

## CRITIQUE
String length is not a semantic metric. Conversely, preserving every English surface form verbatim is not localization quality. The oracle protects distinctions and consequences, while allowing locale-appropriate wording when meaning is equivalent.

## REPRODUCIBLE VALIDATION
Use stable scenario IDs shared with L064/W073. Diff source payload, visible output and recovery/history/export across repair commits and locales. Flag any unreviewed semantic deletion or state-consequence change. Human linguistic quality/comprehension remains OPEN until appropriate review/testing.

## RELATED DOMAIN CHECK
- Type T042 records rendering context without shortening copy.
- Color C073 requires explicit non-color semantic cues.
- Layout L064 must repair spatial allocation before requesting semantic deletion.
- Interaction I060/I058 defines actual state/recovery truth.
- Web W073 carries the same scenario IDs into browser/runtime localization.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives long-string pressure without permission to delete meaning. Type receives script/fallback cases. Interaction receives wording evidence that exposes an ambiguous state contract. Web receives the finite locale corpus and oracle fields.

## Evidence boundary
No actual MintTap locale runtime round trip, linguistic review, AT comprehension or representative-human task PASS is claimed.
