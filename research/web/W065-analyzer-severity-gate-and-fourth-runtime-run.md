# W065 — Analyzer Severity Gate and Fourth Runtime Run

Evidence class: **TRANSFER VALIDATION / EXECUTION REPAIR**

## SOURCE / OBSERVED EVIDENCE
MintTap Actions run `35249891233` on commit `27ad199...` successfully completed checkout, Flutter 3.47.4 setup, identity capture and dependency resolution. `flutter analyze` then emitted exactly three `info` lints (`use_null_aware_elements` twice, `unnecessary_underscores` once) and exited 1. Widget transfer, Web build and manifest were skipped; evidence upload succeeded.

## CRITIQUE
The previous gate treated info-level style diagnostics as equivalent to blocking analyzer errors. That made code-style hygiene mask the primary product-transfer experiment after the API-drift blocker had already been removed.

## PRACTICE / REPAIR
MintTap workflow commit `27b8f3938350ed83e1380511bc357d0929b7f171` changes the analyzer invocation to `flutter analyze --no-fatal-infos ...`. Analyzer diagnostics remain captured in `analyze.txt`; warnings/errors remain blocking. The push launched Actions run `35255971379`.

## STUDIO JUDGMENT
CI gates should be severity-aware and evidence-preserving. Diagnostic tooling must not prevent higher-value behavioral execution unless the diagnostic indicates a condition that invalidates that execution.

## RELATED DOMAIN CHECK
- Type: info lints are not typography defects; T021 gate order unchanged.
- Color: contradiction fixture requires actual rendering.
- Layout/Interaction: skipped runtime is NOT EXECUTED, not task failure.
- Content: synthetic semantic fixture and actual Dart locale pipeline remain distinct.
- UX: evidence state must preserve EXECUTED-PASS / EXECUTED-FAIL / NOT-EXECUTED / BLOCKED.

## HANDOFFS TO OTHER SPECIALISTS
All specialists should consume run `35255971379` under one identity when complete. If smoke executes, prioritize actual locale and pending/failure/ambiguous/recovery expansion.

## OPEN
Fourth run completion, widget matrix, Web build, browser engine execution, accessibility diagnostics, independent engine, physical device, field LCP/INP/CLS and human evidence remain open.