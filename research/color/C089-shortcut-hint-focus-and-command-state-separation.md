# C089 — Shortcut hint, focus and command-state separation

Date: 2026-09-19
Stage: 3 PRACTICE
Purpose: TRANSFER VALIDATION of I076/L080 into semantic color-state integrity.

## RELATED DOMAIN CHECK
I076 owns physical/logical/character/IME command identity. L080 owns hint geometry. CD095 owns wording. W089 owns rendered browser evidence. Type transfer remains gated by T021.

## SYSTEMS PRACTICE
Model independent axes: `focus owner`, `command eligible/ineligible`, `shortcut hint present/absent`, `composition active/inactive`, `selection/caret`, `recovery available/stale/superseded`, `success/failure/no-op`. Map each to token → paint owner → visible surface → non-color cue → accessible meaning.

## CRITIQUE
FAIL if hint tint implies command eligibility; if disabled/stale recovery and secondary shortcut metadata collapse to the same visual state; if composition decoration is confused with focus/validation; or if forced-colors removes the only ownership cue. Color never determines which shortcut fires.

## REPRODUCIBLE VALIDATION
Once runtime exists, capture light/night/forced-colors at baseline and 200% for eligible, non-owning, composing and stale states, twice per scenario. Compare visible and accessibility meaning; retain semantic distinctions when authored hue is overridden.

## OPEN
No rendered C089, forced-colors, independent-engine, calibrated-display, observer or human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Web must expose actual state/forced-colors evidence. Content must not use color references as command explanation. Layout keeps hint/action association under reflow. Type later checks key legends and mixed-script rendering without compensating for semantic ambiguity.