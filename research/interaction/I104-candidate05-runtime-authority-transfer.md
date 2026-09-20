# I104 — Candidate 05 runtime authority transfer

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION / RUNTIME OPEN**

## Question
Can Candidate 05 move from visual-only owner review to real interaction without inventing behavior from its pills, search shell, bands or selected styling?

## RELATED DOMAIN CHECK
T086, C117, L108, W116/CD122 and Candidate 05 coordinator evidence checked. Candidate 05 freezes IA/order/data/action placement but explicitly leaves runtime open.

## Authority model
`visible affordance ≠ available action ≠ requested transition ≠ pending state ≠ authoritative result ≠ persisted projection ≠ restored route/state`.

The following first runtime fixtures are permitted without expanding product semantics:
1. month previous/next → projection update → Back/restore where routing/history applies;
2. Recent Flight row → record → Back with context restoration;
3. Add Flight → destination entry → return;
4. View Logbook → destination entry → return;
5. Activity period selection → selected state → updated projection.

Search remains a shell until SEARCH-001 behavior is actually wired. A rounded search-looking control is not evidence of query submission, search-on-type, results, empty/error behavior or history restoration.

## PRACTICE / reproducible checks
For each fixture capture stable object/destination IDs, action source, focus before/after, route/history representation, selected/current state, projection identity and return state. Repeat after max text scaling and narrow/SafeArea recomposition to detect action-owner separation.

## CRITIQUE / failure conditions
- FAIL if visual selected styling is treated as committed state without authority.
- FAIL if Back returns to a visually similar but semantically reset projection.
- FAIL if reflow separates a control from the object/state it owns.
- FAIL if Search behavior is inferred from appearance.
- FAIL if a status string or Color token defines system state instead of reflecting it.

## Human boundary
Discoverability, softness/familiarity, workload, trust and pilot task performance remain OPEN for human validation; static expert review does not close them.

## HANDOFFS TO OTHER SPECIALISTS
L108 preserves object/action geometry; C117 encodes only these authorized states; CD123 names only implemented states/actions; W117 should capture all five fixtures from the exact build.