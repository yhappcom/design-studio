# W058 — Execution blocker protocol and artifact contract

Status: STAGE 3 PRACTICE / EXECUTION BLOCKED IN CURRENT CONNECTOR RUNTIME

## PURPOSE
W057 correctly froze adjacent theory expansion. This run cannot execute Flutter/browser binaries through the available GitHub connector. W058 therefore does not claim runtime validation; it formalizes the minimum handoff that converts the current blocker into an executable CI/product job rather than another browser micro-study.

## RELATED DOMAIN CHECK
T027, C058, L049, I045 and CD064 define domain-specific oracles. W057 remains the runtime identity authority. No separate UX owner exists.

## BLOCKER
Current environment can read/write repository text and inspect GitHub metadata but has no checked-out product runtime, Flutter SDK/browser process, or workflow-dispatch capability exposed here. Therefore screenshots, semantics tree, focus trace, runtime logs and task results cannot be honestly generated in this run.

## REQUIRED EXECUTION PACKAGE
One run manifest must bind:
- product repository + commit SHA;
- build command/build ID;
- scenario ID + fixture/data hash;
- browser engine/version or native platform/device;
- viewport/device-pixel ratio;
- locale/currency;
- text scale or browser zoom;
- theme + forced/high-contrast condition;
- network/offline condition;
- screenshot path;
- semantics/accessibility-tree path;
- focus/history trace path;
- console/runtime log path;
- automated accessibility result path;
- task-state result;
- T027/C058/L049/I045/CD064 oracle results.

## MINIMUM MATRIX
Do not claim cross-browser from Chromium alone. Minimum product-transfer closure requires Chromium plus one independent engine; Safari/WebKit remains separately relevant where product scope requires it. Scenarios must include signed/zero/large KRW/USD values, long localization, maximum supported text/zoom, high-income + negative-return contradiction, estimated/final ROC, partial/unavailable data, error/retry/recovery, navigation/history/deep-link and export/history semantics.

## PERFORMANCE BOUNDARY
Lab traces/Lighthouse are lab evidence only. LCP/INP/CLS become field evidence only when sourced from an actual field dataset such as CrUX/RUM with provenance and sampling context.

## WCAG BASELINE
Use WCAG 2.2 as the current W3C baseline. Automated checks are necessary but not sufficient for conformance or human usability.

## STOP RULE
Until this package can execute, Web should not add adjacent Chromium micro-tests merely to increase evidence volume. Work should instead improve the executable product/CI handoff or analyze actual returned artifacts.

## HANDOFFS
All specialists should consume the same manifest identity. A domain PASS cannot be promoted from a different build/scenario than the integrated result.