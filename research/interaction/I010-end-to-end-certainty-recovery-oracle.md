# I010 — End-to-end certainty and recovery oracle

Classification: **SYSTEMS PRACTICE + TRANSFER VALIDATION DESIGN**

## Purpose
Turn I009 lifecycle semantics into an end-to-end UX/runtime oracle spanning interruption, responsive changes, localization and recovery.

## RELATED DOMAIN CHECK
L015 owns spatial preservation. C024 reinforces state but cannot define it. W021 integrates runtime. CD027/CD028 binds semantic revision/release. T022 rendering must not alter state meaning.

## State truth
Keep distinct: pending, confirmed, known failure, outcome unknown, offline/stale, conflict. A presentation change cannot mutate these states.

## Recovery tuple
A recovery surface is sufficient only when it restores or exposes:
`object identity + interrupted task + certainty + safe authorized action`.
Navigation back to a screen is not sufficient by itself.

## Transition oracle
Across viewport, theme, locale, zoom, reduced-motion, reload simulation and interruption:
- certainty cannot improve without new authoritative evidence;
- outcome unknown cannot expose blind retry merely because space is constrained;
- offline/stale cannot be presented as confirmed-current;
- known failure may offer retry only when Interaction truth authorizes it;
- conflict requires an explicit resolution path or bounded block, not silent last-write presentation;
- pending feedback must remain perceivable without motion dependency.

## UX integration risks
High-risk contradictions are semantic compression at narrow widths, generic error wording that erases certainty, hidden recovery behind navigation, and visual success styling before authoritative confirmation.

## Evidence boundary
These are deterministic expert assertions. They do not prove user comprehension, trust, workload or successful recovery.

## HANDOFFS TO OTHER SPECIALISTS
Web binds assertions to W021 state fixtures; Content binds stable semantic IDs; Layout preserves recovery tuple spatially; Color reinforces states without hue dependence; Type preserves literal identifiers.

## Gate result
**END-TO-END INTERACTION ORACLE READY; RUNTIME/BACKEND/HUMAN EVIDENCE OPEN.**