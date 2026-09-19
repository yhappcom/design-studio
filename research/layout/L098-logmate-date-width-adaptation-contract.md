# L098 — LogMate Date Width Adaptation Contract

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION — no gate promotion**

## PURPOSE
Resolve H3 as a spatial contract rather than a fixed-column or typography-compression problem.

## RELATED DOMAIN CHECK
T076, C107, I094, W107 and CD113 checked. L097 large-text modes are reused rather than duplicated.

## PRACTICE
For Home, View Logbook, Activity and Add Flight, test the same canonical date through the actual product representation plus bounded stress representations. Record date-zone width, adjacent Flight/DEP/ARR/duration geometry, wrap, row height, focus rectangle, sticky overlap and disclosure path.

Preferred adaptation order: intrinsic room within semantic zone → redistribute local columns → allow row growth/wrap where semantics permit → disclosure/detail transfer → recoverable truncation only when full date remains available. Do not globally freeze x-coordinates across surfaces.

## CRITIQUE
A fixed width derived from one `MM/DD/YYYY`-like specimen is fragile. Conversely, making every ledger date fully fluid can destroy SC-A comparison calibration. The contract therefore protects the comparison relationship, not one string width.

## SYNTHESIS
H3 is satisfied only when allowed date representations vary without displacing or obscuring higher-priority operational comparisons/actions beyond the surface contract.

## OPEN
Exact production date policy; real View Logbook/Home/Activity implementations; actual font/browser widths; representative-pilot comparison needs.

## HANDOFFS TO OTHER SPECIALISTS
- Type: provide real mature-font widths; no metric rescue.
- Content: enumerate only product-permitted representations.
- Web: execute geometry in served primary + independent engines.
- Interaction: preserve focus/edit/recovery identity through recomposition.