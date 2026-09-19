# W101 — Served import: file, parser, duplicate and transaction provenance

Date: 2026-09-19
State: STAGE 3 PRACTICE — CLOSURE MANIFEST; production runtime evidence OPEN

## RELATED DOMAIN CHECK
Transfers I088/L092/C101/CD107/T070 into real PWA/browser validation. This deliberately avoids another isolated Chromium micro-test; value lies in served product provenance and independent-engine transfer.

## SOURCE
The Web File API exposes File objects after explicit user selection or drag/drop; FileReader reads selected File/Blob data asynchronously. Browser acquisition/read success does not establish parser, duplicate, transaction or persistence success. WCAG 2.2 SC 4.1.3 applies to qualifying status messages that report progress/results/errors without changing context.

## CLOSURE LADDER
`LogMate implementation → production Web build → served primary engine → independent engine → 200% → forced-colors → physical mobile/iPad transfer`.

Use identical fixture/scenario IDs and REPLICATION x2 where executable. Do not promote local static or synthetic harness results to product PASS.

## PROVENANCE MANIFEST
Capture build/route/browser/device; file-input vs drag/drop acquisition; File metadata; fixture hash; read start/result/error; parser/source-system/version; normalized record IDs; duplicate-rule/version; row classification/resolution; preview hash/counts; batch transaction/inverse IDs; projection hash; semantic focus; visible/a11y status payload; L092 rectangles/scroll offsets; persistence/sync truth.

Scenarios: valid mixed fixture; malformed file; unsupported source; exact/possible duplicates; correction/exclusion; cancel before commit; commit; Undo success/failure; repeated same-file import; Back/Forward/reload before/after commit; 200%; forced colors; independent engine.

## PERFORMANCE EVIDENCE
Import parsing duration and responsiveness may be measured in LAB, but Lighthouse/DevTools/CI and local timing remain LAB. LCP/INP/CLS are FIELD only when provenance-bearing representative RUM/aggregate evidence exists. Import-specific long-task/interaction measurements must not be mislabeled as field INP without field provenance.

## FAILURE CONDITIONS
FAIL if file-read success is conflated with import success; browser-specific picker behavior is generalized without transfer; row/batch visible and accessibility results diverge; focus is moved only to announce routine status; preview/commit hashes disagree unexplained; or persistence is claimed from local transaction completion.

## OPEN
Actual LogMate importer, real source fixtures, independent engine, physical iPad/mobile picker behavior, screen-reader evidence, persistence/offline/sync, field Core Web Vitals and human UX remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Return browser/file-picker limitations to Interaction; geometry to Layout; computed state failures to Color; payload/announcement failures to Content; reproduced font/fallback failures to Type.
