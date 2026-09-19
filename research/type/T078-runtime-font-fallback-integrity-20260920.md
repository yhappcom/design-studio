# T078 — Runtime font fallback integrity

Date: 2026-09-20
Status: Stage 2 PRACTICE / H5 RUNTIME TRANSFER

## Purpose
Extend T077 from cross-surface design intent into degraded runtime conditions: delayed/failed webfont load, fallback substitution, reload/update, offline launch and route return.

## RELATED DOMAIN CHECK
Checked C108, I095/L099, W108 and CD114. Reuse their semantic-state, geometry, provenance and content invariants. This is TRANSFER VALIDATION, not a new font-selection study.

## SOURCE → PRACTICE → CRITIQUE
Browser/runtime evidence can change the actually rendered family after initial composition. Therefore a LogMate type role is not production-stable until the actual loaded family and resulting wraps/truncation are observed. Practice fixture: Home summary, ledger row/detail, Add Flight validation/review, import preview and recovery strings under intended font, declared fallback, blocked-font first load and reload.

Critique rule: FAIL if fallback changes field identity, hides required consequence/recovery text, destroys a protected comparison relationship, or is compensated by negative tracking/glyph narrowing. Layout adaptation precedes semantic shortening.

## Reproducible validation
For each surface record requested family, actual family, font-load state, viewport, text-spacing/enlargement state, line count, truncation recovery and protected comparison-axis geometry. Repeat first-load and reload. Hand to Web for served-engine provenance.

## Gate discipline
T021 remains upstream. Widths/sidebearings stay frozen and kerning OFF. Runtime fallback evidence cannot be used to bypass drawing → general spacing → residual kerning.

## OPEN
Exact production mono/fallback, T021 closure, independent-engine/device rendering, AT and human recognition remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web: treat fallback metric change as a runtime geometry input, not a Type defect to hide. Content: do not shorten necessary strings solely to preserve preferred fallback geometry. Color: font-load state is not a semantic color state.