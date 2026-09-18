# L080 — Shortcut-hint layout and input-context geometry

Date: 2026-09-19
Stage: 3 PRACTICE
Purpose: TRANSFER VALIDATION from I076 into responsive spatial evidence.

## RELATED DOMAIN CHECK
I076 owns shortcut identity/routing; CD095 owns wording; T058 owns later rendering stress; C089 owns state paint; W089 owns browser evidence. Layout must not infer command availability from proximity or keycap appearance.

## PRACTICE
Compare three structures for an eligible recovery action: action label only; label + platform shortcut hint; context-qualified recovery where competing text/configuration histories exist. Measure at baseline and 200%: owning-region box, action/hint boxes, focus box, editor box, wrapping, scroll delta, sticky/safe-area overlap and reading/semantic order.

## CRITIQUE
A shortcut hint is secondary metadata, not the primary affordance. FAIL if a hint separates from its action under reflow, if a platform-specific hint crowds out the semantic action label, if a stale/non-owning shortcut remains visually adjacent to an enabled recovery action, or if 200% text causes overlap/clipping/obscuration. WCAG 2.2 Focus Not Obscured (Minimum) remains an AA floor; Studio additionally checks unexplained displacement and ownership ambiguity.

## REPRODUCIBLE VALIDATION
Run baseline and 200% twice for each available EN/KO string and primary/alternate platform hint. Record semantic IDs before rectangles. Geometry PASS cannot override an I076 routing FAIL.

## OPEN
Actual product shortcut UI, Korean runtime strings, independent browser, forced colors, physical-device and human discoverability evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
I076 determines whether a hint is truthful. CD095 supplies semantic label/hint text. C089 must distinguish hint metadata from enabled/focus state. W089 captures served geometry. T058 later attributes clipping/wrapping only with type evidence.