# W089 — Keyboard-layout shortcut served-runtime closure

Date: 2026-09-19
Stage: 3 PRACTICE
Purpose: move I076/CD095/L080/C089/T058 into real served-browser evidence rather than another isolated Chromium micro-test.

## RELATED DOMAIN CHECK
I076 defines shortcut identity/routing oracle; L080 geometry; C089 state paint; CD095 semantic copy; T058 rendering transfer remains gated by T021.

## SOURCE / IMPLEMENTATION BOUNDARY
Flutter HardwareKeyboard distinguishes physical/logical key data and produced character; `KeyEvent.character` explicitly does not model IME edits. Flutter Shortcuts routes key events through activators/intents/actions. These framework facts are not evidence that all browsers/layouts/IMEs behave identically.

## CLOSURE MANIFEST
For each scenario capture build/commit, browser+version, OS, keyboard layout, input method, locale, viewport/zoom/theme/forced-colors, focused semantic ID, composition range, physical/logical/character event identity where observable, modifiers, matched activator, resolved Intent/Action, scope/eligibility, editor value/selection, configuration branch/inverse/projection hash, visible/a11y status, action/hint/focus/editor rectangles, scroll/obscuration and runtime exceptions.

Scenario families: US Ctrl/Cmd+Z; Korean layout IME inactive/active; layout switch while focus remains; dead/combining-key adjacency where available; explicit Undo button equivalence; any printable-character accelerator if product introduces one.

## ACCEPTANCE
Run twice per available path. Promotion ladder: production Web build → served primary engine → independent engine → 200% → forced-colors. A matching key glyph is not a PASS; intended semantic consequence and competing editor/configuration histories must be proven. Browser/OS limitations are recorded, not normalized away.

WCAG 2.2 SC 2.1.4 is specifically checked if a character-only shortcut exists. Focus Not Obscured remains part of geometry acceptance.

## PERFORMANCE
Lighthouse/DevTools/CI remain LAB. Only provenance-bearing aggregate/RUM can support FIELD LCP/INP/CLS claims.

## OPEN
No W089 runtime, independent-browser, physical-layout/IME, screen-reader, field-CWV or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Return routing contradictions to Interaction, string/hint issues to Content, geometry to Layout, state-paint failures to Color, and reproduced font/fallback failures to Type.