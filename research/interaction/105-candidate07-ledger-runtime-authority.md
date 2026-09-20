# I105 — Candidate 07 Ledger Runtime Authority

Date: 2026-09-20
State: **TRANSFER VALIDATION / STAGE 3 PRACTICE — NOT PASS**

## PURPOSE
Transfer the established LogMate action/state authority into Candidate 07 without mistaking static controls for implemented behavior.

## RELATED DOMAIN CHECK
T087 prevents fit-driven wording/type distortion; C118 separates semantic states; L109 protects owner/action relationships; W118 owns runtime provenance; CD124 preserves visible/accessibility semantics.

## PROJECT EVIDENCE
Candidate 07 static review records 44px action/search/month/period targets, Material vector icons in Flutter source and Activity selection through underline thickness plus weight/color. Runtime focus, route and AT remain OPEN. The render-harness missing-font search glyph was explicitly not source UI evidence.

## AUTHORITY CONTRACT
Keep distinct:
`visible control ≠ enabled action ≠ requested transition ≠ route/state mutation ≠ authoritative result ≠ restored state`.

First executable fixtures:
1. month previous/next → period projection → Back/restore where applicable;
2. Recent flight row → record → Back → prior Home context;
3. Add Flight → return/cancel/commit only when actual route/state exists;
4. View Logbook → return;
5. Activity range selection → projection update;
6. Search remains a shell until SEARCH-001 behavior exists.

## CRITIQUE / FAILURE CONDITIONS
FAIL if a static underline is treated as committed selection without state authority; if a 44px visual box has a smaller hit region; if Back reconstructs rather than restores the intended context; if icon semantics differ from action; or if Search behavior is invented from appearance.

## REPRODUCIBLE VALIDATION
Record exact source/build, platform, input modality, control semantic ID, focus before/after, requested action, resulting route/state, restored state and failure/recovery path. Run the same primary build twice before second-platform transfer.

## HUMAN EVIDENCE BOUNDARY
Discoverability, workload, trust, preference and pilot task performance remain OPEN; static or automated evidence cannot satisfy them.

## HANDOFFS TO OTHER SPECIALISTS
Web should use these fixtures as runtime provenance cases. Content must bind labels/names to actual actions. Layout must preserve control-owner and selection-projection relationships under reflow.