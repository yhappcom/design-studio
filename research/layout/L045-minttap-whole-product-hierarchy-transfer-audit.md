# L045 — MintTap whole-product hierarchy transfer audit

Evidence purpose: **TRANSFER VALIDATION / UX INTEGRATION**

## RELATED DOMAIN CHECK
Type T022; Color C054; Interaction I040; Web W053; Content CD059.

## Transfer finding
MintTap's source surface includes very large Home, stock-detail, transaction/edit and settings screens. The product-level problem is therefore not a single-card composition problem: information hierarchy, navigation depth, repeated financial controls, state ownership and responsive density must be solved as a system.

A decision-first portfolio sequence is a defensible working hierarchy: context/display state → portfolio value → total performance → income/recovery → holdings → distribution trend → ROC/tax. It explicitly prevents distribution magnitude from becoming a proxy for investment success.

## STUDIO JUDGMENT
Whole-product redesign should precede owner review. Internal iterations may validate components, but human review should be requested at coherent workflow/system gates rather than every micro-change. Preserve existing domain depth through progressive disclosure rather than deleting it.

## UX integration checks
Review end-to-end: onboarding/auth → portfolio context → holding detail → transaction → distribution/ROC/tax → settings. For each: discoverability, current state, primary action, consequence, recovery, back/history, empty/loading/error, 200% text, narrow/wide recomposition.

## OPEN
No human usability evidence; no physical-device/native execution; no claim that the proposed hierarchy is preferred by users.

## HANDOFFS
Type validates financial strings; Color prevents income/outcome semantic conflict; Content owns terminology; Web/native execution validates responsive/focus/runtime behavior.