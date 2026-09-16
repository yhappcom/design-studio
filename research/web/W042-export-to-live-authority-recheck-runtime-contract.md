# W042 — Export-to-Live Authority Recheck Runtime Contract

Evidence purpose: **STAGE 3 PRACTICE / PRODUCT-TRANSFER CLOSURE TARGET** extending W041 rather than adding another isolated Chromium micro-test.

## RELATED DOMAIN CHECK
Type T021 remains behind repair/rerender/general spacing. C042 defines static cue-loss acceptance. I029 defines recheck behavior. L033 defines static-to-live spatial continuity. CD047 supplies snapshot semantics; CD048 should supply recheck semantics.

## Runtime scenario
Execute one durable chain end-to-end:
1. reconstruct audited object/history;
2. generate print/PDF snapshot at authoritative revision r1;
3. persist artifact hash + generation/authority timestamps + event IDs;
4. change authority to r2;
5. open the static artifact and invoke its recheck path;
6. resolve the same live object;
7. present `changedSinceSnapshot` before consequential actions;
8. return to history and verify immutable r1 event facts plus current r2 truth.

Negative branches: offline/timeout, permission loss, object archived/deleted, broken deep link, locale change, missing history, authority changing during recheck.

## Required provenance
`runId`, commit SHA, browser/engine/version, route, network ordering, `artifactId` + hash, `objectId`, event/operation IDs, snapshot generation time, authority-confirmed time, presented/authoritative revisions, locale/resource revision, media mode, viewport/zoom, computed visual state, focus, bounding boxes and page geometry.

## Acceptance
Route restoration alone is insufficient. PASS requires identity continuity, snapshot/current semantic separation, action gating against current authority, C042 cue-loss survival, L033 locality, I029 outcome correctness and Content resource identity. Chromium plus an independent engine is required before cross-browser claims; Safari requires Safari execution.

## Performance boundary
Export duration and recheck latency are functional/lab diagnostics. They are not field LCP/INP/CLS. Field Core Web Vitals require actual field/RUM population evidence and remain separately labeled.

## OPEN
This run lacks an authorized browser-capable execution environment, so no W042 runtime artifact or Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
C042, I029/L033 and CD048 should consume the same W042 IDs/artifacts. Type remains mature fallback until its drawing/general-spacing gates pass.