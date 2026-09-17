# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / L063 FAILURE LOCALIZATION + I059 MATERIAL OWNERSHIP**
Governance sync: 2026-09-18
Canonical paths: `research/layout/`, `research/interaction/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
Run 35255971379 still provides EXECUTED-FAIL evidence: 9.3 px baseline overflow, 47 px enlarged-text overflow and repeated ListTile/DecoratedBox Material assertions. New inspection shows the overflow log is collapsed at a shared `tester.takeException()` boundary, so the exact RenderFlex owner is still unproven. L063 now requires creator-chain/constraint/claimant instrumentation before repair. I059 localizes the Material failure to the ListTile→decorated surface→nearest Material ownership boundary without weakening tap/focus/pressed/selected behavior.

## Active queue
1. Capture exact overflowing RenderFlex creator chain, constraints and direct-child widths at baseline/enlarged text; treat the AppBar fixed claimant set as hypothesis until confirmed.
2. Correct affected ListTile Material ownership while preserving activation, target geometry and state feedback.
3. Rerun baseline, enlarged text, value/locale stress and 1024×768 traversal under one build identity.
4. After smoke is green, resume I058 pending→known-failure→correction/retry and ambiguous→verify/reconcile→safe-retry.
5. Keep AT, physical-device, discoverability, workload and representative-user evidence OPEN.

## Evidence boundary
No Stage 3 PASS, repaired runtime/native/browser transfer PASS, AT, physical-device or representative-human usability PASS is claimed.