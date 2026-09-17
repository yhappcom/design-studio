# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / W061 CI EXECUTION BRIDGE DEFINED / FIRST RUN OPEN**
Governance sync: 2026-09-17
Primary path: `research/web/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
W061 resolves an over-broad blocker statement: direct Flutter/browser execution is unavailable in the current chat runtime, but GitHub Actions is an available execution substrate already used by Design Studio. MintTap `design-lab/minttap-1.0.29` is Flutter 1.0.29+29 with Dart `^3.10.7`, has no branch-local `.github` workflow, and therefore lacks the product-specific CI harness rather than lacking all executable infrastructure. The preferred next step is a MintTap-repository workflow that runs the isolated whole-app lab, uploads exact identity/raw artifacts, then expands to production smoke.

## Active queue
1. Implement and run the MintTap design-lab CI workflow/harness defined by W061.
2. Bind T030/C061/L052/I048/CD067 to one manifest identity including actual text scaler, entrypoint, locale/currency, scenario flags and fixture/network state.
3. Compare current compact-iOS clamp with unclamped diagnostic behavior; capture screenshots, semantics/accessibility evidence, focus/history trace and logs.
4. Require Chromium plus an independent engine before cross-browser claims; Safari/WebKit separately where product scope requires it.
5. Treat Lighthouse/local traces as LAB; only provenance-bearing CrUX/RUM/equivalent counts as field LCP/INP/CLS.
6. Do not add adjacent Web theory before the first artifact-bearing W061 run unless execution reveals a new unknown.

## Evidence boundary
No W061 runtime PASS, product browser PASS, cross-browser/Safari, screen-reader, physical-device, field Core Web Vitals or human UX PASS is claimed.