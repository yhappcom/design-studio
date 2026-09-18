# C079 — Recovery Lifetime & Supersession State Integrity

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION** of C077–C078 under I066 repeated transactions.

## RELATED DOMAIN CHECK
I066 defines active/superseded/invalidated recovery truth. L070 defines recovery-surface geometry. CD085 verbalizes those states. W078 supplies runtime evidence. T047 prevents Type compression from masking state-density problems.

## State axes
Keep independent: field visibility; focus; selection/insertion; move-boundary enabledness; transaction result; Undo availability; Undo supersession/expiry/invalidation; future persistence state.

Contradiction fixtures include:
- focused + moved + Undo available;
- focused + second move + previous Undo superseded;
- boundary-disabled + no new transaction;
- Reset + prior recovery invalidated;
- future only: locally moved + persistence failure/ambiguous.

## Acceptance
`semantic state → token → paint owner → visible surface → non-color cue → accessible meaning` must survive every fixture. Opacity or hue alone cannot distinguish unavailable, failed, superseded or hidden. Recovery state must not erase focus visibility or field visibility semantics. Test light/night/forced-colors and independent engine when implementation exists.

## CRITIQUE
Success-colored transient feedback can falsely imply persistence and can visually dominate focus. A muted expired state can become indistinguishable from disabled/hidden. State orthogonality is therefore more important than adding another status color.

## OPEN
No rendered C079, forced-colors, cross-browser, device, observer or human PASS.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives visual-state collision risks; Content receives the requirement for non-color semantic distinctions; Layout receives layer/overlap constraints; Web receives forced-colors/runtime assertions.
