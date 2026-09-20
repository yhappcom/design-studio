# T087 — Candidate 07 Independent-Concept Type Transfer

Date: 2026-09-20
State: **TRANSFER VALIDATION / PRACTICE — NOT PASS**

## PURPOSE
Test whether the current Type system can support a materially different LogMate Home concept (`Candidate 07 — Linebook`) without copying Candidate 05 typography and without bypassing T021.

## RELATED DOMAIN CHECK
- **Type:** T021 remains upstream: bounded drawing before general spacing, residual kerning last. T086 runtime rules remain reusable.
- **Color:** Candidate 07 uses restrained state accent; Type must not create pseudo-state through weight alone.
- **Layout/Interaction:** ledger rules and repeated axes make column fit and label/value ownership critical.
- **Web:** runtime/resolved-font evidence is still absent.
- **Content:** canonical English strings are fixed-first; geometry does not authorize abbreviation.

## EVIDENCE
**SOURCE / PROJECT EVIDENCE.** Candidate 07 post-render review records compact editorial hierarchy, stable numerics, 390×844 light/dark renders, and leaves production font/fallback/scaling OPEN.

**TRANSFER VALIDATION.** Candidate 07 is intentionally not treated as a derivative of Candidate 05. The transferable Type invariant is role separation, not font-size/weight coordinates:
1. product navigation/section language remains mature proportional UI;
2. operational identifiers/numerics may use mono/tabular treatment only where comparison or representation requires it;
3. actual resolved family/fallback must be captured before any fit claim;
4. enlarged/nonlinear text scaling must be allowed to recompose the ledger rather than be suppressed.

## PRACTICE / CRITIQUE
Candidate 07's denser editorial hierarchy creates a stronger temptation to solve fit with tracking or premature custom metrics. Reject:
- negative tracking as a width fix;
- glyph narrowing to preserve the 390px composition;
- semantic abbreviation solely for line fit;
- kerning work while T021 drawing/general spacing remain immature.

Use the Candidate 07 strings and repeated flight/date/time/numeric rows as a later spacing/fallback stress corpus after the drawing gate.

## REPRODUCIBLE VALIDATION
When exact runtime exists, record for baseline + maximum supported text scaling + forced mature fallback: source commit, platform, TextScaler/accessibility setting, requested family, resolved family where observable, line breaks, clipping, row growth, and any changed semantic order. Repeat the same build twice before cross-platform transfer.

## RESULT
No Type gate changes. Candidate 07 is useful because it tests whether Type principles survive a different visual concept; it does not justify a new typeface or later-gate work.

## OPEN
T021 drawing PASS, general spacing, residual kerning, production font/fallback, runtime scaling, AT and human reading evidence.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web should treat text growth and fallback as allowed geometry-changing inputs. Content should not shorten canonical labels to rescue the ledger. Color/Interaction should not rely on typographic weight as the only state signal.