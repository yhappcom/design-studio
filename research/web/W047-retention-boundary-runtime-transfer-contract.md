# W047 Retention Boundary Runtime Transfer Contract

Evidence mode: STAGE 3 SYSTEMS PRACTICE / PRODUCT TRANSFER TARGET.

## Goal
Execute the destructive-concurrency chain across a real retention/recoverability boundary rather than stopping at delete/restore uncertainty.

## RELATED DOMAIN CHECK
C047 supplies visual-truth assertions. I034 supplies the recoverability/action oracle. L038 supplies spatial continuity. CD053 supplies semantic resources. T021 custom font remains provisional; mature fallback must be used for closure evidence.

## Runtime chain
1. Load authoritative live r1.
2. Confirm deletion under retention policy p1 and record deletionEventId.
3. Confirm recovery capability and authoritative boundary when the backend provides one.
4. Suspend/offline the client across the displayed boundary.
5. Resume with local time beyond the boundary; do not infer irreversibility.
6. Recheck authority and capture recoverable-confirmed, unavailable-confirmed or authority-unavailable.
7. Attempt only the action allowed by I034; include response-loss/duplicate-request variant when recovery is allowed.
8. Reload, deep-link to history, and export/static-inspect the chain.
9. Recheck current authority from the static artifact path when supported.

## Provenance
One run must bind runId, objectId, deletionEventId, recoveryOperationId when any, authorityRevision, retentionPolicyRevision, authoritative boundary value/source, client clock/timezone, locale/resource revision, browser/engine/version, commit SHA, network ordering, semantic resource IDs, computed visual state, focus, geometry and artifact hashes.

## Browser closure
Chromium plus an independent engine are required before cross-browser claims. Safari claims require Safari. Forced colors/reflow/200% text/localization/export are transfer stresses, not substitutes for engine diversity.

## Performance boundary
Runtime/network timings here are lab/functional diagnostics. LCP/INP/CLS are field evidence only with an actual field/RUM population and appropriate attribution/context.

## Product dependency
If production retention, identity continuity, idempotency or recovery policy is unavailable, exercise authority-unavailable safe blocking and record the dependency. Do not invent policy.

## Evidence boundary
No W047 execution, cross-browser, screen-reader, physical-device, field Core Web Vitals or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Return actual cue survival to C047, geometry/focus to L038, state/action discrepancies to I034, and resource/fallback findings to CD053.