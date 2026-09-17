# T025 — Accessibility Scale as Intrinsic Layout Input

Status: TRANSFER VALIDATION / PRACTICE
Date: 2026-09-17

## Question
How should product typography survive accessibility scaling without using a global clamp or sacrificing financial meaning?

## SOURCE
Flutter documents Android 14 nonlinear font scaling up to 200%, recommends testing at the maximum setting, and migrated framework APIs from scalar `textScaleFactor` assumptions toward `TextScaler`. Flutter accessibility guidance also requires interfaces to remain usable at very large text/display scale.

## PRACTICE CONTRACT
1. Treat the complete localized financial string as immutable input: sign, currency, amount, gross/net, estimate/finality and unavailable/partial qualifiers may not be removed merely to fit.
2. Prefer intrinsic sizing, wrap and component recomposition over font shrinking.
3. Do not infer one global scale multiplier from `TextScaler`; measure/render the actual role.
4. Keep mature fallback fonts while T021 drawing remains open.
5. Test representative numerals and punctuation: `₩`, `$`, `+`, `−`, `%`, commas, decimals, parentheses and long localized labels.

## CRITIQUE
A global text clamp produces superficially stable screenshots while suppressing the user's accessibility preference. Conversely, blindly doubling every non-text dimension can also create poor composition because nonlinear scaling is role-dependent. The correct design response is resilient composition, not a universal multiplier.

## REPRODUCIBLE VALIDATION
For each exact build/scenario identity capture default and maximum supported text scaling, narrow and wide layouts, KRW/USD, positive/negative/zero, long localization and partial/unavailable states. Record overflow, clipping, wrapping, hierarchy reversal, fallback substitution and lost qualifiers. Runtime execution remains OPEN until artifacts exist.

## RELATED DOMAIN CHECK
- Color C055: semantic state cannot be rescued by truncating qualifiers.
- Layout L046: protected semantic groups must recompose rather than shrink.
- Interaction I042: controls and recovery remain reachable after reflow.
- Web W055: runtime/build identity owns executable artifact evidence.
- Content CD061: semantic ledger supplies immutable string truth.

## Gate effect
No Stage 2 PASS. T021 drawing remains upstream of spacing/kerning closure; T025 cannot be used to hide drawing defects.