# W072 — Runtime Diagnostic Provenance Gate

## PURPOSE
**TRANSFER VALIDATION / STAGE-CLOSURE SUPPORT.** Make failure localization itself provenance-bearing so anonymous widget exceptions cannot be promoted into browser/product conclusions.

## RELATED DOMAIN CHECK
T041 supplies Type causal boundaries; C072 requires visible state surface; L063 supplies exact spatial owner; I059 supplies Material ownership; CD078 preserves semantic scenario identity.

## EXECUTED EVIDENCE
MintTap run `35255971379` is a real Flutter widget-runtime EXECUTED-FAIL. Analyzer passed, but widget tests failed before Web build. Current logs preserve repository, commit, ref, run ID, runner OS, Flutter/Dart versions and scenario names, but the RenderFlex failures are reduced to overflow amounts at the shared `pumpLab` expectation. Web build/served browser remain NOT EXECUTED.

## PRACTICE
Extend the next evidence manifest with `scenario_id`, exact failing widget/creator chain, viewport/text scaler, failure class, owner domain, repair commit, and post-repair result. Diagnostic capture must happen before exception summarization. Only a green same-build widget matrix may unlock production Web build and served-runtime validation.

## CRITIQUE
Do not infer browser failure from widget failure, or browser PASS from build success. Do not label synthetic/Lighthouse measurements field LCP/INP/CLS. Field evidence requires provenance-bearing aggregate/RUM data.

## VALIDATION / OPEN
W071 ladder remains authoritative: widget → production build → served runtime → primary engine → independent engine → network/state transfer → field evidence. Screen reader, physical device and human UX remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
The manifest becomes the shared evidence identity for T041/C072/L063/I059/CD078 critique.