# W025 — Stage-Closure Runtime Transfer Plan

Evidence type: SYNTHESIS / TRANSFER VALIDATION / DEPENDENCY / OPEN

## RELATED DOMAIN CHECK
W024 closes the bounded six-state Chromium fixture gap. C027 requires focus/overlay adjacency evidence; L018 requires zoom/overlay/safe-area transfer; I013 defines interruption/recovery truth; CD031/CD029 require runtime string/resource evidence; T022 custom drawing remains excluded from product transfer.

## Why this replaces more Chromium micro-tests
Further deterministic local-state permutations have diminishing value. Stage 3 closure now depends on crossing environment boundaries that W024 does not test.

## Integrated transfer stack
### A. True-origin route/history/network
Serve the integrated surface from a real HTTP origin. Exercise direct route entry, back/forward history, reload, Fetch success, classified failure, delayed response, abort/timeout, offline transition, reconnect and conflict fixture supplied through an actual request boundary. Verify that I013 state classification—not transport event names—drives recovery.

### B. Browser transfer
Repeat the same core workflow in Chromium, Firefox and Safari/WebKit when executable. Compare native control behavior, focus traversal, sticky/overlay behavior, zoom/reflow and forced/high-contrast support where available. Browser absence is a blocker, not a PASS.

### C. Accessibility/runtime transfer
Execute keyboard traversal plus available screen-reader/AT inspection on the complete state surface. WCAG 2.2 remains baseline; SC 2.4.11 specifically makes authored focus occlusion an AA concern. Static DOM inspection is not AT evidence.

### D. Product/device transfer
Run on physical mobile/tablet and the actual PWA/app surface when available, including software keyboard and safe-area behavior. Simulation remains labelled simulation.

### E. Performance evidence boundary
Local/lab traces may diagnose implementation. They must not be labelled field LCP/INP/CLS. Field Core Web Vitals require field/RUM evidence with population/context recorded.

## Stage-closure evidence ledger
For each run store environment/version, route, viewport/zoom, input mode, state transition, expected/observed action, focus visibility, semantic status, overflow/reflow, network classification and evidence artifact. A single success does not generalize across browsers/devices.

## Current result
**W025 CLOSURE PLAN COMPLETE / ENVIRONMENT TRANSFER OPEN.** This is deliberately not another Chromium PASS.

## HANDOFFS TO OTHER SPECIALISTS
C027 receives adjacency/focus results; L018 receives geometry; I013 receives transport→state contradictions; Content receives actual runtime message/ARIA/resource findings; Type receives font loading/fallback evidence only after its relevant product-font track is ready; UX integration receives end-to-end workflow failures separately from human usability evidence.
