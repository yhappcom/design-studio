# T028 — Pre-runtime Type Acceptance Vector

Status: PRACTICE / TRANSFER VALIDATION PREPARATION  
Date: 2026-09-17

## PURPOSE
Convert T027's failure taxonomy into a finite, product-transfer specimen contract that can be executed later without violating the open T021 drawing gate.

## RELATED DOMAIN CHECK
- Type: T021 remains drawing-first; provisional custom metrics must not drive product geometry. T026/T027 own scaling/runtime failure classification.
- Color: C058 needs signed/zero/partial/finality cases but does not own string rendering.
- Layout/Interaction: L049/I045 require semantic groups to survive reflow and focus/recovery stress.
- Web: W058 owns runtime identity/artifact packaging; no runtime PASS exists yet.
- Content: CD064 owns truth-bearing source strings and forbids semantic shortening to make geometry fit.

Analytical purpose: TRANSFER VALIDATION preparation, not new type theory.

## SOURCE CHECK
Flutter documents Android 14 nonlinear font scaling up to 200%, recommends testing maximum font size, and migrated from scalar `textScaleFactor` toward `TextScaler`. This supports treating text scale as a rendering/composition input rather than assuming a linear scalar.

## PRACTICE — finite acceptance vector
Until T021 R1 closes, use mature fallback for product-transfer specimens. Preserve these classes as exact semantic pressures rather than shortening them for fit:

1. signed USD: `-$12,345.67`, `+$0.00`;
2. signed KRW: `-₩12,345,678`, `+₩0`;
3. large portfolio value: `$1,234,567.89` / `₩1,234,567,890`;
4. ticker + identifier pressure: `BRK.B`, `CONY`, airport/registration-like uppercase controls where relevant;
5. certainty qualifier: `Estimated ROC`, `Final ROC`;
6. availability qualifier: `Partial data`, `Unavailable`;
7. basis qualifier: `After tax`, `Before tax`;
8. long localized realization supplied by Content without semantic deletion.

For each vector capture font identity/fallback, locale, viewport, TextScaler state, line count, clipping/ellipsis, numeral/punctuation ambiguity, baseline/vertical collision, and whether the failure belongs to drawing, metrics, general spacing, pair residual, fallback, composition pressure, semantic truncation or rasterization.

## CRITIQUE RULES
- A wrap is not automatically a Type failure.
- A truth-bearing qualifier removed to keep one line is a semantic-truncation failure and is handed to Content/Layout.
- A pair defect is not kerning evidence until drawing and general spacing are defensible.
- A fallback substitution is not a custom-font drawing failure.
- A provisional T021 glyph may not be promoted to production merely because a mature fallback specimen passes.

## REPRODUCIBLE VALIDATION CONTRACT
Runtime executor must bind the vector to W058 identity: commit/build/scenario, platform/browser, viewport, locale, text scaling, theme, font/fallback identity and raw screenshot/log/semantics artifacts. Same identity is consumed by C058/L049/I045/CD064.

## HANDOFFS TO OTHER SPECIALISTS
- Color receives the same signed/finality/availability cases for redundant semantic encoding.
- Layout receives measured wrapping and semantic-group pressure, not requests to shrink strings.
- Interaction receives focus/status behavior for the same state cases.
- Web receives the finite specimen list for W058 execution.
- Content retains authority over exact truth-bearing wording/localized realizations.

## EVIDENCE BOUNDARY
No T021 R1 closure, spacing closure, kerning entry, runtime raster PASS, browser/native breadth, AT or human recognition PASS is claimed. This file only makes the next execution finite and auditable.