# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / W028 BACKEND CONTRACT VALIDATED — BROWSER CAPTURE OPEN**
Governance sync: 2026-09-16
Primary path: `research/web/`
Active studies: `W025`–`W028`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
W028 adds a controlled same-origin backend for W027 and an executed standard-library HTTP validation. `confirm`, `reject`, `drop-before` and `drop-after` were exercised by operation ID. Critically, both drop modes produced the same client-visible transport exception while reconciliation distinguished no recorded commit from confirmed commit. This is executable evidence for the I015 rule that transport failure alone is not authoritative operation failure.

W027 was also bound to these four modes and now reconciles the exact last operation ID. Browser DOM/focus/zoom/forced-colors/history capture has not yet been executed, so W026/C029/L020 browser evidence remains OPEN.

WCAG 2.2 remains the accessibility baseline. Lab diagnostics remain distinct from field LCP/INP/CLS; field labels require actual field/RUM population context.

## Active queue
1. Execute W027+W028 in an actual browser runtime and record coherent W026 capture IDs.
2. Capture route/history/network/recovery plus 200% zoom, narrow reflow, sticky-layer focus intersection and forced-colors where executable.
3. Transfer the identical workflow to Firefox/Safari/WebKit, AT and physical mobile when executable.
4. Bind CD034 resources and valid Type product-font evidence.
5. Preserve field-vs-lab performance evidence boundary.

## Cross-domain state
C029 owns focus/state visual audit; L020/I015 own geometry/recovery semantics; CD034 owns complete content contract; custom Type work remains behind T021.

## Evidence boundary
No Web Stage 3 PASS, browser runtime, cross-browser, screen-reader, physical-device, field Core Web Vitals or human UX PASS is claimed. W028 is backend-contract evidence only.