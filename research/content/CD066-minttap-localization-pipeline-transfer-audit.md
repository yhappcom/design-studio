# CD066 — MintTap Localization Pipeline Product-Transfer Audit

Status: TRANSFER VALIDATION / STATIC PRODUCT EVIDENCE; runtime locale round-trip OPEN.

## RELATED DOMAIN CHECK
T029 protects rendering truth; C060 preserves state without hue; L051/I047 preserve spatial/behavioral meaning; W060/W059 own actual runtime realization.

## Product evidence
MintTap branch `design-lab/minttap-1.0.29` contains a production localization directory with `app_locale.dart`, a large `app_strings.dart`, locale sync, date/currency/country display helpers and trend-color localization. This is the current product implementation target.

## CONTRADICTION REVIEW
Earlier Content queue language treated Flutter ARB/TMS-equivalent execution as if ARB were the concrete MintTap path. Static product inspection shows that assumption is too narrow. The canonical requirement is instead:

`product truth → semantic message contract → current locale pipeline → visible/accessibility realization → history/export realization`.

ARB/TMS remains useful as a method comparison or future architecture, but cannot be required merely because Flutter supports it.

## PRACTICE — current-pipeline corpus
Execute CD065 concepts through the actual Dart pipeline first: portfolio value vs invested capital; total performance vs distributions; gross/net; estimated/final ROC; partial/unavailable/zero; positive/negative tax adjustment; ambiguous outcome; history/export continuity; KRW/USD; long labels.

For each message capture source key/API, locale selection, variables/types, visible string, accessibility string if distinct, history/export form, and fallback behavior. Locale-specific market color convention must never substitute for explicit semantic wording.

## Failure classes
- SOURCE_KEY_COLLISION
- VARIABLE_TYPE_DRIFT
- LOCALE_STATE_COLLISION
- VISIBLE_ACCESSIBLE_DRIFT
- HISTORY_EXPORT_DRIFT
- FALLBACK_SEMANTIC_LOSS
- FIT_DRIVEN_TRUTH_DELETION
- COLOR_REFERENCE_DEPENDENCY

## Validation boundary
Static source confirms the pipeline exists; it does not prove every locale path, plural/format behavior, accessibility surface or export/history path. Runtime locale switching, fallback, persistence, screen-reader output and linguistic review remain OPEN.

## HANDOFFS
W060 corrects the runtime target to the actual Dart localization path. T029/L051 must absorb long-string pressure rather than request semantic deletion. C060 keeps locale color conventions redundant. I047 verifies state wording against actual state/recovery.