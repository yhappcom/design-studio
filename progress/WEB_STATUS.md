# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / W066 FIRST EXECUTED MINTTAP RUNTIME FAILURES**
Governance sync: 2026-09-18
Primary path: `research/web/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
Run `35255971379` on MintTap commit `27b8f3938350ed83e1380511bc357d0929b7f171` passed severity-aware analysis and executed the widget matrix for the first time. Baseline 390×844 overflowed 9.3 px right; 2.0-scale stress overflowed 47 px right; 1024×768 workflow produced repeated ListTile/DecoratedBox assertions that Material ink/background feedback may be invisible. Web build/manifest were skipped after widget failure; artifact upload succeeded. W066 classifies these as genuine runtime transfer failures.

## Active queue
1. Support compact recomposition and Material-layer repair, then rerun the same three scenarios.
2. Preserve analyzer diagnostics without allowing info-only lints to mask behavioral execution.
3. Once widget smoke passes, execute Web build and then actual browser runtime; require an independent engine before cross-browser claims.
4. Add actual product localization and pending/failure/ambiguous/recovery states after minimum smoke.
5. Treat Lighthouse/local traces as LAB; only provenance-bearing CrUX/RUM/equivalent counts as field LCP/INP/CLS.

## Evidence boundary
No widget runtime PASS, product browser PASS, cross-browser/Safari, screen-reader, physical-device, field Core Web Vitals or human UX PASS is claimed.
