# W037 — Multi-action race runtime closure contract

Date: 2026-09-16
Purpose: **STAGE 3 PRODUCT-LIKE TRANSFER / EXECUTION CONTRACT**

## RELATED DOMAIN CHECK
I024 defines temporal/action invariants; L028 geometry/focus locality; C037 cue precedence; CD043 resource semantics; Type remains mature-fallback-only until T021 drawing/general spacing.

## Why W037
W036 proves action-specific authority can be recorded. W037 adds a harder product-like condition: multiple actions whose availability changes while requests, optimistic presentation, late responses and authoritative revisions race.

## Required scenario
Execute at least one deterministic sequence:
`rev1 → A enabled → dispatch A → optimistic UI → rev2/conflict → B reevaluated → late A response → reconciliation → stable retrieval`.

For every transition preserve run ID, engine/version/platform, commit SHA, object/operation IDs, presented revision, authoritative revision, required-fact revisions, action enabled/blocked state, semantic resource ID/revision/locale, focus target, relevant rectangles, computed visual state and raw network event ordering.

## Closure assertions
- Browser presentation never upgrades authority by itself.
- Enabled state matches I024/I023 oracle at dispatch.
- Late network completion cannot silently replace newer authority.
- Focus/reflow remains safe when controls change availability.
- C037 dominant styling does not contradict blocked/unknown/conflict state.
- CD043 wording changes with certainty without inventing backend guarantees.

## Accessibility/performance boundary
Use WCAG 2.2 as baseline. Actual 200% zoom and focus-obscuration require executed browser evidence. Functional/lab timing is diagnostic only; field LCP/INP/CLS require real field/RUM population context.

## Execution status
**CONTRACT READY / EXECUTION OPEN.** No multi-engine browser artifact is fabricated. Chromium plus an independent engine is required before cross-browser claims; Safari claims require Safari execution.

## UX integration
This fixture supports deterministic evaluation of workflow consistency under concurrency. It does not establish discoverability, cognitive load, trust, perceived salience or professional task performance; those remain human evidence.