# T034 — CI Analyzer Severity Transfer Boundary

Evidence class: **TRANSFER VALIDATION / CRITIQUE**

## Finding
MintTap run `35249891233` reached Flutter analysis after the unsupported semantics helper was removed. Analysis reported only three `info` lints and exited 1, so the typography matrix never executed. None of those diagnostics establishes a glyph, metrics, spacing, kerning, fallback, wrapping, clipping, or raster defect.

## STUDIO JUDGMENT
Analyzer severity is an execution-gate concern, not Type evidence. Info-only style diagnostics may be preserved while allowing the behavioral matrix to run; warnings/errors remain blocking. T021 drawing → spacing → residual kerning order is unchanged.

## RELATED DOMAIN CHECK
- Color: contradiction fixture remained NOT EXECUTED.
- Layout/Interaction: reflow/workflow fixtures remained NOT EXECUTED.
- Web: W065 owns execution-gate correction.
- Content: semantic fixture remained NOT EXECUTED.

## HANDOFFS TO OTHER SPECIALISTS
Web should preserve analyzer output while preventing info-only lints from masking primary transfer evidence. Layout and Content should treat skipped scenarios as NOT EXECUTED, never PASS/FAIL.

## OPEN
Runtime typography evidence remains open until the repaired matrix executes. Native/browser breadth, AT and human recognition remain open.